import { describe, expect, it } from 'vitest';

import { evaluateRequiredChecks } from '../src/github/checks.js';
import type {
  CheckTruth,
  DeliveryEnvelope,
  GitHubReadClient,
  GitHubTruthSnapshot,
  LiveRulesetRequiredChecks,
  PullRequestTruth,
  ShadowReadRequest,
  ShadowTarget,
  WorkflowTruth,
} from '../src/github/model.js';
import {
  classifyDeliveryAgainstTruth,
  reconcileShadowTruth,
} from '../src/github/reconciliation.js';
import {
  collectAuthoritativeGitHubTruth,
  runBoundedReadOnlyShadowWindow,
  runReadOnlyShadow,
  type ShadowClock,
} from '../src/github/shadow.js';
import { ShadowJournal } from '../src/storage/shadow-journal.js';

const candidateSha = 'candidate-123';
const baseSha = 'base-456';
const observedAt = '2026-09-28T17:45:00Z';

function successfulCheck(
  name = 'Implementation Verification',
  headSha = candidateSha,
  id = 1,
): CheckTruth {
  return {
    id,
    name,
    headSha,
    status: 'completed',
    conclusion: 'success',
    startedAt: '2026-09-28T17:40:00Z',
    completedAt: '2026-09-28T17:44:00Z',
  };
}

function truth(overrides: Partial<GitHubTruthSnapshot> = {}): GitHubTruthSnapshot {
  return {
    repositoryId: 1275654940,
    repositoryFullName: 'SethDKelly/Mudac',
    observedAt,
    pullRequest: {
      number: 23,
      state: 'open',
      merged: false,
      draft: true,
      headSha: candidateSha,
      baseRef: 'aut-001/b-start-gate',
      baseSha,
      mergeCommitSha: null,
    },
    baseRef: { ref: 'aut-001/b-start-gate', sha: baseSha },
    checks: [successfulCheck()],
    workflows: [],
    mergeCommitInBase: false,
    ...overrides,
  };
}

function target(overrides: Partial<ShadowTarget> = {}): ShadowTarget {
  return {
    candidateSha,
    expectedBaseSha: baseSha,
    requiredCheckNames: ['Implementation Verification'],
    initialLifecycleState: 'AWAITING_PR_CI',
    lifecycleFacts: [],
    expectedLifecycleState: 'AWAITING_G5',
    expectedNextActions: ['gate.g5.pass', 'failure.changes_required_within_existing_g2'],
    ...overrides,
  };
}

function observationTarget(): ShadowTarget {
  return {
    candidateSha,
    expectedBaseSha: baseSha,
    requiredCheckNames: ['Implementation Verification'],
    initialLifecycleState: 'AWAITING_PR_CI',
    lifecycleFacts: [],
  };
}

function delivery(overrides: Partial<DeliveryEnvelope> = {}): DeliveryEnvelope {
  return {
    deliveryId: 'delivery-1',
    sourceIdentity: 'hook-1',
    sourceType: 'WEBHOOK',
    repositoryId: 1275654940,
    repositoryFullName: 'SethDKelly/Mudac',
    eventFamily: 'pull_request',
    action: 'synchronize',
    receivedAt: observedAt,
    signatureVerified: true,
    payloadDigest: 'digest-a',
    pullRequestNumber: 23,
    payloadHeadSha: candidateSha,
    payloadBaseSha: baseSha,
    ...overrides,
  };
}

class FakeReadClient implements GitHubReadClient {
  readonly calls: string[] = [];
  pr: PullRequestTruth = truth().pullRequest;
  ref = truth().baseRef;
  checks: readonly CheckTruth[] = truth().checks;
  workflows: readonly WorkflowTruth[] = [];
  ruleset: LiveRulesetRequiredChecks = {
    rulesetId: 1,
    rulesetName: 'main — protected',
    enforcement: 'active',
    target: 'branch',
    requiredContexts: ['Implementation Verification'],
    refNameCondition: {
      include: ['~DEFAULT_BRANCH'],
      exclude: [],
    },
  };
  ancestor: boolean | 'UNKNOWN' = false;
  failOn?: string;
  checkSequence: Array<readonly CheckTruth[]> = [];

  async readPullRequest(): Promise<PullRequestTruth> {
    this.calls.push('readPullRequest');
    if (this.failOn === 'readPullRequest') throw new Error('read_pr_failed');
    return structuredClone(this.pr);
  }

  async readRef(): Promise<{ ref: string; sha: string }> {
    this.calls.push('readRef');
    if (this.failOn === 'readRef') throw new Error('read_ref_failed');
    return structuredClone(this.ref);
  }

  async readChecks(): Promise<readonly CheckTruth[]> {
    this.calls.push('readChecks');
    if (this.failOn === 'readChecks') throw new Error('read_checks_failed');
    if (this.checkSequence.length > 0) {
      const next = this.checkSequence.shift();
      return structuredClone(next ?? []);
    }
    return structuredClone(this.checks);
  }

  async readWorkflows(): Promise<readonly WorkflowTruth[]> {
    this.calls.push('readWorkflows');
    if (this.failOn === 'readWorkflows') throw new Error('read_workflows_failed');
    return structuredClone(this.workflows);
  }

  async readRulesetRequiredChecks(): Promise<LiveRulesetRequiredChecks> {
    this.calls.push('readRulesetRequiredChecks');
    if (this.failOn === 'readRulesetRequiredChecks') throw new Error('ruleset_failed');
    return structuredClone(this.ruleset);
  }

  async isAncestor(): Promise<boolean | 'UNKNOWN'> {
    this.calls.push('isAncestor');
    if (this.failOn === 'isAncestor') throw new Error('ancestry_failed');
    return this.ancestor;
  }
}

class FakeClock implements ShadowClock {
  #ms: number;
  readonly sleeps: number[] = [];

  constructor(startIso: string) {
    this.#ms = Date.parse(startIso);
  }

  now(): Date {
    return new Date(this.#ms);
  }

  async sleep(ms: number): Promise<void> {
    this.sleeps.push(ms);
    this.#ms += ms;
  }

  advance(ms: number): void {
    this.#ms += ms;
  }
}

const request: ShadowReadRequest = {
  repositoryId: 1275654940,
  repositoryFullName: 'SethDKelly/Mudac',
  pullRequestNumber: 23,
  baseRef: 'aut-001/b-start-gate',
  observedAt,
};

const agreedAuthority = {
  status: 'AGREED' as const,
  requiredContexts: ['Implementation Verification'],
  packageAuthority: {
    packageContractPath: 'docs/routing/aut001_implementation_package_contract.json',
    packageSchema: 'mudac.aut001-implementation-package/v1',
    rulesetName: 'main — protected',
    rulesetEnforcement: 'active',
    packageRequiredContexts: ['Implementation Verification'],
    expectedRefNameCondition: {
      include: ['~DEFAULT_BRANCH'],
      exclude: [] as string[],
    },
    stageAuthorityDeltaPath: 'docs/routing/aut001_b_stage_authority_material_delta.json',
  },
  liveRuleset: {
    rulesetId: 1,
    rulesetName: 'main — protected',
    enforcement: 'active' as const,
    target: 'branch' as const,
    requiredContexts: ['Implementation Verification'],
    refNameCondition: {
      include: ['~DEFAULT_BRANCH'],
      exclude: [] as string[],
    },
  },
};

describe('AUT-001-B delivery journal', () => {
  it('treats identical redelivery as idempotent by delivery identity plus payload digest', () => {
    const journal = new ShadowJournal();
    expect(journal.appendDelivery(delivery(), 'attempt-1').status).toBe('ACCEPTED');
    expect(
      journal.appendDelivery(
        delivery({ receivedAt: '2026-09-28T17:46:00Z', redelivery: true }),
        'attempt-2',
      ).status,
    ).toBe('IDEMPOTENT_NOOP');
    expect(journal.snapshot().deliveries).toHaveLength(1);
    expect(journal.snapshot().processingAttempts).toHaveLength(2);
  });

  it('fails closed when the same delivery key carries a conflicting payload digest', () => {
    const journal = new ShadowJournal();
    journal.appendDelivery(delivery(), 'attempt-1');
    const result = journal.appendDelivery(delivery({ payloadDigest: 'digest-b' }), 'attempt-2');
    expect(result.status).toBe('CONFLICT');
    expect(journal.snapshot().deliveries).toHaveLength(1);
  });

  it('rejects unverified webhook delivery without retaining it as accepted truth', () => {
    const journal = new ShadowJournal();
    const result = journal.appendDelivery(delivery({ signatureVerified: false }), 'attempt-1');
    expect(result.status).toBe('REJECTED_SIGNATURE');
    expect(journal.snapshot().deliveries).toHaveLength(0);
  });

  it('classifies unknown event families as RECORD_NO_ADVANCE', () => {
    const item = delivery({ eventFamily: 'unknown', action: 'future_action' });
    expect(classifyDeliveryAgainstTruth(item, truth())).toBe('RECORD_NO_ADVANCE');
  });

  it('classifies known family with unknown action as RECORD_NO_ADVANCE', () => {
    const item = delivery({ eventFamily: 'pull_request', action: 'labeled' });
    expect(classifyDeliveryAgainstTruth(item, truth())).toBe('RECORD_NO_ADVANCE');
  });

  it('classifies accepted pull_request action as CURRENT_NOTIFICATION', () => {
    expect(classifyDeliveryAgainstTruth(delivery({ action: 'opened' }), truth())).toBe(
      'CURRENT_NOTIFICATION',
    );
  });

  it('classifies a late known action for a superseded head as historical only', () => {
    const item = delivery({ action: 'synchronize', payloadHeadSha: 'old-head' });
    expect(classifyDeliveryAgainstTruth(item, truth())).toBe('HISTORICAL_NO_ADVANCE');
  });
});

describe('AUT-001-B required-check reconciliation', () => {
  it('allows exact-head terminal success to derive only the non-human CI transition', () => {
    const result = reconcileShadowTruth('obs-1', target(), truth());
    expect(result.requiredChecks.disposition).toBe('PASS');
    expect(result.derivedLifecycleFact?.payload.eventType).toBe('github.check.required_set_pass');
    expect(result.projectionAfterReconciliation.state).toBe('AWAITING_G5');
    expect(result.blocking).toBe(false);
  });

  it('does not allow a successful check for a superseded candidate to satisfy current CI', () => {
    const result = reconcileShadowTruth(
      'obs-2',
      target(),
      truth({ checks: [successfulCheck('Implementation Verification', 'old-head')] }),
    );
    expect(result.requiredChecks.disposition).toBe('NOT_READY');
    expect(result.derivedLifecycleFact).toBeUndefined();
    expect(result.projectionAfterReconciliation.state).toBe('AWAITING_PR_CI');
  });

  it('fails inconclusive on conflicting newest timestamps for the same required context', () => {
    const evaluation = evaluateRequiredChecks(
      [
        successfulCheck('Implementation Verification', candidateSha, 1),
        {
          ...successfulCheck('Implementation Verification', candidateSha, 2),
          conclusion: 'failure',
          completedAt: '2026-09-28T17:44:00Z',
        },
      ],
      candidateSha,
      ['Implementation Verification'],
    );
    expect(evaluation.disposition).toBe('INCONCLUSIVE');
  });
});

describe('AUT-001-B drift, merge and divergence policy', () => {
  it('blocks optimistic advancement on PR head drift', () => {
    const result = reconcileShadowTruth(
      'obs-head-drift',
      target({ expectedLifecycleState: 'AWAITING_PR_CI' }),
      truth({ pullRequest: { ...truth().pullRequest, headSha: 'new-head' } }),
    );
    expect(result.divergences.some((item) => item.kind === 'HEAD_DRIFT')).toBe(true);
    expect(result.derivedLifecycleFact).toBeUndefined();
    expect(result.blocking).toBe(true);
  });

  it('detects base drift and performs no synchronization transition', () => {
    const result = reconcileShadowTruth(
      'obs-base-drift',
      target({ expectedLifecycleState: 'AWAITING_PR_CI' }),
      truth({ pullRequest: { ...truth().pullRequest, baseSha: 'new-base' } }),
    );
    expect(result.divergences.some((item) => item.kind === 'BASE_DRIFT')).toBe(true);
    expect(result.derivedLifecycleFact).toBeUndefined();
    expect(result.blocking).toBe(true);
  });

  it('does not synthesize merge authority from a merge notification alone', () => {
    const journal = new ShadowJournal();
    const notification = delivery({ eventFamily: 'pull_request', action: 'closed' });
    journal.appendDelivery(notification, 'attempt-merge-notification');
    expect(classifyDeliveryAgainstTruth(notification, truth())).toBe('CURRENT_NOTIFICATION');

    const result = reconcileShadowTruth(
      'obs-merge-notification',
      target({
        initialLifecycleState: 'AWAITING_HUMAN_MERGE',
        lifecycleFacts: [],
        expectedLifecycleState: 'AWAITING_HUMAN_MERGE',
        expectedNextActions: [
          'github.pull_request.merged_after_human_approval',
          'invalidation.review_required',
        ],
      }),
      truth(),
    );
    expect(result.projectionAfterReconciliation.state).toBe('AWAITING_HUMAN_MERGE');
    expect(result.derivedLifecycleFact).toBeUndefined();
  });

  it('requires merge identity and base ancestry when authoritative PR truth says merged', () => {
    const mergedTruth = truth({
      pullRequest: {
        ...truth().pullRequest,
        state: 'closed',
        merged: true,
        mergeCommitSha: 'merge-sha',
      },
      mergeCommitInBase: 'UNKNOWN',
    });
    const result = reconcileShadowTruth(
      'obs-merge-ambiguous',
      target({
        initialLifecycleState: 'AWAITING_HUMAN_MERGE',
        expectedLifecycleState: 'AWAITING_HUMAN_MERGE',
      }),
      mergedTruth,
    );
    expect(result.blocking).toBe(true);
    expect(result.divergences.some((item) => item.kind === 'MANDATORY_TRUTH_UNAVAILABLE')).toBe(
      true,
    );
  });

  it('records state disagreement and blocks an unsafe optimistic advancement prediction', () => {
    const result = reconcileShadowTruth(
      'obs-unsafe',
      target({ expectedLifecycleState: 'AWAITING_PR_CI', expectedNextActions: [] }),
      truth(),
    );
    expect(result.divergences.some((item) => item.kind === 'UNSAFE_ADVANCEMENT_PREDICTION')).toBe(
      true,
    );
    expect(result.blocking).toBe(true);
  });
});

describe('AUT-001-B live read-only shadow orchestration', () => {
  it('collects current truth using only the declared read-only client methods', async () => {
    const client = new FakeReadClient();
    const snapshot = await collectAuthoritativeGitHubTruth(client, request);
    expect(snapshot.pullRequest.headSha).toBe(candidateSha);
    expect(client.calls).toEqual(['readPullRequest', 'readRef', 'readChecks', 'readWorkflows']);
  });

  it('reconstructs current truth without requiring a triggering delivery', async () => {
    const client = new FakeReadClient();
    const journal = new ShadowJournal();
    const result = await runReadOnlyShadow(
      client,
      journal,
      request,
      target(),
      'run-missed-delivery',
      'obs-missed-delivery',
    );
    expect(result.status).toBe('OBSERVED');
    expect(journal.snapshot().deliveries).toHaveLength(0);
    expect(journal.snapshot().observations).toHaveLength(1);
    expect(journal.snapshot().observations[0]?.projectionAfterReconciliation.state).toBe(
      'AWAITING_G5',
    );
  });

  it('preserves append-only history across restart and performs fresh authoritative reconciliation', async () => {
    const client = new FakeReadClient();
    const first = new ShadowJournal();
    first.appendDelivery(delivery(), 'delivery-attempt-1');
    await runReadOnlyShadow(client, first, request, target(), 'run-1', 'obs-1');

    const restarted = new ShadowJournal(first.snapshot());
    client.checks = [
      {
        ...successfulCheck(),
        id: 2,
        completedAt: '2026-09-28T17:50:00Z',
      },
    ];
    await runReadOnlyShadow(
      client,
      restarted,
      { ...request, observedAt: '2026-09-28T17:50:00Z' },
      target(),
      'run-2',
      'obs-2',
    );

    const snapshot = restarted.snapshot();
    expect(snapshot.deliveries).toHaveLength(1);
    expect(snapshot.observations).toHaveLength(2);
    expect(snapshot.runAttempts).toHaveLength(2);
  });

  it('fails inconclusive when mandatory GitHub truth is unavailable and does not fabricate an observation', async () => {
    const client = new FakeReadClient();
    client.failOn = 'readChecks';
    const journal = new ShadowJournal();
    const result = await runReadOnlyShadow(
      client,
      journal,
      request,
      target(),
      'run-unavailable',
      'obs-unavailable',
    );
    expect(result.status).toBe('INCONCLUSIVE');
    expect(journal.snapshot().observations).toHaveLength(0);
    expect(journal.snapshot().runAttempts[0]?.reason).toContain(
      'mandatory_github_truth_unavailable',
    );
  });

  it('preserves zero-mutation behavior during a complete shadow run', async () => {
    const client = new FakeReadClient();
    const journal = new ShadowJournal();
    await runReadOnlyShadow(client, journal, request, target(), 'run-readonly', 'obs-readonly');
    expect(client.calls.every((name) => name.startsWith('read'))).toBe(true);
    expect(client.calls).not.toContain('write');
  });
});

describe('AUT-001-B bounded observation window', () => {
  it('observes pending then success without retry-until-green semantics', async () => {
    const client = new FakeReadClient();
    client.checkSequence = [
      [
        {
          ...successfulCheck(),
          status: 'in_progress',
          conclusion: null,
          completedAt: null,
        },
      ],
      [successfulCheck()],
      [successfulCheck()],
    ];
    const clock = new FakeClock('2026-09-28T17:45:00Z');
    const { result, journal } = await runBoundedReadOnlyShadowWindow({
      client,
      journal: new ShadowJournal(),
      baseRequest: {
        repositoryId: request.repositoryId,
        repositoryFullName: request.repositoryFullName,
        pullRequestNumber: request.pullRequestNumber,
        baseRef: request.baseRef,
      },
      target: observationTarget(),
      authorityComparison: agreedAuthority,
      clock,
      config: {
        maxAttempts: 5,
        intervalMs: 1_000,
        timeoutMs: 60_000,
        confirmAfterTerminal: true,
      },
      candidateSha,
    });

    expect(result.status).toBe('TERMINAL');
    expect(result.terminalDisposition).toBe('PASS');
    expect(result.restartReconstructionCount).toBeGreaterThan(0);
    expect(journal.snapshot().observations.length).toBeGreaterThanOrEqual(3);
    expect(journal.snapshot().runAttempts.length).toBe(journal.snapshot().observations.length);
  });

  it('treats pending then failure as terminal evidence rather than retrying away failure', async () => {
    const client = new FakeReadClient();
    client.checkSequence = [
      [
        {
          ...successfulCheck(),
          status: 'in_progress',
          conclusion: null,
          completedAt: null,
        },
      ],
      [{ ...successfulCheck(), conclusion: 'failure' }],
      [{ ...successfulCheck(), conclusion: 'failure' }],
    ];
    const clock = new FakeClock('2026-09-28T17:45:00Z');
    const { result } = await runBoundedReadOnlyShadowWindow({
      client,
      journal: new ShadowJournal(),
      baseRequest: {
        repositoryId: request.repositoryId,
        repositoryFullName: request.repositoryFullName,
        pullRequestNumber: request.pullRequestNumber,
        baseRef: request.baseRef,
      },
      target: observationTarget(),
      authorityComparison: agreedAuthority,
      clock,
      config: {
        maxAttempts: 5,
        intervalMs: 1_000,
        timeoutMs: 60_000,
        confirmAfterTerminal: true,
      },
      candidateSha,
    });
    expect(result.status).toBe('TERMINAL');
    expect(result.terminalDisposition).toBe('FAILED');
  });

  it('times out when required checks remain pending', async () => {
    const client = new FakeReadClient();
    client.checks = [
      {
        ...successfulCheck(),
        status: 'in_progress',
        conclusion: null,
        completedAt: null,
      },
    ];
    const clock = new FakeClock('2026-09-28T17:45:00Z');
    const { result, journal } = await runBoundedReadOnlyShadowWindow({
      client,
      journal: new ShadowJournal(),
      baseRequest: {
        repositoryId: request.repositoryId,
        repositoryFullName: request.repositoryFullName,
        pullRequestNumber: request.pullRequestNumber,
        baseRef: request.baseRef,
      },
      target: observationTarget(),
      authorityComparison: agreedAuthority,
      clock,
      config: {
        maxAttempts: 3,
        intervalMs: 1_000,
        timeoutMs: 1_500,
        confirmAfterTerminal: true,
      },
      candidateSha,
    });
    expect(result.status).toBe('TIMED_OUT');
    expect(result.timedOut).toBe(true);
    expect(journal.snapshot().observations.length).toBeGreaterThan(0);
  });

  it('continues after a transient mandatory truth failure within the bounded window', async () => {
    const client = new FakeReadClient();
    let reads = 0;
    const original = client.readChecks.bind(client);
    client.readChecks = async () => {
      reads += 1;
      if (reads === 1) throw new Error('temporary_outage');
      return original();
    };
    const clock = new FakeClock('2026-09-28T17:45:00Z');
    const { result } = await runBoundedReadOnlyShadowWindow({
      client,
      journal: new ShadowJournal(),
      baseRequest: {
        repositoryId: request.repositoryId,
        repositoryFullName: request.repositoryFullName,
        pullRequestNumber: request.pullRequestNumber,
        baseRef: request.baseRef,
      },
      target: observationTarget(),
      authorityComparison: agreedAuthority,
      clock,
      config: {
        maxAttempts: 4,
        intervalMs: 1_000,
        timeoutMs: 60_000,
        confirmAfterTerminal: true,
      },
      candidateSha,
    });
    expect(result.status).toBe('TERMINAL');
    expect(result.terminalDisposition).toBe('PASS');
  });
});

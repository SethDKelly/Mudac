import { describe, expect, it } from 'vitest';

import { evaluateRequiredChecks } from '../src/github/checks.js';
import type {
  CheckTruth,
  DeliveryEnvelope,
  GitHubReadClient,
  GitHubTruthSnapshot,
  PullRequestTruth,
  ShadowReadRequest,
  ShadowTarget,
  WorkflowTruth,
} from '../src/github/model.js';
import {
  classifyDeliveryAgainstTruth,
  reconcileShadowTruth,
} from '../src/github/reconciliation.js';
import { collectAuthoritativeGitHubTruth, runReadOnlyShadow } from '../src/github/shadow.js';
import { ShadowJournal } from '../src/storage/shadow-journal.js';

const candidateSha = 'candidate-123';
const baseSha = 'base-456';
const observedAt = '2026-09-28T17:45:00Z';

function successfulCheck(
  name = 'Implementation Verification',
  headSha = candidateSha,
  attempt = 1,
): CheckTruth {
  return {
    id: attempt,
    name,
    headSha,
    attempt,
    status: 'completed',
    conclusion: 'success',
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
  ancestor: boolean | 'UNKNOWN' = false;
  failOn?: string;

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
    return structuredClone(this.checks);
  }

  async readWorkflows(): Promise<readonly WorkflowTruth[]> {
    this.calls.push('readWorkflows');
    if (this.failOn === 'readWorkflows') throw new Error('read_workflows_failed');
    return structuredClone(this.workflows);
  }

  async isAncestor(): Promise<boolean | 'UNKNOWN'> {
    this.calls.push('isAncestor');
    if (this.failOn === 'isAncestor') throw new Error('ancestry_failed');
    return this.ancestor;
  }
}

const request: ShadowReadRequest = {
  repositoryId: 1275654940,
  repositoryFullName: 'SethDKelly/Mudac',
  pullRequestNumber: 23,
  baseRef: 'aut-001/b-start-gate',
  observedAt,
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

  it('records unknown event families without lifecycle advancement semantics', () => {
    const item = delivery({ eventFamily: 'unknown', action: 'future_action' });
    const journal = new ShadowJournal();
    expect(journal.appendDelivery(item, 'attempt-1').status).toBe('ACCEPTED');
    expect(classifyDeliveryAgainstTruth(item, truth())).toBe('RECORD_NO_ADVANCE');
  });

  it('classifies a late event for a superseded head as historical only', () => {
    const item = delivery({ payloadHeadSha: 'old-head' });
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

  it.each([
    ['missing', [] as CheckTruth[]],
    [
      'running',
      [
        {
          ...successfulCheck(),
          status: 'in_progress' as const,
          conclusion: null,
        },
      ],
    ],
    [
      'failed',
      [
        {
          ...successfulCheck(),
          conclusion: 'failure' as const,
        },
      ],
    ],
    [
      'cancelled',
      [
        {
          ...successfulCheck(),
          conclusion: 'cancelled' as const,
        },
      ],
    ],
  ])('does not treat %s required-check state as pass', (_label, checks) => {
    const evaluation = evaluateRequiredChecks(checks, [], candidateSha, [
      'Implementation Verification',
    ]);
    expect(evaluation.disposition).not.toBe('PASS');
  });

  it('fails inconclusive on conflicting latest attempts for the same required context', () => {
    const evaluation = evaluateRequiredChecks(
      [successfulCheck(), { ...successfulCheck(), id: 99, conclusion: 'failure' }],
      [],
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
    client.checks = [{ ...successfulCheck(), attempt: 2 }];
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

import { readFileSync } from 'node:fs';
import { join, resolve } from 'node:path';
import { describe, expect, it } from 'vitest';

import {
  AppendOnlyFactStore,
  classifyRevisionDelta,
  createEvidenceBinding,
  phase021Identity,
  phase021LifecycleFacts,
  projectLifecycle,
  resolveFailureInjection,
  runPhase021Replay,
  type EvidenceNode,
  type LifecycleFact,
} from '../../tools/autonomy-control/src/index.js';

const repository = resolve(import.meta.dirname, '../..');
const replayContract = JSON.parse(
  readFileSync(join(repository, 'docs/routing/autonomy_shadow_replay_exit_contract.json'), 'utf8'),
) as {
  shadow_replay_cases: { id: string; result: string }[];
  failure_injection_cases: { id: string; injection: string; expected: string; result: string }[];
};

describe('AUT-001-A deterministic Phase-021 replay', () => {
  it('replays all seven historical shadow cases from executable state and revision rules', () => {
    const actual = runPhase021Replay();
    expect(actual).toHaveLength(7);
    expect(actual.map((item) => [item.id, item.pass])).toEqual(
      replayContract.shadow_replay_cases.map((item) => [item.id, item.result === 'PASS']),
    );
  });

  it('is deterministic for the same immutable fact set', () => {
    const first = projectLifecycle('PLANNING_READY', phase021LifecycleFacts);
    const second = projectLifecycle('PLANNING_READY', structuredClone(phase021LifecycleFacts));
    expect(second).toEqual(first);
    expect(first.state).toBe('COMPLETE');
  });

  it('keeps stale evidence historical rather than advancing current state', () => {
    const projection = projectLifecycle('PLANNING_READY', phase021LifecycleFacts);
    expect(projection.trace.find((entry) => entry.factId === '021-stale-check')).toMatchObject({
      disposition: 'HISTORICAL_NO_ADVANCE',
    });
  });
});

describe('AUT-001-A fail-closed lifecycle behavior', () => {
  it('blocks a human-stop transition without explicit human authority', () => {
    const facts = structuredClone(phase021LifecycleFacts.slice(0, 3));
    const g2 = facts[2];
    expect(g2).toBeDefined();
    if (!g2) throw new Error('missing fixture');
    delete g2.payload.humanAuthorityRef;
    const projection = projectLifecycle('PLANNING_READY', facts);
    expect(projection.state).toBe('BLOCKED');
    expect(projection.terminalReason).toBe('human_authority_required');
  });

  it('fails inconclusive on an unknown event', () => {
    const unknown: LifecycleFact = {
      factId: 'unknown',
      factType: 'lifecycle.event',
      logicalOrder: 1,
      payloadDigest: 'unknown',
      payload: { eventType: 'unknown.event', guardDecision: 'PASS' },
    };
    const projection = projectLifecycle('PLANNING_READY', [unknown]);
    expect(projection.state).toBe('INCONCLUSIVE');
  });

  it('fails inconclusive on ambiguous logical ordering', () => {
    const [first] = phase021LifecycleFacts;
    expect(first).toBeDefined();
    if (!first) throw new Error('missing fixture');
    const conflict: LifecycleFact = {
      factId: 'conflict',
      factType: 'lifecycle.event',
      logicalOrder: first.logicalOrder,
      payloadDigest: 'conflict',
      payload: { eventType: 'start_gate.ready', guardDecision: 'PASS' },
    };
    const projection = projectLifecycle('PLANNING_READY', [first, conflict]);
    expect(projection.state).toBe('INCONCLUSIVE');
    expect(projection.terminalReason).toBe('ambiguous_logical_order');
  });

  it('requires a fresh G2 after post-completion invalidation', () => {
    const invalidation: LifecycleFact = {
      factId: 'post-completion-invalidation',
      factType: 'lifecycle.event',
      logicalOrder: 27,
      payloadDigest: 'post-completion-invalidation',
      payload: { eventType: 'invalidation.material_confirmed', guardDecision: 'PASS' },
    };
    const projection = projectLifecycle('PLANNING_READY', [...phase021LifecycleFacts, invalidation]);
    expect(projection.state).toBe('REOPEN_REQUIRED');
    expect(projection.eligibleNextActions).toContain('authority.reopen_g2_granted');
  });
});

describe('AUT-001-A append-only fact semantics', () => {
  it('is idempotent for identical fact identity and digest and rejects conflicting reuse', () => {
    const store = new AppendOnlyFactStore<{ value: number }>();
    const fact = {
      factId: 'fact-1',
      factType: 'test',
      logicalOrder: 1,
      payloadDigest: 'digest-1',
      payload: { value: 1 },
    };
    expect(store.append(fact).status).toBe('APPENDED');
    expect(store.append(structuredClone(fact)).status).toBe('IDEMPOTENT_NOOP');
    expect(store.append({ ...fact, payloadDigest: 'digest-2' }).status).toBe('CONFLICT');
    expect(store.size).toBe(1);
  });
});

describe('AUT-001-A evidence classification and reuse', () => {
  it('classifies unmapped changed material as inconclusive', () => {
    const result = classifyRevisionDelta({
      oldRevision: phase021Identity.initialCandidate,
      newRevision: phase021Identity.repairedCandidate,
      changedSurfaces: [
        { surfaceId: 'unknown', surfaceClass: 'EXECUTABLE_MATERIAL', mapped: false },
      ],
    });
    expect(result.classification).toBe('INCONCLUSIVE');
    expect(result.reusableEvidence).toBe(false);
  });

  it('reuses evidence only by creating a binding that preserves original subject identity', () => {
    const evidence: EvidenceNode = {
      evidenceId: 'evidence-1',
      subject: phase021Identity.repairedCandidate,
      materialBoundaryIds: ['dependency-enforcement'],
      contentDigest: 'evidence-digest',
    };
    const binding = createEvidenceBinding(
      'binding-1',
      evidence,
      phase021Identity.reboundHead,
      'governance_delta_executable_surfaces_equivalent',
    );
    expect(binding.originalSubject).toEqual(phase021Identity.repairedCandidate);
    expect(binding.targetSubject).toEqual(phase021Identity.reboundHead);
    expect(evidence.subject).toEqual(phase021Identity.repairedCandidate);
  });
});

describe('AUT-001-A R-G failure policy executable baseline', () => {
  for (const failureCase of replayContract.failure_injection_cases) {
    it(`${failureCase.id} resolves ${failureCase.injection} to its declared fail-safe disposition`, () => {
      expect(resolveFailureInjection(failureCase.injection)).toBe(failureCase.expected);
      expect(failureCase.result).toBe('PASS');
    });
  }

  it('fails closed for a failure injection absent from the declared policy', () => {
    expect(resolveFailureInjection('unregistered_failure')).toBe(
      'INCONCLUSIVE_UNKNOWN_FAILURE_INJECTION',
    );
  });
});

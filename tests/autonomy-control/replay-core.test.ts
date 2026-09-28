import { readFileSync } from 'node:fs';
import { join, resolve } from 'node:path';
import { describe, expect, it } from 'vitest';

import {
  AppendOnlyFactStore,
  classifyRevisionDelta,
  createEvidenceBinding,
  executeStageAFailureCase,
  failureCaseMatrix,
  phase021Identity,
  phase021LifecycleFacts,
  projectLifecycle,
  runPhase021Replay,
  type EvidenceNode,
  type FailureCaseId,
  type LifecycleFact,
  type MaterialSurfaceClass,
} from '../../tools/autonomy-control/src/index.js';

const repository = resolve(import.meta.dirname, '../..');
const replayContract = JSON.parse(
  readFileSync(join(repository, 'docs/routing/autonomy_shadow_replay_exit_contract.json'), 'utf8'),
) as {
  shadow_replay_cases: { id: string }[];
  failure_injection_cases: { id: string; injection: string }[];
};

const stateAfter = (factId: string) => {
  const { projection } = runPhase021Replay();
  return projection.trace.find((entry) => entry.factId === factId)?.stateAfter;
};

const disposition = (factId: string) => {
  const { projection } = runPhase021Replay();
  return projection.trace.find((entry) => entry.factId === factId)?.disposition;
};

describe('AUT-001-A deterministic Phase-021 replay', () => {
  it('covers the seven canonical SR case identities without importing their PASS flags as an oracle', () => {
    expect(replayContract.shadow_replay_cases.map((item) => item.id)).toEqual([
      'SR-01',
      'SR-02',
      'SR-03',
      'SR-04',
      'SR-05',
      'SR-06',
      'SR-07',
    ]);
  });

  it('SR-01 routes the initial adversarial failure through bounded repair and a new candidate', () => {
    const { classifications } = runPhase021Replay();
    expect(stateAfter('021-10')).toBe('REPAIR_REQUIRED');
    expect(stateAfter('021-11')).toBe('IMPLEMENTING');
    expect(stateAfter('021-12')).toBe('CANDIDATE_REGISTERED');
    expect(classifications[0]?.classification).toBe('EXECUTABLE_MATERIAL_DELTA');
  });

  it('SR-02 proves the repaired candidate traverses fresh review, CI, and G5 in order', () => {
    expect(stateAfter('021-15')).toBe('AWAITING_ADVERSARIAL_REVIEW');
    expect(stateAfter('021-16')).toBe('AWAITING_PR_CI');
    expect(stateAfter('021-17')).toBe('AWAITING_G5');
    expect(stateAfter('021-18')).toBe('AWAITING_HUMAN_MERGE');
  });

  it('SR-03 freezes governance drift and requires fresh review while preserving executable equivalence', () => {
    const { classifications } = runPhase021Replay();
    expect(classifications[1]?.classification).toBe('GOVERNANCE_MATERIAL_DELTA');
    expect(classifications[1]?.reusableEvidence).toBe(true);
    expect(stateAfter('021-19')).toBe('AWAITING_INDEPENDENT_REVIEW');
    expect(stateAfter('021-20')).toBe('AWAITING_ADVERSARIAL_REVIEW');
    expect(stateAfter('021-21')).toBe('AWAITING_PR_CI');
  });

  it('SR-04 keeps stale CI historical and G5 behind the human merge stop', () => {
    expect(disposition('021-stale-check')).toBe('HISTORICAL_NO_ADVANCE');
    expect(stateAfter('021-22')).toBe('AWAITING_G5');
    expect(stateAfter('021-23')).toBe('AWAITING_HUMAN_MERGE');
  });

  it('SR-05 registers a distinct same-tree integration identity only after human merge authority', () => {
    const { classifications } = runPhase021Replay();
    expect(classifications[2]?.classification).toBe('PROVENANCE_ONLY_CHANGE');
    expect(stateAfter('021-24')).toBe('INTEGRATION_VERIFYING');
  });

  it('SR-06 treats closure evidence as non-executable and preserves the closure human stop', () => {
    const { classifications } = runPhase021Replay();
    expect(classifications[3]?.classification).toBe('NON_MATERIAL_TREE_CHANGE');
    expect(stateAfter('021-25')).toBe('AWAITING_CLOSURE_MERGE');
  });

  it('SR-07 completes only after human closure merge and does not synthesize Phase-022 authority', () => {
    const { projection, classifications } = runPhase021Replay();
    expect(classifications[4]?.classification).toBe('PROVENANCE_ONLY_CHANGE');
    expect(stateAfter('021-26')).toBe('COMPLETE');
    expect(projection.state).toBe('COMPLETE');
    expect(projection.eligibleNextActions).toEqual(['invalidation.material_confirmed']);
  });

  it('is deterministic for the same immutable fact set', () => {
    const first = projectLifecycle('PLANNING_READY', phase021LifecycleFacts);
    const second = projectLifecycle('PLANNING_READY', structuredClone(phase021LifecycleFacts));
    expect(second).toEqual(first);
  });
});

describe('AUT-001-A fail-closed lifecycle behavior', () => {
  it('fails inconclusive when guardDecision is omitted', () => {
    const fact: LifecycleFact = {
      factId: 'missing-guard',
      factType: 'lifecycle.event',
      logicalOrder: 1,
      payloadDigest: 'missing-guard',
      payload: { eventType: 'start_gate.ready' },
    };
    const projection = projectLifecycle('PLANNING_READY', [fact]);
    expect(projection.state).toBe('INCONCLUSIVE');
    expect(projection.terminalReason).toBe('missing_or_invalid_guard_decision');
  });

  it('blocks a human-stop transition without explicit matching human authority', () => {
    const missingAuthority = structuredClone(phase021LifecycleFacts.slice(0, 3));
    const g2 = missingAuthority[2];
    expect(g2).toBeDefined();
    if (!g2) throw new Error('missing fixture');
    delete g2.payload.humanAuthorityRef;
    const missingProjection = projectLifecycle('PLANNING_READY', missingAuthority);
    expect(missingProjection.state).toBe('BLOCKED');

    const wrongAuthority = structuredClone(phase021LifecycleFacts.slice(0, 3));
    const wrongG2 = wrongAuthority[2];
    expect(wrongG2).toBeDefined();
    if (!wrongG2) throw new Error('missing fixture');
    wrongG2.payload.humanAuthorityKind = 'PROTECTED_IMPLEMENTATION_MERGE';
    const wrongProjection = projectLifecycle('PLANNING_READY', wrongAuthority);
    expect(wrongProjection.state).toBe('BLOCKED');
    expect(wrongProjection.terminalReason).toBe('matching_human_authority_required');
  });

  it('fails inconclusive on an unknown event', () => {
    const unknown: LifecycleFact = {
      factId: 'unknown',
      factType: 'lifecycle.event',
      logicalOrder: 1,
      payloadDigest: 'unknown',
      payload: { eventType: 'unknown.event', guardDecision: 'PASS' },
    };
    expect(projectLifecycle('PLANNING_READY', [unknown]).state).toBe('INCONCLUSIVE');
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

  it('rejects duplicate event identity even when a caller reuses the same digest label for different payload', () => {
    const first: LifecycleFact = {
      factId: 'duplicate',
      factType: 'lifecycle.event',
      logicalOrder: 1,
      payloadDigest: 'same-label',
      payload: { eventType: 'start_gate.ready', guardDecision: 'PASS' },
    };
    const conflicting: LifecycleFact = {
      ...first,
      payload: { eventType: 'start_gate.pass', guardDecision: 'PASS' },
    };
    const projection = projectLifecycle('PLANNING_READY', [first, conflicting]);
    expect(projection.state).toBe('INCONCLUSIVE');
    expect(projection.terminalReason).toBe('conflicting_duplicate_event');
  });

  it('requires a fresh G2 after post-completion invalidation', () => {
    const invalidation: LifecycleFact = {
      factId: 'post-completion-invalidation',
      factType: 'lifecycle.event',
      logicalOrder: 27,
      payloadDigest: 'post-completion-invalidation',
      payload: { eventType: 'invalidation.material_confirmed', guardDecision: 'PASS' },
    };
    const projection = projectLifecycle('PLANNING_READY', [
      ...phase021LifecycleFacts,
      invalidation,
    ]);
    expect(projection.state).toBe('REOPEN_REQUIRED');
    expect(projection.eligibleNextActions).toContain('authority.reopen_g2_granted');
  });
});

describe('AUT-001-A append-only fact semantics', () => {
  it('is idempotent only for identical fact contents and rejects same-id conflicting contents', () => {
    const store = new AppendOnlyFactStore<{ value: number }>();
    const fact = {
      factId: 'fact-1',
      factType: 'test',
      logicalOrder: 1,
      payloadDigest: 'same-label',
      payload: { value: 1 },
    };
    expect(store.append(fact).status).toBe('APPENDED');
    expect(store.append(structuredClone(fact)).status).toBe('IDEMPOTENT_NOOP');
    expect(store.append({ ...fact, payload: { value: 2 } }).status).toBe('CONFLICT');
    expect(store.snapshot()).toEqual([fact]);
    expect(store.size).toBe(1);
  });

  it('stores a clone so caller mutation cannot rewrite accepted history', () => {
    const store = new AppendOnlyFactStore<{ nested: { value: number } }>();
    const fact = {
      factId: 'immutable',
      factType: 'test',
      logicalOrder: 1,
      payloadDigest: 'digest',
      payload: { nested: { value: 1 } },
    };
    store.append(fact);
    fact.payload.nested.value = 99;
    expect(store.snapshot()[0]?.payload.nested.value).toBe(1);
  });
});

describe('AUT-001-A revision classification and evidence reuse', () => {
  const oldRevision = { sha: 'old', treeSha: 'tree-old' };
  const changedRevision = { sha: 'new', treeSha: 'tree-new' };
  const surface = (surfaceClass: MaterialSurfaceClass) => ({
    surfaceId: surfaceClass,
    surfaceClass,
    mapped: true,
  });

  it('covers every revision classification and the same-SHA conflict path', () => {
    expect(
      classifyRevisionDelta({ oldRevision, newRevision: oldRevision, changedSurfaces: [] })
        .classification,
    ).toBe('IDENTICAL_REVISION');
    expect(
      classifyRevisionDelta({
        oldRevision,
        newRevision: { sha: 'new-sha', treeSha: oldRevision.treeSha },
        changedSurfaces: [],
      }).classification,
    ).toBe('PROVENANCE_ONLY_CHANGE');
    expect(
      classifyRevisionDelta({
        oldRevision,
        newRevision: changedRevision,
        changedSurfaces: [surface('EVIDENCE_ONLY')],
      }).classification,
    ).toBe('NON_MATERIAL_TREE_CHANGE');
    expect(
      classifyRevisionDelta({
        oldRevision,
        newRevision: changedRevision,
        changedSurfaces: [surface('AUTHORITY_GOVERNANCE_MATERIAL')],
      }).classification,
    ).toBe('GOVERNANCE_MATERIAL_DELTA');
    expect(
      classifyRevisionDelta({
        oldRevision,
        newRevision: changedRevision,
        changedSurfaces: [surface('CI_EVALUATOR_MATERIAL')],
      }).classification,
    ).toBe('EVALUATOR_MATERIAL_DELTA');
    expect(
      classifyRevisionDelta({
        oldRevision,
        newRevision: changedRevision,
        changedSurfaces: [surface('EXECUTABLE_MATERIAL')],
      }).classification,
    ).toBe('EXECUTABLE_MATERIAL_DELTA');
    expect(
      classifyRevisionDelta({
        oldRevision,
        newRevision: changedRevision,
        changedSurfaces: [surface('EXECUTABLE_MATERIAL'), surface('CI_EVALUATOR_MATERIAL')],
      }).classification,
    ).toBe('MIXED_MATERIAL_DELTA');
    expect(
      classifyRevisionDelta({
        oldRevision,
        newRevision: { sha: oldRevision.sha, treeSha: 'conflicting-tree' },
        changedSurfaces: [],
      }).classification,
    ).toBe('INCONCLUSIVE');
  });

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

describe('AUT-001-A R-G failure-case partition and executable subset', () => {
  it('covers every canonical FI identity and injection without reading contract expected/result fields', () => {
    expect(failureCaseMatrix.map(({ id, injection }) => ({ id, injection }))).toEqual(
      replayContract.failure_injection_cases,
    );
    expect(failureCaseMatrix).toHaveLength(28);
  });

  const stageAExpected: Readonly<Partial<Record<FailureCaseId, string>>> = {
    'FI-01': 'IDEMPOTENT_NOOP',
    'FI-02': 'INCONCLUSIVE_SECURITY_RECONCILIATION',
    'FI-03': 'HISTORICAL_NO_CURRENT_TRANSITION',
    'FI-04': 'RECONCILE_OR_INCONCLUSIVE',
    'FI-05': 'FREEZE_MERGE_AND_R_C_DELTA_CLASSIFY',
    'FI-06': 'INCONCLUSIVE_FAIL_CLOSED',
    'FI-11': 'BLOCKED_HUMAN_DISPOSITION_OR_REAUTHORIZATION',
    'FI-12': 'BLOCKED_HUMAN_PROGRAM_EXTENSION_REQUIRED',
    'FI-20': 'NO_REQUIRED_CI_PASS_TRANSITION',
    'FI-22': 'AWAIT_HUMAN_MERGE',
    'FI-23': 'DENY_NO_AUTHORITY_SYNTHESIS',
    'FI-24': 'REOPEN_REQUIRED_OLD_G2_NOT_RESTORED',
  };

  for (const [id, expected] of Object.entries(stageAExpected) as [FailureCaseId, string][]) {
    it(`${id} exercises Stage-A behavior and independently yields ${expected}`, () => {
      expect(executeStageAFailureCase(id)).toMatchObject({
        id,
        status: 'EXECUTED',
        observedDisposition: expected,
      });
    });
  }

  it('marks later-stage cases deferred instead of claiming Stage-A PASS', () => {
    const executableIds = new Set(Object.keys(stageAExpected));
    for (const definition of failureCaseMatrix) {
      if (executableIds.has(definition.id)) continue;
      const result = executeStageAFailureCase(definition.id);
      expect(result.status).toBe('DEFERRED');
      expect(result.deferredTo?.length).toBeGreaterThan(0);
      expect(result.observedDisposition).toBeUndefined();
    }
  });
});

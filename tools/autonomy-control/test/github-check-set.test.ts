import { describe, expect, it } from 'vitest';

import { evaluateRequiredChecks } from '../src/github/checks.js';
import { reconcileShadowTruth } from '../src/github/reconciliation.js';

describe('AUT-001-B required-check set authority', () => {
  it('fails inconclusive when the required-check set is empty', () => {
    expect(evaluateRequiredChecks([], [], 'candidate', [])).toEqual({
      disposition: 'INCONCLUSIVE',
      reason: 'required_check_set_missing_or_invalid',
      matched: {},
      missing: [],
    });
  });

  it('does not derive CI advancement from an empty required-check set', () => {
    const observation = reconcileShadowTruth(
      'obs-empty-required-set',
      {
        candidateSha: 'candidate',
        expectedBaseSha: 'base',
        requiredCheckNames: [],
        initialLifecycleState: 'AWAITING_PR_CI',
        lifecycleFacts: [],
        expectedLifecycleState: 'AWAITING_PR_CI',
      },
      {
        repositoryId: 1,
        repositoryFullName: 'SethDKelly/Mudac',
        observedAt: '2026-09-28T18:05:00Z',
        pullRequest: {
          number: 23,
          state: 'open',
          merged: false,
          draft: true,
          headSha: 'candidate',
          baseRef: 'aut-001/b-start-gate',
          baseSha: 'base',
          mergeCommitSha: null,
        },
        baseRef: { ref: 'aut-001/b-start-gate', sha: 'base' },
        checks: [],
        workflows: [],
        mergeCommitInBase: false,
      },
    );

    expect(observation.requiredChecks.disposition).toBe('INCONCLUSIVE');
    expect(observation.derivedLifecycleFact).toBeUndefined();
    expect(observation.projectionAfterReconciliation.state).toBe('AWAITING_PR_CI');
    expect(observation.blocking).toBe(true);
  });
});

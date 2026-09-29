import { describe, expect, it } from 'vitest';

import { evaluateRequiredChecks } from '../src/github/checks.js';
import type { CheckTruth, WorkflowTruth } from '../src/github/model.js';
import { reconcileShadowTruth } from '../src/github/reconciliation.js';
import { compareRequiredCheckAuthority } from '../src/github/required-check-authority.js';

function check(overrides: Partial<CheckTruth> & Pick<CheckTruth, 'name' | 'id'>): CheckTruth {
  return {
    headSha: 'candidate',
    status: 'completed',
    conclusion: 'success',
    startedAt: '2026-09-28T18:00:00Z',
    completedAt: '2026-09-28T18:01:00Z',
    ...overrides,
  };
}

describe('AUT-001-B required-check set authority', () => {
  const packageAuthority = {
    packageContractPath: 'docs/routing/aut001_implementation_package_contract.json',
    packageSchema: 'mudac.aut001-implementation-package/v1',
    rulesetName: 'main — protected',
    rulesetEnforcement: 'active',
    packageRequiredContexts: [
      'Validate agentic/documentation conformance',
      'Implementation Verification',
      'CodeQL JavaScript/TypeScript',
    ],
  };

  it('agrees when package and live ruleset contexts match exactly', () => {
    const comparison = compareRequiredCheckAuthority(packageAuthority, {
      rulesetId: 1,
      rulesetName: 'main — protected',
      enforcement: 'active',
      target: 'branch',
      requiredContexts: [
        'CodeQL JavaScript/TypeScript',
        'Implementation Verification',
        'Validate agentic/documentation conformance',
      ],
    });
    expect(comparison.status).toBe('AGREED');
    if (comparison.status === 'AGREED') {
      expect(comparison.requiredContexts).toEqual([
        'CodeQL JavaScript/TypeScript',
        'Implementation Verification',
        'Validate agentic/documentation conformance',
      ]);
    }
  });

  it('mismatches when package and live contexts differ', () => {
    const comparison = compareRequiredCheckAuthority(packageAuthority, {
      rulesetId: 1,
      rulesetName: 'main — protected',
      enforcement: 'active',
      target: 'branch',
      requiredContexts: ['Implementation Verification', 'CodeQL'],
    });
    expect(comparison.status).toBe('MISMATCH');
  });

  it('fails inconclusive when the required-check set is empty', () => {
    expect(evaluateRequiredChecks([], 'candidate', [])).toEqual({
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

describe('AUT-001-B required check-run identity', () => {
  const required = ['Implementation Verification'];

  it('passes when the exact check-run context is successful', () => {
    expect(
      evaluateRequiredChecks(
        [check({ id: 1, name: 'Implementation Verification' })],
        'candidate',
        required,
      ).disposition,
    ).toBe('PASS');
  });

  it.each([
    ['missing', [] as CheckTruth[]],
    [
      'running',
      [
        check({
          id: 1,
          name: 'Implementation Verification',
          status: 'in_progress',
          conclusion: null,
          completedAt: null,
        }),
      ],
    ],
    ['failed', [check({ id: 1, name: 'Implementation Verification', conclusion: 'failure' })]],
    ['cancelled', [check({ id: 1, name: 'Implementation Verification', conclusion: 'cancelled' })]],
    ['skipped', [check({ id: 1, name: 'Implementation Verification', conclusion: 'skipped' })]],
  ])('does not treat %s required-check state as pass', (_label, checks) => {
    expect(evaluateRequiredChecks(checks, 'candidate', required).disposition).not.toBe('PASS');
  });

  it('rejects stale wrong-head contexts', () => {
    const evaluation = evaluateRequiredChecks(
      [check({ id: 1, name: 'Implementation Verification', headSha: 'old-head' })],
      'candidate',
      required,
    );
    expect(evaluation.disposition).toBe('NOT_READY');
    expect(evaluation.missing).toEqual(['Implementation Verification']);
  });

  it('selects the newest check run when currentness is unambiguous', () => {
    const evaluation = evaluateRequiredChecks(
      [
        check({
          id: 1,
          name: 'Implementation Verification',
          conclusion: 'failure',
          completedAt: '2026-09-28T18:00:00Z',
        }),
        check({
          id: 2,
          name: 'Implementation Verification',
          conclusion: 'success',
          completedAt: '2026-09-28T18:05:00Z',
        }),
      ],
      'candidate',
      required,
    );
    expect(evaluation.disposition).toBe('PASS');
    expect(evaluation.matched['Implementation Verification']?.checkRunId).toBe(2);
  });

  it('fails closed when multiple check runs cannot be ordered unambiguously', () => {
    const evaluation = evaluateRequiredChecks(
      [
        check({
          id: 1,
          name: 'Implementation Verification',
          conclusion: 'success',
          completedAt: '2026-09-28T18:05:00Z',
        }),
        check({
          id: 2,
          name: 'Implementation Verification',
          conclusion: 'failure',
          completedAt: '2026-09-28T18:05:00Z',
        }),
      ],
      'candidate',
      required,
    );
    expect(evaluation.disposition).toBe('INCONCLUSIVE');
  });

  it('does not allow a workflow with a matching name to substitute for a missing check run', () => {
    const workflows: WorkflowTruth[] = [
      {
        id: 99,
        name: 'Implementation Verification',
        headSha: 'candidate',
        attempt: 1,
        status: 'completed',
        conclusion: 'success',
      },
    ];
    void workflows;
    const evaluation = evaluateRequiredChecks([], 'candidate', required);
    expect(evaluation.disposition).toBe('NOT_READY');
    expect(evaluation.missing).toEqual(['Implementation Verification']);
  });
});

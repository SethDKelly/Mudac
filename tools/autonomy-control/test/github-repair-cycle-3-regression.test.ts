import { describe, expect, it } from 'vitest';

import { evaluateRequiredChecks, parseComparableInstant } from '../src/github/checks.js';
import type { CheckTruth } from '../src/github/model.js';
import { reconcileShadowTruth } from '../src/github/reconciliation.js';

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

describe('AUT-001-B Repair Cycle 3 timestamp and reconciliation falsification', () => {
  const required = ['Implementation Verification'];

  it('rejects independent offset impossible-calendar success (AUT-B-R2-IR-01)', () => {
    expect(parseComparableInstant('2026-09-31T10:00:00+00:00', 'completedAt')).toEqual({
      kind: 'INVALID',
      reason: 'malformed_completedAt',
    });
  });

  it('rejects February 30 and non-leap February 29 under strict UTC-Z grammar', () => {
    expect(parseComparableInstant('2026-02-30T10:00:00+00:00', 'completedAt').kind).toBe(
      'INVALID',
    );
    expect(parseComparableInstant('2026-02-30T10:00:00Z', 'completedAt').kind).toBe('INVALID');
    expect(parseComparableInstant('2025-02-29T10:00:00Z', 'completedAt').kind).toBe('INVALID');
  });

  it('accepts a valid leap-day UTC instant', () => {
    expect(parseComparableInstant('2028-02-29T10:00:00Z', 'completedAt')).toEqual({
      kind: 'OK',
      ms: Date.UTC(2028, 1, 29, 10, 0, 0),
    });
  });

  it('rejects older valid failure + malformed newer offset success without PASS (AUT-B-R2-IR-03)', () => {
    const evaluation = evaluateRequiredChecks(
      [
        check({
          id: 1,
          name: 'Implementation Verification',
          conclusion: 'failure',
          completedAt: '2026-09-30T18:00:00Z',
        }),
        check({
          id: 2,
          name: 'Implementation Verification',
          conclusion: 'success',
          completedAt: '2026-09-31T10:00:00+00:00',
        }),
      ],
      'candidate',
      required,
    );
    expect(evaluation.disposition).toBe('INCONCLUSIVE');
    expect(evaluation.disposition).not.toBe('PASS');
  });

  it('keeps malformed sole success from establishing PASS', () => {
    expect(
      evaluateRequiredChecks(
        [
          check({
            id: 1,
            name: 'Implementation Verification',
            completedAt: '2026-09-31T10:00:00+00:00',
          }),
        ],
        'candidate',
        required,
      ).disposition,
    ).toBe('INCONCLUSIVE');
  });

  it('rejects malformed newer failure after valid older success without PASS', () => {
    const evaluation = evaluateRequiredChecks(
      [
        check({
          id: 1,
          name: 'Implementation Verification',
          conclusion: 'success',
          completedAt: '2026-09-30T18:00:00Z',
        }),
        check({
          id: 2,
          name: 'Implementation Verification',
          conclusion: 'failure',
          completedAt: '2026-09-31T10:00:00+00:00',
        }),
      ],
      'candidate',
      required,
    );
    expect(evaluation.disposition).toBe('INCONCLUSIVE');
    expect(evaluation.disposition).not.toBe('PASS');
  });

  it('rejects equal valid latest timestamps with competing conclusions', () => {
    expect(
      evaluateRequiredChecks(
        [
          check({
            id: 1,
            name: 'Implementation Verification',
            conclusion: 'success',
            completedAt: '2026-09-30T18:05:00Z',
          }),
          check({
            id: 2,
            name: 'Implementation Verification',
            conclusion: 'failure',
            completedAt: '2026-09-30T18:05:00Z',
          }),
        ],
        'candidate',
        required,
      ).disposition,
    ).toBe('INCONCLUSIVE');
  });

  it('rejects completed before started and completed without completedAt', () => {
    expect(
      evaluateRequiredChecks(
        [
          check({
            id: 1,
            name: 'Implementation Verification',
            startedAt: '2026-09-30T18:05:00Z',
            completedAt: '2026-09-30T18:01:00Z',
          }),
        ],
        'candidate',
        required,
      ).disposition,
    ).toBe('INCONCLUSIVE');
    expect(
      evaluateRequiredChecks(
        [
          check({
            id: 1,
            name: 'Implementation Verification',
            status: 'completed',
            conclusion: 'success',
            completedAt: null,
          }),
        ],
        'candidate',
        required,
      ).disposition,
    ).toBe('INCONCLUSIVE');
  });

  it('rejects nonterminal runs that still carry completedAt', () => {
    expect(
      evaluateRequiredChecks(
        [
          check({
            id: 1,
            name: 'Implementation Verification',
            status: 'in_progress',
            conclusion: null,
            startedAt: '2026-09-30T18:00:00Z',
            completedAt: '2026-09-30T18:01:00Z',
          }),
        ],
        'candidate',
        required,
      ).disposition,
    ).toBe('INCONCLUSIVE');
  });

  it('preserves valid newer-failure / newer-success / in-progress / wrong-SHA selection', () => {
    expect(
      evaluateRequiredChecks(
        [
          check({
            id: 1,
            name: 'Implementation Verification',
            conclusion: 'success',
            completedAt: '2026-09-30T18:00:00Z',
          }),
          check({
            id: 2,
            name: 'Implementation Verification',
            conclusion: 'failure',
            completedAt: '2026-09-30T18:10:00Z',
          }),
        ],
        'candidate',
        required,
      ).disposition,
    ).toBe('FAILED');

    expect(
      evaluateRequiredChecks(
        [
          check({
            id: 1,
            name: 'Implementation Verification',
            conclusion: 'failure',
            completedAt: '2026-09-30T18:00:00Z',
          }),
          check({
            id: 2,
            name: 'Implementation Verification',
            conclusion: 'success',
            completedAt: '2026-09-30T18:10:00Z',
          }),
        ],
        'candidate',
        required,
      ).disposition,
    ).toBe('PASS');

    expect(
      evaluateRequiredChecks(
        [
          check({
            id: 1,
            name: 'Implementation Verification',
            conclusion: 'success',
            completedAt: '2026-09-30T18:00:00Z',
          }),
          check({
            id: 2,
            name: 'Implementation Verification',
            status: 'in_progress',
            conclusion: null,
            startedAt: '2026-09-30T18:10:00Z',
            completedAt: null,
          }),
        ],
        'candidate',
        required,
      ).disposition,
    ).toBe('NOT_READY');

    expect(
      evaluateRequiredChecks(
        [
          check({
            id: 1,
            name: 'Implementation Verification',
            headSha: 'other-candidate',
            conclusion: 'success',
            completedAt: '2026-09-30T19:00:00Z',
          }),
          check({
            id: 2,
            name: 'Implementation Verification',
            conclusion: 'failure',
            completedAt: '2026-09-30T18:00:00Z',
          }),
        ],
        'candidate',
        required,
      ).disposition,
    ).toBe('FAILED');
  });

  it('blocks optimistic lifecycle advancement through full reconciliation (AUT-B-R2-IR-03)', () => {
    const observation = reconcileShadowTruth(
      'obs-rc3-offset-impossible-calendar',
      {
        candidateSha: 'candidate',
        expectedBaseSha: 'base',
        requiredCheckNames: required,
        initialLifecycleState: 'AWAITING_PR_CI',
        lifecycleFacts: [],
        expectedLifecycleState: 'AWAITING_PR_CI',
      },
      {
        repositoryId: 1,
        repositoryFullName: 'SethDKelly/Mudac',
        observedAt: '2026-09-30T20:00:00Z',
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
        checks: [
          check({
            id: 1,
            name: 'Implementation Verification',
            conclusion: 'failure',
            completedAt: '2026-09-30T18:00:00Z',
          }),
          check({
            id: 2,
            name: 'Implementation Verification',
            conclusion: 'success',
            completedAt: '2026-09-31T10:00:00+00:00',
          }),
        ],
        workflows: [],
        mergeCommitInBase: false,
      },
    );

    expect(observation.requiredChecks.disposition).not.toBe('PASS');
    expect(observation.requiredChecks.disposition).toBe('INCONCLUSIVE');
    expect(observation.derivedLifecycleFact).toBeUndefined();
    expect(observation.projectionAfterReconciliation.state).toBe('AWAITING_PR_CI');
    expect(observation.projectionAfterReconciliation.state).not.toBe('AWAITING_G5');
    expect(observation.blocking).toBe(true);
    expect(
      observation.divergences.some(
        (item) => item.kind === 'AMBIGUOUS_REQUIRED_CHECK_TRUTH' && item.severity === 'BLOCKING',
      ),
    ).toBe(true);
  });
});

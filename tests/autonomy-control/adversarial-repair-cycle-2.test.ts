import { describe, expect, it } from 'vitest';

import {
  executeStageAFailureCase,
  projectLifecycle,
  type LifecycleFact,
} from '../../tools/autonomy-control/src/index.js';

const fact = (
  factId: string,
  logicalOrder: number,
  eventType: string,
  extra: Partial<LifecycleFact['payload']> = {},
): LifecycleFact => ({
  factId,
  factType: 'adversarial-regression',
  logicalOrder,
  payloadDigest: `${factId}:${eventType}`,
  payload: {
    eventType,
    guardDecision: 'PASS',
    ...extra,
  },
});

describe('AUT-001-A repair-cycle-2 adversarial regressions', () => {
  it.each([Number.NaN, Number.POSITIVE_INFINITY, Number.NEGATIVE_INFINITY])(
    'fails closed before sorting for non-finite logicalOrder %s',
    (logicalOrder) => {
      const projection = projectLifecycle('PLANNING_READY', [
        fact('invalid-order-1', logicalOrder, 'start_gate.ready'),
        fact('invalid-order-2', logicalOrder, 'start_gate.pass'),
      ]);

      expect(projection.state).toBe('INCONCLUSIVE');
      expect(projection.terminalReason).toBe('invalid_logical_order');
      expect(projection.trace).toEqual([]);
    },
  );

  it('fails closed on a malformed required fact envelope before transition evaluation', () => {
    const malformed = fact('malformed', 1, 'start_gate.ready');
    malformed.payloadDigest = '   ';

    const projection = projectLifecycle('PLANNING_READY', [malformed]);
    expect(projection.state).toBe('INCONCLUSIVE');
    expect(projection.terminalReason).toBe('invalid_fact_envelope');
  });

  it('rejects whitespace-only human authority references', () => {
    const projection = projectLifecycle('AWAITING_G2', [
      fact('whitespace-authority', 1, 'authority.g2_granted', {
        humanAuthorityRef: '   ',
        humanAuthorityKind: 'G2',
      }),
    ]);

    expect(projection.state).toBe('BLOCKED');
    expect(projection.terminalReason).toBe('matching_human_authority_required');
  });

  it('implements canonical F03 scope expansion as a distinct blocked semantic', () => {
    const projection = projectLifecycle('REPAIR_REQUIRED', [
      fact('scope-expansion', 1, 'repair.scope_or_budget_expansion_required', {
        repairBlocker: 'SCOPE_EXPANSION',
      }),
    ]);

    expect(projection.state).toBe('BLOCKED');
    expect(projection.terminalReason).toBe(
      'repair_scope_expansion_requires_human_disposition_or_reauthorization',
    );
    expect(executeStageAFailureCase('FI-11').observedDisposition).toBe(
      'BLOCKED_HUMAN_DISPOSITION_OR_REAUTHORIZATION',
    );
  });

  it('implements canonical F03 budget exhaustion as a distinct blocked semantic', () => {
    const projection = projectLifecycle('REPAIR_REQUIRED', [
      fact('budget-exhausted', 1, 'repair.scope_or_budget_expansion_required', {
        repairBlocker: 'BUDGET_EXHAUSTED',
      }),
    ]);

    expect(projection.state).toBe('BLOCKED');
    expect(projection.terminalReason).toBe(
      'repair_budget_exhausted_requires_human_program_extension',
    );
    expect(executeStageAFailureCase('FI-12').observedDisposition).toBe(
      'BLOCKED_HUMAN_PROGRAM_EXTENSION_REQUIRED',
    );
  });

  it('fails inconclusive when F03 lacks a recognized repair blocker semantic', () => {
    const projection = projectLifecycle('REPAIR_REQUIRED', [
      fact('missing-blocker', 1, 'repair.scope_or_budget_expansion_required'),
    ]);

    expect(projection.state).toBe('INCONCLUSIVE');
    expect(projection.terminalReason).toBe('repair_blocker_kind_required');
  });
});

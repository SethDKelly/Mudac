import { isDeepStrictEqual } from 'node:util';

import type {
  GuardDecision,
  HumanAuthorityKind,
  LifecycleFact,
  LifecycleState,
  ProjectionResult,
  ProjectionTraceEntry,
  RepairBlockerKind,
} from './model.js';

interface Transition {
  eventType: string;
  from: readonly LifecycleState[];
  to: LifecycleState;
  requiredHumanAuthorityKind?: HumanAuthorityKind;
}

const transition = (
  eventType: string,
  from: LifecycleState | readonly LifecycleState[],
  to: LifecycleState,
  requiredHumanAuthorityKind?: HumanAuthorityKind,
): Transition => ({
  eventType,
  from: Array.isArray(from) ? from : [from],
  to,
  ...(requiredHumanAuthorityKind ? { requiredHumanAuthorityKind } : {}),
});

const transitions: readonly Transition[] = [
  transition('start_gate.ready', 'PLANNING_READY', 'START_GATE_READY'),
  transition('start_gate.pass', 'START_GATE_READY', 'AWAITING_G2'),
  transition('authority.g2_granted', 'AWAITING_G2', 'G2_AUTHORIZED', 'G2'),
  transition('workspace.provision_requested', 'G2_AUTHORIZED', 'WORKSPACE_PROVISIONING'),
  transition('workspace.provisioned', 'WORKSPACE_PROVISIONING', 'IMPLEMENTING'),
  transition('candidate.registered', 'IMPLEMENTING', 'CANDIDATE_REGISTERED'),
  transition('verification.started', 'CANDIDATE_REGISTERED', 'VERIFYING'),
  transition('verification.pass', 'VERIFYING', 'AWAITING_INDEPENDENT_REVIEW'),
  transition(
    'review.independent.pass',
    'AWAITING_INDEPENDENT_REVIEW',
    'AWAITING_ADVERSARIAL_REVIEW',
  ),
  transition('review.adversarial.pass', 'AWAITING_ADVERSARIAL_REVIEW', 'AWAITING_PR_CI'),
  transition('github.check.required_set_pass', 'AWAITING_PR_CI', 'AWAITING_G5'),
  transition('gate.g5.pass', 'AWAITING_G5', 'AWAITING_HUMAN_MERGE'),
  transition(
    'failure.changes_required_within_existing_g2',
    [
      'VERIFYING',
      'AWAITING_INDEPENDENT_REVIEW',
      'AWAITING_ADVERSARIAL_REVIEW',
      'AWAITING_PR_CI',
      'AWAITING_G5',
    ],
    'REPAIR_REQUIRED',
  ),
  transition('repair.resume', 'REPAIR_REQUIRED', 'IMPLEMENTING'),
  transition('repair.scope_or_budget_expansion_required', 'REPAIR_REQUIRED', 'BLOCKED'),
  transition('invalidation.review_required', 'AWAITING_HUMAN_MERGE', 'AWAITING_INDEPENDENT_REVIEW'),
  transition(
    'github.pull_request.merged_after_human_approval',
    'AWAITING_HUMAN_MERGE',
    'INTEGRATION_VERIFYING',
    'PROTECTED_IMPLEMENTATION_MERGE',
  ),
  transition('integration.pass', 'INTEGRATION_VERIFYING', 'AWAITING_CLOSURE_MERGE'),
  transition(
    'closure.merged_after_human_approval',
    'AWAITING_CLOSURE_MERGE',
    'COMPLETE',
    'CLOSURE_MERGE',
  ),
  transition('invalidation.material_confirmed', 'COMPLETE', 'REOPEN_REQUIRED'),
  transition('authority.reopen_g2_granted', 'REOPEN_REQUIRED', 'G2_AUTHORIZED', 'REOPEN_G2'),
  transition(
    'invalidation.disposition_completion_remains_valid',
    'REOPEN_REQUIRED',
    'COMPLETE',
    'COMPLETION_VALIDITY_DISPOSITION',
  ),
];

const nextActions: Readonly<Record<LifecycleState, readonly string[]>> = {
  IDLE: [],
  PLANNING_READY: ['start_gate.ready'],
  START_GATE_READY: ['start_gate.pass'],
  AWAITING_G2: ['authority.g2_granted'],
  G2_AUTHORIZED: ['workspace.provision_requested'],
  WORKSPACE_PROVISIONING: ['workspace.provisioned'],
  IMPLEMENTING: ['candidate.registered'],
  CANDIDATE_REGISTERED: ['verification.started'],
  VERIFYING: ['verification.pass', 'failure.changes_required_within_existing_g2'],
  AWAITING_INDEPENDENT_REVIEW: [
    'review.independent.pass',
    'failure.changes_required_within_existing_g2',
  ],
  REPAIR_REQUIRED: ['repair.resume', 'repair.scope_or_budget_expansion_required'],
  AWAITING_ADVERSARIAL_REVIEW: [
    'review.adversarial.pass',
    'failure.changes_required_within_existing_g2',
  ],
  AWAITING_PR_CI: ['github.check.required_set_pass', 'failure.changes_required_within_existing_g2'],
  AWAITING_G5: ['gate.g5.pass', 'failure.changes_required_within_existing_g2'],
  AWAITING_HUMAN_MERGE: [
    'github.pull_request.merged_after_human_approval',
    'invalidation.review_required',
  ],
  INTEGRATION_VERIFYING: ['integration.pass'],
  AWAITING_CLOSURE_MERGE: ['closure.merged_after_human_approval'],
  COMPLETE: ['invalidation.material_confirmed'],
  BLOCKED: [],
  INCONCLUSIVE: [],
  REOPEN_REQUIRED: [
    'authority.reopen_g2_granted',
    'invalidation.disposition_completion_remains_valid',
  ],
};

function terminal(
  state: LifecycleState,
  trace: ProjectionTraceEntry[],
  reason: string,
): ProjectionResult {
  return { state, eligibleNextActions: nextActions[state], trace, terminalReason: reason };
}

function isGuardDecision(value: unknown): value is GuardDecision {
  return value === 'PASS' || value === 'BLOCKED' || value === 'INCONCLUSIVE';
}

function isRepairBlockerKind(value: unknown): value is RepairBlockerKind {
  return value === 'SCOPE_EXPANSION' || value === 'BUDGET_EXHAUSTED';
}

function hasRequiredFactEnvelope(fact: LifecycleFact): boolean {
  return (
    typeof fact.factId === 'string' &&
    fact.factId.trim().length > 0 &&
    typeof fact.factType === 'string' &&
    fact.factType.trim().length > 0 &&
    typeof fact.payloadDigest === 'string' &&
    fact.payloadDigest.trim().length > 0 &&
    typeof fact.payload === 'object' &&
    fact.payload !== null &&
    typeof fact.payload.eventType === 'string' &&
    fact.payload.eventType.trim().length > 0
  );
}

export function projectLifecycle(
  initialState: LifecycleState,
  inputFacts: readonly LifecycleFact[],
): ProjectionResult {
  if (inputFacts.some((fact) => !Number.isFinite(fact.logicalOrder))) {
    return terminal('INCONCLUSIVE', [], 'invalid_logical_order');
  }
  if (inputFacts.some((fact) => !hasRequiredFactEnvelope(fact))) {
    return terminal('INCONCLUSIVE', [], 'invalid_fact_envelope');
  }

  const facts = [...inputFacts].sort(
    (left, right) =>
      left.logicalOrder - right.logicalOrder || left.factId.localeCompare(right.factId),
  );
  const trace: ProjectionTraceEntry[] = [];
  const seenFacts = new Map<string, LifecycleFact>();
  let state = initialState;
  let previousLogicalOrder: number | undefined;
  let previousFactId: string | undefined;

  for (const fact of facts) {
    const seen = seenFacts.get(fact.factId);
    if (seen) {
      if (!isDeepStrictEqual(seen, fact)) {
        trace.push({
          factId: fact.factId,
          eventType: fact.payload.eventType,
          stateBefore: state,
          stateAfter: 'INCONCLUSIVE',
          disposition: 'INCONCLUSIVE',
          reason: 'duplicate_event_identity_has_conflicting_fact_contents',
        });
        return terminal('INCONCLUSIVE', trace, 'conflicting_duplicate_event');
      }
      trace.push({
        factId: fact.factId,
        eventType: fact.payload.eventType,
        stateBefore: state,
        stateAfter: state,
        disposition: 'IDEMPOTENT_NOOP',
        reason: 'duplicate_event_identity_same_fact',
      });
      continue;
    }
    seenFacts.set(fact.factId, structuredClone(fact));

    if (
      previousLogicalOrder === fact.logicalOrder &&
      previousFactId !== undefined &&
      previousFactId !== fact.factId
    ) {
      trace.push({
        factId: fact.factId,
        eventType: fact.payload.eventType,
        stateBefore: state,
        stateAfter: 'INCONCLUSIVE',
        disposition: 'INCONCLUSIVE',
        reason: 'ambiguous_logical_order',
      });
      return terminal('INCONCLUSIVE', trace, 'ambiguous_logical_order');
    }
    previousLogicalOrder = fact.logicalOrder;
    previousFactId = fact.factId;

    if (!isGuardDecision(fact.payload.guardDecision)) {
      trace.push({
        factId: fact.factId,
        eventType: fact.payload.eventType,
        stateBefore: state,
        stateAfter: 'INCONCLUSIVE',
        disposition: 'INCONCLUSIVE',
        reason: 'missing_or_invalid_guard_decision',
      });
      return terminal('INCONCLUSIVE', trace, 'missing_or_invalid_guard_decision');
    }

    if (fact.payload.stale === true) {
      trace.push({
        factId: fact.factId,
        eventType: fact.payload.eventType,
        stateBefore: state,
        stateAfter: state,
        disposition: 'HISTORICAL_NO_ADVANCE',
        reason: 'stale_or_superseded_subject',
      });
      continue;
    }

    const candidates = transitions.filter((item) => item.eventType === fact.payload.eventType);
    if (candidates.length === 0) {
      trace.push({
        factId: fact.factId,
        eventType: fact.payload.eventType,
        stateBefore: state,
        stateAfter: 'INCONCLUSIVE',
        disposition: 'INCONCLUSIVE',
        reason: 'unknown_event_type',
      });
      return terminal('INCONCLUSIVE', trace, 'unknown_event_type');
    }

    const selected = candidates.find((item) => item.from.includes(state));
    if (!selected) {
      trace.push({
        factId: fact.factId,
        eventType: fact.payload.eventType,
        stateBefore: state,
        stateAfter: 'INCONCLUSIVE',
        disposition: 'INCONCLUSIVE',
        reason: 'event_not_valid_from_current_state',
      });
      return terminal('INCONCLUSIVE', trace, 'out_of_order_or_contradictory_event');
    }

    if (fact.payload.guardDecision === 'BLOCKED') {
      trace.push({
        factId: fact.factId,
        eventType: fact.payload.eventType,
        stateBefore: state,
        stateAfter: 'BLOCKED',
        disposition: 'BLOCKED',
        reason: 'transition_guard_blocked',
      });
      return terminal('BLOCKED', trace, 'transition_guard_blocked');
    }
    if (fact.payload.guardDecision === 'INCONCLUSIVE') {
      trace.push({
        factId: fact.factId,
        eventType: fact.payload.eventType,
        stateBefore: state,
        stateAfter: 'INCONCLUSIVE',
        disposition: 'INCONCLUSIVE',
        reason: 'transition_guard_inconclusive',
      });
      return terminal('INCONCLUSIVE', trace, 'transition_guard_inconclusive');
    }

    if (fact.payload.eventType === 'repair.scope_or_budget_expansion_required') {
      if (!isRepairBlockerKind(fact.payload.repairBlocker)) {
        trace.push({
          factId: fact.factId,
          eventType: fact.payload.eventType,
          stateBefore: state,
          stateAfter: 'INCONCLUSIVE',
          disposition: 'INCONCLUSIVE',
          reason: 'repair_blocker_kind_required',
        });
        return terminal('INCONCLUSIVE', trace, 'repair_blocker_kind_required');
      }

      const reason =
        fact.payload.repairBlocker === 'SCOPE_EXPANSION'
          ? 'repair_scope_expansion_requires_human_disposition_or_reauthorization'
          : 'repair_budget_exhausted_requires_human_program_extension';
      trace.push({
        factId: fact.factId,
        eventType: fact.payload.eventType,
        stateBefore: state,
        stateAfter: 'BLOCKED',
        disposition: 'BLOCKED',
        reason,
      });
      return terminal('BLOCKED', trace, reason);
    }

    if (selected.requiredHumanAuthorityKind) {
      if (
        typeof fact.payload.humanAuthorityRef !== 'string' ||
        fact.payload.humanAuthorityRef.trim().length === 0 ||
        fact.payload.humanAuthorityKind !== selected.requiredHumanAuthorityKind
      ) {
        trace.push({
          factId: fact.factId,
          eventType: fact.payload.eventType,
          stateBefore: state,
          stateAfter: 'BLOCKED',
          disposition: 'BLOCKED',
          reason: 'matching_human_authority_required',
        });
        return terminal('BLOCKED', trace, 'matching_human_authority_required');
      }
    }

    const stateBefore = state;
    state = selected.to;
    trace.push({
      factId: fact.factId,
      eventType: fact.payload.eventType,
      stateBefore,
      stateAfter: state,
      disposition: 'APPLIED',
      reason: selected.requiredHumanAuthorityKind
        ? 'matching_human_authority_observed'
        : 'guards_passed',
    });
  }

  return { state, eligibleNextActions: nextActions[state], trace };
}

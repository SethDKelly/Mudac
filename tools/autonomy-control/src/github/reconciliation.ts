import { createHash } from 'node:crypto';

import { projectLifecycle } from '../lifecycle.js';
import type { LifecycleFact, LifecycleState } from '../model.js';
import { evaluateRequiredChecks } from './checks.js';
import type {
  DeliveryEnvelope,
  GitHubTruthSnapshot,
  ShadowDivergence,
  ShadowObservation,
  ShadowTarget,
} from './model.js';

export type DeliveryTruthDisposition =
  'CURRENT_NOTIFICATION' | 'HISTORICAL_NO_ADVANCE' | 'RECORD_NO_ADVANCE';

const lifecycleRank: Readonly<Partial<Record<LifecycleState, number>>> = {
  IDLE: 0,
  PLANNING_READY: 1,
  START_GATE_READY: 2,
  AWAITING_G2: 3,
  G2_AUTHORIZED: 4,
  WORKSPACE_PROVISIONING: 5,
  IMPLEMENTING: 6,
  CANDIDATE_REGISTERED: 7,
  VERIFYING: 8,
  AWAITING_INDEPENDENT_REVIEW: 9,
  REPAIR_REQUIRED: 9,
  AWAITING_ADVERSARIAL_REVIEW: 10,
  AWAITING_PR_CI: 11,
  AWAITING_G5: 12,
  AWAITING_HUMAN_MERGE: 13,
  INTEGRATION_VERIFYING: 14,
  AWAITING_CLOSURE_MERGE: 15,
  COMPLETE: 16,
};

function digest(value: unknown): string {
  return createHash('sha256').update(JSON.stringify(value)).digest('hex');
}

function sameSet(left: readonly string[], right: readonly string[]): boolean {
  const a = [...new Set(left)].sort();
  const b = [...new Set(right)].sort();
  return a.length === b.length && a.every((item, index) => item === b[index]);
}

function nextLogicalOrder(facts: readonly LifecycleFact[]): number | undefined {
  if (facts.length === 0) return 0;
  const max = Math.max(...facts.map((fact) => fact.logicalOrder));
  if (!Number.isFinite(max) || max >= Number.MAX_SAFE_INTEGER) return undefined;
  return Math.floor(max) + 1;
}

export function classifyDeliveryAgainstTruth(
  delivery: DeliveryEnvelope,
  truth: GitHubTruthSnapshot,
): DeliveryTruthDisposition {
  if (delivery.eventFamily === 'unknown') return 'RECORD_NO_ADVANCE';
  if (delivery.pullRequestNumber && delivery.pullRequestNumber !== truth.pullRequest.number) {
    return 'HISTORICAL_NO_ADVANCE';
  }
  if (delivery.payloadHeadSha && delivery.payloadHeadSha !== truth.pullRequest.headSha) {
    return 'HISTORICAL_NO_ADVANCE';
  }
  return 'CURRENT_NOTIFICATION';
}

export function reconcileShadowTruth(
  observationId: string,
  target: ShadowTarget,
  truth: GitHubTruthSnapshot,
): ShadowObservation {
  const before = projectLifecycle(target.initialLifecycleState, target.lifecycleFacts);
  const divergences: ShadowDivergence[] = [];

  const headMatches = truth.pullRequest.headSha === target.candidateSha;
  const baseMatches = truth.pullRequest.baseSha === target.expectedBaseSha;

  if (!headMatches) {
    divergences.push({
      kind: 'HEAD_DRIFT',
      severity: 'BLOCKING',
      explanation: `current PR head ${truth.pullRequest.headSha} differs from target ${target.candidateSha}`,
      disposition: 'FREEZE_OPTIMISTIC_ADVANCEMENT_AND_ROUTE_R_C_DELTA_CLASSIFICATION',
    });
  }

  if (!baseMatches) {
    divergences.push({
      kind: 'BASE_DRIFT',
      severity: 'BLOCKING',
      explanation: `current PR base SHA ${truth.pullRequest.baseSha} differs from expected ${target.expectedBaseSha}`,
      disposition: 'RECONCILE_READ_ONLY_NO_SYNCHRONIZATION_WRITE',
    });
  }

  const requiredChecks = evaluateRequiredChecks(
    truth.checks,
    truth.workflows,
    target.candidateSha,
    target.requiredCheckNames,
  );

  if (requiredChecks.disposition === 'INCONCLUSIVE') {
    divergences.push({
      kind: 'AMBIGUOUS_REQUIRED_CHECK_TRUTH',
      severity: 'BLOCKING',
      explanation: requiredChecks.reason,
      disposition: 'NO_CI_PASS_TRANSITION_RECONCILIATION_REQUIRED',
    });
  }

  let derivedLifecycleFact: LifecycleFact | undefined;
  let after = before;

  if (
    headMatches &&
    baseMatches &&
    requiredChecks.disposition === 'PASS' &&
    before.state === 'AWAITING_PR_CI'
  ) {
    const logicalOrder = nextLogicalOrder(target.lifecycleFacts);
    if (logicalOrder === undefined) {
      divergences.push({
        kind: 'MANDATORY_TRUTH_UNAVAILABLE',
        severity: 'BLOCKING',
        explanation: 'cannot allocate an unambiguous finite logical order for reconciled CI fact',
        disposition: 'INCONCLUSIVE_NO_ADVANCEMENT',
      });
    } else {
      const payload = {
        eventType: 'github.check.required_set_pass',
        guardDecision: 'PASS' as const,
        subjectSha: target.candidateSha,
      };
      derivedLifecycleFact = {
        factId: `github-required-set:${target.candidateSha}:${digest(requiredChecks.matched).slice(0, 16)}`,
        factType: 'GITHUB_RECONCILED_REQUIRED_CHECK_SET',
        logicalOrder,
        payloadDigest: digest(payload),
        payload,
      };
      after = projectLifecycle(target.initialLifecycleState, [
        ...target.lifecycleFacts,
        derivedLifecycleFact,
      ]);
    }
  }

  if (truth.pullRequest.merged) {
    if (!truth.pullRequest.mergeCommitSha || truth.mergeCommitInBase !== true) {
      divergences.push({
        kind: 'MANDATORY_TRUTH_UNAVAILABLE',
        severity: 'BLOCKING',
        explanation:
          'PR reports merged but integration identity/base ancestry is not fully reconciled',
        disposition: 'MERGE_NOTIFICATION_INSUFFICIENT_RECONCILIATION_REQUIRED',
      });
    }
  }

  if (target.expectedLifecycleState && after.state !== target.expectedLifecycleState) {
    const projectedRank = lifecycleRank[after.state];
    const expectedRank = lifecycleRank[target.expectedLifecycleState];
    const unsafeAdvance =
      projectedRank !== undefined && expectedRank !== undefined && projectedRank > expectedRank;
    divergences.push({
      kind: unsafeAdvance ? 'UNSAFE_ADVANCEMENT_PREDICTION' : 'STATE_DIVERGENCE',
      severity: unsafeAdvance ? 'BLOCKING' : 'RECORD_ONLY',
      explanation: `projected lifecycle state ${after.state} differs from authoritative coordination state ${target.expectedLifecycleState}`,
      disposition: unsafeAdvance
        ? 'BLOCK_ACCEPTANCE_UNTIL_DISPOSITIONED'
        : 'RECORD_EXPLAIN_AND_DISPOSITION',
    });
  }

  if (
    target.expectedNextActions &&
    !sameSet(after.eligibleNextActions, target.expectedNextActions)
  ) {
    divergences.push({
      kind: 'NEXT_ACTION_DIVERGENCE',
      severity: 'RECORD_ONLY',
      explanation: `projected next actions ${after.eligibleNextActions.join(',')} differ from authoritative coordination next actions ${target.expectedNextActions.join(',')}`,
      disposition: 'RECORD_EXPLAIN_AND_DISPOSITION',
    });
  }

  return {
    observationId,
    observedAt: truth.observedAt,
    targetCandidateSha: target.candidateSha,
    truth,
    requiredChecks,
    projectionBeforeReconciliation: before,
    projectionAfterReconciliation: after,
    ...(derivedLifecycleFact ? { derivedLifecycleFact } : {}),
    divergences,
    blocking: divergences.some((item) => item.severity === 'BLOCKING'),
  };
}

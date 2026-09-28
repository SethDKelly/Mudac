import { classifyRevisionDelta } from './evidence.js';
import { AppendOnlyFactStore } from './fact-store.js';
import { projectLifecycle } from './lifecycle.js';
import { phase021Identity } from './replay.js';
import type {
  GuardDecision,
  HumanAuthorityKind,
  LifecycleFact,
  RepairBlockerKind,
} from './model.js';

export type AutFailureStage =
  'AUT-001-A' | 'AUT-001-B' | 'AUT-001-C' | 'AUT-001-D' | 'AUT-001-E' | 'AUT-001-F' | 'AUT-001-G';

export type FailureCaseId =
  | 'FI-01'
  | 'FI-02'
  | 'FI-03'
  | 'FI-04'
  | 'FI-05'
  | 'FI-06'
  | 'FI-07'
  | 'FI-08'
  | 'FI-09'
  | 'FI-10'
  | 'FI-11'
  | 'FI-12'
  | 'FI-13'
  | 'FI-14'
  | 'FI-15'
  | 'FI-16'
  | 'FI-17'
  | 'FI-18'
  | 'FI-19'
  | 'FI-20'
  | 'FI-21'
  | 'FI-22'
  | 'FI-23'
  | 'FI-24'
  | 'FI-25'
  | 'FI-26'
  | 'FI-27'
  | 'FI-28';

export interface FailureCaseDefinition {
  id: FailureCaseId;
  injection: string;
  stageA: 'EXECUTABLE_IN_A' | 'DEFERRED';
  deferredTo?: readonly AutFailureStage[];
}

export interface FailureExecutionResult {
  id: FailureCaseId;
  injection: string;
  status: 'EXECUTED' | 'DEFERRED';
  observedDisposition?: string;
  deferredTo?: readonly AutFailureStage[];
}

export const failureCaseMatrix: readonly FailureCaseDefinition[] = [
  { id: 'FI-01', injection: 'duplicate_delivery_same_payload', stageA: 'EXECUTABLE_IN_A' },
  { id: 'FI-02', injection: 'duplicate_delivery_conflicting_payload', stageA: 'EXECUTABLE_IN_A' },
  {
    id: 'FI-03',
    injection: 'late_success_check_for_superseded_candidate',
    stageA: 'EXECUTABLE_IN_A',
  },
  {
    id: 'FI-04',
    injection: 'out_of_order_merge_notification_without_reconciled_current_truth',
    stageA: 'EXECUTABLE_IN_A',
  },
  { id: 'FI-05', injection: 'pr_head_moves_after_review_or_g5', stageA: 'EXECUTABLE_IN_A' },
  {
    id: 'FI-06',
    injection: 'changed_path_not_mapped_to_material_surface',
    stageA: 'EXECUTABLE_IN_A',
  },
  {
    id: 'FI-07',
    injection: 'independent_reviewer_reuses_implementer_run_or_worktree',
    stageA: 'DEFERRED',
    deferredTo: ['AUT-001-C', 'AUT-001-G'],
  },
  {
    id: 'FI-08',
    injection: 'adversarial_review_reuses_prior_review_session',
    stageA: 'DEFERRED',
    deferredTo: ['AUT-001-C', 'AUT-001-G'],
  },
  {
    id: 'FI-09',
    injection: 'reviewer_edits_candidate',
    stageA: 'DEFERRED',
    deferredTo: ['AUT-001-C', 'AUT-001-G'],
  },
  {
    id: 'FI-10',
    injection: 'dispatch_uses_stale_authority_digest',
    stageA: 'DEFERRED',
    deferredTo: ['AUT-001-C', 'AUT-001-D'],
  },
  { id: 'FI-11', injection: 'repair_requires_scope_expansion', stageA: 'EXECUTABLE_IN_A' },
  { id: 'FI-12', injection: 'repair_budget_exhausted', stageA: 'EXECUTABLE_IN_A' },
  {
    id: 'FI-13',
    injection: 'generic_shell_git_github_http_sql_or_cloud_capability_requested',
    stageA: 'DEFERRED',
    deferredTo: ['AUT-001-D', 'AUT-001-G'],
  },
  {
    id: 'FI-14',
    injection: 'production_target_selected_through_development_control',
    stageA: 'DEFERRED',
    deferredTo: ['AUT-001-D', 'AUT-001-G'],
  },
  {
    id: 'FI-15',
    injection: 'production_target_selected_through_test_control',
    stageA: 'DEFERRED',
    deferredTo: ['AUT-001-F', 'AUT-001-G'],
  },
  {
    id: 'FI-16',
    injection: 'passing_test_control_run_attempts_to_advance_implementation_state',
    stageA: 'DEFERRED',
    deferredTo: ['AUT-001-F', 'AUT-001-G'],
  },
  {
    id: 'FI-17',
    injection: 'same_operation_id_conflicting_request_digest',
    stageA: 'DEFERRED',
    deferredTo: ['AUT-001-D', 'AUT-001-E', 'AUT-001-G'],
  },
  {
    id: 'FI-18',
    injection: 'serialized_surface_conflict',
    stageA: 'DEFERRED',
    deferredTo: ['AUT-001-C', 'AUT-001-E', 'AUT-001-G'],
  },
  {
    id: 'FI-19',
    injection: 'github_write_precondition_subject_changed',
    stageA: 'DEFERRED',
    deferredTo: ['AUT-001-B', 'AUT-001-E', 'AUT-001-G'],
  },
  {
    id: 'FI-20',
    injection: 'required_check_missing_running_cancelled_or_failed',
    stageA: 'EXECUTABLE_IN_A',
  },
  {
    id: 'FI-21',
    injection: 'mandatory_evidence_retry_until_green',
    stageA: 'DEFERRED',
    deferredTo: ['AUT-001-E', 'AUT-001-G'],
  },
  {
    id: 'FI-22',
    injection: 'g5_complete_attempts_automatic_protected_merge',
    stageA: 'EXECUTABLE_IN_A',
  },
  {
    id: 'FI-23',
    injection: 'merge_or_completion_event_attempts_to_authorize_phase022',
    stageA: 'EXECUTABLE_IN_A',
  },
  {
    id: 'FI-24',
    injection: 'post_completion_material_invalidation',
    stageA: 'EXECUTABLE_IN_A',
  },
  {
    id: 'FI-25',
    injection: 'secret_or_protected_credential_retrieval',
    stageA: 'DEFERRED',
    deferredTo: ['AUT-001-D', 'AUT-001-F', 'AUT-001-G'],
  },
  {
    id: 'FI-26',
    injection: 'missed_webhook_or_control_plane_restart',
    stageA: 'DEFERRED',
    deferredTo: ['AUT-001-B', 'AUT-001-G'],
  },
  {
    id: 'FI-27',
    injection: 'test_control_fault_or_cleanup_state_unresolved',
    stageA: 'DEFERRED',
    deferredTo: ['AUT-001-F', 'AUT-001-G'],
  },
  {
    id: 'FI-28',
    injection:
      'same_provider_used_for_implementer_and_reviews_but_distinct_role_bound_fresh_sessions',
    stageA: 'DEFERRED',
    deferredTo: ['AUT-001-C', 'AUT-001-G'],
  },
] as const;

function lifecycleFact(
  factId: string,
  eventType: string,
  options: {
    guardDecision?: GuardDecision;
    stale?: boolean;
    humanAuthorityRef?: string;
    humanAuthorityKind?: HumanAuthorityKind;
    repairBlocker?: RepairBlockerKind;
  } = {},
): LifecycleFact {
  return {
    factId,
    factType: 'failure-injection',
    logicalOrder: 1,
    payloadDigest: `${factId}:${eventType}`,
    payload: {
      eventType,
      guardDecision: options.guardDecision ?? 'PASS',
      ...(options.stale === true ? { stale: true } : {}),
      ...(options.humanAuthorityRef ? { humanAuthorityRef: options.humanAuthorityRef } : {}),
      ...(options.humanAuthorityKind ? { humanAuthorityKind: options.humanAuthorityKind } : {}),
      ...(options.repairBlocker ? { repairBlocker: options.repairBlocker } : {}),
    },
  };
}

function executed(
  definition: FailureCaseDefinition,
  observedDisposition: string,
): FailureExecutionResult {
  return {
    id: definition.id,
    injection: definition.injection,
    status: 'EXECUTED',
    observedDisposition,
  };
}

export function executeStageAFailureCase(id: FailureCaseId): FailureExecutionResult {
  const definition = failureCaseMatrix.find((item) => item.id === id);
  if (!definition) throw new Error(`unknown failure case: ${id}`);
  if (definition.stageA === 'DEFERRED') {
    return {
      id: definition.id,
      injection: definition.injection,
      status: 'DEFERRED',
      ...(definition.deferredTo ? { deferredTo: definition.deferredTo } : {}),
    };
  }

  switch (id) {
    case 'FI-01': {
      const store = new AppendOnlyFactStore<{ value: number }>();
      const fact = {
        factId: 'delivery-1',
        factType: 'delivery',
        logicalOrder: 1,
        payloadDigest: 'digest-1',
        payload: { value: 1 },
      };
      store.append(fact);
      return executed(definition, store.append(structuredClone(fact)).status);
    }
    case 'FI-02': {
      const store = new AppendOnlyFactStore<{ value: number }>();
      const fact = {
        factId: 'delivery-1',
        factType: 'delivery',
        logicalOrder: 1,
        payloadDigest: 'same-digest-label',
        payload: { value: 1 },
      };
      store.append(fact);
      const conflict = store.append({ ...fact, payload: { value: 2 } });
      return executed(
        definition,
        conflict.status === 'CONFLICT' ? 'INCONCLUSIVE_SECURITY_RECONCILIATION' : conflict.status,
      );
    }
    case 'FI-03': {
      const projection = projectLifecycle('AWAITING_PR_CI', [
        lifecycleFact('late-check', 'github.check.required_set_pass', { stale: true }),
      ]);
      const historical = projection.trace[0]?.disposition === 'HISTORICAL_NO_ADVANCE';
      return executed(
        definition,
        projection.state === 'AWAITING_PR_CI' && historical
          ? 'HISTORICAL_NO_CURRENT_TRANSITION'
          : 'UNEXPECTED_ADVANCE',
      );
    }
    case 'FI-04': {
      const projection = projectLifecycle('AWAITING_PR_CI', [
        lifecycleFact('late-merge', 'github.pull_request.merged_after_human_approval', {
          humanAuthorityRef: 'human-merge',
          humanAuthorityKind: 'PROTECTED_IMPLEMENTATION_MERGE',
        }),
      ]);
      return executed(
        definition,
        projection.state === 'INCONCLUSIVE' ? 'RECONCILE_OR_INCONCLUSIVE' : projection.state,
      );
    }
    case 'FI-05': {
      const classification = classifyRevisionDelta({
        oldRevision: phase021Identity.repairedCandidate,
        newRevision: phase021Identity.reboundHead,
        changedSurfaces: [
          {
            surfaceId: 'authority-delta',
            surfaceClass: 'AUTHORITY_GOVERNANCE_MATERIAL',
            mapped: true,
          },
        ],
      });
      const projection = projectLifecycle('AWAITING_HUMAN_MERGE', [
        lifecycleFact('head-drift', 'invalidation.review_required'),
      ]);
      return executed(
        definition,
        classification.classification === 'GOVERNANCE_MATERIAL_DELTA' &&
          projection.state === 'AWAITING_INDEPENDENT_REVIEW'
          ? 'FREEZE_MERGE_AND_R_C_DELTA_CLASSIFY'
          : 'UNEXPECTED_HEAD_DRIFT_DISPOSITION',
      );
    }
    case 'FI-06': {
      const classification = classifyRevisionDelta({
        oldRevision: phase021Identity.initialCandidate,
        newRevision: phase021Identity.repairedCandidate,
        changedSurfaces: [
          { surfaceId: 'unmapped', surfaceClass: 'EXECUTABLE_MATERIAL', mapped: false },
        ],
      });
      return executed(
        definition,
        classification.classification === 'INCONCLUSIVE'
          ? 'INCONCLUSIVE_FAIL_CLOSED'
          : classification.classification,
      );
    }
    case 'FI-11': {
      const projection = projectLifecycle('REPAIR_REQUIRED', [
        lifecycleFact('scope-expansion', 'repair.scope_or_budget_expansion_required', {
          repairBlocker: 'SCOPE_EXPANSION',
        }),
      ]);
      return executed(
        definition,
        projection.state === 'BLOCKED' &&
          projection.terminalReason ===
            'repair_scope_expansion_requires_human_disposition_or_reauthorization'
          ? 'BLOCKED_HUMAN_DISPOSITION_OR_REAUTHORIZATION'
          : projection.terminalReason ?? projection.state,
      );
    }
    case 'FI-12': {
      const projection = projectLifecycle('REPAIR_REQUIRED', [
        lifecycleFact('budget-exhausted', 'repair.scope_or_budget_expansion_required', {
          repairBlocker: 'BUDGET_EXHAUSTED',
        }),
      ]);
      return executed(
        definition,
        projection.state === 'BLOCKED' &&
          projection.terminalReason === 'repair_budget_exhausted_requires_human_program_extension'
          ? 'BLOCKED_HUMAN_PROGRAM_EXTENSION_REQUIRED'
          : projection.terminalReason ?? projection.state,
      );
    }
    case 'FI-20': {
      const projection = projectLifecycle('AWAITING_PR_CI', []);
      return executed(
        definition,
        projection.state === 'AWAITING_PR_CI' ? 'NO_REQUIRED_CI_PASS_TRANSITION' : projection.state,
      );
    }
    case 'FI-22': {
      const projection = projectLifecycle('AWAITING_G5', [
        lifecycleFact('g5-pass', 'gate.g5.pass'),
      ]);
      return executed(
        definition,
        projection.state === 'AWAITING_HUMAN_MERGE' ? 'AWAIT_HUMAN_MERGE' : projection.state,
      );
    }
    case 'FI-23': {
      const projection = projectLifecycle('COMPLETE', [
        lifecycleFact('phase022-attempt', 'authority.phase022_granted'),
      ]);
      return executed(
        definition,
        projection.state === 'INCONCLUSIVE' ? 'DENY_NO_AUTHORITY_SYNTHESIS' : projection.state,
      );
    }
    case 'FI-24': {
      const projection = projectLifecycle('COMPLETE', [
        lifecycleFact('post-completion-invalidation', 'invalidation.material_confirmed'),
      ]);
      return executed(
        definition,
        projection.state === 'REOPEN_REQUIRED'
          ? 'REOPEN_REQUIRED_OLD_G2_NOT_RESTORED'
          : projection.state,
      );
    }
    default:
      throw new Error(`Stage-A executable case has no executor: ${id}`);
  }
}

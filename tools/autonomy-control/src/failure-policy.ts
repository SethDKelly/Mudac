export const failurePolicies = {
  duplicate_delivery_same_payload: 'IDEMPOTENT_NOOP',
  duplicate_delivery_conflicting_payload: 'INCONCLUSIVE_SECURITY_RECONCILIATION',
  late_success_check_for_superseded_candidate: 'HISTORICAL_NO_CURRENT_TRANSITION',
  out_of_order_merge_notification_without_reconciled_current_truth: 'RECONCILE_OR_INCONCLUSIVE',
  pr_head_moves_after_review_or_g5: 'FREEZE_MERGE_AND_R_C_DELTA_CLASSIFY',
  changed_path_not_mapped_to_material_surface: 'INCONCLUSIVE_FAIL_CLOSED',
  independent_reviewer_reuses_implementer_run_or_worktree: 'REVIEW_INDEPENDENCE_NOT_PROVEN_REJECT',
  adversarial_review_reuses_prior_review_session: 'FRESHNESS_NOT_PROVEN_REJECT_OR_INCONCLUSIVE',
  reviewer_edits_candidate: 'ROLE_CONVERTS_TO_IMPLEMENTER_AND_FRESH_REVIEW_REQUIRED',
  dispatch_uses_stale_authority_digest: 'REJECT_RECONCILE_AUTHORITY',
  repair_requires_scope_expansion: 'BLOCKED_HUMAN_DISPOSITION_OR_REAUTHORIZATION',
  repair_budget_exhausted: 'BLOCKED_HUMAN_PROGRAM_EXTENSION_REQUIRED',
  generic_shell_git_github_http_sql_or_cloud_capability_requested: 'DENY_UNSUPPORTED_CAPABILITY',
  production_target_selected_through_development_control: 'DENY_HARD',
  production_target_selected_through_test_control: 'DENY_HARD_FAIL_CLOSED',
  passing_test_control_run_attempts_to_advance_implementation_state:
    'EVIDENCE_REFERENCE_ONLY_NO_DIRECT_TRANSITION',
  same_operation_id_conflicting_request_digest: 'INCONCLUSIVE',
  serialized_surface_conflict: 'BLOCKED_NO_SILENT_STEAL',
  github_write_precondition_subject_changed: 'RECONCILE_NO_FORCE_OVERWRITE',
  required_check_missing_running_cancelled_or_failed: 'NO_REQUIRED_CI_PASS_TRANSITION',
  mandatory_evidence_retry_until_green: 'FORBIDDEN_FAILURE_HISTORY_RETAINED',
  g5_complete_attempts_automatic_protected_merge: 'AWAIT_HUMAN_MERGE',
  merge_or_completion_event_attempts_to_authorize_phase022: 'DENY_NO_AUTHORITY_SYNTHESIS',
  post_completion_material_invalidation: 'REOPEN_REQUIRED_OLD_G2_NOT_RESTORED',
  secret_or_protected_credential_retrieval: 'DENY_HARD',
  missed_webhook_or_control_plane_restart:
    'RECONCILE_FROM_CURRENT_GITHUB_AND_IMMUTABLE_LOCAL_FACTS',
  test_control_fault_or_cleanup_state_unresolved: 'BLOCKED_OR_INCONCLUSIVE',
  same_provider_used_for_implementer_and_reviews_but_distinct_role_bound_fresh_sessions:
    'ALLOWED_IF_INDEPENDENCE_EVIDENCE_COMPLETE',
} as const;

export type FailureInjection = keyof typeof failurePolicies;
export type FailureDisposition = (typeof failurePolicies)[FailureInjection];

export function resolveFailureInjection(injection: string): string {
  if (Object.hasOwn(failurePolicies, injection)) {
    return failurePolicies[injection as FailureInjection];
  }
  return 'INCONCLUSIVE_UNKNOWN_FAILURE_INJECTION';
}

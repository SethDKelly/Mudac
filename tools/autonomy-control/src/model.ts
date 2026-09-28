export type LifecycleState =
  | 'IDLE'
  | 'PLANNING_READY'
  | 'START_GATE_READY'
  | 'AWAITING_G2'
  | 'G2_AUTHORIZED'
  | 'WORKSPACE_PROVISIONING'
  | 'IMPLEMENTING'
  | 'CANDIDATE_REGISTERED'
  | 'VERIFYING'
  | 'AWAITING_INDEPENDENT_REVIEW'
  | 'REPAIR_REQUIRED'
  | 'AWAITING_ADVERSARIAL_REVIEW'
  | 'AWAITING_PR_CI'
  | 'AWAITING_G5'
  | 'AWAITING_HUMAN_MERGE'
  | 'INTEGRATION_VERIFYING'
  | 'AWAITING_CLOSURE_MERGE'
  | 'COMPLETE'
  | 'BLOCKED'
  | 'INCONCLUSIVE'
  | 'REOPEN_REQUIRED';

export type GuardDecision = 'PASS' | 'BLOCKED' | 'INCONCLUSIVE';

export type HumanAuthorityKind =
  | 'G2'
  | 'PROTECTED_IMPLEMENTATION_MERGE'
  | 'CLOSURE_MERGE'
  | 'REOPEN_G2'
  | 'COMPLETION_VALIDITY_DISPOSITION';

export type RepairBlockerKind = 'SCOPE_EXPANSION' | 'BUDGET_EXHAUSTED';

export interface ImmutableFact<TPayload = unknown> {
  factId: string;
  factType: string;
  logicalOrder: number;
  payloadDigest: string;
  payload: TPayload;
}

export interface LifecycleEventPayload {
  eventType: string;
  guardDecision?: GuardDecision;
  subjectSha?: string;
  humanAuthorityRef?: string;
  humanAuthorityKind?: HumanAuthorityKind;
  repairBlocker?: RepairBlockerKind;
  stale?: boolean;
}

export type LifecycleFact = ImmutableFact<LifecycleEventPayload>;

export interface ProjectionTraceEntry {
  factId: string;
  eventType: string;
  stateBefore: LifecycleState;
  stateAfter: LifecycleState;
  disposition: 'APPLIED' | 'HISTORICAL_NO_ADVANCE' | 'IDEMPOTENT_NOOP' | 'BLOCKED' | 'INCONCLUSIVE';
  reason: string;
}

export interface ProjectionResult {
  state: LifecycleState;
  eligibleNextActions: readonly string[];
  trace: readonly ProjectionTraceEntry[];
  terminalReason?: string;
}

export type MaterialSurfaceClass =
  | 'EXECUTABLE_MATERIAL'
  | 'AUTHORITY_GOVERNANCE_MATERIAL'
  | 'CI_EVALUATOR_MATERIAL'
  | 'EVIDENCE_ONLY'
  | 'ROUTING_PROJECTION'
  | 'HISTORICAL_NONCURRENT';

export interface RevisionIdentity {
  sha: string;
  treeSha: string;
}

export interface ChangedSurface {
  surfaceId: string;
  surfaceClass: MaterialSurfaceClass;
  mapped: boolean;
}

export interface RevisionDeltaInput {
  oldRevision: RevisionIdentity;
  newRevision: RevisionIdentity;
  changedSurfaces: readonly ChangedSurface[];
}

export type RevisionClass =
  | 'IDENTICAL_REVISION'
  | 'PROVENANCE_ONLY_CHANGE'
  | 'NON_MATERIAL_TREE_CHANGE'
  | 'GOVERNANCE_MATERIAL_DELTA'
  | 'EVALUATOR_MATERIAL_DELTA'
  | 'EXECUTABLE_MATERIAL_DELTA'
  | 'MIXED_MATERIAL_DELTA'
  | 'INCONCLUSIVE';

export interface RevisionClassification {
  classification: RevisionClass;
  reusableEvidence: boolean;
  requiredActions: readonly string[];
  reason: string;
}

export interface EvidenceNode {
  evidenceId: string;
  subject: RevisionIdentity;
  materialBoundaryIds: readonly string[];
  contentDigest: string;
}

export interface EvidenceBinding {
  bindingId: string;
  evidenceId: string;
  originalSubject: RevisionIdentity;
  targetSubject: RevisionIdentity;
  reason: string;
}

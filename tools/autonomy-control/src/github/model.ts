import type { LifecycleFact, LifecycleState, ProjectionResult } from '../model.js';

export type GitHubEventFamily =
  'pull_request' | 'check_run' | 'check_suite' | 'workflow_run' | 'push' | 'unknown';

export interface DeliveryEnvelope {
  deliveryId: string;
  sourceIdentity: string;
  sourceType: 'WEBHOOK';
  repositoryId: number;
  repositoryFullName: string;
  eventFamily: GitHubEventFamily;
  action: string | null;
  receivedAt: string;
  signatureVerified: boolean;
  payloadDigest: string;
  pullRequestNumber?: number;
  ref?: string;
  payloadHeadSha?: string;
  payloadBaseSha?: string;
  checkRunId?: number;
  checkSuiteId?: number;
  workflowRunId?: number;
  workflowAttempt?: number;
  redelivery?: boolean;
}

export type GitHubSemanticFactType =
  'PR_HEAD' | 'PR_STATE' | 'PR_MERGE' | 'REF' | 'CHECK' | 'WORKFLOW';

export interface GitHubSemanticFact {
  factId: string;
  factType: GitHubSemanticFactType;
  observedAt: string;
  payloadDigest: string;
  payload: Record<string, unknown>;
}

export interface PullRequestTruth {
  number: number;
  state: 'open' | 'closed';
  merged: boolean;
  draft: boolean;
  headSha: string;
  baseRef: string;
  baseSha: string;
  mergeCommitSha: string | null;
}

export interface RefTruth {
  ref: string;
  sha: string;
}

export interface CheckTruth {
  id: number;
  name: string;
  headSha: string;
  status: 'queued' | 'in_progress' | 'completed';
  conclusion:
    | 'success'
    | 'failure'
    | 'cancelled'
    | 'timed_out'
    | 'action_required'
    | 'neutral'
    | 'skipped'
    | null;
  startedAt: string | null;
  completedAt: string | null;
}

export interface WorkflowTruth {
  id: number;
  name: string;
  headSha: string;
  attempt: number;
  status: 'queued' | 'in_progress' | 'completed';
  conclusion:
    | 'success'
    | 'failure'
    | 'cancelled'
    | 'timed_out'
    | 'action_required'
    | 'neutral'
    | 'skipped'
    | null;
}

export interface RulesetRefNameCondition {
  include: readonly string[];
  exclude: readonly string[];
}

export interface LiveRulesetRequiredChecks {
  rulesetId: number;
  rulesetName: string;
  enforcement: 'active';
  target: 'branch';
  requiredContexts: readonly string[];
  refNameCondition: RulesetRefNameCondition;
}

export interface PackageRequiredCheckAuthority {
  packageContractPath: string;
  packageSchema: string;
  rulesetName: string;
  rulesetEnforcement: string;
  packageRequiredContexts: readonly string[];
  expectedRefNameCondition: RulesetRefNameCondition;
  stageAuthorityDeltaPath: string;
}

export type RequiredCheckAuthorityComparison =
  | {
      status: 'AGREED';
      requiredContexts: readonly string[];
      packageAuthority: PackageRequiredCheckAuthority;
      liveRuleset: LiveRulesetRequiredChecks;
    }
  | {
      status: 'MISMATCH' | 'INCONCLUSIVE';
      reason: string;
      packageAuthority: PackageRequiredCheckAuthority;
      liveRuleset?: LiveRulesetRequiredChecks;
      packageContexts: readonly string[];
      liveContexts: readonly string[];
    };

export interface GitHubTruthSnapshot {
  repositoryId: number;
  repositoryFullName: string;
  observedAt: string;
  pullRequest: PullRequestTruth;
  baseRef: RefTruth;
  checks: readonly CheckTruth[];
  workflows: readonly WorkflowTruth[];
  mergeCommitInBase: boolean | 'UNKNOWN';
}

export interface ShadowReadRequest {
  repositoryId: number;
  repositoryFullName: string;
  pullRequestNumber: number;
  baseRef: string;
  observedAt: string;
}

export interface GitHubReadClient {
  readPullRequest(repositoryFullName: string, pullRequestNumber: number): Promise<PullRequestTruth>;
  readRef(repositoryFullName: string, ref: string): Promise<RefTruth>;
  readChecks(repositoryFullName: string, headSha: string): Promise<readonly CheckTruth[]>;
  readWorkflows(repositoryFullName: string, headSha: string): Promise<readonly WorkflowTruth[]>;
  readRulesetRequiredChecks(
    repositoryFullName: string,
    rulesetName: string,
  ): Promise<LiveRulesetRequiredChecks>;
  isAncestor(
    repositoryFullName: string,
    ancestorSha: string,
    descendantSha: string,
  ): Promise<boolean | 'UNKNOWN'>;
}

export interface ShadowTarget {
  candidateSha: string;
  expectedBaseSha: string;
  requiredCheckNames: readonly string[];
  initialLifecycleState: LifecycleState;
  lifecycleFacts: readonly LifecycleFact[];
  expectedLifecycleState?: LifecycleState;
  expectedNextActions?: readonly string[];
}

export type RequiredCheckDisposition = 'PASS' | 'NOT_READY' | 'FAILED' | 'INCONCLUSIVE';

export interface RequiredCheckEvaluation {
  disposition: RequiredCheckDisposition;
  reason: string;
  matched: Readonly<
    Record<
      string,
      {
        checkRunId: number;
        status: string;
        conclusion: string | null;
        startedAt: string | null;
        completedAt: string | null;
      }
    >
  >;
  missing: readonly string[];
}

export type DivergenceSeverity = 'BLOCKING' | 'RECORD_ONLY';

export type ShadowDivergenceKind =
  | 'HEAD_DRIFT'
  | 'BASE_DRIFT'
  | 'STATE_DIVERGENCE'
  | 'NEXT_ACTION_DIVERGENCE'
  | 'UNSAFE_ADVANCEMENT_PREDICTION'
  | 'NOTIFICATION_TRUTH_DIVERGENCE'
  | 'MANDATORY_TRUTH_UNAVAILABLE'
  | 'AMBIGUOUS_REQUIRED_CHECK_TRUTH'
  | 'REQUIRED_CHECK_AUTHORITY_MISMATCH';

export interface ShadowDivergence {
  kind: ShadowDivergenceKind;
  severity: DivergenceSeverity;
  explanation: string;
  disposition: string;
}

export interface ShadowObservation {
  observationId: string;
  observedAt: string;
  targetCandidateSha: string;
  truth: GitHubTruthSnapshot;
  requiredChecks: RequiredCheckEvaluation;
  projectionBeforeReconciliation: ProjectionResult;
  projectionAfterReconciliation: ProjectionResult;
  derivedLifecycleFact?: LifecycleFact;
  divergences: readonly ShadowDivergence[];
  blocking: boolean;
}

export interface ShadowRunAttempt {
  attemptId: string;
  observedAt: string;
  status: 'OBSERVED' | 'INCONCLUSIVE';
  reason: string;
  observationId?: string;
}

export interface ShadowJournalSnapshot {
  deliveries: readonly DeliveryEnvelope[];
  processingAttempts: readonly DeliveryProcessingAttempt[];
  semanticFacts: readonly GitHubSemanticFact[];
  observations: readonly ShadowObservation[];
  runAttempts: readonly ShadowRunAttempt[];
}

export interface DeliveryProcessingAttempt {
  attemptId: string;
  deliveryKey: string;
  observedAt: string;
  disposition: 'ACCEPTED' | 'IDEMPOTENT_NOOP' | 'CONFLICT' | 'REJECTED_SIGNATURE';
  reason: string;
}

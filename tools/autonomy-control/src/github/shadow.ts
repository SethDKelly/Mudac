import type { ShadowJournal } from '../storage/shadow-journal.js';
import type {
  GitHubReadClient,
  GitHubTruthSnapshot,
  ShadowReadRequest,
  ShadowRunAttempt,
  ShadowTarget,
} from './model.js';
import { normalizeGitHubTruth } from './normalize.js';
import { reconcileShadowTruth } from './reconciliation.js';

export interface ShadowRunResult {
  status: 'OBSERVED' | 'INCONCLUSIVE';
  reason: string;
  observationId?: string;
  truth?: GitHubTruthSnapshot;
}

export async function collectAuthoritativeGitHubTruth(
  client: GitHubReadClient,
  request: ShadowReadRequest,
): Promise<GitHubTruthSnapshot> {
  const pullRequest = await client.readPullRequest(
    request.repositoryFullName,
    request.pullRequestNumber,
  );
  const baseRef = await client.readRef(request.repositoryFullName, request.baseRef);
  const checks = await client.readChecks(request.repositoryFullName, pullRequest.headSha);
  const workflows = await client.readWorkflows(request.repositoryFullName, pullRequest.headSha);

  let mergeCommitInBase: boolean | 'UNKNOWN' = false;
  if (pullRequest.merged && pullRequest.mergeCommitSha) {
    mergeCommitInBase = await client.isAncestor(
      request.repositoryFullName,
      pullRequest.mergeCommitSha,
      baseRef.sha,
    );
  }

  return {
    repositoryId: request.repositoryId,
    repositoryFullName: request.repositoryFullName,
    observedAt: request.observedAt,
    pullRequest,
    baseRef,
    checks,
    workflows,
    mergeCommitInBase,
  };
}

export async function runReadOnlyShadow(
  client: GitHubReadClient,
  journal: ShadowJournal,
  request: ShadowReadRequest,
  target: ShadowTarget,
  attemptId: string,
  observationId: string,
): Promise<ShadowRunResult> {
  try {
    const truth = await collectAuthoritativeGitHubTruth(client, request);

    if (
      truth.repositoryFullName !== request.repositoryFullName ||
      truth.pullRequest.number !== request.pullRequestNumber ||
      truth.pullRequest.baseRef !== request.baseRef ||
      truth.baseRef.ref !== request.baseRef
    ) {
      const attempt: ShadowRunAttempt = {
        attemptId,
        observedAt: request.observedAt,
        status: 'INCONCLUSIVE',
        reason: 'authoritative_truth_identity_mismatch',
      };
      journal.recordRunAttempt(attempt);
      return { status: 'INCONCLUSIVE', reason: attempt.reason };
    }

    for (const semanticFact of normalizeGitHubTruth(truth)) {
      const append = journal.appendSemanticFact(semanticFact);
      if (append.status === 'CONFLICT') {
        const reason = `semantic_fact_conflict:${append.factId}`;
        journal.recordRunAttempt({
          attemptId,
          observedAt: request.observedAt,
          status: 'INCONCLUSIVE',
          reason,
        });
        return { status: 'INCONCLUSIVE', reason };
      }
    }

    const observation = reconcileShadowTruth(observationId, target, truth);
    journal.recordObservation(observation);
    journal.recordRunAttempt({
      attemptId,
      observedAt: request.observedAt,
      status: 'OBSERVED',
      reason: observation.blocking
        ? 'observation_recorded_with_blocking_divergence'
        : 'observation_recorded',
      observationId,
    });

    return {
      status: 'OBSERVED',
      reason: observation.blocking
        ? 'observation_recorded_with_blocking_divergence'
        : 'observation_recorded',
      observationId,
      truth,
    };
  } catch (error) {
    const reason =
      error instanceof Error
        ? `mandatory_github_truth_unavailable:${error.message}`
        : 'mandatory_github_truth_unavailable:unknown_error';
    journal.recordRunAttempt({
      attemptId,
      observedAt: request.observedAt,
      status: 'INCONCLUSIVE',
      reason,
    });
    return { status: 'INCONCLUSIVE', reason };
  }
}

import { createHash } from 'node:crypto';

import type { GitHubSemanticFact, GitHubTruthSnapshot } from './model.js';

function digest(value: unknown): string {
  return createHash('sha256').update(JSON.stringify(value)).digest('hex');
}

function fact(
  factId: string,
  factType: GitHubSemanticFact['factType'],
  observedAt: string,
  payload: Record<string, unknown>,
): GitHubSemanticFact {
  return {
    factId,
    factType,
    observedAt,
    payloadDigest: digest(payload),
    payload: structuredClone(payload),
  };
}

export function normalizeGitHubTruth(snapshot: GitHubTruthSnapshot): readonly GitHubSemanticFact[] {
  const repo = snapshot.repositoryId;
  const pr = snapshot.pullRequest;
  const facts: GitHubSemanticFact[] = [
    fact(`PR_HEAD:${repo}:${pr.number}:${pr.headSha}`, 'PR_HEAD', snapshot.observedAt, {
      repositoryId: repo,
      pullRequestNumber: pr.number,
      headSha: pr.headSha,
    }),
    fact(
      `PR_STATE:${repo}:${pr.number}:${pr.headSha}:${pr.state}:${pr.draft}:${pr.merged}`,
      'PR_STATE',
      snapshot.observedAt,
      {
        repositoryId: repo,
        pullRequestNumber: pr.number,
        state: pr.state,
        draft: pr.draft,
        merged: pr.merged,
        headSha: pr.headSha,
      },
    ),
    fact(
      `REF:${repo}:${snapshot.baseRef.ref}:${snapshot.baseRef.sha}`,
      'REF',
      snapshot.observedAt,
      {
        repositoryId: repo,
        ref: snapshot.baseRef.ref,
        sha: snapshot.baseRef.sha,
      },
    ),
  ];

  if (pr.merged && pr.mergeCommitSha) {
    facts.push(
      fact(`PR_MERGE:${repo}:${pr.number}:${pr.mergeCommitSha}`, 'PR_MERGE', snapshot.observedAt, {
        repositoryId: repo,
        pullRequestNumber: pr.number,
        mergeCommitSha: pr.mergeCommitSha,
        mergeCommitInBase: snapshot.mergeCommitInBase,
      }),
    );
  }

  for (const check of snapshot.checks) {
    facts.push(
      fact(`CHECK:${repo}:${check.id}:${check.attempt}`, 'CHECK', snapshot.observedAt, {
        repositoryId: repo,
        checkRunId: check.id,
        name: check.name,
        attempt: check.attempt,
        headSha: check.headSha,
        status: check.status,
        conclusion: check.conclusion,
      }),
    );
  }

  for (const workflow of snapshot.workflows) {
    facts.push(
      fact(`WORKFLOW:${repo}:${workflow.id}:${workflow.attempt}`, 'WORKFLOW', snapshot.observedAt, {
        repositoryId: repo,
        workflowRunId: workflow.id,
        name: workflow.name,
        attempt: workflow.attempt,
        headSha: workflow.headSha,
        status: workflow.status,
        conclusion: workflow.conclusion,
      }),
    );
  }

  return facts;
}

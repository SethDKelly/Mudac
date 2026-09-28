import process from 'node:process';

import { ShadowJournal } from '../storage/shadow-journal.js';
import type { GitHubFetch } from './rest-read-client.js';
import { GitHubRestReadClient } from './rest-read-client.js';
import { runReadOnlyShadow } from './shadow.js';

function requiredEnvironment(name: string): string {
  const value = process.env[name];
  if (!value || value.trim().length === 0) {
    throw new Error(`missing_required_environment:${name}`);
  }
  return value.trim();
}

function requiredPositiveInteger(name: string): number {
  const parsed = Number(requiredEnvironment(name));
  if (!Number.isSafeInteger(parsed) || parsed <= 0) {
    throw new Error(`invalid_required_integer:${name}`);
  }
  return parsed;
}

const repositoryFullName = requiredEnvironment('AUT001_REPOSITORY');
const pullRequestNumber = requiredPositiveInteger('AUT001_PR_NUMBER');
const candidateSha = requiredEnvironment('AUT001_CANDIDATE_SHA');
const baseSha = requiredEnvironment('AUT001_BASE_SHA');
const baseRef = requiredEnvironment('AUT001_BASE_REF');
const requiredCheckNames = requiredEnvironment('AUT001_REQUIRED_CHECKS')
  .split(',')
  .map((name) => name.trim())
  .filter((name) => name.length > 0);
const repositoryId = requiredPositiveInteger('AUT001_REPOSITORY_ID');
const observedAt = new Date().toISOString();

const calls: Array<{ method: string; url: string }> = [];
const boundedFetch: GitHubFetch = async (url, init) => {
  calls.push({ method: init.method, url });
  if (init.method !== 'GET') {
    throw new Error('live_shadow_non_get_attempt');
  }
  return fetch(url, init);
};

const journal = new ShadowJournal();
const client = new GitHubRestReadClient(boundedFetch);
const result = await runReadOnlyShadow(
  client,
  journal,
  {
    repositoryId,
    repositoryFullName,
    pullRequestNumber,
    baseRef,
    observedAt,
  },
  {
    candidateSha,
    expectedBaseSha: baseSha,
    requiredCheckNames,
    initialLifecycleState: 'AWAITING_PR_CI',
    lifecycleFacts: [],
  },
  `live-shadow:${candidateSha}:${observedAt}`,
  `live-shadow-observation:${candidateSha}:${observedAt}`,
);

const snapshot = journal.snapshot();
const observation = snapshot.observations.at(-1);
const nonGetCalls = calls.filter((call) => call.method !== 'GET');

const evidence = {
  schema: 'mudac.aut001-b-live-shadow-evidence/v1',
  subject: {
    repositoryId,
    repositoryFullName,
    pullRequestNumber,
    candidateSha,
    baseSha,
    baseRef,
    observedAt,
  },
  runtimeBoundary: {
    adapter: 'GitHubRestReadClient',
    apiBase: 'https://api.github.com',
    credentialsPassedToAdapter: false,
    callCount: calls.length,
    nonGetCallCount: nonGetCalls.length,
    calls,
  },
  result,
  observation: observation
    ? {
        requiredChecks: observation.requiredChecks,
        projectionBefore: observation.projectionBeforeReconciliation,
        projectionAfter: observation.projectionAfterReconciliation,
        divergences: observation.divergences,
        blocking: observation.blocking,
      }
    : null,
  appendOnlyEvidence: {
    deliveryCount: snapshot.deliveries.length,
    semanticFactCount: snapshot.semanticFacts.length,
    observationCount: snapshot.observations.length,
    runAttemptCount: snapshot.runAttempts.length,
  },
};

console.log(JSON.stringify(evidence, null, 2));

if (nonGetCalls.length > 0 || result.status !== 'OBSERVED' || observation?.blocking === true) {
  process.exitCode = 1;
}

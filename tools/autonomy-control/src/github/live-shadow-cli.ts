import { writeFileSync } from 'node:fs';
import process from 'node:process';

import { ShadowJournal } from '../storage/shadow-journal.js';
import { loadPackageRequiredCheckAuthority } from './package-authority.js';
import { compareRequiredCheckAuthority } from './required-check-authority.js';
import type { GitHubFetch } from './rest-read-client.js';
import { GitHubRestReadClient } from './rest-read-client.js';
import { runBoundedReadOnlyShadowWindow, type ShadowClock } from './shadow.js';

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

function optionalPositiveInteger(name: string, fallback: number): number {
  const raw = process.env[name];
  if (!raw || raw.trim().length === 0) return fallback;
  const parsed = Number(raw.trim());
  if (!Number.isSafeInteger(parsed) || parsed <= 0) {
    throw new Error(`invalid_optional_integer:${name}`);
  }
  return parsed;
}

const repositoryFullName = requiredEnvironment('AUT001_REPOSITORY');
const pullRequestNumber = requiredPositiveInteger('AUT001_PR_NUMBER');
const candidateSha = requiredEnvironment('AUT001_CANDIDATE_SHA');
const baseSha = requiredEnvironment('AUT001_BASE_SHA');
const baseRef = requiredEnvironment('AUT001_BASE_REF');
const repositoryId = requiredPositiveInteger('AUT001_REPOSITORY_ID');
const packageContractPath = requiredEnvironment('AUT001_PACKAGE_CONTRACT_PATH');
const evidencePath = requiredEnvironment('AUT001_EVIDENCE_PATH');
const maxAttempts = optionalPositiveInteger('AUT001_SHADOW_MAX_ATTEMPTS', 24);
const intervalMs = optionalPositiveInteger('AUT001_SHADOW_INTERVAL_MS', 30_000);
const timeoutMs = optionalPositiveInteger('AUT001_SHADOW_TIMEOUT_MS', 1_200_000);

const calls: Array<{ method: string; url: string }> = [];
const boundedFetch: GitHubFetch = async (url, init) => {
  calls.push({ method: init.method, url });
  if (init.method !== 'GET') {
    throw new Error('live_shadow_non_get_attempt');
  }
  return fetch(url, init);
};

const systemClock: ShadowClock = {
  now: () => new Date(),
  sleep: async (ms) => {
    await new Promise((resolve) => setTimeout(resolve, ms));
  },
};

const packageAuthority = loadPackageRequiredCheckAuthority(packageContractPath);
const client = new GitHubRestReadClient(boundedFetch);
const liveRuleset = await client.readRulesetRequiredChecks(
  repositoryFullName,
  packageAuthority.rulesetName,
);
const authorityComparison = compareRequiredCheckAuthority(packageAuthority, liveRuleset);

if (authorityComparison.status !== 'AGREED') {
  const evidence = {
    schema: 'mudac.aut001-b-live-shadow-evidence/v2',
    subject: {
      repositoryId,
      repositoryFullName,
      pullRequestNumber,
      candidateSha,
      baseSha,
      baseRef,
    },
    packageAuthorityRecord: {
      path: packageAuthority.packageContractPath,
      schema: packageAuthority.packageSchema,
      rulesetName: packageAuthority.rulesetName,
      requiredContexts: packageAuthority.packageRequiredContexts,
    },
    liveRuleset: {
      rulesetId: liveRuleset.rulesetId,
      rulesetName: liveRuleset.rulesetName,
      requiredContexts: liveRuleset.requiredContexts,
    },
    authoritySetComparison: authorityComparison,
    runtimeBoundary: {
      adapter: 'GitHubRestReadClient',
      apiBase: 'https://api.github.com',
      credentialsPassedToAdapter: false,
      callCount: calls.length,
      nonGetCallCount: calls.filter((call) => call.method !== 'GET').length,
      calls,
    },
    terminalDisposition: null,
    windowTerminatedNormally: false,
    timedOut: false,
    result: {
      status: 'FAILED_CLOSED',
      reason: authorityComparison.reason,
    },
  };
  writeFileSync(evidencePath, `${JSON.stringify(evidence, null, 2)}\n`, 'utf8');
  console.log(JSON.stringify(evidence, null, 2));
  process.exitCode = 1;
} else {
  const requiredCheckNames = authorityComparison.requiredContexts;
  const initialJournal = new ShadowJournal();
  const { result, journal } = await runBoundedReadOnlyShadowWindow({
    client,
    journal: initialJournal,
    baseRequest: {
      repositoryId,
      repositoryFullName,
      pullRequestNumber,
      baseRef,
    },
    target: {
      candidateSha,
      expectedBaseSha: baseSha,
      requiredCheckNames,
      initialLifecycleState: 'AWAITING_PR_CI',
      lifecycleFacts: [],
    },
    authorityComparison,
    clock: systemClock,
    config: {
      maxAttempts,
      intervalMs,
      timeoutMs,
      confirmAfterTerminal: true,
    },
    candidateSha,
  });

  const snapshot = journal.snapshot();
  const observations = snapshot.observations.map((observation) => ({
    observationId: observation.observationId,
    observedAt: observation.observedAt,
    requiredChecks: observation.requiredChecks,
    projectionBefore: observation.projectionBeforeReconciliation,
    projectionAfter: observation.projectionAfterReconciliation,
    divergences: observation.divergences,
    blocking: observation.blocking,
  }));
  const nonGetCalls = calls.filter((call) => call.method !== 'GET');
  const blockingDivergence = observations.some((item) => item.blocking);

  const evidence = {
    schema: 'mudac.aut001-b-live-shadow-evidence/v2',
    subject: {
      repositoryId,
      repositoryFullName,
      pullRequestNumber,
      candidateSha,
      baseSha,
      baseRef,
    },
    packageAuthorityRecord: {
      path: packageAuthority.packageContractPath,
      schema: packageAuthority.packageSchema,
      rulesetName: packageAuthority.rulesetName,
      requiredContexts: packageAuthority.packageRequiredContexts,
    },
    liveRuleset: {
      rulesetId: liveRuleset.rulesetId,
      rulesetName: liveRuleset.rulesetName,
      requiredContexts: liveRuleset.requiredContexts,
    },
    authoritySetComparison: {
      status: authorityComparison.status,
      requiredContexts: authorityComparison.requiredContexts,
    },
    runtimeBoundary: {
      adapter: 'GitHubRestReadClient',
      apiBase: 'https://api.github.com',
      credentialsPassedToAdapter: false,
      callCount: calls.length,
      nonGetCallCount: nonGetCalls.length,
      calls,
    },
    boundedWindow: {
      maxAttempts,
      intervalMs,
      timeoutMs,
      confirmAfterTerminal: true,
      status: result.status,
      reason: result.reason,
      terminalDisposition: result.terminalDisposition,
      windowTerminatedNormally: result.windowTerminatedNormally,
      timedOut: result.timedOut,
      observationCount: result.observationCount,
      restartReconstructionCount: result.restartReconstructionCount,
    },
    observations,
    appendOnlyEvidence: {
      deliveryCount: snapshot.deliveries.length,
      semanticFactCount: snapshot.semanticFacts.length,
      observationCount: snapshot.observations.length,
      runAttemptCount: snapshot.runAttempts.length,
      runAttempts: snapshot.runAttempts,
    },
    terminalDisposition: result.terminalDisposition,
    windowTerminatedNormally: result.windowTerminatedNormally,
    timedOut: result.timedOut,
    result,
  };

  writeFileSync(evidencePath, `${JSON.stringify(evidence, null, 2)}\n`, 'utf8');
  console.log(JSON.stringify(evidence, null, 2));

  if (
    nonGetCalls.length > 0 ||
    result.status !== 'TERMINAL' ||
    result.timedOut ||
    !result.windowTerminatedNormally ||
    blockingDivergence ||
    result.terminalDisposition === null
  ) {
    process.exitCode = 1;
  }
}

import { ShadowJournal } from '../storage/shadow-journal.js';
import { isTerminalRequiredCheckDisposition } from './checks.js';
import type {
  GitHubReadClient,
  GitHubTruthSnapshot,
  RequiredCheckAuthorityComparison,
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

export interface ShadowClock {
  now(): Date;
  sleep(ms: number): Promise<void>;
}

export interface BoundedShadowWindowConfig {
  maxAttempts: number;
  intervalMs: number;
  timeoutMs: number;
  confirmAfterTerminal: boolean;
}

export interface BoundedShadowWindowResult {
  status: 'TERMINAL' | 'TIMED_OUT' | 'FAILED_CLOSED';
  reason: string;
  terminalDisposition: string | null;
  windowTerminatedNormally: boolean;
  timedOut: boolean;
  observationCount: number;
  restartReconstructionCount: number;
  authorityComparison: RequiredCheckAuthorityComparison;
  finalObservationId?: string;
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

export async function runBoundedReadOnlyShadowWindow(input: {
  client: GitHubReadClient;
  journal: ShadowJournal;
  baseRequest: Omit<ShadowReadRequest, 'observedAt'>;
  target: ShadowTarget;
  authorityComparison: RequiredCheckAuthorityComparison;
  clock: ShadowClock;
  config: BoundedShadowWindowConfig;
  candidateSha: string;
}): Promise<{ result: BoundedShadowWindowResult; journal: ShadowJournal }> {
  const startedMs = input.clock.now().getTime();
  let journal = input.journal;
  let restartReconstructionCount = 0;
  let terminalDisposition: string | null = null;
  let finalObservationId: string | undefined;
  let sawTerminal = false;

  if (input.authorityComparison.status !== 'AGREED') {
    return {
      journal,
      result: {
        status: 'FAILED_CLOSED',
        reason: `required_check_authority_${input.authorityComparison.status.toLowerCase()}:${input.authorityComparison.reason}`,
        terminalDisposition: null,
        windowTerminatedNormally: false,
        timedOut: false,
        observationCount: journal.snapshot().observations.length,
        restartReconstructionCount,
        authorityComparison: input.authorityComparison,
      },
    };
  }

  for (let attempt = 1; attempt <= input.config.maxAttempts; attempt += 1) {
    const elapsed = input.clock.now().getTime() - startedMs;
    if (elapsed > input.config.timeoutMs) {
      return {
        journal,
        result: {
          status: 'TIMED_OUT',
          reason: 'bounded_observation_window_timeout',
          terminalDisposition,
          windowTerminatedNormally: false,
          timedOut: true,
          observationCount: journal.snapshot().observations.length,
          restartReconstructionCount,
          authorityComparison: input.authorityComparison,
          ...(finalObservationId ? { finalObservationId } : {}),
        },
      };
    }

    if (attempt > 1) {
      // Reconstruct as though after process restart before the next observation.
      journal = new ShadowJournal(journal.snapshot());
      restartReconstructionCount += 1;
    }

    const observedAt = input.clock.now().toISOString();
    const observationId = `live-shadow-observation:${input.candidateSha}:${attempt}:${observedAt}`;
    const attemptId = `live-shadow:${input.candidateSha}:${attempt}:${observedAt}`;
    const result = await runReadOnlyShadow(
      input.client,
      journal,
      { ...input.baseRequest, observedAt },
      input.target,
      attemptId,
      observationId,
    );

    if (result.status === 'INCONCLUSIVE') {
      const transient = result.reason.startsWith('mandatory_github_truth_unavailable:');
      if (!transient) {
        return {
          journal,
          result: {
            status: 'FAILED_CLOSED',
            reason: result.reason,
            terminalDisposition,
            windowTerminatedNormally: false,
            timedOut: false,
            observationCount: journal.snapshot().observations.length,
            restartReconstructionCount,
            authorityComparison: input.authorityComparison,
            ...(finalObservationId ? { finalObservationId } : {}),
          },
        };
      }
    } else {
      const observation = journal
        .snapshot()
        .observations.find((item) => item.observationId === observationId);
      if (!observation) {
        return {
          journal,
          result: {
            status: 'FAILED_CLOSED',
            reason: 'observation_missing_after_observed_status',
            terminalDisposition,
            windowTerminatedNormally: false,
            timedOut: false,
            observationCount: journal.snapshot().observations.length,
            restartReconstructionCount,
            authorityComparison: input.authorityComparison,
          },
        };
      }

      finalObservationId = observation.observationId;
      const disposition = observation.requiredChecks.disposition;

      if (observation.blocking && disposition === 'INCONCLUSIVE') {
        return {
          journal,
          result: {
            status: 'FAILED_CLOSED',
            reason: observation.requiredChecks.reason,
            terminalDisposition: disposition,
            windowTerminatedNormally: false,
            timedOut: false,
            observationCount: journal.snapshot().observations.length,
            restartReconstructionCount,
            authorityComparison: input.authorityComparison,
            finalObservationId,
          },
        };
      }

      if (isTerminalRequiredCheckDisposition(disposition)) {
        terminalDisposition = disposition;
        if (!sawTerminal) {
          sawTerminal = true;
          if (!input.config.confirmAfterTerminal) {
            return {
              journal,
              result: {
                status: 'TERMINAL',
                reason: `required_checks_terminal:${disposition}`,
                terminalDisposition,
                windowTerminatedNormally: true,
                timedOut: false,
                observationCount: journal.snapshot().observations.length,
                restartReconstructionCount,
                authorityComparison: input.authorityComparison,
                finalObservationId,
              },
            };
          }
        } else {
          return {
            journal,
            result: {
              status: 'TERMINAL',
              reason: `required_checks_terminal_confirmed:${disposition}`,
              terminalDisposition,
              windowTerminatedNormally: true,
              timedOut: false,
              observationCount: journal.snapshot().observations.length,
              restartReconstructionCount,
              authorityComparison: input.authorityComparison,
              finalObservationId,
            },
          };
        }
      }
    }

    if (attempt < input.config.maxAttempts) {
      const remaining = input.config.timeoutMs - (input.clock.now().getTime() - startedMs);
      if (remaining <= 0) break;
      await input.clock.sleep(Math.min(input.config.intervalMs, remaining));
    }
  }

  if (sawTerminal && !input.config.confirmAfterTerminal) {
    return {
      journal,
      result: {
        status: 'TERMINAL',
        reason: `required_checks_terminal:${terminalDisposition}`,
        terminalDisposition,
        windowTerminatedNormally: true,
        timedOut: false,
        observationCount: journal.snapshot().observations.length,
        restartReconstructionCount,
        authorityComparison: input.authorityComparison,
        ...(finalObservationId ? { finalObservationId } : {}),
      },
    };
  }

  return {
    journal,
    result: {
      status: 'TIMED_OUT',
      reason: sawTerminal
        ? 'bounded_observation_window_timeout_before_confirmation'
        : 'bounded_observation_window_timeout',
      terminalDisposition,
      windowTerminatedNormally: false,
      timedOut: true,
      observationCount: journal.snapshot().observations.length,
      restartReconstructionCount,
      authorityComparison: input.authorityComparison,
      ...(finalObservationId ? { finalObservationId } : {}),
    },
  };
}

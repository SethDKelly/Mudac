import type { RequiredCheckDisposition } from './model.js';

export type LiveShadowWindowStatus = 'TERMINAL' | 'FAILED_CLOSED' | 'INCONCLUSIVE' | string;

export interface LiveShadowExitDecisionInput {
  terminalDisposition: RequiredCheckDisposition | null;
  windowTerminatedNormally: boolean;
  timedOut: boolean;
  blockingDivergence: boolean;
  nonGetCallCount: number;
  status: LiveShadowWindowStatus;
}

/**
 * Green AUT-001 Read-Only Shadow workflow means the bounded window reached
 * terminal PASS with no blocking divergence, timeout, mutation, or structural
 * failure. Terminal FAILED, INCONCLUSIVE, timeout, mutation, or structural
 * failure must exit nonzero. Artifact retention remains the workflow's job.
 */
export function decideLiveShadowProcessExitCode(input: LiveShadowExitDecisionInput): number {
  if (input.nonGetCallCount > 0) return 1;
  if (input.timedOut) return 1;
  if (input.blockingDivergence) return 1;
  if (!input.windowTerminatedNormally) return 1;
  if (input.status !== 'TERMINAL') return 1;
  if (input.terminalDisposition === 'PASS') return 0;
  return 1;
}

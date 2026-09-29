import { describe, expect, it } from 'vitest';

import { decideLiveShadowProcessExitCode } from '../src/github/live-shadow-exit.js';

describe('AUT-B-R1-IR-04 live shadow exit semantics', () => {
  it('exits 0 only for terminal PASS without structural failure', () => {
    expect(
      decideLiveShadowProcessExitCode({
        terminalDisposition: 'PASS',
        windowTerminatedNormally: true,
        timedOut: false,
        blockingDivergence: false,
        nonGetCallCount: 0,
        status: 'TERMINAL',
      }),
    ).toBe(0);
  });

  it.each([
    ['FAILED', 'FAILED' as const],
    ['INCONCLUSIVE', 'INCONCLUSIVE' as const],
    ['null disposition', null],
  ])('exits nonzero for terminal %s', (_label, terminalDisposition) => {
    expect(
      decideLiveShadowProcessExitCode({
        terminalDisposition,
        windowTerminatedNormally: true,
        timedOut: false,
        blockingDivergence: false,
        nonGetCallCount: 0,
        status: 'TERMINAL',
      }),
    ).toBe(1);
  });

  it('exits nonzero on timeout', () => {
    expect(
      decideLiveShadowProcessExitCode({
        terminalDisposition: 'PASS',
        windowTerminatedNormally: false,
        timedOut: true,
        blockingDivergence: false,
        nonGetCallCount: 0,
        status: 'TERMINAL',
      }),
    ).toBe(1);
  });

  it('exits nonzero on blocking divergence', () => {
    expect(
      decideLiveShadowProcessExitCode({
        terminalDisposition: 'PASS',
        windowTerminatedNormally: true,
        timedOut: false,
        blockingDivergence: true,
        nonGetCallCount: 0,
        status: 'TERMINAL',
      }),
    ).toBe(1);
  });

  it('exits nonzero on any non-GET attempt', () => {
    expect(
      decideLiveShadowProcessExitCode({
        terminalDisposition: 'PASS',
        windowTerminatedNormally: true,
        timedOut: false,
        blockingDivergence: false,
        nonGetCallCount: 1,
        status: 'TERMINAL',
      }),
    ).toBe(1);
  });

  it('exits nonzero when the window did not terminate normally', () => {
    expect(
      decideLiveShadowProcessExitCode({
        terminalDisposition: 'PASS',
        windowTerminatedNormally: false,
        timedOut: false,
        blockingDivergence: false,
        nonGetCallCount: 0,
        status: 'TERMINAL',
      }),
    ).toBe(1);
  });

  it('exits nonzero for non-TERMINAL status even if disposition claims PASS', () => {
    expect(
      decideLiveShadowProcessExitCode({
        terminalDisposition: 'PASS',
        windowTerminatedNormally: true,
        timedOut: false,
        blockingDivergence: false,
        nonGetCallCount: 0,
        status: 'FAILED_CLOSED',
      }),
    ).toBe(1);
  });
});

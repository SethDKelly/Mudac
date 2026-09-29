import { describe, expect, it } from 'vitest';

import { evaluateRequiredChecks } from '../src/github/checks.js';
import { decideLiveShadowProcessExitCode } from '../src/github/live-shadow-exit.js';
import type { CheckTruth } from '../src/github/model.js';
import { normalizeGitHubTruth } from '../src/github/normalize.js';
import { loadPackageRequiredCheckAuthority } from '../src/github/package-authority.js';
import { classifyDeliveryAgainstTruth } from '../src/github/reconciliation.js';
import { compareRequiredCheckAuthority } from '../src/github/required-check-authority.js';

function check(overrides: Partial<CheckTruth> & Pick<CheckTruth, 'name' | 'id'>): CheckTruth {
  return {
    headSha: 'candidate',
    status: 'completed',
    conclusion: 'success',
    startedAt: '2026-09-28T18:00:00Z',
    completedAt: '2026-09-28T18:01:00Z',
    ...overrides,
  };
}

describe('AUT-001-B Repair Cycle 2 cross-finding regression matrix', () => {
  it('keeps malformed currentness from establishing PASS (AUT-B-R1-IR-01 / AUT-C02 / AUT-C05)', () => {
    const evaluation = evaluateRequiredChecks(
      [
        check({
          id: 1,
          name: 'Implementation Verification',
          conclusion: 'failure',
          completedAt: '2026-09-28T18:00:00Z',
        }),
        check({
          id: 2,
          name: 'Implementation Verification',
          conclusion: 'success',
          completedAt: 'not-an-iso-timestamp',
        }),
      ],
      'candidate',
      ['Implementation Verification'],
    );
    expect(evaluation.disposition).toBe('INCONCLUSIVE');
  });

  it('classifies vitest.config.ts only through the additive Stage-B delta (AUT-B-R1-IR-02)', () => {
    const authority = loadPackageRequiredCheckAuthority(
      'docs/routing/aut001_implementation_package_contract.json',
    );
    expect(authority.stageAuthorityDeltaPath).toBe(
      'docs/routing/aut001_b_stage_authority_material_delta.json',
    );
  });

  it('requires authorized ref_name scope for required-check authority agreement (AUT-B-R1-IR-03)', () => {
    const packageAuthority = loadPackageRequiredCheckAuthority(
      'docs/routing/aut001_implementation_package_contract.json',
    );
    const comparison = compareRequiredCheckAuthority(packageAuthority, {
      rulesetId: 1,
      rulesetName: packageAuthority.rulesetName,
      enforcement: 'active',
      target: 'branch',
      requiredContexts: packageAuthority.packageRequiredContexts,
      refNameCondition: {
        include: ['refs/heads/main'],
        exclude: [],
      },
    });
    expect(comparison.status).toBe('MISMATCH');
  });

  it('keeps green exit reserved for terminal PASS only (AUT-B-R1-IR-04)', () => {
    expect(
      decideLiveShadowProcessExitCode({
        terminalDisposition: 'FAILED',
        windowTerminatedNormally: true,
        timedOut: false,
        blockingDivergence: false,
        nonGetCallCount: 0,
        status: 'TERMINAL',
      }),
    ).toBe(1);
  });

  it('preserves AUT-B-IR-03 semantic identity vs observedAt-only change', () => {
    const first = normalizeGitHubTruth({
      repositoryId: 1,
      repositoryFullName: 'SethDKelly/Mudac',
      observedAt: '2026-09-28T18:06:00Z',
      pullRequest: {
        number: 23,
        state: 'open',
        merged: false,
        draft: true,
        headSha: 'candidate',
        baseRef: 'aut-001/b-start-gate',
        baseSha: 'base',
        mergeCommitSha: null,
      },
      baseRef: { ref: 'aut-001/b-start-gate', sha: 'base' },
      checks: [check({ id: 1, name: 'Implementation Verification' })],
      workflows: [],
      mergeCommitInBase: false,
    });
    const second = normalizeGitHubTruth({
      repositoryId: 1,
      repositoryFullName: 'SethDKelly/Mudac',
      observedAt: '2026-09-28T18:07:00Z',
      pullRequest: {
        number: 23,
        state: 'open',
        merged: false,
        draft: true,
        headSha: 'candidate',
        baseRef: 'aut-001/b-start-gate',
        baseSha: 'base',
        mergeCommitSha: null,
      },
      baseRef: { ref: 'aut-001/b-start-gate', sha: 'base' },
      checks: [check({ id: 1, name: 'Implementation Verification' })],
      workflows: [],
      mergeCommitInBase: false,
    });
    expect(first.map((fact) => fact.factId)).toEqual(second.map((fact) => fact.factId));
    expect(first.map((fact) => fact.payloadDigest)).toEqual(
      second.map((fact) => fact.payloadDigest),
    );
  });

  it('preserves AUT-B-IR-04 unknown-action RECORD_NO_ADVANCE behavior', () => {
    const disposition = classifyDeliveryAgainstTruth(
      {
        deliveryId: 'd-unknown-action',
        sourceIdentity: 'hook',
        sourceType: 'WEBHOOK',
        repositoryId: 1,
        repositoryFullName: 'SethDKelly/Mudac',
        eventFamily: 'pull_request',
        action: 'mystery_action',
        receivedAt: '2026-09-28T18:00:00Z',
        signatureVerified: true,
        payloadDigest: 'digest-unknown',
        pullRequestNumber: 23,
        payloadHeadSha: 'candidate',
        payloadBaseSha: 'base',
      },
      {
        repositoryId: 1,
        repositoryFullName: 'SethDKelly/Mudac',
        observedAt: '2026-09-28T18:00:00Z',
        pullRequest: {
          number: 23,
          state: 'open',
          merged: false,
          draft: true,
          headSha: 'candidate',
          baseRef: 'aut-001/b-start-gate',
          baseSha: 'base',
          mergeCommitSha: null,
        },
        baseRef: { ref: 'aut-001/b-start-gate', sha: 'base' },
        checks: [],
        workflows: [],
        mergeCommitInBase: false,
      },
    );
    expect(disposition).toBe('RECORD_NO_ADVANCE');
  });

  it('keeps wrong enforcement-scope rulesets from agreeing (AUT-C15)', () => {
    const packageAuthority = loadPackageRequiredCheckAuthority(
      'docs/routing/aut001_implementation_package_contract.json',
    );
    const wrongScope = compareRequiredCheckAuthority(packageAuthority, {
      rulesetId: 1,
      rulesetName: packageAuthority.rulesetName,
      enforcement: 'active',
      target: 'branch',
      requiredContexts: packageAuthority.packageRequiredContexts,
      refNameCondition: {
        include: ['~DEFAULT_BRANCH', 'refs/heads/release'],
        exclude: [],
      },
    });
    expect(wrongScope.status).toBe('MISMATCH');
  });
});

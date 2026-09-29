import { describe, expect, it } from 'vitest';

import type { GitHubTruthSnapshot } from '../src/github/model.js';
import { normalizeGitHubTruth } from '../src/github/normalize.js';
import { ShadowJournal } from '../src/storage/shadow-journal.js';

function snapshot(overrides: Partial<GitHubTruthSnapshot> = {}): GitHubTruthSnapshot {
  return {
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
    checks: [
      {
        id: 100,
        name: 'Implementation Verification',
        headSha: 'candidate',
        status: 'in_progress',
        conclusion: null,
        startedAt: '2026-09-28T18:06:00Z',
        completedAt: null,
      },
    ],
    workflows: [
      {
        id: 200,
        name: 'CodeQL',
        headSha: 'candidate',
        attempt: 1,
        status: 'in_progress',
        conclusion: null,
      },
    ],
    mergeCommitInBase: false,
    ...overrides,
  };
}

describe('AUT-001-B semantic fact identity vs observation metadata', () => {
  it('treats identical PR_HEAD payloads at T1/T2 as idempotent', () => {
    const journal = new ShadowJournal();
    const first = normalizeGitHubTruth(snapshot({ observedAt: '2026-09-28T18:06:00Z' }));
    const second = normalizeGitHubTruth(snapshot({ observedAt: '2026-09-28T18:07:00Z' }));
    for (const fact of first) expect(journal.appendSemanticFact(fact).status).toBe('APPENDED');
    const prHead = second.find((fact) => fact.factType === 'PR_HEAD');
    expect(prHead).toBeDefined();
    expect(journal.appendSemanticFact(prHead!).status).toBe('IDEMPOTENT_NOOP');
  });

  it('treats identical PR_STATE payloads at T1/T2 as idempotent', () => {
    const journal = new ShadowJournal();
    const first = normalizeGitHubTruth(snapshot({ observedAt: '2026-09-28T18:06:00Z' }));
    const second = normalizeGitHubTruth(snapshot({ observedAt: '2026-09-28T18:07:00Z' }));
    for (const fact of first) journal.appendSemanticFact(fact);
    const prState = second.find((fact) => fact.factType === 'PR_STATE');
    expect(journal.appendSemanticFact(prState!).status).toBe('IDEMPOTENT_NOOP');
  });

  it('treats identical REF payloads at T1/T2 as idempotent', () => {
    const journal = new ShadowJournal();
    const first = normalizeGitHubTruth(snapshot({ observedAt: '2026-09-28T18:06:00Z' }));
    const second = normalizeGitHubTruth(snapshot({ observedAt: '2026-09-28T18:07:00Z' }));
    for (const fact of first) journal.appendSemanticFact(fact);
    const ref = second.find((fact) => fact.factType === 'REF');
    expect(journal.appendSemanticFact(ref!).status).toBe('IDEMPOTENT_NOOP');
  });

  it('appends changed CHECK status/conclusion as a new immutable version', () => {
    const journal = new ShadowJournal();
    const pending = normalizeGitHubTruth(snapshot());
    const completed = normalizeGitHubTruth(
      snapshot({
        observedAt: '2026-09-28T18:07:00Z',
        checks: [
          {
            id: 100,
            name: 'Implementation Verification',
            headSha: 'candidate',
            status: 'completed',
            conclusion: 'success',
            startedAt: '2026-09-28T18:06:00Z',
            completedAt: '2026-09-28T18:07:00Z',
          },
        ],
      }),
    );
    for (const fact of pending) expect(journal.appendSemanticFact(fact).status).toBe('APPENDED');
    for (const fact of completed) {
      expect(journal.appendSemanticFact(fact).status).not.toBe('CONFLICT');
    }
    const checkFacts = journal.snapshot().semanticFacts.filter((fact) => fact.factType === 'CHECK');
    expect(checkFacts).toHaveLength(2);
    expect(checkFacts[0]?.factId).not.toBe(checkFacts[1]?.factId);
  });

  it('succeeds after restart from snapshot followed by fresh observation', () => {
    const first = new ShadowJournal();
    for (const fact of normalizeGitHubTruth(snapshot({ observedAt: '2026-09-28T18:06:00Z' }))) {
      first.appendSemanticFact(fact);
    }
    first.recordRunAttempt({
      attemptId: 'run-1',
      observedAt: '2026-09-28T18:06:00Z',
      status: 'INCONCLUSIVE',
      reason: 'historical_failure_retained',
    });

    const restarted = new ShadowJournal(first.snapshot());
    for (const fact of normalizeGitHubTruth(snapshot({ observedAt: '2026-09-28T18:08:00Z' }))) {
      expect(restarted.appendSemanticFact(fact).status).not.toBe('CONFLICT');
    }
    restarted.recordRunAttempt({
      attemptId: 'run-2',
      observedAt: '2026-09-28T18:08:00Z',
      status: 'OBSERVED',
      reason: 'observation_recorded',
    });

    const snapshotState = restarted.snapshot();
    expect(snapshotState.runAttempts).toHaveLength(2);
    expect(snapshotState.runAttempts[0]?.reason).toBe('historical_failure_retained');
    expect(snapshotState.semanticFacts.length).toBeGreaterThan(0);
  });

  it('fails closed when the same immutable semantic identity has conflicting contents', () => {
    const journal = new ShadowJournal();
    const base = normalizeGitHubTruth(snapshot())[0]!;
    expect(journal.appendSemanticFact(base).status).toBe('APPENDED');
    expect(
      journal.appendSemanticFact({
        ...base,
        observedAt: '2026-09-28T18:09:00Z',
        payload: { ...base.payload, headSha: 'other' },
      }).status,
    ).toBe('CONFLICT');
  });
});

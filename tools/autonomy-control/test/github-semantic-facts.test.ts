import { describe, expect, it } from 'vitest';

import { normalizeGitHubTruth, ShadowJournal } from '../src/index.js';
import type { GitHubTruthSnapshot } from '../src/index.js';

function snapshot(
  status: 'in_progress' | 'completed',
  conclusion: 'success' | null,
): GitHubTruthSnapshot {
  return {
    repositoryId: 1,
    repositoryFullName: 'SethDKelly/Mudac',
    observedAt: status === 'in_progress' ? '2026-09-28T18:06:00Z' : '2026-09-28T18:07:00Z',
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
        attempt: 100,
        status,
        conclusion,
      },
    ],
    workflows: [
      {
        id: 200,
        name: 'CodeQL',
        headSha: 'candidate',
        attempt: 1,
        status,
        conclusion,
      },
    ],
    mergeCommitInBase: false,
  };
}

describe('AUT-001-B immutable semantic fact versions', () => {
  it('appends superseding check/workflow states instead of conflicting with prior history', () => {
    const journal = new ShadowJournal();
    const first = normalizeGitHubTruth(snapshot('in_progress', null));
    const second = normalizeGitHubTruth(snapshot('completed', 'success'));

    for (const fact of first) {
      expect(journal.appendSemanticFact(fact).status).toBe('APPENDED');
    }
    for (const fact of second) {
      expect(journal.appendSemanticFact(fact).status).not.toBe('CONFLICT');
    }

    const checkFacts = journal.snapshot().semanticFacts.filter((fact) => fact.factType === 'CHECK');
    const workflowFacts = journal
      .snapshot()
      .semanticFacts.filter((fact) => fact.factType === 'WORKFLOW');
    expect(checkFacts).toHaveLength(2);
    expect(workflowFacts).toHaveLength(2);
    expect(checkFacts[0]?.factId).not.toBe(checkFacts[1]?.factId);
    expect(workflowFacts[0]?.factId).not.toBe(workflowFacts[1]?.factId);
  });
});

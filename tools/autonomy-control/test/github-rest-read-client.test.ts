import { describe, expect, it } from 'vitest';

import { GitHubRestReadClient } from '../src/index.js';
import type { GitHubFetch } from '../src/index.js';

function response(value: unknown, status = 200) {
  return {
    ok: status >= 200 && status < 300,
    status,
    async json(): Promise<unknown> {
      return structuredClone(value);
    },
  };
}

describe('AUT-001-B bounded GitHub REST read client', () => {
  it('uses only canonical GitHub GET requests with no authorization header', async () => {
    const calls: Array<{ url: string; method: string; headers: Readonly<Record<string, string>> }> =
      [];
    const fetchImpl: GitHubFetch = async (url, init) => {
      calls.push({ url, method: init.method, headers: init.headers });
      return response({
        number: 23,
        state: 'open',
        merged: false,
        draft: true,
        merge_commit_sha: null,
        head: { sha: 'head-1' },
        base: { ref: 'aut-001/b-start-gate', sha: 'base-1' },
      });
    };
    const client = new GitHubRestReadClient(fetchImpl);
    const pr = await client.readPullRequest('SethDKelly/Mudac', 23);
    expect(pr.headSha).toBe('head-1');
    expect(calls).toHaveLength(1);
    expect(calls[0]?.url).toBe('https://api.github.com/repos/SethDKelly/Mudac/pulls/23');
    expect(calls[0]?.method).toBe('GET');
    expect(
      Object.keys(calls[0]?.headers ?? {}).some((name) => name.toLowerCase() === 'authorization'),
    ).toBe(false);
  });

  it('rejects any noncanonical API base instead of becoming a generic HTTP client', () => {
    expect(() => new GitHubRestReadClient(async () => response({}), 'https://example.com')).toThrow(
      'github_api_base_must_be_canonical',
    );
  });

  it('fails closed when a bounded check query would require unimplemented pagination', async () => {
    const fetchImpl: GitHubFetch = async () =>
      response({
        total_count: 101,
        check_runs: [
          {
            id: 1,
            name: 'Implementation Verification',
            head_sha: 'head-1',
            status: 'completed',
            conclusion: 'success',
          },
        ],
      });
    const client = new GitHubRestReadClient(fetchImpl);
    await expect(client.readChecks('SethDKelly/Mudac', 'head-1')).rejects.toThrow(
      'github_check_truth_pagination_incomplete',
    );
  });

  it('fails closed on non-success GitHub responses', async () => {
    const client = new GitHubRestReadClient(async () => response({ message: 'rate limited' }, 403));
    await expect(client.readPullRequest('SethDKelly/Mudac', 23)).rejects.toThrow(
      'github_read_failed:403',
    );
  });
});

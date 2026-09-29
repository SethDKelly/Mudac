import { describe, expect, it } from 'vitest';

import { loadPackageRequiredCheckAuthority } from '../src/github/package-authority.js';
import { GitHubRestReadClient } from '../src/github/rest-read-client.js';
import type { GitHubFetch } from '../src/github/rest-read-client.js';

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

  it('fails closed on an unknown pull-request state instead of coercing it to closed', async () => {
    const client = new GitHubRestReadClient(async () =>
      response({
        number: 23,
        state: 'future_state',
        merged: false,
        draft: true,
        merge_commit_sha: null,
        head: { sha: 'head-1' },
        base: { ref: 'aut-001/b-start-gate', sha: 'base-1' },
      }),
    );

    await expect(client.readPullRequest('SethDKelly/Mudac', 23)).rejects.toThrow(
      'invalid_github_response:pull_request.state',
    );
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
            started_at: '2026-09-28T17:40:00Z',
            completed_at: '2026-09-28T17:44:00Z',
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

  it('loads package required-check authority from the versioned package contract', () => {
    const authority = loadPackageRequiredCheckAuthority(
      'docs/routing/aut001_implementation_package_contract.json',
    );
    expect(authority.rulesetName).toBe('main — protected');
    expect(authority.packageRequiredContexts).toEqual([
      'Validate agentic/documentation conformance',
      'Implementation Verification',
      'CodeQL JavaScript/TypeScript',
    ]);
  });

  it('reads the named active ruleset and extracts required contexts', async () => {
    const fetchImpl: GitHubFetch = async (url) => {
      if (url.endsWith('/rulesets?per_page=100')) {
        return response([
          {
            id: 24024518,
            name: 'main — protected',
            target: 'branch',
            enforcement: 'active',
          },
        ]);
      }
      if (url.endsWith('/rulesets/24024518')) {
        return response({
          id: 24024518,
          name: 'main — protected',
          target: 'branch',
          enforcement: 'active',
          rules: [
            {
              type: 'required_status_checks',
              parameters: {
                required_status_checks: [
                  { context: 'Validate agentic/documentation conformance' },
                  { context: 'Implementation Verification' },
                  { context: 'CodeQL JavaScript/TypeScript' },
                ],
              },
            },
          ],
        });
      }
      return response({}, 404);
    };
    const client = new GitHubRestReadClient(fetchImpl);
    const ruleset = await client.readRulesetRequiredChecks('SethDKelly/Mudac', 'main — protected');
    expect(ruleset.requiredContexts).toEqual([
      'Validate agentic/documentation conformance',
      'Implementation Verification',
      'CodeQL JavaScript/TypeScript',
    ]);
  });

  it('fails closed when the named ruleset is missing', async () => {
    const client = new GitHubRestReadClient(async () => response([]));
    await expect(
      client.readRulesetRequiredChecks('SethDKelly/Mudac', 'main — protected'),
    ).rejects.toThrow('github_ruleset_not_found');
  });

  it('fails closed when duplicate same-name rulesets are returned', async () => {
    const client = new GitHubRestReadClient(async () =>
      response([
        { id: 1, name: 'main — protected', target: 'branch', enforcement: 'active' },
        { id: 2, name: 'main — protected', target: 'branch', enforcement: 'active' },
      ]),
    );
    await expect(
      client.readRulesetRequiredChecks('SethDKelly/Mudac', 'main — protected'),
    ).rejects.toThrow('github_ruleset_name_not_unique');
  });

  it('fails closed when the matching ruleset is inactive', async () => {
    const client = new GitHubRestReadClient(async () =>
      response([{ id: 1, name: 'main — protected', target: 'branch', enforcement: 'disabled' }]),
    );
    await expect(
      client.readRulesetRequiredChecks('SethDKelly/Mudac', 'main — protected'),
    ).rejects.toThrow('github_ruleset_inactive');
  });

  it('fails closed when required-status-check rule is absent', async () => {
    const fetchImpl: GitHubFetch = async (url) => {
      if (url.includes('?per_page=')) {
        return response([
          { id: 1, name: 'main — protected', target: 'branch', enforcement: 'active' },
        ]);
      }
      return response({
        id: 1,
        name: 'main — protected',
        target: 'branch',
        enforcement: 'active',
        rules: [{ type: 'pull_request', parameters: {} }],
      });
    };
    const client = new GitHubRestReadClient(fetchImpl);
    await expect(
      client.readRulesetRequiredChecks('SethDKelly/Mudac', 'main — protected'),
    ).rejects.toThrow('github_ruleset_required_status_checks_missing');
  });

  it('fails closed on malformed required context entries', async () => {
    const fetchImpl: GitHubFetch = async (url) => {
      if (url.includes('?per_page=')) {
        return response([
          { id: 1, name: 'main — protected', target: 'branch', enforcement: 'active' },
        ]);
      }
      return response({
        id: 1,
        name: 'main — protected',
        target: 'branch',
        enforcement: 'active',
        rules: [
          {
            type: 'required_status_checks',
            parameters: {
              required_status_checks: [{ context: ' Implementation Verification' }],
            },
          },
        ],
      });
    };
    const client = new GitHubRestReadClient(fetchImpl);
    await expect(
      client.readRulesetRequiredChecks('SethDKelly/Mudac', 'main — protected'),
    ).rejects.toThrow('github_ruleset_required_context_malformed');
  });

  it('fails closed when ruleset list completeness cannot be established', async () => {
    const client = new GitHubRestReadClient(async () =>
      response(
        Array.from({ length: 100 }, (_, index) => ({
          id: index + 1,
          name: `ruleset-${index}`,
          target: 'branch',
          enforcement: 'active',
        })),
      ),
    );
    await expect(
      client.readRulesetRequiredChecks('SethDKelly/Mudac', 'main — protected'),
    ).rejects.toThrow('github_ruleset_list_pagination_incomplete');
  });
});

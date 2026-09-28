import type {
  CheckTruth,
  GitHubReadClient,
  PullRequestTruth,
  RefTruth,
  WorkflowTruth,
} from './model.js';

interface JsonResponse {
  ok: boolean;
  status: number;
  json(): Promise<unknown>;
}

export type GitHubFetch = (
  url: string,
  init: { method: 'GET'; headers: Readonly<Record<string, string>> },
) => Promise<JsonResponse>;

const defaultFetch: GitHubFetch = async (url, init) => fetch(url, init);

function record(value: unknown, context: string): Record<string, unknown> {
  if (typeof value !== 'object' || value === null || Array.isArray(value)) {
    throw new Error(`invalid_github_response:${context}`);
  }
  return value as Record<string, unknown>;
}

function text(value: unknown, context: string): string {
  if (typeof value !== 'string' || value.length === 0) {
    throw new Error(`invalid_github_response:${context}`);
  }
  return value;
}

function numberValue(value: unknown, context: string): number {
  if (typeof value !== 'number' || !Number.isFinite(value)) {
    throw new Error(`invalid_github_response:${context}`);
  }
  return value;
}

function booleanValue(value: unknown, context: string): boolean {
  if (typeof value !== 'boolean') throw new Error(`invalid_github_response:${context}`);
  return value;
}

function nullableText(value: unknown, context: string): string | null {
  if (value === null) return null;
  return text(value, context);
}

function conclusion(value: unknown): CheckTruth['conclusion'] {
  if (value === null) return null;
  if (
    value === 'success' ||
    value === 'failure' ||
    value === 'cancelled' ||
    value === 'timed_out' ||
    value === 'action_required' ||
    value === 'neutral' ||
    value === 'skipped'
  ) {
    return value;
  }
  throw new Error('invalid_github_response:conclusion');
}

function status(value: unknown): CheckTruth['status'] {
  if (value === 'queued' || value === 'in_progress' || value === 'completed') return value;
  throw new Error('invalid_github_response:status');
}

function repositoryPath(repositoryFullName: string): string {
  const parts = repositoryFullName.split('/');
  if (
    parts.length !== 2 ||
    !parts[0] ||
    !parts[1] ||
    !/^[A-Za-z0-9_.-]+$/.test(parts[0]) ||
    !/^[A-Za-z0-9_.-]+$/.test(parts[1])
  ) {
    throw new Error('invalid_repository_full_name');
  }
  return `${encodeURIComponent(parts[0])}/${encodeURIComponent(parts[1])}`;
}

export class GitHubRestReadClient implements GitHubReadClient {
  readonly #fetch: GitHubFetch;
  readonly #apiBase: string;

  constructor(fetchImpl: GitHubFetch = defaultFetch, apiBase = 'https://api.github.com') {
    if (apiBase !== 'https://api.github.com') {
      throw new Error('github_api_base_must_be_canonical');
    }
    this.#fetch = fetchImpl;
    this.#apiBase = apiBase;
  }

  async #get(repositoryFullName: string, suffix: string): Promise<unknown> {
    const repo = repositoryPath(repositoryFullName);
    const url = `${this.#apiBase}/repos/${repo}${suffix}`;
    const response = await this.#fetch(url, {
      method: 'GET',
      headers: {
        Accept: 'application/vnd.github+json',
        'X-GitHub-Api-Version': '2022-11-28',
        'User-Agent': 'mudac-aut001-read-only-shadow',
      },
    });
    if (!response.ok) {
      throw new Error(`github_read_failed:${response.status}`);
    }
    return response.json();
  }

  async readPullRequest(
    repositoryFullName: string,
    pullRequestNumber: number,
  ): Promise<PullRequestTruth> {
    if (!Number.isSafeInteger(pullRequestNumber) || pullRequestNumber <= 0) {
      throw new Error('invalid_pull_request_number');
    }
    const value = record(
      await this.#get(repositoryFullName, `/pulls/${pullRequestNumber}`),
      'pull_request',
    );
    const head = record(value.head, 'pull_request.head');
    const base = record(value.base, 'pull_request.base');
    const baseRef = text(base.ref, 'pull_request.base.ref');
    return {
      number: numberValue(value.number, 'pull_request.number'),
      state: text(value.state, 'pull_request.state') === 'open' ? 'open' : 'closed',
      merged: booleanValue(value.merged, 'pull_request.merged'),
      draft: booleanValue(value.draft, 'pull_request.draft'),
      headSha: text(head.sha, 'pull_request.head.sha'),
      baseRef,
      baseSha: text(base.sha, 'pull_request.base.sha'),
      mergeCommitSha: nullableText(value.merge_commit_sha, 'pull_request.merge_commit_sha'),
    };
  }

  async readRef(repositoryFullName: string, ref: string): Promise<RefTruth> {
    if (ref.trim().length === 0) throw new Error('invalid_ref');
    const value = record(
      await this.#get(repositoryFullName, `/git/ref/heads/${encodeURIComponent(ref)}`),
      'ref',
    );
    const object = record(value.object, 'ref.object');
    return { ref, sha: text(object.sha, 'ref.object.sha') };
  }

  async readChecks(repositoryFullName: string, headSha: string): Promise<readonly CheckTruth[]> {
    const value = record(
      await this.#get(
        repositoryFullName,
        `/commits/${encodeURIComponent(headSha)}/check-runs?per_page=100`,
      ),
      'check_runs',
    );
    const raw = value.check_runs;
    if (!Array.isArray(raw)) throw new Error('invalid_github_response:check_runs.list');
    const total = numberValue(value.total_count, 'check_runs.total_count');
    if (total > raw.length) throw new Error('github_check_truth_pagination_incomplete');

    return raw.map((item, index) => {
      const entry = record(item, `check_runs.${index}`);
      const id = numberValue(entry.id, `check_runs.${index}.id`);
      return {
        id,
        name: text(entry.name, `check_runs.${index}.name`),
        headSha: text(entry.head_sha, `check_runs.${index}.head_sha`),
        attempt: id,
        status: status(entry.status),
        conclusion: conclusion(entry.conclusion),
      };
    });
  }

  async readWorkflows(
    repositoryFullName: string,
    headSha: string,
  ): Promise<readonly WorkflowTruth[]> {
    const value = record(
      await this.#get(
        repositoryFullName,
        `/actions/runs?head_sha=${encodeURIComponent(headSha)}&per_page=100`,
      ),
      'workflow_runs',
    );
    const raw = value.workflow_runs;
    if (!Array.isArray(raw)) throw new Error('invalid_github_response:workflow_runs.list');
    const total = numberValue(value.total_count, 'workflow_runs.total_count');
    if (total > raw.length) throw new Error('github_workflow_truth_pagination_incomplete');

    return raw.map((item, index) => {
      const entry = record(item, `workflow_runs.${index}`);
      return {
        id: numberValue(entry.id, `workflow_runs.${index}.id`),
        name: text(entry.name, `workflow_runs.${index}.name`),
        headSha: text(entry.head_sha, `workflow_runs.${index}.head_sha`),
        attempt: numberValue(entry.run_attempt, `workflow_runs.${index}.run_attempt`),
        status: status(entry.status),
        conclusion: conclusion(entry.conclusion),
      };
    });
  }

  async isAncestor(
    repositoryFullName: string,
    ancestorSha: string,
    descendantSha: string,
  ): Promise<boolean | 'UNKNOWN'> {
    const value = record(
      await this.#get(
        repositoryFullName,
        `/compare/${encodeURIComponent(ancestorSha)}...${encodeURIComponent(descendantSha)}`,
      ),
      'compare',
    );
    const comparison = text(value.status, 'compare.status');
    if (comparison === 'identical' || comparison === 'ahead') return true;
    if (comparison === 'behind' || comparison === 'diverged') return false;
    return 'UNKNOWN';
  }
}

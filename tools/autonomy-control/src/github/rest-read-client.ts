import type {
  CheckTruth,
  GitHubReadClient,
  LiveRulesetRequiredChecks,
  PullRequestTruth,
  RefTruth,
  RulesetRefNameCondition,
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

const RULESET_PAGE_SIZE = 100;

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

function pullRequestState(value: unknown): PullRequestTruth['state'] {
  if (value === 'open' || value === 'closed') return value;
  throw new Error('invalid_github_response:pull_request.state');
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

function stringList(value: unknown, context: string): readonly string[] {
  if (!Array.isArray(value)) {
    throw new Error(`invalid_github_response:${context}`);
  }
  return value.map((item, index) => {
    const entry = text(item, `${context}.${index}`);
    if (entry !== entry.trim()) {
      throw new Error(`invalid_github_response:${context}.${index}.whitespace`);
    }
    return entry;
  });
}

export function parseRulesetRefNameCondition(conditions: unknown): RulesetRefNameCondition {
  if (conditions === undefined || conditions === null) {
    throw new Error('github_ruleset_conditions_missing');
  }
  const conditionsRecord = record(conditions, 'ruleset_details.conditions');
  if (!('ref_name' in conditionsRecord) || conditionsRecord.ref_name === undefined) {
    throw new Error('github_ruleset_ref_name_missing');
  }
  const refName = record(conditionsRecord.ref_name, 'ruleset_details.conditions.ref_name');
  if (!('include' in refName) || !('exclude' in refName)) {
    throw new Error('github_ruleset_ref_name_malformed');
  }
  const include = stringList(refName.include, 'ruleset_details.conditions.ref_name.include');
  const exclude = stringList(refName.exclude, 'ruleset_details.conditions.ref_name.exclude');
  if (include.length === 0) {
    throw new Error('github_ruleset_ref_name_include_empty');
  }
  return { include, exclude };
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
      state: pullRequestState(value.state),
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
      return {
        id: numberValue(entry.id, `check_runs.${index}.id`),
        name: text(entry.name, `check_runs.${index}.name`),
        headSha: text(entry.head_sha, `check_runs.${index}.head_sha`),
        status: status(entry.status),
        conclusion: conclusion(entry.conclusion),
        startedAt: nullableText(entry.started_at ?? null, `check_runs.${index}.started_at`),
        completedAt: nullableText(entry.completed_at ?? null, `check_runs.${index}.completed_at`),
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

  async readRulesetRequiredChecks(
    repositoryFullName: string,
    rulesetName: string,
  ): Promise<LiveRulesetRequiredChecks> {
    if (rulesetName.trim().length === 0 || rulesetName !== rulesetName.trim()) {
      throw new Error('invalid_ruleset_name');
    }

    const listed = await this.#get(repositoryFullName, `/rulesets?per_page=${RULESET_PAGE_SIZE}`);
    if (!Array.isArray(listed)) {
      throw new Error('invalid_github_response:rulesets.list');
    }
    if (listed.length >= RULESET_PAGE_SIZE) {
      throw new Error('github_ruleset_list_pagination_incomplete');
    }

    const matching: Array<{ id: number; name: string; enforcement: string; target: string }> = [];
    for (const [index, item] of listed.entries()) {
      const entry = record(item, `rulesets.${index}`);
      const name = text(entry.name, `rulesets.${index}.name`);
      if (name !== rulesetName) continue;
      matching.push({
        id: numberValue(entry.id, `rulesets.${index}.id`),
        name,
        enforcement: text(entry.enforcement, `rulesets.${index}.enforcement`),
        target: text(entry.target, `rulesets.${index}.target`),
      });
    }

    if (matching.length === 0) {
      throw new Error('github_ruleset_not_found');
    }
    if (matching.length > 1) {
      throw new Error('github_ruleset_name_not_unique');
    }

    const selected = matching[0];
    if (!selected) throw new Error('github_ruleset_not_found');
    if (selected.enforcement !== 'active') {
      throw new Error('github_ruleset_inactive');
    }
    if (selected.target !== 'branch') {
      throw new Error('github_ruleset_unsupported_target');
    }

    const details = record(
      await this.#get(repositoryFullName, `/rulesets/${selected.id}`),
      'ruleset_details',
    );
    if (text(details.name, 'ruleset_details.name') !== rulesetName) {
      throw new Error('github_ruleset_detail_name_mismatch');
    }
    if (text(details.enforcement, 'ruleset_details.enforcement') !== 'active') {
      throw new Error('github_ruleset_inactive');
    }
    if (text(details.target, 'ruleset_details.target') !== 'branch') {
      throw new Error('github_ruleset_unsupported_target');
    }

    const refNameCondition = parseRulesetRefNameCondition(details.conditions);

    const rules = details.rules;
    if (!Array.isArray(rules)) throw new Error('invalid_github_response:ruleset_details.rules');

    const requiredStatusRules = rules.filter((item, index) => {
      const entry = record(item, `ruleset_details.rules.${index}`);
      return entry.type === 'required_status_checks';
    });
    if (requiredStatusRules.length === 0) {
      throw new Error('github_ruleset_required_status_checks_missing');
    }
    if (requiredStatusRules.length > 1) {
      throw new Error('github_ruleset_required_status_checks_ambiguous');
    }

    const rule = record(requiredStatusRules[0], 'ruleset_details.required_status_checks');
    const parameters = record(rule.parameters, 'ruleset_details.required_status_checks.parameters');
    const required = parameters.required_status_checks;
    if (!Array.isArray(required) || required.length === 0) {
      throw new Error('github_ruleset_required_contexts_incomplete');
    }

    const requiredContexts = required.map((item, index) => {
      const entry = record(item, `ruleset_details.required_status_checks.${index}`);
      const context = text(
        entry.context,
        `ruleset_details.required_status_checks.${index}.context`,
      );
      if (context !== context.trim()) {
        throw new Error('github_ruleset_required_context_malformed');
      }
      return context;
    });

    return {
      rulesetId: selected.id,
      rulesetName: selected.name,
      enforcement: 'active',
      target: 'branch',
      requiredContexts,
      refNameCondition,
    };
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

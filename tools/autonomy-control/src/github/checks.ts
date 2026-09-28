import type { CheckTruth, RequiredCheckEvaluation, WorkflowTruth } from './model.js';

interface CheckLike {
  name: string;
  headSha: string;
  attempt: number;
  status: 'queued' | 'in_progress' | 'completed';
  conclusion:
    | 'success'
    | 'failure'
    | 'cancelled'
    | 'timed_out'
    | 'action_required'
    | 'neutral'
    | 'skipped'
    | null;
}

function selectLatestForName(
  records: readonly CheckLike[],
  name: string,
  candidateSha: string,
): { kind: 'MISSING' } | { kind: 'AMBIGUOUS' } | { kind: 'FOUND'; record: CheckLike } {
  const matching = records.filter((item) => item.name === name && item.headSha === candidateSha);
  if (matching.length === 0) return { kind: 'MISSING' };

  const maxAttempt = Math.max(...matching.map((item) => item.attempt));
  const latest = matching.filter((item) => item.attempt === maxAttempt);
  const first = latest[0];
  if (!first) return { kind: 'MISSING' };

  if (latest.some((item) => item.status !== first.status || item.conclusion !== first.conclusion)) {
    return { kind: 'AMBIGUOUS' };
  }

  return { kind: 'FOUND', record: first };
}

export function evaluateRequiredChecks(
  checks: readonly CheckTruth[],
  workflows: readonly WorkflowTruth[],
  candidateSha: string,
  requiredNames: readonly string[],
): RequiredCheckEvaluation {
  if (
    requiredNames.length === 0 ||
    requiredNames.some((name) => name.trim().length === 0 || name !== name.trim())
  ) {
    return {
      disposition: 'INCONCLUSIVE',
      reason: 'required_check_set_missing_or_invalid',
      matched: {},
      missing: [],
    };
  }

  const records: readonly CheckLike[] = [...checks, ...workflows];
  const matched: Record<string, { attempt: number; status: string; conclusion: string | null }> =
    {};
  const missing: string[] = [];

  for (const name of [...new Set(requiredNames)].sort()) {
    const selected = selectLatestForName(records, name, candidateSha);
    if (selected.kind === 'AMBIGUOUS') {
      return {
        disposition: 'INCONCLUSIVE',
        reason: `ambiguous_latest_required_check:${name}`,
        matched,
        missing,
      };
    }
    if (selected.kind === 'MISSING') {
      missing.push(name);
      continue;
    }

    const { record } = selected;
    matched[name] = {
      attempt: record.attempt,
      status: record.status,
      conclusion: record.conclusion,
    };

    if (record.status !== 'completed') {
      return {
        disposition: 'NOT_READY',
        reason: `required_check_not_terminal:${name}`,
        matched,
        missing,
      };
    }
    if (record.conclusion !== 'success') {
      return {
        disposition: 'FAILED',
        reason: `required_check_not_success:${name}:${record.conclusion ?? 'null'}`,
        matched,
        missing,
      };
    }
  }

  if (missing.length > 0) {
    return {
      disposition: 'NOT_READY',
      reason: `required_checks_missing:${missing.join(',')}`,
      matched,
      missing,
    };
  }

  return {
    disposition: 'PASS',
    reason: 'all_required_checks_terminal_success_on_exact_candidate',
    matched,
    missing,
  };
}

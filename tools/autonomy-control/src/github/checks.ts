import type { CheckTruth, RequiredCheckEvaluation } from './model.js';

function currentnessTimestamp(check: CheckTruth): string | null {
  if (check.completedAt) return check.completedAt;
  if (check.startedAt) return check.startedAt;
  return null;
}

function selectCurrentCheckRun(
  checks: readonly CheckTruth[],
  name: string,
  candidateSha: string,
):
  | { kind: 'MISSING' }
  | { kind: 'AMBIGUOUS'; reason: string }
  | { kind: 'FOUND'; record: CheckTruth } {
  const matching = checks.filter((item) => item.name === name && item.headSha === candidateSha);
  if (matching.length === 0) return { kind: 'MISSING' };
  if (matching.length === 1) {
    const only = matching[0];
    if (!only) return { kind: 'MISSING' };
    return { kind: 'FOUND', record: only };
  }

  const withTimestamps = matching.map((item) => ({
    item,
    timestamp: currentnessTimestamp(item),
  }));
  if (withTimestamps.some((entry) => entry.timestamp === null)) {
    return {
      kind: 'AMBIGUOUS',
      reason: `ambiguous_check_run_currentness_missing_timestamp:${name}`,
    };
  }

  const sorted = [...withTimestamps].sort((left, right) => {
    const leftTs = left.timestamp ?? '';
    const rightTs = right.timestamp ?? '';
    if (leftTs < rightTs) return 1;
    if (leftTs > rightTs) return -1;
    return 0;
  });

  const newest = sorted[0];
  if (!newest) return { kind: 'MISSING' };
  const tied = sorted.filter((entry) => entry.timestamp === newest.timestamp);
  if (tied.length !== 1) {
    return {
      kind: 'AMBIGUOUS',
      reason: `ambiguous_check_run_currentness_tie:${name}`,
    };
  }

  return { kind: 'FOUND', record: newest.item };
}

export function evaluateRequiredChecks(
  checks: readonly CheckTruth[],
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

  const matched: Record<
    string,
    {
      checkRunId: number;
      status: string;
      conclusion: string | null;
      startedAt: string | null;
      completedAt: string | null;
    }
  > = {};
  const missing: string[] = [];

  for (const name of [...new Set(requiredNames)].sort()) {
    const selected = selectCurrentCheckRun(checks, name, candidateSha);
    if (selected.kind === 'AMBIGUOUS') {
      return {
        disposition: 'INCONCLUSIVE',
        reason: selected.reason,
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
      checkRunId: record.id,
      status: record.status,
      conclusion: record.conclusion,
      startedAt: record.startedAt,
      completedAt: record.completedAt,
    };

    if (record.status !== 'completed') {
      return {
        disposition: 'NOT_READY',
        reason: `required_check_not_terminal:${name}`,
        matched,
        missing,
      };
    }
    if (record.conclusion === 'skipped') {
      return {
        disposition: 'INCONCLUSIVE',
        reason: `required_check_incompatibly_skipped:${name}`,
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

export function isTerminalRequiredCheckDisposition(
  disposition: RequiredCheckEvaluation['disposition'],
): boolean {
  return disposition === 'PASS' || disposition === 'FAILED';
}

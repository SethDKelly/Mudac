import type { CheckTruth, RequiredCheckEvaluation } from './model.js';

/**
 * Authoritative GitHub check-run timestamps are accepted only as canonical UTC
 * instants: YYYY-MM-DDTHH:mm:ss[.fraction]Z. Numeric-offset forms are rejected
 * so the control plane never reimplements general ISO-8601 offset normalization.
 */
const AUTHORITATIVE_UTC_INSTANT =
  /^(\d{4})-(\d{2})-(\d{2})T(\d{2}):(\d{2}):(\d{2})(?:\.(\d{1,9}))?Z$/;

function daysInMonth(year: number, month: number): number {
  if (month === 2) {
    const leap = year % 4 === 0 && (year % 100 !== 0 || year % 400 === 0);
    return leap ? 29 : 28;
  }
  if (month === 4 || month === 6 || month === 9 || month === 11) return 30;
  return 31;
}

/**
 * Parse an authoritative GitHub check timestamp into a comparable instant.
 * Rejects malformed, non-instant, non-UTC-Z, impossible-calendar, or non-finite
 * values fail-closed. Lexical string ordering is never authority for currentness.
 * Do not use Date.parse alone for calendar validity.
 */
export function parseComparableInstant(
  value: string | null,
  field: 'startedAt' | 'completedAt',
): { kind: 'OK'; ms: number } | { kind: 'INVALID'; reason: string } | { kind: 'MISSING' } {
  if (value === null) return { kind: 'MISSING' };
  if (typeof value !== 'string' || value.trim().length === 0 || value !== value.trim()) {
    return { kind: 'INVALID', reason: `malformed_${field}` };
  }

  const match = AUTHORITATIVE_UTC_INSTANT.exec(value);
  if (!match) {
    return { kind: 'INVALID', reason: `malformed_${field}` };
  }

  const year = Number(match[1]);
  const month = Number(match[2]);
  const day = Number(match[3]);
  const hour = Number(match[4]);
  const minute = Number(match[5]);
  const second = Number(match[6]);
  const fraction = match[7] ?? '';

  if (
    !Number.isInteger(year) ||
    !Number.isInteger(month) ||
    !Number.isInteger(day) ||
    !Number.isInteger(hour) ||
    !Number.isInteger(minute) ||
    !Number.isInteger(second) ||
    month < 1 ||
    month > 12 ||
    day < 1 ||
    day > daysInMonth(year, month) ||
    hour > 23 ||
    minute > 59 ||
    second > 59
  ) {
    return { kind: 'INVALID', reason: `malformed_${field}` };
  }

  const millisecond = fraction.length === 0 ? 0 : Number(fraction.padEnd(3, '0').slice(0, 3));
  if (!Number.isInteger(millisecond) || millisecond < 0 || millisecond > 999) {
    return { kind: 'INVALID', reason: `malformed_${field}` };
  }

  const ms = Date.UTC(year, month - 1, day, hour, minute, second, millisecond);
  if (!Number.isFinite(ms)) {
    return { kind: 'INVALID', reason: `malformed_${field}` };
  }

  const utc = new Date(ms);
  if (
    utc.getUTCFullYear() !== year ||
    utc.getUTCMonth() + 1 !== month ||
    utc.getUTCDate() !== day ||
    utc.getUTCHours() !== hour ||
    utc.getUTCMinutes() !== minute ||
    utc.getUTCSeconds() !== second ||
    utc.getUTCMilliseconds() !== millisecond
  ) {
    return { kind: 'INVALID', reason: `malformed_${field}` };
  }

  return { kind: 'OK', ms };
}

function currentnessInstant(
  check: CheckTruth,
):
  | { kind: 'OK'; ms: number; source: 'completedAt' | 'startedAt' }
  | { kind: 'INVALID'; reason: string }
  | { kind: 'MISSING'; reason: string } {
  const started = parseComparableInstant(check.startedAt, 'startedAt');
  const completed = parseComparableInstant(check.completedAt, 'completedAt');

  if (started.kind === 'INVALID') {
    return { kind: 'INVALID', reason: started.reason };
  }
  if (completed.kind === 'INVALID') {
    return { kind: 'INVALID', reason: completed.reason };
  }

  if (check.status === 'completed') {
    if (completed.kind === 'MISSING') {
      return {
        kind: 'INVALID',
        reason: 'completed_status_without_completedAt',
      };
    }
    if (started.kind === 'OK' && completed.ms < started.ms) {
      return {
        kind: 'INVALID',
        reason: 'completedAt_before_startedAt',
      };
    }
    return { kind: 'OK', ms: completed.ms, source: 'completedAt' };
  }

  // Non-terminal runs may use startedAt for currentness ordering among peers.
  if (completed.kind === 'OK') {
    // A non-completed status with a completion timestamp is contradictory.
    return {
      kind: 'INVALID',
      reason: 'contradictory_timestamp_envelope',
    };
  }
  if (started.kind === 'OK') {
    return { kind: 'OK', ms: started.ms, source: 'startedAt' };
  }
  return {
    kind: 'MISSING',
    reason: 'currentness_timestamp_missing',
  };
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

  const resolved = matching.map((item) => ({
    item,
    instant: currentnessInstant(item),
  }));

  const invalid = resolved.find((entry) => entry.instant.kind === 'INVALID');
  if (invalid && invalid.instant.kind === 'INVALID') {
    return {
      kind: 'AMBIGUOUS',
      reason: `ambiguous_check_run_currentness_${invalid.instant.reason}:${name}`,
    };
  }

  if (matching.length === 1) {
    const only = resolved[0];
    if (!only) return { kind: 'MISSING' };
    if (only.instant.kind === 'MISSING') {
      return {
        kind: 'AMBIGUOUS',
        reason: `ambiguous_check_run_currentness_${only.instant.reason}:${name}`,
      };
    }
    return { kind: 'FOUND', record: only.item };
  }

  if (resolved.some((entry) => entry.instant.kind === 'MISSING')) {
    return {
      kind: 'AMBIGUOUS',
      reason: `ambiguous_check_run_currentness_missing_timestamp:${name}`,
    };
  }

  const withInstants = resolved.map((entry) => {
    if (entry.instant.kind !== 'OK') {
      throw new Error('unreachable_currentness_state');
    }
    return { item: entry.item, ms: entry.instant.ms };
  });

  const newestMs = Math.max(...withInstants.map((entry) => entry.ms));
  const tied = withInstants.filter((entry) => entry.ms === newestMs);
  if (tied.length !== 1) {
    return {
      kind: 'AMBIGUOUS',
      reason: `ambiguous_check_run_currentness_tie:${name}`,
    };
  }

  const newest = tied[0];
  if (!newest) return { kind: 'MISSING' };
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

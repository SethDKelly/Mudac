import type {
  LiveRulesetRequiredChecks,
  PackageRequiredCheckAuthority,
  RequiredCheckAuthorityComparison,
} from './model.js';

function sortedUnique(values: readonly string[]): readonly string[] {
  return [...new Set(values)].sort();
}

function sameSet(left: readonly string[], right: readonly string[]): boolean {
  const a = sortedUnique(left);
  const b = sortedUnique(right);
  return a.length === b.length && a.every((item, index) => item === b[index]);
}

export function compareRequiredCheckAuthority(
  packageAuthority: PackageRequiredCheckAuthority,
  liveRuleset: LiveRulesetRequiredChecks,
): RequiredCheckAuthorityComparison {
  const packageContexts = sortedUnique(packageAuthority.packageRequiredContexts);
  const liveContexts = sortedUnique(liveRuleset.requiredContexts);

  if (packageAuthority.rulesetName !== liveRuleset.rulesetName) {
    return {
      status: 'MISMATCH',
      reason: 'package_and_live_ruleset_name_disagree',
      packageAuthority,
      liveRuleset,
      packageContexts,
      liveContexts,
    };
  }

  if (packageAuthority.rulesetEnforcement !== 'active' || liveRuleset.enforcement !== 'active') {
    return {
      status: 'INCONCLUSIVE',
      reason: 'ruleset_enforcement_not_active',
      packageAuthority,
      liveRuleset,
      packageContexts,
      liveContexts,
    };
  }

  if (packageContexts.length === 0 || liveContexts.length === 0) {
    return {
      status: 'INCONCLUSIVE',
      reason: 'required_check_contexts_incomplete',
      packageAuthority,
      liveRuleset,
      packageContexts,
      liveContexts,
    };
  }

  if (!sameSet(packageContexts, liveContexts)) {
    return {
      status: 'MISMATCH',
      reason: 'package_and_live_required_check_sets_differ',
      packageAuthority,
      liveRuleset,
      packageContexts,
      liveContexts,
    };
  }

  return {
    status: 'AGREED',
    requiredContexts: packageContexts,
    packageAuthority,
    liveRuleset,
  };
}

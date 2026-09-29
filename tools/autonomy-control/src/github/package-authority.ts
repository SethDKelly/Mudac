import { readFileSync } from 'node:fs';

import type { PackageRequiredCheckAuthority } from './model.js';

function record(value: unknown, context: string): Record<string, unknown> {
  if (typeof value !== 'object' || value === null || Array.isArray(value)) {
    throw new Error(`invalid_package_authority:${context}`);
  }
  return value as Record<string, unknown>;
}

function text(value: unknown, context: string): string {
  if (typeof value !== 'string' || value.trim().length === 0) {
    throw new Error(`invalid_package_authority:${context}`);
  }
  return value;
}

function stringArray(value: unknown, context: string): readonly string[] {
  if (!Array.isArray(value) || value.length === 0) {
    throw new Error(`invalid_package_authority:${context}`);
  }
  const items = value.map((item, index) => text(item, `${context}.${index}`));
  if (items.some((item) => item !== item.trim())) {
    throw new Error(`invalid_package_authority:${context}.whitespace`);
  }
  return items;
}

export function loadPackageRequiredCheckAuthority(
  packageContractPath: string,
): PackageRequiredCheckAuthority {
  const raw = JSON.parse(readFileSync(packageContractPath, 'utf8')) as unknown;
  const root = record(raw, 'root');
  const baseline = record(root.exact_entry_baseline, 'exact_entry_baseline');
  return {
    packageContractPath,
    packageSchema: text(root.schema, 'schema'),
    rulesetName: text(baseline.main_ruleset, 'exact_entry_baseline.main_ruleset'),
    rulesetEnforcement: text(
      baseline.main_ruleset_enforcement,
      'exact_entry_baseline.main_ruleset_enforcement',
    ),
    packageRequiredContexts: stringArray(
      baseline.required_checks,
      'exact_entry_baseline.required_checks',
    ),
  };
}

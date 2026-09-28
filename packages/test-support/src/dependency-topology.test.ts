import { spawnSync } from 'node:child_process';
import { mkdtempSync, mkdirSync, readFileSync, rmSync, writeFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { dirname, join, relative, resolve } from 'node:path';
import { beforeAll, describe, expect, it } from 'vitest';

const repository = resolve(import.meta.dirname, '../../..');

// Independent BND-007 expectations: importers consume upstream authority.
const upstream: Record<string, string[]> = {
  competition: [],
  'identity-access': ['competition'],
  evaluation: ['competition', 'identity-access'],
  outcomes: ['competition', 'identity-access', 'evaluation'],
  'external-representation': ['competition', 'identity-access', 'evaluation', 'outcomes'],
};
const owners = Object.keys(upstream);
interface Violation {
  from: string;
  to: string;
  rule: { name: string };
}
let violations: Violation[];
let modules: { source: string; dependencies: { resolved: string; couldNotResolve: boolean }[] }[];

// Repair regressions: [consumer, target, pure type import, expected rule names].
const repairProbes: [string, string, boolean, string[]][] = [
  ...[
    'apps/api',
    'packages/application',
    'packages/projections',
    'packages/modules/external-representation/src',
  ].map((consumer): [string, string, boolean, string[]] => [
    `${consumer}/use-outside.ts`,
    'packages/modules/outcomes/outside.ts',
    false,
    ['outcomes-exposes-only-public-contracts'],
  ]),
  [
    'packages/modules/outcomes/src/use-own-outside.ts',
    'packages/modules/outcomes/outside.ts',
    false,
    [],
  ],
  [
    'packages/modules/evaluation/src/downstream-type.ts',
    'packages/modules/outcomes/src/public.ts',
    true,
    ['evaluation-uses-only-upstream-owners'],
  ],
  [
    'packages/modules/external-representation/src/private-type.ts',
    'packages/modules/outcomes/src/private.ts',
    true,
    ['outcomes-exposes-only-public-contracts'],
  ],
  [
    'packages/application/outside-type.ts',
    'packages/modules/outcomes/outside.ts',
    true,
    ['outcomes-exposes-only-public-contracts'],
  ],
  [
    'packages/modules/outcomes/src/upstream-type.ts',
    'packages/modules/evaluation/src/public.ts',
    true,
    [],
  ],
  [
    'packages/modules/outcomes/src/self-private-type.ts',
    'packages/modules/outcomes/src/private.ts',
    true,
    [],
  ],
];

beforeAll(() => {
  const fixture = mkdtempSync(join(tmpdir(), 'mudac-topology-'));
  const write = (path: string, contents: string) => {
    const destination = join(fixture, path);
    mkdirSync(dirname(destination), { recursive: true });
    writeFileSync(destination, contents);
  };
  const edge = (from: string, to: string, typeOnly = false) => {
    const specifier = relative(dirname(from), to).replaceAll('\\', '/');
    const path = specifier.startsWith('.') ? specifier : `./${specifier}`;
    write(
      from,
      typeOnly
        ? `import type { FixtureType } from '${path}';\nexport type ConsumerType = FixtureType;\n`
        : `import '${path}';\n`,
    );
  };
  try {
    // Exercise the actual cruiser CLI and repository rules, including resolution.
    write('rules.cjs', readFileSync(join(repository, '.dependency-cruiser.cjs'), 'utf8'));
    write('tsconfig.node.json', '{"compilerOptions":{"module":"NodeNext"}}');
    for (const owner of [...owners, 'undeclared']) {
      write(`packages/modules/${owner}/src/public.ts`, 'export type FixtureType = string;\n');
      write(`packages/modules/${owner}/src/private.ts`, 'export type FixtureType = string;\n');
    }
    write('packages/modules/outcomes/outside.ts', 'export type FixtureType = string;\n');
    for (const [from, to, typeOnly] of repairProbes) edge(from, to, typeOnly);
    for (const from of owners) {
      for (const to of [...owners, 'undeclared']) {
        edge(`packages/modules/${from}/src/use-${to}.ts`, `packages/modules/${to}/src/public.ts`);
        edge(
          `packages/modules/${from}/src/private-${to}.ts`,
          `packages/modules/${to}/src/private.ts`,
        );
      }
      edge(`apps/api/${from}.ts`, `packages/modules/${from}/src/public.ts`);
      edge(`apps/api/private-${from}.ts`, `packages/modules/${from}/src/private.ts`);
      edge(
        `packages/modules/undeclared/src/use-${from}.ts`,
        `packages/modules/${from}/src/public.ts`,
      );
    }
    edge(
      'packages/modules/evaluation/src/cycle-a.ts',
      'packages/modules/evaluation/src/cycle-b.ts',
    );
    edge(
      'packages/modules/evaluation/src/cycle-b.ts',
      'packages/modules/evaluation/src/cycle-a.ts',
    );
    const result = spawnSync(
      process.execPath,
      [
        join(repository, 'node_modules/dependency-cruiser/bin/dependency-cruise.mjs'),
        'apps',
        'packages',
        '--config',
        'rules.cjs',
        '--output-type',
        'json',
      ],
      { cwd: fixture, encoding: 'utf8' },
    );
    expect(result.error).toBeUndefined();
    // The JSON reporter exits zero even with violations; assert its evidence below.
    expect(result.status, result.stderr).toBe(0);
    const report = JSON.parse(result.stdout) as {
      summary: { violations: Violation[] };
      modules: typeof modules;
    };
    violations = report.summary.violations;
    modules = report.modules;
  } finally {
    rmSync(fixture, { recursive: true, force: true });
  }
}, 30_000);

const rulesFor = (from: string) =>
  violations.filter((violation) => violation.from === from).map((violation) => violation.rule.name);

describe('accepted five-owner topology', () => {
  for (const [from, to, typeOnly, expectedRules] of repairProbes) {
    it(`${from} ${typeOnly ? 'type' : 'value'} import respects the full package seam and direction`, () => {
      // An absent edge is not evidence that an allowed type dependency was checked.
      expect(modules.find((module) => module.source === from)?.dependencies).toEqual(
        expect.arrayContaining([expect.objectContaining({ resolved: to, couldNotResolve: false })]),
      );
      expect(rulesFor(from)).toEqual(expectedRules);
    });
  }
  for (const from of owners) {
    for (const to of owners) {
      it(`${from} ${from === to || upstream[from]?.includes(to) ? 'may' : 'may not'} consume ${to}`, () => {
        const allowed = from === to || upstream[from]?.includes(to);
        expect(rulesFor(`packages/modules/${from}/src/use-${to}.ts`)).toEqual(
          allowed ? [] : [`${from}-uses-only-upstream-owners`],
        );
      });
      it(`${from} respects ${to}'s private seam`, () => {
        const rules = rulesFor(`packages/modules/${from}/src/private-${to}.ts`);
        if (from === to) expect(rules).toEqual([]);
        else expect(rules).toContain(`${to}-exposes-only-public-contracts`);
      });
    }
    it(`${from} rejects undeclared owner coupling in both directions`, () => {
      expect(rulesFor(`packages/modules/${from}/src/use-undeclared.ts`)).toEqual([
        `${from}-uses-only-upstream-owners`,
      ]);
      expect(rulesFor(`packages/modules/undeclared/src/use-${from}.ts`)).toEqual([
        'undeclared-owners-do-not-depend-on-modules',
      ]);
    });
    it(`application code uses only ${from}'s public seam`, () => {
      expect(rulesFor(`apps/api/${from}.ts`)).toEqual([]);
      expect(rulesFor(`apps/api/private-${from}.ts`)).toEqual([
        `${from}-exposes-only-public-contracts`,
      ]);
    });
    it(`${from} exports only its existing public entry point`, () => {
      const manifest = JSON.parse(
        readFileSync(join(repository, `packages/modules/${from}/package.json`), 'utf8'),
      ) as { exports: Record<string, string> };
      expect(manifest.exports).toEqual({ '.': './src/public.ts' });
    });
  }
  it('rejects production cycles', () => {
    expect(rulesFor('packages/modules/evaluation/src/cycle-a.ts')).toContain(
      'no-circular-production-dependencies',
    );
  });
});

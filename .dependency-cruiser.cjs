// BND-002 / BND-007: consumers may use earlier owners' public contracts.
// This order permits upstream consumption; it does not require direct imports.
const owners = [
  'competition',
  'identity-access',
  'evaluation',
  'outcomes',
  'external-representation',
];

module.exports = {
  forbidden: [
    {
      name: 'no-circular-production-dependencies',
      severity: 'error',
      from: { path: '^(apps|packages)/' },
      to: { circular: true },
    },
    {
      name: 'packages-do-not-depend-on-apps',
      severity: 'error',
      from: { path: '^packages/' },
      to: { path: '^apps/' },
    },
    {
      name: 'authoritative-modules-do-not-depend-on-coordination-or-projections',
      severity: 'error',
      from: { path: '^packages/modules/' },
      to: { path: '^packages/(application|projections)/' },
    },
    ...owners.map((owner, index) => ({
      name: `${owner}-uses-only-upstream-owners`,
      severity: 'error',
      from: { path: `^packages/modules/${owner}/` },
      to: {
        path: '^packages/modules/',
        pathNot: `^packages/modules/(${owners.slice(0, index + 1).join('|')})/`,
      },
    })),
    {
      name: 'undeclared-owners-do-not-depend-on-modules',
      severity: 'error',
      from: {
        path: '^packages/modules/',
        pathNot: `^packages/modules/(${owners.join('|')})/`,
      },
      to: { path: '^packages/modules/' },
    },
    // BND-006: relative imports must not bypass the package export seam.
    ...owners.map((owner) => ({
      name: `${owner}-exposes-only-public-contracts`,
      severity: 'error',
      from: { pathNot: `^packages/modules/${owner}/` },
      to: {
        path: `^packages/modules/${owner}/src/`,
        pathNot: `^packages/modules/${owner}/src/public\\.ts$`,
      },
    })),
    {
      name: 'foundation-remains-business-neutral',
      severity: 'error',
      from: { path: '^packages/foundation/' },
      to: {
        path: '^(apps|packages/(modules|application|projections|test-support))/',
      },
    },
    {
      name: 'web-does-not-import-server-implementation',
      severity: 'error',
      from: { path: '^apps/web/' },
      to: {
        path: '^(apps/(api|worker)|packages/(modules|application|projections|test-support))/',
      },
    },
    {
      name: 'production-does-not-import-test-support',
      severity: 'error',
      from: {
        path: '^(apps/(api|worker)|packages/(modules|application|projections|foundation))/',
      },
      to: { path: '^packages/test-support/' },
    },
  ],
  options: {
    doNotFollow: { path: 'node_modules' },
    exclude: { path: '(^|/)(dist|coverage|playwright-report|test-results)/' },
    tsConfig: { fileName: 'tsconfig.node.json' },
    enhancedResolveOptions: {
      exportsFields: ['exports'],
      conditionNames: ['types', 'import', 'default'],
    },
  },
};

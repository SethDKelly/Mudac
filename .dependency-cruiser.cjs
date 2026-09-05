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
    {
      name: 'competition-has-no-downstream-module-dependencies',
      severity: 'error',
      from: { path: '^packages/modules/competition/' },
      to: { path: '^packages/modules/(identity-access|judging-operations|evaluation|outcomes|external-representation)/' },
    },
    {
      name: 'identity-access-has-no-downstream-module-dependencies',
      severity: 'error',
      from: { path: '^packages/modules/identity-access/' },
      to: { path: '^packages/modules/(judging-operations|evaluation|outcomes|external-representation)/' },
    },
    {
      name: 'judging-operations-has-no-downstream-module-dependencies',
      severity: 'error',
      from: { path: '^packages/modules/judging-operations/' },
      to: { path: '^packages/modules/(evaluation|outcomes|external-representation)/' },
    },
    {
      name: 'evaluation-has-no-downstream-module-dependencies',
      severity: 'error',
      from: { path: '^packages/modules/evaluation/' },
      to: { path: '^packages/modules/(outcomes|external-representation)/' },
    },
    {
      name: 'outcomes-has-no-representation-dependency',
      severity: 'error',
      from: { path: '^packages/modules/outcomes/' },
      to: { path: '^packages/modules/external-representation/' },
    },
    {
      name: 'foundation-remains-business-neutral',
      severity: 'error',
      from: { path: '^packages/foundation/' },
      to: { path: '^(apps|packages/(modules|application|projections|test-support))/' },
    },
    {
      name: 'web-does-not-import-server-implementation',
      severity: 'error',
      from: { path: '^apps/web/' },
      to: { path: '^(apps/(api|worker)|packages/(modules|application|projections|test-support))/' },
    },
    {
      name: 'production-does-not-import-test-support',
      severity: 'error',
      from: { path: '^(apps/(api|worker)|packages/(modules|application|projections|foundation))/' },
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

---
type: Implementation Baseline Qualification
title: 008-B — Protected 006-D Baseline Qualification, Drift Audit & Toolchain/Environment Reconciliation
description: Qualifies the retained 006-D executable bootstrap against current Phase 008 authority, records narrow drift remediation, confirms the absence of accidental domain implementation, and preserves unresolved external administration/evidence limits without authorizing domain execution.
status: stable
tags: [phase-008, implementation-planning, baseline, qualification, drift, toolchain, environment, ci, iac, supply-chain]
sources:
  - resource: 008-A-implementation-reentry-authority-canonical-baseline-change-control-planning-guardrails.md
  - resource: ../006-implementation-planning/006-D-environment-iac-ci-cd-local-development-runtime-bootstrap.md
  - resource: ../canonical/governance/design-implementation-boundary.md
  - resource: ../canonical/implementation/implementation-foundation.md
  - resource: ../canonical/implementation/runtime-delivery-bootstrap.md
  - resource: ../canonical/implementation/source-topology.md
  - resource: ../canonical/implementation/verification-strategy.md
  - resource: ../canonical/architecture/application-boundaries.md
  - resource: ../canonical/architecture/aws-runtime-operations.md
  - resource: ../../package.json
  - resource: ../../pnpm-workspace.yaml
  - resource: ../../docker-compose.yml
  - resource: ../../.github/workflows/implementation-verification.yml
generated: { by: openai/gpt-5.6-sol, at: 2026-09-10T17:23:00Z }
---

# Purpose

Qualify the executable non-domain bootstrap retained from 006-D before later Phase 008 planning treats it as a dependable starting point.

008-B is not a feature, schema, authentication, API, browser-domain, or infrastructure implementation slice. It may inspect the executable substrate and make only the narrow non-domain maintenance permitted by the current Design / Implementation Boundary.

The governing question is:

> Does the retained 006-D workspace still realize the accepted toolchain, source-topology, local-development, CI, supply-chain, and IaC bootstrap contracts without containing accidental domain authority or material drift that would make later implementation planning depend on a false baseline?

# Result

**PASS AFTER NARROW REMEDIATION — the retained 006-D substrate is qualified as the current protected non-domain implementation baseline for Phase 008 planning.**

008-B found no architecture-breaking, toolchain-breaking, semantic, or accidental-domain-implementation defect.

Two narrow stale-bootstrap defects were corrected:

1. the browser bootstrap page still stated that domain workflows would arrive in later Phase 006 slices even though 006-E through 006-M are superseded as executable authority;
2. Implementation Verification retained an extra push trigger for `phase-006-*` branches even though Phase 006 is historical and all pull requests plus `main` pushes are already covered.

Neither remediation creates MUDAC domain behavior or changes the accepted technology/source architecture.

The current posture after qualification is:

```text
Jackson Concept Design methodology: COMPLETE / EXITED
implementation planning authority: ESTABLISHED
008-A: COMPLETE
008-B: COMPLETE — PASS AFTER NARROW REMEDIATION
protected 006-D baseline: QUALIFIED FOR PHASE 008 PLANNING
008-C: NEXT
first executable domain slice: NOT YET AUTHORIZED
new domain implementation after 006-D: NOT STARTED
production readiness: NOT ESTABLISHED
```

# Qualification scope

The audit covered the retained areas explicitly named by 008-B:

- workspace/package topology;
- Node/TypeScript/pnpm and application-toolchain pins;
- lockfile and dependency-build posture;
- API/worker/browser composition roots;
- authoritative-module/application/projection/foundation/test-support package seams;
- local PostgreSQL bootstrap and absence of authoritative MUDAC schema;
- dependency-cruiser and ESLint boundary enforcement;
- GitHub Actions verification and CodeQL configuration;
- Dependabot configuration and secret/state ignore posture;
- OpenTofu environment/root/backend structure and absence of application provisioning;
- repository-administration evidence available through the current GitHub integration;
- obvious stale execution guidance inside the executable bootstrap.

It does not attempt to qualify domain behavior that does not yet exist.

# Baseline qualification matrix

| Area | Evidence / observation | Result |
| --- | --- | --- |
| Runtime family | `.node-version` is `24`; root engines require Node `>=24 <25` | PASS |
| Workspace/package manager | root pins `pnpm@11.25.0`; workspace includes `apps/*`, `packages/*`, `packages/modules/*` | PASS |
| TypeScript/tooling | TypeScript `6.0.3`, ESLint `10.8.1`, Prettier `3.9.6`, dependency-cruiser `18.2.0`, Vitest `4.1.11`, Playwright `1.62.1` match the 006-D declared pins | PASS |
| API transport | `apps/api` pins Fastify `5.12.1` and exposes only `/healthz` | PASS |
| Browser shell | React/React DOM `19.2.8`, React Router `8.3.1`, TanStack Query `5.102.8`, Vite `8.2.2`; root route is bootstrap-only | PASS after stale-copy repair |
| Worker | lifecycle/signal bootstrap only; no queue/domain handler | PASS |
| Module topology | six authoritative module workspaces remain present with root-only package exports and placeholder `public.ts` surfaces | PASS |
| Coordination/projections | `@mudac/application` and `@mudac/projections` remain separate empty/minimal seams | PASS |
| Foundation | only generic opaque-brand primitive present; no MUDAC business policy/domain state | PASS |
| Tests | top-level E2E area remains placeholder-only; no domain suite is being misrepresented as implemented evidence | PASS |
| Lockfile | committed lockfile importer pins agree with manifests for root/API/web; no floating workspace dependency baseline discovered | PASS |
| pnpm build-script safety | workspace explicitly allows required `esbuild` build; control is not globally disabled | PASS |
| Dependency boundaries | dependency-cruiser retains circular/app/module/foundation/web/test-support restrictions; ESLint retains web/deep-import restrictions | PASS |
| Local PostgreSQL | Compose provides `postgres:17-alpine` with development-only defaults and persistent local volume; no MUDAC schema/migrations exist | PASS |
| Secret/state hygiene | `.env*` ignored except `.env.example`; Terraform state and `.terraform/` ignored | PASS |
| Dependabot | weekly npm and GitHub Actions updates configured | PASS for configuration; alert inventory not independently readable |
| CodeQL | JavaScript/TypeScript analysis configured for PR/main/schedule; pre-remediation 008-A head run succeeded | PASS for configured/current CI evidence |
| Implementation Verification | frozen install, formatting, typecheck, lint, dependency graph, tests, builds, Compose config and OpenTofu validation retained; pre-remediation 008-A head run succeeded | PASS after obsolete branch-trigger repair |
| OpenTofu version | CI pins `1.12.0`; environment roots require `~> 1.12.0` | PASS |
| IaC environment separation | nonproduction `us-east-2`, production `us-east-2`, recovery `us-east-1` remain separate roots | PASS |
| IaC backend | S3 backend remains partial-configured; examples retain encryption and `use_lockfile = true` | PASS |
| IaC resource boundary | environment roots contain bootstrap locals/version/backend declarations only; reusable modules remain placeholder documentation | PASS — no application provisioning |
| Repository rulesets | repository rulesets endpoint currently returns an empty list | OPEN EXTERNAL ADMIN RESIDUAL |
| Branch protection | current integration receives `403 Resource not accessible by integration` for protection read | UNKNOWN / DO NOT CLAIM |

# Toolchain reconciliation

## Exact retained pins

The executable manifests and lockfile remain aligned with the exact 006-D declared bootstrap pins:

```text
Node                 24 family
pnpm                 11.25.0
TypeScript           6.0.3
Fastify              5.12.1
React / React DOM    19.2.8
React Router         8.3.1
TanStack Query       5.102.8
Vite                 8.2.2
Vitest               4.1.11
Playwright           1.62.1
ESLint               10.8.1
Prettier             3.9.6
dependency-cruiser   18.2.0
OpenTofu             1.12.0 in CI / ~> 1.12.0 roots
```

No upgrade is performed merely because a newer package may exist. Under `IMPL-010`, the relevant qualification question is whether the accepted pinned inputs remain reproducible and compatible with the current baseline. They do.

Future material upgrades remain deliberate implementation decisions with compatibility evidence; 008-B does not turn package freshness into an unplanned architecture/toolchain migration.

# Lockfile and package integrity

The committed `pnpm-lock.yaml` agrees with the root, API, and browser manifest pins inspected by 008-B.

The remaining workspace packages intentionally have no runtime dependencies yet. Their package manifests expose only the narrow public root where applicable rather than wildcard private-source access.

`pnpm-workspace.yaml` retains explicit `allowBuilds.esbuild: true`, preserving the safer-build posture established in 006-D instead of globally permitting dependency install scripts.

# Source-topology qualification

The accepted source topology remains physically present:

```text
apps/
  api/
  worker/
  web/
packages/
  modules/
    competition/
    identity-access/
    judging-operations/
    evaluation/
    outcomes/
    external-representation/
  application/
  projections/
  foundation/
  test-support/
```

`@mudac/api-client` remains absent, which is correct: no authorized transport/client-generation implementation exists yet.

The six semantic module packages remain minimal seams rather than prematurely implemented Concept packages. Package existence is not treated as evidence that Competition, Identity/Access, Judging, Evaluation, Outcome, Export, or Publication behavior exists.

# Accidental-domain-implementation audit

008-B specifically looked for executable behavior that would violate the current Phase 008 planning-only boundary.

## API

The API composition root creates Fastify and exposes only `/healthz`.

No authentication, session, domain command/query, persistence, invitation, Scorecard, Competition, outcome, Export, or Publication endpoint is present.

## Worker

The worker contains process lifetime/signal handling and an empty heartbeat interval only.

No authoritative queue, outbox consumer, projection handler, artifact job, or domain side effect is present.

## Browser

The browser creates a QueryClient, BrowserRouter, and one bootstrap route. It contains no role/session context, domain query, protected route, IndexedDB Draft, judging workflow, Organizer workflow, or domain mutation.

The stale copy referring to later Phase 006 slices was changed to state that domain implementation begins only after an explicitly authorized Phase 009 slice.

## Packages

Authoritative module `public.ts` surfaces remain placeholders. `@mudac/application` and `@mudac/projections` remain placeholders. `@mudac/foundation` contains only the generic opaque-brand utility.

## Persistence

No authoritative MUDAC migration/schema/repository tree was found. Local PostgreSQL remains a service dependency only.

Therefore:

**new domain implementation after 006-D remains NOT STARTED.**

# Dependency-boundary qualification

The existing `dependency-cruiser` rules continue to block the primary structural violations required by the source-topology contract, including:

- circular production dependencies;
- packages depending on deployable applications;
- authoritative modules depending on application coordination/projections;
- upstream modules depending on downstream semantic modules;
- `foundation` acquiring business/server ownership;
- browser import of authoritative server/application/projection/test-support implementation;
- production import of test-support.

ESLint additionally blocks the current browser package names and private/deep package paths for fast local feedback.

The enforcement files remain mechanisms, not semantic owners. Later Phase 009 implementation must extend them when genuinely new surfaces appear rather than bypassing them.

# Local PostgreSQL qualification

`docker-compose.yml` currently provides PostgreSQL 17 Alpine for local development using development-only default credentials and a named local volume.

This is qualified as a **local bootstrap dependency**, not promoted to a production database-version decision and not treated as an authoritative domain schema.

008-D remains responsible for persistence, migration, temporal/history, Versioning, Provenance, governed-exception, outbox, projection, and retention implementation planning before any domain database work can be authorized.

# CI and verification qualification

On the pre-remediation 008-A head `6282f2e96e9375e396d8249062d36a77158b5aa9`:

- Knowledge Validation run `34492767947` completed successfully;
- Implementation Verification run `34492767989` completed successfully;
- CodeQL run `34492768059` completed successfully.

These runs establish that the retained substrate was executable before the two narrow 008-B repairs. The resulting 008-B head must again pass applicable CI before the subgroup is treated as fully integrated.

Implementation Verification continues to cover all pull requests and pushes to `main`. The obsolete special push trigger for `phase-006-*` was removed because it encoded a historical phase-specific branch assumption without adding coverage required by the current delivery model.

This change does not claim actual branch protection. It changes workflow invocation only.

# Supply-chain and security qualification

The baseline retains:

- committed exact dependency pins and lockfile;
- pnpm frozen-install CI;
- explicit dependency build-script allowlisting;
- weekly Dependabot configuration for npm and GitHub Actions;
- CodeQL JavaScript/TypeScript analysis;
- ignored local secret, Terraform-state, and generated-output paths;
- read-only contents permission for ordinary implementation verification.

008-B does **not** claim that there are zero dependency vulnerabilities. The current GitHub connector cannot read the Dependabot-alert endpoint used for that inventory, so alert state remains unavailable evidence rather than an inferred clean result.

Later 008-K security evidence planning may require stronger dependency/container/IaC evidence as concrete artifacts are introduced.

# OpenTofu and environment qualification

The retained infrastructure tree still matches the accepted separation:

```text
infra/
  bootstrap/state/
  modules/
  environments/
    nonproduction/us-east-2/
    production/us-east-2/
    recovery/us-east-1/
```

The three environment roots currently contain no AWS application resources. Their `main.tf` files only identify environment and region; their version files declare OpenTofu and an S3 backend.

Backend examples remain placeholders with environment-specific state keys, encryption, and S3-native locking. No fabricated account IDs, bucket coordinates, credentials, network resources, Cognito pools, RDS instances, ECS services, SQS queues, S3 application buckets, CloudFront distributions, or other domain-purpose runtime resources were found.

Therefore the IaC substrate remains scaffolding, not application provisioning.

# Repository-administration residual

The 006-D repository-administration residual remains open and is now revalidated rather than merely copied forward.

Current evidence:

- repository rulesets endpoint returns `[]`;
- branch-protection endpoint is not readable by the connected integration and returns a permission error;
- no claim can therefore be made that the intended `IMPL-013` merge controls are enforced;
- production protected-environment configuration is likewise not established by this audit.

This residual is not a blocker for continued Phase 008 planning because no domain execution is yet authorized. It must remain visible to 008-C/008-K/008-L and must be closed or explicitly bounded before delivery governance depends on it.

# Drift findings and remediation

## D-01 — stale Phase 006 browser guidance

**Finding:** bootstrap UI said domain workflows would arrive in later Phase 006 slices.

**Consequence:** semantically harmless to runtime, but operationally misleading after 007-I/008-A because 006-E–M are no longer executable authority.

**Disposition:** repaired in 008-B. The bootstrap now points to an explicitly authorized Phase 009 slice.

## D-02 — historical Phase 006 branch trigger

**Finding:** Implementation Verification ran on pull requests, `main`, and direct pushes matching `phase-006-*`.

**Consequence:** no correctness defect, but the historical special-case branch trigger implied Phase 006 remained a current execution family.

**Disposition:** repaired in 008-B. Pull requests remain covered and push verification remains on `main`.

## D-03 — repository protection evidence gap

**Finding:** no repository rulesets are visible; branch protection cannot be read with the current integration.

**Consequence:** workflow availability cannot be promoted to enforced merge governance.

**Disposition:** retained as external administrative residual. Not silently closed.

## D-04 — dependency vulnerability inventory unavailable through current connector

**Finding:** configured Dependabot/CodeQL controls are visible, but the connected GitHub interface does not expose the Dependabot alert inventory used by this audit.

**Consequence:** 008-B can qualify the control configuration and successful CodeQL execution, but cannot certify zero open dependency findings.

**Disposition:** retain as evidence limitation; do not infer cleanliness.

# What 008-B deliberately does not change

008-B does not:

- upgrade the toolchain simply because later versions may exist;
- create Kysely/`pg` persistence code, migrations, domain schemas, repositories, outbox, or projections;
- create Cognito/session/Participation/Access/invitation implementation;
- create domain command/query/API surfaces;
- create IndexedDB Draft or browser domain state;
- create Competition/Judging/Evaluation/Outcome/Export/Publication behavior;
- provision AWS application infrastructure;
- add a generic shared-service or infrastructure package;
- alter the six accepted semantic module boundaries;
- claim branch protection, deployment authority, or production readiness.

# Baseline status after qualification

The protected bootstrap is now qualified for use as an input to the rest of Phase 008 planning.

That means later planning may assume:

- the selected toolchain family/pins are presently coherent and reproducible enough to plan against;
- the current source/package skeleton still realizes the accepted module/composition separation;
- CI and static dependency enforcement are functioning as bootstrap evidence;
- local PostgreSQL exists only as an unowned local database service, not a domain schema;
- environment/IaC roots are separated but contain no application provisioning;
- no new MUDAC domain implementation has accidentally started.

It does **not** mean later plans may skip their own design/implementation choices or evidence gates.

# Exit review

008-B exit criteria are satisfied:

1. current repository/package topology has been compared with accepted source contracts;
2. retained runtime/toolchain pins match the 006-D declared baseline and lockfile;
3. API/worker/browser/package contents do not contain accidental domain implementation;
4. local PostgreSQL remains schema-free bootstrap infrastructure;
5. dependency and browser/server boundary enforcement remains present;
6. CI and CodeQL have recent successful evidence on the immediately preceding baseline;
7. IaC roots remain separated and resource-free;
8. stale executable guidance/phase-specific CI drift discovered by the audit was repaired;
9. external repository-administration and dependency-alert evidence limits remain explicit rather than guessed closed;
10. no implementation authority has been granted.

**Verdict: PASS AFTER NARROW REMEDIATION.**

# Handoff

Proceed to **008-C — Residual-Risk Ingestion, Historical 006 Mapping, Decision Register & Supersession Matrix**.

008-C may now treat the 006-D executable substrate as qualified current planning input, while still preserving the external repository-administration and security-evidence limitations identified here.

New domain implementation remains **NOT STARTED**, and no first executable slice is authorized before 008-L.
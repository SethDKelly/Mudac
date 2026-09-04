---
type: Implementation Planning Record
title: 006-A — Implementation Authority, Delivery Governance, Toolchain & Repository Enforcement
description: Selects the implementation toolchain and establishes implementation authority, repository delivery governance, dependency/version policy, security-scanning baseline, and Phase 006 completion rules.
status: stable
tags: [phase-006, implementation, toolchain, governance, repository, delivery]
sources:
  - resource: ../005-system-application-data-synchronization-architecture/005-J-phase-005-consolidation-threat-failure-review-implementation-readiness-exit.md
  - resource: ../canonical/governance/documentation-authority.md
  - resource: ../canonical/governance/change-governance.md
  - resource: ../canonical/governance/validation-enforcement.md
  - resource: ../canonical/architecture/application-boundaries.md
  - resource: ../canonical/architecture/data-persistence.md
  - resource: ../canonical/architecture/commands-api-concurrency.md
  - resource: ../canonical/architecture/frontend-interaction.md
  - resource: ../canonical/architecture/aws-runtime-operations.md
  - resource: https://nodejs.org/en/about/previous-releases
  - resource: https://www.typescriptlang.org/docs/handbook/release-notes/typescript-6-0.html
  - resource: https://fastify.dev/docs/v5.12.x/
  - resource: https://www.kysely.dev/
  - resource: https://pnpm.io/
  - resource: https://opentofu.org/blog/
generated: { by: openai/gpt-5.6-sol, at: 2026-09-04T12:45:00Z }
---

# Purpose

Establish the implementation authority and replaceable toolchain decisions that every later Phase 006 subgroup must share so MUDAC does not accumulate incompatible foundations, framework-owned domain rules, unenforced repository conventions, or dependency/version drift.

006-A selects implementation mechanisms but does not define detailed source/package topology, database schemas, API endpoints, test fixtures, or production infrastructure modules. Those remain owned by later Phase 006 groups.

# Governing principle

Implementation is downstream of canonical product, UX, governance, and architecture knowledge.

```text
canonical product / UX / governance
        ↓
canonical architecture
        ↓
canonical implementation contracts
        ↓
source code / migrations / IaC / tests
```

If implementation convenience conflicts with a canonical rule, implementation adapts unless the human deliberately requests a semantic redesign through `CHG-*`.

# Repository starting condition

At 006-A entry the repository contains documentation/governance tooling but no application `package.json`, source tree, database migrations, browser build, container definition, or IaC implementation. No existing application stack therefore constrains the implementation selection.

# Toolchain decision

## Language/runtime

Use **Node.js 24 LTS** as the initial server/build runtime and **TypeScript 6.x** as the application language for both server and browser code.

Rationale:

- the browser architecture already requires React + TypeScript;
- one language/toolchain reduces duplicated build, validation, DTO/client, and contributor conventions;
- Node is a natural fit for the accepted ECS/Fargate runtime;
- TypeScript supports explicit module/API contracts without requiring runtime framework inheritance;
- the system is event-shaped rather than CPU-heavy compute infrastructure.

Node 26 is current rather than LTS at this review point, so the production baseline remains Node 24 LTS until an intentional runtime upgrade is verified.

## Server framework

Use **Fastify 5.x** as the HTTP/application-host adapter.

Fastify owns transport concerns such as request lifecycle, route registration, validation/serialization integration, hooks, and server startup/shutdown. It does not own MUDAC modules, domain entities, application commands, transactions, Access rules, or persistence ownership.

NestJS was considered but rejected as the baseline because its framework-level module/DI/decorator model would add a second architectural vocabulary that could easily be mistaken for the `MOD-*` semantic module model. A full-stack React/Next-style server was likewise rejected because the accepted architecture separates the React client from the authoritative modular-monolith API.

## Workspace/package management

Use **pnpm workspaces** with a committed lockfile.

Do not introduce Nx, Turborepo, Bazel, or another workspace orchestration/cache layer initially. `pnpm` recursive/workspace scripts plus ordinary CI job composition are sufficient until measured build/test pressure demonstrates otherwise.

Detailed workspace/package boundaries are deferred to 006-C.

## PostgreSQL access and migrations

Use **Kysely** with **node-postgres (`pg`)** as the typed SQL/query layer.

Use explicit, version-controlled forward migrations through the Kysely migration boundary; production does not use schema `push`/auto-sync behavior. Migration ownership remains module-scoped and later 006-E must define naming, ordering, expand/contract, rollback/recovery, and generated database-type conventions.

Kysely is selected over a heavier identity-map/active-record ORM because MUDAC already has explicit domain/module ownership and should not allow ORM entities or relation navigation to become the application model. SQL remains inspectable and transaction boundaries remain explicit.

## API schemas and OpenAPI

Fastify route adapters use explicit JSON-schema-compatible transport schemas. Accepted public schemas generate an OpenAPI document from the HTTP boundary rather than generating domain models from OpenAPI or serializing persistence/domain objects directly.

The browser API client may later be generated from the published OpenAPI contract, but exact schema/type-provider and client-generator packages are selected in 006-G after API package boundaries are defined.

## Test tooling baseline

Use **Vitest** as the TypeScript unit/module/integration test runner family and **Playwright** for browser end-to-end testing. 006-B owns the exact verification matrix, fixture system, database-test topology, accessibility tooling, security tests, and CI evidence gates.

Vitest 5 released immediately before this planning record, so initial manifests must pin a tested compatible release rather than adopting a new major solely because it is newest.

## Formatting, lint and static analysis

The baseline is:

- TypeScript `strict` type checking;
- ESLint flat configuration with TypeScript-aware rules;
- Prettier for deterministic formatting;
- no blanket lint/type suppressions without narrow explanation;
- dependency-boundary enforcement added in 006-C rather than relying on folder naming convention.

## Infrastructure as Code

Use **OpenTofu** for persistent AWS infrastructure.

OpenTofu was selected over application-language CDK as the baseline because MUDAC benefits from an explicit declarative infrastructure plan/state boundary independent of application modules and framework packages. The AWS architecture is already service-specific, so a separate HCL IaC layer does not create a competing product architecture.

006-D owns actual module/state/backend/environment topology. Production changes use reviewed plans and GitHub OIDC deployment roles under `AWS-*`.

# Dependency and supply-chain policy

Application/runtime/tool dependencies are exact-version pinned through the lockfile used in CI and container builds. Direct dependencies should use an intentional bounded version policy in manifests; lockfile changes are reviewed as code.

Automated dependency-update pull requests are allowed and encouraged but never auto-merge merely because an update is available. Major upgrades require compatibility evidence and an implementation decision note when they change runtime/tooling behavior materially.

Generated code is identified by path/header/convention, reproducible from checked-in source contracts, and not hand-edited. Generated artifacts that materially affect the build are regenerated and diff-checked in CI where practical.

# Security scanning baseline

Implementation CI will include, as relevant to the files introduced:

- GitHub Dependabot/dependency alerts and dependency review;
- GitHub CodeQL for JavaScript/TypeScript;
- package-manager vulnerability audit as a signal, with severity/false-positive handling governed rather than ignored globally;
- Trivy filesystem/container/IaC scanning;
- OpenTofu formatting/validation and TFLint once IaC exists;
- container image scanning before production promotion;
- secret scanning/protection where repository/platform capability permits.

006-B defines blocking thresholds and evidence handling. A scanner finding is not silently suppressed; accepted residual risk has an owner/reason/expiry or equivalent explicit disposition.

# Repository delivery governance

The intended `main` policy is:

1. changes reach `main` through pull requests once implementation work begins;
2. required status checks include Knowledge Validation plus the applicable implementation CI aggregate check;
3. required checks must be current with the target branch before merge;
4. force pushes and branch deletion are prohibited;
5. unresolved review conversations block merge when review is used;
6. no mandatory reviewer count is imposed while the repository is effectively single-maintainer, because that would create ceremonial self-approval rather than independent review;
7. reviewer/CODEOWNERS requirements may be strengthened when additional maintainers exist;
8. production deployment is separately gated by a protected GitHub environment/explicit approval under `AWS-011` and is never implied by merge alone.

At 006-A the connector available to this design session can read but cannot administer GitHub rulesets/branch protection. Therefore the intended ruleset is a required 006-D repository-configuration action and remains an explicit implementation-entry gate until verified from GitHub.

# GitHub Actions authority

CI verifies implementation evidence; it does not become product authority.

A green workflow means the selected checks passed for the tested revision. It does not prove untested semantic correctness, production readiness, human verification, or permission to weaken canonical rules.

Workflow definitions are code-reviewed and version-controlled. Production deployment workflows use GitHub OIDC, protected environments, least-privilege AWS roles, immutable release identities, and no long-lived AWS keys.

# Implementation decision records

Material implementation choices that are downstream/reversible but affect multiple subgroups use an implementation decision record under the Phase 006 history/decision area established in 006-C. The record must identify:

- decision and scope;
- upstream stable rules/architecture constraints;
- alternatives considered;
- operational/security/testing consequences;
- reversibility/migration consequence;
- supersession relationship if later replaced.

An implementation ADR cannot redefine canonical product or architecture meaning. If a choice would do that, use `CHG-*` and update the canonical owner first.

# Definition of done for a Phase 006 subgroup

A subgroup is complete only when all applicable conditions are true:

1. the scoped implementation decisions are explicit and no material decision is hidden as an accidental code default;
2. affected canonical implementation owner(s) or current routing are updated where durable current meaning was established;
3. implementation artifacts introduced by the subgroup pass their defined formatting/type/lint/test/security checks;
4. canonical rule IDs materially implemented by the subgroup are traceable from tests or implementation planning without copying their rule bodies;
5. no known cross-module dependency/storage/authority violation remains unclassified;
6. migration/API/backward-compatibility implications are addressed where relevant;
7. security/accessibility/recovery implications are tested or explicitly carried as a later named gate;
8. documentation/knowledge validation remains green;
9. the subgroup identifies the next dependency-safe handoff;
10. `verified` metadata is not fabricated merely because CI passed.

# Alternatives rejected at baseline

## Python/FastAPI backend

Technically viable, but would create a second primary language/toolchain without a demonstrated domain/runtime benefit. It remains possible only if a later workload or ecosystem need justifies the additional boundary.

## NestJS

Provides useful enterprise conventions but introduces framework modules/providers/decorators whose concepts overlap the deliberately framework-neutral semantic module architecture. MUDAC prefers a thinner server adapter.

## Prisma-style heavy ORM baseline

Rejected because the accepted architecture favors explicit module-owned transactions, SQL constraints, projections, and historical/version tables. A lighter typed SQL boundary reduces pressure to expose persistence entities as domain models.

## Nx/Turborepo from day one

Rejected until actual repository size/build timings demonstrate the need for task graph/caching infrastructure.

## AWS CDK as baseline IaC

Rejected in favor of OpenTofu because persistent cloud infrastructure should remain explicit and independently reviewable from the TypeScript application dependency graph. This is a tool choice, not a rejection of AWS-native architecture.

# Exit result

006-A establishes a coherent initial implementation authority/toolchain and closes the repository/tool-selection ambiguity required by 006-B through 006-H.

No product or Phase 005 architecture rule is changed.

The next dependency-safe subgroup is **006-B — Verification Strategy, Test Harness, Evidence Fixtures & Quality Gates**.
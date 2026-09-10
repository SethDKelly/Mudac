---
type: Implementation Contract
title: Source Topology, Package Boundaries & Dependency Enforcement
description: Defines MUDAC's current workspace/source topology, authoritative module packages, public/private package seams, coordination/projection placement, browser layering, shared-foundation limits, test ownership, persistence/migration placement, and dependency-graph enforcement.
status: stable
tags: [implementation, source-topology, packages, modules, dependencies, monorepo, enforcement]
sources:
  - resource: ../../006-implementation-planning/006-C-source-topology-module-package-boundaries-shared-foundation-dependency-enforcement.md
  - resource: ../../008-implementation-reentry/008-D-persistence-temporal-truth-versioning-provenance-governed-exceptions-outbox-projection-migration-implementation-plan.md
  - resource: implementation-foundation.md
  - resource: verification-strategy.md
  - resource: persistence-history-projection.md
  - resource: ../architecture/application-boundaries.md
  - resource: ../architecture/frontend-interaction.md
  - resource: ../architecture/data-persistence.md
  - resource: ../architecture/commands-api-concurrency.md
generated: { by: openai/gpt-5.6-sol, at: 2026-09-10T19:13:00Z }
---

# Purpose

Define the durable implementation source/package boundaries that realize MUDAC's modular-monolith and browser architecture. Packages make ownership enforceable; they do not create new product Concepts or deployment/service authority.

This owner intentionally does not introduce a new stable-rule namespace. Dependency configuration and downstream implementation should cite the existing stable architecture/implementation rules it realizes—especially `MOD-*`, `FE-*`, `DATA-*`, and `IMPL-*`—and link this owner for the concrete source/package consequence rather than creating a second package-rule universe.

## Source topology realizes semantic ownership without mirroring the knowledge tree

The implementation uses packages for meaningful runtime/source ownership boundaries, especially the six accepted authoritative modules. It does not create a package per Concept, document, table, command, screen, or architecture topic.

Knowledge-directory shape is not source-code topology under `DOC-006`.

## Deployable apps are composition roots, not semantic owners

`apps/api`, `apps/worker`, and `apps/web` own runtime/bootstrap/composition concerns. They do not own authoritative product facts merely because they are deployable entrypoints.

The API/worker compose module/application/projection contracts; the browser consumes public transport/client adapters.

## Each authoritative server module is a separate workspace package

The six initial authoritative module packages are:

- `@mudac/competition`;
- `@mudac/identity-access`;
- `@mudac/judging-operations`;
- `@mudac/evaluation`;
- `@mudac/outcomes`;
- `@mudac/external-representation`.

They compile into the modular-monolith runtime; package separation does not imply six network services.

## Module public exports are explicit and private implementation is not cross-importable

Each authoritative module exposes a narrow production root export for stable IDs and legitimate public command/query/fact/composition contracts. Restrictive package `exports` do not provide wildcard deep access.

Cross-package consumers may not import another module's repositories, Kysely row/table types, adapters, internal services/entities, SQL helpers, Fastify handlers, or vendor clients.

## Cross-module dependencies follow an explicit acyclic allowlist and use public contracts

Physical module dependencies follow `MOD-005`'s upstream-to-downstream authority direction and are added only when actually needed.

The baseline ordering is:

```text
competition
  ↓
identity-access
  ↓
judging-operations
  ↓
evaluation
  ↓
outcomes
  ↓
external-representation
```

A downstream module may consume an upstream public contract/reference without acquiring mutation authority. Authoritative modules never depend on downstream modules, `application`, `projections`, or `apps/*`.

## Cross-module application coordination lives above module owners

`@mudac/application` may depend on module public contracts and coordinate cross-module use cases/transactions established by `MOD-004`/`API-006`.

It owns no domain entity/table/invariant and never becomes a generic service layer imported by authoritative modules.

008-D permits a narrowly technical migration area under `packages/application/migrations/platform/` for shared one-database mechanics such as migration bookkeeping and transactional outbox infrastructure. That exception does not authorize application-owned domain tables.

## Cross-module projections are isolated and non-authoritative

`@mudac/projections` owns projection/read shapes, projection handlers, generation/freshness metadata, and projection-owned storage/query adapters. It may consume public module snapshots/queries/change facts but cannot mutate authoritative module storage or become the sole precondition source for consequential commands.

Authoritative modules do not depend on projections.

## Shared foundation remains small, business-neutral, and runtime-neutral

`@mudac/foundation` contains only broadly reusable technical primitives such as generic opaque-ID mechanics, Clock/ID-generator interfaces, request/correlation primitives, exhaustive helpers, and business-neutral value/serialization helpers.

It does not contain domain entities/statuses, Access decisions, repositories, business policy, shared persistence ownership, or generic multi-domain `Service`/`Model` dumping grounds. Domain-specific IDs remain named/exported by their owning module.

Foundation is browser-safe by default; Node/vendor-specific dependencies require an explicit reviewed boundary rather than contaminating all consumers.

## Infrastructure adapters stay owner-local and depend inward

Persistence/provider/queue/object-store implementations normally live inside the module whose ports they implement. Deployable roots supply environment/runtime dependencies and compose module factories.

A central infrastructure package with unrestricted access to every module/table is not the default. 008-D explicitly found no need for a new generic persistence/infrastructure workspace package.

## Browser source cannot import server semantic or persistence implementation

`apps/web` may consume browser-safe foundation and the public/generated API-client boundary, but it must not import authoritative server module packages, `@mudac/application`, server persistence/Kysely/`pg`, Fastify, server AWS adapters, or server-only test helpers.

Type reuse is not sufficient reason to cross this boundary.

## Front-end layers have enforceable inward dependency direction

Within `apps/web/src`, use `app/routes → features → patterns → primitives`, with features/routes/app consuming explicit browser adapters for API/query/session/IndexedDB/artifact concerns.

Primitives do not depend on patterns/features/routes; patterns do not depend on features; features do not depend on routes/app; adapters do not depend on feature components or route state. Direct feature-to-feature imports are disallowed by default; routes compose features and reusable semantics move to patterns.

## Generated transport artifacts are isolated, reproducible consumers of API contracts

Accepted HTTP transport schemas remain at the API transport boundary and generate OpenAPI outward under `IMPL-006`/`IMPL-011`.

When 008-F later plans a browser client boundary, generated transport code lives behind one `@mudac/api-client`-style boundary. Generated DTOs do not become domain entities, and feature code may wrap them with browser semantic/recovery adapters.

## Test/source boundaries preserve production ownership

Unit/module tests remain owner-local. Modules may expose a deliberate test-only `./testing` entry for synthetic builders of their own resources; cross-module scenarios compose those entries/public contracts.

`@mudac/test-support` is technical-only and may host disposable PostgreSQL, clock/ID, HTTP/browser, and evidence helpers. Production source cannot import module `./testing`, `@mudac/test-support`, or top-level `tests/`.

## Workspace dependencies are explicit and cannot bypass package exports

Every workspace declares direct dependencies in its own `package.json`. Internal dependencies use pnpm `workspace:` references. The root owns repository-wide development tooling, not hidden runtime dependencies relied upon by child packages.

Cross-workspace imports use package names/public exports. Relative traversal across workspace roots and tsconfig/path aliases that bypass package exports are forbidden.

## Package exports and dependency-cruiser enforce the source graph

Restrictive package exports form the first physical public/private seam. `dependency-cruiser` is the repository dependency-graph rule engine for cross-package/module/browser/test/layer restrictions and undeclared/unresolvable dependency checks; ESLint restrictions may provide faster local feedback but are not the sole architecture control.

The executable rule configuration was introduced with the 006-D workspace/bootstrap and remains part of stable **Implementation Verification**.

## Circular production dependencies and boundary violations are blocking defects

Circular package/source dependencies and prohibited dependency edges fail implementation verification rather than being accepted as architectural debt by default.

Cycles are resolved through correct ownership, upward coordination, owner-defined ports/public facts, or genuinely business-neutral foundation extraction—not by creating an unowned `common` package or re-exporting private internals.

# Repository topology

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
  api-client/              # only once later authorized transport implementation needs it

infra/
scripts/
tests/
docs/
```

The pnpm workspace covers `apps/*`, `packages/*`, and `packages/modules/*`.

# Module internal shape

A module may use this shape as responsibilities appear:

```text
src/
  public.ts
  domain/
  application/
  ports/
  adapters/
  composition/
  testing/
migrations/
```

Do not create empty layers merely to satisfy the diagram.

008-D now owns the migration placement/ordering contract: authoritative module migrations remain owner-local, projection migrations remain under `@mudac/projections`, narrow one-database technical migrations may live under `packages/application/migrations/platform/`, and repository-level `scripts/db/` performs orchestration without becoming semantic ownership.

# Persistence/migration source placement

When an authorized Phase 009 slice actually introduces persistence, the planned layout is:

```text
packages/modules/<owner>/migrations/
packages/modules/<owner>/src/adapters/postgres/
packages/projections/migrations/
packages/projections/src/adapters/postgres/
packages/application/migrations/platform/
scripts/db/migrate.ts
```

Each module defines its own Kysely table/row mappings privately. Cross-module code consumes public contracts, not another package's persistence types.

Shared PostgreSQL pool/transaction composition is supplied at application/runtime composition boundaries. 008-F owns the exact transaction-context interface; it does not alter owner-local storage access.

# Allowed module dependency matrix

| Module package | Allowed internal workspace dependencies |
| --- | --- |
| competition | foundation |
| identity-access | foundation; competition public surface |
| judging-operations | foundation; competition; identity-access public surfaces |
| evaluation | foundation; competition; identity-access; judging-operations public surfaces |
| outcomes | foundation; upstream public surfaces actually required, especially evaluation/judging/competition |
| external-representation | foundation; upstream public surfaces actually required, especially evaluation/outcomes |

The table is an upper bound, not a requirement to declare every listed dependency.

# Deployable/package relationship

```text
apps/api
  ├── application
  ├── projections
  └── authoritative module public/composition surfaces

apps/worker
  └── application and/or relevant module public/composition surfaces

apps/web
  └── api-client + browser-safe foundation/adapters
```

One API/worker deployment may contain code from many packages while semantic ownership remains unchanged.

# Handoff

The protected 006-D baseline instantiates the package/application skeleton and dependency enforcement without domain behavior. 008-D has now fixed the downstream persistence/migration placement for future authorized work.

008-E may plan Identity/Participation/Access/session storage inside the `identity_access` owner boundary. 008-F may plan shared transaction composition without exposing owner-private tables. No new domain implementation is authorized before 008-L.
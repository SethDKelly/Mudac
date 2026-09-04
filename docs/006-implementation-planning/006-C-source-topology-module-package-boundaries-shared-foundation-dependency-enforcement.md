---
type: Implementation Planning Record
title: 006-C — Source Topology, Module/Package Boundaries, Shared Foundation & Dependency Enforcement
description: Defines MUDAC's implementation source/workspace topology, semantic module package boundaries, public/private export seams, application coordination and projection placement, front-end layering, shared-foundation limits, test ownership, and automated dependency enforcement.
status: stable
tags: [phase-006, implementation, source-topology, modules, packages, dependencies, monorepo]
sources:
  - resource: ../canonical/implementation/implementation-foundation.md
  - resource: ../canonical/implementation/verification-strategy.md
  - resource: ../canonical/architecture/application-boundaries.md
  - resource: ../canonical/architecture/frontend-interaction.md
  - resource: ../canonical/architecture/data-persistence.md
  - resource: ../canonical/architecture/commands-api-concurrency.md
  - resource: ../canonical/governance/documentation-authority.md
  - resource: https://pnpm.io/workspaces
  - resource: https://github.com/sverweij/dependency-cruiser/blob/main/doc/cli.md
generated: { by: openai/gpt-5.6-sol, at: 2026-09-04T15:23:00Z }
---

# Purpose

Translate the accepted modular-monolith and browser architecture into an enforceable repository/source shape before executable application scaffolding is created.

006-C defines physical ownership and dependency direction. It does **not** turn packages into independent services, mirror the OKF knowledge tree into source code, define database schemas/endpoints, or create a package per product Concept.

# Governing shape

```text
knowledge ownership
      ↓ constrains
semantic module ownership (`MOD-*`)
      ↓ realized by
workspace/package boundaries
      ↓ enforced by
package exports + declared workspace deps + dependency rules + CI
```

A package is an implementation boundary. A deployable app is a composition/runtime boundary. Neither independently creates product authority.

# Accepted top-level repository topology

When executable implementation is bootstrapped, use this baseline:

```text
apps/
  api/                       # Fastify HTTP/session composition root
  worker/                    # bounded SQS/background worker composition root
  web/                       # React browser application

packages/
  modules/
    competition/
    identity-access/
    judging-operations/
    evaluation/
    outcomes/
    external-representation/

  application/               # thin cross-module use-case coordination
  projections/               # non-authoritative cross-module read models
  foundation/                # small business-neutral/runtime-neutral primitives
  test-support/              # technical test harness only

  api-client/                # introduced by 006-G when generated browser contract exists

infra/                       # OpenTofu; implemented by 006-D
scripts/                     # repository/build/validation automation
tests/                       # system/browser/operational scenarios spanning packages/apps
docs/                        # knowledge and implementation planning
```

`packages/api-client/` is a reserved boundary, not permission to fabricate an API contract during 006-C. It is created only when 006-G establishes generation and compatibility mechanics.

The pnpm workspace will cover `apps/*`, `packages/*`, and `packages/modules/*`. Deployable apps remain `private` workspace packages.

# Why six server module packages

The six packages correspond to the six accepted semantic module owners from `MOD-*`, not to every Concept or document:

| Package | Semantic owner |
| --- | --- |
| `@mudac/competition` | Competition Governance |
| `@mudac/identity-access` | Identity, Participation & Access |
| `@mudac/judging-operations` | Judging Operations |
| `@mudac/evaluation` | Evaluation |
| `@mudac/outcomes` | Outcomes & Closeout |
| `@mudac/external-representation` | External Representation |

This is enough physical separation to make ownership enforceable while preserving the modular-monolith-first deployment posture.

Do not create packages for every Concept, every database table, every command, every UI screen, or every architecture document.

# Authoritative module package shape

Each authoritative server module follows the same broad internal structure while retaining freedom to omit unnecessary layers/files:

```text
packages/modules/<module>/
  package.json
  tsconfig.json
  src/
    public.ts               # only normal cross-package production entry
    domain/                 # owner business rules/state/value objects
    application/            # owner commands/queries/use cases
    ports/                  # owner-required infrastructure abstractions
    adapters/               # persistence/vendor implementations owned by module
    composition/            # owner factory/wiring exposed only as needed
    testing/                # test-only builders/public harness entry
  migrations/               # when introduced; owner-local, 006-E governs details
```

This is an implementation template, not a requirement to create empty directories. A module should add a layer only when it has content with that responsibility.

## Public production surface

A module package exposes an intentionally narrow production surface from its root (`.`), including only what another package legitimately needs, such as:

- stable resource/reference ID types;
- public command/query interfaces;
- public result/event/fact contracts;
- module composition/factory entry needed by deployable roots.

It does not expose:

- repository implementations;
- Kysely table/row models;
- SQL helpers;
- Fastify types/routes;
- AWS SDK clients;
- internal domain services/entities solely for convenience;
- adapter implementation classes;
- another module's re-exported API.

Each module package uses a restrictive `package.json#exports` map. There is no wildcard deep export such as `./*`.

## Test-only surface

A module may expose a deliberate `./testing` entry containing synthetic builders/scenario helpers for its own resources. Production source outside tests may not import this entry.

Cross-module tests compose module-owned testing/public contracts rather than directly inserting foreign tables or importing private persistence models.

# Cross-module dependency direction

Physical imports must preserve the acyclic authority direction from `MOD-005`.

The baseline allowlist is:

```text
foundation
   ↑
competition
   ↑
identity-access
   ↑
judging-operations
   ↑
evaluation
   ↑
outcomes
   ↑
external-representation
```

This diagram describes allowed downstream knowledge of upstream public contracts, not mandatory dependencies.

More precisely:

| Package | May depend on |
| --- | --- |
| `competition` | `foundation` |
| `identity-access` | `foundation`, `competition` public surface |
| `judging-operations` | `foundation`, `competition`, `identity-access` public surfaces |
| `evaluation` | `foundation`, `competition`, `identity-access`, `judging-operations` public surfaces |
| `outcomes` | `foundation`, `competition`, `identity-access`, `judging-operations`, `evaluation` public surfaces as actually needed |
| `external-representation` | `foundation`, upstream module public surfaces actually needed, especially `evaluation`/`outcomes` |

Unused dependencies are not added preemptively. A downstream package may depend on a stable upstream ID/contract without gaining authority to mutate upstream state.

No authoritative module depends on `application`, `projections`, `apps/*`, or a downstream semantic module.

# Application coordination package

`@mudac/application` contains only cross-module use-case coordination that cannot correctly live inside one semantic owner.

It may:

- depend on public contracts from all authoritative modules;
- sequence owner operations;
- host narrow cross-module transaction/workflow coordination established by `API-006`;
- expose use-case entrypoints to API/worker composition roots.

It may not:

- own domain entities/state;
- define another module's invariant;
- access module-private repositories/tables;
- become a generic `services` dumping ground;
- become a required dependency of authoritative module packages.

# Projection/read-model package

`@mudac/projections` owns non-authoritative cross-module read shapes, projection handlers/builders, and projection-specific persistence/query adapters.

It may consume:

- public module query/snapshot contracts;
- committed change/outbox facts intended for projection use;
- projection-owned storage.

It may not:

- mutate authoritative module tables;
- expose a command path that writes source authority;
- become the sole precondition provider for consequential commands;
- import module-private persistence internals to make querying convenient.

The API may use projections for operational reads while authoritative commands return to module/application owners.

# Shared foundation

`@mudac/foundation` is intentionally small, runtime-neutral, and business-neutral. It may contain primitives such as:

- opaque/branded-ID mechanics used by owner-defined IDs;
- Clock/ID-generator interfaces and deterministic basic implementations;
- correlation/causation/request-context primitives;
- exhaustive-match/assertion helpers;
- generic serialization/value helpers that contain no product policy.

It does **not** contain:

- Competition/Scorecard/Participation entities or statuses;
- role/Access decisions;
- repositories or generic domain `Service` bases;
- shared database tables;
- business validation/policy;
- giant `common`, `models`, `services`, or `utils` buckets.

Domain-specific IDs remain named/exported by their owning module even if their opaque-ID mechanism comes from `foundation`.

`foundation` must be safe for browser consumption unless an explicit Node-only sub-boundary is later introduced; adding Node/vendor dependencies to it requires review because that would contaminate the web dependency graph.

# Infrastructure adapter placement

Infrastructure stays owner-local where it implements an owner's port.

Examples:

```text
evaluation/adapters/postgres/*
identity-access/adapters/cognito/*
external-representation/adapters/s3/*
external-representation/adapters/sqs/*
```

A technical adapter used by several modules may become a business-neutral package only after demonstrated reuse; the default is **not** a central `infrastructure` package that can reach every table and service.

Deployable apps supply environment/configuration clients and compose module factories. Infrastructure types do not leak into module public contracts.

# Deployable applications

## `apps/api`

Owns Fastify/runtime composition only:

- process bootstrap/shutdown;
- configuration/environment loading;
- HTTP/session/CSRF middleware;
- route registration and transport mapping;
- OpenAPI exposure/generation boundary;
- module/application/projection wiring;
- health/readiness endpoints;
- runtime telemetry wiring.

It does not own product rules or persistence tables.

## `apps/worker`

Owns bounded worker runtime composition:

- SQS receive/ack/retry/DLQ integration;
- job-envelope decoding;
- module/application handler invocation;
- worker health/telemetry/shutdown.

A worker is not a seventh semantic module and does not obtain direct storage authority merely because it is asynchronous.

## `apps/web`

Owns the React browser product composition and may depend only on browser-safe packages/contracts. It must not import server module packages, `@mudac/application`, server persistence code, Kysely/`pg`, Fastify, AWS server SDK adapters, or server testing helpers.

# Front-end source layers

Within `apps/web/src/`, use these responsibilities:

```text
app/               providers, router creation, top-level composition
routes/            route loaders/actions/layout compositions
features/          domain-facing browser features/workflows
patterns/          reusable MUDAC semantic interaction patterns
primitives/        accessible low-level UI primitives
adapters/          API/query/session/IndexedDB/artifact adapters
styles/            design tokens/global style foundations
```

Dependency direction is roughly:

```text
app / routes
      ↓
features
      ↓
patterns
      ↓
primitives

features/routes/app → adapters → generated/public API contracts
```

Rules:

- primitives do not import features/routes;
- patterns do not import domain features;
- features do not import routes/app;
- direct feature-to-feature imports are disallowed by default; routes compose features, and genuine reusable UI semantics move to patterns;
- adapters do not import feature components or route state;
- browser code cannot import server-private/domain/persistence implementation simply for type reuse.

This realizes `FE-011` without making component-library folders semantic authorities.

# Generated transport/client boundary

006-G will establish exact OpenAPI/client generation. 006-C reserves these rules:

- accepted HTTP transport schemas live at the API transport boundary, not in domain packages;
- generated OpenAPI/client outputs are identifiable and reproducible under `IMPL-011`;
- the generated browser client, when introduced, lives behind `@mudac/api-client` or an equivalent single transport-client boundary;
- generated transport DTOs do not become module/domain entities;
- browser feature code uses an adapter above generated transport details where semantic mapping/recovery behavior is needed.

# Test/source topology

Use three test locations with different ownership:

1. **colocated package tests** for unit/module behavior owned by that package;
2. **module `./testing` exports** for synthetic owner-approved builders used by dependent scenarios;
3. top-level `tests/` for genuine multi-app/system/browser/operational scenarios.

`@mudac/test-support` contains only technical harnesses such as disposable PostgreSQL lifecycle helpers, deterministic clocks/IDs, generic HTTP/browser setup, and privacy-safe evidence helpers. Domain builders remain with their owning module.

Production source cannot depend on `@mudac/test-support`, top-level tests, or any module `./testing` entry.

# Workspace dependency declaration

Every workspace package declares its direct dependencies in its own `package.json`.

Internal workspace dependencies use pnpm's `workspace:` protocol so resolution cannot silently fall back to an unrelated registry package with the same name.

The root package contains repository-wide development tooling and scripts, not undeclared runtime dependencies that child packages accidentally consume.

Cross-workspace imports use package names/public exports. Relative traversal across workspace roots and tsconfig path aliases that bypass package exports are forbidden.

# Dependency enforcement

Use **dependency-cruiser** as the repository dependency-graph rule engine, pinned in the implementation lockfile when the executable workspace is created.

The configuration must fail on at least:

- circular production dependencies;
- authoritative module → downstream module dependencies;
- any module → `application`/`projections`/`apps` dependency;
- cross-module deep/private imports;
- production source → `./testing`, `test-support`, or top-level tests;
- `apps/web` → server-only/module/application/persistence packages;
- front-end layer reversals;
- adapters/infrastructure imported by domain/application layers where dependency direction is inverted;
- undeclared/unresolvable workspace dependencies.

Restrictive package `exports` provide a second boundary. ESLint `no-restricted-imports` may provide fast editor feedback for obvious prohibited paths, but it does not replace the repository graph check.

The dependency-cruiser check becomes part of the stable **Implementation Verification** aggregate defined by 006-B when 006-D creates executable CI.

# Circular dependency posture

Circular package dependencies are errors, including cycles that appear only because a convenience/shared type was placed in the wrong package.

A cycle is resolved by examining ownership:

- move business-neutral mechanism to `foundation` only if truly generic;
- move coordination upward to `application`;
- depend on the actual upstream public owner;
- introduce an owner-defined port/fact where inversion is appropriate;
- reconsider a mistaken module responsibility through architecture governance if necessary.

Do not fix a cycle by creating an unowned `common` package or re-exporting one module through another.

# Initial dependency graph

```text
                       apps/web
                          │
                    api-client(*)
                          │
                       adapters

apps/api ─────┬──── application ─────┐
              │                       │
              ├──── projections       │
              │                       │
              └──── module public contracts

apps/worker ─────── application / relevant module public contracts

modules:
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

(all may use foundation; arrows between modules mean downstream may consume upstream public contracts only)

(*) introduced by 006-G
```

# Deliberate non-selections

006-C does not add:

- Nx/Turborepo/Bazel;
- a DI container framework;
- a central enterprise `shared-domain` package;
- a central all-powerful infrastructure/data-access package;
- a package per Concept/table/command;
- separate services/repos per module;
- frontend micro-frontends;
- broad path aliases that bypass package exports.

These would increase indirection before evidence warrants it.

# Exit result

006-C establishes a source/package graph that can enforce `MOD-*`, `FE-*`, `IMPL-*`, and the 006-B fixture/test ownership contract before source volume accumulates.

No product/architecture meaning is changed. 006-D can now instantiate the pnpm workspace, root configs, dependency-cruiser rules, TypeScript package configs, executable API/worker/web skeletons, OpenTofu layout, local runtime, and CI without deciding semantic ownership ad hoc.

The next dependency-safe subgroup is **006-D — Environment, IaC, CI/CD, Local Development & Runtime Bootstrap**.

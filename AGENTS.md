# MUDAC Repository Agent Rules

This file is a **bootstrap adapter**, not the canonical source of MUDAC product, synchronization, architecture, implementation, verification, source-topology, runtime, or documentation rules.

Canonical governance lives under [`docs/canonical/governance/`](docs/canonical/governance/).

## Required start

1. Start at [`docs/index.md`](docs/index.md).
2. For current meaning, use [`docs/canonical/`](docs/canonical/).
3. For behavior spanning more than one Concept, load the relevant owner under [`docs/canonical/synchronizations/`](docs/canonical/synchronizations/) rather than reconstructing coordination from old phase history.
4. **Before any implementation/code/IaC task, read [`Design / Implementation Boundary`](docs/canonical/governance/design-implementation-boundary.md). MUDAC is currently in design re-entry and executable work is frozen at the 006-D non-domain prototype boundary.**
5. For architecture work, load only the relevant owner(s) under [`docs/canonical/architecture/`](docs/canonical/architecture/) plus materially relevant upstream constraints.
6. For implementation-maintenance work that is permitted by the freeze, load the relevant owner(s) under [`docs/canonical/implementation/`](docs/canonical/implementation/), the architecture owner(s) they realize, and materially relevant product/UX/governance constraints.
7. Verification/test work additionally loads [`Verification Strategy, Evidence & Quality Gates`](docs/canonical/implementation/verification-strategy.md).
8. Source/package/import work additionally loads [`Source Topology, Package Boundaries & Dependency Enforcement`](docs/canonical/implementation/source-topology.md).
9. Runtime/environment/CI/IaC work additionally loads [`Runtime, Environment & Delivery Bootstrap`](docs/canonical/implementation/runtime-delivery-bootstrap.md).
10. Use numbered phase history only for rationale, chronology, rejected alternatives, implementation lineage, or source audit.

Governed by `DOC-*`, `CTX-*`, `CHG-*`, `META-*`, `VAL-*`, task-relevant canonical synchronization/architecture rules, [`IMPL-*`](docs/canonical/implementation/implementation-foundation.md), the task-relevant canonical implementation owners, and the current [Design / Implementation Boundary](docs/canonical/governance/design-implementation-boundary.md).

## Current design-reentry freeze

The executable work created through 006-D is retained as a **frozen non-domain bootstrap/prototype**.

Until an explicit later Jackson-methodology exit authorizes implementation to resume, agents must not advance into:

- domain PostgreSQL schema/migrations/repositories;
- Cognito/session/Participation/Access/invitation implementation;
- production command/query API or idempotency/transaction implementation;
- IndexedDB Draft semantics;
- Competition, Judging, Evaluation, Outcome, Award, Export, Artifact or Publication feature implementation;
- real AWS application provisioning/deployment intended to support those deferred domain paths.

Permitted executable changes are narrow maintenance needed to keep the existing bootstrap safe/buildable and must not introduce domain semantics. Current work should default to deliberate design refinement under Phase 007+.

## Do not

- recursively preload all of `docs/` for ordinary work;
- reconstruct current rules from old phase history when a canonical owner exists;
- duplicate synchronization semantics independently inside multiple Concept/architecture/implementation documents when the canonical synchronization owner can be referenced;
- copy complete canonical rules into downstream docs/tests/configuration when a rule ID/link plus local consequence is sufficient;
- let README/index/traceability/agent/test-fixture files become competing rule stores;
- silently resolve canonical contradictions by choosing convenient implementation wording;
- change product semantics only in code, tests, migrations, IaC, generated schemas, or comments;
- infer package/service/database structure from the knowledge-directory layout;
- create a package per Concept/table/command/screen/document merely because the subject is named;
- create `common`, `shared-domain`, generic `services`/`models`, or central infrastructure packages to bypass ownership;
- deep-import another workspace's private source or bypass package `exports` through cross-root relative paths/path aliases;
- let browser code import authoritative server modules, persistence implementations, or server-only test helpers;
- let Fastify routes, Kysely rows, OpenAPI DTOs, React components, OpenTofu modules, mocks, fixtures, or snapshots become alternate domain owners;
- substitute SQLite/in-memory evidence for real PostgreSQL when PostgreSQL semantics matter;
- hide flaky consequential tests behind retries or indefinite quarantine;
- treat CI, coverage, scanners, workflow existence, IaC validation, or deployment configuration as semantic verification or production certification;
- infer that green implementation checks or the historical 005-J exit authorize implementation beyond 006-D while the design freeze is active.

## Frozen executable baseline

The selected implementation family remains Node.js 24 LTS + TypeScript, pnpm workspaces, Fastify, Kysely + node-postgres, explicit migrations, outward-generated OpenAPI, Vitest/Playwright, strict TypeScript + ESLint + Prettier, and OpenTofu.

Current source/runtime consequences retained from 006-D:

- `apps/api`, `apps/worker`, and `apps/web` are composition roots;
- six authoritative module packages remain empty/minimal semantic seams within the modular monolith;
- `@mudac/application` coordinates above owners and `@mudac/projections` is non-authoritative;
- `@mudac/foundation` remains business-neutral;
- package exports, dependency-cruiser, and ESLint enforce the dependency graph;
- local development uses host Node processes plus Docker Compose PostgreSQL;
- external AWS/provider behavior uses deterministic fakes locally and targeted real-service evidence in nonproduction when later authorized;
- `Implementation Verification` is the stable executable CI check surface;
- OpenTofu has separate nonproduction `us-east-2`, production `us-east-2`, and cold-recovery `us-east-1` roots/state identities;
- actual GitHub branch/ruleset and protected production-environment administration remains an external repository-admin gate until independently configured.

These are preserved substrate choices, not authorization to implement their deferred domain use.

## Validation

Knowledge changes:

```text
python -m pip install -r requirements-docs.txt
python scripts/validate_knowledge.py
```

Permitted executable-maintenance changes:

```text
pnpm install --frozen-lockfile
pnpm verify
```

CI additionally validates current OpenTofu roots. Passing checks are evidence for the tested revision, not OKF verification, design-methodology closure, implementation-resume authority, or production certification.

## Canonical changes

If the human requests a semantic change, use [`CHG-*`](docs/canonical/governance/change-governance.md). If implementation/test/architecture conflicts with canonical meaning and redesign was not requested, the downstream mechanism adapts.

## Context stopping rule

Once sufficient authoritative context is loaded to perform the task safely, stop expanding context unless a concrete unresolved dependency remains.

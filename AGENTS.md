# MUDAC Repository Agent Rules

This file is a **bootstrap adapter**, not the canonical source of MUDAC product, architecture, implementation, verification, source-topology, runtime, or documentation rules.

Canonical governance lives under [`docs/canonical/governance/`](docs/canonical/governance/).

## Required start

1. Start at [`docs/index.md`](docs/index.md).
2. For current meaning, use [`docs/canonical/`](docs/canonical/).
3. For architecture work, load only the relevant owner(s) under [`docs/canonical/architecture/`](docs/canonical/architecture/) plus materially relevant upstream constraints.
4. For implementation work, load the relevant owner(s) under [`docs/canonical/implementation/`](docs/canonical/implementation/), the architecture owner(s) they realize, and materially relevant product/UX/governance constraints.
5. Verification/test work additionally loads [`Verification Strategy, Evidence & Quality Gates`](docs/canonical/implementation/verification-strategy.md).
6. Source/package/import work additionally loads [`Source Topology, Package Boundaries & Dependency Enforcement`](docs/canonical/implementation/source-topology.md).
7. Runtime/environment/CI/IaC/deployment work additionally loads [`Runtime, Environment & Delivery Bootstrap`](docs/canonical/implementation/runtime-delivery-bootstrap.md).
8. Use numbered phase history only for rationale, chronology, rejected alternatives, implementation lineage, or source audit.

Governed by `DOC-*`, `CTX-*`, `CHG-*`, `META-*`, `VAL-*`, task-relevant architecture rules, [`IMPL-*`](docs/canonical/implementation/implementation-foundation.md), and the task-relevant canonical implementation owners.

## Do not

- recursively preload all of `docs/` for ordinary work;
- reconstruct current rules from old phase history when a canonical owner exists;
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
- treat CI, coverage, scanners, workflow existence, IaC validation, or deployment configuration as semantic verification or production certification.

## Current executable implementation baseline

The implementation family remains Node.js 24 LTS + TypeScript, pnpm workspaces, Fastify, Kysely + node-postgres, explicit migrations, outward-generated OpenAPI, Vitest/Playwright, strict TypeScript + ESLint + Prettier, and OpenTofu.

Current source/runtime consequences:

- `apps/api`, `apps/worker`, and `apps/web` are composition roots;
- six authoritative module packages remain semantic owners within the modular monolith;
- `@mudac/application` coordinates above owners and `@mudac/projections` is non-authoritative;
- `@mudac/foundation` remains business-neutral;
- package exports, dependency-cruiser, and ESLint enforce the dependency graph;
- local development uses host Node processes plus Docker Compose PostgreSQL;
- external AWS/provider behavior uses deterministic fakes locally and targeted real-service evidence in nonproduction when needed;
- `Implementation Verification` is the stable executable CI check surface;
- OpenTofu has separate nonproduction `us-east-2`, production `us-east-2`, and cold-recovery `us-east-1` roots/state identities;
- actual GitHub branch/ruleset and protected production-environment administration remains an external repository-admin gate until independently configured.

## Validation

Knowledge changes:

```text
python -m pip install -r requirements-docs.txt
python scripts/validate_knowledge.py
```

Implementation changes:

```text
pnpm install --frozen-lockfile
pnpm verify
```

CI additionally validates current OpenTofu roots. Passing checks are evidence for the tested revision, not OKF verification or production certification.

## Canonical changes

If the human requests a semantic change, use [`CHG-*`](docs/canonical/governance/change-governance.md). If implementation/test/architecture conflicts with canonical meaning and redesign was not requested, the downstream mechanism adapts.

## Context stopping rule

Once sufficient authoritative context is loaded to perform the task safely, stop expanding context unless a concrete unresolved dependency remains.

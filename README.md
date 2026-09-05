# MUDAC Competition Demo

MUDAC is a design- and implementation-governed web application effort for fair, traceable, resilient judging at live student data competitions.

Student Teams present analyses to Panels of volunteer Judges. Each Judge independently authors a Rubric-based Scorecard in a Judging Encounter; authoritative Scorecards feed explicit Coverage, aggregation, ranking, Awards, and controlled official-closeout semantics while preserving Judge independence, provenance, anonymity, accessibility, and paper continuity.

## Start here

* [`AGENTS.md`](AGENTS.md) — repository-agent bootstrap.
* [`docs/index.md`](docs/index.md) — preferred OKF progressive-disclosure entry point.
* [`docs/canonical/`](docs/canonical/) — current product/domain, UX, governance, architecture, and implementation authority.
* [`docs/canonical/implementation/`](docs/canonical/implementation/) — current implementation contracts.
* [`docs/006-implementation-planning/`](docs/006-implementation-planning/) — active implementation sequence/history.

Numbered phase directories preserve rationale and planning history; canonical owners govern current meaning.

## Status

* Phase 001 — Concept Design Foundation: **Complete**
* Phase 002 — Concept Specification: **Complete**
* Phase 003 — Conceptual UX Architecture: **Complete**
* Phase 004 — Knowledge Architecture / OKF Governance: **Complete**
* Phase 005 — System/Application/Data/Synchronization Architecture: **Complete**
* Phase 006 — Implementation Planning & Delivery: **In Progress**
  * 006-A toolchain/governance: Complete
  * 006-B verification/evidence: Complete
  * 006-C source/package boundaries: Complete
  * 006-D environment/IaC/CI/local/runtime bootstrap: Complete
  * **006-E Persistence, Schema, Migration, Provenance, Outbox & Projection Foundation: Next**

The full Phase 006 decomposition lives in [`docs/006-implementation-planning/README.md`](docs/006-implementation-planning/README.md).

## Executable implementation bootstrap

006-D has moved the repository beyond documentation-only planning while keeping domain features intentionally absent.

The repository now contains:

```text
apps/
  api/       Fastify bootstrap + /healthz
  worker/    worker lifecycle bootstrap
  web/       React + React Router + TanStack Query shell

packages/
  modules/   six authoritative module package seams
  application/
  projections/
  foundation/
  test-support/

infra/
  bootstrap/state/
  environments/
    nonproduction/us-east-2/
    production/us-east-2/
    recovery/us-east-1/
```

The pinned workspace uses Node.js 24, TypeScript 6, pnpm, Fastify, React, Vite, Vitest, Playwright, ESLint, Prettier, dependency-cruiser, and OpenTofu. A generated `pnpm-lock.yaml` is committed and frozen installs are required.

Local development runs API/worker/web processes on the host and PostgreSQL through Docker Compose. External AWS/provider behavior is introduced behind deterministic fakes locally and tested against real nonproduction services when vendor semantics matter.

GitHub Actions now contains the stable **Implementation Verification** aggregate plus CodeQL; Dependabot covers npm and GitHub Actions updates. Implementation Verification checks formatting, strict TypeScript, lint, dependency graph rules, tests, builds, Compose configuration, and OpenTofu formatting/root validation. Knowledge Validation remains separate.

OpenTofu separates nonproduction, production, and cold-recovery root/state identities. Production remains single-active `us-east-2`; `us-east-1` is cold recovery, not a second active writer.

Actual GitHub branch/ruleset and protected production-environment administration remains an explicit external repository-admin action because the current connected GitHub capability cannot configure those controls. Workflow existence is not represented as enforced merge/deployment policy.

This bootstrap is **not production certification**. Persistence/security/API/browser foundations and domain vertical slices remain downstream Phase 006 work.

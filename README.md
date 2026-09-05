# MUDAC Competition Demo

MUDAC is a design-governed web application effort for fair, traceable, resilient judging at live student data competitions.

Student Teams present analyses to Panels of volunteer Judges. Each Judge independently authors a Rubric-based Scorecard in a Judging Encounter; authoritative Scorecards feed explicit Coverage, aggregation, ranking, Awards, and controlled official-closeout semantics while preserving Judge independence, provenance, anonymity, accessibility, and paper continuity.

## Start here

* [`AGENTS.md`](AGENTS.md) — repository-agent bootstrap and current implementation freeze routing.
* [`docs/index.md`](docs/index.md) — preferred OKF progressive-disclosure entry point.
* [`docs/canonical/`](docs/canonical/) — current product/domain, UX, governance, architecture, and retained implementation authority.
* [`docs/canonical/governance/design-implementation-boundary.md`](docs/canonical/governance/design-implementation-boundary.md) — current design-reentry and executable-work freeze.
* [`docs/007-design-refinement/`](docs/007-design-refinement/) — active deliberate design-refinement phase.

Numbered phase directories preserve rationale and planning history; canonical owners govern current meaning.

## Status

* Phase 001 — Concept Design Foundation: **Complete**
* Phase 002 — Concept Specification: **Complete**
* Phase 003 — Conceptual UX Architecture: **Complete**
* Phase 004 — Knowledge Architecture / OKF Governance: **Complete**
* Phase 005 — System/Application/Data/Synchronization Architecture: **Complete as historical architecture exit**
* Phase 006 — Implementation Planning & Delivery: **Frozen after 006-D**
  * 006-A toolchain/governance: Complete
  * 006-B verification/evidence: Complete
  * 006-C source/package boundaries: Complete
  * 006-D environment/IaC/CI/local/runtime bootstrap: Complete and frozen
  * 006-E through 006-M: **Deferred**
* Phase 007 — Jackson Design Refinement & Methodology Closure: **In Progress**
  * 007-A design re-entry/freeze/completion criteria: Complete
  * **007-B Concept Completeness, Independence & Genericity Audit: Next**

## Frozen executable bootstrap

006-D moved the repository beyond documentation-only planning, but only at a deliberately non-domain substrate level.

The retained prototype includes:

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

The pinned workspace, CI, dependency checks, local PostgreSQL service and OpenTofu roots are retained for future use. They do **not** authorize continued implementation.

Until a later explicit Jackson-methodology exit, do not advance domain schema/persistence, authentication/session/Access, production command/query APIs, IndexedDB Draft semantics, MUDAC feature behavior, or real application AWS provisioning/deployment.

Narrow security/compatibility maintenance needed to keep the existing bootstrap safe/buildable is permitted only when it does not encode domain semantics.

## Current direction

MUDAC has returned to deliberate design refinement. Phase 007 will re-audit the current concept system after the later UX and architecture work, beginning with **Concept Completeness, Independence & Genericity** and continuing until an explicit methodology exit establishes that implementation can safely resume.

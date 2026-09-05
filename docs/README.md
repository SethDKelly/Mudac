# MUDAC Design Documentation

The repository is the durable design and implementation authority; conversation history is working context.

## Preferred navigation

Start at [index.md](index.md), the OKF v0.2 bundle root. Current product/domain, UX, governance, architecture, and implementation meaning lives under [Canonical Knowledge](canonical/). Root [`AGENTS.md`](../AGENTS.md) is only a bootstrap adapter into those owners.

Use numbered phase directories for rationale, design evolution, alternatives, implementation planning, and provenance.

## Status

* Phase 001 — Concept Design Foundation: **Complete**
* Phase 002 — Concept Specification, Policy & Synchronization Refinement: **Complete**
* Phase 003 — Conceptual UX Architecture: **Complete**
* Phase 004 — Knowledge Architecture, OKF Retrofit & Documentation Governance: **Complete**
* Phase 005 — System, Application, Data & Synchronization Architecture: **Complete**
* Phase 006 — Implementation Planning, Delivery Slices & Verification Strategy: **In Progress**
  * 006-A — implementation authority/toolchain: **Complete**
  * 006-B — verification/evidence strategy: **Complete**
  * 006-C — source/package/dependency topology: **Complete**
  * 006-D — environment/IaC/CI/CD/local/runtime bootstrap: **Complete**
  * **006-E — Persistence, Schema, Migration, Provenance, Outbox & Projection Foundation: Next**
  * 006-F through 006-M: Planned

The complete Phase 006 dependency plan lives in [006-implementation-planning/README.md](006-implementation-planning/README.md).

## Current implementation posture

Current implementation owners are under [canonical/implementation/](canonical/implementation/):

* [Implementation Authority, Toolchain & Delivery Governance](canonical/implementation/implementation-foundation.md);
* [Verification Strategy, Evidence & Quality Gates](canonical/implementation/verification-strategy.md);
* [Source Topology, Package Boundaries & Dependency Enforcement](canonical/implementation/source-topology.md);
* [Runtime, Environment & Delivery Bootstrap](canonical/implementation/runtime-delivery-bootstrap.md).

The repository now contains an executable pinned pnpm/TypeScript workspace with `apps/api`, `apps/worker`, and `apps/web`; six authoritative module package seams; application/projection/foundation/test-support packages; dependency-cruiser enforcement; Docker Compose PostgreSQL for local development; a committed generated lockfile; **Implementation Verification**, CodeQL, and Dependabot workflows; and separate OpenTofu nonproduction, production, and cold-recovery roots.

This is a bootstrap substrate, not a production-readiness claim. The domain persistence/security/API/browser feature foundations remain 006-E through 006-H, and user-visible vertical slices begin at 006-I.

Actual GitHub branch/ruleset and protected production-environment administration remains explicitly unclaimed because the current connected GitHub capability cannot configure those controls. Workflow existence must not be treated as enforced merge or deployment policy.

Knowledge Validation checks deterministic knowledge structure. Implementation Verification checks the executable workspace/IaC substrate. Neither creates semantic verification metadata or production certification.

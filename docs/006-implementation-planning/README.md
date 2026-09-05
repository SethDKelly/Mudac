# Phase 006 — Implementation Planning, Delivery Slices & Verification Strategy

Status: **Frozen after 006-D**

## Current authority

Phase 006 began implementation planning and then crossed into executable bootstrap work at 006-D. A later human design decision now freezes that executable substrate and returns MUDAC to deliberate Jackson Concept Design refinement before any domain implementation continues.

The current freeze is owned by [Design / Implementation Boundary](../canonical/governance/design-implementation-boundary.md) and recorded by [007-A — Design Re-entry, Implementation Freeze & Jackson Completion Criteria](../007-design-refinement/007-A-design-reentry-implementation-freeze-jackson-completion-criteria.md).

005-J remains historical provenance for the earlier architecture-exit decision; it is not retroactively rewritten.

## Status of the original dependency-safe plan

| Group | Topic | Status |
| --- | --- | --- |
| 006-A | [Implementation Authority, Delivery Governance, Toolchain & Repository Enforcement](006-A-implementation-authority-delivery-governance-toolchain-repository-enforcement.md) | **Complete** |
| 006-B | [Verification Strategy, Test Harness, Evidence Fixtures & Quality Gates](006-B-verification-strategy-test-harness-evidence-fixtures-quality-gates.md) | **Complete** |
| 006-C | [Source Topology, Module/Package Boundaries, Shared Foundation & Dependency Enforcement](006-C-source-topology-module-package-boundaries-shared-foundation-dependency-enforcement.md) | **Complete** |
| 006-D | [Environment, IaC, CI/CD, Local Development & Runtime Bootstrap](006-D-environment-iac-ci-cd-local-development-runtime-bootstrap.md) | **Complete — frozen prototype boundary** |
| 006-E | Persistence, Schema, Migration, Provenance, Outbox & Projection Foundation | **Deferred** |
| 006-F | Identity, Session, Access, Security & Invitation Foundation | **Deferred** |
| 006-G | API, Commands, Queries, Transactions, Idempotency & Concurrency Foundation | **Deferred** |
| 006-H | Browser Shell, Routing, Remote/Local State, Component Primitives & Accessibility Foundation | **Deferred** |
| 006-I | Competition Setup, Participation & Judging Operations Vertical Slice | **Deferred** |
| 006-J | Evaluation, Scorecard, Draft Synchronization, Conflict & Paper-Capture Vertical Slice | **Deferred** |
| 006-K | Reconciliation, Coverage, Ranking, Awards, Finalization & Official Outcome Vertical Slice | **Deferred** |
| 006-L | Export, Artifact, Publication, Print & External Representation Vertical Slice | **Deferred** |
| 006-M | Integrated Security, Observability, Performance, Recovery, Operational Readiness & Phase Exit | **Deferred** |

## Frozen executable baseline

006-D remains in the repository as a deliberately non-domain prototype containing:

- the pinned pnpm/TypeScript workspace and lockfile;
- minimal API, worker and browser composition roots;
- package/module seams without MUDAC domain behavior;
- local PostgreSQL service bootstrap without authoritative domain schema;
- CI/static/dependency checks;
- OpenTofu environment/root scaffolding without production provisioning.

The bootstrap may receive narrow security/compatibility maintenance needed to remain buildable, but it must not advance persistence, authentication, API semantics, IndexedDB Draft behavior, domain features or real application AWS provisioning.

## Deferred implementation plan

The original 006-E through 006-M decomposition is preserved as planning lineage. It may be revised or superseded after the renewed design runway reaches a formal methodology exit.

Its original dependency intent remains useful context:

```text
006-E persistence
   ↓
006-F identity/access
   ↓
006-G API/concurrency
   ↓
006-H browser foundation
   ↓
006-I competition/judging ops
   ↓
006-J evaluation/sync/paper
   ↓
006-K outcomes/finalization
   ↓
006-L representation/publication
   ↓
006-M integrated readiness
```

But this chain is **not executable authority while the design freeze is active**.

## Resume condition

Implementation resumes only after a later explicit Jackson-methodology exit and human/design decision. Green CI, the existence of 006-E plans, or the prior 005-J conclusion does not independently authorize continuation.

## Next

Proceed to [Phase 007 — Jackson Design Refinement & Methodology Closure](../007-design-refinement/), beginning with **007-B — Concept Completeness, Independence & Genericity Audit**.

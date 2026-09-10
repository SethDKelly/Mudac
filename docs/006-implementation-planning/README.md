# Phase 006 — Implementation Planning, Delivery Slices & Verification Strategy

Status: **Historical planning/bootstrap phase — execution interrupted after 006-D**

## Current authority

Phase 006 began implementation planning and crossed into executable non-domain bootstrap work at 006-D. 007-A later froze further domain implementation and reopened deliberate Jackson Concept Design. Phase 007 has now formally exited that renewed methodology through 007-I.

The current boundary is owned by [Design / Implementation Boundary](../canonical/governance/design-implementation-boundary.md).

Phase 006 is **not reopened as the active execution queue**. Its records remain planning/bootstrap provenance and useful dependency rationale for the Phase 008 refresh.

005-J remains historical provenance for the earlier architecture-exit decision; it is not retroactively rewritten.

## Status of the original dependency-safe plan

| Group | Topic | Status |
| --- | --- | --- |
| 006-A | [Implementation Authority, Delivery Governance, Toolchain & Repository Enforcement](006-A-implementation-authority-delivery-governance-toolchain-repository-enforcement.md) | **Complete — historical planning** |
| 006-B | [Verification Strategy, Test Harness, Evidence Fixtures & Quality Gates](006-B-verification-strategy-test-harness-evidence-fixtures-quality-gates.md) | **Complete — historical planning** |
| 006-C | [Source Topology, Module/Package Boundaries, Shared Foundation & Dependency Enforcement](006-C-source-topology-module-package-boundaries-shared-foundation-dependency-enforcement.md) | **Complete — historical planning** |
| 006-D | [Environment, IaC, CI/CD, Local Development & Runtime Bootstrap](006-D-environment-iac-ci-cd-local-development-runtime-bootstrap.md) | **Complete — retained protected non-domain baseline** |
| 006-E | Persistence, Schema, Migration, Provenance, Outbox & Projection Foundation | **Not executed — historical plan lineage** |
| 006-F | Identity, Session, Access, Security & Invitation Foundation | **Not executed — historical plan lineage** |
| 006-G | API, Commands, Queries, Transactions, Idempotency & Concurrency Foundation | **Not executed — historical plan lineage** |
| 006-H | Browser Shell, Routing, Remote/Local State, Component Primitives & Accessibility Foundation | **Not executed — historical plan lineage** |
| 006-I | Competition Setup, Participation & Judging Operations Vertical Slice | **Not executed — historical plan lineage** |
| 006-J | Evaluation, Scorecard, Draft Synchronization, Conflict & Paper-Capture Vertical Slice | **Not executed — historical plan lineage** |
| 006-K | Reconciliation, Coverage, Ranking, Awards, Finalization & Official Outcome Vertical Slice | **Not executed — historical plan lineage** |
| 006-L | Export, Artifact, Publication, Print & External Representation Vertical Slice | **Not executed — historical plan lineage** |
| 006-M | Integrated Security, Observability, Performance, Recovery, Operational Readiness & Phase Exit | **Not executed — historical plan lineage** |

## Retained 006-D implementation baseline

006-D remains in the repository as a deliberately non-domain implementation substrate containing:

- pinned pnpm/TypeScript workspace and lockfile;
- minimal API, worker and browser composition roots;
- package/module seams without MUDAC domain behavior;
- local PostgreSQL service bootstrap without authoritative domain schema;
- CI/static/dependency checks;
- OpenTofu environment/root scaffolding without production application provisioning.

It is now a **protected baseline**, not a design-incomplete freeze marker.

Until Phase 008 explicitly authorizes the first domain implementation slice, executable changes remain limited to narrow dependency/security/compatibility maintenance, non-domain verification/tooling repair, documentation/routing changes, and removal of accidental behavior that conflicts with current design.

## Original dependency intent

The earlier dependency chain remains useful planning evidence:

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

However, **this chain is no longer current executable authority**.

Phase 007 materially refined the semantics that those slices must implement. Phase 008 may preserve, split, merge, rename, reorder, or replace the old slices after deliberate dependency review.

## Phase 007 reconciliation requirements

Any refreshed implementation plan must incorporate at least:

- temporal/correction/invalidation/replacement and latest-declared-official + Affected semantics;
- explicit authority-establishing versus derived/convergent synchronization effects;
- adversarial technical/break-glass and irreversible disclosure-exposure findings;
- Judge/Organizer experience action/authority traceability;
- Operational Exception & Override Governance;
- Export representation-authority monotonicity;
- purpose/source-specific Publication prerequisites;
- the 007-H architecture/implementation/evidence residual register.

## Current post-exit posture

```text
Jackson Concept Design methodology: COMPLETE / EXITED
implementation planning: READY TO RESUME
Phase 008 plan refresh: NEXT / NOT STARTED
new domain implementation after 006-D: NOT STARTED
```

Green CI, historical 006 plans, or the prior 005-J architecture exit do not authorize bypassing Phase 008 plan refresh.

## Next

Proceed by defining **Phase 008 — Implementation Re-entry, Plan Refresh & Execution Readiness** into dependency-safe subgroups.

Use Phase 006 as lineage and input, not as an automatically resumed work queue.
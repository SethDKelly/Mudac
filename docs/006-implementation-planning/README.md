# Phase 006 — Implementation Planning, Delivery Slices & Verification Strategy

Status: **Historical planning/bootstrap phase — execution interrupted after 006-D; deferred queue now explicitly superseded by Phase 008**

## Current authority

Phase 006 began implementation planning and crossed into executable non-domain bootstrap work at 006-D. 007-A later froze further domain implementation and reopened deliberate Jackson Concept Design. Phase 007 subsequently exited that renewed methodology through 007-I.

The current boundary is owned by [Design / Implementation Boundary](../canonical/governance/design-implementation-boundary.md).

Phase 006 is **not reopened as the active execution queue**. Its records remain planning/bootstrap provenance and dependency rationale. [008-C](../008-implementation-reentry/008-C-residual-risk-ingestion-historical-006-mapping-decision-register-supersession-matrix.md) now owns the explicit current disposition of 006-E through 006-M.

005-J remains historical provenance for the earlier architecture-exit decision; it is not retroactively rewritten.

## Status of the original dependency-safe plan

| Group | Original topic | Historical status | Current disposition |
| --- | --- | --- | --- |
| 006-A | [Implementation Authority, Delivery Governance, Toolchain & Repository Enforcement](006-A-implementation-authority-delivery-governance-toolchain-repository-enforcement.md) | Complete — historical planning | Durable current rules live in canonical implementation/governance owners. |
| 006-B | [Verification Strategy, Test Harness, Evidence Fixtures & Quality Gates](006-B-verification-strategy-test-harness-evidence-fixtures-quality-gates.md) | Complete — historical planning | Durable verification contracts remain canonical; 008-K later refreshes evidence/readiness planning. |
| 006-C | [Source Topology, Module/Package Boundaries, Shared Foundation & Dependency Enforcement](006-C-source-topology-module-package-boundaries-shared-foundation-dependency-enforcement.md) | Complete — historical planning | Current source-topology contract remains canonical. |
| 006-D | [Environment, IaC, CI/CD, Local Development & Runtime Bootstrap](006-D-environment-iac-ci-cd-local-development-runtime-bootstrap.md) | Complete — retained non-domain bootstrap | **Qualified by 008-B** as the protected Phase 008 planning baseline. |
| 006-E | Persistence, Schema, Migration, Provenance, Outbox & Projection Foundation | Not executed | **Preserve + expand → 008-D**. |
| 006-F | Identity, Session, Access, Security & Invitation Foundation | Not executed | **Preserve + expand/rename → 008-E**; cross-cutting security evidence → 008-K. |
| 006-G | API, Commands, Queries, Transactions, Idempotency & Concurrency Foundation | Not executed | **Preserve + expand → 008-F**. |
| 006-H | Browser Shell, Routing, Remote/Local State, Component Primitives & Accessibility Foundation | Not executed | **Preserve + refine → 008-G**; cross-cutting accessibility evidence → 008-K. |
| 006-I | Competition Setup, Participation & Judging Operations Vertical Slice | Not executed | **Preserve + expand → 008-H**. |
| 006-J | Evaluation, Scorecard, Draft Synchronization, Conflict & Paper-Capture Vertical Slice | Not executed | **Split → 008-G + 008-I**. Generic browser Draft/conflict moves to 008-G; Scorecard/evaluation/paper stays in 008-I. |
| 006-K | Reconciliation, Coverage, Ranking, Awards, Finalization & Official Outcome Vertical Slice | Not executed | **Preserve + expand → 008-J**. |
| 006-L | Export, Artifact, Publication, Print & External Representation Vertical Slice | Not executed | **Merge → 008-J** with outcomes/finalization/externalization authority chain. |
| 006-M | Integrated Security, Observability, Performance, Recovery, Operational Readiness & Phase Exit | Not executed | **Split → 008-K + 008-L**. Evidence/readiness planning in 008-K; roadmap/authorization/exit in 008-L. |

The historical 006-E through 006-M sequence is therefore **fully superseded as an executable roadmap**. Preserve it for provenance; do not resume it mechanically.

## Retained 006-D implementation baseline

006-D remains in the repository as a deliberately non-domain implementation substrate containing:

- pinned pnpm/TypeScript workspace and lockfile;
- minimal API, worker and browser composition roots;
- package/module seams without MUDAC domain behavior;
- local PostgreSQL service bootstrap without authoritative domain schema;
- CI/static/dependency checks;
- OpenTofu environment/root scaffolding without production application provisioning.

008-B audited and qualified this substrate after narrow non-domain remediation. Qualification is planning evidence, not permission to begin domain implementation.

Until 008-L explicitly authorizes the first domain implementation slice, executable changes remain limited to narrow dependency/security/compatibility maintenance, non-domain verification/tooling repair, documentation/routing changes, and removal of accidental behavior that conflicts with current design.

## Original dependency intent retained as provenance

The earlier dependency direction remains useful evidence:

```text
persistence
   ↓
identity/access
   ↓
API/concurrency
   ↓
browser foundation
   ↓
competition/judging ops
   ↓
evaluation/paper
   ↓
outcomes/finalization
   ↓
representation/publication
   ↓
integrated readiness
```

008-C preserves that dependency intent while changing boundaries where the completed Phase 007 design requires cleaner ownership.

The current Phase 008 planning chain is:

```text
008-D persistence / temporal / history / provenance / exception / outbox
   ↓
008-E Identity / Participation / Access / session
   ↓
008-F commands / queries / transactions / CAS / idempotency / API
   ↓
008-G browser / Draft / synchronization / recovery
   ↓
008-H Competition + Judging Operations
   ↓
008-I Scorecard + evaluation evidence + amendment + paper
   ↓
008-J outcomes + Finalization + official outcome + Export + Publication
   ↓
008-K cross-cutting evidence / operations / retention
   ↓
008-L roadmap + first-slice authorization
```

This is planning order, not execution authority.

## Phase 007/008 reconciliation requirements

The refreshed implementation plan must preserve:

- temporal/correction/invalidation/replacement and latest-declared-official + Affected semantics;
- explicit authority-establishing versus derived/convergent synchronization effects;
- adversarial technical/break-glass and irreversible disclosure-exposure findings;
- Judge/Organizer experience action/authority traceability;
- Operational Exception & Override Governance;
- Export representation-authority monotonicity;
- purpose/source-specific Publication prerequisites;
- the 007-H architecture/implementation/evidence residual register;
- the 008-C ownership and supersession decisions.

## Current post-reconciliation posture

```text
Jackson Concept Design methodology: COMPLETE / EXITED
008-A: COMPLETE
008-B: COMPLETE — protected 006-D baseline qualified
008-C: COMPLETE — residual/historical-plan ownership closed
008-D: NEXT / NOT STARTED
historical 006-E–M executable queue: SUPERSEDED / MAPPED
new domain implementation after 006-D: NOT STARTED
first executable slice: NOT YET AUTHORIZED
```

Green CI, historical 006 plans, or the prior 005-J architecture exit do not authorize bypassing Phase 008 or the 008-L first-slice gate.

## Next

Use [Phase 008](../008-implementation-reentry/) for current implementation planning. The next dependency-safe subgroup is **008-D — Persistence, Temporal Truth, Versioning, Provenance, Governed Exceptions, Outbox, Projection & Migration Implementation Plan**.

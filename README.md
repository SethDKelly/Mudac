# MUDAC Competition Demo

MUDAC is a design-governed web application effort for fair, traceable, resilient judging at live student data competitions.

Student Teams present analyses to Panels of volunteer Judges. Each Judge independently authors a Rubric-based Scorecard in a Judging Encounter; authoritative Scorecards feed explicit Coverage, aggregation, ranking, Awards, and controlled official-closeout semantics while preserving Judge independence, provenance, anonymity, accessibility, and paper continuity.

## Start here

* [`AGENTS.md`](AGENTS.md) — repository-agent bootstrap and current Phase 008 execution boundary.
* [`docs/index.md`](docs/index.md) — preferred OKF progressive-disclosure entry point.
* [`docs/canonical/`](docs/canonical/) — current product/domain, synchronization, temporal/correction, UX, governance, architecture, and implementation authority.
* [`docs/canonical/governance/design-implementation-boundary.md`](docs/canonical/governance/design-implementation-boundary.md) — current planning/execution authority boundary.
* [`docs/canonical/implementation/persistence-history-projection.md`](docs/canonical/implementation/persistence-history-projection.md) — accepted 008-D persistence/history/outbox/projection/migration implementation contract.
* [`docs/008-implementation-reentry/`](docs/008-implementation-reentry/) — active implementation re-entry, plan refresh, and execution-readiness phase.

Numbered phase directories preserve rationale and planning history; canonical owners govern current meaning.

## Status

* Phase 001 — Concept Design Foundation: **Complete**
* Phase 002 — Concept Specification: **Complete**
* Phase 003 — Conceptual UX Architecture: **Complete**
* Phase 004 — Knowledge Architecture / OKF Governance: **Complete**
* Phase 005 — System/Application/Data/Synchronization Architecture: **Complete as historical architecture exit**
* Phase 006 — Implementation Planning & Delivery: **Historical after 006-D**
  * 006-A through 006-D: completed historical planning/bootstrap work
  * 006-D executable portion: retained and re-qualified by 008-B as the protected non-domain baseline
  * 006-E through 006-M: explicitly mapped/superseded by 008-C; preserved as planning lineage only
* Phase 007 — Jackson Design Refinement & Methodology Closure: **Complete — formal methodology exit passed**
* Phase 008 — Implementation Re-entry, Plan Refresh & Execution Readiness: **In Progress**
  * 008-A — Implementation Re-entry Authority, Canonical Baseline, Change Control & Planning Guardrails: **Complete**
  * 008-B — Protected 006-D Baseline Qualification, Drift Audit & Toolchain/Environment Reconciliation: **Complete — PASS AFTER NARROW REMEDIATION**
  * 008-C — Residual-Risk Ingestion, Historical 006 Mapping, Decision Register & Supersession Matrix: **Complete — PASS**
  * 008-D — Persistence, Temporal Truth, Versioning, Provenance, Governed Exceptions, Outbox, Projection & Migration Implementation Plan: **Complete — PASS**
  * 008-E — Identity, Authentication, Participation, Access, Session, Invitation, Secrets & Technical-Authority Implementation Plan: **Next**

## Current posture

The renewed Jackson Concept Design methodology is complete for the current MUDAC baseline. Implementation planning is active, but no executable domain slice has yet been authorized.

008-B qualified the retained 006-D executable substrate. 008-C reconciled every accepted residual/historical-plan item. 008-D now establishes the first detailed implementation contract while leaving the executable baseline unchanged and schema-free.

The current boundary is:

```text
Jackson Concept Design methodology: COMPLETE / EXITED
implementation planning authority: ESTABLISHED
008-A: COMPLETE
008-B: COMPLETE — PASS AFTER NARROW REMEDIATION
008-C: COMPLETE — PASS
008-D: COMPLETE — PASS
protected 006-D baseline: QUALIFIED FOR PHASE 008 PLANNING
persistence/history implementation plan: ACCEPTED / NOT IMPLEMENTED
008-E: NEXT / NOT STARTED
first executable domain slice: NOT YET AUTHORIZED
new domain implementation after 006-D: NOT STARTED
production readiness: NOT ESTABLISHED
```

A qualified bootstrap or accepted implementation plan is not implementation authorization. Phase 008 remains planning, qualification, reconciliation, and authorization work. Only 008-L may authorize a first executable domain slice, and actual new domain implementation then begins in Phase 009.

## Accepted persistence direction

008-D fixes the downstream database mechanics before Identity/API/browser/domain slice planning can depend on them:

```text
PostgreSQL authority database
  ├── 6 module-owned authoritative schemas
  ├── projection              non-authoritative
  └── platform                narrow shared technical records

current state       mutable owner roots + bigint revision
Version history     immutable owner-local lineage snapshots
Provenance          append-stable, module-local actor/author/authorizer history
exceptions          policy-specific immutable decisions
outbox              transactionally coupled, at-least-once
projections         explicit basis + idempotent convergence/rebuild
migrations          SQL-first forward, checksum/advisory-lock protected
retention           authoritative history preserved pending 008-K policy
```

Technical root revision is not a semantic Version. Queue/outbox ordering is not authoritative commit ordering. No generic soft-delete, catch-all status, central Provenance god-table, or universal override table is introduced.

## Reconciled implementation-plan direction

```text
008-D persistence / temporal / history / provenance / exception / outbox   COMPLETE
   ↓
008-E Identity / Participation / Access / session                          NEXT
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
   ↓
Phase 009 implementation
```

Repository protection remains an external administration/evidence limit: no repository rulesets are currently visible and branch-protection state cannot be read through the connected integration. Dependabot is configured, but its alert inventory is unavailable through the current connector. Those limitations remain assigned to 008-K/008-L.

## Current direction

Proceed to **008-E — Identity, Authentication, Participation, Access, Session, Invitation, Secrets & Technical-Authority Implementation Plan**.

008-E remains planning only. New domain persistence/authentication implementation is not authorized until 008-L explicitly authorizes a Phase 009 entry slice.

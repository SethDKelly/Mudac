# Phase 008 — Implementation Re-entry, Plan Refresh & Execution Readiness

Status: **In Progress — 008-A/B/C/D complete; 008-E next**

## Purpose

Convert the completed Jackson Concept Design baseline and accepted architecture into a refreshed, dependency-safe implementation plan without beginning new MUDAC domain implementation.

Phase 008 exists because the historical 006-E through 006-M plan predates the Phase 007 methodology refinements. Those records remain planning provenance and dependency evidence, but they are not current executable authority.

Current execution posture is owned by [Design / Implementation Boundary](../canonical/governance/design-implementation-boundary.md). Detailed Phase 008 records are indexed in [index.md](index.md).

## Phase boundary

```text
Phase 007
Jackson Concept Design COMPLETE / EXITED
        ↓
Phase 008
plan refresh + execution readiness
        ↓
008-L explicit first-slice authorization
        ↓
Phase 009
new domain implementation begins
```

No Phase 008 subgroup implements new domain behavior. The retained 006-D workspace remains a qualified protected non-domain implementation baseline.

## Completed entry, reconciliation and persistence-planning gates

[008-A](008-A-implementation-reentry-authority-canonical-baseline-change-control-planning-guardrails.md) is **Complete** and establishes current authority, `CHG-*` escalation, planning-versus-execution states, and progressive-disclosure/anti-bloat rules.

[008-B](008-B-protected-006-D-baseline-qualification-drift-audit-toolchain-environment-reconciliation.md) is **Complete — PASS AFTER NARROW REMEDIATION** and qualifies the retained 006-D executable substrate.

[008-C](008-C-residual-risk-ingestion-historical-006-mapping-decision-register-supersession-matrix.md) is **Complete — PASS** and closes residual/historical-plan ownership.

[008-D](008-D-persistence-temporal-truth-versioning-provenance-governed-exceptions-outbox-projection-migration-implementation-plan.md) is **Complete — PASS** and establishes the concrete downstream persistence/history substrate without creating domain schema.

008-D fixes these implementation-planning choices:

- one PostgreSQL authority database with six module-owned schemas plus non-authoritative `projection` and narrow technical `platform` schemas;
- stable UUID resource identity, per-root monotonic `bigint` revision, and explicit `timestamptz` temporal fields;
- mutable current/root state distinct from semantic Versioning and append-stable history;
- owner-local immutable Version lineage, Provenance, invalidation/replacement/correction records;
- policy-specific governed-exception records rather than a universal override table;
- immutable Official Outcome Revision physical substrate with a separate latest-declared pointer;
- a transactional at-least-once outbox whose message ordering is not treated as authority ordering;
- explicit-basis projections with idempotent/out-of-order convergence and generation-based rebuild by default;
- SQL-first owner-scoped forward migrations with checksum ledger, advisory locking, no runtime auto-migrate, and expand/migrate/contract deployment posture;
- conservative non-destructive retention until 008-K establishes applicable retention requirements.

Durable current implementation ownership for these choices lives in [Persistence, History, Provenance, Outbox, Projection & Migration Implementation Contract](../canonical/implementation/persistence-history-projection.md).

## Dependency-safe subgroup plan

| Group | Topic | Status |
| --- | --- | --- |
| 008-A | [Implementation Re-entry Authority, Canonical Baseline, Change Control & Planning Guardrails](008-A-implementation-reentry-authority-canonical-baseline-change-control-planning-guardrails.md) | **Complete** |
| 008-B | [Protected 006-D Baseline Qualification, Drift Audit & Toolchain/Environment Reconciliation](008-B-protected-006-D-baseline-qualification-drift-audit-toolchain-environment-reconciliation.md) | **Complete — PASS** |
| 008-C | [Residual-Risk Ingestion, Historical 006 Mapping, Decision Register & Supersession Matrix](008-C-residual-risk-ingestion-historical-006-mapping-decision-register-supersession-matrix.md) | **Complete — PASS** |
| 008-D | [Persistence, Temporal Truth, Versioning, Provenance, Governed Exceptions, Outbox, Projection & Migration Implementation Plan](008-D-persistence-temporal-truth-versioning-provenance-governed-exceptions-outbox-projection-migration-implementation-plan.md) | **Complete — PASS** |
| 008-E | **Identity, Authentication, Participation, Access, Session, Invitation, Secrets & Technical-Authority Implementation Plan** | **Next** |
| 008-F | **Commands, Queries, Transactions, CAS, Idempotency, Concurrency, Lost-Response Reconciliation & API Implementation Plan** | Planned |
| 008-G | **Browser Shell, Routing, Remote State, Draft Continuity, Synchronization, Recovery, Responsive & Accessibility Implementation Plan** | Planned |
| 008-H | **Competition Configuration, Team/Division/Alias, Rubric, Participation, Panel & Encounter Operations Slice Plan** | Planned |
| 008-I | **Scorecard, Evaluation Evidence, Amendment, Paper Capture, Verification & Convergence Slice Plan** | Planned |
| 008-J | **Reconciliation, Coverage, Aggregate, Rank, Awards, Finalization, Official Outcome, Export, Publication & Disclosure Slice Plan** | Planned |
| 008-K | **Security, Privacy, Accessibility, Observability, Performance, Recovery/DR, Retention & Operational Evidence Plan** | Planned |
| 008-L | **Consolidated Dependency Graph, Implementation Roadmap, First-Slice Authorization & Phase Exit Review** | Planned |

## Dependency rationale

```text
008-A authority and guardrails                         COMPLETE
   ↓
008-B retained substrate qualification                 COMPLETE
   ↓
008-C residual + historical-plan reconciliation        COMPLETE
   ↓
008-D durable data / temporal authority plan           COMPLETE
   ↓
008-E identity / access / session plan                 NEXT
   ↓
008-F command / API / concurrency plan
   ↓
008-G browser / Draft / recovery plan
   ↓
008-H competition + judging operations slices
   ↓
008-I evaluation evidence + paper slices
   ↓
008-J outcomes + externalization slices
   ↓
008-K cross-cutting verification / evidence gates
   ↓
008-L consolidated roadmap + first-slice authorization
   ↓
Phase 009 implementation
```

008-E follows 008-D because Identity/Participation/Access/session persistence can now rely on a fixed owner-local relational/history/migration substrate without inventing its own database conventions.

## Planning guardrails

Phase 008 still does not create domain tables, migrations, repositories, authentication/session behavior, domain APIs, IndexedDB domain state, product features, or domain-purpose AWS application resources.

A completed persistence plan is not persistence implementation. Green CI is not implementation authorization, merge authority, deployment authority, or production certification.

If planning exposes a genuine semantic contradiction or missing semantic owner, use `CHG-*`; implementation convenience does not silently weaken current design.

## Current status

```text
Jackson Concept Design: COMPLETE / EXITED
Phase 008 subdivision: COMPLETE
implementation planning authority: ESTABLISHED
008-A: COMPLETE
008-B: COMPLETE — PASS AFTER NARROW REMEDIATION
008-C: COMPLETE — PASS
008-D: COMPLETE — PASS
protected 006-D baseline: QUALIFIED FOR PHASE 008 PLANNING
historical 006-E–M executable queue: SUPERSEDED / MAPPED
008-E: NEXT / NOT STARTED
new domain implementation after 006-D: NOT STARTED
first executable slice: NOT YET AUTHORIZED
production readiness: NOT ESTABLISHED
```

## Next

Proceed to **008-E — Identity, Authentication, Participation, Access, Session, Invitation, Secrets & Technical-Authority Implementation Plan**.

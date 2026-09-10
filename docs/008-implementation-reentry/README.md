# Phase 008 — Implementation Re-entry, Plan Refresh & Execution Readiness

Status: **In Progress — 008-A complete; 008-B next**

## Purpose

Convert the completed Jackson Concept Design baseline and accepted architecture into a refreshed, dependency-safe implementation plan without beginning new MUDAC domain implementation.

Phase 008 exists because the historical 006-E through 006-M plan predates the Phase 007 methodology refinements. Those records remain planning provenance and dependency evidence, but they are not current executable authority.

Current execution posture is owned by [Design / Implementation Boundary](../canonical/governance/design-implementation-boundary.md). Detailed Phase 008 history and handoffs are indexed in [index.md](index.md).

## Phase boundary

Phase 008 is an **implementation-planning and execution-readiness phase**.

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

No 008 subgroup implements new domain behavior. Concrete implementation choices made during Phase 008 remain planning/implementation contracts until 008-L explicitly authorizes a first executable slice.

The retained 006-D workspace remains a protected non-domain implementation baseline throughout Phase 008.

## Current authority established by 008-A

[008-A — Implementation Re-entry Authority, Canonical Baseline, Change Control & Planning Guardrails](008-A-implementation-reentry-authority-canonical-baseline-change-control-planning-guardrails.md) is **Complete**.

It establishes the subject-sensitive constraint direction:

```text
canonical semantic / governance owners
        ↓
canonical architecture
        ↓
canonical implementation contracts
        ↓
Phase 008 planning decisions
        ↓
future executable realization and evidence
```

The Design / Implementation Boundary separately owns execution posture.

008-A also makes the following distinctions explicit:

```text
planning decision
    ≠
first-slice authorization
    ≠
code start
    ≠
merge readiness
    ≠
deployment readiness
    ≠
production readiness
```

If a proposed implementation mechanism conflicts with current canonical meaning, the mechanism changes by default. Genuine semantic contradictions, missing semantic ownership, or intentional product changes route through `CHG-*`; they are not resolved silently in Phase 008 plans, schemas, APIs, tests, components, or ADRs.

No new stable-rule namespace was required for 008-A; existing `DOC-*`, `CTX-*`, `CHG-*`, `IMPL-*`, and the current Design / Implementation Boundary already own the durable rules.

## Dependency-safe subgroup plan

| Group | Topic | Status |
| --- | --- | --- |
| 008-A | [Implementation Re-entry Authority, Canonical Baseline, Change Control & Planning Guardrails](008-A-implementation-reentry-authority-canonical-baseline-change-control-planning-guardrails.md) | **Complete** |
| 008-B | **Protected 006-D Baseline Qualification, Drift Audit & Toolchain/Environment Reconciliation** | **Next** |
| 008-C | **Residual-Risk Ingestion, Historical 006 Mapping, Decision Register & Supersession Matrix** | Planned |
| 008-D | **Persistence, Temporal Truth, Versioning, Provenance, Governed Exceptions, Outbox, Projection & Migration Implementation Plan** | Planned |
| 008-E | **Identity, Authentication, Participation, Access, Session, Invitation, Secrets & Technical-Authority Implementation Plan** | Planned |
| 008-F | **Commands, Queries, Transactions, CAS, Idempotency, Concurrency, Lost-Response Reconciliation & API Implementation Plan** | Planned |
| 008-G | **Browser Shell, Routing, Remote State, Draft Continuity, Synchronization, Recovery, Responsive & Accessibility Implementation Plan** | Planned |
| 008-H | **Competition Configuration, Team/Division/Alias, Rubric, Participation, Panel & Encounter Operations Slice Plan** | Planned |
| 008-I | **Scorecard, Evaluation Evidence, Amendment, Paper Capture, Verification & Convergence Slice Plan** | Planned |
| 008-J | **Reconciliation, Coverage, Aggregate, Rank, Awards, Finalization, Official Outcome, Export, Publication & Disclosure Slice Plan** | Planned |
| 008-K | **Security, Privacy, Accessibility, Observability, Performance, Recovery/DR, Retention & Operational Evidence Plan** | Planned |
| 008-L | **Consolidated Dependency Graph, Implementation Roadmap, First-Slice Authorization & Phase Exit Review** | Planned |

## Dependency rationale

The default planning order is:

```text
008-A authority and guardrails
   ↓
008-B retained substrate qualification
   ↓
008-C residual + historical-plan reconciliation
   ↓
008-D durable data / temporal authority plan
   ↓
008-E identity / access / session plan
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

This sequence prevents downstream convenience from defining upstream authority. Persistence/temporal semantics are planned before Identity/Access; Identity/Access before transport; server authority before browser continuity; operational context before evaluation evidence; evaluation evidence before official outcomes/publication; and cross-cutting verification before executable authorization.

## Subgroup scopes

**008-B** qualifies the retained 006-D toolchain, package topology, CI, local PostgreSQL, OpenTofu roots, supply-chain posture, and absence of accidental domain implementation against current authority.

**008-C** maps all 007-H Class 2/3 residuals and historical 006-E–M tasks into explicit current owners and records preserve/split/merge/reorder/rename/supersede dispositions while keeping Class 4 future scope out of the baseline.

**008-D** plans relational authority, temporal/history representation, Versioning, Provenance, governed exceptions, outbox/projections, migrations, and retention safeguards.

**008-E** plans provider authentication, stable Identity linkage, Participation/Access context, sessions, invitations, re-verification, technical/operator separation, and secrets boundaries.

**008-F** plans command/query surfaces, transactions, CAS, idempotency, concurrency, lost-response reconciliation, semantic errors, API contracts, and projection freshness.

**008-G** plans the React/browser realization, remote-cache boundaries, IndexedDB Draft continuity, synchronization/conflict recovery, role-mode isolation, responsive behavior, and accessibility.

**008-H** plans Competition preparation/live-operations slices across Team, Division, Alias, Rubric, Participation, Panel, and Encounter semantics.

**008-I** plans authoritative Scorecard evidence, Finalization, amendment, Judge authorship, paper capture/verification, duplicate convergence, invalidation, and correction paths.

**008-J** plans Reconciliation, Coverage, Aggregate, Rank, Awards, Finalization, Official Outcome Revision, Export, Publication, and disclosure without collapsing calculated/official/public/published states.

**008-K** derives security, privacy, accessibility, observability, performance, recovery/DR, retention, and operational evidence gates from the refreshed implementation plan.

**008-L** consolidates the dependency graph and implementation roadmap, identifies the smallest dependency-safe first executable slice, and explicitly decides whether that Phase 009 entry slice is authorized. 008-L itself still performs no domain implementation.

## Phase 008 planning guardrails

Phase 008 does not:

- create domain tables, migrations, repositories, authentication/session behavior, domain APIs, browser domain state, features, or domain-purpose AWS application resources;
- reopen completed Concept Design merely because implementation is inconvenient;
- treat historical 006-E–M labels as current slice authority;
- let code/tests/schemas/components/infra become alternate semantic owners;
- allow technical/operator capability to substitute for semantic authority;
- turn projections into editable authoritative sources;
- guess away uncertainty, history, correction, invalidation, supersession, or affected/stale state;
- treat green CI as implementation authorization, deployment authority, or production certification;
- pull future Stage/Round, student application, scheduling, notifications, calibrated scoring, rich public results, or advanced Award governance into the baseline without deliberate design change.

## Documentation and retrieval discipline

Phase 008 records preserve planning rationale, dependency decisions, accepted implementation choices, risks, and handoffs. Durable current rules belong in the applicable canonical owner.

Agents follow `CTX-*` progressive disclosure: load the current boundary, this phase route, and only the task-relevant canonical owners. Historical phase records are loaded when rationale, chronology, or supersession requires them—not recursively by default.

## Current status

```text
Jackson Concept Design: COMPLETE / EXITED
Phase 008 subdivision: COMPLETE
implementation planning authority: ESTABLISHED
008-A: COMPLETE
008-B: NEXT / NOT STARTED
protected 006-D baseline: NOT YET QUALIFIED BY PHASE 008
new domain implementation after 006-D: NOT STARTED
first executable slice: NOT YET AUTHORIZED
production readiness: NOT ESTABLISHED
```

## Next

Proceed to **008-B — Protected 006-D Baseline Qualification, Drift Audit & Toolchain/Environment Reconciliation**.

---
type: Documentation Authority
title: Design / Implementation Boundary
description: Defines MUDAC's current post-Concept-Design posture, active Phase 008 planning authority, qualified protected 006-D baseline, accepted persistence-plan contract, and the explicit gate before new domain implementation begins.
status: stable
tags: [governance, methodology, design, implementation, boundary, jackson, planning]
sources:
  - resource: ../../007-design-refinement/007-I-formal-jackson-concept-design-methodology-exit-accepted-residual-uncertainty-implementation-resume-boundary-decision.md
  - resource: ../../008-implementation-reentry/README.md
  - resource: ../../008-implementation-reentry/008-A-implementation-reentry-authority-canonical-baseline-change-control-planning-guardrails.md
  - resource: ../../008-implementation-reentry/008-B-protected-006-D-baseline-qualification-drift-audit-toolchain-environment-reconciliation.md
  - resource: ../../008-implementation-reentry/008-C-residual-risk-ingestion-historical-006-mapping-decision-register-supersession-matrix.md
  - resource: ../../008-implementation-reentry/008-D-persistence-temporal-truth-versioning-provenance-governed-exceptions-outbox-projection-migration-implementation-plan.md
  - resource: change-governance.md
  - resource: methodology-terminology.md
  - resource: ../synchronizations/concept-synchronizations.md
  - resource: ../synchronizations/temporal-truth-correction.md
  - resource: ../policies/operational-exception-governance.md
  - resource: ../experience/action-authority-traceability.md
  - resource: ../implementation/runtime-delivery-bootstrap.md
  - resource: ../implementation/implementation-foundation.md
  - resource: ../implementation/persistence-history-projection.md
generated: { by: openai/gpt-5.6-sol, at: 2026-09-10T19:13:00Z }
---

# Purpose

Keep the boundary between completed MUDAC Concept Design, active implementation planning, the qualified bootstrap substrate, future domain implementation, deployment authority, and production readiness explicit.

# Current state

MUDAC has formally exited the renewed Jackson Concept Design methodology for the current accepted baseline. 008-A established implementation-planning authority and guardrails. 008-B qualified the retained 006-D executable substrate. 008-C reconciled accepted residuals and historical 006-E–M into current owners. 008-D has now accepted the first detailed implementation contract for persistence, temporal/history, Versioning, Provenance, governed exceptions, outbox, projections and migrations.

The governing status is:

```text
Jackson Concept Design methodology: COMPLETE / EXITED
baseline semantic design: COMPLETE
known baseline semantic blockers: NONE OPEN
Phase 008 subdivision: COMPLETE
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

The formal design exit is scoped to the current baseline. New scope or a genuine later contradiction may require renewed design under canonical change governance.

# Current planning authority

Phase 008 follows the authority direction established in 008-A:

```text
canonical product / synchronization / policy / mechanism /
invariant / experience / governance meaning
        ↓
canonical architecture
        ↓
canonical implementation contracts
        ↓
Phase 008 implementation-planning decisions
        ↓
future executable realization and evidence
```

The Design / Implementation Boundary separately owns **execution posture**.

Historical phase records provide rationale/provenance. Routing artifacts route. Code, tests, schema, generated artifacts and IaC realize downstream choices. None silently replaces its upstream owner.

# Qualified protected 006-D baseline

008-B audited the retained non-domain workspace against current authority and found no semantic, architectural, or accidental-domain-implementation blocker.

The baseline remains qualified for later Phase 008 planning and contains only the accepted bootstrap class:

- pinned Node/pnpm/TypeScript/application-tool manifests and committed lockfile;
- minimal API, worker and browser composition roots;
- six authoritative module package seams without domain behavior;
- `application`, `projections`, `foundation`, and `test-support` boundaries;
- Docker Compose PostgreSQL without authoritative MUDAC schema/migrations;
- CI/static/dependency enforcement and supply-chain configuration;
- separate OpenTofu nonproduction/production/recovery roots without AWS application resources.

Qualification means the substrate may be relied upon as **planning input**. It does not authorize domain extension of that substrate.

# Reconciled residual and historical-plan ownership

008-C closes the ambiguity around accepted downstream uncertainty.

All six 007-H Class 2 architecture details and all twelve Class 3 implementation/evidence questions have current Phase 008 owners. The two 008-B administration/evidence limitations are carried to 008-K/008-L. All seven Class 4 future-scope items remain outside the current baseline unless `CHG-*` deliberately reopens them.

Historical 006-E through 006-M is fully superseded as an executable roadmap. Its useful dependency rationale remains provenance, but current planning routes only through 008-D through 008-L.

# Accepted 008-D persistence implementation contract

008-D resolves the physical persistence choices needed by downstream planning while remaining non-executable.

Current implementation planning may now assume:

- one PostgreSQL authority database with module-owned `competition`, `identity_access`, `judging_operations`, `evaluation`, `outcomes`, and `external_representation` schemas plus non-authoritative `projection` and narrow technical `platform` schemas;
- stable UUID resource identities and monotonic per-root `bigint` concurrency revisions;
- mutable current/root rows distinct from immutable semantic Version history;
- module-local Provenance with compatible actor/author/authorizer/source/time structure;
- explicit correction/invalidation/replacement records rather than universal status/soft-delete semantics;
- policy-specific immutable governed-exception records rather than a universal override table;
- immutable Official Outcome Revision substrate with a separate latest-declared pointer;
- transactionally coupled at-least-once outbox messages and basis-aware idempotent projections;
- generation-based rebuild for non-trivial cross-module projections by default;
- SQL-first owner-scoped forward migrations with checksum verification/advisory locking and no application-startup auto-migration;
- conservative non-destructive historical retention until 008-K resolves applicable retention requirements.

Durable detail is owned by [Persistence, History, Provenance, Outbox, Projection & Migration Implementation Contract](../implementation/persistence-history-projection.md).

These are **accepted planning constraints, not created database objects**.

# What Phase 008 planning authority permits

Current work may:

- use the qualified 006-D substrate as a concrete starting assumption;
- consume the 008-C residual/historical-plan ownership map;
- consume the accepted 008-D persistence/history implementation contract;
- define concrete downstream Identity/Access, transaction/API, browser, vertical-slice, outcome/externalization and evidence mechanisms where upstream authority leaves implementation latitude;
- create implementation decision records where `IMPL-015` warrants them;
- update canonical implementation owners when durable downstream contracts change;
- define verification/evidence gates and explicit implementation-entry criteria;
- prepare a specifically bounded first domain implementation slice for 008-L authorization.

008-E is next and owns Identity, Authentication, Participation, Access, Session, Invitation, Secrets & Technical-Authority implementation planning.

# What Phase 008 does not authorize

Completion of 008-A through 008-D does **not** authorize domain implementation.

Until **008-L — Consolidated Dependency Graph, Implementation Roadmap, First-Slice Authorization & Phase Exit Review** explicitly authorizes a first executable slice, do not create new:

- authoritative domain PostgreSQL schemas, migrations, repositories, outbox or projections described by 008-D;
- Cognito/session/Identity/Participation/Access/invitation behavior;
- production domain commands, queries, APIs, transactions or idempotency behavior;
- IndexedDB domain Draft/synchronization behavior;
- Competition/Judging/Evaluation/Outcome/Award/Export/Publication feature behavior;
- domain-purpose AWS application provisioning/deployment.

The status distinctions remain:

```text
qualified bootstrap
    ≠
accepted implementation plan
    ≠
first executable slice authorized
    ≠
domain implementation started
    ≠
merge ready
    ≠
deployment ready
    ≠
production ready
```

008-L may authorize a Phase 009 entry slice. 008-L itself performs no domain implementation.

# Phase 006 treatment

Phase 006 remains historical implementation-planning/bootstrap provenance.

006-A through 006-D accurately record prior planning/bootstrap work. The executable portion of 006-D was re-qualified by 008-B rather than silently resumed.

006-E through 006-M remain preserved historical planning lineage but are fully superseded as current executable authority. Their explicit disposition is owned by 008-C. The persistence-planning substance historically assigned to 006-E is now superseded by the current 008-D record and canonical implementation contract.

# Open evidence and administration limits

008-C carries the 008-B limitations forward to named owners:

1. repository rulesets/branch-protection enforcement remains an 008-K evidence/admin item and an 008-L authorization consideration; workflow existence must not be represented as enforced merge policy;
2. Dependabot alert inventory remains unavailable through the current connector and is assigned to 008-K security evidence; zero open dependency findings must not be inferred.

008-D additionally leaves actual retention periods, backup/restore objectives, production RDS sizing, migration deployment evidence and projection recovery exercises to 008-K rather than claiming planning equals operational readiness.

# Change control during implementation planning

Completed Concept Design remains current semantic authority, not immutable dogma.

If planning or later implementation discovers a genuine canonical contradiction, missing independent Concept, impossible synchronization/authority requirement, unmodeled correction/history condition, or material new product scope, return through `CHG-*` and deliberate design as necessary.

If an implementation mechanism merely conflicts with current canonical meaning, the mechanism changes by default under `CHG-005` and `IMPL-001`.

Implementation inconvenience, framework preference, storage convenience, UI convenience, testing convenience, or technical/operator privilege alone does not authorize semantic weakening.

# Documentation and context boundary

Phase 008 follows `DOC-*` and `CTX-*`:

- canonical owners control durable current meaning;
- numbered Phase 008 records preserve planning rationale/evidence without becoming a parallel rule store;
- `persistence-history-projection.md` owns the durable implementation result from 008-D;
- historical phases are loaded only when rationale, chronology, or supersession requires them;
- routing artifacts summarize and link rather than own rules;
- agents stop expanding context once the material authority set is sufficient.

# Current handoff

Proceed to **008-E — Identity, Authentication, Participation, Access, Session, Invitation, Secrets & Technical-Authority Implementation Plan** under [Phase 008](../../008-implementation-reentry/).

008-E may rely on the accepted 008-D persistence contract as planning input. New domain implementation remains **NOT STARTED** and no first executable slice is authorized until 008-L explicitly changes this boundary.

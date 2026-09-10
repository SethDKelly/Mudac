---
type: Documentation Authority
title: Design / Implementation Boundary
description: Defines MUDAC's current post-Concept-Design posture, Phase 008 planning authority, qualified protected 006-D baseline, reconciled residual/historical-plan ownership, and the explicit gate before new domain implementation begins.
status: stable
tags: [governance, methodology, design, implementation, boundary, jackson, planning]
sources:
  - resource: ../../007-design-refinement/007-I-formal-jackson-concept-design-methodology-exit-accepted-residual-uncertainty-implementation-resume-boundary-decision.md
  - resource: ../../008-implementation-reentry/README.md
  - resource: ../../008-implementation-reentry/008-A-implementation-reentry-authority-canonical-baseline-change-control-planning-guardrails.md
  - resource: ../../008-implementation-reentry/008-B-protected-006-D-baseline-qualification-drift-audit-toolchain-environment-reconciliation.md
  - resource: ../../008-implementation-reentry/008-C-residual-risk-ingestion-historical-006-mapping-decision-register-supersession-matrix.md
  - resource: change-governance.md
  - resource: methodology-terminology.md
  - resource: ../synchronizations/concept-synchronizations.md
  - resource: ../synchronizations/temporal-truth-correction.md
  - resource: ../policies/operational-exception-governance.md
  - resource: ../experience/action-authority-traceability.md
  - resource: ../implementation/runtime-delivery-bootstrap.md
  - resource: ../implementation/implementation-foundation.md
generated: { by: openai/gpt-5.6-sol, at: 2026-09-10T18:04:00Z }
---

# Purpose

Keep the boundary between completed MUDAC Concept Design, active implementation planning, the qualified bootstrap substrate, future domain implementation, deployment authority, and production readiness explicit.

# Current state

MUDAC has formally exited the renewed Jackson Concept Design methodology for the current accepted baseline. 008-A established implementation-planning authority and guardrails. 008-B qualified the retained 006-D executable substrate. 008-C has now reconciled the accepted residual register and historical 006-E through 006-M plan into explicit current Phase 008 ownership.

The governing status is:

```text
Jackson Concept Design methodology: COMPLETE / EXITED
baseline semantic design: COMPLETE
known baseline semantic blockers: NONE OPEN
Phase 008 subdivision: COMPLETE
implementation planning authority: ESTABLISHED
008-A: COMPLETE
008-B: COMPLETE — PASS AFTER NARROW REMEDIATION
protected 006-D baseline: QUALIFIED FOR PHASE 008 PLANNING
008-C: COMPLETE — PASS
residual ownership: CLOSED FOR CURRENT BASELINE
historical 006-E–M executable queue: SUPERSEDED / MAPPED
008-D: NEXT / NOT STARTED
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

The baseline is qualified for later Phase 008 planning and contains only the accepted bootstrap class:

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

All six 007-H Class 2 architecture details and all twelve Class 3 implementation/evidence questions now have current Phase 008 planning owners. The two 008-B administration/evidence limitations are carried to 008-K/008-L. All seven Class 4 future-scope items remain outside the current baseline unless `CHG-*` deliberately reopens them.

Historical 006-E through 006-M is now fully superseded as an executable roadmap. Its useful dependency rationale remains provenance, but current planning routes only through 008-D through 008-L.

The material decomposition changes include:

- browser Draft/synchronization/conflict foundation moves from old 006-J into 008-G;
- old 006-L externalization work merges into 008-J so outcomes, Finalization, Official Outcome Revision, Export, Publication and disclosure stay in one downstream authority chain without collapsing their meanings;
- old 006-M splits into 008-K cross-cutting evidence/readiness planning and 008-L consolidated authorization/exit.

008-C does not decide the physical mechanisms assigned to later groups. It makes those decisions visible, owned and dependency-ordered.

# What Phase 008 planning authority permits

Current work may:

- use the qualified 006-D substrate as a concrete starting assumption;
- consume the 008-C residual/historical-plan ownership map;
- define concrete downstream mechanisms where accepted architecture and semantics leave implementation latitude;
- create implementation decision records where `IMPL-015` warrants them;
- update canonical architecture/implementation owners when durable downstream contracts change;
- define verification/evidence gates and explicit implementation-entry criteria;
- prepare a specifically bounded first domain implementation slice for 008-L authorization.

008-D is next and owns the detailed persistence, temporal-history, Versioning, Provenance, governed-exception, outbox, projection and migration implementation plan.

# What Phase 008 does not authorize

Completion of 008-A through 008-C does **not** authorize domain implementation.

Until **008-L — Consolidated Dependency Graph, Implementation Roadmap, First-Slice Authorization & Phase Exit Review** explicitly authorizes a first executable slice, do not create new:

- authoritative domain PostgreSQL schemas, migrations, repositories, outbox or projections;
- Cognito/session/Identity/Participation/Access/invitation behavior;
- production domain commands, queries, APIs, transactions or idempotency behavior;
- IndexedDB domain Draft/synchronization behavior;
- Competition/Judging/Evaluation/Outcome/Award/Export/Publication feature behavior;
- domain-purpose AWS application provisioning/deployment.

The status distinctions remain:

```text
qualified bootstrap
    ≠
planning decision
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

006-E through 006-M remain preserved historical planning lineage but are **fully superseded as current executable authority**. Their explicit preserve/split/merge/rename/reorder disposition is owned by 008-C.

# Open evidence and administration limits

008-C carries the 008-B limitations forward to named owners:

1. repository rulesets/branch-protection enforcement remains an 008-K evidence/admin item and an 008-L authorization consideration; workflow existence must not be represented as enforced merge policy;
2. Dependabot alert inventory remains unavailable through the current connector and is assigned to 008-K security evidence; zero open dependency findings must not be inferred.

Neither limit blocks continued Phase 008 planning. Both become consequential when later gates rely on them.

# Change control during implementation planning

Completed Concept Design remains current semantic authority, not immutable dogma.

If planning or later implementation discovers a genuine canonical contradiction, missing independent Concept, impossible synchronization/authority requirement, unmodeled correction/history condition, or material new product scope, return through `CHG-*` and deliberate design as necessary.

If an implementation mechanism merely conflicts with current canonical meaning, the mechanism changes by default under `CHG-005` and `IMPL-001`.

Implementation inconvenience, framework preference, storage convenience, UI convenience, testing convenience, or technical/operator privilege alone does not authorize semantic weakening.

# Documentation and context boundary

Phase 008 follows `DOC-*` and `CTX-*`:

- canonical owners control durable current meaning;
- numbered Phase 008 records preserve planning rationale and evidence without becoming a parallel rule store;
- 008-C is the provenance owner for residual/historical-plan mapping rather than a new canonical rule namespace;
- historical phases are loaded only when rationale, chronology, or supersession requires them;
- routing artifacts summarize and link rather than own rules;
- agents stop expanding context once the material authority set is sufficient.

# Current handoff

Proceed to **008-D — Persistence, Temporal Truth, Versioning, Provenance, Governed Exceptions, Outbox, Projection & Migration Implementation Plan** under [Phase 008](../../008-implementation-reentry/).

008-D may rely on the qualified bootstrap and 008-C ownership map as planning inputs. New domain implementation remains **NOT STARTED** and no first executable slice is authorized until 008-L explicitly changes this boundary.

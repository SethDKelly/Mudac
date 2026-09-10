---
type: Documentation Authority
title: Design / Implementation Boundary
description: Defines MUDAC's current post-Concept-Design posture, implementation-planning authority, protected 006-D baseline, Phase 008 execution boundary, and the gate before new domain implementation begins.
status: stable
tags: [governance, methodology, design, implementation, boundary, jackson, planning]
sources:
  - resource: ../../007-design-refinement/007-A-design-reentry-implementation-freeze-jackson-completion-criteria.md
  - resource: ../../007-design-refinement/007-B-concept-completeness-independence-genericity-audit.md
  - resource: ../../007-design-refinement/007-C-cross-concept-synchronization-completeness-authority-seam-audit.md
  - resource: ../../007-design-refinement/007-D-temporal-state-correction-invalidation-supersession-historical-truth-closure.md
  - resource: ../../007-design-refinement/007-E-end-to-end-scenario-exception-failure-adversarial-authority-validation.md
  - resource: ../../007-design-refinement/007-F-judge-organizer-experience-concept-action-synchronization-authority-traceability-audit.md
  - resource: ../../007-design-refinement/007-G-policy-representation-outcome-disclosure-operational-governance-closure-audit.md
  - resource: ../../007-design-refinement/007-H-cross-layer-design-completeness-residual-semantic-risk-jackson-methodology-exit-readiness-audit.md
  - resource: ../../007-design-refinement/007-I-formal-jackson-concept-design-methodology-exit-accepted-residual-uncertainty-implementation-resume-boundary-decision.md
  - resource: ../../008-implementation-reentry/README.md
  - resource: ../../008-implementation-reentry/008-A-implementation-reentry-authority-canonical-baseline-change-control-planning-guardrails.md
  - resource: change-governance.md
  - resource: methodology-terminology.md
  - resource: ../synchronizations/concept-synchronizations.md
  - resource: ../synchronizations/temporal-truth-correction.md
  - resource: ../policies/operational-exception-governance.md
  - resource: ../experience/action-authority-traceability.md
  - resource: ../implementation/runtime-delivery-bootstrap.md
  - resource: ../implementation/implementation-foundation.md
generated: { by: openai/gpt-5.6-sol, at: 2026-09-10T15:04:00Z }
---

# Purpose

Keep the current boundary between completed MUDAC Concept Design, active implementation planning, retained bootstrap code, future domain implementation, and production readiness explicit.

This owner preserves the historical 006-D implementation freeze as provenance, records the later 007-I methodology exit, and now incorporates the 008-A planning-authority reset that governs Phase 008.

# Current state

MUDAC has formally exited the renewed Jackson Concept Design methodology for the current accepted baseline. Phase 008 has been subdivided, and 008-A has established the current implementation-planning authority hierarchy and guardrails.

The governing status is:

```text
Jackson Concept Design methodology: COMPLETE / EXITED
baseline semantic design: COMPLETE
known baseline semantic blockers: NONE OPEN
Phase 008 subdivision: COMPLETE
implementation planning authority: ESTABLISHED
008-A: COMPLETE
008-B: NEXT / NOT STARTED
protected 006-D baseline: NOT YET QUALIFIED BY PHASE 008
first executable domain slice: NOT YET AUTHORIZED
new domain implementation after 006-D: NOT STARTED
production readiness: NOT ESTABLISHED
```

The formal design exit is scoped to the current baseline. New scope or a genuine later contradiction may require a new design cycle under canonical change governance.

# Current planning authority

008-A establishes the subject-sensitive authority hierarchy used throughout Phase 008:

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

The hierarchy does not make Phase 008 records a second canonical tree. Durable current decisions belong in the applicable canonical owner; numbered Phase 008 records preserve rationale, dependency decisions, accepted implementation choices, residual risks, and handoff evidence.

The current Design / Implementation Boundary separately owns **execution posture**.

# What Phase 008 planning authority permits

Current work may:

- reconcile the retained 006-D substrate against completed canonical design and accepted architecture;
- refresh implementation slices and dependency ordering;
- map the 007-H residual issue register into architecture/implementation/evidence tasks;
- define concrete downstream implementation mechanisms where accepted architecture and semantics sufficiently constrain the choice;
- create implementation decision records where `IMPL-015` warrants them;
- update canonical architecture/implementation owners when a durable downstream contract changes;
- define verification gates and explicit implementation-entry criteria;
- prepare an explicit first domain implementation slice for authorization.

The active Phase 008 routing is [Implementation Re-entry, Plan Refresh & Execution Readiness](../../008-implementation-reentry/).

# What Phase 008 does not authorize

Neither the Phase 008 subdivision nor completion of 008-A authorizes domain implementation.

Until **008-L — Consolidated Dependency Graph, Implementation Roadmap, First-Slice Authorization & Phase Exit Review** explicitly authorizes a first executable slice, do not advance into new:

- domain PostgreSQL schema, migrations, repositories, or projections;
- Cognito/session/Identity/Participation/Access/invitation behavior;
- production domain commands, queries, APIs, transaction/idempotency behavior;
- IndexedDB Draft synchronization semantics;
- Competition/Judging/Evaluation/Outcome/Award/Export/Publication feature behavior;
- application AWS provisioning whose purpose is to advance those domain paths.

The distinction is intentional:

```text
implementation planning active
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

008-L may authorize a Phase 009 entry slice. 008-L itself still performs no domain implementation.

# Protected 006-D baseline

The executable workspace created in 006-D remains accepted as a **protected non-domain bootstrap baseline**.

It may contain the pinned workspace/toolchain manifests and lockfile; minimal API, worker and browser composition roots; package/module seams without domain behavior; local PostgreSQL service bootstrap without authoritative domain schema; CI/static/dependency checks; OpenTofu environment/root scaffolding without production application provisioning; and supply-chain/security automation needed to keep the substrate maintainable.

Before first-slice authorization, permitted executable changes remain limited to narrow dependency/security/compatibility maintenance, non-domain verification/tooling repair, documentation/routing changes, and removal of accidental behavior that conflicts with current canonical design.

008-A does not qualify this substrate as current or drift-free. That is the purpose of 008-B.

# Phase 006 treatment

Phase 006 remains historical implementation-planning/bootstrap provenance.

006-A through 006-D accurately record earlier planning and the bootstrap work that occurred before design re-entry. 006-E through 006-M remain useful dependency reasoning, but are **superseded as the current executable queue** because they predate the Phase 007 refinements.

They must not be resumed mechanically.

Phase 008 may preserve, split, merge, rename, reorder, or replace those slices while retaining useful rationale and provenance. 008-C owns the explicit disposition mapping after 008-B qualifies the retained substrate.

# Required Phase 008 refresh

Before new domain implementation starts, Phase 008 must refresh the implementation plan against current canonical design, including at minimum:

- temporal/correction/invalidation/replacement and latest-declared-official + Affected semantics;
- explicit authority-establishing versus derived/convergent synchronization effects;
- adversarial technical/break-glass and irreversible disclosure-exposure findings;
- Judge/Organizer experience action/authority traceability;
- Operational Exception & Override Governance;
- Export representation-authority monotonicity;
- purpose/source-specific Publication prerequisites;
- the 007-H residual architecture/implementation/evidence register.

The refreshed plan must identify a dependency-safe first implementation slice and explicitly authorize it before new domain code begins.

Phase 008 ordering keeps authority/baseline qualification before durable persistence planning; persistence before Identity/Access; Identity/Access before commands/API; server contracts before browser continuity; operational domain slices before evaluation evidence; evaluation evidence before official outcomes/externalization; and cross-cutting verification before first-slice authorization.

# Change-control during implementation planning

Completed Concept Design remains current semantic authority, not immutable dogma.

If implementation planning or later implementation discovers a real canonical contradiction, missing independent Concept, impossible synchronization/authority requirement, unmodeled correction/history condition, or material new product scope, return through `CHG-*` and deliberate design as necessary.

If an implementation mechanism merely conflicts with current canonical meaning, the implementation mechanism changes by default under `CHG-005` and `IMPL-001`.

Implementation inconvenience, framework preference, storage convenience, UI convenience, testing convenience, or technical/operator privilege alone does not authorize semantic weakening.

# Documentation and context boundary

Phase 008 follows `DOC-*` and `CTX-*`:

- canonical owners control durable current meaning;
- Phase 008 records preserve planning rationale and decisions without becoming a parallel rule store;
- historical phases are loaded only when rationale, chronology, or supersession requires them;
- routing artifacts summarize and link rather than owning rules;
- agents stop loading context once the material authority set is sufficient.

No Phase 008-specific stable-rule namespace is created merely to restate existing governance.

# Current methodology evidence

Phase 007 established and revalidated:

1. complete Purpose/State/Actions/Operational Principle ownership for the current sixteen Concepts;
2. Concept independence and genericity;
3. cross-Concept synchronization completeness;
4. temporal/correction/historical-truth closure;
5. ordinary, exceptional, adversarial, degraded, retry and recovery scenarios;
6. Judge/Organizer experience-to-authority traceability;
7. policy, outcome, disclosure, exception, Export and Publication closure;
8. cross-layer contradiction/back-drive review with no known baseline semantic blocker;
9. explicit formal methodology exit and accepted residual-uncertainty classification in 007-I.

These findings justify design exit. They do not establish implementation correctness, deployment readiness, or production readiness.

# Accepted residual uncertainty

The following categories are intentionally carried downstream rather than treated as unresolved Concept Design:

- physical temporal/history representation;
- governed-exception persistence/coordination realization;
- Official Outcome Revision materialization;
- Export/Artifact physical realization;
- cross-module coordinator placement;
- projection refresh/freshness realization;
- schema/API/session/synchronization/rendering/tooling choices;
- security/accessibility/performance/recovery evidence;
- repository administration and production operations;
- future Stage/Round, student application, scheduling, notifications, calibrated scoring, rich public results, and advanced Award governance.

Their detailed classification is owned by 007-H and accepted by 007-I. Phase 008 routes the Class 2 and Class 3 items into explicit implementation-plan owners while preserving Class 4 outside the current baseline.

# Relationship to historical exits

005-J remains historical evidence that the Phase 005 architecture was implementation-planning ready at that time.

007-A later froze execution and required renewed full-methodology closure. 007-B through 007-H supplied that evidence. 007-I formally exited the renewed methodology. Phase 008 now owns the active implementation-plan refresh, with 008-A establishing the authority model for that work.

None of those historical records is rewritten retroactively.

# Current handoff

Proceed to **008-B — Protected 006-D Baseline Qualification, Drift Audit & Toolchain/Environment Reconciliation** under [Phase 008](../../008-implementation-reentry/).

008-B may inspect and qualify the retained executable substrate and perform only boundary-permitted non-domain maintenance. New domain implementation remains **not started** and no first executable slice is authorized until 008-L explicitly changes this boundary.

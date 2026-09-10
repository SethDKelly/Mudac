---
type: Documentation Authority
title: Design / Implementation Boundary
description: Defines MUDAC's current post-Concept-Design posture, implementation-planning authority, protected 006-D baseline, required plan refresh, and the boundary before new domain implementation begins.
status: stable
tags: [governance, methodology, design, implementation, boundary, jackson]
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
  - resource: change-governance.md
  - resource: methodology-terminology.md
  - resource: ../synchronizations/concept-synchronizations.md
  - resource: ../synchronizations/temporal-truth-correction.md
  - resource: ../policies/operational-exception-governance.md
  - resource: ../experience/action-authority-traceability.md
  - resource: ../implementation/runtime-delivery-bootstrap.md
  - resource: ../implementation/implementation-foundation.md
generated: { by: openai/gpt-5.6-sol, at: 2026-09-10T14:31:00Z }
---

# Purpose

Keep the current boundary between completed MUDAC Concept Design, implementation planning, retained bootstrap code, new domain implementation, and production readiness explicit.

This owner preserves the historical 006-D implementation freeze as provenance while recording the later 007-I methodology exit that changes the current posture prospectively.

# Current state

MUDAC has formally exited the renewed Jackson Concept Design methodology for the current accepted baseline, and Phase 008 has now been divided into a dependency-safe implementation-reentry plan.

The governing status is:

```text
Jackson Concept Design methodology: COMPLETE / EXITED
baseline semantic design: COMPLETE
known baseline semantic blockers: NONE OPEN
Phase 008 subdivision: COMPLETE
implementation planning: ACTIVE
008-A: NEXT / NOT STARTED
first executable domain slice: NOT YET AUTHORIZED
new domain implementation after 006-D: NOT STARTED
production readiness: NOT ESTABLISHED
```

The formal exit is scoped to the current baseline. New scope or a genuine later contradiction may require a new design cycle under canonical change governance.

# What Phase 008 planning authority permits

Current work may now:

- reconcile the retained 006-D substrate against the completed canonical design;
- refresh implementation slices and dependency ordering;
- map the 007-H residual issue register into architecture/implementation/evidence tasks;
- define concrete downstream implementation mechanisms where accepted architecture and semantics sufficiently constrain the choice;
- define verification gates and explicit implementation-entry criteria;
- prepare an explicit first domain implementation slice for authorization.

The active Phase 008 routing is [Implementation Re-entry, Plan Refresh & Execution Readiness](../../008-implementation-reentry/).

# What Phase 008 does not authorize

The completed Phase 008 subdivision does **not** authorize agents to implement domain behavior.

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
```

# Protected 006-D baseline

The executable workspace created in 006-D remains accepted as a **protected non-domain bootstrap baseline**.

It may contain the pinned workspace/toolchain manifests and lockfile; minimal API, worker and browser composition roots; package/module seams without domain behavior; local PostgreSQL service bootstrap without authoritative domain schema; CI/static/dependency checks; OpenTofu environment/root scaffolding without production application provisioning; and supply-chain/security automation needed to keep the substrate maintainable.

Before first-slice authorization, permitted executable changes remain limited to narrow dependency/security/compatibility maintenance, non-domain verification/tooling repair, documentation/routing changes, and removal of accidental behavior that conflicts with current canonical design.

# Phase 006 treatment

Phase 006 remains historical implementation-planning/bootstrap provenance.

006-A through 006-D accurately record earlier planning and the bootstrap work that occurred before design re-entry. 006-E through 006-M remain useful dependency reasoning, but are **superseded as the current executable queue** because they predate the Phase 007 refinements.

They must not be resumed mechanically.

Phase 008 may preserve, split, merge, rename, reorder, or replace those slices while retaining useful rationale and provenance.

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

Phase 008 is subdivided so that authority/baseline qualification precedes durable persistence planning; persistence precedes Identity/Access; Identity/Access precedes commands/API; server contracts precede browser continuity; operational domain slices precede evaluation evidence; evaluation evidence precedes official outcomes/externalization; and cross-cutting verification precedes first-slice authorization.

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

These findings justify design exit. They do not establish production readiness or prove future implementation correctness.

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

Their detailed classification is owned by 007-H and accepted by 007-I. Phase 008 must route the Class 2 and Class 3 items into explicit implementation-plan owners while preserving Class 4 outside the current baseline.

# Change-control after design exit

Completed Concept Design remains current semantic authority, not immutable dogma.

If implementation planning or later implementation discovers a real canonical contradiction, missing independent Concept, impossible synchronization/authority requirement, unmodeled correction/history condition, or material new product scope, return through `CHG-*` and deliberate design as necessary.

Implementation inconvenience, framework preference, storage convenience, UI convenience, or technical/operator privilege alone does not authorize semantic weakening.

# Relationship to historical exits

005-J remains historical evidence that the Phase 005 architecture was implementation-planning ready at that time.

007-A later froze execution and required renewed full-methodology closure. 007-B through 007-H supplied that evidence. 007-I formally exited the renewed methodology. Phase 008 now owns the active implementation-plan refresh.

None of those historical records is rewritten retroactively.

# Current handoff

Proceed to **008-A — Implementation Re-entry Authority, Canonical Baseline, Change Control & Planning Guardrails** under [Phase 008](../../008-implementation-reentry/).

New domain implementation remains **not started** and no first executable slice is authorized until 008-L explicitly changes this boundary.
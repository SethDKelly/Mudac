---
type: Documentation Authority
title: Design / Implementation Boundary
description: Defines MUDAC's reopened Concept Design posture, suspended downstream architecture/implementation authority, frozen 006-D bootstrap, and the design-only gate that remains in force until successful methodology closure.
status: stable
tags: [governance, methodology, design, implementation, boundary, jackson, reentry]
sources:
  - resource: ../../009-jackson-methodology-realignment/009-A-methodology-authority-reset-prior-exit-reopen-design-only-guardrails.md
  - resource: ../../009-jackson-methodology-realignment/009-B-jackson-base-lifecycle-crosswalk-evidence-reuse-gap-map.md
  - resource: ../../009-jackson-methodology-realignment/009-C-downstream-authority-quarantine-completion-runway-phase-exit.md
  - resource: ../../010-project-purpose-candidate-specification-modularity/010-A-phase-intent-evidence-reuse-gap-closure-subphase-planning.md
  - resource: ../../010-project-purpose-candidate-specification-modularity/010-B-current-project-mandate-actors-outcomes-scope-constraints-evidence-reconciliation.md
  - resource: ../../010-project-purpose-candidate-specification-modularity/010-C-purpose-need-success-tension-purpose-to-concept-traceability-revalidation.md
  - resource: ../../010-project-purpose-candidate-specification-modularity/010-D-candidate-concept-rediscovery-divergent-alternatives-rejected-deferred-candidate-reassessment.md
  - resource: ../../010-project-purpose-candidate-specification-modularity/010-E-retained-concept-purpose-operational-principle-state-action-behavioral-specification-current-truth-audit.md
  - resource: ../../010-project-purpose-candidate-specification-modularity/010-F-specificity-purpose-singularity-concept-boundary-alternative-audit.md
  - resource: ../../010-project-purpose-candidate-specification-modularity/010-G-completeness-independence-genericity-for-boundary-audit.md
  - resource: ../project/mandate-context.md
  - resource: ../project/purpose-needs-success-tensions.md
  - resource: downstream-authority-quarantine.md
  - resource: methodology-terminology.md
  - resource: change-governance.md
---

# Purpose

Keep the boundary between reopened Jackson Concept Design, historical downstream work, the frozen 006-D bootstrap, future architecture/engineering handoff, implementation execution and production readiness explicit.

# Current state

Phase 009 reopened the previous 007-I methodology exit. Phase 010 is active. 010-A established the completion sequence; 010-B/C reconciled project and purpose truth; 010-D/E completed candidate rediscovery/behavioral specification; 010-F completed specificity/purpose singularity; and 010-G completed completeness, intrinsic-independence and genericity-for-boundary analysis for the eighteen validated candidates.

```text
Jackson Concept Design methodology: REOPENED / IN PROGRESS
previous 007-I methodology exit: SUPERSEDED AS CURRENT CLOSURE AUTHORITY
Phase 008 implementation re-entry: HALTED AFTER 008-E
008-A..E: HISTORICAL / PREMATURE DOWNSTREAM PLANNING
008-F..L: NOT STARTED / NOT ACTIVE
006-D executable bootstrap: FROZEN HISTORICAL NON-DOMAIN SUBSTRATE
canonical architecture authority: SUSPENDED PENDING DESIGN CLOSURE
canonical implementation authority: SUSPENDED PENDING DESIGN CLOSURE
implementation readiness: NOT READY
new domain implementation: NOT STARTED
implementation authorization: NOT YET
Phase 009: COMPLETE — PASS
Phase 010: IN PROGRESS
010-A: COMPLETE — PASS
010-B: COMPLETE — PASS
010-C: COMPLETE — PASS
010-D: COMPLETE — PASS
010-E: COMPLETE — PASS
010-F: COMPLETE — PASS
010-G: COMPLETE — PASS
010-H: NEXT
production readiness: NOT ESTABLISHED
```

# Current authority direction

During reopened Concept Design:

```text
human product intent / evidence
        ↓
canonical Project Context
        ↓
canonical Purpose / Needs / Success / Tensions
        ↓
phase-specific Jackson discovery/specification/modularity analysis
        ↓
corrected current conceptual owners after convergence

historical architecture / implementation
        = evidence or contamination probe only
        ≠ design constraint
```

The current project/purpose baseline is [Project Context & Purpose](../project/). The current boundary rationale is [010-F](../../010-project-purpose-candidate-specification-modularity/010-F-specificity-purpose-singularity-concept-boundary-alternative-audit.md), and the validated modularity result is [010-G](../../010-project-purpose-candidate-specification-modularity/010-G-completeness-independence-genericity-for-boundary-audit.md).

# What remains authoritative before 010-H

Current product/conceptual authority includes task-relevant canonical Project Context & Purpose, incumbent Concepts, synchronizations, policies, mechanisms, invariants, experience/mapping knowledge, and methodology/documentation/change governance.

These owners remain subject to correction by Phases 010–017.

During the transition into 010-H:

- the current sixteen Concept pages remain incumbent current knowledge until the convergence commit makes new ownership unambiguous;
- 010-F/G validate an eighteen-candidate boundary set that 010-H must reconcile canonically;
- Evaluation Occurrence, Evaluation Obligation and Outcome Declaration are validated phase-level Concepts awaiting current owners;
- current Judging Encounter and Official Outcome Revision ownership are known to require convergence;
- Evaluation Sufficiency/Coverage and Reconciliation remain non-Concept;
- no architecture or implementation choice may decide the convergence result.

# Validated Phase-010 boundary set

010-G confirms the following eighteen candidates are complete/independent enough for canonical convergence when its re-specification corrections are applied:

```text
Competition
Division
Team
Panel
Evaluation Occurrence
Evaluation Obligation
Rubric
Scorecard
Award
Identity
Participation
Alias
Access
Versioning
Provenance
Outcome Declaration
Export
Publication
```

Mandatory own-purpose corrections entering 010-H are:

- Evaluation Obligation successor responsibility after previously terminal/satisfied work when valid application semantics require re-evaluation;
- Rubric response interpretation/validation queries;
- Versioning explicit invalidation/current-eligible-authority behavior;
- Export explicit representation-currency behavior.

010-G also requires appropriate abstract parameterization so direct peer Concept types do not create false intrinsic dependence.

This work does not authorize code, schemas, APIs, persistence or architecture.

# Project-purpose versus downstream constraints

Current representation-independent constraints include live-event operation, independent judgment, bias-sensitive identity disclosure, accessibility, degraded connectivity/device conditions, paper continuity, historical truth, explainability and separation of technical authority from competition judgment.

Current purpose obligations P-01–P-09 and their tensions are conceptual constraints. They do not select realization mechanisms.

Historical intent for:

```text
GitHub → GitHub Actions → AWS ecosystem
```

is retained only as a downstream delivery constraint. Existing Node/TypeScript/Fastify/React/PostgreSQL/OpenTofu choices remain historical implementation facts, not conceptual requirements.

# What is suspended

Until successful Phase 017 closure:

- Phase 005 architecture conclusions do not constrain Concept Design;
- `docs/canonical/architecture/` is preserved as candidate downstream knowledge, not current design authority;
- Phase 006 implementation planning is historical only;
- Phase 008 implementation planning is halted;
- `docs/canonical/implementation/` is preserved as downstream candidate/tooling knowledge, not current domain realization authority;
- 008-D persistence/history choices and 008-E identity/authentication/session choices are hypotheses requiring post-closure revalidation.

# Frozen 006-D executable substrate

The repository contains a non-domain bootstrap created before design completion was reassessed. It remains frozen and may receive only narrow safety/build maintenance that does not add MUDAC domain semantics or constrain design.

# Prohibited work during Phases 010–017

Do not begin or resume:

- domain database schemas/migrations/repositories/outbox/projections;
- login/session/Identity/Participation/Access implementation;
- production domain commands/queries/APIs/transactions/idempotency mechanisms;
- client-side domain Draft/synchronization implementation;
- Competition/Judging/Evaluation/Outcome/Award/Export/Publication feature code;
- domain-purpose AWS provisioning;
- implementation-plan continuation from 008-F through 008-L;
- architecture decisions intended to constrain remaining Concept Design.

# Permitted work

Current work may:

- execute Phases 010–017;
- update Project Context/Purpose or other canonical conceptual owners when design meaning changes;
- perform 010-H canonical Concept/mechanism re-specification and supersession;
- inspect historical architecture/implementation only for contamination, assumptions, counterexamples or later handoff evidence;
- maintain the frozen bootstrap narrowly for repository safety/buildability;
- improve documentation/routing/validation supporting the design process.

# Active Phase 010 decomposition

```text
010-A intent / evidence reuse / decomposition                 COMPLETE
010-B project/context reconciliation                          COMPLETE
010-C purpose / need / success / tensions                     COMPLETE
010-D candidate rediscovery / divergent alternatives          COMPLETE
010-E behavioral specification current-truth audit            COMPLETE
010-F specificity / purpose singularity / boundary options    COMPLETE
010-G completeness / independence / boundary genericity       COMPLETE
010-H convergence / re-specification / canonical reconciliation NEXT
010-I consolidation / exit / Phase 011 handoff
```

# Completion runway

```text
009 realignment / gap map                         COMPLETE
  ↓
010 foundational project/purpose/discovery/
    specification/modularity completion           IN PROGRESS
  ↓
011 composition / synchronization revalidation
  ↓
012 dependence / subsets / product-family / scope
  ↓
013 mapping / representation revalidation
  ↓
014 familiarity / reuse / genericity
  ↓
015 integrity / interference
  ↓
016 scenario / misfit / adversarial validation
  ↓
017 methodology completeness / canonical closure
```

# Meaning of future successful closure

A successful Phase 017 may establish Concept Design readiness for downstream work. It does **not** start implementation or grant implementation authorization; it authorizes only a separate architecture/engineering re-entry.

# Current handoff

Proceed to:

> **010-H — Concept Boundary Convergence, Re-specification & Canonical Reconciliation**

010-H must make the validated eighteen-candidate boundary set current and unambiguous, incorporate 010-G completeness/genericity corrections, preserve historical rationale/supersession, and leave Phase 011 synchronization plus Phase 012 inclusion dependence unresolved.
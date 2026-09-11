---
type: Documentation Authority
title: Design / Implementation Boundary
description: Defines MUDAC's reopened Concept Design posture, suspended downstream architecture/implementation authority, frozen 006-D bootstrap, and the design-only gate that remains in force until a successful methodology closure.
status: stable
tags: [governance, methodology, design, implementation, boundary, jackson, reentry]
sources:
  - resource: ../../009-jackson-methodology-realignment/009-A-methodology-authority-reset-prior-exit-reopen-design-only-guardrails.md
  - resource: ../../009-jackson-methodology-realignment/009-B-jackson-base-lifecycle-crosswalk-evidence-reuse-gap-map.md
  - resource: ../../009-jackson-methodology-realignment/009-C-downstream-authority-quarantine-completion-runway-phase-exit.md
  - resource: ../../010-project-purpose-candidate-specification-modularity/010-A-phase-intent-evidence-reuse-gap-closure-subphase-planning.md
  - resource: ../../010-project-purpose-candidate-specification-modularity/010-B-current-project-mandate-actors-outcomes-scope-constraints-evidence-reconciliation.md
  - resource: ../project/mandate-context.md
  - resource: downstream-authority-quarantine.md
  - resource: methodology-terminology.md
  - resource: change-governance.md
---

# Purpose

Keep the boundary between reopened Jackson Concept Design, historical downstream work, the frozen 006-D bootstrap, future architecture/engineering handoff, implementation execution and production readiness explicit.

# Current state

Phase 009 reopened the previous 007-I methodology exit. Phase 010 is active. Its 010-A start gate established the foundational completion sequence and 010-B reconciled current project/intake truth independently of the incumbent Concept catalog.

Current governing posture:

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
010-C: NEXT
production readiness: NOT ESTABLISHED
```

# Current authority direction

During reopened Concept Design:

```text
human product intent / evidence
        ↓
canonical Project Context
        ↓
phase-specific Jackson methodology analysis
        ↓
corrected current conceptual owners

historical architecture / implementation
        = evidence or contamination probe only
        ≠ design constraint
```

The current project/intake baseline is [MUDAC Project Mandate & Current Context](../project/mandate-context.md). The durable quarantine rule is [Downstream Architecture & Implementation Authority Quarantine](downstream-authority-quarantine.md).

# What remains authoritative

Current product/conceptual authority includes task-relevant canonical:

- Project Context;
- Concepts;
- synchronizations and temporal/correction semantics;
- policies;
- mechanisms where intentionally non-Concepts;
- invariants;
- conceptual experience/mapping knowledge;
- methodology/documentation/change governance.

These owners remain subject to correction by Phases 010–017.

During Phase 010, the current sixteen-Concept catalog is an incumbent design hypothesis. It may be changed when purpose, rediscovery, specification or modularity evidence warrants it.

# Project-context versus downstream constraints

010-B established that live-event operation, independent judgment, bias-sensitive identity disclosure, accessibility, degraded connectivity/device conditions, paper continuity, historical truth, explainability and separation of technical authority from competition judgment are current representation-independent constraints.

Historical intent for:

```text
GitHub → GitHub Actions → AWS ecosystem
```

is retained only as a downstream delivery constraint. It does not determine Concepts, state/actions, UI mapping, persistence, authentication, APIs, services or AWS resources.

# What is suspended

Until successful Phase 017 closure:

- Phase 005 architecture conclusions do not constrain Concept Design;
- `docs/canonical/architecture/` is preserved as candidate downstream knowledge, not current design authority;
- Phase 006 implementation planning is historical only;
- Phase 008 implementation planning is halted;
- `docs/canonical/implementation/` is preserved as downstream candidate/tooling knowledge, not current domain realization authority;
- 008-D persistence/history choices and 008-E identity/authentication/session choices are hypotheses requiring post-closure revalidation.

# Frozen 006-D executable substrate

The repository already contains a non-domain bootstrap created before design completion was reassessed.

It remains frozen and may receive only narrow safety/build maintenance that does not add MUDAC domain semantics or constrain the design. Existing Node/TypeScript/Fastify/React/PostgreSQL/OpenTofu choices are historical implementation facts, not conceptual requirements.

# Prohibited work during Phases 010–017

Do not begin or resume:

- domain PostgreSQL schemas, migrations, repositories, outbox or projections;
- Cognito/login/session/Identity/Participation/Access implementation;
- production domain commands, queries, APIs, transactions or idempotency mechanisms;
- IndexedDB domain Draft/synchronization implementation;
- Competition/Judging/Evaluation/Outcome/Award/Export/Publication feature code;
- domain-purpose AWS application provisioning;
- implementation-plan continuation from 008-F through 008-L;
- architecture decisions intended to constrain remaining Concept Design.

# Permitted work

Current work may:

- execute Phases 010–017 of the methodology completion runway;
- update Project Context or other canonical conceptual owners when design meaning changes;
- inspect historical architecture/implementation only for contamination, assumptions, counterexamples or later handoff evidence;
- maintain the frozen bootstrap narrowly for repository safety/buildability;
- improve documentation/routing/validation supporting the design process.

# Active Phase 010 decomposition

```text
010-A intent / evidence reuse / decomposition                 COMPLETE
  ↓
010-B project mandate / actors / outcomes / scope / evidence  COMPLETE
  ↓
010-C purpose / need / success / tension / traceability       NEXT
  ↓
010-D candidate rediscovery / divergent alternatives
  ↓
010-E behavioral specification current-truth audit
  ↓
010-F specificity / purpose singularity / boundary options
  ↓
010-G completeness / independence / boundary genericity
  ↓
010-H convergence / re-specification / canonical reconciliation
  ↓
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

A successful Phase 017 may establish:

```text
Concept Design readiness for downstream work: READY
implementation execution: NOT STARTED
implementation authorization: NOT GRANTED BY CONCEPT-DESIGN CLOSURE
```

It will authorize only a separate downstream architecture/engineering re-entry. It will not automatically reactivate Phase 005 architecture, Phase 008 planning or any old first-slice proposal.

# Current handoff

Proceed to:

> **010-C — Purpose, Need, Success, Tension & Purpose-to-Concept Traceability Revalidation**

010-C begins from [Canonical Project Context](../project/mandate-context.md) and must not derive purpose from incumbent Concept names.

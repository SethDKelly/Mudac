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
  - resource: downstream-authority-quarantine.md
  - resource: methodology-terminology.md
  - resource: change-governance.md
---

# Purpose

Keep the boundary between reopened Jackson Concept Design, historical downstream work, the frozen 006-D bootstrap, future architecture/engineering handoff, implementation execution, and production readiness explicit.

# Current state

A fresh methodology review superseded the previous 007-I Concept Design closure as current authority. Phase 009 has completed the formal realignment/gap map and established the dependency-safe completion runway.

Current governing posture:

```text
Jackson Concept Design methodology: REOPENED / NOT COMPLETE
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
Phase 010: NEXT
production readiness: NOT ESTABLISHED
```

# Current authority direction

During reopened Concept Design:

```text
human product intent / evidence
        ↓
current canonical conceptual owners
        ↓
phase-specific Jackson methodology analysis
        ↓
corrected current conceptual design

historical architecture / implementation
        = evidence or contamination probe only
        ≠ design constraint
```

The durable quarantine rule is [Downstream Architecture & Implementation Authority Quarantine](downstream-authority-quarantine.md).

# What remains authoritative

Current product/conceptual authority remains in task-relevant canonical:

- Concepts;
- synchronizations and temporal/correction semantics;
- policies;
- mechanisms where they are intentionally non-Concepts;
- invariants;
- conceptual experience/mapping knowledge;
- methodology/documentation/change governance.

These owners are subject to correction by the remaining Jackson phases. Historical phase records remain evidence and rationale rather than immutable truth.

# What is suspended

Until successful Phase 017 closure:

- Phase 005 architecture conclusions do not constrain Concept Design;
- `docs/canonical/architecture/` is preserved as candidate downstream knowledge, not current design authority;
- Phase 006 implementation planning is historical only;
- Phase 008 implementation planning is halted;
- `docs/canonical/implementation/` is preserved as downstream candidate/tooling knowledge, not current domain realization authority;
- 008-D persistence/history choices and 008-E identity/authentication/session choices are hypotheses requiring post-closure revalidation.

# Frozen 006-D executable substrate

The repository already contains a real non-domain bootstrap created before design completion was reassessed.

It remains frozen and may receive only narrow safety/build maintenance that does not add MUDAC domain semantics or constrain the design. Existing Node/TypeScript/Fastify/React/PostgreSQL/OpenTofu/tooling choices are historical implementation facts, not conceptual requirements.

# Prohibited work during Phases 010–017

Do not begin or resume:

- domain PostgreSQL schemas, migrations, repositories, outbox or projections;
- Cognito/login/session/Identity/Participation/Access implementation;
- production domain commands, queries, APIs, transactions or idempotency mechanisms;
- IndexedDB domain Draft/synchronization implementation;
- Competition/Judging/Evaluation/Outcome/Award/Export/Publication feature code;
- domain-purpose AWS application provisioning;
- implementation-plan continuation from 008-F through 008-L;
- architecture decisions intended to constrain the remaining Concept Design.

# Permitted work

Current work may:

- execute Phases 010–017 of the methodology completion runway;
- update canonical conceptual owners when design meaning changes;
- inspect historical architecture/implementation only for contamination, assumptions, counterexamples or later handoff evidence;
- maintain the frozen bootstrap narrowly for repository safety/buildability;
- improve documentation/routing/validation that supports the design process.

# Completion runway

```text
009 realignment / gap map                         COMPLETE
  ↓
010 purpose / rediscovery / specification /
    modularity completion                         NEXT
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

The sequence may reopen earlier design owners when later evidence exposes a defect.

# Meaning of future successful closure

A successful Phase 017 may establish:

```text
Concept Design readiness for downstream work: READY
implementation execution: NOT STARTED
implementation authorization: NOT GRANTED BY CONCEPT-DESIGN CLOSURE
```

It will authorize only a separate downstream architecture/engineering re-entry. It will not automatically reactivate Phase 005 architecture, Phase 008 planning, or any old first-slice proposal.

# Current handoff

Proceed to the **Phase 010 entry/decomposition exercise** for:

> **Phase 010 — Project/Purpose Traceability, Candidate Rediscovery, Specification & Modularity Completion**

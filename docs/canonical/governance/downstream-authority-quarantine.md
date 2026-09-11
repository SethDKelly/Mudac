---
type: Documentation Authority
title: Downstream Architecture & Implementation Authority Quarantine
description: Suspends premature architecture and implementation material from constraining reopened Concept Design while preserving it as historical evidence and future downstream candidate knowledge.
status: stable
tags: [governance, methodology, design, architecture, implementation, quarantine, jackson]
sources:
  - resource: ../../009-jackson-methodology-realignment/009-A-methodology-authority-reset-prior-exit-reopen-design-only-guardrails.md
  - resource: ../../009-jackson-methodology-realignment/009-B-jackson-base-lifecycle-crosswalk-evidence-reuse-gap-map.md
  - resource: ../../009-jackson-methodology-realignment/009-C-downstream-authority-quarantine-completion-runway-phase-exit.md
  - resource: design-implementation-boundary.md
  - resource: methodology-terminology.md
---

# Purpose

Prevent architecture, toolchain, persistence, authentication, API, cloud, source-topology or other downstream decisions made before complete Jackson Concept Design closure from back-driving the reopened conceptual design.

This contract preserves prior work rather than deleting it. It changes what that work is allowed to mean **now**.

# Governing rule

While Concept Design is reopened and incomplete:

```text
current conceptual product meaning
        ↓
remaining Jackson methodology work

architecture / implementation material
        = historical evidence or future candidate only
        ≠ conceptual constraint
        ≠ completion evidence
        ≠ implementation authorization
```

If downstream material conflicts with current or newly refined conceptual meaning, downstream material yields by default.

# Material under quarantine

## Canonical architecture

Files under `docs/canonical/architecture/` are preserved as the architecture MUDAC had selected before methodology completion was reassessed.

During Phases 009–017 they are **suspended as current design constraints**.

They may be loaded only when:

- testing whether architecture has contaminated conceptual meaning;
- understanding why a historical decision was made;
- identifying assumptions worth challenging during Concept Design;
- preparing for future post-closure architecture revalidation.

They must not be used to argue that a Concept, dependency, synchronization, mapping, scope choice, familiarity decision or integrity trade-off is correct because the architecture already expects it.

## Canonical implementation

Files under `docs/canonical/implementation/` are preserved as implementation/tooling knowledge produced before the reassessment.

During reopened Concept Design:

- 006-D bootstrap/toolchain facts remain historical executable facts;
- 008-D persistence/history realization is a **suspended downstream candidate**;
- 008-E identity/authentication/session realization is a **suspended downstream candidate**;
- later implementation-planning work is not active.

Implementation contracts do not currently constrain conceptual state, actions, authority, dependence, scope, mapping or lifecycle semantics.

## Phase 005 architecture records

Phase 005 records remain valuable architecture rationale and pressure-test evidence, but they are not evidence that Concept Design is complete. Their conclusions require post-closure revalidation before becoming active architecture authority again.

## Phase 006 implementation planning/bootstrap

006-A through 006-M remain historical implementation lineage.

006-D's executable substrate is frozen as a non-domain bootstrap/prototype. No framework, package, database, AWS or CI choice inside it becomes Concept Design authority.

## Phase 008 implementation re-entry

008-A through 008-E remain preserved historical planning records.

008-D and 008-E in particular are concrete downstream hypotheses that may later save work, but their physical choices must be reconsidered against the successfully closed conceptual design before adoption.

008-F through 008-L are not an active queue.

# Permitted maintenance of 006-D

Narrow executable maintenance may occur only when necessary to keep the repository safe/buildable, such as:

- critical dependency/security remediation;
- broken non-domain CI/tooling repair;
- compatibility maintenance that does not encode MUDAC semantics;
- removal of accidental behavior that conflicts with current design authority.

Do not use maintenance as a path to advance domain implementation.

# Concept-design context rule

During Phases 010–017, agents should load:

1. the current phase record/entry gate;
2. current canonical conceptual owners needed by that phase;
3. relevant historical design evidence;
4. this quarantine contract and Design / Implementation Boundary.

Do **not** preload canonical architecture or implementation knowledge unless the task explicitly needs it for contamination analysis or historical comparison.

This preserves Jackson's representation/implementation independence and limits agentic back-drive.

# Post-closure treatment

A successful future Phase 017 closure does not automatically reactivate quarantined downstream material.

Instead, a separate downstream architecture/engineering re-entry must:

- compare the closed conceptual design against prior architecture;
- retain choices still justified;
- revise or reject choices invalidated by design completion;
- decide what implementation planning is required;
- establish a fresh execution-authorization boundary.

No old phase number or prior `PASS` automatically restores authority.

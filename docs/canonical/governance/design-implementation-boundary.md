---
type: Documentation Authority
title: Design / Implementation Boundary
description: "Defines MUDAC's reopened Concept Design posture after Phase 012 dependence/product-family closure, with Phase 013 mapping entry authorized and downstream architecture/implementation authority still suspended through Phase 017 closure."
status: stable
tags: [governance, methodology, design, implementation, boundary, jackson, dependence, mapping, reentry]
sources:
  - resource: ../../009-jackson-methodology-realignment/009-A-methodology-authority-reset-prior-exit-reopen-design-only-guardrails.md
  - resource: ../../009-jackson-methodology-realignment/009-C-downstream-authority-quarantine-completion-runway-phase-exit.md
  - resource: ../../010-project-purpose-candidate-specification-modularity/010-I-phase-010-consolidation-methodology-coverage-decision-phase-011-handoff.md
  - resource: ../../011-concept-composition-synchronization/011-J-canonical-synchronization-reconciliation-phase-011-consolidation-phase-012-handoff.md
  - resource: ../../012-concept-dependence-product-family-subset-scope/012-K-canonical-dependence-reconciliation-phase-012-consolidation-phase-013-handoff.md
  - resource: ../dependence/application-family-dependence.md
  - resource: ../dependence/whole-graph-subset-validation.md
  - resource: ../dependence/product-family-scope.md
  - resource: ../experience/phase-013-entry-handoff.md
  - resource: downstream-authority-quarantine.md
---

# Purpose

Keep the boundary between reopened Jackson Concept Design, historical downstream work, the frozen 006-D bootstrap, future architecture/engineering handoff, implementation execution, and production readiness explicit.

# Current state

Phase 009 reopened the prior methodology exit. Phase 010 completed foundational Concept Design. Phase 011 completed representation-independent Concept composition/synchronization with **PASS**. Phase 012 completed Concept dependence, coherent-subset/product-family analysis, PF-01 scope selection and mapping handoff with **PASS**.

Phase 013 is now authorized to begin with its mandatory start gate:

> **013-A — Mapping Scope, Representation Semantics, Experience Risk & Subphase Planning**

```text
Jackson Concept Design methodology: REOPENED / IN PROGRESS
Phase 008 implementation re-entry: HALTED AFTER 008-E
006-D executable bootstrap: FROZEN HISTORICAL NON-DOMAIN SUBSTRATE
canonical architecture authority: SUSPENDED PENDING DESIGN CLOSURE
canonical implementation authority: SUSPENDED PENDING DESIGN CLOSURE
implementation readiness: NOT READY
new domain implementation: NOT STARTED
implementation authorization: NOT YET
Phase 009: COMPLETE — PASS
Phase 010: COMPLETE — PASS
Phase 011: COMPLETE — PASS
Phase 012: COMPLETE — PASS
Phase 013: AUTHORIZED
013-A: NEXT
production readiness: NOT ESTABLISHED
```

# Current authority direction

```text
human product intent / evidence
        ↓
canonical Project Context & Purpose
        ↓
current canonical Concepts / mechanisms / policies / invariants
        ↓
reconciled canonical synchronization/composition authority (Phase 011)
        ↓
canonical direct dependence + capability rules
        ↓
whole-graph validation / subset semantics
        ↓
PF-01 product-family scope
        ↓
Phase-013 Mapping Entry Authority
        ↓
013-A mapping start gate

historical architecture / implementation / incumbent UI
        = evidence or contamination probe only
        ≠ Concept Design constraint
```

# Current Concept boundary

Phase 010 converged and exited with eighteen Concepts:

Competition, Division, Team, Panel, Evaluation Occurrence, Evaluation Obligation, Rubric, Scorecard, Award, Identity, Participation, Alias, Access, Versioning, Provenance, Outcome Declaration, Export, and Publication.

Phase 012 confirms no Phase-010 reopening is required.

# Current composition boundary

Phase 011 remains current authority for application actions and cross-Concept synchronization.

Phase 012 confirms no Phase-011 reopening is currently required for PF-01.

Phase 013 must map the established application action surface rather than exposing every intrinsic Concept action as a generic user control.

# Current product-family authority

[MUDAC Product-Family Scope](../dependence/product-family-scope.md) selects:

> **PF-01 — MUDAC Live Competition Judging & Official Outcome**

PF-01 keeps all eighteen Concepts in the supported capability envelope. This is product scope, not blanket direct dependence and not a requirement that every Competition exercise every Concept.

# Phase-012 exit result

```text
whole dependence graph: ACYCLIC
new direct edge required: NO
PF-01 scope change required: NO
Phase-010 reopen required: NO
Phase-011 reopen required: NO
Phase-012 repair required: NO
Phase-013 mapping revalidation required: YES
```

The mapping issue is currentness of older Experience material, not a semantic-model failure. Several earlier Experience records still use deprecated `Encounter` and `Official Outcome Revision` language.

[Phase 013 Mapping Entry Authority](../experience/phase-013-entry-handoff.md) establishes the current entry precedence:

```text
Purpose / Concepts / Synchronizations / Dependence / PF-01 scope
  = current conceptual authority

older Experience contracts
  = incoming mapping evidence pending revalidation
```

# Explanation-order boundary

Dependence can constrain what must be intelligible without becoming UI structure:

```text
dependence order != navigation order
synchronization chain != mandatory wizard
```

Mapping may reorganize experience, but it may not hide or falsify material context, authority, target, currentness, consequence or history.

# Reopening discipline during mapping

- purpose conflict → reopen current project-purpose owner;
- undefined Concept behavior/state/action → current Concept/specification owner;
- Concept boundary/independence defect → Phase 010;
- missing/invalid application action or synchronization → Phase 011;
- incorrect dependence/scope assumption → Phase 012;
- terminology/representation issue only → Phase 013.

Do not solve an upstream semantic defect with presentation behavior.

# Phase-013 implementation prohibition

Phase 013 may establish semantic representation obligations, state-query/view obligations, action mapping, terminology, required distinctions, feedback and accessibility/context-of-use semantics.

It must **not** select or prescribe:

- frontend framework/component library;
- route tree or exact screen hierarchy;
- CSS/design tokens;
- client-state/view-model architecture;
- API/endpoints/messages;
- websocket/polling/subscription/cache strategy;
- database/persistence realization;
- AWS/runtime topology;
- executable UI implementation/tests.

# Suspended downstream authority

Until successful Phase 017 closure, historical architecture/implementation conclusions remain downstream evidence only; 006-D remains frozen except narrow non-domain safety/build maintenance; Phase 008 remains halted.

`GitHub → GitHub Actions → AWS ecosystem` remains only a downstream delivery constraint.

# Meaning of future successful closure

A successful Phase 017 may establish readiness for a **separate architecture/engineering re-entry**. It does not start implementation or automatically reactivate prior plans.

# Current handoff

Proceed to:

> **013-A — Mapping Scope, Representation Semantics, Experience Risk & Subphase Planning**

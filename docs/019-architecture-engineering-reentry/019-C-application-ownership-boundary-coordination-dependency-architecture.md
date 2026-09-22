---
type: Architecture Decision
title: 019-C — Application Ownership, Boundary, Coordination & Dependency Architecture
description: "Resolves ADQ-002 after completing Q4R-001, compares ownership-preserving modular monolith, simpler monolith/package topology and selective distribution, and accepts a five-boundary modular monolith with explicit application coordination, non-authoritative projections and evidence-gated future extraction."
status: stable
tags: [phase-019, architecture, adq-002, boundaries, modular-monolith, ownership, coordination]
sources:
  - resource: ../canonical/architecture/application-ownership-boundaries.md
  - resource: ../canonical/architecture/architecture-drivers.md
  - resource: ../canonical/architecture/application-boundaries.md
  - resource: 019-C-Q4R-001-application-boundaries-semantic-repair.md
  - resource: ../canonical/dependence/application-family-dependence.md
  - resource: ../canonical/synchronizations/application-action-surface-composition.md
  - resource: ../canonical/synchronizations/evaluation-occurrence-obligation.md
  - resource: ../canonical/synchronizations/evaluation-outcome-finalization-declaration.md
  - resource: ../canonical/synchronizations/temporal-truth-correction.md
  - resource: ../canonical/governance/downstream-realization-obligations.md
  - resource: ../routing/phase019_architecture_decision_control.json
generated: { by: openai/gpt-5.6-sol, at: 2026-09-22T07:48:00-05:00 }
---

# Purpose

019-C resolves ADQ-002.

It first repairs the stale semantic bindings in the historical Application Boundaries candidate, then compares current topology alternatives against accepted DRV architecture drivers and current Concept/composition authority.

# 1. Entry state

~~~text
Phase 019                       ACTIVE
019-A / 019-B                   COMPLETE
019-C                           NEXT ELIGIBLE / USER AUTHORIZED

ADQ-001                         ACCEPTED
ADQ-002                         PLANNED
ADQ-003..010                    PLANNED

Q4R-001                         REQUIRED
Q4 repairs complete             0 / 4
technical probes                0

accepted whole architecture     false
implementation packages         0
implementation execution        false
~~~

# 2. Q4 prerequisite

019-C completed:

> **Q4R-001 — Historical Application-Boundary Semantic Repair**

The repair translates:

~~~text
Judging Encounter
  → Evaluation Occurrence
    + Evaluation Obligation

Official Outcome Revision
  → Outcome Declaration affected/successor authority
    + temporal correction composition
~~~

The historical file itself remains unchanged.

Q4R-001 makes the repaired historical hypothesis comparison-eligible.

It does not adopt it.

# 3. Current constraints

ADQ-002 must preserve:

- ENG-001 — semantics precede mechanism;
- ENG-004 — Identity/Participation/Access/authorship/technical privilege remain distinct;
- ENG-009 — outcome/officiality distinctions remain explicit;
- ENG-011 — security/disclosure protects semantic authority;
- ENG-017 — historical architecture remains evidence;
- INV-004 — Organizer/support does not become Judge author;
- INV-005 — current and historical truth remain distinct;
- INV-006 — calculated state is not official authority;
- DRV-001 — current semantic authority constrains architecture;
- DRV-002 — semantic/trust integrity outranks convenience;
- DRV-005 — workload is bounded/live-event shaped;
- DRV-007/008 — trust/disclosure boundaries are explicit;
- DRV-010 — operational complexity requires demonstrated benefit;
- DRV-011 — reversibility/lock-in are explicit dimensions.

# 4. Current ownership/coupling evidence

The current eighteen-Concept family does not imply eighteen runtime modules.

The strongest cohesive clusters are:

## Competition context

Competition, Division, Team and Alias share competition/competitor structural context.

## Identity and authority context

Identity, Participation and Access form the scoped actor/authority context while remaining semantically distinct.

## Evaluation

Panel, Evaluation Occurrence, Evaluation Obligation, Rubric and Scorecard have strong application-level coordination:

- Panel proposes evaluator grouping;
- occurrence begin records actual evaluators;
- obligations represent responsibility;
- Rubric supplies exact basis;
- Scorecard records/finalizes Judge judgment;
- Finalization satisfies responsibility;
- paper/electronic continuity must converge on one logical evaluation;
- invalidation/replacement may affect occurrence, responsibility and evidence eligibility.

This coordination pressure is materially higher than the benefit of separating historical Judging Operations and Evaluation modules.

## Outcomes and officiality

Award and Outcome Declaration are independent authorities but consume derived Coverage/Aggregate/Rank and closeout composition.

Competition Finalization remains Competition-owned and is coordinated with explicit Outcome Declaration.

## External representation

Export and Publication are intentionally downstream from source authority.

## Cross-cutting lineage

Versioning and Provenance are cross-cutting Concepts.

Their semantic meaning remains attached to each affected natural owner; shared technical primitives do not justify a central write-authority module.

# 5. Alternatives

## Alternative A — Historical six-module modular monolith after Q4 repair

Structure approximately:

- Competition Governance;
- Identity/Participation/Access;
- Judging Operations;
- Evaluation;
- Outcomes/Closeout;
- External Representation.

Strengths:

- explicit ownership;
- good downstream direction;
- prior architectural reasoning;
- service-extraction seams.

Weaknesses:

- preserves an artificial Judging Operations ↔ Evaluation seam;
- ordinary evaluation activity crosses that seam frequently;
- Scorecard Finalization/responsibility and paper/recovery coordination would carry avoidable transaction/orchestration pressure;
- historical grouping reflects older semantic boundaries.

**Rejected as exact topology.**

Its boundary principles remain useful.

## Alternative B — Simpler broad monolith/package topology

Use a single broad domain/application layer with internal namespaces or light folders and minimal hard module contracts.

Strengths:

- lowest initial structural overhead;
- straightforward in-process transactions;
- fewer public internal interfaces.

Weaknesses:

- weak protection against cross-owner mutation and derived-authority leakage;
- makes it easier for technical/admin access to bypass natural owners;
- encourages generic services/common-domain dumping grounds;
- makes later extraction more costly because ownership seams are implicit;
- conflicts with ERI-09 pressure and the mature Concept ownership model.

**Rejected.**

## Alternative C — Selectively distributed services now

Potential service boundaries could align to Identity, Evaluation, Outcomes, or Representation.

Strengths:

- stronger runtime isolation;
- independent scaling/deployment;
- potential failure containment.

Weaknesses:

- current workload does not demonstrate independent scaling need;
- network boundaries add uncertainty, retries, coordination and operational cost;
- cross-service consistency would complicate event-day high-consequence workflows;
- no team/deployment-cadence evidence requires independent services;
- premature provider/runtime coupling would reduce reversibility.

**Rejected for current architecture.**

Service extraction remains an evolution option.

## Alternative D — Five-boundary ownership-preserving modular monolith

Modules:

1. Competition Context;
2. Identity & Access;
3. Evaluation;
4. Outcomes & Officiality;
5. External Representation.

Plus:

- cross-cutting Versioning/Provenance semantics at natural owners;
- application coordination above modules;
- non-authoritative read projections;
- explicit public owner contracts;
- evidence-gated later extraction.

**Selected.**

# 6. Decision

**ADQ-002 — ACCEPTED.**

Current owner:

> docs/canonical/architecture/application-ownership-boundaries.md

Stable rules:

> BND-001 through BND-012

Selected topology:

> **Five-boundary ownership-preserving modular monolith: Competition Context; Identity & Access; Evaluation; Outcomes & Officiality; External Representation; with cross-cutting Versioning/Provenance semantics retained at natural owners, explicit application coordination, and non-authoritative cross-module projections.**

# 7. Why Evaluation is one module

Combining the historical Judging Operations and Evaluation modules does **not** merge Concepts.

It recognizes application-level cohesion.

The following remain separate semantic owners:

~~~text
Panel
Evaluation Occurrence
Evaluation Obligation
Rubric
Scorecard
~~~

But ordinary live judging repeatedly composes them.

Putting them in one module:

- lowers cross-module coordination frequency;
- avoids requiring distributed-style transaction semantics internally;
- improves paper/electronic reconciliation locality;
- reduces circular dependency pressure;
- preserves one module-level authority boundary for evaluation work.

# 8. Coordination architecture

Cross-module use cases coordinate above module owners.

The coordinator may sequence or compose calls, but it does not own business truth.

Examples:

- current Identity/Access + Competition context → Evaluation action;
- Evaluation evidence + Outcomes basis → closeout;
- Competition.finalize + OutcomeDeclaration.declare → official closeout;
- corrected source → owner-specific affected/recompute/successor actions;
- source authority → Export → Publication.

A generic Workflow/Task/Case/Result owner remains unavailable.

# 9. Dependency architecture

Accepted dependency tendency:

~~~text
Competition Context
        ↓
Identity & Access
        ↓
Evaluation
        ↓
Outcomes & Officiality
        ↓
External Representation
~~~

This is not mandatory direct-import chaining.

Stable references and application coordination may avoid direct module dependencies.

The architecture forbids:

- upstream dependency on Export/Publication;
- Evaluation depending on Awards/Outcome Declaration;
- direct cross-module repository/table/ORM access;
- using a read projection as command authority;
- circular write ownership.

# 10. Read/projection architecture

Cross-module operational reads may use denormalized projections.

Projection owners may optimize:

- Organizer live dashboards;
- remaining-work views;
- readiness/reconciliation summaries;
- search/reporting.

Projection state is not product-domain write authority.

High-consequence commands revalidate with current owners.

# 11. Versioning and Provenance

019-C explicitly rejects a central lineage god-module.

A shared lineage implementation may exist later, but:

~~~text
shared technical primitive
  != shared semantic write owner
~~~

Each module retains the semantic meaning of version, correction and provenance for the resources it owns.

# 12. Trust and authority effects

The module topology preserves:

- authentication proof distinct from Identity/Participation/Access;
- technical privilege distinct from semantic authority;
- Judge authorship distinct from Organizer capture/support;
- current evidence distinct from outcome derivation;
- calculated outcome distinct from explicit official declaration;
- source authority distinct from representation/release.

These seams align with DRV-007/008 trust boundaries.

# 13. Evidence

Acceptance evidence class:

> **DOCUMENTATION_REASONING**

No technical probe is needed.

The decision is about semantic ownership/decomposition, and current Concept/synchronization/dependence evidence is sufficient.

Technical enforcement and runtime behavior will require later evidence.

# 14. Reversibility and migration

This is a low-to-moderate lock-in architecture decision.

Positive reversibility:

- modules remain in one application;
- no network protocol is selected;
- no database-per-module requirement is selected;
- no framework/package layout is selected;
- public ownership contracts create future extraction seams.

Cost of later change:

- moving a Concept between modules requires architecture-governance evidence;
- extracting a module introduces network/failure/consistency contracts;
- collapsing modules later requires proving authority seams remain enforceable.

The frozen historical scaffold may require refactoring during Phase 020, but existing source topology does not constrain this decision.

# 15. Residual uncertainty

Accepted with bounded uncertainty:

- exact internal package/workspace layout;
- exact transaction boundaries for cross-module coordinated actions;
- exact command/query transport;
- whether any module later requires its own runtime process;
- exact read-projection implementation;
- persistence ownership/storage layout;
- authentication/session mechanism;
- deployment/provider topology.

Those questions belong to ADQ-003 through ADQ-009.

# 16. Revisit triggers

Reopen ADQ-002 if later evidence shows:

- a module needs materially independent scale/isolation/availability/runtime;
- ordinary workflows are dominated by expensive cross-module coordination;
- selected persistence/transaction mechanisms cannot preserve the boundary model;
- security requirements demand stronger runtime isolation;
- team/deployment ownership becomes independently governed;
- whole-architecture validation finds unacceptable coupling or failure propagation.

# 17. Scenario impact

This decision directly constrains:

- conflicting legitimate authority;
- partial bulk result;
- post-finalization correction.

It also establishes owner boundaries used by later retry, offline, access and externalization architecture.

# 18. Risk disposition

## ERI-02 — historical candidate mistaken for current architecture

**Controlled.**

Q4R-001 repaired the candidate before comparison; current authority is a new BND-* owner.

## ERI-04 — stale semantic bindings survive candidate reuse

**CLOSED for Application Boundaries.**

Judging Encounter and Official Outcome Revision no longer participate in the comparison.

## ERI-09 — cross-owner coupling / derived-authority leakage

**Materially reduced; carried to 019-K.**

Explicit modules, coordinator non-ownership, downstream dependency rules and projection non-authority now constrain later designs.

## ERI-03 — architecture emerges from existing implementation

**Controlled.**

Existing package/source topology was not used as the selected module map.

# 19. Implementation boundary

After 019-C:

~~~text
accepted bounded decisions       2 / 10
Q4 repairs complete              1 / 4
technical probes                 0

accepted whole architecture      false

active implementation packages   0
package derivation               false
implementation execution         false
~~~

No implementation package may be derived from BND-* yet.

# 20. Exit decision

**019-C — COMPLETE — PASS.**

**Q4R-001 — COMPLETE.**

**ADQ-002 — ACCEPTED.**

Next eligible:

> **019-D — Persistence, History, Provenance, Projection, Migration & Recovery Architecture**

019-D is not automatically authorized.

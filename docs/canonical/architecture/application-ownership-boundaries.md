---
type: Accepted Architecture Decision
title: Current Application Ownership, Boundary, Coordination & Dependency Architecture
description: "Accepted ADQ-002 application topology for MUDAC: a five-boundary ownership-preserving modular monolith, explicit cross-owner coordination, acyclic dependency posture, non-authoritative read projections, natural-owner Versioning/Provenance semantics, and evidence-gated future extraction."
status: stable
tags: [architecture, current, boundaries, modular-monolith, ownership, coordination, dependencies]
sources:
  - resource: architecture-drivers.md
  - resource: application-boundaries.md
  - resource: ../concepts/index.md
  - resource: ../synchronizations/application-action-surface-composition.md
  - resource: ../synchronizations/evaluation-occurrence-obligation.md
  - resource: ../synchronizations/evaluation-outcome-finalization-declaration.md
  - resource: ../synchronizations/temporal-truth-correction.md
  - resource: ../dependence/application-family-dependence.md
  - resource: ../governance/downstream-realization-obligations.md
  - resource: ../governance/architecture-decision-authority.md
  - resource: ../../019-architecture-engineering-reentry/019-C-Q4R-001-application-boundaries-semantic-repair.md
  - resource: ../../019-architecture-engineering-reentry/019-C-application-ownership-boundary-coordination-dependency-architecture.md
generated: { by: openai/gpt-5.6-sol, at: 2026-09-22T07:43:00-05:00 }
---

# Authority

This document is **current accepted architecture authority for ADQ-002**.

It establishes the application ownership/decomposition topology used by later Phase-019 decisions.

It does not select source-workspace names, framework packages, persistence technology, API transport, cloud services, or physical deployment details beyond the current modular-monolith posture.

<a id="bnd-001"></a>
## BND-001 — The initial authoritative application topology is an ownership-preserving modular monolith

MUDAC uses one authoritative application boundary divided into explicit semantic modules.

The initial topology is not distributed by default.

Independent network services require a demonstrated scale, isolation, availability, team-ownership, deployment-cadence, security or incompatible-runtime driver.

This decision is compatible with later runtime workers/adapters where 019-J justifies them; such runtime units do not automatically become semantic modules.

<a id="bnd-002"></a>
## BND-002 — Current authoritative ownership is grouped into five cohesive modules

The accepted module map is:

### Competition Context

Owns:

- Competition;
- Division;
- Team;
- Alias;
- Competition-owned structural/configuration facts that are not separate Concepts.

Competition lifecycle, including Finalization, remains here.

### Identity & Access

Owns:

- Identity;
- Participation;
- Access.

Authentication-provider proof is an adapter concern and does not own MUDAC Identity/Participation/Access semantics.

### Evaluation

Owns:

- Panel;
- Evaluation Occurrence;
- Evaluation Obligation;
- Rubric;
- Scorecard.

These Concepts remain semantically distinct.

They share one application module because current PF-01 composition creates high coordination pressure among evaluator grouping, actual occurrence history, responsibility, evaluation basis, Draft/final judgment, and paper/electronic continuity.

### Outcomes & Officiality

Owns:

- Award;
- Outcome Declaration;
- application realization of Coverage/Aggregate/Rank derived mechanisms and outcome-readiness composition.

It does not own Competition lifecycle.

Finalization plus declaration is a coordinated cross-module action.

### External Representation

Owns:

- Export;
- Publication.

It consumes identified source authority but cannot redefine that source.

<a id="bnd-003"></a>
## BND-003 — Versioning and Provenance are cross-cutting Concepts, not central god-modules

Versioning and Provenance remain product Concepts.

For architecture, the module owning the affected authoritative resource also owns the resource-specific meaning of version/correction/provenance transitions.

Shared technical primitives may standardize:

- durable IDs;
- revision envelopes;
- actor/represented-authority metadata;
- timestamps;
- provenance records;
- optimistic/concurrency metadata where later selected.

No central Versioning or Provenance module may acquire write authority over every domain owner merely because the implementation primitive is shared.

<a id="bnd-004"></a>
## BND-004 — Every authoritative fact and state-changing command has one primary module owner

A business fact or command has one natural module owner.

Other modules may:

- hold stable references;
- consume public read contracts;
- request an owner action through a public application contract;
- react to published facts/events where later architecture selects that mechanism.

They may not mutate another module's authoritative state directly.

<a id="bnd-005"></a>
## BND-005 — Cross-owner workflows coordinate above owners without becoming a new semantic owner

Application coordinators may compose multiple owner operations for actions such as:

- establish/begin evaluation work;
- participant/responsibility adjustment;
- Scorecard Finalization plus obligation satisfaction;
- occurrence invalidation/replacement consequences;
- Finalize Competition & Declare Outcome;
- post-finalization correction propagation;
- Export/Publication successor workflows.

The coordinator owns orchestration mechanics only.

It does not own a generic Workflow, Case, Task, Reconciliation, Result or Finalization Concept.

<a id="bnd-006"></a>
## BND-006 — Cross-module state access uses public contracts and stable identities, never another module's storage

A module must not establish authority by directly reading or writing another module's:

- repository implementation;
- database table/collection;
- ORM entity;
- internal service object;
- cache as if it were source truth.

Cross-module validation uses public owner contracts, supplied stable references, or explicit coordinated queries.

Exact API/function/event transport is deferred to ADQ-005.

<a id="bnd-007"></a>
## BND-007 — Dependency direction is acyclic and follows authority flow

The default dependency/consumption direction is:

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

This is an application architecture dependency tendency, not a claim that every module directly imports the one above it.

Cross-module references may remain opaque stable IDs and coordination may happen at the application layer.

The critical rules are:

- downstream outcome/representation concerns do not drive upstream evidence authority;
- Evaluation does not depend backward on Awards, Outcome Declaration, Export or Publication;
- Competition Context does not depend on later derived/output modules merely to simplify orchestration;
- cycles are rejected unless a later architecture decision documents why the apparent cycle is actually separated by contracts/events and does not create ownership ambiguity.

<a id="bnd-008"></a>
## BND-008 — Read projections may compose across modules but never become write authority

Operational dashboards, readiness views, search, reconciliation queues and reporting projections may combine information from several modules.

They may be optimized, denormalized, cached or stale where explicitly tolerated.

Consequential commands revalidate against current module owners.

A projection, cache or search index is never the sole authoritative basis for a high-consequence transition.

<a id="bnd-009"></a>
## BND-009 — Identity/Access enforcement remains explicit at protected owner boundaries

Identity & Access owns Identity, Participation and Access state.

Protected actions in another module remain owned by that module and require current application-side access/context validation.

Technical authentication, session possession, route possession or operator privilege does not grant semantic authority.

The exact authentication/session/authorization realization remains ADQ-004.

<a id="bnd-010"></a>
## BND-010 — External Representation is strictly downstream of source authority

Export and Publication may represent or release current/historical source state under current disclosure/release authority.

Upstream modules never depend on an Export artifact or Publication state to establish their own semantic truth.

Source correction does not silently retarget Export/Publication; successor representation/release remains explicit.

<a id="bnd-011"></a>
## BND-011 — Module extraction is allowed only through preserved contracts and demonstrated drivers

A current module may later become a separately deployable service only when evidence justifies:

- materially different scaling;
- security/isolation;
- failure containment;
- availability requirement;
- team ownership/deployment cadence;
- incompatible runtime/technology need.

Extraction must preserve stable identities, public contracts, authority ownership, historical semantics and failure/uncertainty behavior.

Network distribution does not justify semantic re-ownership.

<a id="bnd-012"></a>
## BND-012 — Source/package layout and provider/runtime deployment remain later decisions

ADQ-002 establishes semantic application boundaries.

It does not choose:

- exact workspace/package names;
- directory structure;
- internal framework;
- ORM/query tooling;
- API protocol;
- queue/event technology;
- AWS compute/network service;
- process count;
- worker topology;
- container/serverless packaging.

Those choices must conform to this boundary architecture when addressed later.

# Cross-module coordination examples

## Begin evaluation work

~~~text
Competition Context
  supplies current subject/competition context

Identity & Access
  supplies current evaluator Participation / Access context

Evaluation
  establishes current Evaluation Occurrence / Evaluation Obligations
~~~

Panel planning remains input evidence; it does not become actual occurrence truth merely by being configured.

## Finalize Scorecard

~~~text
Evaluation
  validates Scorecard / basis / Judge authority
  finalizes authoritative Scorecard
  satisfies corresponding Evaluation Obligation
~~~

Because Scorecard and Evaluation Obligation share one module, ordinary Finalization does not require a cross-service transaction merely to keep those tightly coordinated semantics consistent.

## Official closeout

~~~text
Evaluation
  supplies current eligible evidence

Outcomes & Officiality
  supplies Coverage / Aggregate / Rank / Award / OutcomeBasis state

Application coordinator
  → Competition Context: Competition.finalize
  → Outcomes & Officiality: OutcomeDeclaration.declare
~~~

The coordinator does not become owner of Finalization or official outcome authority.

## External release

~~~text
identified source authority
  → External Representation.Export
  → explicit Publication action
~~~

External Representation cannot mutate the source merely because a representation is stale.

# Rationale for combining historical Judging Operations and Evaluation modules

The historical six-module candidate separated:

- Judging Operations; and
- Evaluation.

Current semantic convergence shows the seam is highly coupled:

- occurrence begin establishes obligations;
- participant changes require explicit responsibility disposition;
- Scorecard Finalization satisfies responsibility;
- paper/electronic continuity must converge on one logical evaluation;
- invalidation/replacement can affect occurrence, responsibility and evidence eligibility together.

Keeping those Concepts in one Evaluation module reduces cross-module transaction/coordination pressure while preserving their Concept boundaries.

This is an architecture grouping decision, not a Concept merge.

# Dependency and coupling posture

The architecture prefers:

- semantic cohesion inside modules;
- explicit owner contracts between modules;
- application coordination for cross-owner actions;
- downstream-only consumption where practical;
- non-authoritative projections for cross-cutting reads;
- no generic shared business-service layer.

A future source/package design should make violations mechanically difficult where proportionate, but implementation enforcement belongs to Phase 020.

# Revisit triggers

Reopen ADQ-002 when credible evidence shows:

- one module requires materially independent scale/isolation/availability/runtime;
- repeated cross-module coordination dominates ordinary transactions;
- a selected persistence/identity/runtime mechanism creates an unavoidable ownership contradiction;
- team/deployment ownership becomes materially independent;
- a module cannot preserve its current authority without cyclic write dependencies;
- whole-architecture validation exposes unacceptable coupling or failure propagation.

# ADQ-002 accepted decision

Selected topology:

> **Five-boundary ownership-preserving modular monolith: Competition Context; Identity & Access; Evaluation; Outcomes & Officiality; External Representation; with cross-cutting Versioning/Provenance semantics retained at natural owners, explicit application coordination, and non-authoritative cross-module projections.**

Whole-architecture acceptance remains false until 019-L.

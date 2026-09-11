---
type: Canonical Project Context
title: MUDAC Project Mandate & Current Context
description: "Current representation-independent project/intake baseline for MUDAC: contemplated capability, actors and affected parties, outcome directions, scope, constraints, assumptions, open questions and evidence posture."
status: stable
tags: [canonical, project, context, mandate, actors, scope, constraints, evidence]
sources:
  - resource: ../../010-project-purpose-candidate-specification-modularity/010-B-current-project-mandate-actors-outcomes-scope-constraints-evidence-reconciliation.md
  - resource: ../../010-project-purpose-candidate-specification-modularity/010-C-purpose-need-success-tension-purpose-to-concept-traceability-revalidation.md
  - resource: ../../010-project-purpose-candidate-specification-modularity/010-D-candidate-concept-rediscovery-divergent-alternatives-rejected-deferred-candidate-reassessment.md
  - resource: ../../010-project-purpose-candidate-specification-modularity/010-F-specificity-purpose-singularity-concept-boundary-alternative-audit.md
  - resource: ../../010-project-purpose-candidate-specification-modularity/010-G-completeness-independence-genericity-for-boundary-audit.md
---

# Purpose

Provide one concise current owner for MUDAC's project definition before final Concept selection.

This document answers **what project is being designed and under what conditions**. [Purpose, Needs, Success & Tensions](purpose-needs-success-tensions.md) answers why the product matters. Neither document protects the current Concept catalog.

# Current mandate

MUDAC is a design-governed software effort supporting the **operational judging and outcome lifecycle of a live student data competition**.

The baseline capability should help volunteer Judges and competition Organizers conduct, preserve, reconcile and explain independent evaluation under real event-day constraints, while controlling bias-sensitive identity disclosure and preserving trustworthy historical evidence.

Current capability spans preparation, live evaluation, paper/electronic continuity, correction, outcome formation and controlled external representation.

# Stable competition context

Current evidence supports these facts:

- student Teams present work for evaluation;
- volunteer Judges form individual judgments from multiple perspectives;
- Organizers prepare and operate the live competition and establish official outcomes;
- institutional identity may bias judging and therefore requires controlled disclosure;
- live judging is time-bounded and operationally dynamic;
- first-time users, phones, interruptions, poor connectivity, accessibility needs and paper operation are realistic conditions;
- corrections must preserve meaningful history rather than silently rewriting authoritative evidence;
- competition outcomes must remain explainable from evaluation evidence and declared rules;
- stable printable or deliberately released representations may be needed operationally or after closeout.

# Actors and affected parties

## Direct product actors

- **Judge** — volunteer human evaluator needing low-friction, accessible, independent/private judgment participation.
- **Organizer** — human responsible for preparation, live operation, exception handling, reconciliation and official closeout.
- **Technical administrator/support operator** — operates/supports the technical environment; technical power does not automatically confer competition decision authority.

## Materially affected non-actors

- **Student Team** — competitor whose outcome depends on fair, sufficiently supported, bias-aware evaluation. Student-facing application use is outside the baseline.
- **External recipient** — consumer of print/external representations who needs honest source/authority/disclosure meaning; not evidence for a rich public-results portal.

No separate sponsor, faculty-advisor, institutional-representative or event-leadership software role is currently established by evidence.

# Current capability boundary

## In scope

At capability level, MUDAC includes:

- competition judging-context/policy setup;
- competitor establishment and competition-facing identity handling;
- volunteer evaluator preparation and event participation;
- evaluator grouping/coordination for live judging;
- declaration of evaluation criteria/basis;
- independent judgment and qualitative evidence capture;
- preservation of incomplete/draft work distinct from authoritative evaluation;
- paper/electronic evaluation continuity;
- Organizer visibility into completion, gaps and exceptions;
- provenance-preserving correction and historical evidence;
- derived/reconciled competition evaluation, coverage and ordering;
- organizer-defined recognition/Awards;
- official outcome closeout;
- stable printable/external representations tied to identified source state;
- deliberate release/withdrawal of external representations where disclosure rules permit.

These are capability areas, not assignments to particular Concepts.

## Out of current baseline

- student registration/accounts/dashboard;
- student submission management;
- dataset hosting/distribution;
- notebook/analytics/ML execution infrastructure;
- faculty-advisor management;
- general ticketing/marketing;
- prize payment/disbursement;
- general-purpose competition management outside judging/outcomes;
- advanced Judge normalization/calibration as a default core function;
- formal room/time-slot scheduling optimization;
- notification systems as required core functionality;
- rich public-results portal beyond controlled representation/release.

Formal Stage/Round abstractions and other format extensions remain possible later scope; Phase 012 owns product-family/subset analysis.

# Product and operational constraints

The current design must respect these representation-independent constraints:

- **Live event:** delays, substitutions, incomplete work and rapid exception handling matter.
- **Independent judgment:** ordinary Judge evaluation must not depend on peer scores/notes or live standings.
- **Bias-sensitive disclosure:** administrative/institutional Team identity must be controllable in judging contexts.
- **Accessibility:** the product cannot assume perfect vision, color perception, fine motor control, hearing, one device or touch-only interaction.
- **Degraded connectivity/devices:** interruption, poor connectivity and device problems are expected conditions.
- **Paper continuity:** paper must be a valid continuity/accommodation path with compatible evaluation meaning.
- **Historical truth:** correction must not require destructive rewriting of meaningful authoritative history.
- **Explainability:** competition outcomes must be reconstructible from underlying evaluation evidence and declared rules.
- **Authority separation:** technical system privilege must not silently become authority to author or revise competition judgment.

# Downstream-only delivery constraint

Historical project intent targets:

```text
GitHub → GitHub Actions → AWS ecosystem
```

This is only a **downstream delivery constraint**. It does not determine Concepts, state/actions, UI mapping, persistence, authentication, APIs, service topology or specific AWS services.

The existing Node/TypeScript/Fastify/React/PostgreSQL/OpenTofu bootstrap is a frozen historical executable fact, not project-intake authority.

# Working assumptions

Current but challengeable assumptions:

- Judge and Organizer are the principal direct product-user modes, plus narrow technical operation/support;
- Student Teams remain non-user participants in the baseline;
- competitive grouping is configurable rather than fixed to one exact taxonomy;
- judging commonly seeks multiple evaluator perspectives, while exact expertise categories/quotas are policy choices;
- controlled external release remains in the present capability boundary, while a rich public portal does not;
- formal scheduling may remain external/lightweight unless later purpose/dependence work shows it necessary.

# Open questions after 010-G

Foundational modularity analysis is now complete at phase level. All eighteen post-specificity candidates survived completeness, intrinsic-independence and boundary-genericity testing.

Current project context intentionally leaves open:

- whether 010-H can canonically converge/re-specify all validated boundaries without exposing a hidden upstream defect;
- exact synchronization triggers/preconditions/postconditions among the converged Concepts, owned by Phase 011;
- which Concepts are intrinsically independent yet extrinsically required together in coherent application variants, owned by Phase 012;
- whether Division, Panel, Award, Publication or other capabilities are optional in specific product-family members;
- detailed evaluation, coverage, ranking, tie, Award and disclosure policies;
- exact retention/regulatory requirements not currently evidenced;
- mapping/interaction refinements, familiarity/reuse refinement, integrity/adversarial closure, architecture and implementation realization.

010-G found no project-context defect and no nineteenth Concept. Evaluation Sufficiency/Coverage remains derived; Reconciliation remains process/work mode; Recovery/Continuity remains a cross-cutting obligation rather than a Concept.

# Evidence posture

Use historical Phase 001–003/007 material as evidence and rationale, not immutable truth.

Architecture and implementation produced before methodology completion are quarantined from constraining this project definition. When later design evidence changes the mandate, update this document as the natural current owner and preserve older conclusions in phase history.

# Current handoff

Phase 010-B reconciled project/intake truth, 010-C established the purpose model, 010-D rediscovered candidates, 010-E established behavioral specifications, 010-F established the post-specificity boundary set, and 010-G validated completeness/independence/boundary-genericity for all eighteen candidates. The next methodology task is:

> **010-H — Concept Boundary Convergence, Re-specification & Canonical Reconciliation**

010-H must make the validated boundary decisions current and unambiguous without solving Phase 011 synchronization or Phase 012 product-family dependence prematurely.
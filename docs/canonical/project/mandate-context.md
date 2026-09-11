---
type: Canonical Project Context
title: MUDAC Project Mandate & Current Context
description: Current representation-independent project/intake baseline for MUDAC: contemplated capability, actors and affected parties, outcome directions, scope, constraints, assumptions, open questions and evidence posture.
status: stable
tags: [canonical, project, context, mandate, actors, scope, constraints, evidence]
sources:
  - resource: ../../010-project-purpose-candidate-specification-modularity/010-B-current-project-mandate-actors-outcomes-scope-constraints-evidence-reconciliation.md
---

# Purpose

Provide one concise current owner for MUDAC's project definition before purpose decomposition and Concept selection.

This document answers **what project is being designed and under what conditions**. It does not define the final Jackson purpose model or protect the current Concept catalog.

# Current mandate

MUDAC is a design-governed software effort supporting the **operational judging and outcome lifecycle of a live student data competition**.

The baseline capability should help volunteer Judges and competition Organizers conduct, preserve, reconcile and explain independent evaluation under real event-day constraints, while controlling bias-sensitive identity disclosure and preserving trustworthy historical evidence.

Current capability spans preparation, live evaluation, paper/electronic continuity, correction, outcome formation and controlled external representation.

The present sixteen-Concept catalog is an incumbent design hypothesis. This project mandate does not require those exact Concept identities or boundaries.

# Stable competition context

Current evidence supports these context facts:

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

- **Judge** — volunteer human evaluator. Needs low-friction participation and independent/private judgment capture.
- **Organizer** — human responsible for preparation, live operation, exception handling, reconciliation and official closeout.
- **Technical administrator/support operator** — operates or supports the technical environment; technical power does not automatically confer competition decision authority.

## Materially affected non-actors

- **Student Team** — competitor whose outcome depends on fair, sufficiently covered, bias-aware evaluation. Student-facing application use is outside the current baseline.
- **External recipients of released material** — consumers of print/external representations; not currently direct application actors and not evidence for a rich public-results portal.

The repository does not currently establish sponsor, faculty-advisor, institutional-representative or event-leadership roles as separate application actors. Later purpose analysis may identify distinct affected-party needs without inventing software roles prematurely.

# Outcome directions for Phase 010-C

These are current desired directions, not the final purpose decomposition:

- Judges can record independent judgment without excessive administrative friction;
- Organizers can coordinate the event and understand incomplete/exceptional conditions;
- official outcomes are traceable to evaluation evidence and governing rules;
- bias-sensitive Team identity is not revealed to Judges merely for convenience;
- missing evaluation remains distinguishable from a deliberate low score;
- paper and electronic judging preserve compatible evaluation meaning;
- interruption and degraded connectivity do not unnecessarily destroy valid work;
- corrections preserve authorship, provenance and historical truth;
- provisional/live information is distinguishable from official information;
- external representations do not silently promote unauthorized or provisional information into official truth.

Phase 010-C owns the need-focused, evaluable purpose model and tensions among these outcomes.

# Current capability boundary

## In scope

At capability level, MUDAC currently includes:

- competition judging-context/policy setup;
- competitor establishment and competition-facing identity handling;
- volunteer evaluator preparation and event participation;
- evaluator grouping/coordination for live judging;
- declaration of evaluation criteria/basis;
- independent judgment and qualitative evidence capture;
- preservation of incomplete/draft work distinct from authoritative evaluation;
- paper and electronic evaluation continuity;
- Organizer visibility into completion, gaps and exceptions;
- provenance-preserving correction and historical evidence;
- derived/reconciled competition evaluation, coverage and ordering;
- organizer-defined recognition/awards;
- official outcome closeout;
- stable printable/external representations tied to identified source state;
- deliberate release/withdrawal of external representations where disclosure rules permit.

These are capability areas, not assignments to current Concepts.

## Out of current baseline

- student registration/accounts/dashboard;
- student submission management;
- dataset hosting/distribution;
- notebook, analytics or ML execution infrastructure;
- faculty-advisor management;
- general ticketing/marketing;
- prize payment/disbursement;
- general-purpose competition management outside judging/outcomes;
- advanced Judge normalization/calibration as a default core function;
- formal room/time-slot scheduling optimization;
- notification systems as required core functionality;
- rich public-results portal beyond controlled representation/release.

Formal Stage/Round abstractions and other format extensions remain possible later scope; Phase 012 owns application-family/subset analysis.

# Pre-Concept vocabulary

The project can use these terms descriptively without treating them as protected Concepts:

- **Team** — student competitor/group;
- **Judge** — human evaluator;
- **Organizer** — competition operator/governor;
- **Panel** — ordinary competition term for Judges evaluating together;
- **Rubric** — declared evaluation criteria/basis;
- **Scorecard** — ordinary repository term for one Judge's recorded evaluation;
- **Division** — organizer-defined competitive grouping where used.

`Judging Encounter` remains useful shorthand for a bounded evaluator/Team judging occurrence, but whether it should remain a distinct Concept is explicitly open to Phase 010-D–G.

Other incumbent Concept names are not prerequisites of the project definition.

# Product and operational constraints

The current design must respect these representation-independent constraints:

- **Live event:** delays, substitutions, incomplete work and rapid exception handling matter.
- **Independent judgment:** ordinary Judge evaluation must not depend on peer scores/notes or live standings.
- **Bias-sensitive disclosure:** administrative/institutional Team identity must be controllable in judging contexts.
- **Accessibility:** the product cannot assume perfect vision, color perception, fine motor control, hearing, a single device or touch-only operation.
- **Degraded connectivity/devices:** interruption, poor connectivity and device problems are expected conditions.
- **Paper continuity:** paper must be a valid continuity/accommodation path with compatible evaluation meaning.
- **Historical truth:** correction must not require destructive rewriting of meaningful authoritative history.
- **Explainability:** competition outcomes must be reconstructible from underlying evaluation evidence and declared rules.
- **Authority separation:** technical system privilege must not silently become authority to author or revise competition judgment.

# Downstream-only delivery constraint

Historical project intent targets an eventual delivery chain of:

```text
GitHub → GitHub Actions → AWS ecosystem
```

This is retained only as a **downstream delivery constraint**. It does not determine Concepts, Concept boundaries, state/actions, UI mapping, persistence, authentication, APIs, service topology or specific AWS services.

The existing Node/TypeScript/Fastify/React/PostgreSQL/OpenTofu bootstrap is a frozen historical executable fact, not project-intake authority.

# Working assumptions

Current but challengeable assumptions:

- Judge and Organizer are the principal direct product-user modes, plus narrow technical operation/support;
- Student Teams remain non-user participants in the baseline;
- competitive grouping is configurable rather than fixed to one exact taxonomy;
- judging commonly seeks multiple evaluator perspectives, while exact expertise categories/quotas are policy choices;
- controlled external release remains in the present capability boundary, while a rich public portal does not;
- formal scheduling may remain external/lightweight unless later purpose/dependence work shows it is necessary.

# Open questions

Current project context intentionally leaves these open:

- final purpose/need/success decomposition and stakeholder tensions;
- whether additional affected parties have distinct software-relevant needs;
- which capability areas belong in every coherent MUDAC variant;
- which incumbent Concepts survive rediscovery and modularity review;
- detailed evaluation, coverage, ranking, tie, Award and disclosure policies;
- exact retention/regulatory requirements not currently evidenced;
- final mappings, architecture and implementation realization.

# Evidence posture

Use historical Phase 001–003/007 material as evidence and rationale, not immutable truth.

Architecture and implementation produced before methodology completion are quarantined from constraining this project definition. When later design evidence changes the mandate, update this document as the natural current owner and preserve the older conclusion in phase history.

# Current handoff

Phase 010-B has reconciled project/intake truth. The next methodology task is:

> **010-C — Purpose, Need, Success, Tension & Purpose-to-Concept Traceability Revalidation**

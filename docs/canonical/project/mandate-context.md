---
type: Canonical Project Context
title: MUDAC Project Mandate & Current Context
description: "Current representation-independent project/intake baseline for MUDAC: mandate, actors, scope, constraints, assumptions, converged Concept context, and bounded closure/downstream questions."
status: stable
tags: [canonical, project, context, mandate, actors, scope, constraints]
sources:
  - resource: ../../010-project-purpose-candidate-specification-modularity/010-B-current-project-mandate-actors-outcomes-scope-constraints-evidence-reconciliation.md
  - resource: ../../010-project-purpose-candidate-specification-modularity/010-C-purpose-need-success-tension-purpose-to-concept-traceability-revalidation.md
  - resource: ../../010-project-purpose-candidate-specification-modularity/010-H-concept-boundary-convergence-respecification-canonical-reconciliation.md
  - resource: purpose-needs-success-tensions.md
generated: { by: openai/gpt-5.6-sol, at: 2026-09-12T03:12:00Z }
---

# Purpose

Provide the current representation-independent project definition for MUDAC.

This document answers **what project is being designed and under what conditions**. [Purpose, Needs, Success & Tensions](purpose-needs-success-tensions.md) answers why the product matters. The [Concept catalog](../concepts/) now owns the converged current behavioral units.

# Current mandate

MUDAC is a design-governed software effort supporting the **operational judging and outcome lifecycle of a live student data competition**.

The baseline capability helps volunteer Judges and competition Organizers conduct, preserve, coordinate and explain independent evaluation under real event-day constraints while controlling bias-sensitive identity disclosure and preserving trustworthy historical evidence.

Current capability spans preparation, live evaluation, paper/electronic continuity, correction, outcome formation, explicit outcome declaration, and controlled external representation/release.

# Stable competition context

- Student Teams present work for evaluation.
- Volunteer Judges form individual judgments from multiple perspectives.
- Organizers prepare and operate the live competition and establish official outcomes.
- Institutional identity may bias judging and therefore requires controlled disclosure.
- Live judging is time-bounded and operationally dynamic.
- First-time users, phones, interruptions, poor connectivity, accessibility needs and paper operation are realistic conditions.
- Corrections must preserve meaningful history rather than silently rewriting authoritative evidence.
- Outcomes must remain explainable from evaluation evidence and declared rules.
- Stable printable/external representations may be needed operationally or after closeout.

# Actors and affected parties

## Direct product actors

- **Judge** — volunteer evaluator needing low-friction, accessible, independent/private judgment participation.
- **Organizer** — human responsible for preparation, live operation, exception handling, reconciliation and official closeout.
- **Technical administrator/support operator** — operates/supports the technical environment; technical power does not automatically confer competition decision authority.

## Materially affected non-actors

- **Student Team** — competitor whose outcome depends on fair, sufficiently supported, bias-aware evaluation; student-facing application use is outside the baseline.
- **External recipient** — consumer of print/external representations who needs honest source/authority/disclosure meaning.

No separate sponsor, faculty-advisor, institutional-representative or event-leadership software role is currently established by evidence.

# Current capability boundary

## In scope

- competition judging-context/policy setup;
- competitor establishment and competition-facing identity handling;
- evaluator preparation and event participation;
- reusable evaluator grouping and live evaluation occurrences;
- evaluator responsibility/remaining-work tracking without inventing judgment;
- evaluation criteria/basis;
- independent judgment and qualitative evidence capture;
- Draft versus authoritative judgment;
- paper/electronic continuity;
- Organizer visibility into completion, gaps and exceptions;
- provenance-preserving correction and historical evidence;
- derived Coverage/Aggregate/Rank;
- organizer-defined recognition/Awards;
- explicit outcome declaration and successor authority after correction;
- stable source-bound external representations;
- deliberate release/withdrawal/supersession of representations.

These are capability areas, not instructions that every product variant must contain every current Concept. Phase 012 owns product-family/subset analysis.

## Out of current baseline

- student registration/accounts/dashboard;
- student submission management;
- dataset hosting/distribution;
- notebook/analytics/ML execution infrastructure;
- faculty-advisor management;
- general ticketing/marketing;
- prize payment/disbursement;
- general-purpose competition management outside judging/outcomes;
- advanced Judge normalization/calibration as default core behavior;
- formal room/time-slot scheduling optimization;
- notification systems as required core functionality;
- rich public-results portal beyond controlled representation/release.

Formal Stage/Round abstractions and other competition-format extensions remain possible later scope questions.

# Product and operational constraints

- **Live event:** delays, substitutions, incomplete work and rapid exception handling matter.
- **Independent judgment:** ordinary Judge evaluation must not depend on peer scores/notes or live standings.
- **Bias-sensitive disclosure:** administrative/institutional Team identity must be controllable in judging contexts.
- **Accessibility:** the product cannot assume perfect vision, color perception, fine motor control, hearing, one device or touch-only interaction.
- **Degraded connectivity/devices:** interruption, poor connectivity and device problems are expected.
- **Paper continuity:** paper must be a valid continuity/accommodation path with compatible evaluation meaning.
- **Historical truth:** correction must not require destructive rewriting of meaningful authoritative history.
- **Explainability:** outcomes must be reconstructible from underlying evidence, policy and declared authority.
- **Authority separation:** technical privilege must not silently become Judge/Organizer semantic authority.

# Current canonical Concept context after 010-H

Phase 010 modularity convergence establishes eighteen current Concepts:

Competition, Division, Team, Panel, Evaluation Occurrence, Evaluation Obligation, Rubric, Scorecard, Award, Identity, Participation, Alias, Access, Versioning, Provenance, Outcome Declaration, Export, and Publication.

This catalog is current knowledge, but later methodology phases may still reopen a natural owner if new evidence exposes a defect.

# Downstream-only delivery constraint

Historical project intent targets:

```text
GitHub → GitHub Actions → AWS ecosystem
```

This remains only a downstream delivery constraint. It does not determine Concept state/actions, synchronization, mapping, persistence, authentication, APIs, service topology, or specific AWS services.

The existing Node/TypeScript/Fastify/React/PostgreSQL/OpenTofu bootstrap remains a frozen historical executable fact.

# Working assumptions

- Judge and Organizer are the principal direct product-user modes, plus narrow technical operation/support.
- Student Teams remain non-user participants in the baseline.
- Competitive grouping is configurable rather than fixed to one taxonomy.
- Judging commonly seeks multiple evaluator perspectives; exact expertise categories/quotas are policy choices.
- Controlled external release remains in the capability boundary; a rich public portal does not.
- Formal scheduling may remain external/lightweight unless later scope/dependence work proves it necessary.

# Current closure-bounded items

Concept modularity, synchronization, dependence/PF-01 scope, mapping, familiarity/genericity, whole-system integrity and mature scenario validation are complete through Phase 016.

The remaining non-closed-design subjects are explicitly classified:

- **Methodology closure** — Phase 017 is current process work, not an unresolved product-semantic question.
- **Competition-configurable policy values** — detailed evaluation thresholds, ranking/tie choices, Award rules and disclosure selections are intentional Competition policy/configuration variation within the current policy model; they are not missing Concept Design defaults unless a future product requirement demands fixed defaults.
- **Retention/regulatory detail** — exact retention periods, jurisdiction-specific legal obligations and compliance procedures are not established by current evidence. This is a bounded evidence limitation, not permission to discard history/privacy semantics. Before production in a concrete jurisdiction, downstream product/legal/architecture work must reconcile those obligations against current Provenance, historical-truth, confidentiality and release requirements.
- **Downstream realization** — representation, architecture, security, persistence, authentication, concurrency, offline behavior and delivery mechanisms remain downstream implementation/architecture work after successful Concept Design closure and explicit re-entry.

Current scope also deliberately excludes a rich public portal and treats formal scheduling as external/lightweight unless future scope evidence reopens dependence.

None of these items is an open semantic blocker for the current PF-01 Concept Design.

# Current handoff

The current eighteen-Concept baseline has survived Phases 011–016 without a Concept reopen.

Proceed to:

> **017-B — Canonical Current-Truth, Supersession, Contradiction & Knowledge-Graph Reconciliation**

---
type: Design Concept
title: Scorecard
description: One evaluator's independent judgment over a supplied subject, occurrence context, and evaluation basis.
status: stable
tags: [concept, judging, evidence, scorecard]
sources:
  - resource: ../../002-concept-specification/002-D-rubric-criterion-scorecard-notes-specifications.md
  - resource: ../../002-concept-specification/002-E-versioning-provenance-correction-authority-preservation.md
  - resource: ../../010-project-purpose-candidate-specification-modularity/010-G-completeness-independence-genericity-for-boundary-audit.md
  - resource: ../../010-project-purpose-candidate-specification-modularity/010-H-concept-boundary-convergence-respecification-canonical-reconciliation.md
  - resource: ../../011-concept-composition-synchronization/011-E-evaluation-basis-scorecard-authority-versioning-provenance-paper-capture-composition.md
  - resource: ../../011-concept-composition-synchronization/011-F-temporal-correction-invalidation-replacement-successor-work-affected-state-propagation.md
generated: { by: openai/gpt-5.6-sol, at: 2026-09-14T13:36:00-05:00 }
---

# Purpose

Capture one evaluator's independent judgment for a supplied Subject under a supplied OccurrenceContext and exact EvaluationBasis, preserving Draft versus authoritative judgment and legitimate successor-authority correction history.

# Abstract parameters

Conceptually:

`Scorecard<Evaluator, Subject, OccurrenceContext, EvaluationBasis>`

Scorecard stores the semantic identities/basis it judged under; it does not require peer Concept internals.

# State

Scorecard owns:

- one stable logical identity;
- Evaluator / semantic author;
- Subject;
- OccurrenceContext reference/snapshot sufficient to identify the judging context;
- fixed EvaluationBasis;
- working criterion responses and Notes;
- non-authoritative Draft state;
- current authoritative response state when one exists;
- successor/amendment Draft state when one exists;
- semantic amendment and source-faithful successor-correction history as coordinated by the application.

`Not Started` is responsibility state outside Scorecard, not a Scorecard lifecycle state.

# Actions and queries

Conceptual actions are `start`, `setCriterionScore`, `clearCriterionScore`, `setCriterionNote`, `clearCriterionNote`, `setOverallNote`, `clearOverallNote`, `finalize`, `beginAmendment`, `abandonAmendment`, and `finalizeAmendment`.

Queries include Draft/current-authoritative responses, basis/context identity, completion status under supplied EvaluationBasis validation, and successor/amendment history.

# Operational Principle

An evaluator starts one logical judgment for a Subject under a fixed OccurrenceContext and EvaluationBasis, works incrementally in a non-authoritative Draft, and explicitly Finalizes a valid completed evaluation.

A later legitimate successor correction begins from current authoritative Scorecard state while the predecessor remains current until successor finalization. In ordinary semantic amendment, the evaluator changes their own judgment. MUDAC application composition may also use the same successor-state mechanics for a source-faithful capture/transcription correction where the semantic Judge content is unchanged and the acting correction actor differs from the represented Judge authority. Provenance/policy distinguish those correction classes; Scorecard does not transfer authorship.

<a id="sc-001"></a>
## SC-001 — Draft is non-authoritative

Completeness of working responses does not itself establish authority. Explicit successful Finalization is required.

<a id="sc-002"></a>
## SC-002 — Amendment/successor work preserves prior authority until successor establishment

Beginning successor correction work never displaces the prior authoritative judgment. The predecessor remains current until the successor is explicitly finalized through application composition with authoritative-history owners.

<a id="sc-003"></a>
## SC-003 — Structural identity is not ordinary successor-correction content

Ordinary semantic amendment or source-faithful capture correction may change response/note representation while preserving the same underlying logical evaluation, but cannot silently change Evaluator, Subject, OccurrenceContext, or EvaluationBasis. Structural errors use explicit invalidation/replacement paths.

# MUDAC composition binding

MUDAC normally binds Evaluator to Judge Participation identity, Subject to Team, OccurrenceContext to Evaluation Occurrence, and EvaluationBasis to an exact authoritative Rubric Version. Rubric supplies response validity semantics.

[Evaluation Basis, Scorecard Authority & Capture Composition](../synchronizations/evaluation-basis-scorecard-authority.md) establishes initial Finalization, Versioning/Provenance participation and Evaluation Obligation satisfaction.

[Temporal Truth, Correction & Historical Authority](../synchronizations/temporal-truth-correction.md) establishes how the same logical Scorecard handles source-faithful post-authority capture correction, when current evidence must instead be invalidated, and why structural identity errors never rebind the logical Scorecard silently.

Versioning and Provenance remain external composition owners. Scorecard successor-state mechanics do not by themselves classify a change as Judge amendment versus capture correction; correction authority, actor/represented-authority distinction and source explanation belong to application policy/Provenance.

# Boundaries

Scorecard does not decide who is responsible to evaluate, who participated in an occurrence, who has Access, whether an occurrence/basis remains eligible, how authoritative snapshots/provenance are coordinated, whether new responsibility is required after evidence invalidation, or how multiple judgments are aggregated/ranked.

Paper/electronic capture shares this same judgment Concept; capture channel belongs to explanatory Provenance rather than changing evaluator authorship.

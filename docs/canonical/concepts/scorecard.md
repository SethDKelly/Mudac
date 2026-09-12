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
generated: { by: openai/gpt-5.6-sol, at: 2026-09-12T03:12:00Z }
---

# Purpose

Capture one evaluator's independent judgment for a supplied Subject under a supplied OccurrenceContext and exact EvaluationBasis, preserving Draft versus authoritative judgment and legitimate amendment history.

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
- amendment Draft state when one exists;
- semantic amendment history.

`Not Started` is responsibility state outside Scorecard, not a Scorecard lifecycle state.

# Actions and queries

Conceptual actions are `start`, `setCriterionScore`, `clearCriterionScore`, `setCriterionNote`, `clearCriterionNote`, `setOverallNote`, `clearOverallNote`, `finalize`, `beginAmendment`, `abandonAmendment`, and `finalizeAmendment`.

Queries include Draft/current-authoritative responses, basis/context identity, completion status under supplied EvaluationBasis validation, and amendment history.

# Operational Principle

An evaluator starts one logical judgment for a Subject under a fixed OccurrenceContext and EvaluationBasis, works incrementally in a non-authoritative Draft, and explicitly Finalizes a valid completed evaluation. A later legitimate author correction begins an Amendment Draft while the prior authoritative judgment remains current; successful amendment finalization establishes a successor authoritative judgment without creating an additional evaluator vote.

<a id="sc-001"></a>
## SC-001 — Draft is non-authoritative

Completeness of working responses does not itself establish authority. Explicit successful Finalization is required.

<a id="sc-002"></a>
## SC-002 — Amendment preserves prior authority until successor establishment

Beginning an Amendment never displaces the prior authoritative judgment. The predecessor remains current until the successor is explicitly finalized through application composition with authoritative-history owners.

<a id="sc-003"></a>
## SC-003 — Structural identity is not ordinary amendment content

Ordinary amendment may change evaluator-authored response/note content but cannot silently change Evaluator, Subject, OccurrenceContext, or EvaluationBasis. Structural errors use explicit correction/invalidation/replacement paths.

# MUDAC composition binding

MUDAC normally binds Evaluator to Judge Participation identity, Subject to Team, OccurrenceContext to Evaluation Occurrence, and EvaluationBasis to an exact authoritative Rubric basis. Rubric supplies response validity semantics. Versioning and Provenance may preserve authoritative snapshots/history through Phase 011 synchronization. Finalization may satisfy an Evaluation Obligation, but Scorecard does not own that responsibility state.

# Boundaries

Scorecard does not decide who is responsible to evaluate, who participated in an occurrence, who has Access, how authoritative snapshots/provenance are coordinated, or how multiple judgments are aggregated/ranked.

Paper/electronic capture shares this same judgment Concept; capture channel belongs to explanatory Provenance rather than changing evaluator authorship.
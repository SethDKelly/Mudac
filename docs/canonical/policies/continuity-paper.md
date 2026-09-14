---
type: Design Policy
title: Continuity and Paper Policy
description: Rules preserving one evaluation model across normal, degraded, mixed electronic, assisted, and paper operation.
status: stable
tags: [policy, continuity, paper]
sources:
  - resource: ../../002-concept-specification/002-H-export-print-operational-continuity-external-representations.md
  - resource: ../../003-conceptual-ux-architecture/003-G-paper-capture-export-print-publication-experience.md
  - resource: ../../003-conceptual-ux-architecture/003-H-accessibility-mobile-responsive-degraded-mode-interaction-architecture.md
  - resource: ../../011-concept-composition-synchronization/011-E-evaluation-basis-scorecard-authority-versioning-provenance-paper-capture-composition.md
  - resource: ../../011-concept-composition-synchronization/011-F-temporal-correction-invalidation-replacement-successor-work-affected-state-propagation.md
  - resource: ../synchronizations/evaluation-basis-scorecard-authority.md
  - resource: ../synchronizations/temporal-truth-correction.md
generated: { by: openai/gpt-5.6-sol, at: 2026-09-14T13:36:00-05:00 }
---

# Canonical contract

Operational failure may change capture channel but never evaluation meaning, authorship, basis or weight.

Paper judging uses the same Team, Evaluation Occurrence, Evaluation Obligation, Judge, exact authoritative Rubric Version, Criterion, Note and Scorecard semantics as electronic judging.

The Judge remains evaluation author. An Organizer or support actor may be the capture/verification actor only when the identified source unambiguously represents the Judge's recorded content and completed/committed evaluation intent. Capture authority never permits invention of missing/ambiguous judgment.

Paper-origin transcription remains a non-authoritative Scorecard Draft until it has been checked against an identified physical source and the ordinary Scorecard authority-establishment conditions are satisfied. Successful verified paper Finalization establishes the same logical Scorecard authority as electronic Finalization, while [Provenance](../concepts/provenance.md) records the paper source, capture/verification actor, represented Judge authority, and materially distinct occurrence/capture times.

Electronic Draft and paper fallback for the same Evaluation Obligation converge on **one logical Scorecard**, never two votes. The Satisfied obligation refers to that logical Scorecard; [Versioning](../concepts/versioning.md) separately identifies its current authoritative snapshot.

## Post-authority source-faithful correction

If an authoritative digital paper-origin Scorecard is later shown to mismatch the retained physical source while Evaluator, Subject, OccurrenceContext and EvaluationBasis remain correct, the mismatch is a **capture/transcription correction**.

The application preserves the same logical Scorecard and Judge authorship, establishes a successor authoritative Scorecard Version from the verified source, and records Organizer/correction actor versus Judge represented authority through Provenance. The Satisfied Evaluation Obligation remains satisfied by the same logical Scorecard.

This is not a Judge semantic amendment and must not be labeled as one.

If the source is ambiguous, or if correction requires changing Judge, Team, occurrence or Rubric basis, ordinary capture correction is prohibited. Use [Temporal Truth, Correction & Historical Authority](../synchronizations/temporal-truth-correction.md) for structural invalidation/replacement/successor-work semantics.

Ambiguous physical Judge intent cannot be guessed by Organizer. Uncertain authority-establishment state must remain distinguishable from confirmed Finalization/Satisfaction. Duplicate capture of the same physical source or repeated semantic Finalization intent must converge on the existing logical evaluation rather than create another one.

See [Evaluation Basis, Scorecard Authority & Capture Composition](../synchronizations/evaluation-basis-scorecard-authority.md), [Temporal Truth, Correction & Historical Authority](../synchronizations/temporal-truth-correction.md), [Capture-Channel Parity](../invariants/capture-channel-parity.md), [INV-002](../invariants/one-logical-scorecard.md#inv-002), [INV-004](../invariants/organizer-not-judge-author.md#inv-004), and [Truthful Authority Under Uncertainty](../invariants/truthful-authority-under-uncertainty.md).

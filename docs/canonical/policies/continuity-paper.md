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
  - resource: ../synchronizations/evaluation-basis-scorecard-authority.md
generated: { by: openai/gpt-5.6-sol, at: 2026-09-14T11:58:00-05:00 }
---

# Canonical contract

Operational failure may change capture channel but never evaluation meaning, authorship, basis or weight.

Paper judging uses the same Team, Evaluation Occurrence, Evaluation Obligation, Judge, exact authoritative Rubric Version, Criterion, Note and Scorecard semantics as electronic judging.

The Judge remains evaluation author. An Organizer or support actor may be the capture/verification actor only when the identified source unambiguously represents the Judge's recorded content and completed/committed evaluation intent. Capture authority never permits invention of missing/ambiguous judgment.

Paper-origin transcription remains a non-authoritative Scorecard Draft until it has been checked against an identified physical source and the ordinary Scorecard authority-establishment conditions are satisfied. Successful verified paper Finalization establishes the same logical Scorecard authority as electronic Finalization, while [Provenance](../concepts/provenance.md) records the paper source, capture/verification actor, represented Judge authority, and materially distinct occurrence/capture times.

Electronic Draft and paper fallback for the same Evaluation Obligation converge on **one logical Scorecard**, never two votes. The Satisfied obligation refers to that logical Scorecard; [Versioning](../concepts/versioning.md) separately identifies its current authoritative snapshot.

If authoritative Scorecard evidence already exists and another paper/electronic source conflicts materially, ordinary capture does not silently replace authority. The conflict enters explicit correction/invalidation handling.

Ambiguous physical Judge intent cannot be guessed by Organizer. Uncertain authority-establishment state must remain distinguishable from confirmed Finalization/Satisfaction. Duplicate capture of the same physical source or repeated semantic Finalization intent must converge on the existing logical evaluation rather than create another one.

See [Evaluation Basis, Scorecard Authority & Capture Composition](../synchronizations/evaluation-basis-scorecard-authority.md), [Capture-Channel Parity](../invariants/capture-channel-parity.md), [INV-002](../invariants/one-logical-scorecard.md#inv-002), [INV-004](../invariants/organizer-not-judge-author.md#inv-004), and [Truthful Authority Under Uncertainty](../invariants/truthful-authority-under-uncertainty.md).
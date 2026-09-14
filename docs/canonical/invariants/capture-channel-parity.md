---
type: Design Invariant
title: Capture-Channel Parity
description: Electronic, degraded, assisted, and paper capture paths preserve the same evaluation meaning, authorship, basis, logical identity, and weight.
status: stable
tags: [invariant, paper, continuity]
sources:
  - resource: ../../002-concept-specification/002-H-export-print-operational-continuity-external-representations.md
  - resource: ../../003-conceptual-ux-architecture/003-H-accessibility-mobile-responsive-degraded-mode-interaction-architecture.md
  - resource: ../../011-concept-composition-synchronization/011-E-evaluation-basis-scorecard-authority-versioning-provenance-paper-capture-composition.md
  - resource: ../synchronizations/evaluation-basis-scorecard-authority.md
generated: { by: openai/gpt-5.6-sol, at: 2026-09-14T11:58:00-05:00 }
---

<a id="inv-008"></a>
# INV-008 — Capture-Channel Parity

Changing capture channel must not change the identity of Team/Subject, Judge/evaluator, Evaluation Occurrence/context, Evaluation Obligation, exact authoritative Rubric Version/Evaluation Basis, Criterion/Note semantics, logical Scorecard identity, Judge authorship, or evaluation weight.

Assistance or Organizer transcription may change the capture/verification **Actor**, never the semantic evaluator / `RepresentedAuthority`. [Provenance](../concepts/provenance.md) preserves that distinction.

Paper, assisted and electronic traces for the same Evaluation Obligation converge on one logical Scorecard. A paper-origin transcription is non-authoritative until source fidelity and the Judge's completed/committed evaluation intent are established under [Evaluation Basis, Scorecard Authority & Capture Composition](../synchronizations/evaluation-basis-scorecard-authority.md).

Capture ambiguity must remain ambiguity. No capture actor may infer missing Judge judgment, invent Finalization intent, or create a second vote merely to resolve operational uncertainty.

See [Continuity & Paper](../policies/continuity-paper.md), [INV-002](one-logical-scorecard.md#inv-002), and [INV-004](organizer-not-judge-author.md#inv-004).
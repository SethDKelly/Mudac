---
type: Design Policy
title: Continuity and Paper Policy
description: Rules preserving one evaluation model across normal, degraded, mixed electronic, and paper operation.
status: stable
tags: [policy, continuity, paper]
sources:
  - resource: ../../002-concept-specification/002-H-export-print-operational-continuity-external-representations.md
  - resource: ../../003-conceptual-ux-architecture/003-G-paper-capture-export-print-publication-experience.md
  - resource: ../../003-conceptual-ux-architecture/003-H-accessibility-mobile-responsive-degraded-mode-interaction-architecture.md
---

# Canonical contract

Operational failure may change capture channel but never evaluation meaning or weight.

Paper judging uses the same Team/Encounter/Judge/Rubric/Criterion/Note semantics as electronic judging. The Judge remains evaluation author; Organizer may be capture actor. Paper-origin capture becomes eligible only after verification against an identified physical source.

Electronic Draft and paper fallback for the same Judge × Encounter must converge on one logical Scorecard, never two votes.

Ambiguous physical Judge intent cannot be guessed by Organizer. Recovery must be duplicate-safe and stale-state-safe.

See [Capture-Channel Parity](../invariants/capture-channel-parity.md) and [Truthful Authority Under Uncertainty](../invariants/truthful-authority-under-uncertainty.md).
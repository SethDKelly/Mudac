---
type: Design Concept
title: Division
description: Competitive partition within which Teams are compared by default.
status: stable
tags: [concept, competition, ranking]
sources:
  - resource: ../../001-concept-design/001-H-phase-consolidation-initial-concept-catalog.md
  - resource: ../../002-concept-specification/002-A-competition-division-team-alias-specifications.md
  - resource: ../../002-concept-specification/002-I-phase-consolidation-specification-exit-review.md
---

# Purpose

Partition competing Teams into mutually exclusive populations that should be compared against one another.

# Canonical contract

A participating Team belongs to exactly one active Division in the Competition. Division definitions are configurable rather than hard-coded academic labels.

Division assignment is current operational truth. A later correction does not rewrite the Division historically presented during an already-completed [Judging Encounter](judging-encounter.md).

# Boundaries

Division does not own Team identity, evaluation evidence, Aggregate, Rank, or Awards. [Rank](../mechanisms/rank.md) is derived within Division scope under [Evaluation Policy](../policies/evaluation-policy.md).

See [Current vs Historical Truth](../invariants/current-vs-historical-truth.md).
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
  - resource: ../../007-design-refinement/007-B-concept-completeness-independence-genericity-audit.md
---

# Purpose

Partition competing Teams into mutually exclusive populations that should be compared against one another.

# State

Division owns Competition-scoped Division definitions with stable identity, name/description, and Active/Retired status, plus the current Team-to-Division assignment relation. Historical Encounter presentation remains outside Division.

# Actions

Conceptual actions are `define`, `updateDefinition`, `retire`, `assign`, and explicit `correctAssignment`.

Ordinary competition operation treats assignment as stable; a later correction is semantically different from routine movement between cohorts.

# Operational Principle

An Organizer defines the Competition's Divisions and assigns each participating Team to the appropriate competitive cohort. If a Team was misclassified, the Organizer explicitly corrects the assignment; existing Judge evaluations remain attached to the same Team while affected Division-scoped derivations are reassessed.

# Canonical contract

A participating Team belongs to exactly one active Division in the Competition before Ready/Active. Division definitions are configurable rather than hard-coded academic labels.

Division assignment is current operational truth. A later correction does not rewrite the Division historically presented during an already-completed [Judging Encounter](judging-encounter.md).

# Boundaries

Division does not own Team identity, Alias, evaluation evidence, Aggregate, Rank, or Awards. [Rank](../mechanisms/rank.md) is derived within Division scope under [Evaluation Policy](../policies/evaluation-policy.md).

See [Current vs Historical Truth](../invariants/current-vs-historical-truth.md).
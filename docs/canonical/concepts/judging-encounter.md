---
type: Design Concept
title: Judging Encounter
description: One bounded occurrence of a Panel evaluating one Team.
status: stable
tags: [concept, judging, encounter]
sources:
  - resource: ../../001-concept-design/001-H-phase-consolidation-initial-concept-catalog.md
  - resource: ../../002-concept-specification/002-C-panel-membership-judging-encounter-specifications.md
  - resource: ../../002-concept-specification/002-I-phase-consolidation-specification-exit-review.md
---

# Purpose

Represent one bounded occurrence of one [Panel](panel.md) evaluating one [Team](team.md).

# Canonical contract

An Encounter preserves the Panel/Team occurrence, presented Alias and Division context, lifecycle, effective participants, participant adjustments such as absence/recusal/replacement, and evaluation obligations.

Its baseline lifecycle is `Prepared → Open → Complete`, with cancellation before meaningful judging and invalidation/replacement when a completed/open occurrence must no longer contribute officially.

Effective Encounter participation—not nominal Panel membership—creates Scorecard obligations.

# Boundaries

Later Panel, Alias, or Division changes never rewrite what this Encounter historically observed. Same Panel + Team initiation should converge on one valid occurrence unless an explicit rejudge replaces an invalidated one.

See [Scorecard](scorecard.md), [Panel Membership & Composition](../mechanisms/panel-membership-composition.md), and [Current vs Historical Truth](../invariants/current-vs-historical-truth.md).
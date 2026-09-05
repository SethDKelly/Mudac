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
  - resource: ../../007-design-refinement/007-B-concept-completeness-independence-genericity-audit.md
  - resource: ../../007-design-refinement/007-D-temporal-state-correction-invalidation-supersession-historical-truth-closure.md
---

# Purpose

Represent one bounded occurrence of one [Panel](panel.md) evaluating one [Team](team.md).

# State

Encounter owns stable Competition/Panel/Team identity, the presented Alias and Division snapshots, lifecycle, timing, starting participant snapshot, participant adjustments, effective evaluation obligations, and any cancellation/invalidation/replacement relationship.

The baseline lifecycle is `Prepared → Open → Complete`, with `Cancelled` before meaningful judging and `Invalidated` when an occurrence that happened must no longer contribute officially.

# Actions

Conceptual actions are `prepare`, `begin`, `confirmPresentationComplete`, `recordParticipantAdjustment`, `complete`, `cancel`, `invalidate`, and `linkReplacement`.

# Operational Principle

A Panel is ready to judge a Team. The application prepares or resolves the Encounter. When judging begins it snapshots the Team-facing context and participating Judges, creating the basis for individual evaluation obligations. Absence, recusal, or replacement is recorded explicitly. When all remaining required obligations are resolved, the Encounter becomes Complete.

# Canonical contract

Effective Encounter participation—not nominal Panel membership—creates Scorecard obligations.

Invalidating an Encounter preserves that the occurrence happened and preserves the Scorecards Judges authored from it, while making evaluation evidence dependent on that invalid Encounter ineligible for ordinary official aggregation. A rejudge is a distinct replacement Encounter with its own participant/context snapshots and evaluation obligations rather than a mutation of the invalidated occurrence.

# Boundaries

Later Panel, Alias, or Division changes never rewrite what this Encounter historically observed. Same Panel + Team initiation should converge on one valid occurrence unless an explicit rejudge/replacement creates another occurrence.

Encounter does not own Judge judgment, Rubric semantics, or downstream aggregation/ranking.

See [Scorecard](scorecard.md), [Panel Membership & Composition](../mechanisms/panel-membership-composition.md), [Current vs Historical Truth](../invariants/current-vs-historical-truth.md), and [Temporal Truth, Correction & Historical Authority](../synchronizations/temporal-truth-correction.md).

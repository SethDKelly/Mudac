---
type: Design Concept
title: Competition
description: Lifecycle and governing context for one MUDAC competition occurrence.
status: stable
tags: [concept, competition, lifecycle]
sources:
  - resource: ../../001-concept-design/001-H-phase-consolidation-initial-concept-catalog.md
  - resource: ../../002-concept-specification/002-A-competition-division-team-alias-specifications.md
  - resource: ../../002-concept-specification/002-I-phase-consolidation-specification-exit-review.md
---

# Purpose

Establish the lifecycle and governing context of one Competition occurrence.

<a id="comp-001"></a>
## COMP-001 — Competition lifecycle

The Competition lifecycle is:

`Draft → Ready → Active → Event Completed → Finalized`

`Reconciliation` is Organizer work, not a Competition state. `Historical` is a retention/presentation condition, not another lifecycle state.

The Organizer prepares a Draft Competition, explicitly marks it Ready when derived gates pass, activates live judging, completes the live event, reconciles remaining outcome-affecting work, and explicitly Finalizes an official outcome.

<a id="comp-002"></a>
## COMP-002 — Post-Finalization correction preserves Finalized lifecycle

A post-Finalization correction does not roll Competition back to Active or Event Completed. Corrected evidence may lead to a successor [Official Outcome Revision](../mechanisms/official-outcome-revision.md#out-002) while Competition remains Finalized.

# Boundaries

Competition does not absorb Team, Division, Panel, Rubric, Scorecard, Rank, or Award semantics. Those remain independent Concepts or derived mechanisms.

See [Evaluation Policy](../policies/evaluation-policy.md), [Awards & Finalization](../policies/awards-finalization.md), and [Organizer Preparation](../experience/organizer-preparation.md).
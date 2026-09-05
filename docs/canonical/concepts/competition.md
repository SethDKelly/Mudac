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
  - resource: ../../007-design-refinement/007-B-concept-completeness-independence-genericity-audit.md
---

# Purpose

Establish the lifecycle and governing context of one Competition occurrence.

# State

Conceptual state includes stable Competition identity, descriptive event details, scheduled event period, lifecycle state, and meaningful lifecycle-transition timestamps.

The lifecycle is:

`Draft → Ready → Active → Event Completed → Finalized`

`Reconciliation` is Organizer work, not a Competition state. `Historical` is a retention/presentation condition, not another lifecycle state.

# Actions

Conceptual actions are `create`, `updateDetails`, `markReady`, `returnToDraft`, `activate`, `completeEvent`, exceptional `resumeEvent`, and `finalize`.

Readiness and finalization gates are derived from related concepts/policies; Competition owns the transition, not every prerequisite fact.

# Operational Principle

An Organizer creates a Competition and prepares related Divisions, Teams, identities, judging configuration, and operational material. After derived readiness gates pass the Organizer marks it Ready and activates live judging. When live judging ends the Organizer completes the event, reconciliation continues without restoring ordinary Judge access, and explicit Finalization establishes the Competition as a finalized occurrence with an identified official outcome basis.

<a id="comp-001"></a>
## COMP-001 — Competition lifecycle

The Competition lifecycle is:

`Draft → Ready → Active → Event Completed → Finalized`

The Organizer prepares a Draft Competition, explicitly marks it Ready when derived gates pass, activates live judging, completes the live event, reconciles remaining outcome-affecting work, and explicitly Finalizes an official outcome.

<a id="comp-002"></a>
## COMP-002 — Post-Finalization correction preserves Finalized lifecycle

A post-Finalization correction does not roll Competition back to Active or Event Completed. Corrected evidence may lead to a successor [Official Outcome Revision](../mechanisms/official-outcome-revision.md#out-002) while Competition remains Finalized.

# Boundaries

Competition does not absorb Team, Division, Panel, Rubric, Scorecard, Rank, Award, Access, Export, or Publication semantics. Those remain independent Concepts or derived mechanisms coordinated through synchronization.

See [Evaluation Policy](../policies/evaluation-policy.md), [Awards & Finalization](../policies/awards-finalization.md), and [Organizer Preparation](../experience/organizer-preparation.md).
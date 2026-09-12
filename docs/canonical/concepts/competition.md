---
type: Design Concept
title: Competition
description: Lifecycle and governing context for one competition occurrence.
status: stable
tags: [concept, competition, lifecycle]
sources:
  - resource: ../../002-concept-specification/002-A-competition-division-team-alias-specifications.md
  - resource: ../../010-project-purpose-candidate-specification-modularity/010-F-specificity-purpose-singularity-concept-boundary-alternative-audit.md
  - resource: ../../010-project-purpose-candidate-specification-modularity/010-G-completeness-independence-genericity-for-boundary-audit.md
  - resource: ../../010-project-purpose-candidate-specification-modularity/010-H-concept-boundary-convergence-respecification-canonical-reconciliation.md
generated: { by: openai/gpt-5.6-sol, at: 2026-09-12T03:12:00Z }
---

# Purpose

Establish the lifecycle and governing context of one competition occurrence.

# State

Competition owns stable occurrence identity, descriptive event context, scheduled period, lifecycle state, and meaningful lifecycle-transition history.

The baseline lifecycle is:

`Draft → Ready → Active → Event Completed → Finalized`

`Reconciliation` is Organizer work, not a Competition lifecycle state. `Historical` is a retention/presentation condition, not another lifecycle state.

Competition does **not** own the content identity/currentness of the declared official result. That authority belongs to [Outcome Declaration](outcome-declaration.md).

# Actions and queries

Conceptual actions are `create`, `updateDetails`, `markReady`, `returnToDraft`, `activate`, `completeEvent`, exceptional `resumeEvent`, and `finalize`.

Conceptual queries include `state`, `details`, `scheduledPeriod`, and lifecycle history.

Intrinsic transition guards concern the Competition lifecycle itself. Application-specific readiness/finalization prerequisites are supplied by policy/composition; Competition does not inspect peer Concept internals to define its own transitions.

# Operational Principle

An Organizer creates a Competition, updates its event context while it is being prepared, marks it Ready when the application establishes that preparation requirements are satisfied, activates live judging, records the end of the live event, and eventually Finalizes the competition occurrence after the application establishes that closeout conditions are satisfied. Finalization closes the Competition lifecycle while the separately owned Outcome Declaration records which supplied outcome basis has been explicitly declared authoritative.

<a id="comp-001"></a>
## COMP-001 — Competition lifecycle

The lifecycle is `Draft → Ready → Active → Event Completed → Finalized`.

A transition changes the Competition occurrence's lifecycle authority; it does not automatically create, amend, publish, or retract state owned by another Concept.

<a id="comp-002"></a>
## COMP-002 — Post-Finalization correction does not roll back Competition

A legitimate post-Finalization source correction does not roll Competition back to Active or Event Completed. Competition remains Finalized while [Outcome Declaration](outcome-declaration.md) may become Affected and later receive an explicitly confirmed successor through application synchronization.

# MUDAC composition binding

MUDAC normally evaluates preparation/readiness from Team, Division, Alias, judging configuration, evaluation basis and other current source state. Finalization normally coordinates closeout evidence and an Outcome Declaration. Those are application-level composition rules, not intrinsic Competition state.

# Boundaries

Competition does not absorb Team, Division, Panel, Evaluation Occurrence, Evaluation Obligation, Rubric, Scorecard, Rank, Award, Access, Outcome Declaration, Export, or Publication semantics.

See [Evaluation Policy](../policies/evaluation-policy.md), [Awards & Finalization](../policies/awards-finalization.md), and [Organizer Preparation](../experience/organizer-preparation.md).
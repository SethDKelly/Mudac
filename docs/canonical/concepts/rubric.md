---
type: Design Concept
title: Rubric
description: Structured evaluation definition governing valid Judge judgment.
status: stable
tags: [concept, judging, rubric]
sources:
  - resource: ../../001-concept-design/001-H-phase-consolidation-initial-concept-catalog.md
  - resource: ../../002-concept-specification/002-D-rubric-criterion-scorecard-notes-specifications.md
  - resource: ../../002-concept-specification/002-I-phase-consolidation-specification-exit-review.md
  - resource: ../../007-design-refinement/007-B-concept-completeness-independence-genericity-audit.md
---

# Purpose

Define the structured evaluation instrument and semantics of valid judgment.

# State

Rubric owns stable lineage/applicability context, name and instructions, scoring model, ordered Criteria, score domains/guidance, contribution configuration, note policies, and working-definition validity state.

# Actions

Conceptual actions are `createDraft`, `rename`, `updateInstructions`, `configureScoringModel`, `addCriterion`, `editCriterion`, `reorderCriterion`, `removeCriterion`, `configureCriterionNotePolicy`, `configureOverallNotePolicy`, `validate`, and `prepareForUse`.

Establishing an immutable authoritative Rubric Version composes with [Versioning](versioning.md); Rubric itself owns whether its working definition is valid.

# Operational Principle

An Organizer creates a Rubric, defines its scoring model and Criteria, supplies guidance and note requirements, validates the working definition, and establishes an authoritative Version. A Judge later receives that exact Version in an Encounter and records one Scorecard under its semantics.

# Canonical contract

A Scorecard is bound to one exact authoritative Rubric [Version](versioning.md). Semantic Rubric changes require a new Version; existing Scorecards never silently rebind.

Missing, zero, and not-applicable semantics must remain distinguishable where supported. Scoring math must be deterministic and avoid hidden double weighting.

# Boundaries

Criterion and Note are subordinate evaluation structure rather than independent MUDAC Concepts. Rubric does not know which Team or Judge is being evaluated and does not own Competition aggregation/ranking.

See [Criterion & Notes](../mechanisms/criterion-notes.md), [Scorecard](scorecard.md), and [Evaluation Policy](../policies/evaluation-policy.md).
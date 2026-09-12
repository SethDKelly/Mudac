---
type: Design Concept
title: Rubric
description: Structured evaluation definition governing interpretation and validity of judgment responses.
status: stable
tags: [concept, judging, rubric, evaluation-basis]
sources:
  - resource: ../../002-concept-specification/002-D-rubric-criterion-scorecard-notes-specifications.md
  - resource: ../../010-project-purpose-candidate-specification-modularity/010-G-completeness-independence-genericity-for-boundary-audit.md
  - resource: ../../010-project-purpose-candidate-specification-modularity/010-H-concept-boundary-convergence-respecification-canonical-reconciliation.md
generated: { by: openai/gpt-5.6-sol, at: 2026-09-12T03:12:00Z }
---

# Purpose

Define the structured evaluation instrument and the semantics by which supplied judgment responses are interpreted and validated.

# State

Rubric owns stable instrument identity/lineage context, name/instructions, scoring model, ordered Criteria, response/score domains, guidance, contribution configuration, note policies, and working-definition validity state.

Criterion and Note remain subordinate structures rather than independent MUDAC Concepts.

# Actions and queries

Conceptual actions are `createDraft`, `rename`, `updateInstructions`, `configureScoringModel`, `addCriterion`, `editCriterion`, `reorderCriterion`, `removeCriterion`, `configureCriterionNotePolicy`, `configureOverallNotePolicy`, `validateDefinition`, and `prepareForUse`.

Completeness requires Rubric to expose interpretation queries such as:

- `criterionDefinition`;
- `allowedResponseDomain`;
- `interpretResponse`;
- `validateResponse`;
- `validateCompletedResponseSet`;
- `isDefinitionValid`.

These queries define whether supplied response values are semantically valid under the Rubric. A recording Concept such as Scorecard does not invent those semantics.

# Operational Principle

An authorized user defines an evaluation instrument, its Criteria, response domains, scoring semantics, guidance and note requirements. Rubric validates that the working definition is internally coherent and can interpret/validate supplied evaluator responses against that definition. The application may then establish an immutable authoritative basis through Versioning/Provenance synchronization. Evaluators subsequently record judgments against an exact supplied Rubric basis without the recording Concept redefining response meaning.

# Canonical contract

Missing, zero and not-applicable meanings must remain distinguishable where the configured Rubric supports them.

Scoring semantics must be deterministic from the Rubric definition and avoid hidden double weighting.

A semantic Rubric change does not silently reinterpret historical judgment recorded under an earlier supplied basis.

# Generic boundary

Rubric does not intrinsically require Team, Judge, Competition, Evaluation Occurrence, Scorecard, Versioning, or Provenance types. It defines an evaluation instrument and the meaning/validity of response values.

# MUDAC composition binding

MUDAC normally establishes immutable authoritative Rubric states through [Versioning](versioning.md) and [Provenance](provenance.md), then supplies one exact basis to Evaluation Occurrence / Scorecard coordination. Those interactions belong to Phase 011 synchronization rather than Rubric's intrinsic behavior.

# Boundaries

Rubric does not own who is evaluated, who evaluates, evaluator responsibility, judgment authorship, outcome aggregation/ranking, or authoritative lineage mechanics.

See [Criterion & Notes](../mechanisms/criterion-notes.md) and [Evaluation Policy](../policies/evaluation-policy.md).
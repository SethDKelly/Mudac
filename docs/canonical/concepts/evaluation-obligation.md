---
type: Design Concept
title: Evaluation Obligation
description: Responsibility of one evaluator to produce one qualifying independent evaluation for a supplied subject and basis.
status: stable
tags: [concept, judging, obligation, responsibility]
sources:
  - resource: ../../002-concept-specification/002-C-panel-membership-judging-encounter-specifications.md
  - resource: ../../010-project-purpose-candidate-specification-modularity/010-E-retained-concept-purpose-operational-principle-state-action-behavioral-specification-current-truth-audit.md
  - resource: ../../010-project-purpose-candidate-specification-modularity/010-F-specificity-purpose-singularity-concept-boundary-alternative-audit.md
  - resource: ../../010-project-purpose-candidate-specification-modularity/010-G-completeness-independence-genericity-for-boundary-audit.md
  - resource: ../../010-project-purpose-candidate-specification-modularity/010-H-concept-boundary-convergence-respecification-canonical-reconciliation.md
generated: { by: openai/gpt-5.6-sol, at: 2026-09-12T03:12:00Z }
---

# Purpose

Represent one evaluator's responsibility to produce one qualifying independent evaluation for a supplied subject, basis, and scope, without inventing judgment or transferring authorship.

# Abstract parameters

Conceptually:

`EvaluationObligation<Scope, Evaluator, Subject, Basis, OccurrenceRef, EvidenceRef>`

`OccurrenceRef` and `EvidenceRef` are optional references used when the application wants to associate the responsibility with a particular occurrence or qualifying evidence. The Concept does not need peer internals.

# State

Evaluation Obligation owns:

- stable obligation identity;
- Scope, Evaluator, Subject, and Basis values;
- optional Occurrence reference;
- responsibility state such as `Outstanding`, `Satisfied`, `Excused`, or `Cancelled`;
- optional qualifying Evidence reference when Satisfied;
- attributable reason/authority for Excused or Cancelled state when material;
- predecessor/successor responsibility relation for reassignment or legitimate re-evaluation;
- meaningful state-transition history.

A terminal historical obligation is never silently reopened. When a legitimate new responsibility is required after a terminal obligation—for example because prior satisfying evidence becomes unusable—the application creates a **successor obligation** and preserves the predecessor's history.

# Actions and queries

Conceptual actions are `establish`, `satisfy`, `excuse`, `cancel`, `reassignWithSuccessor`, and `requireSuccessorEvaluation`.

Conceptual queries include `state`, `isOutstanding`, `qualifyingEvidence`, `predecessor`, `successor`, and obligation history.

# Operational Principle

An application establishes that one evaluator is responsible for one independent evaluation. The obligation remains Outstanding until qualifying evidence is supplied or an authorized condition ends the responsibility. If another evaluator must take over, the original obligation is ended through an attributable transition and a successor obligation is established rather than changing evaluator identity in place. If already-satisfied evidence later becomes ineligible and legitimate re-evaluation is required, the satisfied obligation remains historical and a new successor responsibility becomes Outstanding.

# Canonical contract

An obligation is not a judgment. `Satisfied` means qualifying evidence has been associated with the responsibility; it does not transfer semantic authorship or imply that the obligation owns the evidence content.

Missing work remains explicitly Outstanding unless it is legitimately Excused or Cancelled. Missing is never represented as zero or as a fabricated Scorecard.

Reassignment and re-evaluation preserve predecessor responsibility history.

# MUDAC composition binding

MUDAC normally binds Evaluator to Judge Participation identity, Subject to Team, Basis to an exact evaluation basis, and optional OccurrenceRef to Evaluation Occurrence. Scorecard finalization may satisfy an obligation through Phase 011 synchronization. Panel membership may contribute to obligation creation, but Panel is not intrinsic to responsibility semantics.

# Boundaries

Evaluation Obligation does not own:

- what happened in the shared occurrence ([Evaluation Occurrence](evaluation-occurrence.md));
- reusable grouping ([Panel](panel.md));
- the evaluator's judgment ([Scorecard](scorecard.md));
- evaluation-instrument semantics ([Rubric](rubric.md));
- factual aggregate sufficiency across multiple obligations/evidence ([Coverage](../mechanisms/coverage.md)).
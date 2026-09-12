---
type: Design Concept
title: Evaluation Occurrence
description: Bounded historical occurrence in which evaluators encounter a subject under a presented context and evaluation basis.
status: stable
tags: [concept, judging, occurrence, history]
sources:
  - resource: ../../002-concept-specification/002-C-panel-membership-judging-encounter-specifications.md
  - resource: ../../010-project-purpose-candidate-specification-modularity/010-F-specificity-purpose-singularity-concept-boundary-alternative-audit.md
  - resource: ../../010-project-purpose-candidate-specification-modularity/010-G-completeness-independence-genericity-for-boundary-audit.md
  - resource: ../../010-project-purpose-candidate-specification-modularity/010-H-concept-boundary-convergence-respecification-canonical-reconciliation.md
generated: { by: openai/gpt-5.6-sol, at: 2026-09-12T03:12:00Z }
---

# Purpose

Preserve the truth of one bounded evaluation occurrence: what subject/context/basis was presented, which evaluators actually participated, when the occurrence happened, and whether that occurrence remains valid for its intended use.

# Abstract parameters

Conceptually:

`EvaluationOccurrence<Scope, Subject, Evaluator, PresentedContext, BasisRef>`

These parameters identify supplied values; they do not require Evaluation Occurrence to understand peer Concept internals.

# State

Evaluation Occurrence owns:

- stable occurrence identity;
- Scope and Subject references;
- presented-context snapshot;
- optional evaluation-basis reference/snapshot sufficient to identify what governed the occurrence;
- starting evaluator set and attributable participant adjustments;
- effective actual participant history;
- occurrence timing;
- lifecycle/validity such as `Prepared`, `Open`, `Complete`, `Cancelled`, or `Invalidated`;
- optional replacement relationship to a distinct successor occurrence.

Completion means the bounded occurrence itself ended. It does **not** mean every evaluator responsibility has been satisfied.

# Actions and queries

Conceptual actions are `prepare`, `begin`, `recordParticipantAdjustment`, `completeOccurrence`, `cancel`, `invalidate`, and `linkReplacement`.

Conceptual queries include `presentedContext`, `basisRef`, `startingEvaluators`, `effectiveParticipants`, `state`, `isEligible`, `replacement`, and occurrence history.

# Operational Principle

An application prepares an occurrence for a subject and captures the context/basis intended to be presented. When the occurrence begins, it records the starting evaluators. Absence, recusal, substitution, or other participant changes are recorded as occurrence history rather than silently rewriting the starting snapshot. When the presentation/evaluation event ends, the occurrence becomes Complete even if individual evaluation work continues afterward. If the occurrence is later found unusable, it may be Invalidated while preserving that it actually happened; a re-evaluation uses a distinct replacement occurrence.

# Canonical contract

Historical occurrence truth is immutable by ordinary changes to current grouping, subject metadata, aliases, cohort assignment, or evaluator participation elsewhere.

Cancellation and invalidation are distinct: cancellation represents an intended occurrence stopped before meaningful qualifying use; invalidation represents an occurrence that happened but later becomes ineligible for its authoritative purpose.

Replacement never mutates the invalidated occurrence into a new one.

# MUDAC composition binding

MUDAC normally binds:

- `Scope` to Competition context;
- `Subject` to a Team identity;
- `Evaluator` to Judge Participation identities;
- `PresentedContext` to Judge-facing Alias/Division and other material presentation facts;
- `BasisRef` to the exact applicable evaluation basis.

Panel may supply an intended starting group, but Panel is not intrinsic to this Concept. Evaluation Obligations may be established from the occurrence through Phase 011 synchronization, but obligation state is not owned here.

# Boundaries

Evaluation Occurrence does not own:

- reusable evaluator grouping ([Panel](panel.md));
- evaluator responsibility ([Evaluation Obligation](evaluation-obligation.md));
- evaluator-authored judgment ([Scorecard](scorecard.md));
- evaluation semantics ([Rubric](rubric.md));
- derived outcome calculations.

The former [Judging Encounter](judging-encounter.md) path is retained only as a deprecated historical adapter.
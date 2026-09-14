---
type: Design Concept
title: Award
description: Scoped recognition definition and attributable conferral over supplied recipient and selection basis.
status: stable
tags: [concept, outcome, award, recognition]
sources:
  - resource: ../../002-concept-specification/002-G-awards-reconciliation-finalization-official-outcomes.md
  - resource: ../../010-project-purpose-candidate-specification-modularity/010-G-completeness-independence-genericity-for-boundary-audit.md
  - resource: ../../010-project-purpose-candidate-specification-modularity/010-H-concept-boundary-convergence-respecification-canonical-reconciliation.md
  - resource: ../../011-concept-composition-synchronization/011-G-coverage-aggregate-rank-award-competition-finalization-outcome-declaration-composition.md
  - resource: ../synchronizations/evaluation-outcome-finalization-declaration.md
generated: { by: openai/gpt-5.6-sol, at: 2026-09-14T14:24:00-05:00 }
---

# Purpose

Define and confer recognized achievement within a supplied Scope under explicit selection semantics.

# Abstract parameters

Conceptually:

`Award<Scope, Recipient, SelectionBasis>`

Award can consume supplied selection evidence/basis without understanding a Rank mechanism internally.

# State

Award owns stable identity within Scope, name/description, recognition scope, selection method/rule, eligibility rules, recipient cardinality, required/optional closeout posture, definition availability/history, and attributable conferral/revocation/correction history.

Selection method is at least `Derived` or `Discretionary` in semantic character and must remain explicit.

# Actions and queries

Conceptual actions are `define`, `updateDefinition`, `retireUnusedDefinition`, `confer`, `revoke`, and `correctConferral`.

Queries include current definition, current conferrals, history, and whether a supplied SelectionBasis is consistent with the declared rule.

# Operational Principle

An authorized actor defines recognition and its selection semantics. For a derived selection method, the application supplies a current SelectionBasis and Award validates that any conferral is consistent with its declared rule. For discretionary recognition, an authorized actor deliberately selects a Recipient without portraying the choice as mathematically implied. Later correction preserves prior conferral/revocation history.

# MUDAC composition binding

MUDAC normally binds Scope to Competition and Recipient to Team.

For rank-derived Awards, current [Evaluation Outcome, Award, Finalization & Declaration Composition](../synchronizations/evaluation-outcome-finalization-declaration.md) supplies Rank as SelectionBasis only after the applicable Division/result is **Ranking Ready**. A provisional calculated ordering is insufficient for rank-derived conferral while material eligibility, correction, compatibility or tie conditions remain unresolved.

The system derives the candidate; `Award.confer` owns recognition. Organizer confirmation cannot contradict the declared rank-derived rule while continuing to label the Award derived.

A later Rank change does not silently move recognition. The supplied basis is reassessed and any required `correctConferral`/`revoke`/new conferral is explicit and attributable.

For discretionary Awards, the SelectionBasis remains explicitly discretionary; Rank/Notes/statistics do not silently become a mathematical selection rule.

# Boundaries

Award is distinct from Rank, Outcome Declaration, Competition lifecycle, and Publication. Outcome Declaration may include an identified Award state in its supplied declared basis without taking ownership of Award semantics.
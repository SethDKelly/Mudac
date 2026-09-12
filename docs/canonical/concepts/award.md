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
generated: { by: openai/gpt-5.6-sol, at: 2026-09-12T03:12:00Z }
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

An authorized actor defines recognition and its selection semantics. For a derived selection method, the application supplies a current SelectionBasis and the Award validates that any conferral is consistent with its declared rule. For discretionary recognition, an authorized actor deliberately selects a Recipient without portraying the choice as mathematically implied. Later correction preserves prior conferral/revocation history.

# MUDAC composition binding

MUDAC normally binds Scope to Competition and Recipient to Team. Rank-derived Awards consume supplied Rank result/basis through application composition; Rank remains a derived mechanism and is not intrinsic Award state.

# Boundaries

Award is distinct from Rank, Outcome Declaration, Competition lifecycle, and Publication. Outcome Declaration may include an identified Award state in its supplied declared basis without taking ownership of Award semantics.
---
type: Design Concept
title: Award
description: Explicit Competition recognition with declared scope and selection semantics.
status: stable
tags: [concept, outcome, award]
sources:
  - resource: ../../001-concept-design/001-H-phase-consolidation-initial-concept-catalog.md
  - resource: ../../002-concept-specification/002-G-awards-reconciliation-finalization-official-outcomes.md
  - resource: ../../002-concept-specification/002-I-phase-consolidation-specification-exit-review.md
  - resource: ../../007-design-refinement/007-B-concept-completeness-independence-genericity-audit.md
---

# Purpose

Define and confer recognized achievement within a Competition.

# State

Award owns stable Competition-scoped Award identity, name/description, scope, selection method, eligibility rules, recipient cardinality, required/optional closeout posture, definition availability/history, and attributable conferral/revocation history.

Selection method is at least `Rank-derived` or `Discretionary` and must remain explicit.

# Actions

Conceptual actions are `define`, `updateDefinition`, `retireUnusedDefinition`, `confer`, `revoke`, and `correctConferral`, subject to Competition lifecycle/correction authority.

# Operational Principle

An Organizer defines a recognition and its selection semantics. For a rank-derived Award, the system derives candidate recipient(s) from the declared Rank rule and an authorized Organizer confirms a consistent conferral. For a discretionary Award, an authorized Organizer deliberately confers recognition without portraying the choice as mathematically implied. Later correction preserves prior conferrals/revocations rather than rewriting history.

# Canonical contract

Awards may be rank-derived or discretionary. A rank-derived Award consumes a ready [Rank](../mechanisms/rank.md) and declared rule; Organizer confirmation cannot contradict that rule. A discretionary Award represents authorized human judgment and must not be portrayed as mathematically implied.

# Boundaries

Award is distinct from Rank. Ranking orders Teams; Award represents recognition. Official-outcome revisioning records which Award state was officially declared but does not replace Award itself.

See [Awards & Finalization](../policies/awards-finalization.md) and [Reconciliation & Finalization Experience](../experience/reconciliation-finalization.md).
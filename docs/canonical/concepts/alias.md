---
type: Design Concept
title: Alias
description: Scoped alternate identity for a Subject that preserves historical mapping without exposing underlying identity by default.
status: stable
tags: [concept, identity, anonymity, alias]
sources:
  - resource: ../../002-concept-specification/002-A-competition-division-team-alias-specifications.md
  - resource: ../../010-project-purpose-candidate-specification-modularity/010-G-completeness-independence-genericity-for-boundary-audit.md
  - resource: ../../010-project-purpose-candidate-specification-modularity/010-H-concept-boundary-convergence-respecification-canonical-reconciliation.md
generated: { by: openai/gpt-5.6-sol, at: 2026-09-12T03:12:00Z }
---

# Purpose

Give a Subject a context-specific alternate identity within a Scope so interaction can use that identity without exposing the underlying subject identity by default.

# Abstract parameters

Conceptually:

`Alias<Subject, Scope, AliasValue>`

Alias is intrinsically generic over subject identity, scope, and alias value.

# State

Alias owns Subject, Scope, AliasValue, Active/Retired-or-Superseded status, uniqueness/reservation within the applicable scope, and historical mapping needed to resolve previously used values.

# Actions and queries

Conceptual actions are `assign`, `replace`, and `retire`.

Conceptual queries include `currentAlias`, `history`, and access-controlled `resolve` to the underlying Subject.

# Operational Principle

A Subject receives an alternate identity for a Scope. Ordinary interaction can use the Alias without revealing underlying identity. If correction replaces an Alias after use, the prior value remains reserved and historically traceable rather than silently reused. Whether a caller may resolve the Alias is an Access decision, not Alias state.

# MUDAC composition binding

MUDAC normally binds Subject to Team and Scope to Competition. The Alias is the Judge-facing competitor identity during blinded judging; Evaluation Occurrence preserves the Alias/presentation value actually shown at the time.

# Boundaries

Alias is not authentication, a secret, Team Name, Division encoding, permanent Subject identity, or an Access-control mechanism.

See [Anonymity & Disclosure](../policies/anonymity-disclosure.md).
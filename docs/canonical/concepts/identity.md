---
type: Design Concept
title: Identity
description: Stable human identity continuity independent of Competition authority.
status: stable
tags: [concept, identity, authority]
sources:
  - resource: ../../001-concept-design/001-H-phase-consolidation-initial-concept-catalog.md
  - resource: ../../002-concept-specification/002-B-identity-participation-access-specifications.md
  - resource: ../../002-concept-specification/002-I-phase-consolidation-specification-exit-review.md
  - resource: ../../007-design-refinement/007-B-concept-completeness-independence-genericity-audit.md
---

# Purpose

Maintain continuity that actions and Participation episodes belong to the same human identity.

# State

Identity owns a stable identity reference, minimal necessary human-facing identification/recovery attributes, verification/reverification state, and status such as `Established` or `Disabled`. Event role/lifecycle state does not belong to Identity.

# Actions

Conceptual actions are `establish`, `verify`, `reverify`, `updateNecessaryIdentityInformation`, `recover`, `recognizeReturningIdentity`, `disable`, and `restore`.

The exact authentication proof mechanism remains outside the Concept.

# Operational Principle

A first-time volunteer establishes enough verified Identity continuity to be distinguished from others and then receives a separate Competition Participation. At a later Competition the same Identity may be recognized and reverified, reducing repeated identity entry while still requiring a new Participation and current Access.

# Canonical contract

Identity answers who the human is. It may persist across Competition occurrences and may be established, reverified, or disabled without rewriting historical attribution.

Identity alone does not grant current Competition authority, restore prior Panel assignment, or imply permanent Judge/Organizer role.

# Boundaries

Authentication/session mechanisms are implementation concerns. Current event capacity is represented by [Participation](participation.md) and current permission/disclosure by [Access](access.md).

See [Judge Onboarding](../experience/judge-onboarding.md).
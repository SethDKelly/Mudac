---
type: Design Concept
title: Alias
description: Competition-scoped Team identity used to support blinded judging.
status: stable
tags: [concept, identity, anonymity]
sources:
  - resource: ../../001-concept-design/001-H-phase-consolidation-initial-concept-catalog.md
  - resource: ../../002-concept-specification/002-A-competition-division-team-alias-specifications.md
  - resource: ../../002-concept-specification/002-I-phase-consolidation-specification-exit-review.md
  - resource: ../../007-design-refinement/007-B-concept-completeness-independence-genericity-audit.md
---

# Purpose

Give a subject a context-specific identity that can be used without exposing its underlying administrative identity.

# State

Alias owns subject, scope, value, Active/Retired-or-Superseded status, and the historical mapping needed to resolve previously used values. For MUDAC, subject is Team and scope is Competition.

# Actions

Conceptual actions are `assign`, `replace`, `retire`, and `resolve`.

Whether a caller may resolve an Alias to its underlying subject is an [Access](access.md) question rather than Alias state.

# Operational Principle

A Team is assigned a competition identity that avoids unnecessary institutional disclosure. Judges interact with that Alias during judging. Authorized Organizer activity may resolve it to the Team. If a correction replaces the Alias after use, the prior value remains reserved and historically traceable rather than being silently reused.

# Canonical contract

Each participating Team requires exactly one active Competition Alias before Ready. Active Aliases are unique in Competition scope, designed not to reveal institution identity, and are not recycled after operational use.

Alias is the canonical Judge-facing Team identity during blinded judging. Historical Encounters preserve the Alias presented at the time even if current Alias is later corrected.

# Boundaries

Alias is not authentication, a secret, Team Name, Division encoding, or stable Team identity.

See [Team](team.md), [Anonymity & Disclosure](../policies/anonymity-disclosure.md), and [Current vs Historical Truth](../invariants/current-vs-historical-truth.md).
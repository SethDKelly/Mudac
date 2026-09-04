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
---

# Purpose

Give a subject a context-specific identity that can be used without exposing its underlying administrative identity.

# Canonical contract

Each participating Team requires exactly one active Competition Alias before Ready. Active Aliases are unique in Competition scope, designed not to reveal institution identity, and are not recycled after use.

Alias is the canonical Judge-facing Team identity during blinded judging. Historical Encounters preserve the Alias presented at the time even if current Alias is later corrected.

# Boundaries

Alias is not authentication, a secret, Team Name, or stable Team identity.

See [Team](team.md), [Anonymity & Disclosure](../policies/anonymity-disclosure.md), and [Current vs Historical Truth](../invariants/current-vs-historical-truth.md).
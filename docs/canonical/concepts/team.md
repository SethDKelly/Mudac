---
type: Design Concept
title: Team
description: Stable administrative representation of one competing student group.
status: stable
tags: [concept, competitor, team]
sources:
  - resource: ../../001-concept-design/001-H-phase-consolidation-initial-concept-catalog.md
  - resource: ../../002-concept-specification/002-A-competition-division-team-alias-specifications.md
  - resource: ../../002-concept-specification/002-A1-team-extensible-attributes-team-name-refinement.md
  - resource: ../../002-concept-specification/002-I-phase-consolidation-specification-exit-review.md
---

# Purpose

Maintain the administrative representation of a student group participating as one competing unit.

# Canonical contract

Team owns stable Team identity, Competition scope, participation status such as Active/Withdrawn, administrative record, and disclosure-controlled descriptive attributes.

A Team may carry optional `teamName` and other explicitly defined descriptive attributes. Those attributes do not replace stable identity and have no competitive effect unless explicit policy gives them one.

# Boundaries

Team does not own [Division](division.md), [Alias](alias.md), Encounters, Scorecards, Aggregate, Rank, or Awards.

`teamName` is not Alias, need not be unique, and is hidden from Judges by default during blinded judging.

See [Team Attributes](../mechanisms/team-attributes.md) and [Anonymity & Disclosure](../policies/anonymity-disclosure.md).
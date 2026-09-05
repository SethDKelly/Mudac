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
  - resource: ../../007-design-refinement/007-B-concept-completeness-independence-genericity-audit.md
---

# Purpose

Maintain the administrative representation of a student group participating as one competing unit.

# State

Team owns stable Team identity, one Competition scope, the Organizer-facing administrative record, disclosure-controlled descriptive attributes, and participation status such as `Active` or `Withdrawn`.

# Actions

Conceptual actions are `create`, `updateAdministrativeRecord`, `withdraw`, and `restore` while Competition policy still permits restoration.

Withdrawal preserves existing authoritative/historical relationships rather than deleting them.

# Operational Principle

An Organizer establishes a Team as the administrative representation of one competing student group. The application separately coordinates its Division and competition-safe Alias. Judges evaluate the Team through that Alias in Encounters without requiring the administrative identity. Withdrawal prevents future ordinary judging while preserving prior evidence and history.

# Canonical contract

A Team may carry optional `teamName` and other explicitly defined descriptive attributes. Those attributes do not replace stable identity and have no competitive effect unless explicit policy gives them one.

# Boundaries

Team does not own [Division](division.md), [Alias](alias.md), Encounters, Scorecards, Aggregate, Rank, or Awards.

`teamName` is not Alias, need not be unique, and is hidden from Judges by default during blinded judging.

See [Team Attributes](../mechanisms/team-attributes.md) and [Anonymity & Disclosure](../policies/anonymity-disclosure.md).
---
type: Design Concept
title: Panel
description: Reusable grouping of Judge Participations intended to evaluate together.
status: stable
tags: [concept, judging, panel]
sources:
  - resource: ../../001-concept-design/001-H-phase-consolidation-initial-concept-catalog.md
  - resource: ../../002-concept-specification/002-C-panel-membership-judging-encounter-specifications.md
  - resource: ../../002-concept-specification/002-I-phase-consolidation-specification-exit-review.md
  - resource: ../../007-design-refinement/007-B-concept-completeness-independence-genericity-audit.md
---

# Purpose

Maintain a reusable grouping of active Judge [Participations](participation.md) intended to evaluate together.

# State

Panel owns stable Competition-scoped identity, human-facing label, Active/Retired availability, membership history, and current optional composition-capacity assignments. Membership preserves effective intervals rather than only a current `panel_id`.

# Actions

Conceptual actions are `create`, `rename`, `addMember`, `endMembership`, `replaceMember`, `assignCompositionCapacity`, `clearCompositionCapacity`, `retire`, and `restore`.

# Operational Principle

An Organizer creates a Panel, groups eligible Judge Participations, assigns composition capacities where useful, and uses the Panel across repeated Team Encounters. Membership may change during the event while previous Encounters retain the participants who actually evaluated at that time.

# Canonical contract

Current Panel membership answers who is intended to judge together now. It does not answer who actually evaluated a Team in a past occurrence.

# Boundaries

Historical participation belongs to [Judging Encounter](judging-encounter.md). Panel membership alone does not create Scorecard obligations. Composition compliance is policy/derivation rather than a Panel lifecycle.

See [Panel Membership & Composition](../mechanisms/panel-membership-composition.md), [Panel Composition Policy](../policies/panel-composition.md), and [Current vs Historical Truth](../invariants/current-vs-historical-truth.md).
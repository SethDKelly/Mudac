---
type: Design Concept
title: Panel
description: Reusable scoped grouping of evaluator Members intended to operate together.
status: stable
tags: [concept, judging, panel, grouping]
sources:
  - resource: ../../002-concept-specification/002-C-panel-membership-judging-encounter-specifications.md
  - resource: ../../010-project-purpose-candidate-specification-modularity/010-G-completeness-independence-genericity-for-boundary-audit.md
  - resource: ../../010-project-purpose-candidate-specification-modularity/010-H-concept-boundary-convergence-respecification-canonical-reconciliation.md
generated: { by: openai/gpt-5.6-sol, at: 2026-09-12T03:12:00Z }
---

# Purpose

Maintain a reusable grouping of evaluator Members intended to operate together within a supplied Scope.

# Abstract parameters

Conceptually:

`Panel<Scope, Member, CapacityLabel>`

Panel needs Member identity and optional composition-capacity labels. It does not require Participation lifecycle semantics.

# State

Panel owns stable Panel identity, Scope, human-facing label, Active/Retired availability, membership history with effective intervals, and optional current composition-capacity assignments.

# Actions and queries

Conceptual actions are `create`, `rename`, `addMember`, `endMembership`, `replaceMember`, `assignCompositionCapacity`, `clearCompositionCapacity`, `retire`, and `restore`.

Queries include current members, membership-as-of, availability, and current composition-capacity assignment.

# Operational Principle

An Organizer creates a Panel, groups evaluator Members, optionally records composition capacities, and reuses the grouping across multiple evaluation situations. Membership may change while earlier occurrences retain their own actual participant history. Panel represents intended reusable grouping, not who actually evaluated in any particular occurrence.

# MUDAC composition binding

MUDAC normally binds Scope to Competition and Member to Judge Participation identity. Participation eligibility and composition-policy compliance are supplied/application concerns. Evaluation Occurrence may use a Panel's current membership as an intended starting group, but Panel membership does not itself create Evaluation Obligations.

# Boundaries

Actual occurrence participants belong to [Evaluation Occurrence](evaluation-occurrence.md). Individual responsibility belongs to [Evaluation Obligation](evaluation-obligation.md). Panel does not own judgment, Access, or derived composition compliance.

See [Panel Membership & Composition](../mechanisms/panel-membership-composition.md).
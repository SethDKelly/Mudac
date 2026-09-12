---
type: Design Concept
title: Team
description: Stable scoped administrative representation of one competing student group.
status: stable
tags: [concept, competitor, team]
sources:
  - resource: ../../002-concept-specification/002-A-competition-division-team-alias-specifications.md
  - resource: ../../002-concept-specification/002-A1-team-extensible-attributes-team-name-refinement.md
  - resource: ../../010-project-purpose-candidate-specification-modularity/010-G-completeness-independence-genericity-for-boundary-audit.md
  - resource: ../../010-project-purpose-candidate-specification-modularity/010-H-concept-boundary-convergence-respecification-canonical-reconciliation.md
generated: { by: openai/gpt-5.6-sol, at: 2026-09-12T03:12:00Z }
---

# Purpose

Maintain the administrative representation of one student group participating as a single competing unit within a supplied Scope.

# Abstract parameter

Conceptually: `Team<Scope>`.

Team requires a Scope identity but does not need Competition lifecycle semantics to define its own competing-unit record.

# State

Team owns stable Team identity, Scope, Organizer-facing administrative record, disclosure-controlled descriptive attributes, and participation status such as `Active` or `Withdrawn`.

# Actions and queries

Conceptual actions are `create`, `updateAdministrativeRecord`, `withdraw`, and `restore` while governing policy permits restoration.

Queries include current status and administrative/descriptive state under the applicable disclosure contract.

# Operational Principle

An Organizer establishes a Team as one competing unit, maintains necessary administrative/descriptive information, and may withdraw or restore it without deleting prior history. Other Concepts may associate the Team with competitive cohort, blinded identity, evaluation occurrences and outcomes, but those relationships do not become Team-owned state merely because they concern the same competitor.

# MUDAC composition binding

MUDAC normally binds Scope to Competition. Division and Alias are coordinated separately; Judges ordinarily encounter the Team through a Judge-safe Alias rather than administrative identity.

# Boundaries

Team does not own Division, Alias, Evaluation Occurrence, Evaluation Obligation, Scorecard, Aggregate, Rank, Award, or Outcome Declaration.

`teamName` is descriptive metadata, not Alias, need not be unique, and has no competitive meaning unless explicit policy gives it one.
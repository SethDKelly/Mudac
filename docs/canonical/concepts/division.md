---
type: Design Concept
title: Division
description: Scoped competitive cohort definition and member assignment for legitimate comparison.
status: stable
tags: [concept, competition, division, cohort]
sources:
  - resource: ../../002-concept-specification/002-A-competition-division-team-alias-specifications.md
  - resource: ../../010-project-purpose-candidate-specification-modularity/010-G-completeness-independence-genericity-for-boundary-audit.md
  - resource: ../../010-project-purpose-candidate-specification-modularity/010-H-concept-boundary-convergence-respecification-canonical-reconciliation.md
generated: { by: openai/gpt-5.6-sol, at: 2026-09-12T03:12:00Z }
---

# Purpose

Partition competing members within a Scope into mutually exclusive cohorts that should be compared under the same competitive grouping.

# Abstract parameters

Conceptually:

`Division<Scope, Member>`

Division needs only scoped Member identity; it does not require the internals of Competition or Team.

# State

Division owns stable cohort identity within Scope, name/description, Active/Retired availability, current Member-to-Division assignment, and attributable correction history for assignment mistakes.

# Actions and queries

Conceptual actions are `define`, `updateDefinition`, `retire`, `assign`, and `correctAssignment`.

Queries include current assignment, active cohorts, and assignment history.

# Operational Principle

An authorized actor defines competitive cohorts within a Scope and assigns each competing Member to the appropriate cohort. Ordinary operation treats assignment as current competitive truth. If a Member was misclassified, the assignment is explicitly corrected rather than silently rewritten; historical evaluation/presentation elsewhere remains governed by the state captured by those Concepts.

# MUDAC composition binding

MUDAC normally binds Scope to Competition and Member to Team identity. Rank is derived within current Division scope under Evaluation Policy, but Division does not calculate ranking.

# Boundaries

Division does not own competitor identity, Alias, evaluation evidence, occurrence history, Aggregate, Rank, Award, or outcome declaration.
---
type: Design Concept
title: Participation
description: Scoped, time-bounded involvement of a Participant in a particular capacity.
status: stable
tags: [concept, participation, authority]
sources:
  - resource: ../../002-concept-specification/002-B-identity-participation-access-specifications.md
  - resource: ../../010-project-purpose-candidate-specification-modularity/010-G-completeness-independence-genericity-for-boundary-audit.md
  - resource: ../../010-project-purpose-candidate-specification-modularity/010-H-concept-boundary-convergence-respecification-canonical-reconciliation.md
generated: { by: openai/gpt-5.6-sol, at: 2026-09-12T03:12:00Z }
---

# Purpose

Represent a Participant taking part in a supplied Scope for a limited period and in a particular Capacity.

# Abstract parameters

Conceptually:

`Participation<Participant, Scope, Capacity>`

Participation needs the Participant identity, Scope, and Capacity value. It does not require Identity or Competition internals.

# State

Participation owns Participant reference, Scope, Capacity, lifecycle/status, lifecycle timestamps, and capacity-relevant declared metadata.

A representative lifecycle is `Enrolled → Checked In → Active → Completed`, with `Withdrawn` as an exceptional non-participating state and restoration where governing policy permits.

# Actions and queries

Conceptual actions are `enroll`, `checkIn`, `activate`, `updateDeclaredAttributes`, `withdraw`, `restore`, and `complete`.

Queries include current state/capacity, effective participation status, and participation history.

# Operational Principle

A Participant enrolls in a Scope in a particular Capacity, becomes operationally active when eligibility/preparation conditions supplied by the application are satisfied, performs capacity-specific work through separately evaluated Access, and later completes or withdraws. A later Scope uses a new Participation even when the same Participant identity is reused.

# MUDAC composition binding

MUDAC normally binds Participant to Identity, Scope to Competition, and Capacity to values such as Judge or Organizer. Returning Identity continuity may simplify reverification but does not resume a prior Participation. Panel may group Judge Participation identities without changing their Participation capacity.

# Boundaries

Participation does not establish permanent human identity, current Access, Panel membership, technical-administrator privilege, or semantic authorship.
---
type: Design Concept
title: Participation
description: Competition-scoped, time-bounded involvement of an Identity in a particular capacity.
status: stable
tags: [concept, participation, authority]
sources:
  - resource: ../../001-concept-design/001-H-phase-consolidation-initial-concept-catalog.md
  - resource: ../../002-concept-specification/002-B-identity-participation-access-specifications.md
  - resource: ../../002-concept-specification/002-I-phase-consolidation-specification-exit-review.md
  - resource: ../../007-design-refinement/007-B-concept-completeness-independence-genericity-audit.md
---

# Purpose

Represent an [Identity](identity.md) taking part in a scoped activity for a limited period and in a particular capacity.

# State

Participation owns Identity reference, one Competition scope, role such as Judge or Organizer, participation lifecycle/status, lifecycle timestamps, and role-relevant declared metadata such as current Judge expertise.

The baseline lifecycle is `Enrolled → Checked In → Active → Completed`, with `Withdrawn` as an exceptional non-participating state and restoration while policy permits.

# Actions

Conceptual actions are `enroll`, `checkIn`, `activate`, `updateDeclaredAttributes`, `withdraw`, `restore`, and `complete`.

# Operational Principle

A volunteer establishes Identity, enrolls for the current Competition in a particular capacity, checks in and becomes Active when operationally eligible, performs role-specific work through separately evaluated Access, and later becomes Completed. A later Competition creates a new Participation even when the Identity is reused.

# Canonical contract

Judge and Organizer are Participation roles, not permanent Identity types. Returning Identity continuity may simplify reverification but does not resume an old Competition Participation.

# Boundaries

Expertise is Participation metadata, not authorization. Technical Administrator authority does not automatically create Organizer Participation. Panel membership does not change Participation role.

Current permission/disclosure is determined through [Access](access.md). See [Judge Onboarding](../experience/judge-onboarding.md).
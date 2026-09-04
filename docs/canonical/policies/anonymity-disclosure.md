---
type: Design Policy
title: Anonymity and Disclosure
description: Purpose-specific disclosure rules for Team identity, Judge evidence, and external representations.
status: stable
tags: [policy, privacy, disclosure]
sources:
  - resource: ../../001-concept-design/001-H-phase-consolidation-initial-concept-catalog.md
  - resource: ../../002-concept-specification/002-B-identity-participation-access-specifications.md
  - resource: ../../002-concept-specification/002-H-export-print-operational-continuity-external-representations.md
  - resource: ../../003-conceptual-ux-architecture/003-J-phase-consolidation-ux-architecture-exit-review.md
---

# Canonical contract

MUDAC provides controlled identity disclosure, not absolute real-world anonymity.

During blinded judging, the Judge-facing Team representation is [Alias](../concepts/alias.md) + Division. Institution/admin identity and optional Team Name are hidden by default. Team attributes require explicit audience/lifecycle disclosure classification.

Judges see their own Scorecards/Notes while ordinary Access remains active, but not peer Scorecards/Notes, live Team Aggregate, Coverage, Rank, or standings.

Representation profiles such as Judge-safe, Organizer-sensitive, Ceremony-safe, and Public are purpose-specific. Organizer visibility does not imply inclusion in an Export/public artifact.

Disclosure rules apply to views, search, deep links, QR payloads, filenames/metadata, print, and publication—not only page bodies.
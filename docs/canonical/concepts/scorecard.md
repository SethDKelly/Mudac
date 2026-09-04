---
type: Design Concept
title: Scorecard
description: One Judge's independent evaluation for one Judging Encounter under one exact Rubric Version.
status: stable
tags: [concept, judging, evidence]
sources:
  - resource: ../../001-concept-design/001-H-phase-consolidation-initial-concept-catalog.md
  - resource: ../../002-concept-specification/002-D-rubric-criterion-scorecard-notes-specifications.md
  - resource: ../../002-concept-specification/002-E-versioning-provenance-correction-authority-preservation.md
  - resource: ../../002-concept-specification/002-I-phase-consolidation-specification-exit-review.md
---

# Purpose

Capture one evaluator's independent judgment within one [Judging Encounter](judging-encounter.md).

# Canonical contract

Logical identity is one Judge Participation × one Encounter. The Scorecard owns criterion responses, Criterion/overall Notes, Judge attribution, Encounter basis, exact [Rubric](rubric.md) Version, and Draft/Finalized/amendment state.

`Draft → Finalized v1 → Amendment Draft → Finalized v2 ...`

A complete Draft is still non-authoritative. While an Amendment Draft exists, the prior Finalized Version remains authoritative. A successor Version replaces authority without adding another unit of evaluation weight.

# Authority boundary

The Judge remains semantic evaluation author. Organizer capture of paper does not transfer judgment authorship, and ordinary Organizer authority cannot edit an electronic evaluation as if authored by the Judge.

Structural identity such as author, Team/Encounter basis, or Rubric basis cannot be changed through ordinary amendment.

See [One Logical Scorecard](../invariants/one-logical-scorecard.md), [Judge Independence](../invariants/judge-independence.md), [Versioning](versioning.md), and [Correction & Authority](../policies/correction-authority.md).
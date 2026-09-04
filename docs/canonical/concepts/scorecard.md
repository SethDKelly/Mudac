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

Capture one evaluator's independent judgment within one [Judging Encounter](judging-encounter.md), under one exact [Rubric](rubric.md) Version.

Logical uniqueness and evaluation weight are owned by [INV-002](../invariants/one-logical-scorecard.md#inv-002). Judge semantic authorship is owned by [INV-004](../invariants/organizer-not-judge-author.md#inv-004).

The Scorecard owns criterion responses, Criterion/overall Notes, Judge attribution, Encounter basis, Rubric-Version basis, and Draft/Finalized/amendment state.

<a id="sc-001"></a>
## SC-001 — Draft is non-authoritative

A Scorecard Draft may be complete enough for Finalization while remaining non-authoritative. Only explicit successful Finalization establishes an authoritative Scorecard Version.

<a id="sc-002"></a>
## SC-002 — Amendment preserves prior authority until successor Finalization

Beginning an Amendment creates an Amendment Draft without displacing the current Finalized Version. The prior Version remains authoritative until the amendment is explicitly Finalized; the successor then becomes current under [Versioning](versioning.md).

Successor Versions do not create additional evaluation weight; that cross-cutting rule remains [INV-002](../invariants/one-logical-scorecard.md#inv-002).

<a id="sc-003"></a>
## SC-003 — Structural Scorecard identity is not amended

Ordinary amendment may change Judge-authored evaluation content such as Criterion responses and Notes, but it cannot silently change semantic author, Team/Encounter basis, or Rubric-Version basis. Structural errors require the explicit correction/invalidation paths in [Correction & Authority](../policies/correction-authority.md).

See [Judge Independence](../invariants/judge-independence.md#inv-001).
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
  - resource: ../../007-design-refinement/007-B-concept-completeness-independence-genericity-audit.md
---

# Purpose

Capture one evaluator's independent judgment within one [Judging Encounter](judging-encounter.md), under one exact [Rubric](rubric.md) Version.

# State

Scorecard owns one stable logical identity, Judge Participation/semantic author, Encounter basis, fixed Rubric-Version basis, working criterion responses and Notes, the current authoritative response Version when one exists, and amendment-Draft state when one exists.

`Not Started` is an Encounter evaluation obligation without Scorecard work, not a Scorecard lifecycle state.

# Actions

Conceptual actions are `start`, `setCriterionScore`, `clearCriterionScore`, `setCriterionNote`, `clearCriterionNote`, `setOverallNote`, `clearOverallNote`, `finalize`, `beginAmendment`, `abandonAmendment`, and `finalizeAmendment`.

Draft persistence/autosave is not itself a user-significant domain action.

# Operational Principle

An effective Judge participant begins one logical Scorecard for an Encounter using the exact applicable Rubric Version, forms judgment incrementally in a non-authoritative Draft, and explicitly Finalizes the complete evaluation. A later legitimate author correction begins an Amendment Draft while the prior finalized Version remains authoritative; finalizing the amendment creates a successor authoritative Version without creating another Judge vote.

Logical uniqueness and evaluation weight are owned by [INV-002](../invariants/one-logical-scorecard.md#inv-002). Judge semantic authorship is owned by [INV-004](../invariants/organizer-not-judge-author.md#inv-004).

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

# Boundaries

Scorecard does not decide who participates in an Encounter, who has Access, how its authoritative Versions are historically preserved, or how multiple evaluations are aggregated/ranked. Paper/electronic capture shares this same Concept; capture channel belongs to [Provenance](provenance.md).

See [Judge Independence](../invariants/judge-independence.md#inv-001).
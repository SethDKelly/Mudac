---
type: Design Concept
title: Export
description: Stable audience-specific external representation tied to identified source state.
status: stable
tags: [concept, export, representation]
sources:
  - resource: ../../001-concept-design/001-H-phase-consolidation-initial-concept-catalog.md
  - resource: ../../002-concept-specification/002-H-export-print-operational-continuity-external-representations.md
  - resource: ../../002-concept-specification/002-I-phase-consolidation-specification-exit-review.md
  - resource: ../../007-design-refinement/007-B-concept-completeness-independence-genericity-audit.md
  - resource: ../../007-design-refinement/007-D-temporal-state-correction-invalidation-supersession-historical-truth-closure.md
---

# Purpose

Produce a stable external representation of identified source information for a declared purpose and audience/disclosure profile.

# State

Export owns stable representation identity, exact source subject/Version/revision/basis, representation purpose/profile, intended audience/disclosure class, format, generation time, generated representation/artifact reference, and representation currency/status such as Current, Affected, Stale, Superseded, or Retired from ordinary use.

Currency is about the Export's relationship to its bound/current source basis; it is distinct from whether a [Publication](publication.md) of that Export is currently distributed.

# Actions

Conceptual actions are `request`, `validateDisclosure`, `generate`, `retrieve`, `regenerateFromCurrentSource`, and `retireFromOrdinaryUse`.

Regeneration from changed source state creates another representation rather than rewriting an operationally meaningful historical Export.

# Operational Principle

An Organizer chooses information to externalize. The application resolves the exact source basis, purpose, and audience/disclosure profile; validates the representation contract; generates a stable representation; and preserves enough identity to explain what the representation means later. If the source changes, the earlier Export remains attributable to its original basis and may become Affected or Stale; a new Export represents the newer source. Deliberate distribution/public release is then handled by [Publication](publication.md), not by generation itself.

<a id="export-001"></a>
## EXPORT-001 — Export represents source truth; it does not replace it

An Export is tied to identified source Version/revision, purpose, and audience/disclosure profile. It may produce paper, files, encoded identifiers, or other artifacts without becoming the authoritative source it represents.

An Export may later be Current, Affected, Stale, Superseded, or Retired from ordinary use while remaining historically attributable to its original source basis. Source correction never silently rewrites that basis.

<a id="export-002"></a>
## EXPORT-002 — Generation and publication are distinct

Generating an Export does not itself publish or release it. External release is a deliberate [Publication](publication.md) action under the relevant audience/disclosure contract.

The broader Finalization/publication separation is owned by [INV-007](../invariants/official-not-automatically-public.md#inv-007). Audience disclosure is governed by [DISC-002](../policies/anonymity-disclosure.md#disc-002). Temporal currency semantics are owned by [Temporal Truth, Correction & Historical Authority](../synchronizations/temporal-truth-correction.md).

# Boundaries

Export does not own its source semantics, Access, or the authoritative decision to distribute/release a representation. PDF, QR, barcode, file layout, and immutable byte-storage mechanics are representations/implementation mechanisms rather than Concepts.

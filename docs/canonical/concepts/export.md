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
---

# Purpose

Produce a stable external representation of identified authoritative information for distribution, printing, or publication.

<a id="export-001"></a>
## EXPORT-001 — Export represents source truth; it does not replace it

An Export is tied to identified source Version/revision, purpose, and audience/disclosure profile. It may produce paper, files, encoded identifiers, or publication artifacts without becoming the authoritative source it represents.

An Export may later be Current, Stale, Superseded, Affected, or withdrawn from current distribution while remaining historically attributable to its source.

<a id="export-002"></a>
## EXPORT-002 — Generation and publication are distinct

Generating an Export does not itself publish or release it. External release remains a deliberate operation under the relevant audience/disclosure contract.

The broader Finalization/publication separation is owned by [INV-007](../invariants/official-not-automatically-public.md#inv-007). Audience disclosure is governed by [DISC-002](../policies/anonymity-disclosure.md#disc-002).

# Boundaries

PDF, QR, barcode, and similar encodings are representations/mechanisms, not Concepts. Possession of an exported identifier does not grant authority.
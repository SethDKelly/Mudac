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

# Canonical contract

Export is tied to a source Version/revision, purpose, and audience/disclosure profile. It may produce paper, files, encoded identifiers, or publication artifacts without becoming source truth.

An Export may later be Current, Stale, Superseded, Affected, or withdrawn from current distribution while remaining historically attributable to the source it represented.

Generation and publication are distinct operations.

# Boundaries

PDF, QR, barcode, and similar encodings are representations/mechanisms, not Concepts. Possession of an exported identifier does not grant authority.

See [Anonymity & Disclosure](../policies/anonymity-disclosure.md), [Official Outcome Revision](../mechanisms/official-outcome-revision.md), and [Paper, Export & Publication](../experience/paper-export-publication.md).
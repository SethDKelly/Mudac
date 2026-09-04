---
type: Design Concept
title: Versioning
description: Preservation of successive authoritative states without erasing history.
status: stable
tags: [concept, versioning, authority]
sources:
  - resource: ../../001-concept-design/001-H-phase-consolidation-initial-concept-catalog.md
  - resource: ../../002-concept-specification/002-E-versioning-provenance-correction-authority-preservation.md
  - resource: ../../002-concept-specification/002-I-phase-consolidation-specification-exit-review.md
---

# Purpose

Preserve successive authoritative states of something that may legitimately change over time.

# Canonical contract

Committed Versions are immutable historical snapshots. One Version may be current authoritative for a lineage while prior Versions remain addressable.

Working Drafts are not authoritative Versions. Supersession means a newer Version represents the same logical valid subject; invalidation means retained evidence is no longer eligible for official use.

Primary uses include Rubric versions and Scorecard amendments.

# Boundaries

Versioning answers **what authoritative states existed**. [Provenance](provenance.md) answers **how, why, when, and through whose authority those states arose**.

See [Correction & Authority](../policies/correction-authority.md).
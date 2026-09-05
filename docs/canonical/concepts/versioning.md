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
  - resource: ../../007-design-refinement/007-B-concept-completeness-independence-genericity-audit.md
---

# Purpose

Preserve successive authoritative states of something that may legitimately change over time.

# State

Versioning owns a stable subject/lineage reference, immutable committed Version identities and snapshots, predecessor/sequence relationships, and at most one current authoritative committed Version for a linear lineage.

Working Drafts are not committed Versions.

# Actions

Conceptual actions are `initializeLineage`, `commitInitialVersion`, `commitSuccessor` against the expected current Version, `currentVersion`, `versionByIdentity`, `history`, and `compare`.

A committed Version must be reconstructible as a complete authoritative state even if storage internally uses deltas.

# Operational Principle

A user works with concept-owned Draft state. When the owning concept establishes that state as authoritative, Versioning commits an immutable Version. A later legitimate correction begins from the current authoritative state and commits a successor only if the expected current Version still matches. Earlier Versions remain addressable and unchanged.

# Canonical contract

Committed Versions are immutable historical snapshots. One Version may be current authoritative for a lineage while prior Versions remain addressable.

Supersession means a newer Version represents the same logical valid subject; invalidation means retained evidence is no longer eligible for official use.

Primary confirmed uses include Rubric Versions and Scorecard amendments.

# Boundaries

Versioning answers **what authoritative states existed**. [Provenance](provenance.md) answers **how, why, when, and through whose authority those states arose**. Versioning does not decide who may revise or what downstream calculations change.

See [Correction & Authority](../policies/correction-authority.md).
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
  - resource: ../../007-design-refinement/007-D-temporal-state-correction-invalidation-supersession-historical-truth-closure.md
---

# Purpose

Preserve successive authoritative states of something that may legitimately change over time.

# State

Versioning owns a stable subject/lineage reference, immutable committed Version identities and snapshots, predecessor/sequence relationships, and at most one **eligible current authoritative Version** for a linear lineage.

A lineage may temporarily have no eligible current authoritative Version when its latest committed authority is invalidated and no legitimate successor has yet been established. Invalidated or superseded Versions remain retained and addressable as history.

Working Drafts are not committed Versions.

# Actions

Conceptual actions are `initializeLineage`, `commitInitialVersion`, `commitSuccessor` against the expected current Version, `currentVersion`, `versionByIdentity`, `history`, and `compare`.

A committed Version must be reconstructible as a complete authoritative state even if storage internally uses deltas.

# Operational Principle

A user works with concept-owned Draft state. When the owning concept establishes that state as authoritative, Versioning commits an immutable Version. A later legitimate correction begins from the current authoritative state and commits a successor only if the expected current Version still matches. Earlier Versions remain addressable and unchanged.

# Canonical contract

Committed Versions are immutable historical snapshots.

**Supersession** means an explicit successor Version becomes current for the same logical subject/lineage; the predecessor remains valid historical authority.

**Invalidation** means a retained Version/subject is no longer eligible for the relevant authoritative purpose. Invalidation does not imply that a successor exists and does not silently reactivate an older predecessor.

**Replacement** of a structurally invalid subject/occurrence is not Version supersession when the replacement has a distinct logical identity. For example, a replacement Judging Encounter is a new occurrence rather than a new Version of the invalidated Encounter.

Primary confirmed uses include Rubric Versions and Scorecard amendments.

# Boundaries

Versioning answers **what authoritative states existed**. [Provenance](provenance.md) answers **how, why, when, and through whose authority those states arose**. Versioning does not decide who may revise, whether a Version should be invalidated, or what downstream calculations change.

Temporal vocabulary and the no-silent-fallback rule are owned by [Temporal Truth, Correction & Historical Authority](../synchronizations/temporal-truth-correction.md).

See [Correction & Authority](../policies/correction-authority.md).

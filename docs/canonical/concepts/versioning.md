---
type: Design Concept
title: Versioning
description: Preservation of successive authoritative states, eligibility, invalidation, and current lineage without erasing history.
status: stable
tags: [concept, versioning, authority, history]
sources:
  - resource: ../../002-concept-specification/002-E-versioning-provenance-correction-authority-preservation.md
  - resource: ../../007-design-refinement/007-D-temporal-state-correction-invalidation-supersession-historical-truth-closure.md
  - resource: ../../010-project-purpose-candidate-specification-modularity/010-G-completeness-independence-genericity-for-boundary-audit.md
  - resource: ../../010-project-purpose-candidate-specification-modularity/010-H-concept-boundary-convergence-respecification-canonical-reconciliation.md
generated: { by: openai/gpt-5.6-sol, at: 2026-09-12T03:12:00Z }
---

# Purpose

Preserve successive authoritative states of a subject that may legitimately change over time while retaining immutable history and representing which committed state, if any, is currently eligible authority.

# Abstract parameters

Conceptually:

`Versioning<Subject, Snapshot>`

Versioning requires subject identity and complete authoritative snapshots. It does not require the domain semantics of the subject being versioned.

# State

Versioning owns:

- stable subject/lineage identity;
- immutable committed Version identities and complete reconstructible Snapshots;
- predecessor/sequence relationships;
- eligibility/validity of each committed Version for the lineage's authoritative purpose;
- at most one current eligible authoritative Version for a linear lineage;
- retained superseded/invalidated history.

Working Drafts are not committed Versions.

A lineage may have **no current eligible authoritative Version** after invalidation when no legitimate successor has yet been established.

# Actions and queries

Conceptual actions are:

- `initializeLineage`;
- `commitInitialVersion`;
- `commitSuccessor(expectedCurrent, snapshot)`;
- `invalidateVersion(version, reasonRef)`.

Conceptual queries are:

- `currentEligibleVersion`;
- `isEligible(version)`;
- `versionByIdentity`;
- `history`;
- `compare`.

Committing a successor against an expected current Version protects semantic currentness. Concrete compare-and-swap realization is not prescribed here.

# Operational Principle

A subject establishes authoritative state and Versioning commits a complete immutable snapshot. A later legitimate change commits a successor against the expected current eligible Version; the predecessor remains historical authority and becomes Superseded. If a committed Version later becomes ineligible for the authoritative purpose, an authorized caller may invalidate it. The invalidated Version remains retained and addressable, and the lineage reports no current eligible Version unless a legitimate successor exists. Older predecessors are never silently revived.

# Canonical contract

**Superseded** means an explicit successor became current for the same logical lineage. The predecessor remains valid historical authority.

**Invalidated** means a retained Version is no longer eligible for the relevant authoritative purpose. Invalidation does not imply a successor and never silently selects an older predecessor as current.

**Replacement** of a structurally invalid distinct subject is not Version supersession; replacement belongs to the owning domain Concept.

# Boundaries

Versioning answers **what authoritative states existed and which committed state is eligible/current**.

[Provenance](provenance.md) answers **how, why, from what source, and through whose represented authority state arose**.

Versioning does not decide whether a domain correction is legitimate, who may authorize invalidation, or which downstream calculations/representations are affected.

See [Temporal Truth, Correction & Historical Authority](../synchronizations/temporal-truth-correction.md) and [Correction & Authority](../policies/correction-authority.md).
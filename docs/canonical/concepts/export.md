---
type: Design Concept
title: Export
description: Stable external representation of an identified source basis for a declared representation purpose and audience profile.
status: stable
tags: [concept, export, representation, currency]
sources:
  - resource: ../../002-concept-specification/002-H-export-print-operational-continuity-external-representations.md
  - resource: ../../007-design-refinement/007-D-temporal-state-correction-invalidation-supersession-historical-truth-closure.md
  - resource: ../../010-project-purpose-candidate-specification-modularity/010-G-completeness-independence-genericity-for-boundary-audit.md
  - resource: ../../010-project-purpose-candidate-specification-modularity/010-H-concept-boundary-convergence-respecification-canonical-reconciliation.md
  - resource: ../../011-concept-composition-synchronization/011-H-export-publication-representation-currency-release-composition.md
generated: { by: openai/gpt-5.6-sol, at: 2026-09-14T16:49:00-05:00 }
---

# Purpose

Produce and preserve a stable external representation of identified source information for a declared purpose and audience/disclosure profile, while keeping the representation's relationship to source currentness explicit.

# Abstract parameters

Conceptually:

`Export<SourceBasis, RepresentationProfile, AudienceProfile>`

`SourceBasis` is an identified supplied source state. Export does not need the source Concept's private semantics.

# State

Export owns:

- stable representation identity;
- exact SourceBasis;
- RepresentationProfile/purpose;
- intended AudienceProfile/disclosure class;
- format/representation kind where semantically relevant;
- generation time;
- generated representation/artifact reference;
- currency such as `Current`, `Affected`, `Stale`, `Superseded`, or `Retired`;
- optional reason/successor reference supporting a currency transition.

Currency is about the representation's relationship to source meaning/currentness. It is distinct from whether the representation has been distributed through [Publication](publication.md).

# Actions and queries

Conceptual actions are `request`, `validateRepresentation`, `generate`, `markAffected`, `markStale`, `supersedeBy`, and `retireFromOrdinaryUse`.

Conceptual queries include `retrieve`, `sourceBasis`, `currency`, `isCurrent`, `successor`, and representation history.

Generating another representation from newer source state creates another Export rather than rewriting an operationally meaningful historical representation.

## `validateRepresentation`

`validateRepresentation` checks semantic fidelity, purpose/audience compatibility and applicable disclosure/currentness constraints for the Export's **unchanged exact SourceBasis**.

It is also the owner-safe revalidation action for an `Affected` Export. Revalidation may reconfirm that same Export as `Current` only when its unchanged SourceBasis, represented content, declared purpose and AudienceProfile remain legitimately applicable for the intended current use.

If current use instead requires newer/corrected source state, `validateRepresentation` cannot rewrite the existing Export. A new Export must be generated from the new SourceBasis.

## Currency distinctions

- `Current` — representation remains truthful/applicable for its intended current use against its bound SourceBasis and representation contract.
- `Affected` — a material dependency changed and review/reconfirmation is required; incorrectness is not yet established.
- `Stale` — representation is known not to reflect the applicable current basis for its intended ordinary current use, even though it may remain historically faithful to its bound SourceBasis.
- `Superseded` — a distinct successor Export has explicitly replaced it for a comparable ordinary use.
- `Retired` — representation remains historical but has been removed from ordinary use.

These currency meanings never substitute for Publication distribution state.

# Operational Principle

An actor selects information to externalize and supplies an exact SourceBasis plus purpose/audience profiles. Export validates the representation contract and creates a stable representation tied to that basis. If later source change means the representation requires review, Export can become Affected; revalidation may reconfirm Current only without changing the bound source, while a known current-use mismatch becomes Stale. A replacement representation of newer/corrected source is a distinct Export and may explicitly supersede the predecessor. The old Export remains attributable to what it represented when generated. Deliberate release remains a separate Publication decision.

<a id="export-001"></a>
## EXPORT-001 — Export represents source authority; it never promotes it

Formatting, summarizing, redacting, or rendering supplied source information must not make that source appear more authoritative, complete, eligible, current, or official than the identified SourceBasis actually is.

<a id="export-002"></a>
## EXPORT-002 — Currency and distribution are separate

Source-currentness transitions do not themselves publish, withdraw, or retarget a representation. Publication owns distribution authority.

<a id="export-003"></a>
## EXPORT-003 — Historical basis is stable

Source correction never silently rewrites the historical SourceBasis of an already meaningful Export. Replacement uses a new Export and explicit supersession relation where appropriate. An Affected Export may return to Current only by validating that the unchanged exact SourceBasis and representation contract remain applicable for the intended current use; revalidation never changes historical SourceBasis or represented content into newer source truth.

# MUDAC composition binding

MUDAC may export competition setup, judging material, calculated/provisional information, or an [Outcome Declaration](outcome-declaration.md). Application synchronization/policy decides when a source change warrants Affected/Stale/Superseded transitions and which disclosure profile is legitimate.

Current MUDAC composition is [External Representation, Currency & Publication Release Composition](../synchronizations/external-representation-publication-release.md).

# Boundaries

Export does not own source semantics, Access decisions, Competition/Outcome authority, or deliberate release. PDF, QR, barcode, file layout, byte storage and transport are realization mechanisms rather than Concept identity.
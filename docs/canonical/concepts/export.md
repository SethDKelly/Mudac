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
generated: { by: openai/gpt-5.6-sol, at: 2026-09-12T03:12:00Z }
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

# Operational Principle

An actor selects information to externalize and supplies an exact SourceBasis plus purpose/audience profiles. Export validates the representation contract and creates a stable representation tied to that basis. If later source change means the representation requires review, Export can become Affected; if it is known not to reflect the applicable current basis, it can become Stale; a replacement representation may explicitly supersede it. The old Export remains attributable to what it represented when generated. Deliberate release remains a separate Publication decision.

<a id="export-001"></a>
## EXPORT-001 — Export represents source authority; it never promotes it

Formatting, summarizing, redacting, or rendering supplied source information must not make that source appear more authoritative, complete, eligible, current, or official than the identified SourceBasis actually is.

<a id="export-002"></a>
## EXPORT-002 — Currency and distribution are separate

Source-currentness transitions do not themselves publish, withdraw, or retarget a representation. Publication owns distribution authority.

<a id="export-003"></a>
## EXPORT-003 — Historical basis is stable

Source correction never silently rewrites the historical SourceBasis of an already meaningful Export. Replacement uses a new Export and explicit supersession relation where appropriate.

# MUDAC composition binding

MUDAC may export competition setup, judging material, calculated/provisional information, or an [Outcome Declaration](outcome-declaration.md). Application synchronization/policy decides when a source change warrants Affected/Stale/Superseded transitions and which disclosure profile is legitimate.

# Boundaries

Export does not own source semantics, Access decisions, Competition/Outcome authority, or deliberate release. PDF, QR, barcode, file layout, byte storage and transport are realization mechanisms rather than Concept identity.
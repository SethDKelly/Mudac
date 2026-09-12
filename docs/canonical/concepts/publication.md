---
type: Design Concept
title: Publication
description: Deliberate release of an identified Representation to a declared Audience/Channel under explicit publishing authority.
status: stable
tags: [concept, publication, disclosure, representation]
sources:
  - resource: ../../002-concept-specification/002-H-export-print-operational-continuity-external-representations.md
  - resource: ../../010-project-purpose-candidate-specification-modularity/010-G-completeness-independence-genericity-for-boundary-audit.md
  - resource: ../../010-project-purpose-candidate-specification-modularity/010-H-concept-boundary-convergence-respecification-canonical-reconciliation.md
generated: { by: openai/gpt-5.6-sol, at: 2026-09-12T03:12:00Z }
---

# Purpose

Deliberately make an identified Representation available to a declared Audience or Channel while preserving what was released, when, and under whose publishing authority.

# Abstract parameters

Conceptually:

`Publication<Representation, Audience, Channel, PublishingAuthority>`

Publication requires a supplied Representation identity/content contract; it does not require Export internals.

# State

Publication owns stable Publication identity, exact Representation, Audience, Channel/destination, PublishingAuthority, publication time, current distribution state, and predecessor/successor relation where a later release supersedes an earlier one.

Distribution states include `Published`, `Withdrawn`, and `Superseded`. Distribution state is independent from the source/currentness of the supplied Representation.

# Actions and queries

Conceptual actions are `publish`, `withdraw`, and `supersedeWith` a successor Publication based on an explicitly selected successor Representation.

Queries include current distribution state, representation identity, audience/channel, predecessor/successor, and publication history.

# Operational Principle

An authorized actor selects an exact Representation, intended Audience, and Channel and explicitly publishes it. The Publication remains historically attributable even if source information later changes. Withdrawal ends current distribution without erasing that release occurred. If correction requires a replacement release, the application supplies a successor Representation and an authorized actor explicitly creates a successor Publication rather than retargeting the prior release.

<a id="pub-001"></a>
## PUB-001 — Publication prerequisites follow representation purpose and source authority

Publication does not decide whether supplied information is semantically official, current, complete, or appropriate for disclosure. The application must satisfy the applicable source-authority and disclosure prerequisites before invoking publication. Publication then owns only the deliberate release and retained distribution history.

Publication cannot promote supplied information into greater semantic authority merely by labeling or distributing it.

Source correction, representation regeneration, or Export-currentness change never silently retargets an existing Publication.

Possession of a URL, QR code, file, or transport reference is not itself Publication authority or Access permission.

# MUDAC composition binding

MUDAC normally supplies an [Export](export.md) as the Representation. Whether all MUDAC product variants containing Publication must also contain Export is an inclusion-dependence question for Phase 012, not intrinsic Publication semantics.

# Boundaries

Publication is distinct from Competition Finalization, [Outcome Declaration](outcome-declaration.md), Export generation/currentness, Access, and transport/delivery infrastructure.

See [Official Does Not Automatically Mean Public](../invariants/official-not-automatically-public.md#inv-007).
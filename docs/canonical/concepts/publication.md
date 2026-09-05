---
type: Design Concept
title: Publication
description: Deliberate distribution or public release of an identified external representation to a declared audience or channel.
status: stable
tags: [concept, publication, disclosure, representation]
sources:
  - resource: ../../002-concept-specification/002-G-awards-reconciliation-finalization-official-outcomes.md
  - resource: ../../002-concept-specification/002-H-export-print-operational-continuity-external-representations.md
  - resource: ../../003-conceptual-ux-architecture/003-G-paper-capture-export-print-publication-experience.md
  - resource: ../../007-design-refinement/007-B-concept-completeness-independence-genericity-audit.md
  - resource: ../../007-design-refinement/007-D-temporal-state-correction-invalidation-supersession-historical-truth-closure.md
---

# Purpose

Deliberately make an identified [Export](export.md) representation available to a declared audience or distribution channel while preserving what was released, when, and under whose authority.

# State

Publication owns stable Publication identity, the exact Export/representation being released, inherited source/disclosure basis, intended audience, channel/destination, publishing actor/authority, publication time, current distribution state, and predecessor/successor relationship when later release supersedes an earlier one.

An established Publication may be `Published`, `Withdrawn`, or `Superseded`. Those distribution states are independent from dependency currency: a Publication may remain Published while its bound Export/source basis is Affected and awaiting explicit withdrawal or successor release.

Preparation/preview before release remains Export/experience state rather than a Published state.

# Actions

Conceptual actions are `publish`, `withdraw`, and `supersedeWith` a successor Publication based on an explicitly selected successor Export.

A corrected source or newly generated Export never silently retargets an existing Publication.

# Operational Principle

An Organizer generates and validates an Export appropriate to a particular audience. When the representation should actually be released, an authorized actor explicitly publishes that exact representation to the intended channel. The Publication remains historically attributable even if its source later changes or it is withdrawn. If correction requires a replacement, the application generates a successor Export and explicitly creates a successor Publication while preserving the earlier release as historical.

# Boundaries

Publication is distinct from:

- Competition Finalization — official internal outcome does not automatically disclose it;
- Export generation — representation existence does not mean distribution;
- source currency — a released representation can become Affected/Stale without changing the historical fact of Publication;
- delivery transport — URL, QR, CDN propagation, print job, or message delivery does not by itself establish Publication authority;
- Access — possession of a reference does not grant permission to private/unpublished material.

Artifact/byte identity and delivery infrastructure remain architecture/implementation mechanisms. Publication owns the deliberate domain act and retained distribution state.

See [Official Does Not Automatically Mean Public](../invariants/official-not-automatically-public.md#inv-007), [Anonymity & Disclosure](../policies/anonymity-disclosure.md), [Temporal Truth, Correction & Historical Authority](../synchronizations/temporal-truth-correction.md), and [Paper Capture, Export and Publication](../experience/paper-export-publication.md).

---
type: Design Policy
title: Anonymity and Disclosure
description: Purpose-specific disclosure rules for Team identity, Judge evidence, and external representations.
status: stable
tags: [policy, privacy, disclosure]
sources:
  - resource: ../../001-concept-design/001-H-phase-consolidation-initial-concept-catalog.md
  - resource: ../../002-concept-specification/002-B-identity-participation-access-specifications.md
  - resource: ../../002-concept-specification/002-H-export-print-operational-continuity-external-representations.md
  - resource: ../../003-conceptual-ux-architecture/003-J-phase-consolidation-ux-architecture-exit-review.md
  - resource: ../../007-design-refinement/007-E-end-to-end-scenario-exception-failure-adversarial-authority-validation.md
---

# Canonical contract

MUDAC provides controlled identity disclosure, not absolute real-world anonymity.

<a id="disc-001"></a>
## DISC-001 — Blinded Judge Team identity

During blinded judging, the Judge-facing Team representation is [Alias](../concepts/alias.md) + Division. Institution/administrative identity and optional Team Name are hidden by default. Team attributes require explicit audience/lifecycle disclosure classification.

Peer-result non-disclosure during ordinary judging is owned by [INV-001 — Judge Independence](../invariants/judge-independence.md#inv-001), rather than restated here as a separate fairness rule.

<a id="disc-002"></a>
## DISC-002 — Disclosure is audience and purpose specific

Representation profiles such as Judge-safe, Organizer-sensitive, Ceremony-safe, and Public are purpose-specific. Organizer visibility does not imply inclusion in an Export or public artifact.

Disclosure rules apply to interactive views, search, deep links, QR payloads, filenames/metadata, print, and publication—not only page bodies.

A denied disclosure attempt creates no authority merely because a user possesses a URL, route, device, prior rendering, or other navigation artifact.

If protected information is actually exposed, later Access revocation can prevent further disclosure but cannot retroactively make the exposure not have happened. The occurrence must remain attributable enough for integrity/correction review. Material impact on blinded or independent evaluation is determined explicitly; it may require invalidating affected Encounter/evidence and establishing a replacement/rejudge, but exposure does not automatically invalidate unrelated evaluation and must not be erased through silent rewrite.

See [Access](../concepts/access.md#acc-001), [Correction & Authority](correction-authority.md), and [Export](../concepts/export.md#export-001).
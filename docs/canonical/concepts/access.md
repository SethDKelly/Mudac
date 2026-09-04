---
type: Design Concept
title: Access
description: Contextual permission and disclosure determined by principal, scope, resource, state, relationship, and time.
status: stable
tags: [concept, access, privacy]
sources:
  - resource: ../../001-concept-design/001-H-phase-consolidation-initial-concept-catalog.md
  - resource: ../../002-concept-specification/002-B-identity-participation-access-specifications.md
  - resource: ../../002-concept-specification/002-I-phase-consolidation-specification-exit-review.md
---

# Purpose

Permit or deny actions and information disclosure according to current context.

<a id="acc-001"></a>
## ACC-001 — Access is contextual

Access depends on Identity/Participation, role, scope, target resource, lifecycle state, relationship, purpose, and time. Identity or role alone is insufficient.

Ordinary Judge Access is limited to Judge-safe event context and the Judge's own evaluation work. At Event Completed, ordinary Judge private-evaluation Access expires while records remain retained. Post-event Judge correction uses narrow temporary reactivation for the specific authorized evaluation.

<a id="acc-002"></a>
## ACC-002 — Access does not transfer semantic authority

Access grants capability; it does not transfer semantic authorship or decision authority. Navigation, URLs, QR codes, and device possession never substitute for Access.

For the Judge-authorship consequence, see [INV-004](../invariants/organizer-not-judge-author.md#inv-004). See also [Anonymity & Disclosure](../policies/anonymity-disclosure.md).
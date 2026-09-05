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
  - resource: ../../007-design-refinement/007-B-concept-completeness-independence-genericity-audit.md
---

# Purpose

Permit or deny actions and information disclosure according to current context.

# State

Ordinary Access may be derived from Identity/Participation, capability, scope, target resource, lifecycle state, relationship, purpose, and time rather than persisted per action.

Where explicit exceptional grants are needed, Access owns principal/context, capability set, resource/scope, validity interval, status, and exceptional reason/purpose. Revocation/expiry changes capability without deleting the protected resource.

# Actions

Conceptual actions are `check`, `grant`, `temporarilyGrant`, `revoke`, and `expire`.

# Operational Principle

During live judging, current Judge context permits Judge-safe event information and the Judge's own evaluation work while denying peer evaluations, protected Team identity, and standings. When the event completes, ordinary private-evaluation Access expires while records remain retained. A legitimate later correction may reverify the Judge and establish a narrowly scoped temporary grant to the specific Scorecard rather than restoring broad history access.

<a id="acc-001"></a>
## ACC-001 — Access is contextual

Access depends on Identity/Participation, role, scope, target resource, lifecycle state, relationship, purpose, and time. Identity or role alone is insufficient.

Ordinary Judge Access is limited to Judge-safe event context and the Judge's own evaluation work. At Event Completed, ordinary Judge private-evaluation Access expires while records remain retained. Post-event Judge correction uses narrow temporary reactivation for the specific authorized evaluation.

<a id="acc-002"></a>
## ACC-002 — Access does not transfer semantic authority

Access grants capability; it does not transfer semantic authorship or decision authority. Navigation, URLs, QR codes, device possession, or authentication proof never substitute for the current Access decision.

# Boundaries

Access does not identify the human ([Identity](identity.md)), establish why they participate ([Participation](participation.md)), or transfer semantic authorship/decision authority.

For the Judge-authorship consequence, see [INV-004](../invariants/organizer-not-judge-author.md#inv-004). See also [Anonymity & Disclosure](../policies/anonymity-disclosure.md).
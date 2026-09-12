---
type: Design Concept
title: Access
description: Contextual capability and disclosure decision over a principal, resource, context facts, and decision rule.
status: stable
tags: [concept, access, privacy, authority]
sources:
  - resource: ../../002-concept-specification/002-B-identity-participation-access-specifications.md
  - resource: ../../010-project-purpose-candidate-specification-modularity/010-G-completeness-independence-genericity-for-boundary-audit.md
  - resource: ../../010-project-purpose-candidate-specification-modularity/010-H-concept-boundary-convergence-respecification-canonical-reconciliation.md
generated: { by: openai/gpt-5.6-sol, at: 2026-09-12T03:12:00Z }
---

# Purpose

Permit or deny actions and information disclosure according to supplied current context without transferring semantic authorship or decision authority.

# Abstract parameters

Conceptually:

`Access<Principal, Capability, Resource, ContextFacts, Rule>`

Access receives the facts needed for a decision. It does not need to understand the private semantics of Identity, Participation, Competition, Scorecard, or other peer Concepts.

# State

Ordinary Access may be derived rather than persisted. The conceptual decision input is:

- Principal;
- requested Capability;
- Resource/scope;
- supplied ContextFacts such as lifecycle, relationship, purpose, time, or capacity facts;
- the applicable decision Rule.

Where an explicit exceptional grant is meaningful, Access owns the grant identity/context, capability set, resource/scope, validity interval, status, reason/purpose, and revocation/expiry history.

# Actions and queries

Conceptual operations are `check`, `grant`, `temporarilyGrant`, `revoke`, and `expire`.

`check(principal, capability, resource, contextFacts, rule)` evaluates the supplied decision contract and returns the current permit/deny result plus any semantically meaningful reason/disclosure constraints required by that rule.

# Operational Principle

The application supplies the active principal/context facts and applicable access rule for a protected action or disclosure. Access evaluates that context rather than inferring authority from identity alone. Ordinary capability can change as time, lifecycle, role/capacity, relationship, or purpose changes. Exceptional grants may be established narrowly and later revoked/expired without deleting protected resources. Permission enables an action; it never changes who is the semantic author or which competition authority owns a decision.

<a id="acc-001"></a>
## ACC-001 — Access is contextual

Principal identity alone is insufficient. A decision may depend on scope, target resource, lifecycle/state facts, relationship, purpose, time, and current capacity facts supplied by the application.

<a id="acc-002"></a>
## ACC-002 — Access does not transfer semantic authority

Navigation, URL possession, QR codes, authentication proof, device possession, technical administration, support privilege, or break-glass capability cannot substitute for the semantic authority required by the protected domain action.

# MUDAC composition binding

MUDAC commonly supplies Identity/Participation-derived principal/capacity facts, Competition lifecycle facts, ownership relationships, and protected-resource context. For example, a Judge may receive access to the Judge's own evaluation work while peer Scorecards, protected Team identity, and standings remain denied; after event completion ordinary access can expire while retained records remain authoritative.

Those supplied facts remain owned by their source Concepts. Access owns only the contextual capability/disclosure decision and explicit exceptional-grant state.

# Boundaries

Access does not identify the human, establish Participation capacity, author Scorecards, confer Organizer/Judge authority, or own the protected resource's lifecycle.

See [Judge Independence](../invariants/judge-independence.md#inv-001), [Organizer Is Not Judge Author](../invariants/organizer-not-judge-author.md#inv-004), and [Anonymity & Disclosure](../policies/anonymity-disclosure.md).
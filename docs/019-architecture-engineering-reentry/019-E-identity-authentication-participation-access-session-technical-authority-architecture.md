---
type: Architecture Decision
title: 019-E — Identity, Authentication, Participation, Access, Session & Technical-Authority Architecture
description: "Resolves ADQ-004 by comparing provider-native authorization, self-hosted authentication, managed external authentication with browser bearer-session patterns, and a managed standards-compatible external IdP behind a MUDAC-owned identity/access adapter plus opaque first-party server session; accepts the latter while keeping provider choice and runtime configuration deferred."
status: stable
tags: [phase-019, architecture, adq-004, identity, authentication, participation, access, session, technical-authority]
sources:
  - resource: ../canonical/architecture/identity-access-authority.md
  - resource: ../canonical/architecture/identity-access-session.md
  - resource: ../canonical/architecture/architecture-drivers.md
  - resource: ../canonical/architecture/application-ownership-boundaries.md
  - resource: ../canonical/architecture/persistence-history-recovery.md
  - resource: ../canonical/concepts/identity.md
  - resource: ../canonical/concepts/participation.md
  - resource: ../canonical/concepts/access.md
  - resource: ../canonical/synchronizations/competition-participation-access.md
  - resource: ../canonical/experience/context-role-modes.md
  - resource: ../canonical/experience/judge-onboarding.md
  - resource: ../canonical/experience/accessibility-resilience.md
  - resource: ../canonical/invariants/organizer-not-judge-author.md
  - resource: ../canonical/invariants/truthful-authority-under-uncertainty.md
  - resource: ../routing/phase019_architecture_decision_control.json
generated: { by: openai/gpt-5.6-sol, at: 2026-09-22T09:23:00-05:00 }
---

# Purpose

019-E resolves ADQ-004.

It establishes how external authentication proof becomes a secure MUDAC interaction context without collapsing:

~~~text
authentication
!= Identity
!= Participation
!= Access
!= session continuity
!= semantic authorship
!= technical/operator authority
~~~

# 1. Entry state

~~~text
Phase 019                       ACTIVE
019-A/B/C/D                     COMPLETE
019-E                           NEXT ELIGIBLE / USER AUTHORIZED

ADQ-001                         ACCEPTED
ADQ-002                         ACCEPTED
ADQ-003                         ACCEPTED
ADQ-004                         PLANNED
ADQ-005..010                    PLANNED

Q4 repairs complete             1 / 4
technical probes                0

accepted whole architecture     false
implementation packages         0
implementation execution        false
~~~

# 2. Decision

**ADQ-004 — ACCEPTED.**

Selected architecture:

> **Managed standards-compatible external authentication behind an application adapter, explicitly linked to stable MUDAC Identity; Competition-scoped Participation and contextual MUDAC-owned Access; opaque first-party server-controlled sessions; explicit multi-capacity isolation; bounded revocation/reverification/step-up; narrow exceptional grants; shared-device context clearing; and strict technical/operator separation from semantic authority.**

Current owner:

> docs/canonical/architecture/identity-access-authority.md

Stable rules:

> IAM-001 through IAM-018

# 3. Current semantic constraints

ADQ-004 preserves:

- ENG-004 — Identity, Participation, Access, authentication, authorship and technical privilege remain distinct;
- ENG-011 — security/disclosure controls protect semantic authority;
- ENG-012 — shared-device/accessibility/degraded operation preserves parity;
- ENG-015 — evidence strength matches claims;
- ENG-017 — historical architecture remains evidence;
- ACC-001 — Access is contextual;
- ACC-002 — Access does not transfer semantic authority;
- INV-004 — Organizer/support authority does not become Judge authorship;
- INV-010 — uncertainty cannot be promoted into authority;
- DRV-001/002/003/007/008/009/010/011;
- BND-002/004/005/006/009;
- PST-002/003/004/007/016.

# 4. Historical identity/session candidate

Input:

> docs/canonical/architecture/identity-access-session.md

Qualification:

~~~text
Q1 / Q2 / Q3
QUALIFIED_COMPARISON_INPUT
authority = suspended-candidate
semantic repair required = false
technology revalidation required = true
~~~

The candidate's strongest current-compatible ideas are:

- authentication proof is not Competition authority;
- stable provider-subject linkage to MUDAC Identity;
- explicit Competition-scoped Participation;
- current application-side Access checks;
- first-party opaque server session;
- multi-capacity isolation;
- narrow post-event correction grants;
- shared-device revocation/clearing;
- technical operator/break-glass separation;
- provider adapter portability.

019-E independently revalidated those principles.

The historical provider/runtime claim involving Cognito remains candidate-only and is not adopted here.

# 5. Alternatives

## Alternative A — Adopt historical Identity/Access/Session architecture unchanged

Strengths:

- strong semantic separation;
- explicit sessions/revocation;
- mature shared-device and technical-authority reasoning;
- prior AWS alignment.

Weaknesses:

- later historical material couples provider realization to Cognito;
- references old architecture owners;
- session/runtime details require fresh integration with current BND/PST decisions.

**Rejected as-is.**

Its provider-independent architecture is re-established under IAM-* current authority.

## Alternative B — Provider-native roles/groups/claims as application authorization

Pattern:

~~~text
external IdP
  → provider roles/groups/claims
  → direct MUDAC capability
~~~

Strengths:

- simple integration;
- fewer application authorization records;
- convenient provider administration.

Weaknesses:

- collapses authentication/infrastructure administration into Competition authority;
- does not naturally represent Competition-scoped Participation history;
- encourages stale token/claim authority;
- makes multi-capacity isolation and contextual Access harder;
- provider migration could rewrite application authority/history;
- conflicts directly with ACC-001/002 and ENG-004.

**Rejected.**

Provider claims may be integration input only.

## Alternative C — Self-hosted MUDAC credentials and authentication protocols

MUDAC would own password storage/reset, MFA/federation and authentication protocol behavior.

Strengths:

- maximum authentication control;
- minimal external provider dependence.

Weaknesses:

- materially higher credential-security and operational burden;
- creates substantial security surface unrelated to MUDAC's semantic purpose;
- no current requirement justifies implementing credential systems as domain infrastructure;
- increases recovery/abuse responsibilities.

**Rejected.**

MUDAC should own application Identity/authority, not password/security-protocol implementation.

## Alternative D — Managed external IdP with long-lived provider tokens directly used by browser/application authorization

Strengths:

- common SPA integration model;
- lower server session-state burden;
- provider-native token lifecycle.

Weaknesses:

- increases browser bearer-token exposure;
- encourages stale claims as application authority;
- makes immediate application revocation/currentness harder;
- risks coupling Access to provider token contents;
- complicates shared-device/privacy posture.

**Rejected for the core application session.**

Provider protocols may still be used behind the server/application adapter.

## Alternative E — Managed standards-compatible external IdP + MUDAC Identity/Participation/Access + first-party opaque session

Strengths:

- preserves semantic authority boundaries;
- provider credentials remain external authentication concerns;
- first-party session can be revoked independently;
- supports shared-device and replacement-device recovery;
- allows current Access checks on consequential operations;
- preserves provider portability;
- supports multi-capacity isolation;
- aligns with bounded modular-monolith architecture.

**Selected.**

# 6. Authentication boundary

The accepted chain is:

~~~text
external authentication proof
        ↓
provider adapter
        ↓
stable MUDAC Identity linkage
        ↓
selected Competition Participation
        ↓
first-party application session context
        ↓
fresh contextual Access
        ↓
resource-owner preconditions
        ↓
authorized protected action/disclosure
~~~

No arrow transfers semantic ownership to the previous layer.

# 7. Stable Identity linkage

Provider principal identity is linked explicitly to MUDAC Identity.

Mutable email or display name may assist recovery or human recognition but cannot silently merge Identities.

Historical authorship remains attached to MUDAC stable Identity even if:

- provider changes;
- email changes;
- credential is recovered;
- Identity becomes disabled;
- a new provider/federation is added later.

# 8. Participation and multi-capacity isolation

One Identity may have several Participations.

For PF-01:

~~~text
current Participation
  = Competition
  + capacity
  + current Participation state
~~~

Judge and Organizer capability sets never union.

Switching capacity selects a distinct already-legitimate Participation context and disclosure posture.

Protected data from the previous context must not leak into the destination context.

# 9. Access enforcement topology

Identity & Access owns current Identity, Participation and Access facts.

Resource-owning modules own final resource/lifecycle truth.

Therefore:

~~~text
Identity & Access
  establishes principal/context/capability decision

resource-owning module
  establishes resource/lifecycle preconditions

protected operation
  requires both where applicable
~~~

There is no detached universal permission service that can override natural semantic owners.

# 10. First-party session architecture

The browser holds an opaque session reference.

Server-controlled session state may retain:

- Identity reference;
- external-auth linkage reference;
- authentication/reverification time;
- selected Participation;
- session lifetime/revocation/security version.

Session state:

~~~text
improves continuity
!= Participation
!= Access
!= semantic authority
~~~

The exact session backing store is deferred.

No separate session service is required by architecture.

# 11. Revocation and stale authority

The architecture supports independent revocation of:

- session;
- provider credential linkage;
- exceptional Access grant;
- Participation-derived capability;
- technical break-glass context.

A technically valid browser session cannot extend a Participation or Access decision that is no longer current.

Consequential reads/actions re-evaluate current application authority.

# 12. Shared-device and device-replacement safety

Device possession is not authority.

After handoff, interruption or replacement:

~~~text
re-establish Identity
+ Participation/capacity
+ Competition
+ protected resource context
+ current Access
~~~

Private cached/session context belonging to the prior person/capacity is cleared, partitioned or inaccessible before protected interaction resumes.

The same stable Identity and same logical evaluation may be resumed after legitimate reauthentication.

# 13. Invitations and entry credentials

Invitation links, QR/event codes and deep links may route or enable bounded Participation claim workflows.

They do not establish authentication, Participation, Panel membership or Access by possession.

Camera-independent entry remains semantically required.

# 14. Step-up and reverification

Fresh or stronger authentication may be required when risk justifies it.

Possible cases include:

- account/provider linking;
- recovery;
- sensitive context change;
- post-event Judge correction;
- break-glass;
- later selected high-consequence Organizer action.

Step-up increases authentication assurance only.

MUDAC Access/resource authority is still independently evaluated.

# 15. Exceptional Access grants

Ordinary Access may be derived.

When an explicit exceptional grant is semantically meaningful, it is durable application state with:

- grant identity;
- principal/Participation;
- Competition/resource;
- capabilities;
- purpose/reason;
- start/end;
- current status;
- revocation/expiry history;
- attributable authorizer.

This supports narrow post-event or recovery authority without reopening broad live-event permissions.

# 16. Technical/operator authority

Infrastructure/security/support/database operation is not Competition Participation.

Technical actors cannot use operator privilege to silently become:

- Judge author;
- Organizer decision-maker;
- outcome authority;
- unrestricted disclosure authority.

Where break-glass is necessary, it is explicit, bounded, attributable and expiring.

Actor and represented authority remain distinct in meaningful Provenance.

# 17. Provider portability

MUDAC will use a managed standards-compatible provider behind an adapter.

This decision selects the **provider boundary**, not the provider.

019-E does not choose:

- Cognito;
- another named IdP;
- enterprise SSO/federation outside current PF-01 need;
- exact MFA method;
- exact secret-management implementation;
- provider-specific groups/role mapping.

019-J may compare concrete provider/runtime options using external/provider evidence.

# 18. Evidence

Acceptance evidence class:

> **DOCUMENTATION_REASONING**

No technical probe is required to establish the authority/session model.

Provider-specific security properties, token/session integration behavior, federation limitations or managed-service guarantees require later external/integration evidence before a concrete provider is accepted.

# 19. Reversibility and lock-in

This architecture intentionally minimizes provider lock-in:

- MUDAC Identity IDs are stable;
- Participation/Access live in application authority;
- provider claims do not become domain roles;
- browser session is application-owned;
- provider integration is adapter-mediated.

Provider replacement still requires account-link/reverification migration and careful session transition, but it does not require rewriting Competition authority history.

# 20. Residual uncertainty

Still open:

- concrete external identity provider;
- exact provider protocol/configuration;
- exact MFA/assurance policy;
- exact cookie/session lifetimes;
- exact session backing store;
- exact rate/abuse-control implementation;
- enterprise federation/SSO outside current PF-01;
- exact break-glass operational procedure;
- final secret-management system.

These belong primarily to ADQ-009 or Phase 020 configuration/implementation planning.

# 21. Scenario impact

ADQ-004 directly constrains:

- shared-device context handoff;
- stale Participation/Access/session state;
- adversarial request volume.

It also supplies identity/authority prerequisites for offline recovery, consequential command and correction scenarios.

# 22. Risk disposition

## ERI-02 — historical candidate mistaken for accepted architecture

**Controlled.**

Current authority is IAM-*; historical AUTH-* remains candidate evidence.

## ERI-03 — architecture emerges from executable/provider scaffold

**Controlled.**

No provider or existing auth package is selected by historical presence.

## ERI-09 — derived-authority leakage

**Materially reduced; carried to 019-K.**

Authentication, application Access, resource authority and technical privilege are now explicit distinct boundaries.

## Shared-device / stale-session risk

**Architecturally controlled; executable evidence remains later.**

IAM-006 through IAM-010 define the required behavior; browser/runtime proof belongs downstream.

# 23. Implementation boundary

After 019-E:

~~~text
accepted bounded decisions       4 / 10
Q4 repairs complete              1 / 4
technical probes                 0

accepted whole architecture      false

implementation packages          0
package derivation               false
implementation execution         false
~~~

G0 remains unsatisfied.

# 24. Exit decision

**019-E — COMPLETE — PASS.**

**ADQ-004 — ACCEPTED.**

Next eligible:

> **019-F — Interface, Command/Query, Transaction, Concurrency, Retry & Idempotency Architecture**

019-F is not automatically authorized.

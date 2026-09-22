---
type: Accepted Architecture Decision
title: Current Identity, Authentication, Participation, Access, Session & Technical-Authority Architecture
description: "Accepted ADQ-004 identity/security architecture for MUDAC: managed standards-compatible external authentication behind an application adapter, explicit linkage to stable MUDAC Identity, Competition-scoped Participation, contextual application-owned Access, opaque first-party server sessions, explicit multi-capacity isolation, reverification/step-up, revocation, shared-device safety, bounded exceptional grants and strict separation of technical/operator privilege from semantic authority."
status: stable
tags: [architecture, current, identity, authentication, participation, access, session, security, authority]
sources:
  - resource: architecture-drivers.md
  - resource: application-ownership-boundaries.md
  - resource: persistence-history-recovery.md
  - resource: identity-access-session.md
  - resource: ../concepts/identity.md
  - resource: ../concepts/participation.md
  - resource: ../concepts/access.md
  - resource: ../synchronizations/competition-participation-access.md
  - resource: ../experience/context-role-modes.md
  - resource: ../experience/judge-onboarding.md
  - resource: ../experience/accessibility-resilience.md
  - resource: ../experience/status-feedback-recovery.md
  - resource: ../invariants/organizer-not-judge-author.md
  - resource: ../invariants/truthful-authority-under-uncertainty.md
  - resource: ../governance/downstream-realization-obligations.md
  - resource: ../../019-architecture-engineering-reentry/019-E-identity-authentication-participation-access-session-technical-authority-architecture.md
generated: { by: openai/gpt-5.6-sol, at: 2026-09-22T09:15:00-05:00 }
---

# Authority

This document is **current accepted architecture authority for ADQ-004**.

It establishes the technical boundary among authentication, stable MUDAC Identity, Competition-scoped Participation, contextual Access, first-party application session, reverification, exceptional grants, shared-device recovery and technical/operator authority.

It does not select a concrete identity provider, provider tenant/configuration, final secret store, organization SSO features outside PF-01, or exact implementation library.

<a id="iam-001"></a>
## IAM-001 — Authentication proves principal control; MUDAC owns application identity and authority

A managed external authentication provider may establish or re-establish control of an external principal.

MUDAC remains authoritative for:

- stable Identity;
- Competition Participation;
- current Access;
- represented capacity/context;
- Judge authorship;
- Organizer authority;
- exceptional application grants;
- Competition and resource lifecycle authority.

Provider groups, roles or claims are never sufficient by themselves to establish MUDAC Competition authority.

<a id="iam-002"></a>
## IAM-002 — External authentication subjects link explicitly to durable MUDAC Identity

The application links a provider principal to MUDAC Identity using a stable provider/issuer + external-subject binding or equivalent stable provider identity.

It must not silently link or merge Identity using only:

- email;
- display name;
- role label;
- device;
- invitation possession.

Identity linking, provider replacement and account recovery preserve historical application Identity and authorship.

<a id="iam-003"></a>
## IAM-003 — Participation is Competition-scoped and never becomes a permanent account role

Authentication resolves Identity.

The application then resolves one or more current Competition Participations.

A prior Judge or Organizer Participation:

- does not become a permanent Identity role;
- does not automatically apply to another Competition;
- does not automatically restore Access after completion/withdrawal;
- does not imply current Panel/evaluation responsibility.

Where multiple Participations are legitimate, one active application context is explicitly selected.

<a id="iam-004"></a>
## IAM-004 — Capabilities never union across Participation contexts

A human may hold multiple Participations, including Judge and Organizer in the same Competition.

The application evaluates one explicit Participation/capacity context at a time for protected reads/actions.

Switching context:

- does not merge capability sets;
- does not mutate either Participation;
- changes applicable disclosure posture;
- requires protected views/actions to be re-evaluated under the destination context;
- preserves the actual Participation context in meaningful Provenance.

<a id="iam-005"></a>
## IAM-005 — Access is evaluated from current application authority at protected boundaries

Protected reads and state-changing actions use current application-side facts including as applicable:

- Identity status;
- active Participation;
- Competition scope/lifecycle;
- resource ownership/relationship;
- represented authority;
- current responsibility;
- purpose;
- time;
- exceptional grant/revocation;
- resource state;
- applicable disclosure rule.

UI visibility, route possession, cached role data, authentication token claims or session context do not substitute for current Access evaluation.

Resource-owning modules remain responsible for final lifecycle/resource preconditions.

<a id="iam-006"></a>
## IAM-006 — Browser continuity uses an opaque first-party server-controlled session

The core browser application uses an opaque first-party session identifier.

The browser holds only the session reference required for application continuity, in a production-protected cookie posture appropriate to the final runtime design.

Application session state remains server-controlled and revocable.

Long-lived provider access/refresh credentials are not application authorization state and are not stored in ordinary script-readable browser storage for the core MUDAC session.

<a id="iam-007"></a>
## IAM-007 — Session state is continuity and assurance evidence, not capability authority

A server session may retain:

- MUDAC Identity reference;
- provider/authentication linkage reference;
- authentication/reverification timestamps or assurance metadata;
- selected Participation/context reference;
- creation/last-use/absolute-expiry data;
- revocation/security-version data.

It may improve usability.

It cannot extend expired/revoked Participation or Access.

Consequential application decisions still evaluate current owner state.

<a id="iam-008"></a>
## IAM-008 — Sessions are bounded, revocable and replaceable without changing semantic Identity

The architecture supports:

- explicit logout;
- idle expiry;
- absolute expiry;
- administrative/security revocation;
- revocation after credential compromise;
- replacement-device reauthentication;
- session replacement/rotation;
- invalidation after material security events.

Session loss or revocation does not create a new MUDAC Identity or duplicate logical evaluation work.

Exact timeout values remain configuration/evidence decisions.

<a id="iam-009"></a>
## IAM-009 — Shared-device and context handoff terminates prior private context before reuse

On a shared device, user/capacity handoff must not leave the prior context's protected data or authorization usable by the next participant.

A safe handoff re-establishes enough of:

- current Identity;
- Participation/capacity;
- Competition;
- protected resource context;
- current Access.

Browser/server state associated with the prior protected context is cleared, partitioned or made inaccessible before the next context is exposed.

A route, QR code, browser session or cached view never proves current Access.

<a id="iam-010"></a>
## IAM-010 — Invitation, QR, event and deep-link credentials route or claim bounded context; they do not authenticate authority

Invitation links, event codes, QR codes and similar entry credentials may:

- identify Competition/context;
- route the participant;
- enable a bounded Participation claim/enrollment step where policy permits.

Possession alone does not establish:

- trusted Identity;
- Judge/Organizer Participation;
- current Access;
- Panel membership;
- evaluation responsibility.

Camera-independent entry remains possible because QR is convenience, not authority.

<a id="iam-011"></a>
## IAM-011 — Reverfication and step-up strengthen principal assurance but never create application capability

Fresh authentication or step-up may be required for higher-risk actions such as:

- provider/account linking or recovery;
- sensitive context transition;
- post-event correction;
- exceptional grant exercise;
- break-glass operation;
- later high-consequence Organizer actions where evidence justifies it.

Stronger authentication proves principal control more strongly.

The application must still independently evaluate MUDAC Participation, Access, resource/lifecycle preconditions and represented authority.

<a id="iam-012"></a>
## IAM-012 — Exceptional application Access is narrow, attributable, expiring and revocable

Where ordinary Participation-derived Access has expired but legitimate exceptional work remains, MUDAC may create a narrow Access grant with:

- stable grant identity;
- intended principal/Participation;
- Competition/resource scope;
- capability set;
- purpose/reason;
- validity interval;
- status;
- revocation/expiry history;
- attributable authorizer.

Examples include a permitted post-event Judge correction.

Exceptional grant does not restore broad event-day capability or unrelated disclosure.

<a id="iam-013"></a>
## IAM-013 — Identity recovery/linking cannot silently rewrite historical attribution

Credential/provider recovery may change how a human proves control of Identity.

It must not:

- rewrite the stable MUDAC Identity of historical actions;
- merge two Identities merely because current email/name matches;
- transfer Judge authorship;
- rewrite Participation history.

Potential duplicate/linked Identity resolution is an explicit governed action with retained evidence.

<a id="iam-014"></a>
## IAM-014 — Technical/operator authority is a separate principal/context from Competition Participation

Infrastructure, deployment, support, database and security privileges do not automatically grant Judge or Organizer application authority.

Routine technical operation must not silently permit an operator to:

- author Judge evaluation;
- inspect protected Judge data without an application-authorized purpose;
- reveal blinded Team identity;
- alter Competition outcomes;
- Finalize a Competition;
- publish application authority.

If the same human also has a Competition Participation, that Participation is a distinct application context.

<a id="iam-015"></a>
## IAM-015 — Break-glass access is exceptional technical authority, not semantic impersonation

Where necessary, break-glass operation is:

- explicitly invoked;
- stronger-authenticated where appropriate;
- time/resource/capability bounded;
- reason-bearing;
- attributable;
- auditable;
- automatically expiring/revocable.

Break-glass may restore or diagnose technical operation.

It cannot fabricate Judge intent or silently impersonate semantic authorship.

If an application correction requires represented authority, Provenance records Actor and RepresentedAuthority distinctly under current policy.

<a id="iam-016"></a>
## IAM-016 — Authentication-provider integration remains replaceable behind an application adapter

MUDAC uses a managed standards-compatible external authentication provider behind an application-owned adapter.

Core application code does not make provider-native groups/roles the semantic authorization model.

Provider replacement or added federation must preserve:

- MUDAC Identity IDs;
- Participation history;
- Access semantics;
- authorship;
- Provenance;
- current application-session boundary.

Provider-specific configuration and provider selection remain ADQ-009/runtime evidence decisions.

<a id="iam-017"></a>
## IAM-017 — Authentication/provider unavailability reduces capability safely; it does not broaden authority

When authentication or provider reverification is unavailable:

- already established application sessions may continue only within their valid bounded session/security posture and current application Access;
- operations requiring fresh/reverification proof may become unavailable;
- the system must not bypass authentication/Access merely to preserve convenience;
- cached provider claims do not become permanent authority.

Safe unavailability is preferred to privilege broadening.

<a id="iam-018"></a>
## IAM-018 — Access denial and security response preserve truthful, non-leaking explanation

Access/security failures distinguish enough meaning to support legitimate recovery without disclosing protected facts.

The application may distinguish categories such as:

- authentication/reverification required;
- no current Participation;
- Participation not active/current enough;
- current Access denied;
- exceptional grant required/expired;
- session revoked/expired;
- protected resource/lifecycle state disallows action.

The explanation must not itself reveal protected competitor, Judge, outcome or administrative information.

# Selected architecture

ADQ-004 selects:

> **Managed standards-compatible external authentication behind an application adapter, explicitly linked to stable MUDAC Identity; Competition-scoped Participation and contextual MUDAC-owned Access; opaque first-party server-controlled sessions; explicit multi-capacity isolation; bounded revocation/reverification/step-up; narrow exceptional grants; shared-device context clearing; and strict technical/operator separation from semantic authority.**

# Session storage boundary

This decision requires server-controlled, revocable session state.

It does not require a separate session service.

The exact backing store may be selected during runtime/implementation planning, provided it satisfies:

- revocation/currentness;
- bounded lifetime;
- event-day availability needs;
- shared-device safety;
- no use of session state as domain authority.

PST-001..016 remain authoritative for durable product-domain persistence.

# Provider/runtime boundary

This decision does **not** select:

- Amazon Cognito;
- another named managed IdP;
- organization SAML/enterprise federation;
- a final secret-management product;
- exact MFA policy;
- exact cookie lifetime;
- exact session backing store.

Those decisions require provider/runtime evidence in ADQ-009 or bounded implementation configuration.

# Revisit triggers

Reopen ADQ-004 when credible evidence shows:

- a concrete provider cannot preserve stable application Identity or application-owned Access;
- shared-device operation cannot be made safe with the selected session model;
- required federation/SSO changes the application/provider authority boundary;
- session availability/revocation requirements cannot be met proportionately;
- legal/security requirements change authentication assurance or retention expectations;
- whole-architecture validation exposes unacceptable privilege, stale-access or operator-authority leakage.

Whole-architecture acceptance remains false until 019-L.

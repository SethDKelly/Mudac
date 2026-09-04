---
type: Architecture Contract
title: Identity, Authentication, Access & Session Architecture
description: Defines provider-neutral authentication, MUDAC Identity/Participation mapping, contextual Access, first-party sessions, role-context isolation, revocation, correction grants, and administrator/break-glass boundaries.
status: stable
tags: [architecture, identity, authentication, authorization, access, session, security]
sources:
  - resource: ../../005-system-application-data-synchronization-architecture/005-D-identity-authentication-participation-access-session-architecture.md
  - resource: architectural-foundation.md
  - resource: application-boundaries.md
  - resource: data-persistence.md
  - resource: ../concepts/identity.md
  - resource: ../concepts/participation.md
  - resource: ../concepts/access.md
  - resource: ../experience/judge-onboarding.md
generated: { by: openai/gpt-5.6-sol, at: 2026-09-04T04:36:00Z }
---

# Purpose

Define how authentication proof becomes a secure MUDAC interaction context while preserving the canonical distinction between Identity, Competition Participation, and contextual Access.

The core chain is:

```text
authentication proof
    ↓
MUDAC Identity
    ↓
selected Competition Participation
    ↓
contextual Access evaluation
    ↓
authorized action/disclosure
```

<a id="auth-001"></a>
## AUTH-001 — Authentication establishes principal continuity, not Competition authority

A managed external authentication provider establishes/reverifies control of an external principal. MUDAC remains authoritative for Identity, Participation, Access, Scorecard authorship, Organizer authority, and Competition lifecycle capability.

Provider groups/roles/claims may be inputs or integration metadata but cannot be the sole authority for MUDAC Competition permissions.

<a id="auth-002"></a>
## AUTH-002 — External subjects link explicitly to stable MUDAC Identity

Authentication identities are linked to MUDAC Identity through stable provider/issuer + external-subject identity, not by mutable email address, display name, role, or device.

Identity merging/linking is explicit and governed; matching names/emails never silently merge distinct people. Historical attribution survives Identity disablement or provider change.

<a id="auth-003"></a>
## AUTH-003 — Participation context is explicit and never inferred as a permanent Identity role

Authentication resolves an Identity, after which MUDAC resolves current Competition Participation(s). Prior Competition Participation never automatically becomes current in a later Competition.

Where one Identity has multiple legitimate Participations, the active operating context is explicitly selected rather than capability-unioned.

<a id="auth-004"></a>
## AUTH-004 — Access is evaluated from current authoritative context at protected boundaries

Consequential actions and sensitive disclosures evaluate current Identity status, Participation, Competition/resource state, relationship/authorship, capability, purpose, explicit grants/revocations, and time as relevant.

Cached client/session role claims or UI visibility do not substitute for current authorization. This realizes [ACC-001](../concepts/access.md#acc-001), [ACC-002](../concepts/access.md#acc-002), and [ARCH-002](architectural-foundation.md#arch-002).

<a id="auth-005"></a>
## AUTH-005 — Browser authentication terminates in a first-party opaque server session

The initial browser application uses an opaque first-party session identifier held in a production-protected cookie (including `Secure`, `HttpOnly`, and intentional `SameSite` behavior) and server-managed session state.

Long-lived provider/access/refresh bearer credentials are not stored in ordinary script-readable browser storage for the core application session. Provider secrets/tokens remain behind the server application boundary where practical.

<a id="auth-006"></a>
## AUTH-006 — Session context is convenience state, not authorization authority

A server session may remember Identity and selected Participation context for usability, but stored session context cannot extend revoked/expired Participation or Access.

Sessions have bounded lifetime and support logout, idle/absolute expiry, revocation, replacement-device reauthentication, and stronger re-verification/step-up where required.

<a id="auth-007"></a>
## AUTH-007 — Event completion expires Judge capability through source-state authorization

After successful Competition Event Completion, stale Judge sessions no longer authorize ordinary private-evaluation access even if the browser cookie remains technically valid for Identity continuity.

A later legitimate event resume recalculates Access from current state rather than blindly reviving cached capabilities.

<a id="auth-008"></a>
## AUTH-008 — Event invitations and QR/codes accelerate entry but do not confer Identity or Access

Competition links, QR codes, event codes, and invitation/enrollment tokens may route or authorize a bounded Participation-claim workflow, but possession alone never establishes a trusted Judge/Organizer.

Individual invitation credentials are scoped/expiring/revocable as appropriate, and claim occurs only after required Identity authentication/reverification and current-state validation. Camera-independent entry remains available.

<a id="auth-009"></a>
## AUTH-009 — Dual-role capability sets remain isolated by explicit Participation context

A person with Judge and Organizer Participation does not receive the union of both capability/disclosure sets in one implicit mode. Context switching is explicit, actions retain the actual Participation context in Provenance, and higher-sensitivity transitions may require deliberate confirmation or step-up.

Client-side private cached data must be cleared/partitioned sufficiently that Organizer-only information is not exposed through the active Judge context.

<a id="auth-010"></a>
## AUTH-010 — Post-event Judge correction uses narrow temporary Access plus reverification

Correction after ordinary Judge Access expiry uses an explicit, auditable, resource/capability/Competition/time-bounded grant tied to the intended Judge Participation and purpose.

The Judge reverifies current Identity control before exercising it. The grant does not restore broad judging history, Notes, peer evaluations, Aggregate, or Rank access.

<a id="auth-011"></a>
## AUTH-011 — Device loss or handoff revokes session state without changing semantic identity

A lost/replaced/shared device does not create a new Identity, Participation, or logical Scorecard. Sessions can be revoked independently, and replacement-device authentication resolves the same durable MUDAC context.

Shared-device transitions explicitly terminate/clear prior private local/session context before another person begins. See [ARCH-003](architectural-foundation.md#arch-003) and [ARCH-006](architectural-foundation.md#arch-006).

<a id="auth-012"></a>
## AUTH-012 — System administration and break-glass authority remain separate from Competition authority

Routine infrastructure/operator privileges do not automatically grant application capabilities to inspect private Judge data, rewrite evaluations, resolve blinded Team identity, alter outcomes, or Finalize a Competition.

Break-glass access, when necessary, is explicit, stronger-authenticated as appropriate, time/resource/capability bounded, reason-bearing, auditable, and automatically expires. Technical actor identity remains distinct from semantic Judge/Organizer authorship.

<a id="auth-013"></a>
## AUTH-013 — Step-up authentication strengthens proof but never creates capability

Fresh authentication/step-up may be required for credential linking/recovery, sensitive role-context changes, post-event correction, break-glass use, or later identified high-consequence Organizer actions.

Step-up only increases confidence that the current principal controls the credential; the application must still independently authorize the requested capability from current MUDAC state.

<a id="auth-014"></a>
## AUTH-014 — Authentication-provider implementation remains replaceable behind an adapter

MUDAC integrates a managed standards-compatible identity provider through an application-owned adapter. MUDAC does not implement password storage/reset/MFA/federation protocols as core domain logic.

Provider replacement or added federation must preserve MUDAC Identity IDs, Participation history, authorship, Access semantics, and Provenance rather than rewriting domain identity.

# Access enforcement topology

```text
browser / external principal
        ↓ authenticate
identity-provider adapter
        ↓ external subject
Identity / Participation / Access module
        ↓ session + current context
application/module command/query boundary
        ↓ contextual authorization + resource preconditions
authoritative module state
```

The Identity/Participation/Access module owns identity/security facts, but resource-owning modules still enforce the final resource/lifecycle conditions for their authoritative commands. Authorization therefore does not become a detached generic permission service that replaces domain ownership.

# Session posture

Server session state may include session ID, Identity ID, authentication/assurance timestamps, selected Participation ID, created/last-seen/absolute-expiry data, revocation state, and a security/session version. Exact storage and duration are runtime configuration choices.

Client-side state may improve UX but cannot extend server-side session or Access authority.

# Provider posture

005-D selects **managed, standards-compatible, provider-adapted authentication** but does not yet select Cognito, Auth0, Entra ID, Okta, or another vendor, nor a single passwordless/federated/passkey mechanism. Vendor/runtime selection belongs to later architecture once deployment, cost, federation, and operations are evaluated.

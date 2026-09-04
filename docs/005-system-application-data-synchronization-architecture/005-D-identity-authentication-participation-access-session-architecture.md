---
type: Design Phase Record
title: 005-D — Identity, Authentication, Participation, Access & Session Architecture
description: Defines provider-neutral authentication, MUDAC Identity linking, Competition Participation, contextual Access evaluation, first-party sessions, event-day onboarding, role switching, revocation, correction access, and administrator/break-glass boundaries.
status: stable
tags: [phase-005, architecture, identity, authentication, authorization, access, session, security]
sources:
  - resource: ../canonical/architecture/architectural-foundation.md
  - resource: ../canonical/architecture/application-boundaries.md
  - resource: ../canonical/architecture/data-persistence.md
  - resource: ../canonical/concepts/identity.md
  - resource: ../canonical/concepts/participation.md
  - resource: ../canonical/concepts/access.md
  - resource: ../canonical/experience/judge-onboarding.md
  - resource: ../002-concept-specification/002-B-identity-participation-access-specifications.md
generated: { by: openai/gpt-5.6-sol, at: 2026-09-04T04:36:00Z }
---

# Purpose

005-D defines the security architecture that turns authentication evidence into a usable MUDAC session without collapsing Identity, Competition Participation, and contextual Access into identity-provider roles or client-side claims.

The governing chain is:

```text
external authentication proof
        ↓
MUDAC Identity
        ↓
Competition Participation context
        ↓
contextual Access decision
        ↓
authorized application action/disclosure
```

Authentication proves current control of a credential/principal. It does not itself grant Judge, Organizer, Competition, Scorecard, outcome, or publication authority.

# 1. Authentication boundary

MUDAC should integrate with a managed standards-compatible identity provider behind an application-owned authentication adapter. The concrete provider remains open until runtime/AWS evaluation.

The adapter must support at least:

- establishing or reverifying a human principal;
- stable external subject identity independent of display/email changes;
- first-time and returning-user flows;
- account/credential recovery;
- session/token validation suitable for a server-side web application;
- future federation without changing MUDAC Identity/Participation semantics.

The architecture does not require a permanent username/password account experience for event-day Judges. Passwordless email verification, federated login, passkey, or another provider-supported proof may be used later when usability/security tradeoffs are evaluated.

# 2. External principal to MUDAC Identity mapping

An external authenticated subject is linked to a stable MUDAC Identity through an explicit credential-link record such as:

```text
IdentityCredential
    identity_id
    issuer/provider
    external_subject
    status
    linked_at
    last_verified_at
```

`issuer + external_subject` is the authentication-side stable key. Email address, display name, Competition role, or device identifier is not the MUDAC identity key.

MUDAC must not silently merge two Identities solely because their email/name matches. Multiple external credentials may later be deliberately linked to the same Identity through a governed linking/recovery flow.

Disabling a MUDAC Identity prevents ordinary future use while historical Participation, authorship, Version, and Provenance remain retained.

# 3. Participation architecture

Participation remains authoritative MUDAC application state owned by the Identity/Participation/Access module.

A successful login resolves Identity continuity, then the application resolves zero/one/many current Competition Participations for that Identity. A prior Competition Participation is never reactivated merely because the same Identity authenticates again.

Participation lifecycle/state is persisted independently from provider groups/claims. Judge expertise, check-in, current status, and Competition role remain MUDAC-owned state.

Dual-role Identity is supported by separate Participation records. The current operating context is explicit rather than capability-unioned.

# 4. Event-day invitation and onboarding

Low-friction event entry may use Competition URLs, QR codes, event codes, or individualized invitation/enrollment tokens.

These are routing/enrollment proofs, not authentication or final Access authority.

A safe individualized invitation flow is:

```text
open invitation
    ↓
authenticate / reverify Identity
    ↓
validate invitation scope + expiry + intended Participation
    ↓
claim/link the Competition Participation
    ↓
confirm current-event attributes / check-in
    ↓
derive Ready to Judge
```

Invitation tokens should be high-entropy, time/scoped, revocable where appropriate, and avoid encoding protected business information in URLs. General QR/event codes must have a non-camera equivalent.

Organizer-assisted recovery/enrollment may establish or reconnect Participation, but it cannot substitute for Judge authorship or silently bypass the chosen Identity-verification policy.

# 5. Access decision architecture

MUDAC uses capability-oriented contextual authorization rather than broad role checks.

An Access decision evaluates the relevant combination of:

```text
Identity status
active Participation context
role
Competition scope + lifecycle
capability
resource identity/state
resource relationship / authorship
purpose
explicit temporary grants/revocations
current time
step-up/reverification state where required
```

This is an application-owned policy decision. Provider roles/groups may be inputs for system-level integration but cannot be the sole authority for Competition capabilities.

Ordinary Access should generally be derived from authoritative state/policy rather than persisted as one permission row for every action. Exceptional temporary grants/revocations are persisted when their bounded authority must be explicit/auditable.

# 6. Module enforcement

Each authoritative module enforces Access at its public application/command boundary for the resources/capabilities it owns. UI hiding and gateway-level authentication are defense-in-depth only.

The Identity/Participation/Access module provides authoritative Identity, Participation, grant/revocation, and policy-context facts. It does not become a generic remote permission oracle that other modules bypass their own resource/lifecycle checks to call blindly.

Application coordination may assemble cross-module context, but the owner of a consequential command must validate the final relevant Access/preconditions under `ARCH-002` and `MOD-002`.

# 7. First-party browser session model

The initial web application uses a first-party server-managed session.

The browser receives only an opaque session identifier in a cookie configured for transport/confidentiality protections appropriate to production, including `Secure`, `HttpOnly`, and an intentional `SameSite` policy. Long-lived authentication/refresh bearer tokens are not stored in browser `localStorage`/ordinary script-readable storage for the core session.

Server-side session state contains/references only what is needed to establish the current principal and interaction context, for example:

```text
session_id
identity_id
authentication_time / assurance context
active_participation_id?
created_at
last_seen_at
absolute_expiry
revoked_at?
security/session version
```

The session may remember the selected Participation context for UX continuity, but that selection is not itself authorization. Consequential requests reevaluate current Participation/Access/resource state.

The exact server-side session storage technology and durations remain operational configuration decisions. They must support revocation and expected event concurrency.

# 8. Session lifetime and revalidation

Sessions use bounded lifetime rather than indefinite validity. The architecture supports:

- idle expiry;
- absolute expiry;
- explicit logout;
- per-session/device revocation;
- Identity-wide/session-family revocation when compromise requires it;
- renewal/reverification without changing logical Identity or Participation;
- invalidation/reevaluation when security-sensitive basis changes.

Event completion does not require every browser cookie to disappear synchronously. It requires that stale Judge sessions cease to authorize expired capabilities immediately when they next interact with authoritative application boundaries.

Thus Access expiry is source-state driven, not dependent on clients receiving a logout push.

# 9. Event completion and resume

When `Competition.completeEvent` succeeds, ordinary Judge private-evaluation capabilities expire according to `ACC-001`. Retained sessions can at most authenticate the Identity; they no longer authorize those resources.

If a Competition is legitimately resumed, live Access is recalculated from current Competition/Participation state. Prior cached capabilities are not blindly restored.

Organizer Participation may remain active for reconciliation/closeout, but result-changing capabilities close as the Competition lifecycle/policy requires.

# 10. Post-event correction access

Judge correction after ordinary access expiry uses a narrow persisted temporary grant associated with:

- intended Identity / Judge Participation;
- specific Scorecard/resource or narrow resource set;
- amendment capability;
- Competition scope;
- purpose/reason;
- grantor/authorizer;
- validity window/consumption state;
- Provenance/audit identifiers.

The Judge must reverify current Identity control before exercising the grant. The grant does not restore general Scorecard history, Notes, peer information, Ranking, or broader event capabilities.

After completion/expiry/revocation, ordinary denial resumes.

# 11. Dual-role context switching

When one Identity legitimately has both Judge and Organizer Participations, the application exposes an explicit role/Participation context switch.

Capabilities are not unioned across contexts. Judge-mode views/queries remain Judge-safe even though the same Identity also has Organizer authority.

Switching into a higher-sensitivity context may require deliberate confirmation or step-up/reverification according to the operation/security policy. Switching context should invalidate/clear incompatible client-side cached private views so Organizer-only information is not left exposed in an active Judge context.

Provenance for state-changing actions records the actual Participation/authority context used, not merely the underlying Identity.

# 12. Shared, loaner, and lost devices

Device identity is not principal identity.

Shared/loaner device handoff requires an explicit end of the prior interaction context and clearing of locally retained private state. The next Judge authenticates/reverifies into a new server session and must not inherit prior Scorecards, Notes, Team context, or reusable credentials.

For a lost device, the affected session can be revoked without changing the Judge Participation or creating another logical Scorecard. Reverification on a replacement device recovers the same Identity/Participation and whatever Draft state was durably preserved.

Offline/local Draft cleanup and synchronization details remain for 005-F, but local persistence must be partitioned by authenticated/session identity and designed for secure clearing.

# 13. Step-up/reverification posture

Not every command needs repeated authentication. Step-up should be proportional to consequence and threat.

Candidates include:

- account/credential linking or recovery;
- sensitive dual-role context transition;
- exceptional post-event Judge correction;
- break-glass administration;
- particularly high-consequence Organizer operations if later threat analysis justifies it.

Step-up proves fresh control/assurance. It does not itself grant the capability; contextual Access must still allow the action.

# 14. Administrator and break-glass architecture

Runtime/system Administrator authority remains separate from Competition Participation.

Routine infrastructure/operator access should not automatically create application sessions capable of reading Judge Notes, resolving Team identity, altering Scorecards, changing Rank/Awards, or Finalizing a Competition.

Extraordinary break-glass access is explicit, time/resource/capability bounded, independently auditable, reason-bearing, and automatically expires. Where practical, it should use a distinct elevated path/credential and require stronger authentication/approval than routine operation.

A break-glass technical actor remains the actor in Provenance/security audit; it cannot be represented as the Judge/Organizer semantic author unless canonical product authority actually permits that role.

# 15. Security/privacy posture

The architecture minimizes identity/profile data to what is operationally needed. Authentication secrets/provider tokens should not be copied into MUDAC domain tables.

Sensitive session/identity events should be security-auditable without logging raw credentials, session secrets, magic-link/one-time tokens, private Notes, or unnecessary administrative Team identity.

Invitation/session/recovery tokens are secrets: store/compare them using mechanisms that do not require recovering the original bearer value where feasible, rotate/revoke as appropriate, and never expose them through ordinary telemetry.

# 16. Authentication-provider portability

The provider adapter exposes MUDAC-oriented operations such as authenticate callback/subject resolution, reverify/step-up initiation, logout/revocation hooks where available, and external credential linking.

MUDAC stores its own Identity, Participation, Access-grant, and session semantics. Provider change/federation expansion must therefore not require rewriting Scorecard authorship or Competition role history.

The initial provider should be managed and standards-compatible rather than MUDAC implementing password storage, reset flows, MFA enrollment, or federation protocols itself.

# 17. Threat/failure scenarios

## AUTH-QA-01 — Stale Judge session after Event Completed

A Judge leaves a browser tab open before `completeEvent` and later requests an old Scorecard URL.

Required: authentication may still identify the human, but Access reevaluation denies private evaluation retrieval; the URL/session cannot resurrect expired authority.

## AUTH-QA-02 — Lost Judge phone

Organizer/support revokes the compromised session. Judge reverifies on a new phone.

Required: same Identity/Participation, no duplicate evaluation, old session unusable, durably saved Draft recoverable under 005-F rules.

## AUTH-QA-03 — Dual-role person switches from Organizer to Judge

Required: Judge context receives only Judge-safe disclosure/capabilities; Organizer analytics are not implicitly retained as Judge authority; later actions record the selected Participation context.

## AUTH-QA-04 — Invitation URL forwarded

Another person obtains a Judge invitation URL.

Required: possession of invitation is insufficient; Identity proof plus invitation/Participation validation controls claim, and conflicting/already-claimed state is surfaced rather than silently reassigning authorship.

## AUTH-QA-05 — Provider temporarily unavailable

Existing valid server sessions may continue only within their established security/session policy and current MUDAC Access basis. New/reverification flows may safely fail. The application does not manufacture identity proof because the provider is unavailable.

## AUTH-QA-06 — Temporary correction grant expires mid-session

Required: session remains capable of identifying the Judge, but the amendment capability is denied after grant expiry; cached UI state cannot extend the grant.

## AUTH-QA-07 — Shared device changes users

Required: Judge A private local/session context is cleared/revoked before Judge B begins; Judge B cannot read Judge A Notes, Scorecard Draft, or history.

# 18. Non-decisions

005-D does not yet select:

- Cognito/Auth0/Entra/Okta or another concrete identity provider;
- passwordless email vs passkey vs federation as the default event-day proof;
- exact idle/absolute session durations;
- exact MFA/step-up factors;
- Redis/database/in-memory session-store implementation;
- exact CSRF implementation details;
- API token format for any future non-browser integration;
- browser offline-Draft encryption/storage/synchronization mechanism;
- concrete AWS IAM/operator break-glass mechanism.

Those decisions remain downstream of this provider-neutral semantic/session architecture and later threat/runtime design.

# 19. Exit result

005-D introduces no new MUDAC Concept and changes no Phase 001–003 product semantics.

It establishes a provider-portable, first-party-session architecture in which authentication establishes Identity continuity; MUDAC Participation and Access retain Competition authority; stale sessions cannot extend expired capability; dual-role and correction authority remain explicit; and operator/break-glass authority stays distinct from product authorship.

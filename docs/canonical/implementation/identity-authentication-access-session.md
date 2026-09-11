---
type: Implementation Contract
title: Identity, Authentication, Participation, Access, Session, Invitation, Secrets & Technical Authority Implementation Contract
description: Defines the accepted Cognito/OIDC adapter, stable external-principal linkage, Participation-context isolation, contextual Access realization, opaque first-party sessions, invitation/recovery/reverification mechanics, secret handling, and technical-authority separation for MUDAC.
status: stable
tags: [implementation, identity, authentication, participation, access, session, invitation, secrets, technical-authority, cognito]
sources:
  - resource: ../../008-implementation-reentry/008-E-identity-authentication-participation-access-session-invitation-secrets-technical-authority-implementation-plan.md
  - resource: ../architecture/identity-access-session.md
  - resource: ../architecture/application-boundaries.md
  - resource: ../architecture/data-persistence.md
  - resource: ../architecture/commands-api-concurrency.md
  - resource: ../architecture/aws-runtime-operations.md
  - resource: ../concepts/identity.md
  - resource: ../concepts/participation.md
  - resource: ../concepts/access.md
  - resource: ../experience/judge-onboarding.md
  - resource: persistence-history-projection.md
  - resource: implementation-foundation.md
  - resource: source-topology.md
  - resource: verification-strategy.md
  - resource: https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-client-apps.html
  - resource: https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-security-best-practices.html
  - resource: https://docs.aws.amazon.com/cognito/latest/developerguide/federation-endpoints-oauth-grants.html
generated: { by: openai/gpt-5.6-sol, at: 2026-09-11T00:40:00Z }
---

# Purpose

Define the durable implementation choices that realize the accepted Identity, Participation, Access, authentication/session, invitation, recovery, secrets, and technical-authority architecture before any of those behaviors are implemented.

This contract is downstream of `AUTH-*`, `ACC-*`, `MOD-*`, `DATA-*`, `API-*`, the Identity/Participation/Access Concepts, Judge Onboarding, and the accepted 008-D persistence contract. It chooses concrete mechanisms where the upstream design intentionally left implementation latitude without turning provider claims, sessions, tokens, role labels, or operator privilege into semantic authority.

This owner introduces no new stable-rule namespace. Later implementation and tests should cite existing stable canonical rule IDs plus this owner where the concrete mechanism matters.

# Current execution boundary

This contract is a **Phase 008 implementation-planning result**. It does not authorize Cognito resources, Identity/Participation/Access tables, login routes, session cookies, invitation flows, secret provisioning, or operator tooling.

Until 008-L explicitly authorizes a Phase 009 entry slice:

- `@mudac/identity-access` remains a placeholder/minimal package seam;
- `identity_access` remains a planned PostgreSQL schema, not an implemented schema;
- no Cognito User Pool/app client/domain is provisioned;
- no browser/server authentication flow is added;
- no real secret or production authority is introduced.

# Authority chain

The implementation preserves one directional chain:

```text
provider authentication proof
        ↓
explicit provider-principal link
        ↓
MUDAC Identity
        ↓
explicit selected Competition Participation
        ↓
Access capability/grant evaluation
        ↓
resource-owner lifecycle/relationship preconditions
        ↓
authorized command or disclosure
```

No lower-level mechanism may skip a step upward.

In particular:

- Cognito authentication is not Participation;
- a MUDAC Identity is not a permanent Judge/Organizer role;
- a Participation is not itself sufficient for every capability;
- a session is not authorization authority;
- a capability/grant cannot transfer Judge authorship or Competition decision authority;
- technical/operator authority cannot satisfy a semantic Judge/Organizer precondition.

# Authentication-provider realization

Amazon Cognito User Pools remains the initial managed authentication provider under `AWS-006` and is isolated behind an application-owned adapter.

## Browser sign-in flow

The browser sign-in path uses OIDC/OAuth 2.0 **authorization-code flow**. The initial implementation enables code flow only for the human browser app; implicit grant is not part of the baseline.

Each authorization attempt uses:

- a fresh cryptographically random `state` value;
- OIDC `nonce` validation;
- PKCE with a fresh verifier/challenge;
- an exact allowlisted callback URI;
- server-side code exchange and provider-token validation.

Provider ID/access/refresh tokens are never placed in ordinary script-readable browser storage.

The baseline does not require MUDAC to retain Cognito access or refresh tokens after the callback has resolved and validated the external principal. Long-lived application continuity is provided by the MUDAC first-party session. A later need for provider API access or silent provider-token refresh requires an explicit implementation decision rather than incidental token hoarding.

A server-side confidential Cognito app client may use a client secret because the application has a trusted server component. If a client secret is configured, it remains server-only and is retrieved from protected secret storage. PKCE remains part of the authorization-code flow as interception resistance rather than making the browser a bearer-token authority.

## Provider claims

The provider adapter validates issuer, audience/client identity, signature/key material, nonce and time validity as applicable before accepting an authentication result.

The durable external-principal key is:

```text
provider/issuer identity + external subject (`sub`)
```

Email, username, display name, Cognito group, token role claim, or mutable profile attribute is never the MUDAC Identity key and never silently merges two MUDAC Identities.

Provider groups are not baseline MUDAC authorization inputs. If later federation supplies groups or enterprise claims, they remain advisory/integration evidence until explicit MUDAC Participation/Access semantics consume them.

# Identity persistence and provider linkage

The `identity_access` schema owns the stable MUDAC Identity and authentication-principal links.

The planned logical records are:

```text
identity
  identity_id
  status
  minimum necessary human-facing/recovery attributes
  revision
  verification / reverification metadata
  recorded timestamps

auth_principal_link
  provider/issuer key
  external subject
  identity_id
  linked_at
  link provenance / assurance metadata
  disabled/unlinked state where permitted
```

The provider/issuer + subject tuple is unique across current links. A provider principal cannot silently point at two MUDAC Identities.

Multiple provider principals may eventually link to one MUDAC Identity, but linking is explicit and stronger-authenticated. Matching email addresses never create such a link automatically.

Identity disablement preserves the Identity and all historical attribution. It removes current application capability and revokes current sessions rather than deleting historical authorship/provenance.

# Participation realization

Participation remains one stable Competition-scoped role episode rather than a claim copied from authentication.

The planned root contains at least:

```text
participation_id
identity_id
competition_id
role
lifecycle state
role-relevant current declared metadata
revision
lifecycle timestamps
```

For the current baseline, one Identity has at most one Participation for a given Competition + role. Judge and Organizer dual-role use therefore creates two distinct Participations, not a role array or merged privilege set.

Withdrawal/restoration and ordinary lifecycle transitions operate on the same stable Participation and produce meaningful Provenance. A later Competition always creates a new Participation even if Identity is reused.

The mutable Participation root uses the 008-D technical revision token for concurrency. That revision is not a semantic Versioning Concept Version.

# Participation-context isolation

A session may reference one selected Participation at a time for usability.

When an Identity has multiple current Participations:

- the user explicitly selects/switches operating context;
- the server revalidates that Participation and current Competition state;
- the session identifier is rotated on meaningful privilege/context change;
- private browser/server context must not be capability-unioned across roles;
- subsequent Provenance records the actual Participation used by the action.

Selecting Organizer context does not make Judge-only information available there unless the protected resource/disclosure policy separately permits it, and vice versa.

# Contextual Access realization

MUDAC does **not** adopt a generic database RBAC/ACL engine as its authority model.

Ordinary Access is primarily evaluated from current authoritative state:

```text
Identity status
+ selected Participation and role/lifecycle
+ Competition scope/state
+ requested capability
+ target resource/relationship/authorship context
+ purpose/time
+ explicit grant/revocation where applicable
```

## Capability vocabulary

Capability identifiers are typed code-level/public-contract vocabulary owned with the relevant semantic/application boundary, not freely editable database strings that can invent new product authority at runtime.

`@mudac/identity-access` may answer whether current Identity/Participation/grant state satisfies the Access-owned portion of a capability check. The resource-owning module still validates final lifecycle, relationship, authorship, disclosure, and domain preconditions.

This deliberately prevents an authorization service from becoming a detached second owner of Competition/Evaluation/Outcome semantics.

## Exceptional Access grants

The Access Concept's explicit temporary grants are persisted in `identity_access` as immutable grant authority plus append-stable revocation/correction evidence.

A grant records at least:

```text
grant_id
identity + intended Participation context
Competition scope
capability
resource scope / stable target reference
purpose/reason
valid_from / expires_at
issuing Identity + Participation/authority
recorded_at
provenance
```

Current validity is derived from the grant, current Identity/Participation/resource state, expiry, and any retained revocation record. Revoking or expiring a grant does not delete the fact that it existed.

A grant never changes semantic authorship. Post-event Scorecard correction can therefore permit the intended Judge to access a specific correction capability without transferring authorship to the Organizer who issued or facilitated the grant.

# Event-completion capability expiry

Event Completed is evaluated from current Competition state at protected server boundaries.

Ordinary Judge access to private evaluation material ends even if:

- the cookie remains technically valid;
- the session still references the Judge Participation;
- a stale browser view still displays prior controls;
- a cached query contains prior private state.

The session can remain useful for Identity continuity or other currently authorized interactions, but it cannot prolong expired Judge capability.

Post-event correction requires a specific temporary Access grant plus current reverification as required by `AUTH-010`.

# First-party session realization

The initial application uses PostgreSQL-backed opaque server sessions in the `identity_access` schema. Redis/DynamoDB is not introduced merely for session storage.

## Session token

The browser receives a cryptographically random opaque token with sufficient entropy. The database stores a one-way digest of the token rather than the bearer value itself.

Production cookie posture is:

```text
__Host- prefixed session cookie where deployment topology permits
Secure
HttpOnly
Path=/
no Domain attribute
intentional SameSite policy
```

008-F owns the final CSRF mechanism that composes with this cookie-authenticated transport.

## Session record

Server session state supports at least:

```text
session_id / token digest
identity_id
selected_participation_id nullable
authenticated_at
reverified/step-up assurance timestamps or provider assurance metadata
created_at
last_seen_at
idle expiry
absolute expiry
revoked_at / revocation reason
session security/version state
```

Exact idle/absolute durations are security configuration, not product semantics. 008-K must set and verify production thresholds. Whatever values are chosen, a session can never outlive revoked Identity/Participation/Access authority because protected operations re-evaluate current state.

Session rotation is required after authentication, recovery/principal relinking, and meaningful privilege/Participation-context changes. Logout and security revocation invalidate the server session; deleting only the browser cookie is not sufficient revocation semantics.

## Provider-token boundary

MUDAC's session is not a copy of a Cognito token. Provider tokens used during callback validation are transient unless a future explicitly justified adapter operation requires retained provider credentials.

Reverification/step-up obtains fresh provider proof rather than trusting an old MUDAC session timestamp indefinitely.

# Authentication transaction state

OIDC authorization attempts use short-lived, single-use server-side transaction state rather than trusting callback query values by themselves.

The planned technical record holds only what is required to reconcile the callback safely, such as hashed/random state identity, PKCE verifier, nonce, intended post-login destination, created/expiry time, and one-time consumption state.

Expired/consumed attempts are rejected. Return destinations are validated as local/allowlisted application paths rather than arbitrary redirect URLs.

This is technical authentication state, not a MUDAC Concept or Participation.

# Invitation and event-entry realization

Invitations, QR codes, links and event codes remain **entry/claim mechanisms**, never Identity or Access authority by possession alone.

The implementation distinguishes two intents:

1. **route-only entry context** — identifies Competition/onboarding destination and contains no enrollment authority;
2. **bounded Participation-claim invitation** — server-side record permits a specific enrollment/claim path after authentication and current-state validation.

## Individual invitation secret

A claim-capable invitation uses a high-entropy random secret. Only its digest is stored. The invitation record binds the secret to explicit scope such as Competition, intended role, optional pre-created Participation/intended recipient constraints, expiry, usage limit, issuing authority, and revocation state.

Claim is atomic and replay-safe. A token is not accepted merely because its URL was previously valid.

After token exchange/claim, the browser is redirected to a clean application URL so the secret is not retained in ordinary navigation/history longer than necessary. Sensitive tokens must be excluded from application logs, analytics, traces, referrers and screenshots.

QR and camera entry always have an equivalent manual code/link path.

## Participation creation/claim

Possession of an invitation can at most satisfy the specific enrollment/claim condition encoded by the server-side invitation record. The user must still authenticate/reverify, resolve a stable MUDAC Identity, and pass current Competition/Participation rules.

Where a Participation was pre-created, the claim associates the authenticated Identity only after server validation. Where current policy permits invitation-authorized enrollment, the server executes the normal Participation `enroll` action rather than creating an alternate invitation-owned role record.

# Identity recovery and principal linking

Credential recovery and MUDAC Identity recovery are distinct.

## Provider credential recovery

Password/passkey/MFA/account recovery that leaves the same Cognito subject intact is primarily delegated to the managed provider. After successful provider recovery, MUDAC resolves the same explicit principal link and therefore the same MUDAC Identity.

## MUDAC principal-link recovery

If a provider subject must be newly linked/replaced, MUDAC uses an explicit recovery/link operation. It must never infer sameness from matching email/name alone.

A recovery/link operation requires:

- stronger current proof or an explicitly authorized recovery process;
- confirmation that the new provider principal is not linked elsewhere;
- attributable reason/evidence;
- revocation of affected existing sessions;
- append-stable Provenance linking the old/new principal relationship where appropriate;
- preservation of the same MUDAC Identity and its historical Participation/authorship when recovery is legitimate.

Identity merge between two already-established MUDAC Identities is **not** an ordinary recovery shortcut. It remains a separately governed exceptional operation and is not required in the first implementation slice unless later planning establishes a safe authority policy.

# Reverification and step-up

Authentication assurance is represented separately from Access.

The session retains enough validated authentication-time/assurance information for protected operations to determine whether a fresh provider proof is required.

Step-up/reverification is required as configured for operations such as:

- post-event Judge correction access;
- credential/principal linking or recovery;
- sensitive role-context transitions where policy requires it;
- break-glass activation;
- later high-consequence Organizer actions identified by 008-K/008-J.

Passing step-up proves fresher principal control only. It does not create Participation, capability, Finalization authority, authorship, or disclosure permission.

# Technical/operator authority

MUDAC keeps technical operation separate from Competition semantic authority at both AWS and application boundaries.

## Runtime/deployment roles

API runtime, worker runtime, migration, deployment, backup/restore and observability privileges remain distinct least-privilege technical identities under `AWS-010`/`AWS-011`.

The ordinary API runtime does not receive migration/DDL or unrestricted break-glass permissions merely because it can authenticate users.

## Application support/break-glass

If application-level support or emergency access is later implemented, it uses a separate technical-authority path with explicit operator principal identity, stronger authentication, bounded capability/resource/time, reason, expiry and security audit evidence.

It does **not** synthesize an Organizer/Judge Participation and does not create a session that impersonates another user's semantic Identity.

Baseline support tooling therefore does not include a generic `impersonate user` or `become organizer` control.

When technical intervention facilitates a legitimate semantic action, Provenance still identifies the actual semantic author/authorizer separately from the technical actor.

# Secrets and protected configuration

Production secrets are never committed to the repository or delivered to browser JavaScript.

Secrets Manager is the baseline store for protected server/runtime secrets such as database credentials and any Cognito confidential-client secret. ECS runtime/deployment identities receive only the secrets required for their function.

Opaque session and invitation tokens are generated from a CSPRNG and persisted only as one-way digests; they do not require a shared plaintext signing secret merely to validate bearer possession.

Local development uses ignored local configuration and deterministic fake-provider/test credentials. Synthetic local secrets must never be mistaken for production defaults.

Secret values are excluded from logs, Provenance, outbox payloads, error responses and generated API/browser artifacts.

Rotation is designed around replaceable references/current+next provider capability where supported rather than requiring source changes or production downtime. Exact rotation cadence and operational evidence belong to 008-K.

# Identity-access package boundary

`@mudac/identity-access` owns:

- Identity state and provider-principal linkage;
- Participation state/lifecycle;
- Access-owned capability/grant evaluation;
- server session state;
- invitation/claim state that establishes or routes Participation intent;
- authentication-provider adapter ports;
- owner-local persistence and Provenance for those subjects.

It does **not** own:

- Competition lifecycle/configuration;
- Panel membership or effective Encounter participation;
- Scorecard authorship/content;
- outcome/finalization semantics;
- Export/Publication disclosure semantics;
- HTTP transport status/error vocabulary;
- browser local-Draft storage;
- AWS operator/deployment IAM policy semantics.

Cross-module consumers use public Identity/Participation/Access references and checks. They do not import identity-access tables or provider SDK objects.

# Verification consequences

When an executable slice is later authorized, 008-E requires evidence for at least:

- issuer+subject linkage and rejection of email/name-based silent merge;
- authorization-code state/nonce/PKCE replay/mismatch failure;
- opaque server-session creation, rotation, expiry and revocation;
- provider tokens absent from browser storage and normal application logs;
- explicit dual-role Participation selection with no capability union;
- Identity disablement and Participation withdrawal/completion removing current capability;
- Event Completed ending ordinary Judge private-evaluation Access despite a live cookie;
- temporary post-event correction grants remaining resource/capability/time bounded;
- invitation expiry/revocation/replay and atomic claim behavior;
- device/session revocation preserving stable Identity/Participation/Scorecard identity;
- step-up increasing assurance without creating capability;
- technical/support authority failing semantic Judge/Organizer-authority checks;
- Secrets/configuration not leaking into browser bundles, logs, fixtures or source;
- real Cognito nonproduction smoke/contract evidence for provider behavior that deterministic fakes cannot prove.

PostgreSQL-sensitive tests use real disposable PostgreSQL under the canonical verification strategy. Provider adapter unit/contract tests use deterministic fakes, with targeted real Cognito integration evidence where provider semantics matter.

008-K later owns the full security/privacy abuse matrix, production session/reverification thresholds, secret-rotation evidence, monitoring and release gate.

# Downstream handoff

008-F may now assume:

- authenticated browser requests resolve through an opaque server session;
- server-derived Identity and exactly one selected Participation context are available to command/query boundaries;
- client-supplied actor/role/Identity claims are never authoritative;
- ordinary Access is contextual, not database RBAC alone;
- explicit grants are retained and scope/time/resource bounded;
- successful authentication/step-up does not create semantic capability;
- session revocation and authority revocation are distinct but compose;
- Identity/Participation/Access persistence follows the accepted 008-D ownership/history conventions.

008-F still owns the concrete HTTP middleware/command envelope, CSRF mechanism, transaction composition, error classes, idempotency and lost-response behavior.

# Execution status

```text
identity/auth/access/session implementation contract: ACCEPTED
Cognito infrastructure: NOT PROVISIONED
Identity/Participation/Access schema: NOT IMPLEMENTED
login/session/invitation behavior: NOT IMPLEMENTED
first executable domain slice: NOT YET AUTHORIZED
```

No new domain implementation begins until 008-L explicitly authorizes a Phase 009 slice.

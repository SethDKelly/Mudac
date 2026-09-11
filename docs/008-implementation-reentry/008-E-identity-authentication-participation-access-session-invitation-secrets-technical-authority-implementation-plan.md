---
type: Implementation Planning Record
title: 008-E — Identity, Authentication, Participation, Access, Session, Invitation, Secrets & Technical-Authority Implementation Plan
description: Resolves the implementation decisions assigned to Identity/Participation/Access/authentication/session planning while preserving provider neutrality, current contextual authority, role isolation, invitation/recovery safety, secret boundaries, and technical-versus-semantic authority separation without beginning implementation.
status: stable
tags: [phase-008, implementation-planning, identity, authentication, participation, access, session, invitation, secrets, technical-authority]
sources:
  - resource: 008-D-persistence-temporal-truth-versioning-provenance-governed-exceptions-outbox-projection-migration-implementation-plan.md
  - resource: 008-C-residual-risk-ingestion-historical-006-mapping-decision-register-supersession-matrix.md
  - resource: ../canonical/governance/design-implementation-boundary.md
  - resource: ../canonical/architecture/identity-access-session.md
  - resource: ../canonical/architecture/application-boundaries.md
  - resource: ../canonical/architecture/data-persistence.md
  - resource: ../canonical/architecture/commands-api-concurrency.md
  - resource: ../canonical/architecture/aws-runtime-operations.md
  - resource: ../canonical/concepts/identity.md
  - resource: ../canonical/concepts/participation.md
  - resource: ../canonical/concepts/access.md
  - resource: ../canonical/experience/judge-onboarding.md
  - resource: ../canonical/implementation/persistence-history-projection.md
  - resource: ../canonical/implementation/identity-authentication-access-session.md
  - resource: ../canonical/implementation/verification-strategy.md
  - resource: https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-client-apps.html
  - resource: https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-security-best-practices.html
  - resource: https://docs.aws.amazon.com/cognito/latest/developerguide/federation-endpoints-oauth-grants.html
generated: { by: openai/gpt-5.6-sol, at: 2026-09-11T00:40:00Z }
---

# Purpose

Turn 008-C's Identity/authentication/session/Access residual assignment and the accepted 008-D persistence substrate into an implementation-ready plan without creating Cognito infrastructure, database schema, login behavior, session cookies, invitations, or domain commands.

008-E must make the following distinctions mechanically unavoidable for later implementation:

```text
authenticated principal ≠ MUDAC Identity
MUDAC Identity ≠ Participation
Participation ≠ Access
Access ≠ semantic authorship/decision authority
session ≠ authorization authority
step-up ≠ new capability
technical privilege ≠ Competition authority
```

# Result

**PASS — the provider, principal-link, Identity/Participation/Access, session, invitation/recovery/reverification, secrets, and technical-authority implementation decisions required before 008-F are sufficiently resolved.**

The durable current implementation result is promoted to [Identity, Authentication, Participation, Access, Session, Invitation, Secrets & Technical Authority Implementation Contract](../canonical/implementation/identity-authentication-access-session.md).

008-E remains planning only. No new domain implementation or AWS application resource is introduced.

Current posture:

```text
Jackson Concept Design: COMPLETE / EXITED
008-A: COMPLETE
008-B: COMPLETE
008-C: COMPLETE
008-D: COMPLETE
008-E: COMPLETE — identity/auth/access/session plan accepted
008-F: NEXT
protected 006-D baseline: QUALIFIED
first executable domain slice: NOT YET AUTHORIZED
new domain implementation after 006-D: NOT STARTED
production readiness: NOT ESTABLISHED
```

# Upstream authority consumed

008-E consumes rather than redefines:

- `AUTH-001` through `AUTH-014` for provider neutrality, Identity linkage, Participation context, contextual Access, opaque sessions, event-completion expiry, invitations, role isolation, correction access, device recovery, break-glass and step-up;
- `ACC-001` and `ACC-002` for contextual capability and non-transfer of semantic authority;
- Identity, Participation and Access Concept state/actions;
- Judge Onboarding's QR/event-entry, returning-Judge and current-event requirements;
- `DATA-*` and the accepted 008-D module-owned PostgreSQL/history/migration model;
- `API-*` separation of server-derived actor context from client transport claims;
- `AWS-006` Cognito selection and `AWS-010`/`AWS-011` least-privilege/secrets/deployment boundaries.

No upstream semantic contradiction was found.

# Residual I3-02 closure

008-C assigned **I3-02 Authentication/session/Access implementation** to 008-E.

**CLOSED FOR IMPLEMENTATION PLANNING.**

The complete realization is now decomposed into:

```text
Cognito/OIDC adapter
      ↓
provider principal link
      ↓
MUDAC Identity
      ↓
Competition Participation
      ↓
opaque MUDAC session + selected Participation context
      ↓
Access-owned capability/grant check
      ↓
resource-owner preconditions
```

This is sufficient for 008-F to define HTTP/command/query authorization mechanics without inventing identity semantics.

# Decision 1 — Cognito remains an adapter, not the identity model

The initial provider is Amazon Cognito User Pools as already selected by `AWS-006`.

The browser human-authentication flow uses OIDC/OAuth authorization code. Implicit grant is not part of the baseline. Current AWS documentation confirms authorization-code support and recommends code-flow/PKCE patterns over implicit token delivery; Cognito app clients also support server-side confidential-client secrets when the backend can protect them.

008-E requires:

- authorization-code flow;
- fresh state and nonce validation;
- PKCE per authorization attempt;
- exact callback allowlisting;
- server-side token exchange/validation;
- no provider bearer tokens in script-readable browser storage.

The provider adapter exposes normalized external-principal/assurance results rather than Cognito SDK/token objects to MUDAC module code.

# Decision 2 — durable MUDAC identity uses explicit issuer/subject linkage

A successful provider callback does not search by email or name.

The durable link is:

```text
provider/issuer + external subject
        ↓
MUDAC Identity ID
```

The combination is unique across current links.

Email may be retained only when product/recovery/contact needs justify it. It remains a mutable attribute and never becomes the database identity key.

Provider role/group claims are not MUDAC Participation or Access authority.

# Decision 3 — Identity and principal-link storage stay inside `identity_access`

008-D already established the owner schema. 008-E plans owner-local records for:

```text
identity
auth_principal_link
participation
access_grant + retained revocation/correction evidence
session
authentication transaction state
invitation / participation-claim state
identity-access Provenance
```

These are logical record families, not authorization to create migrations now.

No cross-module Identity table access is permitted. Other modules consume stable IDs and public Identity/Participation/Access contracts.

# Decision 4 — one Participation per Identity × Competition × role

A returning person reuses Identity but receives a new Competition Participation.

For the current baseline, logical uniqueness is:

```text
Identity + Competition + Participation role
```

Judge and Organizer dual-role therefore produces two stable Participation IDs. It never becomes one Participation containing a role array.

Participation lifecycle and current declared metadata are mutable root state with 008-D revision/concurrency tokens plus meaningful Provenance. They are not semantic Versioning snapshots unless a future canonical change says otherwise.

# Decision 5 — session context selects one Participation, never a union

One session may remember one selected Participation for usability.

A dual-role Identity explicitly changes context. Context switch requires current server validation and session rotation because it changes the active privilege/disclosure context.

The next command records the actual Participation used in Provenance. There is no hidden combined Judge+Organizer authorization context.

This preserves `AUTH-009` and prevents UI mode/state from becoming an alternate authority model.

# Decision 6 — Access is contextual composition, not generic RBAC

008-E rejects a generic database-driven role/permission matrix as the source of MUDAC authority.

Typed capability identifiers exist as implementation/public-contract vocabulary, but authorization composes:

```text
current Identity
current selected Participation
Competition scope/lifecycle
requested capability
explicit Access grant/revocation
purpose/time
resource-owner relationship/authorship/lifecycle rules
```

`@mudac/identity-access` owns the Access portion of that evaluation. A resource-owning module remains responsible for final semantic preconditions.

Example consequence:

```text
Access may say current Judge Participation can attempt evaluation editing
        +
Evaluation must still establish that this Participation is the author/eligible participant
for this exact Scorecard/Encounter/Rubric Version and current lifecycle state
```

This avoids both capability duplication and a central authorization god-service.

# Decision 7 — exceptional Access grants are immutable scoped authority

Explicit Access grants support cases such as post-event Judge correction.

The implementation stores the grant as retained authority with explicit:

- Identity and intended Participation;
- Competition;
- capability;
- target resource/scope;
- purpose/reason;
- validity interval;
- issuer/authorizer;
- recorded time and Provenance.

Revocation/correction is retained separately instead of deleting or silently rewriting the historical grant.

Grant validity is still conditional on current source state. A valid-looking row cannot restore a disabled Identity or invent Judge authorship.

# Decision 8 — Event Completed invalidates ordinary Judge capability from source state

No explicit bulk session rewrite is required to make Event Completed authoritative.

The Access check reads current Competition/Participation/resource state. Therefore a stale cookie/session cannot preserve ordinary private Judge access after Event Completed.

Session revocation may be performed additionally for security/cleanup, but source-state Access denial is the correctness mechanism.

This distinction is important because session revocation is technical state while Event Completed is semantic source state.

# Decision 9 — first-party sessions use PostgreSQL, not a new distributed cache

008-E selects PostgreSQL-backed opaque server sessions in `identity_access`.

There is no current evidence justifying Redis, DynamoDB or another session authority store.

The browser cookie contains only a high-entropy opaque token. The database stores its one-way digest plus server session metadata.

Planned production cookie properties:

```text
Secure
HttpOnly
Path=/
no Domain
__Host- prefix where final origin topology permits
intentional SameSite
```

008-F owns the CSRF mechanism and final mutation-request composition.

# Decision 10 — session lifetime and authority lifetime remain independent

The session record contains Identity, selected Participation, authentication/reverification timestamps, idle/absolute expiry, last-seen/security revision and revocation state.

Exact production idle/absolute values are **not** invented in 008-E. They are security configuration that 008-K must select/test against event continuity and shared-device risk.

This is safe because every protected operation rechecks current authority; a technically live session can exist while a formerly available capability is denied.

Session identifiers rotate after:

- successful login;
- principal recovery/relinking;
- meaningful Participation/privilege context change;
- other fixation-sensitive transitions identified by 008-K.

Logout/revocation invalidates server session state, not merely the browser cookie.

# Decision 11 — provider tokens are transient by default

The authorization-code exchange yields provider tokens, but MUDAC does not persist them by default after it has validated the external principal and established its own session.

This avoids treating Cognito token expiry/refresh as MUDAC Access lifecycle and reduces credential storage.

If a future provider operation genuinely requires a refresh/access token, that requires an explicit decision defining storage, encryption, rotation, revocation and purpose.

Reverification/step-up normally performs a fresh provider round trip rather than silently refreshing a long-lived application bearer credential.

# Decision 12 — authentication transactions are single-use server state

OIDC state/nonce/PKCE reconciliation uses a short-lived server-side authentication-transaction record or equivalently protected server-owned state.

It is consumed once and expires quickly. It holds only what is necessary for callback validation and a validated local return destination.

Callback query parameters alone never determine Identity or post-login authorization.

# Decision 13 — invitation URLs hold secrets, not authority

008-E distinguishes:

```text
route-only entry
bounded Participation-claim invitation
```

A route-only QR/code resolves Competition onboarding context and carries no enrollment capability.

A claim-capable invitation uses a high-entropy one-time/limited-use secret stored only as a digest. The server-side invitation record determines Competition, role, optional Participation/recipient restrictions, issuing authority, expiry, revocation and use limit.

The authenticated Identity must still pass current-state validation before Participation can be established/claimed.

Claim occurs atomically so concurrent/replayed use cannot create duplicate Participation authority.

After exchange, routing removes the secret from ordinary application navigation. Tokens are excluded from logs, analytics, traces and screenshots where practical.

A manual code/link path remains available wherever QR/camera entry is offered.

# Decision 14 — invitation flow reuses Participation actions

Invitation is not a parallel role model.

If the Organizer has pre-created a Participation, claim associates the authenticated Identity under the allowed claim rules.

If current policy permits invitation-authorized enrollment, the application invokes the normal Participation `enroll` semantics. It does not insert a second invitation-owned membership table and later infer that it means Participation.

# Decision 15 — provider recovery and MUDAC recovery remain separate

Ordinary credential reset/recovery within Cognito that preserves the external subject is delegated to the managed provider. The existing issuer/subject link resolves the same MUDAC Identity afterward.

A genuinely new/replaced provider subject requires explicit MUDAC principal-link recovery. Matching email/name alone is insufficient.

Recovery must include strong proof or a specifically authorized recovery process, principal uniqueness checks, session revocation, attributable reason/evidence and preserved Identity history.

Merging two already-established MUDAC Identities is intentionally **not** admitted as a routine recovery implementation. If future operations require Identity merge, it needs separate authority/design rather than a convenience database update.

# Decision 16 — step-up changes assurance, not capability

The session retains current authentication/reverification assurance metadata.

A protected operation may require fresh provider proof, particularly post-event correction, credential linking/recovery, sensitive context changes, and break-glass use.

008-K/008-J may later assign additional actions to explicit step-up thresholds.

Passing step-up cannot independently create:

- Participation;
- Scorecard authorship;
- Organizer authority;
- Finalization capability;
- Award authority;
- disclosure permission.

# Decision 17 — baseline technical authority does not impersonate users

AWS runtime/deployment/migration/observability roles remain separate technical principals under `AWS-010`/`AWS-011`.

If application-level support/break-glass capability is later needed, it uses a separately authenticated technical-operator path with bounded capability/resource/time and audit evidence.

008-E explicitly rejects generic baseline controls such as:

```text
impersonate Judge
impersonate Organizer
become Organizer
force Access
```

Technical intervention may enable infrastructure or a legitimate authorized workflow, but it cannot manufacture the semantic human authority required by a protected action.

# Decision 18 — secrets remain server-side and purpose-scoped

Secrets Manager is the planned production store for server secrets including database credentials and any Cognito confidential-client secret.

Opaque session/invitation tokens are random bearer secrets whose database representations are one-way digests; no plaintext token ledger is required.

Secrets are excluded from:

- repository source;
- browser bundles/storage;
- Provenance;
- outbox payloads;
- normal logs/traces/errors;
- test fixtures committed to source.

Local development uses ignored synthetic configuration and a deterministic authentication-provider fake.

Exact production rotation cadence/evidence belongs to 008-K.

# Cognito client posture

008-E plans a server-backed human browser client using the authorization-code flow.

A confidential client secret is permitted because token exchange happens through the trusted server application; if configured, the secret is stored in Secrets Manager and never emitted to browser code.

PKCE remains required for each authorization attempt as an additional proof binding the authorization request to the code exchange.

The provider app client exposes only the OAuth/OIDC scopes required by the actual MUDAC login/profile need. Provider scopes/groups are never interpreted as MUDAC domain capability by themselves.

No M2M/client-credentials flow is needed for the human MUDAC browser session. Machine/technical AWS authority remains IAM/service identity rather than pretending to be a human Participation.

# Planned identity-access data families

008-E does not write migrations, but fixes enough logical ownership for future schema work:

| Record family | Owner | Authority/history posture |
| --- | --- | --- |
| Identity | `identity_access` | mutable current root + Provenance; never hard-delete historical attribution |
| Authentication principal link | `identity_access` | stable issuer/subject → Identity link; explicit link/recovery history |
| Participation | `identity_access` | mutable current root + lifecycle Provenance; one per Identity/Competition/role |
| Access grant | `identity_access` | retained scoped authority; expiry/revocation/correction preserved |
| Session | `identity_access` | mutable technical security state; not domain authority/history source |
| Authentication transaction | `identity_access` | short-lived single-use technical state |
| Invitation/claim | `identity_access` | scoped secret-backed entry/claim mechanism; claim produces normal Participation semantics |
| Identity-access Provenance | `identity_access` | append-stable meaningful authority/origin history |

No record family grants cross-module mutation access.

# Command/query handoff shape for 008-F

008-F may now assume the server can resolve an application context conceptually containing:

```text
session identity
MUDAC Identity ID/status
selected Participation ID/role/Competition
current authentication/reverification assurance
relevant explicit Access grants
technical/support principal context separately when applicable
```

The context is **server-derived**.

A client-supplied Identity ID, role, Participation ID, Cognito group, email, session metadata or technical-operator label cannot replace it.

008-F still determines:

- Fastify middleware/plugin boundaries;
- CSRF strategy;
- command/query context interfaces;
- transaction placement;
- CAS/idempotency;
- status/error/result mapping;
- lost-response reconciliation;
- authorization denial/concealment transport behavior.

# Browser handoff for 008-G

008-G may assume:

- the browser gets an opaque first-party cookie rather than provider bearer credentials;
- current Identity/Participation/context information comes from authenticated server queries;
- role/context switch is explicit and server-confirmed;
- private cached state must be partitioned/cleared on context switch/logout/Access expiry;
- stale UI controls never extend server authority.

008-G still owns the browser storage/cache/recovery mechanics.

# Security and verification plan

When the first applicable executable slice is eventually authorized, evidence must cover the risks created by this plan.

## Provider/link evidence

Verify:

- state/nonce/PKCE mismatch/replay fails;
- issuer/audience/signature/time checks reject invalid proof;
- issuer+subject links deterministically to Identity;
- matching email/name does not silently merge Identity;
- principal-link uniqueness prevents one external principal from mapping to two current Identities;
- real Cognito nonproduction behavior agrees with the adapter contract where vendor semantics matter.

## Participation/Access evidence

Verify:

- dual-role contexts never union capability sets;
- Participation switch revalidates current state and rotates session identity;
- Identity disable/Participation withdrawal or completion removes applicable capability;
- Event Completed denies ordinary Judge private evaluation access even with an otherwise-live session;
- post-event correction grant is target/capability/time constrained and does not transfer authorship;
- resource-owning modules still reject invalid relationship/lifecycle state after Access-owned checks.

## Session/device evidence

Verify:

- opaque cookie properties and token-digest storage;
- login/context/recovery rotation;
- idle/absolute expiry once 008-K selects thresholds;
- server logout/revocation;
- replacement-device authentication resolves the same stable Identity/Participation;
- shared-device/logout paths do not leave the next user with the prior context.

## Invitation/recovery evidence

Verify:

- invitation expiry/revocation/usage limits;
- atomic one-time claim and replay/concurrency behavior;
- route-only codes cannot create Participation;
- invite secret does not become persistent navigation/log evidence;
- recovery does not use email/name alone to relink Identity;
- recovery revokes affected sessions and preserves historical attribution.

## Technical-authority/secrets evidence

Verify:

- support/deployment/migration authority cannot pass semantic Judge/Organizer checks;
- no generic user impersonation path exists in the baseline;
- provider/database secrets do not enter browser bundles, source, logs, Provenance or outbox payloads;
- ordinary API runtime lacks migration/break-glass permissions when those AWS roles are implemented.

Real PostgreSQL is required for session/token uniqueness, invitation claim concurrency, grant lifecycle and persistence-sensitive tests. Deterministic provider fakes support ordinary tests; targeted Cognito integration proves provider-specific behavior.

008-K later consolidates abuse/threat analysis, production session/step-up thresholds, secret rotation, security monitoring and release-readiness evidence.

# Open decisions intentionally left downstream

008-E does not need to invent every future security parameter.

| Open detail | Owner | Reason |
| --- | --- | --- |
| Exact idle/absolute session durations | 008-K | depends on threat/event continuity evidence; authority checks remain current regardless |
| Exact actions requiring fresh step-up beyond canonical cases | 008-J/008-K | depends on high-consequence workflow/security classification |
| Final SameSite + CSRF composition | 008-F | transport/origin mutation boundary |
| HTTP login/callback/logout/context-switch route hierarchy | 008-F | transport contract detail |
| Browser cache clearing/partition implementation | 008-G | browser/local-state owner |
| Cognito/RDS secret/IAM IaC resources | later authorized Phase 009 + 008-K gates | not executable in Phase 008 |
| Identity merge policy/tooling | future `CHG-*`/design if needed | unsafe to infer from ordinary recovery |

These are not blockers for 008-F because their required authority boundaries are already fixed.

# No semantic redesign required

008-E did not discover a missing Concept or require changing Identity, Participation, Access, Judge Onboarding, technical-authority, correction, or temporal semantics.

The implementation plan fits the existing architecture cleanly:

```text
managed authentication outside semantic ownership
stable MUDAC Identity inside identity-access
Competition-scoped Participation
contextual Access
server session as convenience/security state
resource owner as final semantic gate
```

# Exit criteria

008-E passes because:

- provider flow and adapter boundary are selected;
- durable external-principal linkage is explicit and email-independent;
- Identity and Participation physical ownership is clear;
- dual-role context isolation is mechanically defined;
- Access is contextual and resource-owner preserving;
- temporary grants/revocation history is planned;
- Event Completed cannot be bypassed by stale sessions;
- opaque server-session storage/rotation/revocation is defined;
- invitations are secret-backed bounded claim mechanisms, not authority by possession;
- recovery/reverification semantics preserve stable Identity and do not merge by email;
- technical/break-glass authority cannot synthesize Competition authority;
- secret storage/exposure boundaries are defined;
- 008-F receives a concrete server-derived principal/context contract;
- no implementation was started.

# Handoff

Proceed to **008-F — Commands, Queries, Transactions, CAS, Idempotency, Concurrency, Lost-Response Reconciliation & API Implementation Plan**.

008-F must consume the accepted 008-D persistence contract and 008-E identity/session context rather than redefining either inside transport code.

No executable domain slice is authorized until 008-L; new domain implementation remains **NOT STARTED**.

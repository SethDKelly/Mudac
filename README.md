# MUDAC Competition Demo

MUDAC is a design-governed web application effort for fair, traceable, resilient judging at live student data competitions.

Student Teams present analyses to Panels of volunteer Judges. Each Judge independently authors a Rubric-based Scorecard in a Judging Encounter; authoritative Scorecards feed explicit Coverage, aggregation, ranking, Awards, and controlled official-closeout semantics while preserving Judge independence, provenance, anonymity, accessibility, and paper continuity.

## Start here

* [`AGENTS.md`](AGENTS.md) — repository-agent bootstrap and current Phase 008 execution boundary.
* [`docs/index.md`](docs/index.md) — preferred OKF progressive-disclosure entry point.
* [`docs/canonical/`](docs/canonical/) — current product/domain, synchronization, temporal/correction, UX, governance, architecture, and implementation authority.
* [`docs/canonical/governance/design-implementation-boundary.md`](docs/canonical/governance/design-implementation-boundary.md) — current planning/execution authority boundary.
* [`docs/canonical/implementation/persistence-history-projection.md`](docs/canonical/implementation/persistence-history-projection.md) — accepted 008-D persistence/history/outbox/projection/migration implementation contract.
* [`docs/canonical/implementation/identity-authentication-access-session.md`](docs/canonical/implementation/identity-authentication-access-session.md) — accepted 008-E identity/authentication/Participation/Access/session/invitation/secrets/technical-authority implementation contract.
* [`docs/008-implementation-reentry/`](docs/008-implementation-reentry/) — active implementation re-entry, plan refresh, and execution-readiness phase.

Numbered phase directories preserve rationale and planning history; canonical owners govern current meaning.

## Status

* Phase 001 — Concept Design Foundation: **Complete**
* Phase 002 — Concept Specification: **Complete**
* Phase 003 — Conceptual UX Architecture: **Complete**
* Phase 004 — Knowledge Architecture / OKF Governance: **Complete**
* Phase 005 — System/Application/Data/Synchronization Architecture: **Complete as historical architecture exit**
* Phase 006 — Implementation Planning & Delivery: **Historical after 006-D**
* Phase 007 — Jackson Design Refinement & Methodology Closure: **Complete — formal methodology exit passed**
* Phase 008 — Implementation Re-entry, Plan Refresh & Execution Readiness: **In Progress**
  * 008-A through 008-E: **Complete**
  * 008-F — Commands, Queries, Transactions, CAS, Idempotency, Concurrency, Lost-Response Reconciliation & API Implementation Plan: **Next**

## Current posture

The renewed Jackson Concept Design methodology is complete for the current MUDAC baseline. Implementation planning is active, but no executable domain slice has yet been authorized.

008-B qualified the retained 006-D executable substrate. 008-C reconciled every accepted residual/historical-plan item. 008-D accepted the physical persistence/history implementation contract. 008-E now accepts the authentication-to-authority implementation contract while leaving the executable baseline unchanged and free of domain schema/authentication behavior.

The current boundary is:

```text
Jackson Concept Design methodology: COMPLETE / EXITED
implementation planning authority: ESTABLISHED
008-A: COMPLETE
008-B: COMPLETE — PASS AFTER NARROW REMEDIATION
008-C: COMPLETE — PASS
008-D: COMPLETE — PASS
008-E: COMPLETE — PASS
protected 006-D baseline: QUALIFIED FOR PHASE 008 PLANNING
persistence/history implementation plan: ACCEPTED / NOT IMPLEMENTED
identity/auth/access/session implementation plan: ACCEPTED / NOT IMPLEMENTED
008-F: NEXT / NOT STARTED
first executable domain slice: NOT YET AUTHORIZED
new domain implementation after 006-D: NOT STARTED
production readiness: NOT ESTABLISHED
```

A qualified bootstrap or accepted implementation plan is not implementation authorization. Phase 008 remains planning, qualification, reconciliation, and authorization work. Only 008-L may authorize a first executable domain slice, and actual new domain implementation then begins in Phase 009.

## Accepted persistence direction

008-D fixes one module-owned PostgreSQL authority database, current state distinct from immutable semantic Version/history records, module-local Provenance, policy-specific governed exceptions, immutable Official Outcome Revision substrate, transactional at-least-once outbox, basis-aware projections, SQL-first forward migrations, and conservative historical retention.

Technical root revision is not a semantic Version. Queue/outbox ordering is not authoritative commit ordering.

## Accepted identity/authentication direction

008-E fixes the following authority path:

```text
Cognito/OIDC authentication proof
   ↓
explicit issuer/subject link
   ↓
MUDAC Identity
   ↓
selected Competition Participation
   ↓
contextual Access
   ↓
resource-owner semantic preconditions
```

Cognito groups/claims, mutable email/name, session state, invitation possession, successful step-up, or technical/operator privilege cannot skip this chain.

The planned browser authentication uses authorization-code flow with state/nonce/PKCE and server-side exchange. Provider bearer tokens are not placed in ordinary browser storage and are transient by default after the opaque first-party MUDAC session is created.

One Participation exists per Identity × Competition × role. Dual-role people explicitly select one Participation context rather than receiving a union of Judge and Organizer capability sets. Ordinary Access remains current/contextual; explicit grants are bounded and retained. Event Completed ends ordinary Judge private-evaluation capability from source-state authorization even when a cookie remains technically valid.

Sessions are planned as PostgreSQL-backed opaque server state. Invitations are bounded routing/Participation-claim mechanisms, not Identity/Access authority by possession. Provider credential recovery is separate from explicit MUDAC Identity relinking. Technical/support/break-glass authority cannot synthesize Judge/Organizer semantic authority, and baseline support does not impersonate users.

No Cognito resources, Identity/Participation/Access schema, login/session behavior, invitation flow, or secrets infrastructure has been implemented.

## Reconciled implementation-plan direction

```text
008-D persistence / temporal / history / provenance / exception / outbox   COMPLETE
   ↓
008-E Identity / Participation / Access / session                          COMPLETE
   ↓
008-F commands / queries / transactions / CAS / idempotency / API          NEXT
   ↓
008-G browser / Draft / synchronization / recovery
   ↓
008-H Competition + Judging Operations
   ↓
008-I Scorecard + evaluation evidence + amendment + paper
   ↓
008-J outcomes + Finalization + official outcome + Export + Publication
   ↓
008-K cross-cutting evidence / operations / retention
   ↓
008-L roadmap + first-slice authorization
   ↓
Phase 009 implementation
```

Repository protection remains an external administration/evidence limit: no repository rulesets are currently visible and branch-protection state cannot be read through the connected integration. Dependabot is configured, but its alert inventory is unavailable through the current connector. Those limitations remain assigned to 008-K/008-L.

## Current direction

Proceed to **008-F — Commands, Queries, Transactions, CAS, Idempotency, Concurrency, Lost-Response Reconciliation & API Implementation Plan**.

008-F remains planning only. New domain persistence/authentication/API implementation is not authorized until 008-L explicitly authorizes a Phase 009 entry slice.

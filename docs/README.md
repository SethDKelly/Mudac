# MUDAC Design Documentation

The repository is the durable design and implementation authority; conversation history is working context.

## Preferred navigation

Start at [index.md](index.md), the OKF v0.2 bundle root. Current product/domain, synchronization, temporal/correction, policy, UX, governance, architecture, and implementation meaning lives under [Canonical Knowledge](canonical/). Root [`AGENTS.md`](../AGENTS.md) is only a bootstrap adapter into those owners.

Use numbered phase directories for rationale, design evolution, alternatives, implementation planning, and provenance.

## Status

* Phase 001 — Concept Design Foundation: **Complete**
* Phase 002 — Concept Specification, Policy & Synchronization Refinement: **Complete**
* Phase 003 — Conceptual UX Architecture: **Complete**
* Phase 004 — Knowledge Architecture, OKF Retrofit & Documentation Governance: **Complete**
* Phase 005 — System, Application, Data & Synchronization Architecture: **Complete as historical architecture exit**
* Phase 006 — Implementation Planning, Delivery Slices & Verification Strategy: **Historical after 006-D; 006-E–M explicitly mapped/superseded by 008-C**
* Phase 007 — Jackson Design Refinement & Methodology Closure: **Complete — formal methodology exit passed**
* Phase 008 — Implementation Re-entry, Plan Refresh & Execution Readiness: **In Progress**
  * 008-A through 008-E: **Complete**
  * 008-F — Commands, Queries, Transactions, CAS, Idempotency, Concurrency, Lost-Response Reconciliation & API Implementation Plan: **Next**

## Current posture

MUDAC has formally exited the renewed Jackson Concept Design methodology for the current accepted baseline. Implementation planning is active; no executable domain slice has yet been authorized.

[008-D](008-implementation-reentry/008-D-persistence-temporal-truth-versioning-provenance-governed-exceptions-outbox-projection-migration-implementation-plan.md) fixes the persistence/history implementation substrate. [008-E](008-implementation-reentry/008-E-identity-authentication-participation-access-session-invitation-secrets-technical-authority-implementation-plan.md) now fixes the authentication-to-authority substrate.

The current status is:

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

## Accepted implementation substrates

Durable current persistence detail lives in [Persistence, History, Provenance, Outbox, Projection & Migration Implementation Contract](canonical/implementation/persistence-history-projection.md).

Durable current identity/authentication detail lives in [Identity, Authentication, Participation, Access, Session, Invitation, Secrets & Technical Authority Implementation Contract](canonical/implementation/identity-authentication-access-session.md).

008-E establishes Cognito as a replaceable authentication adapter, explicit issuer/subject linkage to stable MUDAC Identity, one Participation per Identity/Competition/role, explicit dual-role context selection, contextual Access rather than generic RBAC, bounded retained Access grants, source-state Event Completed capability expiry, PostgreSQL-backed opaque first-party sessions, replay-safe invitation/claim mechanics, separate credential-versus-Identity recovery, step-up without capability creation, and technical/operator authority that cannot synthesize Judge/Organizer authority.

No Cognito resources, schema, login/session code, invitation flow or Access behavior has been implemented.

## Phase 008 structure

```text
008-A authority / canonical baseline / change control          COMPLETE
   ↓
008-B protected substrate qualification                       COMPLETE
   ↓
008-C residual-risk + historical-plan reconciliation          COMPLETE
   ↓
008-D persistence / temporal / provenance / exception plan    COMPLETE
   ↓
008-E Identity / Participation / Access / session plan        COMPLETE
   ↓
008-F commands / API / transaction / concurrency plan         NEXT
   ↓
008-G browser / Draft / sync / recovery / accessibility plan
   ↓
008-H Competition + judging-operations slice plan
   ↓
008-I Scorecard + evaluation-evidence + paper slice plan
   ↓
008-J outcomes + finalization + representation slice plan
   ↓
008-K cross-cutting verification / operational evidence plan
   ↓
008-L consolidated roadmap + first-slice authorization
   ↓
Phase 009 implementation
```

No Phase 008 subgroup implements new domain behavior. If 008-L passes, Phase 009 will begin the first explicitly authorized domain implementation slice.

## Planning authority and change control

A qualified bootstrap, accepted implementation plan, first-slice authorization, code start, merge readiness, deployment readiness, and production readiness are separate states.

If implementation planning conflicts with current canonical meaning, the downstream mechanism changes by default. A genuine semantic contradiction, missing semantic owner, or intentional product change routes through `CHG-*`.

Phase 008 follows `CTX-*` progressive disclosure and `DOC-*` one-owner discipline. Durable 008-D and 008-E implementation meaning is canonicalized under `docs/canonical/implementation/`; numbered phase records preserve rationale and decisions.

## Current next work

Proceed to **008-F — Commands, Queries, Transactions, CAS, Idempotency, Concurrency, Lost-Response Reconciliation & API Implementation Plan**.

New domain implementation remains **not started** until 008-L explicitly authorizes the first executable slice.

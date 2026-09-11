---
type: Documentation Authority
title: Design / Implementation Boundary
description: Defines MUDAC's current post-Concept-Design posture, active Phase 008 planning authority, qualified protected 006-D baseline, accepted persistence and identity/authentication implementation contracts, and the explicit gate before new domain implementation begins.
status: stable
tags: [governance, methodology, design, implementation, boundary, jackson, planning]
sources:
  - resource: ../../007-design-refinement/007-I-formal-jackson-concept-design-methodology-exit-accepted-residual-uncertainty-implementation-resume-boundary-decision.md
  - resource: ../../008-implementation-reentry/README.md
  - resource: ../../008-implementation-reentry/008-A-implementation-reentry-authority-canonical-baseline-change-control-planning-guardrails.md
  - resource: ../../008-implementation-reentry/008-B-protected-006-D-baseline-qualification-drift-audit-toolchain-environment-reconciliation.md
  - resource: ../../008-implementation-reentry/008-C-residual-risk-ingestion-historical-006-mapping-decision-register-supersession-matrix.md
  - resource: ../../008-implementation-reentry/008-D-persistence-temporal-truth-versioning-provenance-governed-exceptions-outbox-projection-migration-implementation-plan.md
  - resource: ../../008-implementation-reentry/008-E-identity-authentication-participation-access-session-invitation-secrets-technical-authority-implementation-plan.md
  - resource: change-governance.md
  - resource: methodology-terminology.md
  - resource: ../synchronizations/concept-synchronizations.md
  - resource: ../synchronizations/temporal-truth-correction.md
  - resource: ../policies/operational-exception-governance.md
  - resource: ../experience/action-authority-traceability.md
  - resource: ../implementation/runtime-delivery-bootstrap.md
  - resource: ../implementation/implementation-foundation.md
  - resource: ../implementation/persistence-history-projection.md
  - resource: ../implementation/identity-authentication-access-session.md
generated: { by: openai/gpt-5.6-sol, at: 2026-09-11T00:40:00Z }
---

# Purpose

Keep the boundary between completed MUDAC Concept Design, active implementation planning, the qualified bootstrap substrate, future domain implementation, deployment authority, and production readiness explicit.

# Current state

MUDAC has formally exited the renewed Jackson Concept Design methodology for the current accepted baseline. 008-A established implementation-planning authority and guardrails. 008-B qualified the retained 006-D executable substrate. 008-C reconciled accepted residuals and historical 006-E–M into current owners. 008-D accepted the persistence/history implementation contract. 008-E has now accepted the Identity/authentication/Participation/Access/session/invitation/secrets/technical-authority implementation contract.

The governing status is:

```text
Jackson Concept Design methodology: COMPLETE / EXITED
baseline semantic design: COMPLETE
known baseline semantic blockers: NONE OPEN
Phase 008 subdivision: COMPLETE
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

The formal design exit is scoped to the current baseline. New scope or a genuine later contradiction may require renewed design under canonical change governance.

# Current planning authority

Phase 008 follows the authority direction established in 008-A:

```text
canonical product / synchronization / policy / mechanism /
invariant / experience / governance meaning
        ↓
canonical architecture
        ↓
canonical implementation contracts
        ↓
Phase 008 implementation-planning decisions
        ↓
future executable realization and evidence
```

The Design / Implementation Boundary separately owns **execution posture**.

Historical phase records provide rationale/provenance. Routing artifacts route. Code, tests, schema, generated artifacts and IaC realize downstream choices. None silently replaces its upstream owner.

# Qualified protected 006-D baseline

008-B audited the retained non-domain workspace against current authority and found no semantic, architectural, or accidental-domain-implementation blocker.

The baseline remains qualified for later Phase 008 planning and contains only the accepted bootstrap class:

- pinned Node/pnpm/TypeScript/application-tool manifests and committed lockfile;
- minimal API, worker and browser composition roots;
- six authoritative module package seams without domain behavior;
- `application`, `projections`, `foundation`, and `test-support` boundaries;
- Docker Compose PostgreSQL without authoritative MUDAC schema/migrations;
- CI/static/dependency enforcement and supply-chain configuration;
- separate OpenTofu nonproduction/production/recovery roots without AWS application resources.

Qualification means the substrate may be relied upon as **planning input**. It does not authorize domain extension of that substrate.

# Reconciled residual and historical-plan ownership

008-C closes the ambiguity around accepted downstream uncertainty.

All six 007-H Class 2 architecture details and all twelve Class 3 implementation/evidence questions have current Phase 008 owners. The two 008-B administration/evidence limitations are carried to 008-K/008-L. All seven Class 4 future-scope items remain outside the current baseline unless `CHG-*` deliberately reopens them.

Historical 006-E through 006-M is fully superseded as an executable roadmap. Its useful dependency rationale remains provenance, but current planning routes only through 008-D through 008-L.

# Accepted 008-D persistence implementation contract

008-D resolves the physical persistence choices needed by downstream planning while remaining non-executable.

Current implementation planning may assume one module-owned PostgreSQL authority database; stable UUID resource identities; monotonic mutable-root revisions; mutable current state distinct from immutable semantic Version history; module-local Provenance; explicit correction/invalidation/replacement; policy-specific governed exceptions; immutable Official Outcome Revision substrate; transactional at-least-once outbox; basis-aware rebuildable projections; SQL-first owner-scoped forward migrations; and conservative historical retention.

Durable detail is owned by [Persistence, History, Provenance, Outbox, Projection & Migration Implementation Contract](../implementation/persistence-history-projection.md).

These are **accepted planning constraints, not created database objects**.

# Accepted 008-E identity/authentication implementation contract

008-E resolves the physical authentication-to-authority chain needed by command/API planning while remaining non-executable.

Current implementation planning may assume:

```text
Cognito/OIDC authentication proof
        ↓
explicit provider/issuer + subject link
        ↓
stable MUDAC Identity
        ↓
exactly one selected Competition Participation context
        ↓
contextual Access/grant evaluation
        ↓
resource-owner semantic preconditions
```

The accepted realization includes:

- Cognito User Pools behind a provider adapter, using authorization-code authentication with state/nonce/PKCE and server-side exchange;
- no provider bearer tokens in script-readable browser storage and no default long-term provider-token retention after MUDAC session establishment;
- external principal linkage by provider/issuer + subject rather than email/name/group claims;
- one Participation per Identity × Competition × role and explicit dual-role context selection rather than unioned privileges;
- contextual Access rather than a generic database RBAC authority model;
- retained, resource/capability/time/purpose-bounded explicit grants;
- Event Completed source-state authorization overriding stale session/browser state for ordinary Judge private-evaluation capability;
- opaque PostgreSQL-backed first-party sessions with digest-only bearer-token storage, bounded lifetime, rotation and server revocation;
- bounded invitation/Participation-claim mechanisms whose possession alone does not grant Identity or Access;
- separate provider credential recovery and explicit MUDAC principal-link recovery, with no silent email/name merge;
- step-up/reverification as stronger proof rather than capability creation;
- technical/operator/break-glass authority distinct from Judge/Organizer semantic authority, with no baseline user impersonation mechanism;
- server-only secret storage/configuration boundaries.

Durable detail is owned by [Identity, Authentication, Participation, Access, Session, Invitation, Secrets & Technical Authority Implementation Contract](../implementation/identity-authentication-access-session.md).

These are **accepted planning constraints, not Cognito resources, session cookies, database tables, or implemented authorization behavior**.

# What Phase 008 planning authority permits

Current work may:

- use the qualified 006-D substrate as a concrete starting assumption;
- consume the 008-C residual/historical-plan ownership map;
- consume the accepted 008-D persistence/history implementation contract;
- consume the accepted 008-E server-derived Identity/Participation/Access/session contract;
- define concrete command/query/transaction/API, browser, vertical-slice, outcome/externalization and evidence mechanisms where upstream authority leaves implementation latitude;
- create implementation decision records where `IMPL-015` warrants them;
- update canonical implementation owners when durable downstream contracts change;
- define verification/evidence gates and explicit implementation-entry criteria;
- prepare a specifically bounded first domain implementation slice for 008-L authorization.

008-F is next and owns Commands, Queries, Transactions, CAS, Idempotency, Concurrency, Lost-Response Reconciliation & API implementation planning.

# What Phase 008 does not authorize

Completion of 008-A through 008-E does **not** authorize domain implementation.

Until **008-L — Consolidated Dependency Graph, Implementation Roadmap, First-Slice Authorization & Phase Exit Review** explicitly authorizes a first executable slice, do not create new:

- authoritative domain PostgreSQL schemas, migrations, repositories, outbox or projections described by 008-D;
- Cognito User Pools/app clients/domains, login/callback/session/Invitation/Identity/Participation/Access behavior described by 008-E;
- production domain commands, queries, APIs, transactions or idempotency behavior;
- IndexedDB domain Draft/synchronization behavior;
- Competition/Judging/Evaluation/Outcome/Award/Export/Publication feature behavior;
- domain-purpose AWS application provisioning/deployment.

The status distinctions remain:

```text
qualified bootstrap
    ≠
accepted implementation plan
    ≠
first executable slice authorized
    ≠
domain implementation started
    ≠
merge ready
    ≠
deployment ready
    ≠
production ready
```

008-L may authorize a Phase 009 entry slice. 008-L itself performs no domain implementation.

# Phase 006 treatment

Phase 006 remains historical implementation-planning/bootstrap provenance.

006-A through 006-D accurately record prior planning/bootstrap work. The executable portion of 006-D was re-qualified by 008-B rather than silently resumed.

006-E through 006-M remain preserved historical planning lineage but are fully superseded as current executable authority. Their explicit disposition is owned by 008-C. The persistence substance historically associated with 006-E is superseded by 008-D. The Identity/authentication/session/Access substance historically associated with 006-F is superseded by 008-E.

# Open evidence and administration limits

008-C carries the 008-B limitations forward to named owners:

1. repository rulesets/branch-protection enforcement remains an 008-K evidence/admin item and an 008-L authorization consideration;
2. Dependabot alert inventory remains unavailable through the current connector and is assigned to 008-K security evidence.

008-D leaves retention periods, backup/restore objectives, RDS sizing, migration deployment evidence and projection recovery exercises to 008-K.

008-E additionally leaves concrete production session idle/absolute durations, final step-up thresholds, secret-rotation evidence, abuse/threat testing and security monitoring to 008-K. 008-F owns final CSRF/origin composition; 008-G owns browser cache/private-state cleanup mechanics.

None of those details blocks continued planning because their required authority boundaries are already fixed.

# Change control during implementation planning

Completed Concept Design remains current semantic authority, not immutable dogma.

If planning or later implementation discovers a genuine canonical contradiction, missing independent Concept, impossible synchronization/authority requirement, unmodeled correction/history condition, or material new product scope, return through `CHG-*` and deliberate design as necessary.

If an implementation mechanism merely conflicts with current canonical meaning, the mechanism changes by default under `CHG-005` and `IMPL-001`.

Implementation inconvenience, framework preference, storage convenience, authentication-provider convenience, UI convenience, testing convenience, or technical/operator privilege alone does not authorize semantic weakening.

# Documentation and context boundary

Phase 008 follows `DOC-*` and `CTX-*`:

- canonical owners control durable current meaning;
- numbered Phase 008 records preserve planning rationale/evidence without becoming a parallel rule store;
- `persistence-history-projection.md` owns the durable 008-D implementation result;
- `identity-authentication-access-session.md` owns the durable 008-E implementation result;
- historical phases are loaded only when rationale, chronology, or supersession requires them;
- routing artifacts summarize and link rather than own rules;
- agents stop expanding context once the material authority set is sufficient.

# Current handoff

Proceed to **008-F — Commands, Queries, Transactions, CAS, Idempotency, Concurrency, Lost-Response Reconciliation & API Implementation Plan** under [Phase 008](../../008-implementation-reentry/).

008-F may rely on the accepted 008-D persistence contract and 008-E server-derived identity/access/session contract as planning inputs. New domain implementation remains **NOT STARTED** and no first executable slice is authorized until 008-L explicitly changes this boundary.

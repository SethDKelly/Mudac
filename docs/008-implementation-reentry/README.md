# Phase 008 — Implementation Re-entry, Plan Refresh & Execution Readiness

Status: **In Progress — 008-A/B/C/D/E complete; 008-F next**

## Purpose

Convert the completed Jackson Concept Design baseline and accepted architecture into a refreshed, dependency-safe implementation plan without beginning new MUDAC domain implementation.

Phase 008 exists because the historical 006-E through 006-M plan predates the Phase 007 methodology refinements. Those records remain planning provenance and dependency evidence, but they are not current executable authority.

Current execution posture is owned by [Design / Implementation Boundary](../canonical/governance/design-implementation-boundary.md). Detailed Phase 008 records are indexed in [index.md](index.md).

## Phase boundary

```text
Phase 007
Jackson Concept Design COMPLETE / EXITED
        ↓
Phase 008
plan refresh + execution readiness
        ↓
008-L explicit first-slice authorization
        ↓
Phase 009
new domain implementation begins
```

No Phase 008 subgroup implements new domain behavior. The retained 006-D workspace remains a qualified protected non-domain implementation baseline.

## Completed planning gates

[008-A](008-A-implementation-reentry-authority-canonical-baseline-change-control-planning-guardrails.md) is **Complete** and establishes current authority, `CHG-*` escalation, planning-versus-execution states, and progressive-disclosure/anti-bloat rules.

[008-B](008-B-protected-006-D-baseline-qualification-drift-audit-toolchain-environment-reconciliation.md) is **Complete — PASS AFTER NARROW REMEDIATION** and qualifies the retained 006-D executable substrate.

[008-C](008-C-residual-risk-ingestion-historical-006-mapping-decision-register-supersession-matrix.md) is **Complete — PASS** and closes residual/historical-plan ownership.

[008-D](008-D-persistence-temporal-truth-versioning-provenance-governed-exceptions-outbox-projection-migration-implementation-plan.md) is **Complete — PASS** and establishes the concrete downstream persistence/history substrate without creating domain schema.

[008-E](008-E-identity-authentication-participation-access-session-invitation-secrets-technical-authority-implementation-plan.md) is **Complete — PASS** and establishes the provider/principal/Identity/Participation/Access/session/invitation/recovery/secrets/technical-authority implementation boundary without creating authentication or authorization behavior.

Durable 008-D implementation ownership lives in [Persistence, History, Provenance, Outbox, Projection & Migration Implementation Contract](../canonical/implementation/persistence-history-projection.md). Durable 008-E implementation ownership lives in [Identity, Authentication, Participation, Access, Session, Invitation, Secrets & Technical Authority Implementation Contract](../canonical/implementation/identity-authentication-access-session.md).

008-E fixes these implementation-planning choices:

- Cognito User Pools remains an authentication adapter rather than the MUDAC identity/authority model;
- human browser authentication uses OIDC/OAuth authorization code with state, nonce, PKCE, server-side exchange and no provider bearer tokens in script-readable storage;
- durable external principal linkage uses provider/issuer + subject, never mutable email/name/role claims;
- one Participation exists per Identity × Competition × role, with explicit dual-role context selection rather than capability union;
- Access is contextual composition plus resource-owner preconditions, not generic database RBAC;
- explicit Access grants are resource/capability/time/purpose bounded and retained through revocation/correction history;
- Event Completed removes ordinary Judge private-evaluation capability from current source-state authorization even when a cookie/session remains technically live;
- opaque first-party sessions are PostgreSQL-backed in `identity_access`, with digest-only bearer-token storage, bounded lifetime, server revocation and rotation on authentication/recovery/material context changes;
- invitation/QR/event-entry mechanics are routing or bounded Participation-claim mechanisms and possession alone is never Identity or Access authority;
- provider credential recovery remains separate from explicit MUDAC principal-link recovery; matching email/name never silently merges Identity;
- technical/operator/break-glass authority remains distinct from Judge/Organizer semantic authority and baseline user impersonation is rejected;
- production server secrets remain server-only in Secrets Manager or equivalent protected runtime configuration and are excluded from browser/source/log/Provenance/outbox surfaces.

## Dependency-safe subgroup plan

| Group | Topic | Status |
| --- | --- | --- |
| 008-A | [Implementation Re-entry Authority, Canonical Baseline, Change Control & Planning Guardrails](008-A-implementation-reentry-authority-canonical-baseline-change-control-planning-guardrails.md) | **Complete** |
| 008-B | [Protected 006-D Baseline Qualification, Drift Audit & Toolchain/Environment Reconciliation](008-B-protected-006-D-baseline-qualification-drift-audit-toolchain-environment-reconciliation.md) | **Complete — PASS** |
| 008-C | [Residual-Risk Ingestion, Historical 006 Mapping, Decision Register & Supersession Matrix](008-C-residual-risk-ingestion-historical-006-mapping-decision-register-supersession-matrix.md) | **Complete — PASS** |
| 008-D | [Persistence, Temporal Truth, Versioning, Provenance, Governed Exceptions, Outbox, Projection & Migration Implementation Plan](008-D-persistence-temporal-truth-versioning-provenance-governed-exceptions-outbox-projection-migration-implementation-plan.md) | **Complete — PASS** |
| 008-E | [Identity, Authentication, Participation, Access, Session, Invitation, Secrets & Technical-Authority Implementation Plan](008-E-identity-authentication-participation-access-session-invitation-secrets-technical-authority-implementation-plan.md) | **Complete — PASS** |
| 008-F | **Commands, Queries, Transactions, CAS, Idempotency, Concurrency, Lost-Response Reconciliation & API Implementation Plan** | **Next** |
| 008-G | **Browser Shell, Routing, Remote State, Draft Continuity, Synchronization, Recovery, Responsive & Accessibility Implementation Plan** | Planned |
| 008-H | **Competition Configuration, Team/Division/Alias, Rubric, Participation, Panel & Encounter Operations Slice Plan** | Planned |
| 008-I | **Scorecard, Evaluation Evidence, Amendment, Paper Capture, Verification & Convergence Slice Plan** | Planned |
| 008-J | **Reconciliation, Coverage, Aggregate, Rank, Awards, Finalization, Official Outcome, Export, Publication & Disclosure Slice Plan** | Planned |
| 008-K | **Security, Privacy, Accessibility, Observability, Performance, Recovery/DR, Retention & Operational Evidence Plan** | Planned |
| 008-L | **Consolidated Dependency Graph, Implementation Roadmap, First-Slice Authorization & Phase Exit Review** | Planned |

## Dependency rationale

```text
008-A authority and guardrails                         COMPLETE
   ↓
008-B retained substrate qualification                 COMPLETE
   ↓
008-C residual + historical-plan reconciliation        COMPLETE
   ↓
008-D durable data / temporal authority plan           COMPLETE
   ↓
008-E identity / access / session plan                 COMPLETE
   ↓
008-F command / API / concurrency plan                 NEXT
   ↓
008-G browser / Draft / recovery plan
   ↓
008-H competition + judging operations slices
   ↓
008-I evaluation evidence + paper slices
   ↓
008-J outcomes + externalization slices
   ↓
008-K cross-cutting verification / evidence gates
   ↓
008-L consolidated roadmap + first-slice authorization
   ↓
Phase 009 implementation
```

008-F follows 008-E because the server command/query boundary can now rely on a fixed server-derived Identity + exactly-one-selected-Participation context, contextual Access semantics, opaque session model, and explicit technical-authority separation rather than inventing authentication/authorization rules inside Fastify middleware.

## Planning guardrails

Phase 008 still does not create domain tables, migrations, repositories, authentication/session behavior, domain APIs, IndexedDB domain state, product features, or domain-purpose AWS application resources.

Accepted persistence and identity/authentication plans are not implementation. Green CI is not implementation authorization, merge authority, deployment authority, or production certification.

If planning exposes a genuine semantic contradiction or missing semantic owner, use `CHG-*`; implementation convenience does not silently weaken current design.

## Current status

```text
Jackson Concept Design: COMPLETE / EXITED
Phase 008 subdivision: COMPLETE
implementation planning authority: ESTABLISHED
008-A: COMPLETE
008-B: COMPLETE — PASS AFTER NARROW REMEDIATION
008-C: COMPLETE — PASS
008-D: COMPLETE — PASS
008-E: COMPLETE — PASS
protected 006-D baseline: QUALIFIED FOR PHASE 008 PLANNING
historical 006-E–M executable queue: SUPERSEDED / MAPPED
008-F: NEXT / NOT STARTED
new domain implementation after 006-D: NOT STARTED
first executable slice: NOT YET AUTHORIZED
production readiness: NOT ESTABLISHED
```

## Next

Proceed to **008-F — Commands, Queries, Transactions, CAS, Idempotency, Concurrency, Lost-Response Reconciliation & API Implementation Plan**.

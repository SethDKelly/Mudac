# Phase 008 — Implementation Re-entry, Plan Refresh & Execution Readiness

Status: **Planned — 008-A next**

## Purpose

Convert the completed Jackson Concept Design baseline and accepted architecture into a refreshed, dependency-safe implementation plan without beginning new MUDAC domain implementation.

Phase 008 exists because Phase 006's deferred 006-E through 006-M sequence predates the Phase 007 methodology refinements. Those records remain useful planning provenance, but they are not current executable authority.

The current boundary is owned by [Design / Implementation Boundary](../canonical/governance/design-implementation-boundary.md).

## Phase boundary

Phase 008 is an **implementation-planning and execution-readiness phase**.

```text
Phase 007
Jackson Concept Design COMPLETE / EXITED
        ↓
Phase 008
implementation plan refresh + execution readiness
        ↓
008-L explicit first-slice authorization
        ↓
Phase 009
new domain implementation begins
```

No 008 subgroup implements new domain behavior. Even if a subgroup selects concrete schema, API, persistence, session, browser, rendering, infrastructure, or verification mechanisms, those selections remain planning/architecture-to-implementation contracts until the Phase 008 exit explicitly authorizes an implementation slice.

The retained 006-D executable workspace remains a protected non-domain implementation baseline throughout Phase 008.

## Subdivision principles

The phase is divided around dependency and authority boundaries rather than the historical 006 lettering.

The ordering follows these rules:

1. establish current implementation-planning authority before inspecting the executable baseline;
2. qualify the retained baseline before planning new work on top of it;
3. ingest all accepted residual uncertainty and historical-plan lineage before choosing concrete implementation slices;
4. plan authoritative persistence before security/session and transport layers that depend on durable identity/state semantics;
5. plan authorization/session boundaries before command/API surfaces and browser continuity;
6. plan domain vertical slices only after shared persistence, security, transaction, and client-continuity contracts are reconciled;
7. establish evaluation/evidence authority before official-outcome and publication execution ordering;
8. derive cross-cutting verification/evidence gates from the resulting implementation plan rather than treating tests as a parallel source of product meaning;
9. authorize the first executable slice only after the consolidated dependency graph and readiness review pass.

## Dependency-safe subgroup plan

| Group | Topic | Status |
| --- | --- | --- |
| 008-A | **Implementation Re-entry Authority, Canonical Baseline, Change Control & Planning Guardrails** | **Next** |
| 008-B | **Protected 006-D Baseline Qualification, Drift Audit & Toolchain/Environment Reconciliation** | Planned |
| 008-C | **Residual-Risk Ingestion, Historical 006 Mapping, Decision Register & Supersession Matrix** | Planned |
| 008-D | **Persistence, Temporal Truth, Versioning, Provenance, Governed Exceptions, Outbox, Projection & Migration Implementation Plan** | Planned |
| 008-E | **Identity, Authentication, Participation, Access, Session, Invitation, Secrets & Technical-Authority Implementation Plan** | Planned |
| 008-F | **Commands, Queries, Transactions, CAS, Idempotency, Concurrency, Lost-Response Reconciliation & API Implementation Plan** | Planned |
| 008-G | **Browser Shell, Routing, Remote State, Draft Continuity, Synchronization, Recovery, Responsive & Accessibility Implementation Plan** | Planned |
| 008-H | **Competition Configuration, Team/Division/Alias, Rubric, Participation, Panel & Encounter Operations Slice Plan** | Planned |
| 008-I | **Scorecard, Evaluation Evidence, Amendment, Paper Capture, Verification & Convergence Slice Plan** | Planned |
| 008-J | **Reconciliation, Coverage, Aggregate, Rank, Awards, Finalization, Official Outcome, Export, Publication & Disclosure Slice Plan** | Planned |
| 008-K | **Security, Privacy, Accessibility, Observability, Performance, Recovery/DR, Retention & Operational Evidence Plan** | Planned |
| 008-L | **Consolidated Dependency Graph, Implementation Roadmap, First-Slice Authorization & Phase Exit Review** | Planned |

## 008-A — Implementation Re-entry Authority, Canonical Baseline, Change Control & Planning Guardrails

### Intent

Establish the current implementation-planning authority after formal methodology exit and prevent Phase 008 from becoming an accidental coding phase.

### Must establish

- exact canonical knowledge set that constrains implementation planning;
- precedence among canonical product, synchronization, policy, experience, architecture, implementation, and historical phase records;
- change-governance route when implementation planning discovers a genuine semantic contradiction;
- explicit prohibition on treating old 006-E–M records as current execution authority;
- explicit distinction among planning decision, executable-slice authorization, code start, merge readiness, deployment readiness, and production certification;
- Phase 008 document ownership and anti-bloat/progressive-disclosure expectations;
- rule that no new domain implementation is authorized before 008-L.

### Exit condition

Every later Phase 008 subgroup can determine which current owner constrains its decisions without reconstructing authority from phase history.

## 008-B — Protected 006-D Baseline Qualification, Drift Audit & Toolchain/Environment Reconciliation

### Intent

Determine whether the retained executable bootstrap remains a trustworthy substrate for future implementation after the design hiatus.

### Must review

- current repository/package topology versus accepted `MOD-*` and implementation-source contracts;
- Node/TypeScript/pnpm/Fastify/Kysely/PostgreSQL/Vitest/Playwright/OpenTofu baseline and dependency drift;
- current CI/static/dependency enforcement and known repository-admin gaps;
- local PostgreSQL bootstrap and absence of accidental authoritative schema;
- API/worker/web composition roots and absence of accidental domain authority;
- OpenTofu roots/state boundaries and absence of unintended application provisioning;
- security/supply-chain maintenance accumulated during design re-entry;
- whether any retained 006-D choice now conflicts with Phase 007 semantics.

### Exit condition

The protected baseline is either accepted as-is, repaired through permitted non-domain maintenance, or explicitly replaced in the plan before downstream implementation assumptions depend on it.

## 008-C — Residual-Risk Ingestion, Historical 006 Mapping, Decision Register & Supersession Matrix

### Intent

Translate the accepted 007-H/007-I residual uncertainty and historical Phase 006 plan into an explicit implementation-planning work register.

### Must produce

- mapping of every 007-H Class 2 item to a concrete downstream planning owner;
- mapping of every Class 3 implementation/evidence item to one or more Phase 008/009 work items;
- preservation of Class 4 future scope outside the current baseline;
- 006-E–M disposition matrix: preserve, split, merge, reorder, rename, or supersede;
- implementation decision register for choices not already fixed by architecture;
- semantic-change trigger criteria that route back through `CHG-*` rather than being solved inside implementation planning.

### Exit condition

No accepted residual or historical deferred task remains unowned, duplicated ambiguously, or able to re-enter implementation as hidden scope.

## 008-D — Persistence, Temporal Truth, Versioning, Provenance, Governed Exceptions, Outbox, Projection & Migration Implementation Plan

### Intent

Plan the durable authority substrate before higher layers depend on it.

### Must resolve at implementation-plan level

- relational representation of stable identity, currentness, immutable/versioned history, supersession, invalidation, replacement, occurrence/effective time, correction time, and observed/as-known history;
- Versioning and Provenance persistence patterns;
- transaction/outbox boundary and projection rebuild/freshness strategy;
- policy-specific governed-exception persistence with source condition, scope, authorizer, reason, consequence, and history preserved;
- Official Outcome Revision physical realization constraints without promoting it to a new Concept;
- migration ordering, compatibility, rollback/forward-fix posture, and test evidence;
- module ownership of authoritative tables/repositories versus projection storage;
- retention/deletion safeguards for evidence required by current semantics.

### Dependency

Requires 008-A through 008-C. It must not depend on authentication or API convenience to define data meaning.

### Exit condition

Persistence can be implemented later without deciding unresolved product semantics or collapsing temporal/authority dimensions for schema convenience.

## 008-E — Identity, Authentication, Participation, Access, Session, Invitation, Secrets & Technical-Authority Implementation Plan

### Intent

Plan security identity and contextual authorization on top of the durable authority model.

### Must resolve

- provider-authentication adapter to stable MUDAC Identity;
- Participation selection and role-context isolation;
- contextual Access evaluation and revocation;
- session creation, expiry, renewal, re-verification/step-up and device-recovery behavior;
- invitation/join-code mechanics without granting authority through possession alone;
- Event Completed Judge-access expiry and narrow correction reauthorization;
- dual-role switching and disclosure-context isolation;
- support/operator/break-glass technical capability separated from Competition semantic authority;
- secrets/configuration boundaries and nonproduction/production credential posture.

### Dependency

Requires 008-D's persistence/temporal authority plan.

### Exit condition

Later authentication/session implementation can enforce the accepted Identity → Participation → Access model without inventing a permanent Judge/Organizer user type or operator shortcut.

## 008-F — Commands, Queries, Transactions, CAS, Idempotency, Concurrency, Lost-Response Reconciliation & API Implementation Plan

### Intent

Define how accepted Concept actions and synchronizations cross application/transport boundaries while preserving authority under retry, concurrency, stale state, and uncertain outcomes.

### Must resolve

- command versus query surface and current-context authority checks;
- transaction ownership and cross-module coordinator placement;
- optimistic concurrency/CAS tokens and stale-write behavior;
- durable idempotency identity, scope, storage, retention, and replay behavior;
- unknown/ambiguous commit-result reconciliation before retry;
- semantic error taxonomy without leaking sensitive state;
- exact postcondition confirmation rules for authority-establishing actions;
- projection freshness/uncertainty representation in reads;
- OpenAPI generation direction and DTO/domain isolation;
- CSRF and request-integrity posture where applicable.

### Dependency

Requires 008-D and 008-E because transport cannot define persistence or authority semantics retroactively.

### Exit condition

Every consequential API interaction can be traced from accepted Concept action through authorization, transaction, postcondition, retry/reconciliation, and user-visible confirmed state.

## 008-G — Browser Shell, Routing, Remote State, Draft Continuity, Synchronization, Recovery, Responsive & Accessibility Implementation Plan

### Intent

Plan the browser/client realization after server-side authority, authorization, transaction, and query contracts are known.

### Must resolve

- React application shell and route/context boundaries;
- TanStack Query remote-cache authority and invalidation posture;
- IndexedDB Draft scope, encryption/privacy considerations, cleanup and migration;
- revision-aware Draft synchronization and stale/conflict preservation;
- offline/disconnected working state without offline authoritative transitions;
- Access/session expiry interaction with local Drafts and cached sensitive data;
- role-mode switching and route visibility without navigation becoming authorization;
- high-consequence confirmation/recovery states tied to actual server postconditions;
- phone-primary Judge, exception-first Organizer, keyboard/nonvisual, responsive and paper-adjacent accessibility requirements;
- truthful status/freshness/uncertainty vocabulary.

### Dependency

Requires 008-E and 008-F.

### Exit condition

The browser can later be implemented as a representation/interaction layer over server authority rather than as a second semantic state machine.

## 008-H — Competition Configuration, Team/Division/Alias, Rubric, Participation, Panel & Encounter Operations Slice Plan

### Intent

Define the first family of end-to-end domain slices around Competition preparation and live judging operations.

### Must plan

- Competition lifecycle/configuration and readiness consequences;
- Team, Division and Alias administrative flows and historical-presentation boundaries;
- Rubric draft/validation/authoritative-Version use;
- Identity/Participation onboarding integration without collapsing those Concepts;
- Panel membership and effective Encounter participation distinction;
- Encounter preparation/begin/presentation-complete/complete/cancel/invalidate/replacement semantics;
- current-versus-historical snapshots needed for judging context;
- Organizer operational exception surfaces as projections rather than alternate authority;
- integration/evidence fixtures needed to validate the slice.

### Dependency

Requires 008-D through 008-G.

### Exit condition

The implementation roadmap has a coherent preparation/live-operations slice family whose dependencies are explicit and whose UI/API/data pieces share one accepted semantic basis.

## 008-I — Scorecard, Evaluation Evidence, Amendment, Paper Capture, Verification & Convergence Slice Plan

### Intent

Plan the authoritative evaluation path only after Encounter participation and Rubric-Version binding are stable.

### Must plan

- one logical Scorecard per Judge Participation × Encounter;
- exact Rubric Version binding;
- Draft versus Finalized Version versus Amendment Draft authority;
- criterion and note persistence/edit semantics;
- explicit Finalization and uncertain-result reconciliation;
- amendment successor semantics without in-place history rewrite;
- Judge authorship versus Organizer capture actor;
- paper source identity, capture Draft, verification, duplicate detection and convergence with electronic evidence;
- invalidated evidence eligibility and historical retention;
- Access expiry/re-authorized correction paths;
- evidence fixtures for retry, duplicate capture, stale amendment, device loss, paper/digital overlap and authorship protection.

### Dependency

Requires 008-H plus 008-D through 008-G.

### Exit condition

Evaluation implementation can establish one authoritative evidence model across electronic, paper, amendment, failure, and recovery paths.

## 008-J — Reconciliation, Coverage, Aggregate, Rank, Awards, Finalization, Official Outcome, Export, Publication & Disclosure Slice Plan

### Intent

Plan derived and declared outcomes only after authoritative evaluation evidence is defined.

### Must plan

- reconciliation projections and source-directed resolution actions;
- Coverage separately from Aggregate and Rank;
- policy-specific Coverage/Panel exceptions under `OPG-*` governance;
- evidence/policy basis for Aggregate and Division-scoped Rank;
- ranking readiness and true-tie semantics;
- rank-derived versus discretionary Award decisions and affected-state behavior;
- Competition Finalization and immutable/reconstructible Official Outcome Revision;
- post-Finalization correction with latest-declared-official + Affected semantics and explicit successor declaration;
- Export exact source/purpose/audience/disclosure binding and `EXPORT-003` authority monotonicity;
- Artifact integrity/storage as supporting architecture rather than a new Concept;
- Publication publish/withdraw/supersede semantics and `PUB-001` purpose/source prerequisites;
- operational, ceremony-safe and public representation profiles.

### Dependency

Requires 008-I. It consumes evaluation evidence; it must not back-drive Scorecard meaning merely to simplify ranking or publication.

### Exit condition

The roadmap preserves the full evidence → derived result → official declaration → representation → publication chain without collapsing calculated, official, public, published, or delivered states.

## 008-K — Security, Privacy, Accessibility, Observability, Performance, Recovery/DR, Retention & Operational Evidence Plan

### Intent

Turn cross-cutting quality attributes into concrete implementation evidence gates against the now-refreshed slice plan.

### Must define

- security/privacy threat and abuse cases across roles, devices, caches, APIs, artifacts and operator access;
- accessibility evidence for Judge/Organizer workflows, high-consequence actions and generated/printed materials;
- structured audit/telemetry ownership without leaking protected evaluation data;
- workload assumptions, performance budgets, capacity/load scenarios and event-day SLO evidence;
- backup/restore, regional recovery, paper fallback and degraded-operation exercises;
- migration/rollback/forward-fix evidence;
- projection freshness/rebuild evidence;
- retention/deletion activation gates;
- actual repository/environment/deployment administrative prerequisites;
- which tests are unit, property/invariant, PostgreSQL integration, API, browser E2E, provider integration, security, accessibility, load, restore or operational exercise evidence;
- explicit rule that tests validate current authority but do not become an alternate source of semantics.

### Dependency

Requires 008-D through 008-J so evidence is derived from the actual refreshed plan rather than guessed early.

### Exit condition

Every implementation slice has proportionate entry/exit evidence and high-consequence behavior has an identified verification strategy before execution begins.

## 008-L — Consolidated Dependency Graph, Implementation Roadmap, First-Slice Authorization & Phase Exit Review

### Intent

Consolidate Phase 008 into one active implementation roadmap and decide whether MUDAC may begin new domain implementation.

### Must perform

- cross-check all 008-A through 008-K outputs for contradictions, duplicated ownership and dependency cycles;
- produce the single refreshed dependency graph and implementation slice ordering;
- map superseded 006-E–M tasks into the new roadmap without rewriting their history;
- identify unresolved implementation decisions and prove none is a hidden baseline semantic blocker;
- define slice-specific upstream canonical owners and verification gates;
- identify the smallest dependency-safe first executable domain slice;
- explicitly decide **AUTHORIZED / NOT AUTHORIZED** for that slice;
- if authorized, update the Design / Implementation Boundary from `domain implementation: NOT STARTED` to the exact Phase 009 entry posture;
- preserve production readiness as a later evidence-based decision.

### Exit condition

Phase 008 passes only if the refreshed roadmap is internally coherent, the first implementation slice is dependency-safe and evidence-bounded, and its execution authority is explicit.

008-L itself still performs no domain implementation.

# Dependency graph

The default dependency chain is:

```text
008-A authority/baseline rules
   ↓
008-B retained substrate qualification
   ↓
008-C residual + historical-plan reconciliation
   ↓
008-D durable data/temporal authority plan
   ↓
008-E identity/access/session plan
   ↓
008-F command/API/concurrency plan
   ↓
008-G browser/Draft/recovery plan
   ↓
008-H competition + judging operations slices
   ↓
008-I evaluation/evidence + paper slices
   ↓
008-J outcomes + externalization slices
   ↓
008-K cross-cutting verification/evidence gates
   ↓
008-L consolidated roadmap + first-slice authorization
   ↓
Phase 009 implementation
```

Some implementation work identified inside later plans may ultimately run in parallel once Phase 009 begins, but Phase 008 planning proceeds in this order so a downstream plan does not silently determine an upstream semantic or authority decision.

# Phase 008 non-goals

Phase 008 does not:

- add product scope simply to create a convenient first slice;
- reopen completed Concept Design without evidence of a real semantic contradiction;
- create database tables, domain migrations, repositories, authentication/session behavior, domain APIs, browser domain state, or AWS application resources;
- execute the historical 006-E–M plan;
- treat CI/test success as implementation authorization;
- claim production readiness;
- promote future Stage/Round, student application, scheduling, notifications, calibrated scoring, rich public results, or advanced Award governance into the baseline.

# Current status after subdivision

```text
Jackson Concept Design: COMPLETE / EXITED
Phase 008 subdivision: COMPLETE
008-A: NEXT / NOT STARTED
implementation planning: ACTIVE
new domain implementation after 006-D: NOT STARTED
first executable slice: NOT YET AUTHORIZED
production readiness: NOT ESTABLISHED
```

# Next

Proceed to **008-A — Implementation Re-entry Authority, Canonical Baseline, Change Control & Planning Guardrails**.

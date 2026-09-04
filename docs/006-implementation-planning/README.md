# Phase 006 — Implementation Planning, Delivery Slices & Verification Strategy

Status: **In Progress**

## Purpose

Phase 006 converts the accepted MUDAC product, UX, knowledge-governance, and Phase 005 architecture contracts into an executable implementation plan before broad production-code construction begins.

Phase 006 is not permission to redesign MUDAC for coding convenience. Implementation planning begins from current canonical owners and stable rule IDs, chooses replaceable implementation mechanisms where Phase 005 intentionally left them open, establishes enforceable repository/test/delivery boundaries, and then sequences end-to-end delivery slices so authoritative behavior can be demonstrated incrementally.

The Phase 005 exit review is the immediate upstream handoff: [005-J — Phase 005 Consolidation, Threat/Failure Review & Implementation-Readiness Exit](../005-system-application-data-synchronization-architecture/005-J-phase-005-consolidation-threat-failure-review-implementation-readiness-exit.md).

## Planning principles

1. **Authority before convenience.** Canonical product/UX/architecture rules constrain implementation; implementation mismatch does not silently weaken them.
2. **Enforcement before scale-out.** Repository checks, module dependency rules, test/evidence conventions, migration safety, and security controls are designed before feature volume makes violations expensive.
3. **Foundations before dependent slices.** Persistence, Identity/Access, command semantics, browser state, and runtime conventions are planned before domain slices that rely on them.
4. **Vertical slices over layer completion.** Once foundations exist, delivery proceeds through user-visible, authority-complete slices rather than finishing every backend or frontend layer independently.
5. **Verification is part of each slice.** Unit, integration, contract, security, accessibility, concurrency, recovery, and provenance evidence are planned with the behavior they protect.
6. **Production readiness is evidence-based.** Load, restore, recovery, migration, security, accessibility, and event-day readiness claims require exercised evidence rather than architecture prose.
7. **No speculative platform bloat.** New frameworks/services/helpers require a demonstrated implementation need and must preserve `MOD-*`, `DATA-*`, `AUTH-*`, `API-*`, `SYNC-*`, `REP-*`, `FE-*`, `AWS-*`, and `IMPL-*` ownership boundaries.

## Dependency-safe phase plan

| Group | Topic | Status |
| --- | --- | --- |
| 006-A | [Implementation Authority, Delivery Governance, Toolchain & Repository Enforcement](006-A-implementation-authority-delivery-governance-toolchain-repository-enforcement.md) | **Complete** |
| 006-B | **Verification Strategy, Test Harness, Evidence Fixtures & Quality Gates** | **Next** |
| 006-C | Source Topology, Module/Package Boundaries, Shared Foundation & Dependency Enforcement | Planned |
| 006-D | Environment, IaC, CI/CD, Local Development & Runtime Bootstrap | Planned |
| 006-E | Persistence, Schema, Migration, Provenance, Outbox & Projection Foundation | Planned |
| 006-F | Identity, Session, Access, Security & Invitation Foundation | Planned |
| 006-G | API, Commands, Queries, Transactions, Idempotency & Concurrency Foundation | Planned |
| 006-H | Browser Shell, Routing, Remote/Local State, Component Primitives & Accessibility Foundation | Planned |
| 006-I | Competition Setup, Participation & Judging Operations Vertical Slice | Planned |
| 006-J | Evaluation, Scorecard, Draft Synchronization, Conflict & Paper-Capture Vertical Slice | Planned |
| 006-K | Reconciliation, Coverage, Ranking, Awards, Finalization & Official Outcome Vertical Slice | Planned |
| 006-L | Export, Artifact, Publication, Print & External Representation Vertical Slice | Planned |
| 006-M | Integrated Security, Observability, Performance, Recovery, Operational Readiness & Phase Exit | Planned |

## Dependency graph

```text
006-A  implementation authority / tooling / repository enforcement
   ↓
006-B  verification + evidence framework
   ↓
006-C  source topology + module/package enforcement
   ↓
006-D  environment / IaC / CI-CD / runtime bootstrap
   ↓
006-E  persistence / schema / migrations / outbox / projections
   ↓
006-F  identity / session / Access / security
   ↓
006-G  API / commands / transactions / idempotency / concurrency
   ↓
006-H  browser shell / state / components / accessibility
   ↓
006-I  competition + participation + judging-operations slice
   ↓
006-J  evaluation + Scorecard + sync + paper slice
   ↓
006-K  reconciliation + ranking + awards + finalization slice
   ↓
006-L  export + artifact + publication + print slice
   ↓
006-M  integrated hardening / recovery / readiness / exit
```

The sequence is the default dependency order, not a ban on all parallel work. A later group may begin preparatory work only when its required contracts from preceding groups are stable enough that parallelism cannot create competing foundations.

## Accepted implementation baseline through 006-A

Current implementation authority lives in [Canonical Implementation](../canonical/implementation/) and [Implementation Authority, Toolchain & Delivery Governance](../canonical/implementation/implementation-foundation.md) with `IMPL-001` through `IMPL-016`.

006-A establishes:

- Node.js 24 LTS + TypeScript 6.x as the primary server/browser implementation toolchain;
- pnpm workspaces and committed lockfile, without Nx/Turborepo at baseline;
- Fastify 5.x as the thin server transport/application host rather than a domain framework;
- Kysely + node-postgres for typed PostgreSQL access and explicit version-controlled migrations;
- explicit transport schemas that generate OpenAPI outward rather than serializing domain/persistence models;
- Vitest and Playwright as verification tool families, with the detailed evidence matrix deferred to 006-B;
- strict TypeScript, ESLint flat configuration, and Prettier as mandatory static-quality gates;
- OpenTofu for persistent AWS infrastructure;
- layered dependency/static/container/IaC security scanning;
- committed/reviewed dependency lockfiles and reproducible generated-code policy;
- intended PR/check-gated `main` and separately protected production deployment authority;
- implementation decision records that remain subordinate to canonical architecture;
- a common Phase 006 definition of done.

The current design-session GitHub connection cannot administer repository rulesets/branch protection, so actual protection configuration and verification remain a named 006-D gate rather than being falsely claimed complete.

# 006-B — Verification Strategy, Test Harness, Evidence Fixtures & Quality Gates

Design the verification system before feature implementation proliferates.

Expected scope:

- unit, module integration, database integration, API contract, browser integration, end-to-end, security, accessibility, concurrency, recovery, migration, and operational test layers;
- canonical rule-ID-to-test traceability convention without creating a duplicate rule store;
- deterministic fixtures/factories for Competition, Participation, Encounter, Rubric, Scorecard, Versions, Outcomes, Artifacts, and paper capture;
- golden/contract fixtures where historical or representation fidelity matters;
- test database and migration-test strategy;
- fake/adapter boundaries for Cognito, S3, SQS, time, IDs, email/invitation delivery, and artifact generation;
- accessibility automation plus required manual assistive-technology evidence;
- threat/security test catalog seeded from 005-J;
- CI quality gates and evidence retention;
- criteria for distinguishing structural CI success from semantic/product verification.

# 006-C — Source Topology, Module/Package Boundaries, Shared Foundation & Dependency Enforcement

Translate `MOD-*` into enforceable source-code structure without mirroring the documentation tree mechanically.

Expected scope:

- backend module/package boundaries for the six authoritative modules;
- application-coordination and projection/query placement;
- transport/infrastructure adapter boundaries;
- frontend feature, semantic-pattern, primitive, route, and adapter boundaries;
- business-neutral shared-foundation contents;
- import/dependency direction rules and automated enforcement;
- module public contracts and cross-module stable-ID/reference conventions;
- prohibition of repository/table/ORM-entity leakage across module owners;
- generated API/client contracts and where they may live;
- test package boundaries and fixture ownership.

# 006-D — Environment, IaC, CI/CD, Local Development & Runtime Bootstrap

Plan the executable platform skeleton before domain persistence and services depend on ad hoc environments.

Expected scope:

- local development topology and developer bootstrap;
- production/nonproduction AWS account/environment mapping;
- OpenTofu repository/module/state/backend structure;
- VPC/subnet/NAT/S3-endpoint/CloudFront/internal-ALB/ECS/ECR/RDS/S3/SQS/Cognito/CloudWatch skeleton sequencing;
- GitHub Actions OIDC deployment roles and protected environments;
- actual `main` ruleset/branch protection and required-check verification;
- secret/configuration injection and local equivalents;
- immutable backend/frontend release packaging;
- migration execution identity and deployment ordering;
- environment reset/seed/test data posture;
- deployment smoke-test and rollback hooks;
- cost tags/budgets/anomaly-detection bootstrap.

006-D establishes infrastructure capability but does not yet claim production readiness.

# 006-E — Persistence, Schema, Migration, Provenance, Outbox & Projection Foundation

Turn `DATA-*` and `IMPL-005` into the shared authoritative persistence substrate used by later domain slices.

Expected scope:

- PostgreSQL schema/namespace conventions by module owner;
- stable identifier representation;
- Kysely database-type generation/ownership convention;
- transaction/unit-of-work conventions;
- revision/concurrency-token representation;
- committed Version and Provenance persistence primitives without centralizing their semantics;
- migration naming/order/ownership and expand-contract rules;
- deletion/supersession safeguards;
- idempotency record substrate where appropriate;
- transactional outbox schema/dispatcher boundary;
- projection watermark/rebuild conventions;
- RDS-compatible local/integration testing;
- backup-sensitive migration verification.

# 006-F — Identity, Session, Access, Security & Invitation Foundation

Implement-plan the security path on top of persistence before protected domain commands are delivered.

Expected scope:

- Cognito adapter and stable `issuer + subject` Identity linking;
- server-side opaque-session store, cookie policy, expiry, revocation, and session-version behavior;
- CSRF mechanism compatible with the final CloudFront/application origin topology;
- Participation-context selection and switching;
- contextual Access evaluation interface and resource-owner enforcement contract;
- invitation/claim/check-in token lifecycle;
- dual-role cache/session separation obligations;
- correction grant and step-up hooks;
- shared/lost-device logout/revocation behavior;
- break-glass/operator separation implementation boundary;
- security/audit test gates.

# 006-G — API, Commands, Queries, Transactions, Idempotency & Concurrency Foundation

Establish the transport/application execution model used by all subsequent domain slices.

Expected scope:

- versioned HTTPS/JSON API conventions and route/command style;
- JSON-schema-compatible DTO/schema and OpenAPI generation/compatibility policy;
- server-derived actor/Participation context propagation;
- command/query handler boundary;
- semantic error/result envelope;
- optimistic expected-revision contract;
- idempotency-key storage, fingerprinting, scope, retention, and replay semantics;
- targeted lock/isolation conventions;
- cross-module transaction coordinator mechanics while the shared database is local;
- pagination/order conventions;
- outbox publication after authoritative commit;
- generated browser API adapter strategy.

# 006-H — Browser Shell, Routing, Remote/Local State, Component Primitives & Accessibility Foundation

Establish the React client substrate before domain screens are multiplied.

Expected scope:

- React/TypeScript project/build structure under the pnpm workspace;
- React Router Data-mode route/layout/error-boundary conventions;
- TanStack Query client/cache ownership and context partitioning;
- authenticated shell, Competition/Participation mode selection, and protected-route behavior;
- command-state primitives for submitting/confirmed/rejected/conflict/uncertain;
- IndexedDB Draft adapter contract, schema migration, privacy/retention/cleanup, and failure degradation;
- design tokens and accessible primitive/component strategy;
- semantic status/recovery patterns;
- responsive phone-primary Judge and exception-first Organizer layout conventions;
- WCAG 2.2 AA automated/manual verification hooks;
- frontend telemetry/error boundary posture.

# 006-I — Competition Setup, Participation & Judging Operations Vertical Slice

Deliver the first authority-complete end-to-end business slice across browser, API, modules, persistence, and AWS-compatible runtime.

Expected scope:

- Competition/Division/Team/Alias/Team Attribute setup required for judging;
- Identity/Participation onboarding and Judge/Organizer mode entry;
- Panel membership/composition;
- Judging Encounter creation/lifecycle and effective participants;
- readiness/precondition surfaces needed for judging;
- Judge onboarding/check-in/assigned-work navigation;
- Organizer preparation/live-operations exception views for this slice;
- provenance, Access, responsive/accessibility, and failure tests;
- no scoring/ranking implementation beyond what this slice requires.

# 006-J — Evaluation, Scorecard, Draft Synchronization, Conflict & Paper-Capture Vertical Slice

Deliver the core judging evidence path end to end.

Expected scope:

- Rubric/criterion/version persistence and delivery;
- one logical Scorecard per Judge Participation × Encounter;
- Draft save and server revision semantics;
- local IndexedDB continuity and reconnect synchronization;
- stale-device conflict preservation/reconciliation;
- explicit Finalization and immutable Scorecard Version;
- amendment flow;
- lost-response/idempotent Finalization recovery;
- paper-source identity, capture Draft, verification, transcription correction, and paper/electronic convergence;
- Judge independence/disclosure enforcement;
- mobile/accessibility and degraded-operation evidence.

# 006-K — Reconciliation, Coverage, Ranking, Awards, Finalization & Official Outcome Vertical Slice

Build the downstream outcome path only after authoritative Scorecard evidence is working.

Expected scope:

- Coverage and evaluation-policy application;
- Aggregate and Rank derivation with reconstructible basis;
- missing-never-zero and explicit tie/precision behavior;
- reconciliation queues and affected-state handling;
- Awards, including rank-derived and discretionary provenance;
- Competition Event Completion and Judge access cutoff;
- finalization-readiness evaluation;
- coordinated Competition Finalization + Official Outcome Revision transaction;
- post-finalization correction/successor Official Outcome Revision;
- Organizer reconciliation/finalization UX and required tests.

# 006-L — Export, Artifact, Publication, Print & External Representation Vertical Slice

Build external representations only after their authoritative source states exist.

Expected scope:

- Export identity and exact source/purpose/audience/disclosure binding;
- artifact-generation request/job through outbox/SQS/worker;
- immutable S3 object storage plus digest/metadata registration;
- renderer/template/print tooling selection and containment;
- complete-surface disclosure tests, including metadata/filename/QR/accessibility layers;
- artifact validation and preview;
- explicit Publication and delivery state;
- private/public delivery and bounded signed-access mechanism;
- supersession/withdrawal/republication after source corrections;
- paper rubric/material generation where applicable;
- artifact accessibility and print-quality evidence.

# 006-M — Integrated Security, Observability, Performance, Recovery, Operational Readiness & Phase Exit

Exercise the implemented slices as one deployable system and determine readiness for a production-readiness/release phase.

Expected scope:

- integrated threat-model and abuse-case verification;
- dependency/container/IaC/security scans and remediation;
- semantic and infrastructure observability dashboards/alarms;
- event-shaped workload model and load tests;
- connection/concurrency/finalization-burst tests;
- migration forward/rollback and mixed-version deployment exercises;
- RDS/S3 backup restore tests and measured RPO/RTO;
- regional cold-recovery drill and promote-one-authority validation;
- Cognito/network/SQS/S3/RDS failure injection where practical;
- paper fallback and post-event reconciliation exercise;
- event-day runbooks, pre-scale checklist, change freeze, incident roles, and support/break-glass drill;
- data-retention/deletion policy dependencies before lifecycle deletion;
- residual-risk register and implementation-phase exit decision.

## Parallelism policy

The phase is intentionally serial at major authority seams, but limited parallel execution is safe after prerequisite contracts stabilize:

- portions of 006-B and 006-C may proceed in parallel now that 006-A is stable if test/tooling decisions do not conflict;
- IaC scaffolding in 006-D may proceed alongside late 006-C documentation once package/runtime boundaries are stable;
- frontend primitive/accessibility work in 006-H may begin while late 006-G API details finish if generated/public contracts are stable;
- artifact-renderer prototyping for 006-L may occur before 006-K completes, but authoritative Publication integration waits for real source/outcome contracts;
- 006-M evidence work is accumulated throughout the phase, but its integrated exit decision waits for 006-I through 006-L.

## Exit target

Phase 006 should exit only when:

- implementation choices and package/module boundaries are explicit and enforceable;
- foundations and vertical slices have executable verification strategies;
- the delivered system preserves canonical authority and recovery semantics end to end;
- implementation-entry gates from 005-J are closed or explicitly deferred with owners;
- production-readiness evidence has been gathered enough to determine the next release/readiness phase without reopening architecture by default.

## Next

Proceed to **006-B — Verification Strategy, Test Harness, Evidence Fixtures & Quality Gates**.
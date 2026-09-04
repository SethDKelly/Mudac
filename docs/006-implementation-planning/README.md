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
| 006-B | [Verification Strategy, Test Harness, Evidence Fixtures & Quality Gates](006-B-verification-strategy-test-harness-evidence-fixtures-quality-gates.md) | **Complete** |
| 006-C | [Source Topology, Module/Package Boundaries, Shared Foundation & Dependency Enforcement](006-C-source-topology-module-package-boundaries-shared-foundation-dependency-enforcement.md) | **Complete** |
| 006-D | **Environment, IaC, CI/CD, Local Development & Runtime Bootstrap** | **Next** |
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

## Accepted implementation baseline through 006-C

Current implementation authority lives in [Canonical Implementation](../canonical/implementation/).

[Implementation Authority, Toolchain & Delivery Governance](../canonical/implementation/implementation-foundation.md) owns `IMPL-001` through `IMPL-016` and establishes Node.js 24 LTS + TypeScript 6.x, pnpm workspaces, Fastify, Kysely + node-postgres, explicit migrations, outward-generated OpenAPI transport contracts, Vitest/Playwright tool families, strict static-quality gates, OpenTofu, security scanning, lockfile/generated-code policy, delivery governance, and the Phase 006 definition of done.

[Verification Strategy, Evidence & Quality Gates](../canonical/implementation/verification-strategy.md) establishes the current evidence model without creating another stable-rule namespace. It requires:

- the smallest trustworthy evidence layer for the material authority/failure boundary;
- real PostgreSQL for database/concurrency/migration semantics;
- deterministic synthetic fixtures and explicit time/ID/external-service seams;
- module-owned fixture builders that do not bypass `MOD-*`/`DATA-*`;
- Fastify transport tests and Testing Library-style React interaction tests;
- Playwright critical-journey E2E;
- automated axe-compatible accessibility checks plus manual assistive-technology evidence before production readiness;
- application security/authority/disclosure tests in addition to scanners;
- explicit idempotency/concurrency/lost-response/recovery evidence;
- narrow golden fixtures for intentional external/historical fidelity;
- coverage as diagnostic evidence rather than a correctness oracle;
- a future stable aggregate `Implementation Verification` CI gate plus deeper scheduled/release evidence;
- flaky-test failures remaining visible rather than being normalized by retries;
- privacy-minimized synthetic CI artifacts;
- traceability from evidence to existing canonical stable rule IDs without copying rule bodies.

[Source Topology, Package Boundaries & Dependency Enforcement](../canonical/implementation/source-topology.md) now fixes the physical implementation graph without creating a parallel package-rule namespace:

- `apps/api`, `apps/worker`, and `apps/web` are deployable composition roots rather than semantic owners;
- the six accepted authoritative modules are separate pnpm workspace packages;
- `@mudac/application` coordinates cross-module use cases above owners;
- `@mudac/projections` owns non-authoritative cross-module read models;
- `@mudac/foundation` remains small, business-neutral, runtime-neutral, and browser-safe by default;
- owner infrastructure adapters remain owner-local rather than forming a central all-powerful data-access package;
- package root exports are explicit and deep/private imports are prohibited;
- module dependencies follow the acyclic `MOD-*` authority direction and are declared only when needed;
- `apps/web` cannot import server modules/persistence implementations and follows `app/routes → features → patterns → primitives` plus explicit adapter boundaries;
- module-owned `./testing` exports and technical `@mudac/test-support` preserve test ownership without creating production backdoors;
- internal workspace dependencies use pnpm `workspace:` references and cannot bypass exports through cross-root relative paths or path aliases;
- dependency-cruiser plus package exports provides blocking graph enforcement in the future `Implementation Verification` aggregate.

006-D is therefore free to instantiate the workspace/runtime/IaC/CI skeleton without rediscovering package ownership or dependency direction.

# 006-C — Source Topology, Module/Package Boundaries, Shared Foundation & Dependency Enforcement

**Complete.** Current authority lives in [Source Topology, Package Boundaries & Dependency Enforcement](../canonical/implementation/source-topology.md). The historical decision record is [006-C](006-C-source-topology-module-package-boundaries-shared-foundation-dependency-enforcement.md).

The accepted top-level implementation shape is:

```text
apps/
  api/
  worker/
  web/
packages/
  modules/
    competition/
    identity-access/
    judging-operations/
    evaluation/
    outcomes/
    external-representation/
  application/
  projections/
  foundation/
  test-support/
  api-client/      # introduced only once 006-G establishes generation
infra/
scripts/
tests/
docs/
```

006-D will create executable manifests/configuration and dependency checks for this graph; 006-C intentionally does not create empty placeholder packages/directories merely to make the repository resemble the diagram.

# 006-D — Environment, IaC, CI/CD, Local Development & Runtime Bootstrap

Plan the executable platform skeleton before domain persistence and services depend on ad hoc environments.

Expected scope:

- local development topology and developer bootstrap;
- pnpm workspace/root TypeScript/ESLint/Prettier/Vitest/Playwright configuration and package manifests/exports from 006-C;
- executable dependency-cruiser enforcement of module/browser/test boundaries;
- production/nonproduction AWS account/environment mapping;
- OpenTofu repository/module/state/backend structure;
- VPC/subnet/NAT/S3-endpoint/CloudFront/internal-ALB/ECS/ECR/RDS/S3/SQS/Cognito/CloudWatch skeleton sequencing;
- GitHub Actions OIDC deployment roles and protected environments;
- actual `main` ruleset/branch protection and required-check verification;
- executable `Implementation Verification` workflow/gate from 006-B;
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
- real-PostgreSQL integration and migration compatibility evidence;
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
- security/audit evidence required by the verification owner.

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
- generated browser API adapter strategy;
- transport/idempotency/concurrency evidence required by 006-B.

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
- Testing Library/Playwright/axe/manual accessibility hooks from 006-B;
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
- provenance, Access, responsive/accessibility, and failure evidence;
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

- 006-D may now instantiate workspace/CI/IaC scaffolding because 006-A through 006-C are stable; persistence-specific schema behavior remains 006-E;
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

Proceed to **006-D — Environment, IaC, CI/CD, Local Development & Runtime Bootstrap**.

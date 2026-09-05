# Phase 006 — Implementation Planning, Delivery Slices & Verification Strategy

Status: **In Progress**

## Purpose

Phase 006 converts accepted MUDAC product, UX, governance, and Phase 005 architecture contracts into an executable implementation while preserving canonical authority. Implementation pressure does not silently weaken accepted semantics.

The immediate upstream handoff is [005-J — Phase 005 Consolidation, Threat/Failure Review & Implementation-Readiness Exit](../005-system-application-data-synchronization-architecture/005-J-phase-005-consolidation-threat-failure-review-implementation-readiness-exit.md).

## Planning principles

1. Authority before convenience.
2. Enforcement before feature scale.
3. Foundations before dependent slices.
4. Vertical slices over isolated layer completion.
5. Verification ships with behavior.
6. Production readiness requires exercised evidence.
7. Avoid speculative platform and agent/documentation bloat.

## Dependency-safe phase plan

| Group | Topic | Status |
| --- | --- | --- |
| 006-A | [Implementation Authority, Delivery Governance, Toolchain & Repository Enforcement](006-A-implementation-authority-delivery-governance-toolchain-repository-enforcement.md) | **Complete** |
| 006-B | [Verification Strategy, Test Harness, Evidence Fixtures & Quality Gates](006-B-verification-strategy-test-harness-evidence-fixtures-quality-gates.md) | **Complete** |
| 006-C | [Source Topology, Module/Package Boundaries, Shared Foundation & Dependency Enforcement](006-C-source-topology-module-package-boundaries-shared-foundation-dependency-enforcement.md) | **Complete** |
| 006-D | [Environment, IaC, CI/CD, Local Development & Runtime Bootstrap](006-D-environment-iac-ci-cd-local-development-runtime-bootstrap.md) | **Complete** |
| 006-E | **Persistence, Schema, Migration, Provenance, Outbox & Projection Foundation** | **Next** |
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
006-A authority/tooling/governance
   ↓
006-B verification/evidence
   ↓
006-C source/package boundaries
   ↓
006-D executable environment/runtime/CI/IaC bootstrap
   ↓
006-E persistence/schema/migration/outbox/projections
   ↓
006-F identity/session/access/security
   ↓
006-G API/command/transaction/idempotency/concurrency
   ↓
006-H browser shell/state/components/accessibility
   ↓
006-I competition/participation/judging operations
   ↓
006-J evaluation/Scorecard/sync/paper
   ↓
006-K reconciliation/ranking/awards/finalization
   ↓
006-L export/artifact/publication/print
   ↓
006-M integrated hardening/readiness/exit
```

Limited parallel preparation is allowed only after the relevant preceding contracts are stable enough to prevent competing foundations.

## Accepted implementation baseline through 006-D

Current durable implementation authority lives in [Canonical Implementation](../canonical/implementation/).

### 006-A — toolchain and delivery authority

[Implementation Authority, Toolchain & Delivery Governance](../canonical/implementation/implementation-foundation.md) establishes the Node.js 24 + TypeScript 6 family, pnpm workspaces, Fastify, Kysely/node-postgres, explicit migrations, outward-generated OpenAPI, Vitest/Playwright, strict static checks, OpenTofu, supply-chain scanning, lockfile policy, delivery governance, and Phase 006 completion semantics.

### 006-B — verification

[Verification Strategy, Evidence & Quality Gates](../canonical/implementation/verification-strategy.md) requires the smallest trustworthy evidence layer, real PostgreSQL where its semantics matter, deterministic fixtures/fakes, behavioral security/accessibility/concurrency/recovery evidence, narrow golden fixtures, diagnostic coverage, visible flaky failures, privacy-minimized artifacts, and traceability to existing canonical rule IDs.

### 006-C — physical source topology

[Source Topology, Package Boundaries & Dependency Enforcement](../canonical/implementation/source-topology.md) fixes three composition-root apps, six authoritative module packages, thin application coordination, non-authoritative projections, a small business-neutral foundation, test ownership, browser/server separation, restrictive exports, pnpm workspace dependencies, and dependency-cruiser enforcement.

### 006-D — executable bootstrap

[Runtime, Environment & Delivery Bootstrap](../canonical/implementation/runtime-delivery-bootstrap.md) now instantiates that plan:

- pinned pnpm/Node/TypeScript manifests plus a generated committed lockfile;
- executable `apps/api`, `apps/worker`, and `apps/web` bootstrap roots with no premature domain features;
- module/application/projection/foundation/test-support workspace packages;
- Docker Compose PostgreSQL for local development;
- dependency-cruiser and ESLint boundary enforcement;
- the stable **Implementation Verification** GitHub Actions check;
- CodeQL and Dependabot baseline supply-chain/security automation;
- OpenTofu `nonproduction/us-east-2`, `production/us-east-2`, and cold `recovery/us-east-1` roots with separate state identities;
- S3 remote-state posture with encryption/versioning/least privilege and native `use_lockfile` locking;
- local/provider-fake vs targeted nonproduction real-service boundary;
- explicit merge-vs-production-deployment authority separation.

Actual GitHub branch/ruleset and protected production-environment administration remains a visible external repository-admin action because the current connected GitHub capability cannot write those settings. Workflow existence is not reported as enforced repository policy.

# 006-E — Persistence, Schema, Migration, Provenance, Outbox & Projection Foundation

Turn `DATA-*`, `API-*`, `IMPL-005`, the source topology, and the real-PostgreSQL verification contract into the shared authoritative persistence substrate.

Expected scope:

- module-owned PostgreSQL schema/namespace conventions;
- stable identifier representation;
- Kysely database-type generation and adapter ownership;
- transaction/unit-of-work conventions;
- revision/concurrency-token representation;
- committed Version and Provenance persistence primitives without centralizing semantics;
- migration naming/order/ownership and expand-contract policy;
- deletion/supersession safeguards;
- idempotency storage substrate where appropriate;
- transactional outbox and dispatcher boundary;
- projection watermark/rebuild conventions;
- real PostgreSQL integration, migration, transaction and concurrency evidence;
- backup-sensitive migration verification.

# 006-F — Identity, Session, Access, Security & Invitation Foundation

Implement Cognito adaptation, stable Identity linking, opaque server sessions, cookies/CSRF, expiry/revocation, Participation context switching, contextual Access, invitation/check-in tokens, correction/step-up hooks, shared-device behavior, break-glass boundaries, and security evidence.

# 006-G — API, Commands, Queries, Transactions, Idempotency & Concurrency Foundation

Implement versioned HTTPS/JSON transport conventions, explicit schemas/OpenAPI, server-derived actor/Participation context, command/query handlers, semantic result envelopes, optimistic revisions, idempotency persistence/fingerprints/retention/replay, targeted locking/isolation, coordinated local cross-module transactions, pagination, post-commit outbox publication, generated browser client boundary, and API/concurrency evidence.

# 006-H — Browser Shell, Routing, Remote/Local State, Component Primitives & Accessibility Foundation

Implement the React Router/TanStack Query browser shell, context partitioning, command-state primitives, IndexedDB Draft adapter and privacy/retention behavior, accessible primitives/patterns, responsive Judge/Organizer layouts, accessibility verification hooks, and frontend telemetry/error boundaries.

# 006-I — Competition Setup, Participation & Judging Operations Vertical Slice

Deliver Competition/Division/Team/Alias setup, Participation onboarding, Panel membership/composition, Encounter lifecycle/effective participants, readiness surfaces, Judge assigned-work navigation, Organizer preparation/live-ops exceptions, and required provenance/Access/accessibility/failure evidence without implementing scoring/ranking prematurely.

# 006-J — Evaluation, Scorecard, Draft Synchronization, Conflict & Paper-Capture Vertical Slice

Deliver Rubric/Criteria Versions, one logical Scorecard per Judge Participation × Encounter, server/local Draft continuity, revision-aware sync/conflict preservation, explicit Finalization/Version/amendment, lost-response reconciliation, paper-source capture/verification/transcription correction, channel convergence, Judge independence, and degraded/mobile/accessibility evidence.

# 006-K — Reconciliation, Coverage, Ranking, Awards, Finalization & Official Outcome Vertical Slice

Deliver Coverage, Evaluation Policy application, Aggregate/Rank basis, missing-never-zero/tie/precision behavior, reconciliation, Awards, Event Completion/Judge access cutoff, finalization readiness, atomic Competition Finalization + Official Outcome Revision, successor correction, and Organizer closeout UX/evidence.

# 006-L — Export, Artifact, Publication, Print & External Representation Vertical Slice

Deliver source/purpose/audience/disclosure-bound Exports, outbox/SQS generation jobs, immutable S3 Artifact bytes and digests, rendering/print containment, full-surface disclosure tests, validation/preview, explicit Publication/delivery, private/public access, supersession/republication, and artifact accessibility/print evidence.

# 006-M — Integrated Security, Observability, Performance, Recovery, Operational Readiness & Phase Exit

Exercise the implemented system through threat/abuse testing, scanners, semantic/infrastructure observability, event-shaped load/concurrency, mixed-version/migration exercises, RDS/S3 restores and measured RPO/RTO, regional cold recovery, dependency failure injection, paper fallback/reconciliation, event-day runbooks/change freeze/support/break-glass, retention dependencies, residual-risk closure, and the Phase 006 exit decision.

## Parallelism policy

- 006-E may begin now against the executable 006-D workspace and local PostgreSQL substrate.
- 006-H primitive/accessibility preparation may overlap late 006-G only after generated/public API contracts are stable.
- Artifact-renderer prototypes may precede 006-L integration, but authoritative Publication waits for real outcome/source contracts.
- 006-M evidence may accumulate throughout the phase; its exit decision waits for 006-I through 006-L.

## Exit target

Phase 006 exits only when implementation boundaries are enforceable, foundations and vertical slices carry executable evidence, end-to-end authority/recovery semantics remain intact, 005-J entry gates are closed or explicitly owned, and enough operational evidence exists to define the next release/readiness phase without reopening architecture by default.

## Next

Proceed to **006-E — Persistence, Schema, Migration, Provenance, Outbox & Projection Foundation**.

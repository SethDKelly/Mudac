# MUDAC Competition Demo

MUDAC is a documentation-first design effort for a web application supporting fair, traceable, resilient judging for live student data competitions.

Student Teams present analyses to Panels of volunteer Judges. Each Judge independently authors a Rubric-based Scorecard for a Team in a Judging Encounter. Authoritative Scorecards feed explicit Coverage, aggregation, ranking, Award, and controlled official-closeout semantics while preserving Judge independence, provenance, anonymity boundaries, accessibility, and paper continuity.

## Knowledge-first design

MUDAC uses Daniel Jackson's **Concept Design** methodology to determine product meaning. The repository is organized as an **Open Knowledge Format (OKF) v0.2** knowledge bundle so humans and agents can retrieve current authority without recursively loading historical design phases.

Start here:

* [`AGENTS.md`](AGENTS.md) — concise repository-agent bootstrap into canonical governance, architecture, implementation authority, and validation expectations.
* [`docs/index.md`](docs/index.md) — preferred OKF progressive-disclosure entry point.
* [`docs/canonical/`](docs/canonical/) — current canonical product/domain, conceptual UX, governance, architecture, and implementation knowledge.
* [`docs/canonical/architecture/`](docs/canonical/architecture/) — accepted current system/application architecture contracts.
* [`docs/canonical/implementation/`](docs/canonical/implementation/) — accepted current implementation/toolchain/verification/delivery contracts.
* [`docs/006-implementation-planning/`](docs/006-implementation-planning/) — active dependency-safe implementation planning and delivery sequencing.
* [`docs/README.md`](docs/README.md) — human-oriented documentation authority summary.

Numbered phase directories remain preserved as rationale, design provenance, and implementation-planning history. Canonical documents remain the authority for current product/UX/architecture/implementation meaning.

Knowledge structure is validated by [`scripts/validate_knowledge.py`](scripts/validate_knowledge.py) and read-only GitHub Actions CI. Passing that validator confirms deterministic repository structure only; it is not semantic verification.

## Design status

* **Phase 001 — Concept Design Foundation:** Complete
* **Phase 002 — Concept Specification, Policy & Synchronization Refinement:** Complete
* **Phase 003 — Conceptual UX Architecture:** Complete
* **Phase 004 — Knowledge Architecture, OKF Retrofit & Documentation Governance:** Complete
* **Phase 005 — System, Application, Data & Synchronization Architecture:** Complete
* **Phase 006 — Implementation Planning, Delivery Slices & Verification Strategy:** In Progress
  * 006-A — Implementation Authority, Delivery Governance, Toolchain & Repository Enforcement: Complete
  * 006-B — Verification Strategy, Test Harness, Evidence Fixtures & Quality Gates: Complete
  * **006-C — Source Topology, Module/Package Boundaries, Shared Foundation & Dependency Enforcement: Next**
  * 006-D–006-H — remaining implementation foundations
  * 006-I–006-L — dependency-ordered vertical delivery slices
  * 006-M — integrated hardening/readiness/exit

The full Phase 006 decomposition is in [`docs/006-implementation-planning/README.md`](docs/006-implementation-planning/README.md).

## Current architecture and implementation posture

MUDAC's canonical architecture is a **modular-monolith-first** system with six semantic modules, a PostgreSQL authority store with append-stable Version/Provenance history, explicit command/query and idempotency/concurrency semantics, provider-adapted Identity/Participation/Access, bounded IndexedDB Draft continuity, immutable artifact/evidence storage, React + TypeScript browser architecture, and a concrete AWS runtime.

Production architecture is single-active `us-east-2` and Multi-AZ: CloudFront fronts private origins; ECS/Fargate runs the API and bounded workers; RDS PostgreSQL Multi-AZ is authoritative persistence; Cognito User Pools authenticates while MUDAC retains application authority; SQS carries retryable async work; private evidence/Artifacts use encrypted/versioned S3; GitHub Actions deploys through OIDC-federated AWS roles; CloudWatch/ADOT/Application Signals cover infrastructure and semantic health; and whole-Region live-event failure falls back to paper until one restored digital authority is explicitly validated and promoted.

006-A establishes the initial implementation family: **Node.js 24 LTS + TypeScript**, **pnpm workspaces**, **Fastify 5.x**, **Kysely + node-postgres** with explicit migrations, transport schemas generating **OpenAPI** outward, **Vitest + Playwright** verification families, strict TypeScript + **ESLint + Prettier**, and **OpenTofu** for persistent AWS IaC. These are governed by [`IMPL-*`](docs/canonical/implementation/implementation-foundation.md), not by framework defaults.

006-B establishes the current [verification strategy](docs/canonical/implementation/verification-strategy.md): evidence uses the smallest trustworthy boundary, PostgreSQL-dependent behavior is tested against real PostgreSQL, external adapters use deterministic fakes plus targeted real-service integration where vendor behavior matters, fixtures remain synthetic/module-owned, critical browser/accessibility/security/concurrency/recovery behavior receives explicit evidence, coverage is diagnostic rather than a correctness oracle, flaky failures remain visible, and evidence traces existing canonical rule IDs without creating a parallel test-rule namespace.

The repository remains documentation/planning-only at this point; broad production code construction has not begun. Actual package/source/test topology is intentionally deferred to 006-C and executable environment/IaC/bootstrap plus GitHub branch/environment protection to 006-D.

The [Phase 005 exit review](docs/005-system-application-data-synchronization-architecture/005-J-phase-005-consolidation-threat-failure-review-implementation-readiness-exit.md) found no blocking cross-layer authority contradiction. MUDAC is **implementation-planning ready, not production certified**.

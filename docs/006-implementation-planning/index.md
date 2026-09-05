# Phase 006 — Implementation Planning, Delivery Slices & Verification Strategy

Implementation-planning history and delivery sequencing for MUDAC. Use [docs/index.md](../index.md) and current canonical owners for current product/UX/architecture/implementation meaning.

# Status

Phase 006 is **In Progress**.

# Records and current outputs

* [006-A — Implementation Authority, Delivery Governance, Toolchain & Repository Enforcement](006-A-implementation-authority-delivery-governance-toolchain-repository-enforcement.md) — **Complete**. Current authority: [Implementation Authority, Toolchain & Delivery Governance](../canonical/implementation/implementation-foundation.md).
* [006-B — Verification Strategy, Test Harness, Evidence Fixtures & Quality Gates](006-B-verification-strategy-test-harness-evidence-fixtures-quality-gates.md) — **Complete**. Current authority: [Verification Strategy, Evidence & Quality Gates](../canonical/implementation/verification-strategy.md).
* [006-C — Source Topology, Module/Package Boundaries, Shared Foundation & Dependency Enforcement](006-C-source-topology-module-package-boundaries-shared-foundation-dependency-enforcement.md) — **Complete**. Current authority: [Source Topology, Package Boundaries & Dependency Enforcement](../canonical/implementation/source-topology.md).
* [006-D — Environment, IaC, CI/CD, Local Development & Runtime Bootstrap](006-D-environment-iac-ci-cd-local-development-runtime-bootstrap.md) — **Complete**. Instantiates the pinned pnpm/TypeScript workspace, API/worker/web composition roots, local PostgreSQL, dependency enforcement, Implementation Verification/CodeQL/Dependabot, and separate OpenTofu nonproduction/production/recovery roots. Current authority: [Runtime, Environment & Delivery Bootstrap](../canonical/implementation/runtime-delivery-bootstrap.md).

# Planned work

* **006-E — Persistence, Schema, Migration, Provenance, Outbox & Projection Foundation** — Next.
* 006-F — Identity, Session, Access, Security & Invitation Foundation.
* 006-G — API, Commands, Queries, Transactions, Idempotency & Concurrency Foundation.
* 006-H — Browser Shell, Routing, Remote/Local State, Component Primitives & Accessibility Foundation.
* 006-I — Competition Setup, Participation & Judging Operations Vertical Slice.
* 006-J — Evaluation, Scorecard, Draft Synchronization, Conflict & Paper-Capture Vertical Slice.
* 006-K — Reconciliation, Coverage, Ranking, Awards, Finalization & Official Outcome Vertical Slice.
* 006-L — Export, Artifact, Publication, Print & External Representation Vertical Slice.
* 006-M — Integrated Security, Observability, Performance, Recovery, Operational Readiness & Phase Exit.

# Dependency posture

006-A through 006-D now provide implementation authority, evidence rules, enforceable source ownership, and an executable local/CI/IaC substrate. 006-E can therefore implement real PostgreSQL/Kysely schema and migration primitives without inventing workspace, test, environment, or CI conventions.

The GitHub workflow gates are executable, but repository ruleset/branch-protection and protected production-environment administration remains an explicit external repository-admin action until independently configured and verified. Workflow existence must not be confused with enforced merge/deployment policy.

The full scope, dependency graph, parallelism constraints, subgroup responsibilities, and exit target are defined in [README.md](README.md).

# Authority rule

Phase 006 records implementation reasoning and sequencing. Accepted durable implementation meaning is promoted under [Canonical Implementation](../canonical/implementation/). Implementation choices and evidence must satisfy task-relevant canonical rules; semantic conflicts use canonical change governance rather than being hidden in code, tests, CI, IaC, or this phase.

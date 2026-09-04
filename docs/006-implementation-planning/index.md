# Phase 006 — Implementation Planning, Delivery Slices & Verification Strategy

Implementation-planning history and delivery sequencing for MUDAC. Use [docs/index.md](../index.md) and current canonical owners for product/UX/architecture/implementation meaning.

# Status

Phase 006 is **In Progress**.

# Records and current outputs

* [006-A — Implementation Authority, Delivery Governance, Toolchain & Repository Enforcement](006-A-implementation-authority-delivery-governance-toolchain-repository-enforcement.md) — **Complete**. Selects the common implementation toolchain and delivery-governance baseline; current authority lives in [Implementation Authority, Toolchain & Delivery Governance](../canonical/implementation/implementation-foundation.md) with `IMPL-001` through `IMPL-016`.
* [006-B — Verification Strategy, Test Harness, Evidence Fixtures & Quality Gates](006-B-verification-strategy-test-harness-evidence-fixtures-quality-gates.md) — **Complete**. Establishes the layered evidence model, real-PostgreSQL integration, deterministic fixtures/fakes, stable-rule traceability, security/accessibility/concurrency/recovery testing, coverage/flakiness/privacy posture, and CI quality-gate tiers; current authority lives in [Verification Strategy, Evidence & Quality Gates](../canonical/implementation/verification-strategy.md).

# Planned work

* **006-C — Source Topology, Module/Package Boundaries, Shared Foundation & Dependency Enforcement** — Next.
* 006-D — Environment, IaC, CI/CD, Local Development & Runtime Bootstrap.
* 006-E — Persistence, Schema, Migration, Provenance, Outbox & Projection Foundation.
* 006-F — Identity, Session, Access, Security & Invitation Foundation.
* 006-G — API, Commands, Queries, Transactions, Idempotency & Concurrency Foundation.
* 006-H — Browser Shell, Routing, Remote/Local State, Component Primitives & Accessibility Foundation.
* 006-I — Competition Setup, Participation & Judging Operations Vertical Slice.
* 006-J — Evaluation, Scorecard, Draft Synchronization, Conflict & Paper-Capture Vertical Slice.
* 006-K — Reconciliation, Coverage, Ranking, Awards, Finalization & Official Outcome Vertical Slice.
* 006-L — Export, Artifact, Publication, Print & External Representation Vertical Slice.
* 006-M — Integrated Security, Observability, Performance, Recovery, Operational Readiness & Phase Exit.

# Dependency posture

Foundational groups 006-A through 006-H establish implementation authority, verification, enforceable source/module boundaries, runtime environments, persistence/security/API/browser substrates, and their test contracts. Domain delivery then proceeds through end-to-end vertical slices 006-I through 006-L in semantic dependency order. 006-M integrates the completed slices and produces the implementation-phase exit decision.

006-A fixes the common implementation family. 006-B now fixes the evidence model before source topology exists: tests must exercise the smallest trustworthy boundary, PostgreSQL-dependent behavior uses real PostgreSQL, external adapters use deterministic contract fakes plus targeted real-service evidence, critical browser/accessibility/security/recovery paths have explicit evidence classes, and CI will eventually expose a stable aggregate `Implementation Verification` gate. Source/package/test placement remains 006-C; executable repository/IaC bootstrap and actual GitHub ruleset/environment configuration remain 006-D.

The full scope, dependency graph, safe-parallelism rules, subgroup responsibilities, and exit target are defined in [README.md](README.md).

# Authority rule

Phase 006 records implementation reasoning and sequencing. Accepted durable implementation meaning is promoted under [Canonical Implementation](../canonical/implementation/). Implementation choices and evidence must cite and satisfy task-relevant canonical rules; if implementation pressure reveals a genuine semantic conflict, use canonical change governance rather than silently changing behavior in code, tests, or this phase.
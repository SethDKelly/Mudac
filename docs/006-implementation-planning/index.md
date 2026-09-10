# Phase 006 — Implementation Planning, Delivery Slices & Verification Strategy

Implementation-planning history and delivery sequencing for MUDAC. Use [docs/index.md](../index.md) and current canonical owners for current product/UX/architecture/implementation meaning.

# Status

Phase 006 is **historical after 006-D**. Its deferred 006-E through 006-M queue is now **fully superseded as current executable authority** by [008-C](../008-implementation-reentry/008-C-residual-risk-ingestion-historical-006-mapping-decision-register-supersession-matrix.md).

007-A froze domain implementation and reopened deliberate Jackson Concept Design. 007-I later completed the renewed methodology. 008-B then qualified the retained 006-D non-domain bootstrap, and 008-C mapped all historical deferred work into current Phase 008 owners.

The current execution posture is owned by [Design / Implementation Boundary](../canonical/governance/design-implementation-boundary.md).

# Records and current outputs

* [006-A — Implementation Authority, Delivery Governance, Toolchain & Repository Enforcement](006-A-implementation-authority-delivery-governance-toolchain-repository-enforcement.md) — **Complete historical planning**. Current authority: [Implementation Authority, Toolchain & Delivery Governance](../canonical/implementation/implementation-foundation.md).
* [006-B — Verification Strategy, Test Harness, Evidence Fixtures & Quality Gates](006-B-verification-strategy-test-harness-evidence-fixtures-quality-gates.md) — **Complete historical planning**. Current authority: [Verification Strategy, Evidence & Quality Gates](../canonical/implementation/verification-strategy.md).
* [006-C — Source Topology, Module/Package Boundaries, Shared Foundation & Dependency Enforcement](006-C-source-topology-module-package-boundaries-shared-foundation-dependency-enforcement.md) — **Complete historical planning**. Current authority: [Source Topology, Package Boundaries & Dependency Enforcement](../canonical/implementation/source-topology.md).
* [006-D — Environment, IaC, CI/CD, Local Development & Runtime Bootstrap](006-D-environment-iac-ci-cd-local-development-runtime-bootstrap.md) — **Complete historical bootstrap; qualified by 008-B as protected non-domain baseline**. Current authority: [Runtime, Environment & Delivery Bootstrap](../canonical/implementation/runtime-delivery-bootstrap.md).

# Historical deferred plan and current disposition

* 006-E — Persistence, Schema, Migration, Provenance, Outbox & Projection Foundation → **008-D**.
* 006-F — Identity, Session, Access, Security & Invitation Foundation → **008-E**, with cross-cutting security evidence in **008-K**.
* 006-G — API, Commands, Queries, Transactions, Idempotency & Concurrency Foundation → **008-F**.
* 006-H — Browser Shell, Routing, Remote/Local State, Component Primitives & Accessibility Foundation → **008-G**, with cross-cutting accessibility evidence in **008-K**.
* 006-I — Competition Setup, Participation & Judging Operations Vertical Slice → **008-H**.
* 006-J — Evaluation, Scorecard, Draft Synchronization, Conflict & Paper-Capture Vertical Slice → **split across 008-G and 008-I**.
* 006-K — Reconciliation, Coverage, Ranking, Awards, Finalization & Official Outcome Vertical Slice → **008-J**.
* 006-L — Export, Artifact, Publication, Print & External Representation Vertical Slice → **merged into 008-J**.
* 006-M — Integrated Security, Observability, Performance, Recovery, Operational Readiness & Phase Exit → **split across 008-K and 008-L**.

The full rationale and preserve/split/merge/expand decisions are owned by 008-C. These labels remain history; they must not be resumed as executable slices.

# Authority rule

Phase 006 records implementation reasoning and sequencing. Accepted durable implementation meaning is promoted under [Canonical Implementation](../canonical/implementation/), while [Design / Implementation Boundary](../canonical/governance/design-implementation-boundary.md) owns whether implementation is allowed to advance.

No Phase 008 planning completion before 008-L authorizes domain code. Actual new domain implementation begins only in Phase 009 after explicit first-slice authorization.

# Next

Proceed through [Phase 008 — Implementation Re-entry, Plan Refresh & Execution Readiness](../008-implementation-reentry/). The next dependency-safe subgroup is **008-D — Persistence, Temporal Truth, Versioning, Provenance, Governed Exceptions, Outbox, Projection & Migration Implementation Plan**.

# Implementation

Current accepted MUDAC implementation contracts and toolchain decisions.

Implementation is downstream of canonical product/UX/governance and architecture knowledge. These owners define how accepted architecture is realized in code, tests, migrations, generated contracts, CI/CD, and IaC; they do not redefine product or architecture meaning for implementation convenience.

# Current implementation contracts

* [Implementation Authority, Toolchain & Delivery Governance](implementation-foundation.md) — `IMPL-*` contracts for implementation authority, TypeScript/Node/Fastify/pnpm/Kysely/OpenTofu baseline, static analysis, dependency/version/generated-code policy, repository merge/deployment governance, security scanning, and Phase 006 completion semantics.
* [Verification Strategy, Evidence & Quality Gates](verification-strategy.md) — current verification contract for evidence layers, real PostgreSQL integration, deterministic fixtures/fakes, stable-rule traceability, security/accessibility/concurrency/recovery evidence, coverage posture, CI tiers, flaky-test handling, and privacy-minimized diagnostic artifacts. Verification intentionally traces existing canonical rule IDs rather than creating a parallel stable-rule namespace.
* [Source Topology, Package Boundaries & Dependency Enforcement](source-topology.md) — current workspace/source graph for the three deployable composition roots, six authoritative module packages, application coordination, projections, business-neutral foundation, browser layers, test ownership, package exports, pnpm workspace dependencies, and dependency-cruiser enforcement. This owner realizes existing `MOD-*`, `FE-*`, `DATA-*`, and `IMPL-*` contracts without creating a parallel package-rule namespace.
* [Runtime, Environment & Delivery Bootstrap](runtime-delivery-bootstrap.md) — current executable workspace/local-development/CI/IaC bootstrap, environment/state separation, supply-chain checks, and deployment-authority boundary. It records the still-external GitHub repository/environment administration gate rather than claiming workflow existence equals enforced protection.

# Authority rule

Accepted implementation documents are current owners for durable implementation meaning while numbered Phase 006 records preserve rationale, alternatives, and planning lineage.

Implementation code and tests may cite these contracts but cannot override upstream canonical product, UX, governance, or architecture meaning. If implementation pressure implies a semantic redesign, use the canonical `CHG-*` process rather than changing meaning only downstream.

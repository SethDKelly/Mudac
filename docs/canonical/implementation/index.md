# Implementation

Accepted MUDAC implementation contracts and toolchain decisions.

Implementation is downstream of canonical product/UX/governance and architecture knowledge. These owners define how accepted architecture may be realized in code, tests, migrations, generated contracts, CI/CD, and IaC; they do not redefine product or architecture meaning for implementation convenience.

# Current execution status

**Implementation advancement is currently frozen at the 006-D non-domain bootstrap boundary.**

The controlling current owner is [Design / Implementation Boundary](../governance/design-implementation-boundary.md). Phase 006-E through 006-M are deferred while MUDAC returns to deliberate design refinement under Phase 007+.

These implementation contracts remain valid as retained substrate decisions and future inputs, but their existence does not authorize schema, persistence, authentication, API, browser-domain, feature, or application-AWS implementation while the freeze is active.

# Accepted implementation contracts

* [Implementation Authority, Toolchain & Delivery Governance](implementation-foundation.md) — `IMPL-*` contracts for implementation authority, TypeScript/Node/Fastify/pnpm/Kysely/OpenTofu baseline, static analysis, dependency/version/generated-code policy, repository merge/deployment governance, security scanning, and implementation completion semantics.
* [Verification Strategy, Evidence & Quality Gates](verification-strategy.md) — verification contract for evidence layers, real PostgreSQL integration, deterministic fixtures/fakes, stable-rule traceability, security/accessibility/concurrency/recovery evidence, coverage posture, CI tiers, flaky-test handling, and privacy-minimized diagnostic artifacts.
* [Source Topology, Package Boundaries & Dependency Enforcement](source-topology.md) — workspace/source graph for the three deployable composition roots, six authoritative module packages, application coordination, projections, business-neutral foundation, browser layers, test ownership, package exports, pnpm workspace dependencies, and dependency-cruiser enforcement.
* [Runtime, Environment & Delivery Bootstrap](runtime-delivery-bootstrap.md) — executable workspace/local-development/CI/IaC bootstrap, environment/state separation, supply-chain checks, and deployment-authority boundary retained as the frozen prototype.

# Authority rule

Implementation documents own durable implementation meaning within their scope. The current [Design / Implementation Boundary](../governance/design-implementation-boundary.md) owns whether implementation is permitted to advance.

If an implementation document's historical handoff says a deferred 006-E+ task is “next,” that sequence is not current execution authority while the freeze is active.

Implementation code and tests cannot override upstream canonical product, UX, governance, or architecture meaning. If implementation pressure implies a semantic redesign, use the canonical `CHG-*` process rather than changing meaning only downstream.

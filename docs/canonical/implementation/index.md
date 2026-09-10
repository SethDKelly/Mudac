# Implementation

Accepted MUDAC implementation contracts and toolchain decisions.

Implementation is downstream of canonical product/UX/governance and architecture knowledge. These owners define how accepted architecture may be realized in code, tests, migrations, generated contracts, CI/CD, and IaC; they do not redefine product or architecture meaning for implementation convenience.

# Current execution status

**Implementation planning is active; new domain implementation is not yet started.**

The controlling current owner is [Design / Implementation Boundary](../governance/design-implementation-boundary.md).

The renewed Jackson Concept Design methodology formally exited in 007-I. Phase 008 has now been divided into twelve dependency-safe planning/qualification subgroups. The executable work through 006-D is retained as a protected non-domain implementation baseline. The old 006-E through 006-M sequence remains historical planning lineage and is superseded as the current executable queue.

Current status:

```text
Phase 008 subdivision: COMPLETE
implementation planning: ACTIVE
008-A: NEXT / NOT STARTED
first executable domain slice: NOT YET AUTHORIZED
new domain implementation after 006-D: NOT STARTED
```

# Active implementation-planning phase

Use [Phase 008 — Implementation Re-entry, Plan Refresh & Execution Readiness](../../008-implementation-reentry/) for current implementation-plan rationale, subgroup ordering, residual-risk disposition, and first-slice authorization work.

Phase 008 proceeds from authority/baseline qualification through persistence, Identity/Access, API/concurrency, browser continuity, operational/evaluation/outcome slice planning, cross-cutting verification, and a final explicit first-slice authorization review.

No Phase 008 subgroup implements new MUDAC domain behavior.

# Accepted implementation contracts

* [Implementation Authority, Toolchain & Delivery Governance](implementation-foundation.md) — `IMPL-*` contracts for implementation authority, TypeScript/Node/Fastify/pnpm/Kysely/OpenTofu baseline, static analysis, dependency/version/generated-code policy, repository merge/deployment governance, security scanning, and implementation completion semantics.
* [Verification Strategy, Evidence & Quality Gates](verification-strategy.md) — verification contract for evidence layers, real PostgreSQL integration, deterministic fixtures/fakes, stable-rule traceability, security/accessibility/concurrency/recovery evidence, coverage posture, CI tiers, flaky-test handling, and privacy-minimized diagnostic artifacts.
* [Source Topology, Package Boundaries & Dependency Enforcement](source-topology.md) — workspace/source graph for the three deployable composition roots, six authoritative module packages, application coordination, projections, business-neutral foundation, browser layers, test ownership, package exports, pnpm workspace dependencies, and dependency-cruiser enforcement.
* [Runtime, Environment & Delivery Bootstrap](runtime-delivery-bootstrap.md) — executable workspace/local-development/CI/IaC bootstrap, environment/state separation, supply-chain checks, and deployment-authority boundary retained as the protected 006-D baseline.

# Current planning boundary

During Phase 008, implementation work may include plan reconciliation, dependency analysis, current-baseline verification, implementation decision recording, test/evidence planning, and narrow maintenance of the protected 006-D substrate.

Do not create new MUDAC domain schema, authentication/session behavior, production domain API behavior, IndexedDB domain Draft semantics, feature code, or domain-purpose AWS application provisioning until **008-L** explicitly authorizes the first executable slice.

If 008-L authorizes that slice, actual new domain implementation begins in **Phase 009**, not inside Phase 008.

# Authority rule

Implementation documents own durable implementation meaning within their scope. The current [Design / Implementation Boundary](../governance/design-implementation-boundary.md) owns whether implementation is permitted to advance.

Historical Phase 006 handoffs are lineage rather than current execution authority. Phase 008 decides which portions remain valid, need refinement, or should be superseded.

Implementation code and tests cannot override upstream canonical product, UX, governance, synchronization, temporal, policy, or architecture meaning. If implementation pressure implies a semantic redesign, use canonical `CHG-*` governance rather than changing meaning only downstream.
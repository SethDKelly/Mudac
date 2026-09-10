# Implementation

Accepted MUDAC implementation contracts and toolchain decisions.

Implementation is downstream of canonical product/UX/governance and architecture knowledge. These owners define how accepted architecture may be realized in code, tests, migrations, generated contracts, CI/CD, and IaC; they do not redefine product or architecture meaning for implementation convenience.

# Current execution status

**Implementation planning is active; the retained 006-D bootstrap is qualified; residual/historical-plan ownership is reconciled; new domain implementation is not yet started.**

The controlling current owner is [Design / Implementation Boundary](../governance/design-implementation-boundary.md).

[008-A](../../008-implementation-reentry/008-A-implementation-reentry-authority-canonical-baseline-change-control-planning-guardrails.md) establishes the implementation-planning authority hierarchy and execution guardrails. [008-B](../../008-implementation-reentry/008-B-protected-006-D-baseline-qualification-drift-audit-toolchain-environment-reconciliation.md) qualifies the protected 006-D substrate. [008-C](../../008-implementation-reentry/008-C-residual-risk-ingestion-historical-006-mapping-decision-register-supersession-matrix.md) assigns accepted residuals and historical 006-E–M work to current planning owners.

Current status:

```text
implementation planning authority: ESTABLISHED
008-A: COMPLETE
008-B: COMPLETE — PASS AFTER NARROW REMEDIATION
protected 006-D baseline: QUALIFIED FOR PHASE 008 PLANNING
008-C: COMPLETE — PASS
historical 006-E–M executable queue: SUPERSEDED / MAPPED
008-D: NEXT / NOT STARTED
first executable domain slice: NOT YET AUTHORIZED
new domain implementation after 006-D: NOT STARTED
```

# Active implementation-planning phase

Use [Phase 008 — Implementation Re-entry, Plan Refresh & Execution Readiness](../../008-implementation-reentry/) for current planning rationale, residual-risk disposition, dependency ordering, and first-slice authorization work.

008-D is next and owns the detailed persistence, temporal truth, Versioning, Provenance, governed-exception, outbox, projection and migration implementation plan.

No Phase 008 subgroup implements new MUDAC domain behavior.

# Accepted implementation contracts

* [Implementation Authority, Toolchain & Delivery Governance](implementation-foundation.md) — `IMPL-*` contracts for implementation authority, TypeScript/Node/Fastify/pnpm/Kysely/OpenTofu baseline, static analysis, dependency/version/generated-code policy, repository merge/deployment governance, security scanning, planning-versus-execution separation, and implementation completion semantics.
* [Verification Strategy, Evidence & Quality Gates](verification-strategy.md) — verification contract for evidence layers, PostgreSQL integration, deterministic fixtures/fakes, stable-rule traceability, security/accessibility/concurrency/recovery evidence, CI tiers, flaky-test handling, and privacy-minimized diagnostic artifacts.
* [Source Topology, Package Boundaries & Dependency Enforcement](source-topology.md) — workspace/source graph for the three deployable composition roots, six authoritative module packages, application coordination, projections, business-neutral foundation, browser layers, test ownership, package exports, workspace dependencies, and dependency-cruiser enforcement.
* [Runtime, Environment & Delivery Bootstrap](runtime-delivery-bootstrap.md) — the **qualified protected 006-D baseline**: executable workspace/local-development/CI/IaC bootstrap, environment/state separation, supply-chain checks, and deployment-authority limits.

# Qualified baseline scope

008-B confirms that later Phase 008 planning may assume the retained toolchain pins, lockfile, package/source skeleton, local PostgreSQL service, dependency enforcement, CI configuration, and OpenTofu root separation are coherent planning inputs.

Qualification does not promote local PostgreSQL to a production version contract, does not establish AWS resources, and does not certify repository branch protection or zero dependency vulnerabilities.

# Reconciled planning ownership

008-C turns the accepted residual register into current downstream ownership rather than a generic backlog:

- Class 2 physical/architecture details are assigned primarily to 008-D, 008-F, or 008-J with explicit downstream consumers;
- Class 3 implementation/evidence questions are assigned across 008-D through 008-K, with 008-L retaining authorization-gate responsibility where appropriate;
- Class 4 future scope remains excluded unless `CHG-*` deliberately reopens it;
- repository protection and dependency-alert evidence limitations remain owned by 008-K/008-L;
- historical 006-E through 006-M is preserved as provenance but fully superseded as an executable roadmap.

The current dependency direction is:

```text
008-D persistence / temporal / history / provenance / exception / outbox
   ↓
008-E Identity / Participation / Access / session
   ↓
008-F commands / queries / transactions / CAS / idempotency / API
   ↓
008-G browser / Draft / synchronization / recovery
   ↓
008-H Competition + Judging Operations
   ↓
008-I Scorecard + evaluation evidence + amendment + paper
   ↓
008-J outcomes + Finalization + official outcome + Export + Publication
   ↓
008-K cross-cutting evidence / operations / retention
   ↓
008-L roadmap + first-slice authorization
```

This is planning order, not executable authorization.

# Planning authority

Implementation planning follows:

```text
canonical semantic / governance owners
        ↓
canonical architecture
        ↓
canonical implementation contracts
        ↓
Phase 008 planning decisions
        ↓
future executable realization / evidence
```

The Design / Implementation Boundary separately owns execution posture.

A planning decision or qualified substrate is not executable-slice authorization. 008-L alone may authorize the Phase 009 entry slice, and 008-L itself performs no domain implementation.

# Current planning boundary

During Phase 008, work may include plan reconciliation, dependency analysis, baseline verification, implementation decision recording, test/evidence planning, and narrow maintenance of the qualified protected 006-D substrate.

Do not create new MUDAC domain schema, authentication/session behavior, production domain API behavior, IndexedDB domain Draft semantics, feature code, or domain-purpose AWS application provisioning until **008-L** explicitly authorizes the first executable slice.

If 008-L authorizes that slice, actual new domain implementation begins in **Phase 009**, not inside Phase 008.

# Authority rule

Implementation documents own durable implementation meaning within their scope. Historical Phase 006 records remain lineage rather than current execution authority. 008-C owns the current historical-plan disposition as planning provenance; later material implementation choices are promoted into the applicable canonical implementation owner when `IMPL-015` requires it.

Implementation code and tests cannot override upstream canonical product, UX, governance, synchronization, temporal, policy, or architecture meaning. If implementation pressure implies semantic redesign, use canonical `CHG-*` governance rather than changing meaning only downstream.

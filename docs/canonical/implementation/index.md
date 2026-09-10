# Implementation

Accepted MUDAC implementation contracts and toolchain decisions.

Implementation is downstream of canonical product/UX/governance and architecture knowledge. These owners define how accepted architecture may be realized in code, tests, migrations, generated contracts, CI/CD, and IaC; they do not redefine product or architecture meaning for implementation convenience.

# Current execution status

**Implementation planning is active; the retained 006-D bootstrap is qualified; new domain implementation is not yet started.**

The controlling current owner is [Design / Implementation Boundary](../governance/design-implementation-boundary.md).

[008-A](../../008-implementation-reentry/008-A-implementation-reentry-authority-canonical-baseline-change-control-planning-guardrails.md) establishes the implementation-planning authority hierarchy and execution guardrails. [008-B](../../008-implementation-reentry/008-B-protected-006-D-baseline-qualification-drift-audit-toolchain-environment-reconciliation.md) has qualified the protected 006-D substrate after narrow non-domain remediation.

Current status:

```text
implementation planning authority: ESTABLISHED
008-A: COMPLETE
008-B: COMPLETE — PASS AFTER NARROW REMEDIATION
protected 006-D baseline: QUALIFIED FOR PHASE 008 PLANNING
008-C: NEXT / NOT STARTED
first executable domain slice: NOT YET AUTHORIZED
new domain implementation after 006-D: NOT STARTED
```

# Active implementation-planning phase

Use [Phase 008 — Implementation Re-entry, Plan Refresh & Execution Readiness](../../008-implementation-reentry/) for current planning rationale, residual-risk disposition, dependency ordering, and first-slice authorization work.

008-C next maps the 007-H/007-I residual register and historical 006-E–M work into explicit current planning owners now that the retained substrate has been qualified.

No Phase 008 subgroup implements new MUDAC domain behavior.

# Accepted implementation contracts

* [Implementation Authority, Toolchain & Delivery Governance](implementation-foundation.md) — `IMPL-*` contracts for implementation authority, TypeScript/Node/Fastify/pnpm/Kysely/OpenTofu baseline, static analysis, dependency/version/generated-code policy, repository merge/deployment governance, security scanning, planning-versus-execution separation, and implementation completion semantics.
* [Verification Strategy, Evidence & Quality Gates](verification-strategy.md) — verification contract for evidence layers, PostgreSQL integration, deterministic fixtures/fakes, stable-rule traceability, security/accessibility/concurrency/recovery evidence, CI tiers, flaky-test handling, and privacy-minimized diagnostic artifacts.
* [Source Topology, Package Boundaries & Dependency Enforcement](source-topology.md) — workspace/source graph for the three deployable composition roots, six authoritative module packages, application coordination, projections, business-neutral foundation, browser layers, test ownership, package exports, workspace dependencies, and dependency-cruiser enforcement.
* [Runtime, Environment & Delivery Bootstrap](runtime-delivery-bootstrap.md) — the **qualified protected 006-D baseline**: executable workspace/local-development/CI/IaC bootstrap, environment/state separation, supply-chain checks, and deployment-authority limits.

# Qualified baseline scope

008-B confirms that later Phase 008 planning may assume the retained toolchain pins, lockfile, package/source skeleton, local PostgreSQL service, dependency enforcement, CI configuration, and OpenTofu root separation are coherent planning inputs.

Qualification does not promote local PostgreSQL to a production version contract, does not establish AWS resources, and does not certify repository branch protection or zero dependency vulnerabilities.

The repository rulesets endpoint currently exposes no rulesets; branch protection is unreadable through the current integration. Dependabot is configured but its alert inventory is not available through this connector. These remain explicit evidence/administration limits.

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

Implementation documents own durable implementation meaning within their scope. Historical Phase 006 records remain lineage rather than current execution authority.

Implementation code and tests cannot override upstream canonical product, UX, governance, synchronization, temporal, policy, or architecture meaning. If implementation pressure implies semantic redesign, use canonical `CHG-*` governance rather than changing meaning only downstream.

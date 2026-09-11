# Implementation

Accepted MUDAC implementation contracts and toolchain decisions.

Implementation is downstream of canonical product/UX/governance and architecture knowledge. These owners define how accepted architecture may be realized in code, tests, migrations, generated contracts, CI/CD, and IaC; they do not redefine product or architecture meaning for implementation convenience.

# Current execution status

**Implementation planning is active; the retained 006-D bootstrap is qualified; persistence/history and Identity/authentication/Access/session implementation contracts are accepted; new domain implementation is not yet started.**

The controlling current owner is [Design / Implementation Boundary](../governance/design-implementation-boundary.md).

[008-A](../../008-implementation-reentry/008-A-implementation-reentry-authority-canonical-baseline-change-control-planning-guardrails.md) establishes planning authority. [008-B](../../008-implementation-reentry/008-B-protected-006-D-baseline-qualification-drift-audit-toolchain-environment-reconciliation.md) qualifies the protected 006-D substrate. [008-C](../../008-implementation-reentry/008-C-residual-risk-ingestion-historical-006-mapping-decision-register-supersession-matrix.md) assigns residual/historical work to current owners. [008-D](../../008-implementation-reentry/008-D-persistence-temporal-truth-versioning-provenance-governed-exceptions-outbox-projection-migration-implementation-plan.md) resolves the persistence/history implementation contract. [008-E](../../008-implementation-reentry/008-E-identity-authentication-participation-access-session-invitation-secrets-technical-authority-implementation-plan.md) resolves the Identity/authentication/Participation/Access/session/invitation/secrets/technical-authority contract.

Current status:

```text
implementation planning authority: ESTABLISHED
008-A: COMPLETE
008-B: COMPLETE — PASS AFTER NARROW REMEDIATION
008-C: COMPLETE — PASS
008-D: COMPLETE — PASS
008-E: COMPLETE — PASS
protected 006-D baseline: QUALIFIED FOR PHASE 008 PLANNING
persistence/history implementation contract: ACCEPTED / NOT IMPLEMENTED
identity/auth/access/session implementation contract: ACCEPTED / NOT IMPLEMENTED
008-F: NEXT / NOT STARTED
first executable domain slice: NOT YET AUTHORIZED
new domain implementation after 006-D: NOT STARTED
```

# Active implementation-planning phase

Use [Phase 008 — Implementation Re-entry, Plan Refresh & Execution Readiness](../../008-implementation-reentry/) for current planning rationale, dependency ordering, and first-slice authorization work.

008-F is next and owns commands, queries, transaction composition, CAS, idempotency, concurrency, lost-response reconciliation and HTTP/API implementation planning using the accepted persistence and server-derived Identity/Participation/Access context contracts.

No Phase 008 subgroup implements new MUDAC domain behavior.

# Accepted implementation contracts

* [Implementation Authority, Toolchain & Delivery Governance](implementation-foundation.md) — `IMPL-*` contracts for implementation authority, TypeScript/Node/Fastify/pnpm/Kysely/OpenTofu baseline, static analysis, dependency/version/generated-code policy, repository merge/deployment governance, security scanning, planning-versus-execution separation, and implementation completion semantics.
* [Verification Strategy, Evidence & Quality Gates](verification-strategy.md) — verification contract for evidence layers, PostgreSQL/migration integration, deterministic fixtures/fakes, stable-rule traceability, security/accessibility/concurrency/recovery evidence, CI tiers, flaky-test handling, and privacy-minimized diagnostic artifacts.
* [Source Topology, Package Boundaries & Dependency Enforcement](source-topology.md) — workspace/source graph for the deployable composition roots, six authoritative module packages, application coordination, projections, business-neutral foundation, browser layers, test ownership, persistence/migration placement, package exports, workspace dependencies, and dependency-cruiser enforcement.
* [Runtime, Environment & Delivery Bootstrap](runtime-delivery-bootstrap.md) — the **qualified protected 006-D baseline**: executable workspace/local-development/CI/IaC bootstrap, environment/state separation, supply-chain checks, and deployment-authority limits.
* [Persistence, History, Provenance, Outbox, Projection & Migration Implementation Contract](persistence-history-projection.md) — accepted 008-D physical realization for PostgreSQL schema ownership, stable identity/revision conventions, mutable-current versus immutable Version/history state, module-local Provenance, policy-specific governed exceptions, Official Outcome Revision substrate, transactional outbox, basis-aware projections, SQL-first migrations, and conservative retention defaults.
* [Identity, Authentication, Participation, Access, Session, Invitation, Secrets & Technical Authority Implementation Contract](identity-authentication-access-session.md) — accepted 008-E realization for Cognito/OIDC adapter boundaries, issuer/subject principal linkage, Participation context isolation, contextual Access, opaque PostgreSQL-backed sessions, bounded invitation/recovery/reverification mechanics, server-only secrets, and technical-versus-semantic authority separation.

# Accepted dependency baseline for 008-F

Downstream command/API planning may now rely on:

```text
one module-owned PostgreSQL authority model
+ explicit current/history/version/provenance conventions
+ transaction-capable owner-local adapters
+ opaque server-managed session
+ server-derived MUDAC Identity
+ exactly one selected Participation context
+ contextual Access/grant evaluation
+ resource owner remains final semantic gate
```

The browser/client may never supply authoritative Identity, role, Participation, Cognito group, operator state, or permission claims.

Session validity does not prolong revoked/expired capability. Event Completed removes ordinary Judge private-evaluation Access from current source-state authorization even if a cookie remains valid. Step-up strengthens authentication assurance but does not create semantic authority. Technical/support privilege cannot synthesize a Judge or Organizer Participation.

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

A qualified substrate or accepted implementation contract is not executable-slice authorization. 008-L alone may authorize the Phase 009 entry slice, and 008-L itself performs no domain implementation.

# Current planning boundary

During Phase 008, work may include plan reconciliation, dependency analysis, implementation decision recording, test/evidence planning, and narrow maintenance of the qualified protected 006-D substrate.

Do not create new MUDAC domain schema/migrations/repositories/outbox/projections, Cognito/session/Identity/Participation/Access behavior, production domain API behavior, IndexedDB domain Draft semantics, feature code, or domain-purpose AWS application provisioning until **008-L** explicitly authorizes the first executable slice.

If 008-L authorizes that slice, actual new domain implementation begins in **Phase 009**, not inside Phase 008.

# Authority rule

Implementation documents own durable implementation meaning within their scope. Historical Phase 006 records remain lineage rather than current execution authority. 008-C owns residual/historical-plan disposition as planning provenance. 008-D and 008-E promote their durable implementation choices into dedicated canonical implementation owners under `IMPL-015`.

Implementation code and tests cannot override upstream canonical product, UX, governance, synchronization, temporal, policy, or architecture meaning. If implementation pressure implies semantic redesign, use canonical `CHG-*` governance rather than changing meaning only downstream.

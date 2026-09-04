# MUDAC Design Documentation

The repository is the durable design authority; conversation history is working context.

## Preferred navigation

Start at [index.md](index.md), the OKF v0.2 bundle root.

For current product/domain, conceptual UX, governance, and accepted architecture meaning, use [Canonical Knowledge](canonical/). Repository agents use root [`AGENTS.md`](../AGENTS.md) as a thin bootstrap into the same canonical governance.

Use numbered phase directories for rationale, design evolution, architecture alternatives, implementation planning, and source provenance. Each numbered phase has an `index.md` that routes history/planning toward current canonical authority where applicable.

## Governance

Current governance lives under [canonical/governance/](canonical/governance/), including:

* [Documentation Authority & Canonical Ownership](canonical/governance/documentation-authority.md) — `DOC-*`;
* [Agent Context & Progressive Retrieval](canonical/governance/agent-context.md) — `CTX-*`;
* [Canonical Change & Conflict Governance](canonical/governance/change-governance.md) — `CHG-*`;
* [OKF Metadata, Trust, Verification, Lifecycle & Freshness](canonical/governance/metadata-trust-lifecycle.md) — `META-*`;
* [Knowledge Validation & CI Enforcement](canonical/governance/validation-enforcement.md) — `VAL-*`;
* [Stable Rule Identifiers](canonical/governance/rule-identifiers.md);
* [Source Lineage](canonical/governance/source-lineage.md).

These owners govern the details. This README routes to them and does not reproduce their rule bodies.

## Design / implementation-planning status

* Phase 001 — Concept Design Foundation: **Complete**
* Phase 002 — Concept Specification, Policy & Synchronization Refinement: **Complete**
* Phase 003 — Conceptual UX Architecture: **Complete**
* Phase 004 — Knowledge Architecture, OKF Retrofit & Documentation Governance: **Complete**
* Phase 005 — System, Application, Data & Synchronization Architecture: **Complete**
* Phase 006 — Implementation Planning, Delivery Slices & Verification Strategy: **In Progress**
  * **006-A — Implementation Authority, Delivery Governance, Toolchain & Repository Enforcement: Next**
  * 006-B through 006-H — verification and implementation foundations: Planned
  * 006-I through 006-L — dependency-ordered end-to-end domain slices: Planned
  * 006-M — integrated hardening, operational readiness and phase exit: Planned

The complete Phase 006 subgroup plan and dependency graph live in [006-implementation-planning/README.md](006-implementation-planning/README.md).

Current accepted architecture is routed through [canonical/architecture/](canonical/architecture/): the [Architectural Foundation](canonical/architecture/architectural-foundation.md) owns `ARCH-*`, [Application Boundaries](canonical/architecture/application-boundaries.md) owns `MOD-*`, [Data & Persistence Architecture](canonical/architecture/data-persistence.md) owns `DATA-*`, [Identity, Authentication, Access & Session Architecture](canonical/architecture/identity-access-session.md) owns `AUTH-*`, [Commands, Queries, API, Transaction & Concurrency Architecture](canonical/architecture/commands-api-concurrency.md) owns `API-*`, [Draft Synchronization, Offline & Recovery Architecture](canonical/architecture/synchronization-recovery.md) owns `SYNC-*`, [External Representation, Artifact & Publication Architecture](canonical/architecture/external-representation.md) owns `REP-*`, [Front-End State, Navigation & Interaction Architecture](canonical/architecture/frontend-interaction.md) owns `FE-*`, and [AWS Runtime, Security & Operations Architecture](canonical/architecture/aws-runtime-operations.md) owns `AWS-*`.

The [005-J exit review](005-system-application-data-synchronization-architecture/005-J-phase-005-consolidation-threat-failure-review-implementation-readiness-exit.md) confirms that these owners compose without a blocking authority contradiction. MUDAC is **implementation-planning ready, not production certified**. Phase 006 is responsible for converting those contracts and exit gates into enforceable tooling, tests, package/source boundaries, foundations, vertical delivery slices, and measured readiness evidence without silently changing accepted semantics.

Knowledge CI checks deterministic structure, links, stable IDs, source edges, and routing. A green validation run is structural evidence only and never creates `verified` metadata or replaces semantic review.
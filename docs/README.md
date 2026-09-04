# MUDAC Design Documentation

The repository is the durable design authority; conversation history is working context.

## Preferred navigation

Start at [index.md](index.md), the OKF v0.2 bundle root.

For current product/domain, conceptual UX, governance, accepted architecture, and accepted implementation meaning, use [Canonical Knowledge](canonical/). Repository agents use root [`AGENTS.md`](../AGENTS.md) as a thin bootstrap into the same canonical governance.

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
  * 006-A — Implementation Authority, Delivery Governance, Toolchain & Repository Enforcement: **Complete**
  * 006-B — Verification Strategy, Test Harness, Evidence Fixtures & Quality Gates: **Complete**
  * **006-C — Source Topology, Module/Package Boundaries, Shared Foundation & Dependency Enforcement: Next**
  * 006-D through 006-H — remaining implementation foundations: Planned
  * 006-I through 006-L — dependency-ordered end-to-end domain slices: Planned
  * 006-M — integrated hardening, operational readiness and phase exit: Planned

The complete Phase 006 subgroup plan and dependency graph live in [006-implementation-planning/README.md](006-implementation-planning/README.md).

Current accepted architecture is routed through [canonical/architecture/](canonical/architecture/). Current accepted implementation meaning is routed through [canonical/implementation/](canonical/implementation/): [Implementation Authority, Toolchain & Delivery Governance](canonical/implementation/implementation-foundation.md) owns `IMPL-001` through `IMPL-016`, while [Verification Strategy, Evidence & Quality Gates](canonical/implementation/verification-strategy.md) owns the current evidence/test/CI model without creating a duplicate stable-rule namespace.

The implementation baseline uses Node.js 24 LTS + TypeScript, pnpm workspaces, Fastify, Kysely + node-postgres with explicit migrations, transport schemas generating OpenAPI outward, Vitest/Playwright, strict TypeScript + ESLint + Prettier, OpenTofu, layered scanning, committed lockfiles/reproducible generation, intended PR/check-gated `main`, and separately gated production deployment authority.

The verification baseline requires real PostgreSQL for database/concurrency semantics, deterministic synthetic fixtures and explicit external/nondeterministic seams, module-owned test builders, critical Playwright journeys, Testing Library-style semantic component tests, automated axe-compatible accessibility checks plus manual accessibility evidence before production readiness, behavioral security/authority/disclosure testing in addition to scanners, explicit retry/conflict/uncertainty/recovery evidence, narrow golden fixtures, coverage as diagnostic evidence, visible treatment of flakiness, and privacy-minimized CI artifacts. Evidence traces existing canonical rule IDs rather than copying rule bodies.

Actual implementation workflow/ruleset enforcement remains a 006-D action because the repository has not yet been bootstrapped with application CI and this design-session GitHub connection cannot administer branch protection/rulesets.

The [005-J exit review](005-system-application-data-synchronization-architecture/005-J-phase-005-consolidation-threat-failure-review-implementation-readiness-exit.md) confirms that the architecture owners compose without a blocking authority contradiction. MUDAC is **implementation-planning ready, not production certified**. Phase 006 converts those contracts and exit gates into enforceable tooling, tests, package/source boundaries, foundations, vertical delivery slices, and measured readiness evidence without silently changing accepted semantics.

Knowledge CI checks deterministic structure, links, stable IDs, source edges, and routing. A green validation run is structural evidence only and never creates `verified` metadata or replaces semantic review.
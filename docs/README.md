# MUDAC Design Documentation

The repository is the durable design authority; conversation history is working context.

## Preferred navigation

Start at [index.md](index.md), the OKF v0.2 bundle root.

For current product/domain, conceptual UX, governance, and accepted architecture meaning, use [Canonical Knowledge](canonical/). Repository agents use root [`AGENTS.md`](../AGENTS.md) as a thin bootstrap into the same canonical governance.

Use numbered phase directories for rationale, design evolution, architecture alternatives, and source provenance. Each numbered phase has an OKF `index.md` that maps records forward to current canonical successors.

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

## Design status

* Phase 001 — Concept Design Foundation: **Complete**
* Phase 002 — Concept Specification, Policy & Synchronization Refinement: **Complete**
* Phase 003 — Conceptual UX Architecture: **Complete**
* Phase 004 — Knowledge Architecture, OKF Retrofit & Documentation Governance: **Complete**
* Phase 005 — System, Application, Data & Synchronization Architecture: **In Progress**
  * 005-A — Architectural Drivers, Quality Attributes, Trust Boundaries & Decision Principles: **Complete**
  * 005-B — Application Boundaries, Modules, Domain Services & Dependency Architecture: **Complete**
  * **005-C — Data Model, Persistence, Versioning, Provenance & Derived-Projection Architecture: Next**

Current accepted architecture is routed through [canonical/architecture/](canonical/architecture/): the [Architectural Foundation](canonical/architecture/architectural-foundation.md) owns `ARCH-*`, and [Application Boundaries](canonical/architecture/application-boundaries.md) owns `MOD-*`.

The current application posture is modular-monolith-first with explicit semantic module ownership, non-authoritative cross-module projections, thin coordination above owners, and infrastructure dependency inversion. No database, API protocol, identity provider, front-end framework, or AWS service has yet been selected.

Knowledge CI checks deterministic structure, links, stable IDs, source edges, and routing. A green validation run is structural evidence only and never creates `verified` metadata or replaces semantic review.
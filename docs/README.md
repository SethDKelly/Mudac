# MUDAC Design Documentation

The repository is the durable design authority; conversation history is working context.

## Preferred navigation

Start at [index.md](index.md), the OKF v0.2 bundle root.

For current product/domain and conceptual UX meaning, use [Canonical Knowledge](canonical/). Repository agents use root [`AGENTS.md`](../AGENTS.md) as a thin bootstrap into the same canonical governance.

Use numbered phase directories for rationale, design evolution, and source provenance. Each numbered phase has an OKF `index.md` that maps historical records forward to current canonical successors.

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

Daniel Jackson Concept Design remains the product-design methodology; OKF structures and exposes the resulting knowledge. Canonical current knowledge constrains later architecture/implementation, and downstream artifacts cannot override it merely by restating different behavior.

Knowledge CI checks deterministic structure, links, stable IDs, source edges, and routing. A green validation run is structural evidence only and never creates `verified` metadata or replaces semantic review.

The Phase 004 migration and exit review are complete. Phase 001–003 historical records remain intentionally preserved without bulk metadata rewrite; ordinary retrieval should use canonical owners and follow history only when rationale/provenance is needed.

## Design status

* Phase 001 — Concept Design Foundation: **Complete**
* Phase 002 — Concept Specification, Policy & Synchronization Refinement: **Complete**
* Phase 003 — Conceptual UX Architecture: **Complete**
* Phase 004 — Knowledge Architecture, OKF Retrofit & Documentation Governance: **Complete**
* **Phase 005 — System, Application, Data & Synchronization Architecture: Next**

Phase 005 should start from task-relevant canonical product/UX/governance owners and stable rules. Accepted architecture decisions belong under [canonical/architecture/](canonical/architecture/); numbered Phase 005 records should preserve alternatives, rationale, and source lineage.

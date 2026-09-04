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

Knowledge CI now checks deterministic structure, links, stable IDs, source edges, and routing. A green validation run is structural evidence only and never creates `verified` metadata or replaces semantic review.

## Phase 004 status

* 004-A — Complete
* 004-B — Complete
* 004-C — Complete
* 004-D — Complete
* 004-E — Complete
* 004-F — Complete
* 004-G — Complete
* 004-H — Complete
* **004-I — Next: Repository-Wide Knowledge Graph / Drift Audit & Migration Closure**

System/Application/Data/Synchronization Architecture is planned as Phase 005 after the knowledge-governance retrofit is complete.

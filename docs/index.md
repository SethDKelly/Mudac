---
okf_version: "0.2"
---

# MUDAC Knowledge Bundle

Preferred progressive-disclosure entry point for MUDAC design and architecture knowledge.

Phase 004 has established baseline canonical product/UX knowledge, bidirectional historical lineage, stable high-value rule IDs, repository/agent governance, and the MUDAC OKF metadata/trust/lifecycle profile. Structural validation and final migration audit remain in progress.

# Current Canonical Knowledge

* [Canonical Knowledge](canonical/) - Current MUDAC Concepts, mechanisms, policies, invariants, experience contracts, and governance knowledge.
* [Governance](canonical/governance/) - Documentation authority, agent context, canonical change/conflict rules, source lineage, methodology/terminology, metadata/trust/lifecycle, and stable IDs.
* [Stable Rule Identifiers](canonical/governance/rule-identifiers.md) - Durable normative IDs and cross-reference registry.
* [OKF Metadata, Trust, Verification, Lifecycle & Freshness](canonical/governance/metadata-trust-lifecycle.md) - `META-*` profile for truthful generation/verification/lifecycle/freshness metadata.

# Agent bootstrap

Repository agents begin with [`AGENTS.md`](../AGENTS.md), then follow this bundle root and the relevant canonical owner(s). `AGENTS.md` is an adapter to canonical governance, not a competing rule store.

# External Authorities and References

* [References](references/) - External methodologies, standards, specifications, and MUDAC adoption/profile context, including the pinned [Open Knowledge Format v0.2](references/open-knowledge-format.md) reference.

# Design History and Active Design Work

Each phase directory has an `index.md` that routes historical records toward current canonical successors.

* [Phase 001 — Concept Design Foundation](001-concept-design/) - Concept discovery and initial catalog history.
* [Phase 002 — Concept Specification](002-concept-specification/) - Behavioral, policy, authority, and evidence specification history.
* [Phase 003 — Conceptual UX Architecture](003-conceptual-ux-architecture/) - UX architecture and exit history.
* [Phase 004 — Knowledge Architecture](004-knowledge-architecture/) - Active OKF retrofit/documentation-governance work.

# Navigation Guidance

For current meaning, start with [Canonical Knowledge](canonical/) and load only task-relevant owners/dependencies. When a stable rule ID exists, link the exact owner/anchor instead of creating another normative copy.

For rationale/chronology, follow material `sources` or enter history through a phase `index.md`. Do not recursively load the historical corpus by default.

For external standards/methodology authority, use [References](references/).

For OKF trust/lifecycle interpretation, use the canonical `META-*` profile rather than inferring meaning from field names.

See [docs/README.md](README.md) for a human-oriented authority summary.

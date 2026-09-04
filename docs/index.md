---
okf_version: "0.2"
---

# MUDAC Knowledge Bundle

Preferred progressive-disclosure entry point for MUDAC design, architecture, and implementation-planning knowledge.

Current product/domain, conceptual UX, documentation-governance, accepted architecture, and accepted implementation meaning is organized under canonical knowledge. Numbered phase directories preserve design/history/planning provenance. The OKF migration is structurally closed; legacy Phase 001–003 records remain intentionally preserved rather than bulk-rewritten for cosmetic metadata conformity.

# Current Canonical Knowledge

* [Canonical Knowledge](canonical/) - Current MUDAC Concepts, mechanisms, policies, invariants, experience contracts, governance knowledge, architecture, and accepted implementation contracts.
* [Governance](canonical/governance/) - Documentation authority, agent context, canonical change/conflict, source lineage, methodology/terminology, metadata/trust/lifecycle, validation/CI, and stable IDs.
* [Stable Rule Identifiers](canonical/governance/rule-identifiers.md) - Durable normative IDs and cross-reference registry, including current `ARCH-*`, `MOD-*`, `DATA-*`, `AUTH-*`, `API-*`, `SYNC-*`, `REP-*`, `FE-*`, `AWS-*`, and `IMPL-*` rules.
* [Knowledge Validation & CI Enforcement](canonical/governance/validation-enforcement.md) - `VAL-*` contract for deterministic structural checks and read-only CI.
* [Architecture](canonical/architecture/) - Current accepted system/application architecture contracts.
* [Implementation](canonical/implementation/) - Current accepted implementation contracts, including [Implementation Authority, Toolchain & Delivery Governance](canonical/implementation/implementation-foundation.md) and [Verification Strategy, Evidence & Quality Gates](canonical/implementation/verification-strategy.md).

# Agent bootstrap

Repository agents begin with [`AGENTS.md`](../AGENTS.md), then follow this bundle root and the relevant canonical owner(s). `AGENTS.md` is an adapter to canonical governance, not a competing rule store.

# External Authorities and References

* [References](references/) - External methodologies, standards, specifications, and MUDAC adoption/profile context, including the pinned [Open Knowledge Format v0.2](references/open-knowledge-format.md) reference.

# Design History and Active Implementation Planning

Each completed phase directory has an `index.md` that routes phase records toward current canonical successors. Active Phase 006 planning remains subordinate to those canonical owners.

* [Phase 001 — Concept Design Foundation](001-concept-design/) - Completed Concept discovery and initial-catalog history.
* [Phase 002 — Concept Specification](002-concept-specification/) - Completed behavioral, policy, authority, and evidence specification history.
* [Phase 003 — Conceptual UX Architecture](003-conceptual-ux-architecture/) - Completed UX architecture and exit history.
* [Phase 004 — Knowledge Architecture](004-knowledge-architecture/) - Completed OKF retrofit, documentation-governance, validation, migration-closure, and knowledge-architecture exit history.
* [Phase 005 — System, Application, Data & Synchronization Architecture](005-system-application-data-synchronization-architecture/) - **Complete**. Architecture owners, AWS realization, integrated threat/failure review, and implementation-readiness exit are closed.
* [Phase 006 — Implementation Planning, Delivery Slices & Verification Strategy](006-implementation-planning/) - **In Progress**. 006-A and 006-B are complete; **006-C — Source Topology, Module/Package Boundaries, Shared Foundation & Dependency Enforcement is next**.

# Navigation Guidance

For current meaning, start with [Canonical Knowledge](canonical/) and load only task-relevant owners/dependencies. When a stable rule ID exists, link the exact owner/anchor instead of creating another normative copy.

For rationale/chronology, follow material `sources` or enter history through a phase `index.md`. Do not recursively load the historical corpus by default.

For external standards/methodology authority, use [References](references/).

For validation semantics, use the canonical `VAL-*` contract. Passing CI is structural evidence only and is never an OKF verification event.

For implementation work, begin with the relevant [Canonical Implementation](canonical/implementation/) owner(s), the architecture owner(s) they realize, and only the product/UX/governance constraints materially relevant to the task. Verification work should also load [Verification Strategy, Evidence & Quality Gates](canonical/implementation/verification-strategy.md) and trace evidence to existing canonical rule IDs rather than copying rule text. Do not infer package/source topology from the knowledge-directory tree.

See [docs/README.md](README.md) for a human-oriented authority summary.
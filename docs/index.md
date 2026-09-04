---
okf_version: "0.2"
---

# MUDAC Knowledge Bundle

Preferred progressive-disclosure entry point for MUDAC design and architecture knowledge.

Current product/domain, conceptual UX, documentation-governance, and accepted architecture meaning is organized under canonical knowledge. Numbered phase directories preserve design history and material provenance. The OKF migration is structurally closed; legacy Phase 001–003 records remain intentionally preserved rather than bulk-rewritten for cosmetic metadata conformity.

# Current Canonical Knowledge

* [Canonical Knowledge](canonical/) - Current MUDAC Concepts, mechanisms, policies, invariants, experience contracts, governance knowledge, and accepted architecture.
* [Governance](canonical/governance/) - Documentation authority, agent context, canonical change/conflict, source lineage, methodology/terminology, metadata/trust/lifecycle, validation/CI, and stable IDs.
* [Stable Rule Identifiers](canonical/governance/rule-identifiers.md) - Durable normative IDs and cross-reference registry, including current `ARCH-*`, `MOD-*`, `DATA-*`, `AUTH-*`, and `API-*` architecture rules.
* [Knowledge Validation & CI Enforcement](canonical/governance/validation-enforcement.md) - `VAL-*` contract for deterministic structural checks and read-only CI.
* [Architecture](canonical/architecture/) - Current accepted architecture contracts, including the [Architectural Foundation](canonical/architecture/architectural-foundation.md), [Application Boundaries](canonical/architecture/application-boundaries.md), [Data & Persistence Architecture](canonical/architecture/data-persistence.md), [Identity, Authentication, Access & Session Architecture](canonical/architecture/identity-access-session.md), and [Commands, Queries, API, Transaction & Concurrency Architecture](canonical/architecture/commands-api-concurrency.md).

# Agent bootstrap

Repository agents begin with [`AGENTS.md`](../AGENTS.md), then follow this bundle root and the relevant canonical owner(s). `AGENTS.md` is an adapter to canonical governance, not a competing rule store.

# External Authorities and References

* [References](references/) - External methodologies, standards, specifications, and MUDAC adoption/profile context, including the pinned [Open Knowledge Format v0.2](references/open-knowledge-format.md) reference.

# Design History and Active Design Work

Each phase directory has an `index.md` that routes phase records toward current canonical successors.

* [Phase 001 — Concept Design Foundation](001-concept-design/) - Concept discovery and initial catalog history.
* [Phase 002 — Concept Specification](002-concept-specification/) - Behavioral, policy, authority, and evidence specification history.
* [Phase 003 — Conceptual UX Architecture](003-conceptual-ux-architecture/) - UX architecture and exit history.
* [Phase 004 — Knowledge Architecture](004-knowledge-architecture/) - Completed OKF retrofit, documentation-governance, validation, migration-closure, and knowledge-architecture exit history.
* [Phase 005 — System, Application, Data & Synchronization Architecture](005-system-application-data-synchronization-architecture/) - **Active** architecture design. 005-A through 005-E are complete; 005-F is next.

# Navigation Guidance

For current meaning, start with [Canonical Knowledge](canonical/) and load only task-relevant owners/dependencies. When a stable rule ID exists, link the exact owner/anchor instead of creating another normative copy.

For rationale/chronology, follow material `sources` or enter history through a phase `index.md`. Do not recursively load the historical corpus by default.

For external standards/methodology authority, use [References](references/).

For validation semantics, use the canonical `VAL-*` contract. Passing CI is structural evidence only and is never an OKF verification event.

For architecture work, begin with the relevant current architecture owner plus the task-specific upstream product/UX/governance constraints. Do not infer application topology from the knowledge-directory tree.

See [docs/README.md](README.md) for a human-oriented authority summary.
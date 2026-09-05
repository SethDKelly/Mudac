---
okf_version: "0.2"
---

# MUDAC Knowledge Bundle

Preferred progressive-disclosure entry point for MUDAC design, architecture, and implementation knowledge.

Current product/domain, conceptual UX, documentation-governance, accepted architecture, and accepted implementation meaning is organized under canonical knowledge. Numbered phase directories preserve design/history/planning provenance.

# Current Canonical Knowledge

* [Canonical Knowledge](canonical/) — current MUDAC Concepts, mechanisms, policies, invariants, experience contracts, governance, architecture, and implementation contracts.
* [Governance](canonical/governance/) — documentation authority, agent context, change/conflict, source lineage, metadata/trust/lifecycle, validation/CI, and stable IDs.
* [Stable Rule Identifiers](canonical/governance/rule-identifiers.md) — durable normative IDs and cross-reference registry.
* [Architecture](canonical/architecture/) — current accepted system/application architecture contracts.
* [Implementation](canonical/implementation/) — current implementation owners: [Implementation Authority, Toolchain & Delivery Governance](canonical/implementation/implementation-foundation.md), [Verification Strategy, Evidence & Quality Gates](canonical/implementation/verification-strategy.md), [Source Topology, Package Boundaries & Dependency Enforcement](canonical/implementation/source-topology.md), and [Runtime, Environment & Delivery Bootstrap](canonical/implementation/runtime-delivery-bootstrap.md).

# Agent bootstrap

Repository agents begin with [`AGENTS.md`](../AGENTS.md), then follow this bundle root and only the task-relevant canonical owners. `AGENTS.md` is an adapter, not a competing rule store.

# External Authorities and References

* [References](references/) — external methodologies, standards, specifications, and MUDAC adoption/profile context, including the pinned Open Knowledge Format v0.2 reference.

# Design History and Active Implementation

* [Phase 001 — Concept Design Foundation](001-concept-design/) — Complete.
* [Phase 002 — Concept Specification](002-concept-specification/) — Complete.
* [Phase 003 — Conceptual UX Architecture](003-conceptual-ux-architecture/) — Complete.
* [Phase 004 — Knowledge Architecture](004-knowledge-architecture/) — Complete.
* [Phase 005 — System, Application, Data & Synchronization Architecture](005-system-application-data-synchronization-architecture/) — **Complete**.
* [Phase 006 — Implementation Planning, Delivery Slices & Verification Strategy](006-implementation-planning/) — **In Progress**. 006-A through 006-D are complete; **006-E — Persistence, Schema, Migration, Provenance, Outbox & Projection Foundation is next**.

# Navigation Guidance

For current meaning, use [Canonical Knowledge](canonical/) and load only task-relevant owners/dependencies. Use phase records for rationale, chronology, rejected alternatives, and implementation lineage.

For implementation work, begin with the relevant [Canonical Implementation](canonical/implementation/) owner(s), the architecture owner(s) they realize, and only materially relevant product/UX/governance constraints. Runtime/environment/CI/IaC work should load [Runtime, Environment & Delivery Bootstrap](canonical/implementation/runtime-delivery-bootstrap.md).

Passing Knowledge Validation or Implementation Verification is evidence for the checked revision; neither creates OKF verification metadata or production certification.

See [docs/README.md](README.md) for a human-oriented authority summary.

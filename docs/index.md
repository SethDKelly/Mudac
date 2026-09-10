---
okf_version: "0.2"
---

# MUDAC Knowledge Bundle

Preferred progressive-disclosure entry point for MUDAC design, architecture, implementation, and governance knowledge.

Current meaning is organized under canonical knowledge. Numbered phase directories preserve design/history/planning provenance.

# Current Canonical Knowledge

* [Canonical Knowledge](canonical/) — current MUDAC Concepts, synchronizations, mechanisms, policies, invariants, experience contracts, governance, architecture, and implementation contracts.
* [Concepts](canonical/concepts/) — current sixteen-Concept Jackson catalog.
* [Synchronizations](canonical/synchronizations/) — current cross-concept coordination plus temporal/correction/historical-truth contracts.
* [Policies](canonical/policies/) — Evaluation, disclosure, Panel composition, correction/finalization, continuity, and [Operational Exception & Override Governance](canonical/policies/operational-exception-governance.md).
* [Experience](canonical/experience/) — current Judge/Organizer interaction semantics, including [Experience Action, State & Authority Traceability](canonical/experience/action-authority-traceability.md).
* [Governance](canonical/governance/) — documentation authority, agent context, change/conflict, source lineage, metadata/trust/lifecycle, validation/CI, stable IDs, and the current [Design / Implementation Boundary](canonical/governance/design-implementation-boundary.md).
* [Stable Rule Identifiers](canonical/governance/rule-identifiers.md) — durable normative IDs and cross-reference registry.
* [Architecture](canonical/architecture/) — current accepted system/application architecture contracts.
* [Implementation](canonical/implementation/) — accepted implementation/tooling contracts plus the protected 006-D non-domain bootstrap baseline.

# Agent bootstrap

Repository agents begin with [`AGENTS.md`](../AGENTS.md), then follow this bundle root and only task-relevant canonical owners. `AGENTS.md` is an adapter, not a competing rule store.

Before any implementation/code/IaC task, load [Design / Implementation Boundary](canonical/governance/design-implementation-boundary.md).

# External Authorities and References

* [References](references/) — external methodologies, standards, specifications, and MUDAC adoption/profile context, including the pinned Open Knowledge Format v0.2 reference.

# Design History and Current Phase

* [Phase 001 — Concept Design Foundation](001-concept-design/) — Complete.
* [Phase 002 — Concept Specification](002-concept-specification/) — Complete.
* [Phase 003 — Conceptual UX Architecture](003-conceptual-ux-architecture/) — Complete.
* [Phase 004 — Knowledge Architecture](004-knowledge-architecture/) — Complete.
* [Phase 005 — System, Application, Data & Synchronization Architecture](005-system-application-data-synchronization-architecture/) — Complete as historical architecture exit.
* [Phase 006 — Implementation Planning, Delivery Slices & Verification Strategy](006-implementation-planning/) — Historical/frozen after 006-D; 006-E through 006-M are superseded as the current execution queue and remain planning lineage.
* [Phase 007 — Jackson Design Refinement & Methodology Closure](007-design-refinement/) — **Complete — formal methodology exit passed**.
* [Phase 008 — Implementation Re-entry, Plan Refresh & Execution Readiness](008-implementation-reentry/) — **In Progress — 008-A complete; 008-B next**.

# Active Phase 008 planning posture

[008-A — Implementation Re-entry Authority, Canonical Baseline, Change Control & Planning Guardrails](008-implementation-reentry/008-A-implementation-reentry-authority-canonical-baseline-change-control-planning-guardrails.md) has established the current implementation-planning authority model.

The current boundary is:

```text
Jackson Concept Design methodology: COMPLETE / EXITED
baseline semantic design: COMPLETE
known baseline semantic blockers: NONE OPEN
Phase 008 subdivision: COMPLETE
implementation planning authority: ESTABLISHED
008-A: COMPLETE
008-B: NEXT / NOT STARTED
protected 006-D baseline: NOT YET QUALIFIED BY PHASE 008
first executable domain slice: NOT YET AUTHORIZED
new domain implementation after 006-D: NOT STARTED
production readiness: NOT ESTABLISHED
```

Phase 008 is not a coding phase. It refreshes the implementation plan against completed semantic design, accepted architecture, the 007-H residual register, and the retained 006-D baseline. The old 006-E–M sequence remains planning lineage rather than automatic execution authority.

008-A establishes that current semantic/governance owners constrain architecture, architecture constrains implementation, and implementation plans/code remain downstream. The Design / Implementation Boundary separately owns whether execution is authorized. Semantic contradictions route through `CHG-*`; implementation inconvenience does not silently weaken upstream meaning.

If the Phase 008 exit passes, 008-L may explicitly authorize a dependency-safe first executable slice and hand off to Phase 009. Until then, new domain implementation remains not started.

# Navigation Guidance

For current meaning, use [Canonical Knowledge](canonical/) and load only task-relevant owners/dependencies. For cross-Concept coordination and temporal/correction questions, load [Synchronizations](canonical/synchronizations/) instead of reconstructing semantics from phase history. For material Judge/Organizer interaction or UI-authority design, load the experience action/authority traceability contract plus only the relevant experience owner(s). For policy exceptions, overrides, waiver-like behavior, acknowledgement/resolution, or operational emergency authority, load [Operational Exception & Override Governance](canonical/policies/operational-exception-governance.md) plus the specific governing policy.

For external representation/publication work, preserve exact source authority through [Export](canonical/concepts/export.md), [Publication](canonical/concepts/publication.md), disclosure, official-outcome, and temporal owners.

For implementation planning, load the current [Design / Implementation Boundary](canonical/governance/design-implementation-boundary.md), [Phase 008 routing](008-implementation-reentry/), task-relevant architecture, and accepted implementation contracts. Use historical Phase 006 only when its rationale or prior dependency reasoning materially helps the current subgroup.

The immediate next task is **008-B — Protected 006-D Baseline Qualification, Drift Audit & Toolchain/Environment Reconciliation**.

Passing Knowledge Validation or Implementation Verification is evidence for the checked revision; neither creates OKF verification metadata, implementation correctness, executable-slice authorization, deployment authority, or production certification.

See [docs/README.md](README.md) for a human-oriented authority summary.

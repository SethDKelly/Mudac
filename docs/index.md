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
* [Policies](canonical/policies/) — current governing/configurable semantics, including Operational Exception & Override Governance.
* [Experience](canonical/experience/) — current Judge/Organizer interaction semantics and authority traceability.
* [Governance](canonical/governance/) — documentation/change/context governance and the current [Design / Implementation Boundary](canonical/governance/design-implementation-boundary.md).
* [Stable Rule Identifiers](canonical/governance/rule-identifiers.md) — durable normative IDs and cross-reference registry.
* [Architecture](canonical/architecture/) — current accepted system/application architecture contracts.
* [Implementation](canonical/implementation/) — accepted implementation/tooling contracts plus the qualified protected 006-D non-domain bootstrap baseline.

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
* [Phase 006 — Implementation Planning, Delivery Slices & Verification Strategy](006-implementation-planning/) — Historical after 006-D; 006-E through 006-M are explicitly mapped/superseded planning lineage.
* [Phase 007 — Jackson Design Refinement & Methodology Closure](007-design-refinement/) — **Complete — formal methodology exit passed**.
* [Phase 008 — Implementation Re-entry, Plan Refresh & Execution Readiness](008-implementation-reentry/) — **In Progress — 008-A/B/C complete; 008-D next**.

# Active Phase 008 planning posture

[008-A](008-implementation-reentry/008-A-implementation-reentry-authority-canonical-baseline-change-control-planning-guardrails.md) established the current implementation-planning authority model.

[008-B](008-implementation-reentry/008-B-protected-006-D-baseline-qualification-drift-audit-toolchain-environment-reconciliation.md) qualified the retained 006-D executable substrate after narrow non-domain drift remediation.

[008-C](008-implementation-reentry/008-C-residual-risk-ingestion-historical-006-mapping-decision-register-supersession-matrix.md) has now closed residual/historical-plan ownership: all accepted Class 2/3 residuals have current Phase 008 owners, Class 4 remains outside the baseline, 008-B evidence limitations are carried forward, and historical 006-E through 006-M is fully superseded as an executable roadmap.

The current boundary is:

```text
Jackson Concept Design methodology: COMPLETE / EXITED
baseline semantic design: COMPLETE
known baseline semantic blockers: NONE OPEN
implementation planning authority: ESTABLISHED
008-A: COMPLETE
008-B: COMPLETE — PASS AFTER NARROW REMEDIATION
protected 006-D baseline: QUALIFIED FOR PHASE 008 PLANNING
008-C: COMPLETE — PASS
historical 006-E–M executable queue: SUPERSEDED / MAPPED
008-D: NEXT / NOT STARTED
first executable domain slice: NOT YET AUTHORIZED
new domain implementation after 006-D: NOT STARTED
production readiness: NOT ESTABLISHED
```

008-D now owns detailed planning for persistence, temporal truth, Versioning, Provenance, governed exceptions, outbox/projection behavior, and migrations. This remains planning only; no domain schema or migration is authorized before 008-L.

# Navigation Guidance

For current meaning, use [Canonical Knowledge](canonical/) and load only task-relevant owners/dependencies. For implementation planning, load the current [Design / Implementation Boundary](canonical/governance/design-implementation-boundary.md), [Phase 008 routing](008-implementation-reentry/), task-relevant architecture, and accepted implementation contracts.

Use historical Phase 006 only when rationale or provenance materially helps. For current historical-plan disposition, use 008-C rather than reconstructing the old deferred queue.

The immediate next task is **008-D — Persistence, Temporal Truth, Versioning, Provenance, Governed Exceptions, Outbox, Projection & Migration Implementation Plan**.

Passing Knowledge Validation, Implementation Verification, or CodeQL is evidence for the checked revision; none creates semantic verification, executable-slice authorization, deployment authority, or production certification.

See [docs/README.md](README.md) for a human-oriented authority summary.

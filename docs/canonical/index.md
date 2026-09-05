# Canonical MUDAC Knowledge

This subtree is the preferred source for current MUDAC product, conceptual UX, documentation-governance, accepted architecture, and accepted implementation meaning.

# Current Knowledge

* [Concepts](concepts/) — accepted MUDAC Concepts.
* [Synchronizations](synchronizations/) — current cross-concept trigger, authority, precondition/postcondition, failure/retry, and temporal/history coordination contracts.
* [Mechanisms](mechanisms/) — derived/supporting subjects that intentionally remain non-Concepts.
* [Policies](policies/) — governing/configurable Competition semantics.
* [Invariants](invariants/) — cross-cutting normative constraints.
* [Experience](experience/) — current conceptual UX contracts.

# Governance, Architecture and Implementation

* [Governance](governance/) — methodology/terminology, documentation authority, agent context, canonical change, metadata/trust/lifecycle, validation/CI, source lineage, stable rule IDs, and the current [Design / Implementation Boundary](governance/design-implementation-boundary.md).
* [Architecture](architecture/) — current accepted system/application architecture contracts. Knowledge topology does not dictate source-code topology.
* [Implementation](implementation/) — accepted implementation/tooling contracts and the frozen 006-D bootstrap substrate. These remain subordinate to the active design-reentry freeze and are not current authority to advance domain implementation.

# Current delivery posture

MUDAC has re-entered deliberate design refinement. Executable work is frozen at the 006-D non-domain bootstrap boundary. Phase 006-E through 006-M are deferred until an explicit later Jackson-methodology exit authorizes implementation to resume.

Current design work proceeds through [Phase 007 — Jackson Design Refinement & Methodology Closure](../007-design-refinement/).

007-B established the current sixteen-Concept catalog. 007-C consolidated cross-concept synchronization authority. 007-D consolidated temporal truth, correction, invalidation, supersession, replacement, affected/stale, official-outcome and Publication-history semantics.

# Retrieval Rule

Load only the specific owner documents and linked dependencies required by the task. For behavior spanning more than one Concept, prefer the relevant [Synchronization](synchronizations/) owner rather than reconstructing coordination from scattered phase history. Use stable rule IDs for normative cross-reference and phase history only when rationale/chronology is needed.

For correction/current-vs-historical/invalidation/official-outcome/Publication-timeline questions, also load [Temporal Truth, Correction & Historical Authority](synchronizations/temporal-truth-correction.md).

Before any code, schema, authentication, API, feature, or application-IaC work, load [Design / Implementation Boundary](governance/design-implementation-boundary.md). While the freeze is active, implementation owners are used only for understanding the retained prototype or performing narrowly permitted maintenance.

Passing repository checks is evidence for a tested revision, not semantic verification, design-methodology closure, implementation-resume authority, or production certification.

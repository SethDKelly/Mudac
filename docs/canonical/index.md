# Canonical MUDAC Knowledge

This subtree is the preferred source for current MUDAC product, conceptual UX, documentation-governance, accepted architecture, and accepted implementation meaning.

# Current Knowledge

* [Concepts](concepts/) — accepted MUDAC Concepts.
* [Mechanisms](mechanisms/) — derived/supporting subjects that intentionally remain non-Concepts.
* [Policies](policies/) — governing/configurable Competition semantics.
* [Invariants](invariants/) — cross-cutting normative constraints.
* [Experience](experience/) — current conceptual UX contracts.

# Governance, Architecture and Implementation

* [Governance](governance/) — methodology/terminology, documentation authority, agent context, canonical change, metadata/trust/lifecycle, validation/CI, source lineage, and stable rule IDs.
* [Architecture](architecture/) — current accepted system/application architecture contracts. Knowledge topology does not dictate source-code topology.
* [Implementation](implementation/) — current implementation owners, including [Implementation Authority, Toolchain & Delivery Governance](implementation/implementation-foundation.md), [Verification Strategy, Evidence & Quality Gates](implementation/verification-strategy.md), [Source Topology, Package Boundaries & Dependency Enforcement](implementation/source-topology.md), and [Runtime, Environment & Delivery Bootstrap](implementation/runtime-delivery-bootstrap.md).

# Retrieval Rule

Load only the specific owner documents and linked dependencies required by the task. Use stable rule IDs for normative cross-reference and phase history only when rationale/chronology is needed.

For implementation work, load the relevant implementation owner(s), the architecture owner(s) they realize, and only materially relevant product/UX/governance constraints. Verification uses the verification owner; source/package work uses the source-topology owner; runtime/environment/CI/IaC/deployment work uses the runtime-delivery owner.

Passing repository checks is evidence for a tested revision, not semantic verification or production certification.

# Canonical MUDAC Knowledge

This subtree is the preferred source for current MUDAC product, conceptual UX, documentation-governance, accepted architecture, and accepted implementation meaning.

# Current Knowledge

* [Concepts](concepts/) - The accepted fifteen Daniel Jackson MUDAC Concepts.
* [Mechanisms](mechanisms/) - Important derived/supporting subjects that intentionally remain non-Concepts.
* [Policies](policies/) - Governing/configurable Competition semantics.
* [Invariants](invariants/) - Cross-cutting normative constraints with stable `INV-*` identifiers.
* [Experience](experience/) - Current conceptual UX contracts.

# Governance, Architecture and Implementation

* [Governance](governance/) - Methodology/terminology, documentation authority (`DOC-*`), agent context (`CTX-*`), canonical change (`CHG-*`), metadata/trust/lifecycle (`META-*`), validation/CI (`VAL-*`), source lineage, and stable rule IDs.
* [Architecture](architecture/) - Current accepted system/application architecture contracts, beginning with the [Architectural Foundation](architecture/architectural-foundation.md) and `ARCH-*` rules. Knowledge topology does not dictate source-code topology.
* [Implementation](implementation/) - Current accepted implementation contracts, including [Implementation Authority, Toolchain & Delivery Governance](implementation/implementation-foundation.md) with `IMPL-*` rules, [Verification Strategy, Evidence & Quality Gates](implementation/verification-strategy.md), and [Source Topology, Package Boundaries & Dependency Enforcement](implementation/source-topology.md). Implementation remains downstream of architecture and may not redefine product meaning.

# Retrieval Rule

For current meaning, start at the relevant category index and open only the specific documents and linked dependencies required by the task.

Repository agents follow [Agent Context & Progressive Retrieval](governance/agent-context.md): progressive disclosure, task-relevant dependencies only, history on demand, and stop context expansion when authority is sufficient.

When a stable rule ID exists, downstream knowledge should link that owner/anchor and state only the local consequence rather than recreating the complete rule body.

For knowledge metadata, [OKF Metadata, Trust, Verification, Lifecycle & Freshness](governance/metadata-trust-lifecycle.md) governs `generated`, `verified`, `status`, `stale_after`, source credibility, trust-tier interpretation, and legacy handling.

For deterministic conformance checks, [Knowledge Validation & CI Enforcement](governance/validation-enforcement.md) governs the validator and CI boundary. Passing validation is not semantic verification.

For rationale or design evolution, follow a canonical document's `sources` links. When starting from a historical/design/implementation phase, enter through that phase's `index.md` and follow current-successor links rather than recursively loading the phase corpus.

For architecture work, load the current architecture owner(s) and only the task-relevant upstream product/UX/governance constraints they depend on.

For implementation work, load the relevant [Implementation](implementation/) owner(s), the architecture owner(s) they realize, and only the product/UX/governance constraints materially required by the task. Verification work additionally uses [Verification Strategy, Evidence & Quality Gates](implementation/verification-strategy.md). Source/package/dependency work additionally uses [Source Topology, Package Boundaries & Dependency Enforcement](implementation/source-topology.md). Evidence and source enforcement should trace existing canonical stable rules rather than create parallel rule bodies.

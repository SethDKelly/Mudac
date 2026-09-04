# Canonical MUDAC Knowledge

This subtree is the preferred source for current MUDAC product, conceptual UX, and documentation-governance meaning.

# Current Knowledge

* [Concepts](concepts/) - The accepted fifteen Daniel Jackson MUDAC Concepts.
* [Mechanisms](mechanisms/) - Important derived/supporting subjects that intentionally remain non-Concepts.
* [Policies](policies/) - Governing/configurable Competition semantics.
* [Invariants](invariants/) - Cross-cutting normative constraints with stable `INV-*` identifiers.
* [Experience](experience/) - Current conceptual UX contracts.

# Governance and Architecture

* [Governance](governance/) - Methodology/terminology, documentation authority (`DOC-*`), agent context (`CTX-*`), canonical change (`CHG-*`), metadata/trust/lifecycle (`META-*`), validation/CI (`VAL-*`), source lineage, and stable rule IDs.
* [Architecture](architecture/) - Accepted system/application architecture contracts when established; this category does not dictate source-code topology.

# Retrieval Rule

For current meaning, start at the relevant category index and open only the specific documents and linked dependencies required by the task.

Repository agents follow [Agent Context & Progressive Retrieval](governance/agent-context.md): progressive disclosure, task-relevant dependencies only, history on demand, and stop context expansion when authority is sufficient.

When a stable rule ID exists, downstream knowledge should link that owner/anchor and state only the local consequence rather than recreating the complete rule body.

For knowledge metadata, [OKF Metadata, Trust, Verification, Lifecycle & Freshness](governance/metadata-trust-lifecycle.md) governs `generated`, `verified`, `status`, `stale_after`, source credibility, trust-tier interpretation, and legacy handling.

For deterministic conformance checks, [Knowledge Validation & CI Enforcement](governance/validation-enforcement.md) governs the validator and CI boundary. Passing validation is not semantic verification.

For rationale or design evolution, follow a canonical document's `sources` links. When starting from a historical phase, enter through that phase's `index.md` and follow current-successor links rather than recursively loading the phase corpus.

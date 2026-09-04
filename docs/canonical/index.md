# Canonical MUDAC Knowledge

This subtree is the preferred source for current MUDAC product and conceptual UX meaning.

004-C established baseline canonical product/UX owners; 004-D established bidirectional historical lineage; 004-E added stable rule IDs/reference-first reuse; 004-F established documentation authority, agent-context, and canonical-change governance; 004-G established the MUDAC OKF metadata/trust/lifecycle profile.

# Current Knowledge

* [Concepts](concepts/) - The accepted fifteen Daniel Jackson MUDAC Concepts.
* [Mechanisms](mechanisms/) - Important derived/supporting subjects that intentionally remain non-Concepts.
* [Policies](policies/) - Governing/configurable Competition semantics.
* [Invariants](invariants/) - Cross-cutting normative constraints with stable `INV-*` identifiers.
* [Experience](experience/) - Current conceptual UX contracts.

# Governance and Architecture

* [Governance](governance/) - Methodology/terminology, documentation authority (`DOC-*`), agent context (`CTX-*`), canonical change governance (`CHG-*`), metadata/trust/lifecycle (`META-*`), source lineage, and stable rule IDs.
* [Architecture](architecture/) - Reserved for accepted system/application architecture beginning after Phase 004.

# Retrieval Rule

For current product/UX meaning, start at the relevant category index and open only the specific documents and linked dependencies required by the task.

Repository agents follow [Agent Context & Progressive Retrieval](governance/agent-context.md): progressive disclosure, task-relevant dependencies only, history on demand, and stop context expansion when authority is sufficient.

When a stable rule ID exists, downstream knowledge should link that owner/anchor and state only the local consequence rather than recreating the complete rule body.

For knowledge metadata, [OKF Metadata, Trust, Verification, Lifecycle & Freshness](governance/metadata-trust-lifecycle.md) governs `generated`, `verified`, `status`, `stale_after`, source credibility, trust-tier interpretation, and legacy handling.

For rationale or design evolution, follow a canonical document's `sources` links. When starting from a historical phase, enter through that phase's `index.md` and follow current-successor links rather than recursively loading the phase corpus.

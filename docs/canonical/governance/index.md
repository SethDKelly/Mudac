# Governance

Current repository/design-governance knowledge for MUDAC.

# Methodology and authority

* [Methodology, OKF Adoption & Terminology](methodology-terminology.md) - Concept Design versus OKF authority, adopted terminology, provenance distinction, and knowledge/source-code topology boundary.
* [Documentation Authority & Canonical Ownership](documentation-authority.md) - `DOC-*` rules for current-owner precedence, one-owner discipline, downstream constraints, historical preservation, and routing-artifact boundaries.

# Retrieval and change governance

* [Agent Context & Progressive Retrieval](agent-context.md) - `CTX-*` rules for minimum-sufficient context, progressive disclosure, historical retrieval, and anti-bloat behavior.
* [Canonical Change & Conflict Governance](change-governance.md) - `CHG-*` rules for semantic changes, stable-rule impact review, contradiction handling, and implementation/design mismatch.

# Lineage and reference governance

* [Source Lineage and Historical Design Records](source-lineage.md) - Backward `sources` provenance, forward phase-to-canonical lineage, historical preservation, and material-source selection.
* [Stable Rule Identifiers & Cross-Reference Contract](rule-identifiers.md) - Durable rule IDs, explicit anchors, reference-first reuse, bounded restatement, and the rule registry.

# Agent adapter

Repository agents receive a concise bootstrap through [`AGENTS.md`](../../../AGENTS.md). That adapter routes to these canonical governance owners and is not an independent authority layer.

# Pending governance work

004-G will finalize OKF generation/verification/trust, knowledge lifecycle/status, and freshness conventions. 004-H will add structural validation/CI enforcement. Until then, the governance owners above define repository authority, retrieval, and change behavior.
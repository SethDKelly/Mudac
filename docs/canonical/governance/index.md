# Governance

Current repository/design-governance knowledge for MUDAC.

# Methodology and authority

* [Methodology, OKF Adoption & Terminology](methodology-terminology.md) - Concept Design versus OKF authority, adopted terminology, provenance distinction, and knowledge/source-code topology boundary.
* [Documentation Authority & Canonical Ownership](documentation-authority.md) - `DOC-*` rules for current-owner precedence, one-owner discipline, downstream constraints, historical preservation, and routing-artifact boundaries.
* [Design / Implementation Boundary](design-implementation-boundary.md) - current post-Concept-Design posture, implementation-planning authority, protected 006-D non-domain baseline, required Phase 008 plan refresh, and the boundary before new domain implementation begins.

# Retrieval and change governance

* [Agent Context & Progressive Retrieval](agent-context.md) - `CTX-*` rules for minimum-sufficient context, progressive disclosure, historical retrieval, and anti-bloat behavior.
* [Canonical Change & Conflict Governance](change-governance.md) - `CHG-*` rules for semantic changes, stable-rule impact review, contradiction handling, and implementation/design mismatch.

# Lineage, metadata, validation and reference governance

* [Source Lineage and Historical Design Records](source-lineage.md) - Backward `sources` provenance, forward phase-to-canonical lineage, historical preservation, and material-source selection.
* [OKF Metadata, Trust, Verification, Lifecycle & Freshness](metadata-trust-lifecycle.md) - `META-*` rules for frontmatter profile, generation attribution, real verification, lifecycle status, freshness, trust-tier boundaries, and legacy metadata handling.
* [Knowledge Validation & CI Enforcement](validation-enforcement.md) - `VAL-*` rules for deterministic structural validation, stable-ID/link checks, routing requirements, legacy exemptions, and read-only CI enforcement.
* [Stable Rule Identifiers & Cross-Reference Contract](rule-identifiers.md) - Durable rule IDs, explicit anchors, reference-first reuse, bounded restatement, and the rule registry.

# Current methodology posture

The renewed Jackson Concept Design methodology formally exited for the current MUDAC baseline in [007-I](../../007-design-refinement/007-I-formal-jackson-concept-design-methodology-exit-accepted-residual-uncertainty-implementation-resume-boundary-decision.md).

Implementation planning is ready to resume, but new domain implementation remains not started pending Phase 008 plan refresh and explicit first-slice authorization. The exact current boundary is owned by [Design / Implementation Boundary](design-implementation-boundary.md).

# Agent adapter

Repository agents receive a concise bootstrap through [`AGENTS.md`](../../../AGENTS.md). That adapter routes to these canonical governance owners and is not an independent authority layer.

The numbered [Phase 004 history](../../004-knowledge-architecture/) preserves the rationale, rollout, strict audit, and migration-closure record for the documentation-governance system. [Phase 007](../../007-design-refinement/) preserves the later design re-entry, revalidation, and formal methodology-exit record.
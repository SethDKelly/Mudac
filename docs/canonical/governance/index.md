# Governance

Current repository/design-governance knowledge for MUDAC.

# Methodology and authority

* [Methodology, OKF Adoption & Terminology](methodology-terminology.md) — relationship among Daniel Jackson Concept Design, the Base completion-control lifecycle, OKF v0.2, MUDAC terminology and downstream realization layers.
* [Documentation Authority & Canonical Ownership](documentation-authority.md) — `DOC-*` rules for current-owner precedence, one-owner discipline, downstream constraints, historical preservation and routing-artifact boundaries.
* [Design / Implementation Boundary](design-implementation-boundary.md) — current reopened Concept Design posture, frozen 006-D bootstrap, suspended downstream authority, and design-only execution boundary.
* [Downstream Architecture & Implementation Authority Quarantine](downstream-authority-quarantine.md) — prevents architecture/implementation work produced before methodology completion from constraining reopened Concept Design.

# Retrieval and change governance

* [Agent Context & Progressive Retrieval](agent-context.md) — `CTX-*` rules for minimum-sufficient context, progressive disclosure, historical retrieval and anti-bloat behavior.
* [Canonical Change & Conflict Governance](change-governance.md) — `CHG-*` rules for semantic changes, stable-rule impact review, contradiction handling and downstream/design mismatch.

# Lineage, metadata, validation and reference governance

* [Source Lineage and Historical Design Records](source-lineage.md) — backward `sources` provenance, forward phase-to-canonical lineage, historical preservation and material-source selection.
* [OKF Metadata, Trust, Verification, Lifecycle & Freshness](metadata-trust-lifecycle.md) — `META-*` rules for frontmatter profile, attribution, verification, lifecycle status, freshness and trust-tier boundaries.
* [Knowledge Validation & CI Enforcement](validation-enforcement.md) — `VAL-*` rules for deterministic structural validation, stable-ID/link checks, routing requirements and read-only CI enforcement.
* [Stable Rule Identifiers & Cross-Reference Contract](rule-identifiers.md) — durable rule IDs, explicit anchors, reference-first reuse and the rule registry.

# Current methodology posture

Phase 009 formally reopened and realigned Jackson Concept Design after determining that the earlier 007-I closure was premature.

Current state:

```text
Jackson Concept Design: REOPENED / NOT COMPLETE
009 realignment/gap map: COMPLETE
010 foundational completion: NEXT
architecture: SUSPENDED PENDING DESIGN CLOSURE
implementation planning: SUSPENDED
new domain implementation: NOT STARTED
implementation readiness: NOT READY
implementation authorization: NOT YET
```

The exact current boundary is owned by [Design / Implementation Boundary](design-implementation-boundary.md). Phase 009 history is at [Jackson Methodology Completion Realignment & Design Re-entry](../../009-jackson-methodology-realignment/).

# Agent adapter

Repository agents receive a concise bootstrap through [`AGENTS.md`](../../../AGENTS.md). That adapter routes to these canonical governance owners and is not an independent authority layer.

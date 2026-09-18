# Governance

Current repository/design-governance knowledge for MUDAC.

## Methodology and authority

* [Methodology, OKF Adoption & Terminology](methodology-terminology.md)
* [Documentation Authority & Canonical Ownership](documentation-authority.md)
* [Design / Implementation Boundary](design-implementation-boundary.md) — current reopened-design boundary; Phase 014 active and downstream authority still suspended.
* [Downstream Architecture & Implementation Authority Quarantine](downstream-authority-quarantine.md)

## Retrieval and change governance

* [Agent Context & Progressive Retrieval](agent-context.md)
* [Canonical Change & Conflict Governance](change-governance.md)

## Lineage, metadata and validation

* [Source Lineage and Historical Design Records](source-lineage.md)
* [OKF Metadata, Trust, Verification, Lifecycle & Freshness](metadata-trust-lifecycle.md)
* [Knowledge Validation & CI Enforcement](validation-enforcement.md)
* [Stable Rule Identifiers & Cross-Reference Contract](rule-identifiers.md)

## Current methodology posture

```text
Jackson Concept Design: IN PROGRESS
009: COMPLETE — PASS
010: COMPLETE — PASS
011: COMPLETE — PASS
012: COMPLETE — PASS
013: COMPLETE — PASS
014: IN PROGRESS
014-A: COMPLETE — READY
014-B: NEXT
architecture: SUSPENDED PENDING DESIGN CLOSURE
implementation planning: SUSPENDED
new domain implementation: NOT STARTED
implementation readiness: NOT READY
implementation authorization: NOT YET
```

## Current authority

[Canonical Concepts](../concepts/) owns the eighteen-Concept catalog.

[Canonical Synchronizations](../synchronizations/) owns application composition/action authority.

[Canonical Dependence](../dependence/) owns inclusion dependence and PF-01 product-family scope.

[Final Phase 013 Mapping Authority Baseline](../experience/mapping-authority-baseline.md) plus natural Experience owners own current user-visible mapping semantics.

[Phase 014](../../014-familiarity-reuse-genericity/) now owns the current familiarity/reuse/genericity audit records only; adopted semantic changes still belong to their natural canonical owners.

## Phase-014 governance rule

```text
familiar precedent = comparison evidence
                    != automatic design authority

implementation convention = contamination probe / evidence only
                          != conceptual reuse authority
```

014-A requires explicit semantic comparison and explicit reopen routing when a familiarity/generalization proposal exposes a real upstream defect.

The phase must not create duplicate catalog specifications beside current Concept owners.

## Design / implementation boundary

Architecture and implementation remain quarantined through the remaining Concept Design runway. Phase 014 may study conceptual reuse but may not select code, framework, service, UI-component, storage or runtime reuse.

## Current handoff

Proceed to **014-B — Familiarity Evidence Baseline, Precedent Taxonomy & Comparison Register**.

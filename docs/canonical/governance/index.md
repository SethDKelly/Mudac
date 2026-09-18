# Governance

Current repository/design-governance knowledge for MUDAC.

## Methodology and authority

* [Methodology, OKF Adoption & Terminology](methodology-terminology.md)
* [Documentation Authority & Canonical Ownership](documentation-authority.md)
* [Design / Implementation Boundary](design-implementation-boundary.md)
* [Downstream Architecture & Implementation Authority Quarantine](downstream-authority-quarantine.md)

## Retrieval and change governance

* [Agent Context & Progressive Retrieval](agent-context.md)
* [Canonical Change & Conflict Governance](change-governance.md)

## Product-language authority

Cross-catalog product vocabulary is owned by [MUDAC Domain Vocabulary & Expectation-Transfer Rules](../project/domain-vocabulary-expectation-transfer.md).

Methodology terminology and product/domain terminology remain separate authority layers.

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
014-B: COMPLETE — PASS
014-C: COMPLETE — PASS
014-D: COMPLETE — PASS
014-E: COMPLETE — PASS
014-F: COMPLETE — PASS
014-G: NEXT
architecture: SUSPENDED PENDING DESIGN CLOSURE
implementation planning: SUSPENDED
new domain implementation: NOT STARTED
implementation readiness: NOT READY
implementation authorization: NOT YET
```

## Current authority

Canonical Concepts own the eighteen-Concept catalog; Synchronizations own composition/application actions; Dependence owns PF-01 inclusion/scope; completed Phase 013 owns mapping semantics.

Phase 014 owns familiarity/reuse/genericity analysis only. 014-B established the evidence hierarchy; 014-C through 014-E completed the three Concept-family familiarity audits; 014-F reconciled cross-catalog terminology and expectation transfer.

No familiarity or terminology finding may overwrite canonical semantics merely because a precedent or word is familiar or widespread.

## Completed terminology governance

All eighteen Concept names/boundaries remain current.

Terminology classes are:

```text
T1 canonical semantic term
T2 qualified explanatory label
T3 analogy-only term
T4 high-risk generic term
```

Preserve especially:

```text
Identity != Participation != Access
Evaluation Occurrence != Evaluation Obligation != Scorecard
Rubric != exact authoritative Evaluation Basis
Versioning != Provenance
Rank / selection basis != Award recognition
Competition Finalized != Outcome Declaration
Outcome Declaration != Export != Publication != delivery
```

Generic wording may not create or bypass semantic authority. `Role`, `Task`, `Submission`, `Revision`, `Result`, `Status`, `Share`, `Resolve`, `Override` and similar familiar terms must remain subordinate to natural owners.

014-C routed and repaired one genuine Phase-011 composition defect. 014-D through 014-F found no additional upstream defect requiring reopen.

## Design / implementation boundary

Architecture and implementation remain quarantined through the remaining Concept Design runway. Conceptual reuse/genericity must never be inferred from shared libraries, schemas, storage models, workflow engines, authorization frameworks, revision systems, report generators or publishing infrastructure.

## Current handoff

Proceed to **014-G — Broader Genericity, Parameterization, Duplication & Specialization-Pressure Audit**.

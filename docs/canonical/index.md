# Canonical MUDAC Knowledge

This subtree is the preferred source for current MUDAC conceptual product meaning and governance. Architecture and implementation remain **suspended downstream candidates** while Jackson Concept Design continues.

# Current conceptual knowledge

* [Project Context, Purpose & Vocabulary](project/)
* [Concepts](concepts/)
* [Synchronizations](synchronizations/)
* [Dependence](dependence/)
* [Mechanisms](mechanisms/)
* [Policies](policies/)
* [Invariants](invariants/)
* [Experience](experience/)
* [Governance](governance/)

# Current methodology posture

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
014-G: COMPLETE — PASS
014-H: NEXT
architecture authority: SUSPENDED
implementation-planning authority: SUSPENDED
new domain implementation: NOT STARTED
implementation readiness: NOT READY
implementation authorization: NOT YET
```

# Phase-014 comparison authority

Current canonical knowledge remains the semantic target. Familiar precedents remain comparison evidence only.

014-C through 014-E retain all eighteen current Concept names/boundaries. 014-F establishes the durable [MUDAC Domain Vocabulary & Expectation-Transfer Rules](project/domain-vocabulary-expectation-transfer.md).

014-G establishes the broader-genericity contract:

```text
Generic at the boundary; specific in purpose.
shared parameter != shared purpose
shared fields != shared lifecycle
shared history shape != shared authority
```

The 010-G abstract parameterization remains sufficient for almost all Concepts. One safe broader refinement removes `student` from Team's intrinsic semantics while PF-01 continues to bind Team to student teams.

No generic `Group`, `Scoped Relationship`, `Occurrence`, `Task`, `Result`, `Historical Record` or merged representation/release super-Concept is current authority.

## Cross-family seams retained

```text
Identity != Participation != Access
Panel membership != occurrence participation != responsibility != evidence
Evaluation Occurrence != Evaluation Obligation != Scorecard
Rubric definition != exact authoritative Evaluation Basis
Scorecard Draft != authoritative judgment
Versioning != Provenance
Rank / selection basis != Award recognition
Competition Finalized != Outcome Declaration
Outcome Declaration != Export != Publication != delivery
Export currency != Publication state
```

## Retrieval rule

1. start at the natural canonical owner for current meaning;
2. use [Domain Vocabulary & Expectation-Transfer Rules](project/domain-vocabulary-expectation-transfer.md) when familiar wording could cross owner boundaries;
3. use completed Phase-013 mapping for user-visible semantics;
4. for Phase-014 work, load 014-A/014-B plus relevant completed 014-C through 014-G records;
5. treat reusable-pattern hypotheses as Phase-014 evidence, not new Concepts, until 014-H disposition;
6. use historical adapters only as explicit comparison/counterexample evidence;
7. do not preload architecture/implementation except for contamination/history analysis.

# Next

Proceed to **014-H — Retained Novelty, Reusable Concept-Knowledge & Catalog-Candidate Audit**.

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
014-G: NEXT
architecture authority: SUSPENDED
implementation-planning authority: SUSPENDED
new domain implementation: NOT STARTED
implementation readiness: NOT READY
implementation authorization: NOT YET
```

# Phase-014 comparison authority

Current canonical knowledge remains the semantic target. Familiar precedents remain comparison evidence only.

014-C through 014-E retain all eighteen current Concept names/boundaries. 014-F establishes the durable [MUDAC Domain Vocabulary & Expectation-Transfer Rules](project/domain-vocabulary-expectation-transfer.md).

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

## Terminology discipline

```text
T1 canonical semantic term
T2 qualified explanatory label
T3 analogy-only term
T4 high-risk generic term
```

Familiar words such as `role`, `task`, `session`, `submit`, `final`, `winner`, `revision`, `share`, `status`, `current`, `complete` or `published` must not imply stronger or different semantics than their natural owner.

Owner-qualified state/action language is preferred whenever ambiguity could change behavior or authority.

Historical `Judging Encounter` and `Official Outcome Revision` remain counterexample evidence only.

# Retrieval rule

1. start at the natural canonical owner for current meaning;
2. use [Domain Vocabulary & Expectation-Transfer Rules](project/domain-vocabulary-expectation-transfer.md) when familiar wording could cross owner boundaries;
3. use completed Phase-013 mapping for user-visible semantics;
4. for Phase-014 work, load 014-A/014-B plus relevant completed 014-C through 014-F records;
5. use historical adapters only as explicit comparison/counterexample evidence;
6. do not preload architecture/implementation except for contamination/history analysis.

# Next

Proceed to **014-G — Broader Genericity, Parameterization, Duplication & Specialization-Pressure Audit**.

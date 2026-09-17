---
type: Derived Mechanism
title: Readiness
description: Derived projections indicating whether a consequential operation may legitimately proceed, including Ranking and Finalization Readiness used by current Phase 011-G outcome composition.
status: stable
tags: [mechanism, readiness, lifecycle]
sources:
  - resource: ../../002-concept-specification/002-I-phase-consolidation-specification-exit-review.md
  - resource: ../../003-conceptual-ux-architecture/003-D-organizer-competition-setup-configuration-readiness-experience.md
  - resource: ../../003-conceptual-ux-architecture/003-F-reconciliation-coverage-ranking-awards-finalization-experience.md
  - resource: ../../011-concept-composition-synchronization/011-G-coverage-aggregate-rank-award-competition-finalization-outcome-declaration-composition.md
  - resource: ../../013-concept-mapping-interaction-semantics-user-visible-representation/013-G-live-operations-remaining-work-exception-reconciliation-derived-outcome-state-mapping.md
  - resource: ../synchronizations/evaluation-outcome-finalization-declaration.md
---

# Canonical contract

Readiness is derived from authoritative source state and policy; it is not an editable checklist flag and cannot itself write lifecycle, evidence, Award or declaration authority.

MUDAC uses distinct readiness projections, including Competition Readiness, Judge Readiness, **Ranking Readiness**, and **Finalization Readiness**. Each answers whether a specific next operation may legitimately proceed.

Blocking conditions differ from warnings. A warning may persist while a subject is Ready when policy permits proceeding. Acknowledging, hiding or dismissing a blocker does not repair its source condition.

If source conditions change, readiness recomputes.

# Ranking Readiness

Ranking Readiness is distinct from the existence of a calculated Rank.

For a Division/result scope it normally requires, as applicable:

- current Team/Division eligibility is resolved;
- qualifying evidence selection is reconstructible;
- each Team intended for official ranking has factual Coverage `Satisfied` or an explicit governed exception whose scope permits ranking despite preserved `Incomplete` Coverage;
- applicable Evaluation Basis/Rubric compatibility is resolved;
- current Aggregate/policy basis is available;
- no unresolved invalidation/replacement/successor-work or material correction condition is expected to change the ranking basis;
- declared tie semantics have been applied without hidden/manual override.

A numerical Rank may therefore exist while Ranking Readiness is false.

Current rank-derived Award composition requires a **Ranking Ready** basis; provisional/calculated ordering alone cannot authorize rank-derived recognition.

# Finalization Readiness

Finalization Readiness is distinct from Competition lifecycle state and Outcome Declaration authority.

It derives whether the applicable current evidence, Coverage plus separate exception dispositions, Ranking Readiness, Evaluation Policy, required Award decisions, correction/reconciliation conditions, and reconstructible accepted OutcomeBasis are sufficiently resolved for the coordinated `Finalize Competition & Declare Outcome` application action.

Finalization Readiness becoming true does not itself Finalize Competition or declare an outcome.

# Mapping rule

Phase 013-G maps Ranking/Finalization Readiness as non-editable source-derived explanations.

```text
readiness true
  != lifecycle transition
  != Award authority
  != Outcome Declaration authority
```

When readiness is false, remediation targets the natural source or an explicitly permitted governed exception. No generic `Set Ready` or checklist-completion action exists.

See [Evaluation Outcome, Award, Finalization & Declaration Composition](../synchronizations/evaluation-outcome-finalization-declaration.md), [Organizer Preparation](../experience/organizer-preparation.md), and [Reconciliation & Derived Outcome-State Mapping](../experience/reconciliation-derived-state.md).

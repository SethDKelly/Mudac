# Derived and Supporting Mechanisms

Current MUDAC subjects modeled as derived/supporting mechanisms or processes rather than independent Concepts.

* [Team Attributes](team-attributes.md) — disclosure-controlled descriptive Team metadata, including optional Team Name.
* [Criterion & Notes](criterion-notes.md) — Rubric/Scorecard subordinate evaluation structure.
* [Panel Membership & Composition](panel-membership-composition.md) — current Panel relational/composition support semantics.
* [Readiness](readiness.md) — derived permission-to-proceed projections, including Competition, Judge, Ranking and Finalization Readiness.
* [Coverage](coverage.md) — derived factual sufficiency of qualifying evaluation evidence; exception disposition is separate.
* [Aggregate](aggregate.md) — numerical combination of eligible authoritative individual judgments.
* [Rank](rank.md) — derived ordering under declared comparison policy.
* [Reconciliation](reconciliation.md) — Organizer process/work mode for resolving outcome-affecting conditions.

## Deprecated classification adapter

[Official Outcome Revision](official-outcome-revision.md) is retained only as a deprecated historical adapter. Current official authority is owned by [Outcome Declaration](../concepts/outcome-declaration.md).

## Current classification rules

- Coverage remains `Satisfied | Incomplete`; governed exception does not rewrite factual sufficiency.
- Aggregate is derived numerical state and does not establish Coverage/rank eligibility.
- Rank is derived/non-editable.
- Readiness is derived; `Ready to Judge`, Competition Readiness, Ranking Readiness and Finalization Readiness never become independent writable authority.
- Reconciliation remains process/work context rather than ticket/workflow authority.
- Recovery/Continuity remains a cross-cutting purpose obligation.
- Export owns representation currency; Publication owns release state; transport/delivery remains downstream realization.

## Composition and scope

Phase 011 is **COMPLETE — PASS** and [Canonical Synchronizations](../synchronizations/) owns composition.

Phase 012 is **COMPLETE — PASS** and [MUDAC Product-Family Scope](../dependence/product-family-scope.md) owns PF-01 scope.

## Phase-013 mapping boundary

Phase 013 is **IN PROGRESS**.

Mappings preserve source-versus-derived direction:

```text
source facts
  → derived readiness / operational explanation

eligible authoritative evidence
  → Coverage / Aggregate
  → rank eligibility / Rank
```

Derived state must never appear as an independently editable source of truth.

013-E establishes that active Judge work is upstream of downstream evidence mechanisms:

```text
Outstanding obligation
  → Scorecard Draft
  → explicit Finalize Evaluation
  → authoritative qualifying evidence
  → later Coverage/Aggregate eligibility evaluation
```

Therefore:

```text
Draft score/total != Aggregate input
Occurrence completion != Coverage satisfaction
Obligation Outstanding != zero evidence
Finalized Scorecard existence != automatic current evidence eligibility forever
```

Current evidence eligibility after correction/invalidation is mapped further in 013-F/G; historical satisfaction remains distinct from current eligibility.

See [Phase 013 Mapping Authority Baseline](../experience/mapping-authority-baseline.md) and [Judge Active Evaluation Mapping](../experience/judge-evaluation.md).

```text
Phase 010 COMPLETE — PASS
Phase 011 COMPLETE — PASS
Phase 012 COMPLETE — PASS
Phase 013 IN PROGRESS
013-A COMPLETE — READY
013-B COMPLETE — PASS
013-C COMPLETE — PASS
013-D COMPLETE — PASS
013-E COMPLETE — PASS
013-F NEXT
```
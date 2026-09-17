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

Mappings must preserve source-versus-derived direction:

```text
source facts
  → derived readiness / operational explanation

eligible authoritative evidence
  → Coverage / Aggregate
  → rank eligibility / Rank
```

Derived state must never appear as an independently editable source of truth.

013-C establishes:

```text
Ready to Judge
  = derived explanation over current Identity / Participation /
    relevant preparation/lifecycle/context facts
  != Participation state
  != Panel membership
  != Evaluation Obligation
  != Access grant
```

013-D establishes:

```text
Competition Readiness
  = derived permission-to-mark-ready projection over current preparation sources
  != Competition lifecycle Ready
  != editable checklist state

readiness satisfied
  → may make Mark Competition Ready available
  != automatic lifecycle transition

blocking source change while Competition Ready
  → readiness recomputes blocking
  → current composition returns Competition to Draft
```

A readiness blocker is remediated through its natural source or an explicitly permitted governed exception, not by acknowledging or editing the readiness projection.

See [Phase 013 Mapping Authority Baseline](../experience/mapping-authority-baseline.md), [Judge Entry, Participation & Readiness Mapping](../experience/judge-onboarding.md), and [Organizer Competition Preparation & Readiness Mapping](../experience/organizer-preparation.md).

```text
Phase 010 COMPLETE — PASS
Phase 011 COMPLETE — PASS
Phase 012 COMPLETE — PASS
Phase 013 IN PROGRESS
013-A COMPLETE — READY
013-B COMPLETE — PASS
013-C COMPLETE — PASS
013-D COMPLETE — PASS
013-E NEXT
```

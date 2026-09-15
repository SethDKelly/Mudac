# MUDAC Repository Agent Rules

This file is a bootstrap adapter. Current authority lives under [`docs/`](docs/), especially canonical conceptual/governance owners and the active methodology phase.

## Required start

1. Start at [`docs/index.md`](docs/index.md).
2. Read [`Design / Implementation Boundary`](docs/canonical/governance/design-implementation-boundary.md).
3. Read [`Downstream Architecture & Implementation Authority Quarantine`](docs/canonical/governance/downstream-authority-quarantine.md).
4. Read [Canonical Project Context & Purpose](docs/canonical/project/), [Current Concepts](docs/canonical/concepts/), [Current Synchronizations](docs/canonical/synchronizations/) and [Current Dependence](docs/canonical/dependence/).
5. Use [012-A](docs/012-concept-dependence-product-family-subset-scope/012-A-dependence-scope-subset-semantics-product-family-questions-subphase-planning.md) for Phase 012 semantics and the approved A→K sequence.
6. Use [012-B](docs/012-concept-dependence-product-family-subset-scope/012-B-application-family-boundary-concept-inclusion-roles-candidate-dependence-inventory.md) only as candidate/provisional dependence evidence.
7. Use [012-C](docs/012-concept-dependence-product-family-subset-scope/012-C-competition-actor-competitor-context-bias-control-dependence.md) and [MUDAC Application-Family Concept Dependence](docs/canonical/dependence/application-family-dependence.md) for current accepted Competition/actor/competitor/bias-control dependence.
8. Use canonical synchronization owners for current interaction rules; dependence never replaces composition.
9. Load older phase records only when rationale, alternatives, chronology or evidence materially help the current methodology question.

## Current methodology posture

```text
Jackson Concept Design: REOPENED / IN PROGRESS
007-I previous closure: SUPERSEDED AS CURRENT CLOSURE AUTHORITY
008 implementation re-entry: HALTED AFTER 008-E
architecture authority: SUSPENDED
implementation-planning authority: SUSPENDED
006-D bootstrap: FROZEN HISTORICAL NON-DOMAIN SUBSTRATE
new domain implementation: NOT STARTED
implementation readiness: NOT READY
implementation authorization: NOT YET
009: COMPLETE — PASS
010: COMPLETE — PASS
011: COMPLETE — PASS
012: IN PROGRESS
012-A: COMPLETE — READY
012-B: COMPLETE — PASS
012-C: COMPLETE — PASS
012-D: NEXT
```

## Current Concept authority

The canonical catalog contains eighteen Concepts:

Competition, Division, Team, Panel, Evaluation Occurrence, Evaluation Obligation, Rubric, Scorecard, Award, Identity, Participation, Alias, Access, Versioning, Provenance, Outcome Declaration, Export, and Publication.

`Judging Encounter` and `Official Outcome Revision` remain deprecated historical adapters.

Coverage, Aggregate, Rank and Readiness remain derived mechanisms. Reconciliation remains process/work context. Recovery/Continuity remains a cross-cutting purpose obligation.

## Current composition authority

Phase 011 is complete. Preserve these distinctions:

- Identity continuity ≠ Participation authority ≠ Access permission;
- Panel membership ≠ occurrence participation ≠ Evaluation Obligation responsibility ≠ Scorecard evidence;
- Scorecard Draft ≠ authority;
- Versioning ≠ semantic authorship;
- Provenance ≠ domain authority;
- historical satisfaction ≠ current evidence eligibility;
- missing evidence is never zero;
- Coverage factual sufficiency ≠ exception disposition;
- Aggregate existence ≠ rank eligibility;
- Rank ≠ Award authority;
- Competition Finalization ≠ Outcome Declaration;
- calculated ≠ official ≠ public ≠ delivered;
- source authority ≠ Export representation ≠ Publication release ≠ transport delivery.

Governing automation rule:

> **Automation may propagate knowledge/currentness and execute already-authorized bounded composition consequences; automation may not manufacture semantic authority.**

## Dependence semantics

Phase 012 owns **extrinsic inclusion dependence**, coherent Concept subsets, product/application-family variants and adopted scope.

```text
intrinsic Concept dependence
  = upstream Concept-boundary defect

synchronization/composition
  = how already-included Concepts interact

extrinsic inclusion dependence
  = contextual rule that including A requires B
    for A's intended MUDAC application role

implementation dependency
  = out of scope
```

Do not derive dependence from synchronization, code imports, schemas, service calls, UI layout, deployment topology or ordinary workflow.

## Current accepted dependence through 012-C

Direct edges:

```text
Team          → Competition
Participation → Competition
Participation → Identity
Division      → Team
Alias         → Team
Panel         → Participation
```

Transitive consequences:

```text
Division → Team → Competition
Alias    → Team → Competition
Panel    → Participation → Competition
Panel    → Participation → Identity
```

Do not duplicate transitive reachability as direct edges without a distinct role rationale.

Current explicit universal non-edges:

```text
Competition ↛ Division
Competition ↛ Panel
Team        ↛ Alias
Identity    ↛ Competition
Identity    ↛ Participation
Access      ↛ Participation
Access      ↛ Identity
```

The Access non-edges do not weaken protected-operation composition: Judge/Organizer protected actions still require legitimate Participation context and Access evaluation.

## Current capability/scope rules

- every in-scope MUDAC application variant retains Competition as the family context;
- blinded-judging variants include Alias;
- multi-cohort variants include Division;
- reusable evaluator-grouping variants include Panel;
- ad-hoc evaluator assignment may omit Panel;
- single-cohort operation may omit Division at the dependence level;
- current anonymity/disclosure policy would require later revalidation before a no-Division blinded variant can be adopted.

Do not turn these capability rules into false universal edges.

## Canonical dependence authority

[`docs/canonical/dependence/application-family-dependence.md`](docs/canonical/dependence/application-family-dependence.md) is current dependence authority.

It is explicitly **partial through 012-C**. Do not infer that unresolved 012-D through 012-G candidates are non-edges because they are absent.

012-B remains candidate evidence only.

## Approved Phase 012 order

```text
012-A  scope / semantics / questions / plan                            COMPLETE — READY
012-B  application-family roles / candidate inventory                  COMPLETE — PASS
012-C  Competition / actor / competitor / bias-control dependence      COMPLETE — PASS
012-D  evaluation structure / responsibility / basis / judgment         NEXT
012-E  authority lineage / Provenance / correctability                  PLANNED
012-F  outcome / Award / official-authority dependence                  PLANNED
012-G  Export / Publication / external-representation dependence        PLANNED
012-H  whole graph / transitivity / co-inclusion / minimal subsets      PLANNED
012-I  product-family variants / scope / composition revalidation       PLANNED
012-J  counterexamples / upstream reopen / Phase 013 handoff audit      PLANNED
012-K  canonical reconciliation / Phase 012 exit / Phase 013 handoff    PLANNED
```

## 012-D discipline

012-D owns Evaluation Occurrence, Evaluation Obligation, Rubric and Scorecard dependence.

Use current transitivity rather than redundantly adding context edges. For example, an accepted future `Evaluation Occurrence → Participation` already implies Identity + Competition; `Evaluation Occurrence → Team` already implies Competition.

Do not make Panel mandatory merely because the ordinary occurrence path can begin from Panel candidates.

## Reopening rules

- unjustified purpose/scope role → revisit the natural Phase 010 project/purpose owner;
- intrinsic Concept coupling → reopen the natural Phase 010 Concept owner;
- accepted subset exposes missing composition → reopen/refine the natural Phase 011 synchronization owner;
- derived mechanism appears to require Concept status → review upstream classification first;
- user-visible mapping issue without inclusion change → carry to Phase 013.

## Design-only rules for Phases 012–017

- Do not resume 008-F through 008-L.
- Do not begin new domain implementation.
- Do not infer Concept dependence from source/package/service/database dependency.
- Do not turn the dependence graph into implementation architecture, source order, API direction, persistence ownership or deployment sequence.
- Do not design commercial tiers from Concept subsets.
- Keep accepted current meaning in canonical owners and rejected/counterexample reasoning in numbered phase history.

## Frozen executable substrate

The real 006-D bootstrap remains in the repository. Narrow dependency/security/build maintenance is permitted only when necessary to keep the repository safe/buildable and only if it adds no MUDAC domain semantics or constrains reopened design.

## Knowledge validation

Knowledge-only changes should run repository knowledge validation. Passing CI validates the tested revision; it does not prove methodology completion or authorize downstream work.

## Current next task

Proceed to:

> **012-D — Evaluation Structure, Responsibility, Basis & Judgment Dependence**

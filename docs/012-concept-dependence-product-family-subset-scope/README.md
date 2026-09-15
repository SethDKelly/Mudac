# Phase 012 — Concept Dependence, Product-Family, Subset & Scope Analysis

Status: **IN PROGRESS — 012-A through 012-F complete; 012-G next.**

## Role in the completion runway

Phase 012 corresponds to Base Phase 006 / Daniel Jackson Concept dependence and subset analysis.

Phase 010 established the current eighteen independent Concepts. Phase 011 established how included Concepts interact. Phase 012 asks which Concepts must, may, conditionally, or alternatively be co-included for coherent MUDAC application roles; which subsets are coherent; and which coherent variants are actually in scope.

Architecture and implementation remain suspended.

## Governing distinction

```text
intrinsic Concept dependence
  = upstream Concept-boundary defect

synchronization / composition
  = how already-included Concepts interact

extrinsic inclusion dependence
  = contextual rule that including A requires B
    for A's intended MUDAC application role

capability-conditioned co-inclusion
  = a named application capability requires a Concept set
    without making every underlying Concept universally depend on that set

implementation dependency
  = out of scope
```

## Current subgroup sequence

| Group | Topic | Status |
| --- | --- | --- |
| 012-A | [Dependence Scope, Subset Semantics, Product-Family Questions & Subphase Planning](012-A-dependence-scope-subset-semantics-product-family-questions-subphase-planning.md) | **Complete — READY** |
| 012-B | [Application-Family Boundary, Concept Inclusion Roles & Candidate Dependence Inventory](012-B-application-family-boundary-concept-inclusion-roles-candidate-dependence-inventory.md) | **Complete — PASS** |
| 012-C | [Competition, Actor, Competitor Context & Bias-Control Dependence](012-C-competition-actor-competitor-context-bias-control-dependence.md) | **Complete — PASS** |
| 012-D | [Evaluation Structure, Responsibility, Basis & Judgment Dependence](012-D-evaluation-structure-responsibility-basis-judgment-dependence.md) | **Complete — PASS** |
| 012-E | [Authority Lineage, Provenance & Correctability Dependence](012-E-authority-lineage-provenance-correctability-dependence.md) | **Complete — PASS** |
| 012-F | [Outcome, Recognition & Official-Authority Dependence](012-F-outcome-recognition-official-authority-dependence.md) | **Complete — PASS** |
| 012-G | External Representation & Release Dependence | **Next** |
| 012-H | Whole-Graph Transitivity, Co-Inclusion, Optionality & Minimal/Unfamiliar Subsets | Planned |
| 012-I | Product-Family Variants, Scope Selection & Variant-Specific Composition Revalidation | Planned |
| 012-J | Counterexample, Upstream-Reopen, Explanation-Order & Phase 013 Mapping Handoff Audit | Planned |
| 012-K | Canonical Dependence Reconciliation, Phase 012 Consolidation & Phase 013 Handoff | Planned |

## Current canonical dependence

Current durable dependence lives in [MUDAC Application-Family Concept Dependence](../canonical/dependence/application-family-dependence.md), now **partial through 012-F**.

### Competition / actor / competitor

```text
Team          → Competition
Participation → Competition
Participation → Identity
Division      → Team
Alias         → Team
Panel         → Participation
```

### Evaluation

```text
Evaluation Occurrence → Team / Participation / Rubric
Evaluation Obligation → Team / Participation / Rubric
Scorecard             → Team / Participation / Rubric
```

### Outcome / recognition

```text
Award               → Competition
Award               → Team
Outcome Declaration → Competition
```

## Important non-cycles

The graph intentionally does **not** collapse:

```text
Evaluation Occurrence ↔ Evaluation Obligation ↔ Scorecard
Award ↔ Outcome Declaration
```

The full application synchronizes these layers, but synchronization is not universal inclusion dependence.

## Authority-profile rules

012-E remains current:

```text
Authoritative Rubric Basis
  ⇒ Versioning + Provenance

Authoritative Scorecard Evidence
  ⇒ Versioning + Provenance

Rubric/Scorecard authoritative correction or invalidation
  ⇒ Versioning + Provenance
```

Versioning and Provenance remain independent support Concepts rather than graph-wide sinks.

Outcome Declaration owns its own declaration/currentness/successor lineage and does not universally depend on Versioning or Provenance.

## 012-F outcome result

012-F establishes:

- Award depends on Competition and Team;
- Outcome Declaration depends on Competition;
- Award does not depend on Outcome Declaration;
- Outcome Declaration does not depend on Award;
- Outcome Declaration does not acquire direct Scorecard/Obligation/Occurrence/Rubric edges merely because its accepted OutcomeBasis is traceable to those sources;
- Competition does not universally depend on Award or Outcome Declaration;
- ordinary official closeout is a capability rule requiring Competition + Outcome Declaration;
- current rank-derived Award capability uses a Ranking Ready basis and is Division-contextual under the current Rank mechanism, without creating universal `Award → Division`;
- official OutcomeBasis must be reconstructible, but the source Concept set is variant-specific rather than one fixed graph bundle.

Derived Coverage/Aggregate/Rank/Readiness remain mechanisms, not Concept vertices.

## Scope carry-forwards

012-I must later decide whether to adopt coherent variants such as:

- judging/operation without Award;
- judging/operation without Outcome Declaration;
- official outcome without Award;
- recognition without official declaration;
- discretionary Award without Division;
- no-Division rank-derived recognition, with required Rank/Award policy revalidation;
- exceptional/no-result official declarations with a different source-basis profile from ordinary ranked closeout.

Dependence-valid does not mean adopted.

## Design-only boundary

Phase 012 does not define package/module dependencies, service/database graphs, API direction, deployment order, UI hierarchy, commercial tiers, or implementation sequencing.

If subset analysis exposes a real composition gap, reopen/refine the natural Phase-011 owner. If it exposes intrinsic Concept coupling, reopen the natural Phase-010 owner.

## Current execution posture

```text
Jackson Concept Design: REOPENED / IN PROGRESS
009: COMPLETE — PASS
010: COMPLETE — PASS
011: COMPLETE — PASS
012: IN PROGRESS
012-A: COMPLETE — READY
012-B: COMPLETE — PASS
012-C: COMPLETE — PASS
012-D: COMPLETE — PASS
012-E: COMPLETE — PASS
012-F: COMPLETE — PASS
012-G: NEXT
architecture authority: SUSPENDED
implementation planning: SUSPENDED
new domain implementation: NOT STARTED
implementation readiness: NOT READY
implementation authorization: NOT YET
```

## Next

Proceed to **012-G — External Representation & Release Dependence**.

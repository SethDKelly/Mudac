# Phase 012 — Concept Dependence, Product-Family, Subset & Scope Analysis

Status: **IN PROGRESS — 012-A/B/C/D complete; 012-E next.**

## Role in the completion runway

Phase 012 corresponds to Base Phase 006 / Daniel Jackson Concept dependence and subset analysis.

Phase 010 established the current eighteen independent Concepts. Phase 011 established how included Concepts interact. Phase 012 now asks which Concepts must, may, conditionally or alternatively be co-included for coherent MUDAC application roles, which subsets are coherent, and which coherent variants are actually in scope.

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

implementation dependency
  = out of scope
```

A Phase 011 synchronization edge is evidence to inspect, not automatically a Phase 012 dependence edge.

## Application-family boundary

Phase 012 analyzes the **MUDAC live student data competition judging-and-outcome family**.

Competition is the anchor of every in-scope MUDAC variant, but anchoring is a scope rule rather than a blanket `Competition → every capability` graph edge.

## Current subgroup sequence

| Group | Topic | Status |
| --- | --- | --- |
| 012-A | [Dependence Scope, Subset Semantics, Product-Family Questions & Subphase Planning](012-A-dependence-scope-subset-semantics-product-family-questions-subphase-planning.md) | **Complete — READY** |
| 012-B | [Application-Family Boundary, Concept Inclusion Roles & Candidate Dependence Inventory](012-B-application-family-boundary-concept-inclusion-roles-candidate-dependence-inventory.md) | **Complete — PASS** |
| 012-C | [Competition, Actor, Competitor Context & Bias-Control Dependence](012-C-competition-actor-competitor-context-bias-control-dependence.md) | **Complete — PASS** |
| 012-D | [Evaluation Structure, Responsibility, Basis & Judgment Dependence](012-D-evaluation-structure-responsibility-basis-judgment-dependence.md) | **Complete — PASS** |
| 012-E | Authority Lineage, Provenance & Correctability Dependence | **Next** |
| 012-F | Outcome, Recognition & Official-Authority Dependence | Planned |
| 012-G | External Representation & Release Dependence | Planned |
| 012-H | Whole-Graph Transitivity, Co-Inclusion, Optionality & Minimal/Unfamiliar Subsets | Planned |
| 012-I | Product-Family Variants, Scope Selection & Variant-Specific Composition Revalidation | Planned |
| 012-J | Counterexample, Upstream-Reopen, Explanation-Order & Phase 013 Mapping Handoff Audit | Planned |
| 012-K | Canonical Dependence Reconciliation, Phase 012 Consolidation & Phase 013 Handoff | Planned |

## Current canonical dependence

Current accepted direct edges through 012-D are owned by [MUDAC Application-Family Concept Dependence](../canonical/dependence/application-family-dependence.md).

### Competition / actor / competitor context

```text
Team          → Competition
Participation → Competition
Participation → Identity
Division      → Team
Alias         → Team
Panel         → Participation
```

### Evaluation family

```text
Evaluation Occurrence → Team
Evaluation Occurrence → Participation
Evaluation Occurrence → Rubric

Evaluation Obligation → Team
Evaluation Obligation → Participation
Evaluation Obligation → Rubric

Scorecard             → Team
Scorecard             → Participation
Scorecard             → Rubric
```

Team/Participation edges give each evaluation Concept Competition/Identity transitively where applicable.

## 012-D result

012-D rejects an automatic inclusion bundle among the three evaluation-work Concepts:

```text
Evaluation Occurrence ↛ Evaluation Obligation
Evaluation Obligation ↛ Evaluation Occurrence
Evaluation Occurrence ↛ Scorecard
Scorecard             ↛ Evaluation Occurrence
Evaluation Obligation ↛ Scorecard
Scorecard             ↛ Evaluation Obligation
```

The ordinary full-product chain remains valid Phase-011 synchronization. It is simply not universal inclusion dependence.

Representative dependence-valid contractions now include:

- occurrence-history capability without obligation/judgment capture;
- responsibility/remaining-work capability without bounded occurrence/judgment capture;
- lightweight Scorecard capture without formal obligation/occurrence;
- full evaluation capability containing all three.

These contractions are **not yet adopted product variants**. 012-I owns scope selection. If selected, their natural Phase-011 synchronization owners must be revalidated/refined.

Rubric remains independently useful as reusable evaluation-instrument preparation and has no outgoing evaluation edge in 012-D.

## Conditional capability rules retained

- blinded judging includes Alias;
- multi-cohort competition includes Division;
- reusable intended evaluator grouping includes Panel;
- protected Judge/Organizer actions use Participation context plus Access;
- single-cohort no-Division operation is dependence-coherent but requires later policy/composition revalidation before adoption;
- occurrence-backed responsibility, responsibility-backed Scorecard, and occurrence-backed Scorecard context apply when those Concepts are co-included, without making them universal dependencies.

## Canonical dependence authority

Current accepted dependence lives under:

- [Canonical Dependence](../canonical/dependence/)
- [MUDAC Application-Family Concept Dependence](../canonical/dependence/application-family-dependence.md)

That owner is explicitly **partial through 012-D**. Versioning/Provenance, outcome/recognition, and externalization/release remain unresolved until 012-E through 012-G.

Do not copy contextual dependence into intrinsic Concept specifications.

## Design-only boundary

Phase 012 does not define source/package/module dependencies, service/database graphs, API direction, deployment order, UI hierarchy, commercial tiers, or implementation sequencing.

If subset analysis exposes a real composition gap, reopen/refine the natural Phase 011 owner. If it exposes intrinsic Concept coupling, reopen the natural Phase 010 owner.

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
012-E: NEXT
architecture authority: SUSPENDED
implementation planning: SUSPENDED
new domain implementation: NOT STARTED
implementation readiness: NOT READY
implementation authorization: NOT YET
```

## Next

Proceed to **012-E — Authority Lineage, Provenance & Correctability Dependence**.

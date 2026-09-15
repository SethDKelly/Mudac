# Phase 012 — Concept Dependence, Product-Family, Subset & Scope Analysis

Status: **IN PROGRESS — 012-A/B/C/D/E complete; 012-F next.**

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
  = a named application capability requires a set of Concepts
    even though the underlying Concepts can appear in reduced roles without that set

implementation dependency
  = out of scope
```

A Phase-011 synchronization edge is evidence, not automatically a Phase-012 dependence edge.

## Application-family boundary

Phase 012 analyzes the **MUDAC live student data competition judging-and-outcome family**.

Competition anchors every in-scope MUDAC variant, but that is a scope rule rather than a blanket `Competition → every capability` edge.

## Current subgroup sequence

| Group | Topic | Status |
| --- | --- | --- |
| 012-A | [Dependence Scope, Subset Semantics, Product-Family Questions & Subphase Planning](012-A-dependence-scope-subset-semantics-product-family-questions-subphase-planning.md) | **Complete — READY** |
| 012-B | [Application-Family Boundary, Concept Inclusion Roles & Candidate Dependence Inventory](012-B-application-family-boundary-concept-inclusion-roles-candidate-dependence-inventory.md) | **Complete — PASS** |
| 012-C | [Competition, Actor, Competitor Context & Bias-Control Dependence](012-C-competition-actor-competitor-context-bias-control-dependence.md) | **Complete — PASS** |
| 012-D | [Evaluation Structure, Responsibility, Basis & Judgment Dependence](012-D-evaluation-structure-responsibility-basis-judgment-dependence.md) | **Complete — PASS** |
| 012-E | [Authority Lineage, Provenance & Correctability Dependence](012-E-authority-lineage-provenance-correctability-dependence.md) | **Complete — PASS** |
| 012-F | Outcome, Recognition & Official-Authority Dependence | **Next** |
| 012-G | External Representation & Release Dependence | Planned |
| 012-H | Whole-Graph Transitivity, Co-Inclusion, Optionality & Minimal/Unfamiliar Subsets | Planned |
| 012-I | Product-Family Variants, Scope Selection & Variant-Specific Composition Revalidation | Planned |
| 012-J | Counterexample, Upstream-Reopen, Explanation-Order & Phase 013 Mapping Handoff Audit | Planned |
| 012-K | Canonical Dependence Reconciliation, Phase 012 Consolidation & Phase 013 Handoff | Planned |

## Current canonical dependence

Current accepted direct edges are owned by [MUDAC Application-Family Concept Dependence](../canonical/dependence/application-family-dependence.md).

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

Team/Participation supply Competition transitively and Participation supplies Identity transitively.

## Evaluation non-cycle

Evaluation Occurrence, Evaluation Obligation, and Scorecard are not a mandatory co-inclusion group.

Their current full-product relationships remain Phase-011 synchronization, while dependence-valid contractions may separately support:

- occurrence/history;
- responsibility/remaining work;
- judgment capture;
- or the full evaluation capability.

Those contractions are not yet adopted product variants.

## 012-E authority-history result

012-E adds **no new universal direct graph edge**.

Versioning and Provenance are not graph-wide history sinks and do not universally depend on one another:

```text
Versioning ↛ Provenance
Provenance ↛ Versioning
```

Likewise working Rubric/Scorecard capability does not universally require either support Concept.

Instead, current authority profiles require:

```text
Authoritative Rubric Basis
  ⇒ Versioning + Provenance

Authoritative Scorecard Evidence
  ⇒ Versioning + Provenance

Rubric/Scorecard authoritative correction or invalidation
  ⇒ Versioning + Provenance
```

Outcome Declaration is an explicit counterexample to generic history routing:

```text
Outcome Declaration ↛ Versioning
Outcome Declaration ↛ Provenance
```

It already owns immutable declaration basis, declaring authority, Current/Affected/Superseded state, predecessor/successor history, and reconstructible declaration truth.

Outcome-affecting Evaluation Policy remains a non-Concept cross-cutting authority requirement: once judging begins it must stay reconstructible/versioned/provenanced.

## Conditional capability rules retained

- blinded judging includes Alias;
- multi-cohort competition includes Division;
- reusable intended evaluator grouping includes Panel;
- protected Judge/Organizer actions use Participation context plus Access;
- single-cohort no-Division operation is dependence-coherent but requires later policy/composition revalidation before adoption;
- if 012-I adopts an evaluation contraction, its natural Phase-011 synchronization owner must be revalidated;
- any adopted authoritative-evaluation variant must include Versioning + Provenance for authoritative Rubric/Scorecard state and preserve reconstructible outcome-affecting policy history.

## Canonical dependence authority

Current accepted dependence lives under:

- [Canonical Dependence](../canonical/dependence/)
- [MUDAC Application-Family Concept Dependence](../canonical/dependence/application-family-dependence.md)

The owner is explicitly **partial through 012-E**. Outcome/recognition and externalization/release remain unresolved until 012-F and 012-G.

Do not copy contextual dependence into intrinsic Concept specifications.

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
012-F: NEXT
architecture authority: SUSPENDED
implementation planning: SUSPENDED
new domain implementation: NOT STARTED
implementation readiness: NOT READY
implementation authorization: NOT YET
```

## Next

Proceed to **012-F — Outcome, Recognition & Official-Authority Dependence**.

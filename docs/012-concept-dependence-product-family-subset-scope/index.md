# Phase 012 — Concept Dependence, Product-Family, Subset & Scope Analysis

Phase 012 is the active Jackson/Base dependence phase after the Phase 011 composition exit.

## Status

**In Progress — 012-A/B/C complete; 012-D next.**

## Records

- [012-A — Dependence Scope, Subset Semantics, Product-Family Questions & Subphase Planning](012-A-dependence-scope-subset-semantics-product-family-questions-subphase-planning.md) — **Complete — READY TO BEGIN SUBPHASES**.
- [012-B — Application-Family Boundary, Concept Inclusion Roles & Candidate Dependence Inventory](012-B-application-family-boundary-concept-inclusion-roles-candidate-dependence-inventory.md) — **Complete — PASS**.
- [012-C — Competition, Actor, Competitor Context & Bias-Control Dependence](012-C-competition-actor-competitor-context-bias-control-dependence.md) — **Complete — PASS**.
- **012-D — Evaluation Structure, Responsibility, Basis & Judgment Dependence** — Next.
- 012-E — Authority Lineage, Provenance & Correctability Dependence — Planned.
- 012-F — Outcome, Recognition & Official-Authority Dependence — Planned.
- 012-G — External Representation & Release Dependence — Planned.
- 012-H — Whole-Graph Transitivity, Co-Inclusion, Optionality & Minimal/Unfamiliar Subsets — Planned.
- 012-I — Product-Family Variants, Scope Selection & Variant-Specific Composition Revalidation — Planned.
- 012-J — Counterexample, Upstream-Reopen, Explanation-Order & Phase 013 Mapping Handoff Audit — Planned.
- 012-K — Canonical Dependence Reconciliation, Phase 012 Consolidation & Phase 013 Handoff — Planned.

## Current canonical dependence

012-C establishes the first accepted direct edges:

```text
Team          → Competition
Participation → Competition
Participation → Identity
Division      → Team
Alias         → Team
Panel         → Participation
```

Canonical owner:

- [MUDAC Application-Family Concept Dependence](../canonical/dependence/application-family-dependence.md)

The owner is intentionally **partial through 012-C**. Later Phase 012 subgroups extend it.

## Current transitive consequences

```text
Division → Team → Competition
Alias    → Team → Competition
Panel    → Participation → Competition
Panel    → Participation → Identity
```

These are not duplicated as direct edges.

## Current explicit universal non-edges

```text
Competition ↛ Division
Competition ↛ Panel
Team        ↛ Alias
Identity    ↛ Competition
Identity    ↛ Participation
Access      ↛ Participation
Access      ↛ Identity
```

Access still participates in protected Judge/Organizer capability checks through current composition; the non-edge conclusion is about universal Concept inclusion only.

## Current scope/capability conclusions

- Competition anchors every in-scope MUDAC application variant.
- Division is optional except for variants that need multiple competitive cohorts or policy that explicitly requires Division context.
- Panel is optional when evaluators are assigned ad hoc.
- Alias is required for variants claiming the current blinded-judging role, but Team itself does not universally depend on Alias.
- a single-cohort no-Division variant remains dependence-coherent; current anonymity/disclosure policy would need later variant-specific revalidation before adoption.

## Immediate handoff

012-D now owns Evaluation Occurrence, Evaluation Obligation, Rubric and Scorecard dependence. It should use 012-C transitive reachability rather than redundantly adding Competition/Identity edges wherever Team or Participation already supplies them.

Proceed to **012-D — Evaluation Structure, Responsibility, Basis & Judgment Dependence**.

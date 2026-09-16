# Phase 012 — Concept Dependence, Product-Family, Subset & Scope Analysis

Phase 012 is the active Jackson/Base dependence phase after the Phase 011 composition exit.

## Status

**In Progress — 012-A through 012-G complete; 012-H next.**

## Records

- [012-A — Dependence Scope, Subset Semantics, Product-Family Questions & Subphase Planning](012-A-dependence-scope-subset-semantics-product-family-questions-subphase-planning.md) — **Complete — READY**.
- [012-B — Application-Family Boundary, Concept Inclusion Roles & Candidate Dependence Inventory](012-B-application-family-boundary-concept-inclusion-roles-candidate-dependence-inventory.md) — **Complete — PASS**.
- [012-C — Competition, Actor, Competitor Context & Bias-Control Dependence](012-C-competition-actor-competitor-context-bias-control-dependence.md) — **Complete — PASS**.
- [012-D — Evaluation Structure, Responsibility, Basis & Judgment Dependence](012-D-evaluation-structure-responsibility-basis-judgment-dependence.md) — **Complete — PASS**.
- [012-E — Authority Lineage, Provenance & Correctability Dependence](012-E-authority-lineage-provenance-correctability-dependence.md) — **Complete — PASS**.
- [012-F — Outcome, Recognition & Official-Authority Dependence](012-F-outcome-recognition-official-authority-dependence.md) — **Complete — PASS**.
- [012-G — External Representation & Release Dependence](012-G-external-representation-release-dependence.md) — **Complete — PASS**.
- **012-H — Whole-Graph Transitivity, Co-Inclusion, Optionality & Minimal/Unfamiliar Subsets** — Next.
- 012-I — Product-Family Variants, Scope Selection & Variant-Specific Composition Revalidation — Planned.
- 012-J — Counterexample, Upstream-Reopen, Explanation-Order & Phase 013 Mapping Handoff Audit — Planned.
- 012-K — Canonical Dependence Reconciliation, Phase 012 Consolidation & Phase 013 Handoff — Planned.

## Current canonical owner

[MUDAC Application-Family Concept Dependence](../canonical/dependence/application-family-dependence.md) owns current direct dependence and capability-conditioned co-inclusion through 012-G.

The final family-local edge added by 012-G is:

```text
Publication → Export
```

Important externalization non-edges are:

```text
Export ↛ Publication
Outcome Declaration ↛ Export
Outcome Declaration ↛ Publication
Export ↛ Outcome Declaration
Publication ↛ Outcome Declaration
```

Current capability rules include:

```text
External Representation
  ⇒ Export + exact SourceBasis + RepresentationProfile + AudienceProfile

Public Official-Result Release
  ⇒ Outcome Declaration + Export + Publication
```

Official-but-non-public operation, Export-without-Publication, and public non-official representation are all dependence-coherent. Publication-without-Export is not.

Paper capture continuity does not itself require Export; a stable printable/external representation does.

## Immediate handoff

012-H now owns whole-graph validation across every family resolved in 012-C through 012-G. It must test transitive closure, co-inclusion/cycles, optionality, minimal meaningful subsets, unfamiliar subsets, redundant edges, and consistency between direct edges and capability-conditioned rules.

Proceed to **012-H — Whole-Graph Transitivity, Co-Inclusion, Optionality & Minimal/Unfamiliar Subsets**.

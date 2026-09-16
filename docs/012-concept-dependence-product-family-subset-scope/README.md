# Phase 012 — Concept Dependence, Product-Family, Subset & Scope Analysis

Status: **IN PROGRESS — 012-A through 012-G complete; 012-H next.**

Phase 012 corresponds to Base Phase 006 / Daniel Jackson Concept dependence and subset analysis. Phase 010 established the eighteen independent Concepts; Phase 011 established composition; Phase 012 establishes which Concepts/capabilities must be co-included for coherent MUDAC application roles and which dependence-valid variants belong in scope.

Architecture and implementation remain suspended.

## Governing distinction

```text
intrinsic Concept dependence
  = upstream Concept-boundary defect

synchronization / composition
  = how already-included Concepts interact

extrinsic inclusion dependence
  = including A requires B for A's intended MUDAC role

capability-conditioned co-inclusion
  = a named capability requires a Concept set
    without making each Concept universally depend on that set

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
| 012-G | [External Representation & Release Dependence](012-G-external-representation-release-dependence.md) | **Complete — PASS** |
| 012-H | Whole-Graph Transitivity, Co-Inclusion, Optionality & Minimal/Unfamiliar Subsets | **Next** |
| 012-I | Product-Family Variants, Scope Selection & Variant-Specific Composition Revalidation | Planned |
| 012-J | Counterexample, Upstream-Reopen, Explanation-Order & Phase 013 Mapping Handoff Audit | Planned |
| 012-K | Canonical Dependence Reconciliation, Phase 012 Consolidation & Phase 013 Handoff | Planned |

## Canonical dependence through 012-G

Current durable authority is [MUDAC Application-Family Concept Dependence](../canonical/dependence/application-family-dependence.md).

Direct edge families now cover Competition/actor/competitor, evaluation, outcome/recognition, and externalization. The externalization family adds exactly:

```text
Publication → Export
```

while preserving:

```text
Export ↛ Publication
Outcome Declaration ↛ Export
Outcome Declaration ↛ Publication
Export ↛ Outcome Declaration
Publication ↛ Outcome Declaration
```

The full model therefore preserves:

```text
calculated != recognized != official != public != delivered
source authority != Export representation != Publication release != transport delivery
```

## Externalization capability rules

```text
External Representation
  ⇒ Export + exact SourceBasis + RepresentationProfile + AudienceProfile

Public Official-Result Release
  ⇒ Outcome Declaration + Export + Publication
```

A corrected successor release requires a successor/current Export plus an explicit Publication successor action; correction never silently retargets an old Publication.

Paper capture continuity does **not** universally require Export. Export is required only when a stable printable/external representation is itself part of the capability.

## Representative externalization subsets

Dependence-coherent examples include:

- Export without Publication;
- official Outcome Declaration without Export/Publication;
- official representation prepared but unreleased;
- public non-official material using Export + Publication;
- public official result using Outcome Declaration + Export + Publication.

These are not yet adopted product variants. 012-I owns scope selection.

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
012-G: COMPLETE — PASS
012-H: NEXT
architecture authority: SUSPENDED
implementation planning: SUSPENDED
new domain implementation: NOT STARTED
implementation readiness: NOT READY
implementation authorization: NOT YET
```

## Next

Proceed to **012-H — Whole-Graph Transitivity, Co-Inclusion, Optionality & Minimal/Unfamiliar Subsets**.

# Phase 012 — Concept Dependence, Product-Family, Subset & Scope Analysis

Phase 012 is the active Jackson/Base dependence phase after the Phase 011 composition exit.

## Status

**In Progress — 012-A through 012-F complete; 012-G next.**

## Records

- [012-A — Dependence Scope, Subset Semantics, Product-Family Questions & Subphase Planning](012-A-dependence-scope-subset-semantics-product-family-questions-subphase-planning.md) — **Complete — READY**.
- [012-B — Application-Family Boundary, Concept Inclusion Roles & Candidate Dependence Inventory](012-B-application-family-boundary-concept-inclusion-roles-candidate-dependence-inventory.md) — **Complete — PASS**.
- [012-C — Competition, Actor, Competitor Context & Bias-Control Dependence](012-C-competition-actor-competitor-context-bias-control-dependence.md) — **Complete — PASS**.
- [012-D — Evaluation Structure, Responsibility, Basis & Judgment Dependence](012-D-evaluation-structure-responsibility-basis-judgment-dependence.md) — **Complete — PASS**.
- [012-E — Authority Lineage, Provenance & Correctability Dependence](012-E-authority-lineage-provenance-correctability-dependence.md) — **Complete — PASS**.
- [012-F — Outcome, Recognition & Official-Authority Dependence](012-F-outcome-recognition-official-authority-dependence.md) — **Complete — PASS**.
- **012-G — External Representation & Release Dependence** — Next.
- 012-H — Whole-Graph Transitivity, Co-Inclusion, Optionality & Minimal/Unfamiliar Subsets — Planned.
- 012-I — Product-Family Variants, Scope Selection & Variant-Specific Composition Revalidation — Planned.
- 012-J — Counterexample, Upstream-Reopen, Explanation-Order & Phase 013 Mapping Handoff Audit — Planned.
- 012-K — Canonical Dependence Reconciliation, Phase 012 Consolidation & Phase 013 Handoff — Planned.

## Current canonical owner

[MUDAC Application-Family Concept Dependence](../canonical/dependence/application-family-dependence.md) owns current accepted dependence and capability-conditioned co-inclusion, partial through **012-F**.

## Current direct edge families

```text
Team          → Competition
Participation → Competition
Participation → Identity
Division      → Team
Alias         → Team
Panel         → Participation

Evaluation Occurrence → Team / Participation / Rubric
Evaluation Obligation → Team / Participation / Rubric
Scorecard             → Team / Participation / Rubric

Award               → Competition
Award               → Team
Outcome Declaration → Competition
```

## 012-E authority profile

```text
Authoritative Rubric Basis
  ⇒ Versioning + Provenance

Authoritative Scorecard Evidence
  ⇒ Versioning + Provenance
```

Versioning and Provenance are not universal sinks or a mandatory pair outside those named authority capabilities.

## 012-F outcome result

Recognition and official declaration remain separate capability layers:

```text
Award               ↛ Outcome Declaration
Outcome Declaration ↛ Award
```

Outcome Declaration also does not acquire direct Scorecard, Evaluation Obligation, Evaluation Occurrence, Rubric, or Team edges merely because an ordinary declared basis can be traced to those inputs.

Current capability rules include:

```text
Ordinary Official Closeout
  ⇒ Competition + Outcome Declaration

Rank-Derived Award capability
  ⇒ Award + legitimate Ranking Ready supplied Rank basis
```

Current Rank is Division-scoped, so rank-derived Award capability is Division-contextual under present policy/mechanisms without making `Award → Division` universal.

Official OutcomeBasis must be reconstructible, but its source Concept set is variant-specific.

## Immediate handoff

012-G now owns Export, Publication, external-representation and release dependence while preserving:

- official ≠ public;
- source authority ≠ Export representation ≠ Publication release;
- Award and Outcome Declaration independence;
- explicit release authority rather than automatic publication.

Proceed to **012-G — External Representation & Release Dependence**.

---
type: Canonical Dependence Validation
title: Whole-Graph Dependence & Subset Validation
description: "Current whole-graph validation of MUDAC Concept dependence after Phase 012-J counterexample audit, including acyclicity, transitive closure, optionality, minimal closures and unfamiliar-subset results; product scope remains separately owned by PF-01 scope authority."
status: stable
tags: [canonical, dependence, transitivity, optionality, subsets, phase-012]
sources:
  - resource: application-family-dependence.md
  - resource: product-family-scope.md
  - resource: ../../012-concept-dependence-product-family-subset-scope/012-H-whole-graph-transitivity-co-inclusion-optionality-minimal-unfamiliar-subsets.md
  - resource: ../../012-concept-dependence-product-family-subset-scope/012-J-counterexample-upstream-reopen-explanation-order-phase-013-mapping-handoff-audit.md
---

# Purpose

Validate the current MUDAC application-family dependence graph **as a whole** after family-local analysis completed through 012-G and counterexample audit in 012-J.

This document does not replace [MUDAC Application-Family Concept Dependence](application-family-dependence.md), which owns direct edges, universal non-edges and capability-conditioned rules.

It also does not select product scope. [MUDAC Product-Family Scope](product-family-scope.md) owns the PF-01 adoption decision.

# Validation result

**PASS.**

```text
whole direct graph: ACYCLIC
strongly connected components > 1 Concept: NONE
new direct edge required by closure: NONE
new direct edge required by 012-J counterexamples: NONE
Phase-010 reopening: NOT REQUIRED
Phase-011 reopening: NOT REQUIRED
```

No current Concept pair forms a genuine mutual-dependence/co-inclusion group.

# Family anchor versus optionality

`Competition` is the only universal **in-scope MUDAC family anchor** established by Phase 012.

Every other Concept is globally optional in the mathematical product family: at least one coherent capability/subset can omit it.

This is not a value ranking and does not mean the Concept is omitted from selected PF-01 product scope.

# Complete transitive closure by Concept

| Concept | Direct + transitive dependence requirements |
| --- | --- |
| Competition | none |
| Division | Team, Competition |
| Team | Competition |
| Panel | Participation, Identity, Competition |
| Evaluation Occurrence | Team, Participation, Rubric, Identity, Competition |
| Evaluation Obligation | Team, Participation, Rubric, Identity, Competition |
| Rubric | none |
| Scorecard | Team, Participation, Rubric, Identity, Competition |
| Award | Team, Competition |
| Identity | none |
| Participation | Identity, Competition |
| Alias | Team, Competition |
| Access | none |
| Versioning | none |
| Provenance | none |
| Outcome Declaration | Competition |
| Export | none |
| Publication | Export |

This is graph closure only. Capability-conditioned rules may add Concepts for a named capability without creating reverse universal edges.

# Reachability-redundant direct edge

`Award → Competition` is already reachable through:

```text
Award → Team → Competition
```

but remains intentionally retained because:

```text
Award → Competition = recognition scope
Award → Team        = recipient type
```

It is **reachability-redundant but semantically non-redundant**.

No other accepted direct edge requires pruning.

# Representative minimal closures

```text
Team
  → {Team, Competition}

Division
  → {Division, Team, Competition}

Participation
  → {Participation, Identity, Competition}

Panel
  → {Panel, Participation, Identity, Competition}

Evaluation Occurrence
  → {Evaluation Occurrence, Team, Participation, Rubric, Identity, Competition}

Evaluation Obligation
  → {Evaluation Obligation, Team, Participation, Rubric, Identity, Competition}

Scorecard
  → {Scorecard, Team, Participation, Rubric, Identity, Competition}

Award
  → {Award, Team, Competition}

Outcome Declaration
  → {Outcome Declaration, Competition}

Publication
  → {Publication, Export}
```

Singleton formal closures exist for Identity, Rubric, Access, Versioning, Provenance and Export.

Formal closure does not establish a meaningful or adopted MUDAC product variant.

# Unfamiliar-subset results

| Probe | Result |
| --- | --- |
| single-cohort Competition without Division | coherent |
| ad-hoc judging without Panel | coherent |
| judging-only without Award/Outcome Declaration/Export/Publication | coherent |
| official outcome without Award | coherent |
| official but non-public | coherent |
| Export without Publication | coherent |
| Export from non-outcome source | coherent |
| Publication without Export | invalid |
| no-Alias judging | coherent only outside current blinded-judging profile |
| working Rubric/Scorecard without Versioning/Provenance | coherent only without authoritative claim |
| Evaluation Obligation without Evaluation Occurrence | coherent |
| Evaluation Occurrence without Evaluation Obligation | coherent |
| paper versus electronic | not a Concept-subset axis |
| public non-official material | coherent |
| discretionary Award without Division | coherent |
| official no-result disposition without normal Team-result content | coherent with reconstructible accepted basis |

# Capability consistency

The capability-conditioned rules remain consistent with direct closure:

- authoritative evaluation adds Versioning + Provenance but no reverse support edges;
- rank-derived Award adds Division context under current Rank policy without universal `Award → Division`;
- ordinary official closeout includes Outcome Declaration while earlier Competition states may omit current declaration;
- public official-result release combines Outcome Declaration + Export + Publication without official/public mutual dependence;
- corrected release preserves `Publication → Export` and explicit successor action;
- paper continuity remains channel behavior unless stable printable representation is required.

# Scope after 012-I

The current adopted variant is:

> **PF-01 — MUDAC Live Competition Judging & Official Outcome**

PF-01 keeps all eighteen Concepts in its supported capability envelope.

The coherent contractions above remain counterexamples and future design options, not automatically supported products.

# 012-J counterexample result

012-J specifically re-challenged the whole model with product/state/profile, exceptional-outcome, paper, correction, Access, authority-support and externalization counterexamples.

No challenge requires a graph change.

The one material carry-forward is mapping revalidation: earlier Experience material still contains superseded terms and must be reconciled in Phase 013. That finding does not alter whole-graph validity.

# Current methodology handoff

```text
012-H  COMPLETE — PASS
012-I  COMPLETE — PASS
012-J  COMPLETE — PASS
012-K  NEXT — Canonical Dependence Reconciliation, Phase 012 Consolidation & Phase 013 Handoff
013    NOT STARTED
```

012-K should consolidate the current dependence/scope owners and formally authorize Phase 013 only if documentation integrity remains clean.

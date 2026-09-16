---
type: Canonical Dependence Validation
title: Whole-Graph Dependence & Subset Validation
description: "Current whole-graph validation of MUDAC Concept dependence after Phase 012-H, including acyclicity, transitive closure, optionality, minimal closures, representative unfamiliar subsets, and scope candidates for Phase 012-I."
status: stable
tags: [canonical, dependence, transitivity, optionality, subsets, phase-012]
sources:
  - resource: application-family-dependence.md
  - resource: ../../012-concept-dependence-product-family-subset-scope/012-H-whole-graph-transitivity-co-inclusion-optionality-minimal-unfamiliar-subsets.md
---

# Purpose

Validate the current MUDAC application-family dependence graph **as a whole** after family-local analysis completed through 012-G.

This document does not replace [MUDAC Application-Family Concept Dependence](application-family-dependence.md), which remains the owner of direct edges, universal non-edges, and capability-conditioned co-inclusion rules.

This owner records the durable whole-model conclusions needed for product-family scope selection.

# Validation result

**PASS.**

```text
whole direct graph: ACYCLIC
strongly connected components > 1 Concept: NONE
new direct edge required by closure: NONE
Phase-010 reopening: NOT REQUIRED
immediate Phase-011 reopening: NOT REQUIRED
```

No current Concept pair forms a genuine mutual-dependence/co-inclusion group.

# Family anchor versus optionality

`Competition` is the only universal **in-scope MUDAC family anchor**.

Every other Concept is globally optional in the precise sense that at least one coherent MUDAC-family capability/subset can omit it.

That statement does not rank importance. A globally optional Concept may still be mandatory for a named capability.

Examples:

```text
Authoritative Scorecard Evidence
  ⇒ Versioning + Provenance

current rank-derived Award capability
  ⇒ Division context

Ordinary Official Closeout
  ⇒ Outcome Declaration

Publication
  → Export

Public Official-Result Release
  ⇒ Outcome Declaration + Export + Publication
```

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

This is graph closure only. Capability-conditioned rules add Concepts for the named capability without creating reverse universal edges.

# Reachability-redundant direct edge

`Award → Competition` is already reachable through:

```text
Award → Team → Competition
```

but is intentionally retained because its rationale is independent:

```text
Award → Competition
  = recognition scope

Award → Team
  = recipient type
```

It is therefore **reachability-redundant but semantically non-redundant**.

No other accepted direct edge requires pruning.

# Minimal direct closures

```text
Competition
  → {Competition}

Team
  → {Team, Competition}

Division
  → {Division, Team, Competition}

Alias
  → {Alias, Team, Competition}

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

Singleton formal closures exist for:

```text
Identity
Rubric
Access
Versioning
Provenance
Export
```

Formal closure does not by itself establish a meaningful MUDAC product variant.

# Meaningful representative capability closures

## Competitor structure

```text
Competition + Team
```

## Scoped human participation

```text
Competition + Identity + Participation
```

## Evaluation occurrence history

```text
Competition + Team + Identity + Participation + Rubric + Evaluation Occurrence
```

## Responsibility tracking

```text
Competition + Team + Identity + Participation + Rubric + Evaluation Obligation
```

## Working judgment capture

```text
Competition + Team + Identity + Participation + Rubric + Scorecard
```

## Authoritative judgment

```text
Competition
+ Team
+ Identity
+ Participation
+ Rubric
+ Scorecard
+ Versioning
+ Provenance
```

## Discretionary recognition

```text
Competition + Team + Award
```

## Official disposition

```text
Competition + Outcome Declaration
```

plus a reconstructible accepted OutcomeBasis capability.

## Prepared representation

```text
Competition + Export
```

plus a valid SourceBasis capability.

## Deliberate non-official release

```text
Competition + Export + Publication
```

plus legitimate source/disclosure/publishing authority.

## Public official-result release

```text
Competition + Outcome Declaration + Export + Publication
```

plus accepted source/disclosure/publishing capability.

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
| official no-result disposition without Team-result content | coherent with reconstructible accepted basis |

# Capability consistency

The capability-conditioned rules remain consistent with direct closure:

- authoritative evaluation adds Versioning + Provenance but no reverse support edges;
- rank-derived Award adds Division context under current Rank policy but does not make every Award Division-dependent;
- ordinary official closeout includes Outcome Declaration while other Competition capabilities may omit it;
- public official-result release combines Outcome Declaration + Export + Publication without creating official/public mutual dependence;
- corrected release preserves `Publication → Export` and explicit successor action;
- paper continuity remains channel behavior unless a stable printable representation is required.

# Invalid whole-model claims

```text
Team without Competition
Participation without Competition or Identity
Division without Team
Alias without Team
Panel without Participation
Evaluation Occurrence without Team / Participation / Rubric
Evaluation Obligation without Team / Participation / Rubric
Scorecard without Team / Participation / Rubric
Award without Team or Competition
Outcome Declaration without Competition
Publication without Export
```

Capability-invalid examples include authoritative evaluation without required Versioning/Provenance, ordinary official closeout without Outcome Declaration, an official declaration without reconstructible accepted OutcomeBasis, Export without an exact valid SourceBasis contract, and public official-result release without Outcome Declaration + Export + Publication plus legitimate authority/disclosure.

# Product-family candidates for 012-I

Phase 012-I must deliberately select scope rather than treating every coherent subset as supported.

The decision set includes at least:

- single-cohort versus multi-cohort;
- blinded versus intentionally non-blinded judging;
- ad-hoc versus Panel-based evaluator organization;
- occurrence-history, responsibility-only, working Scorecard and authoritative evaluation contractions;
- recognition with or without official declaration;
- official declaration with or without Award;
- judging/operation without official declaration;
- Export without Publication;
- official-but-non-public;
- public non-official;
- public official-result release;
- current Division-contextual rank-derived recognition;
- possible no-Division ranked recognition requiring policy/composition generalization;
- paper/electronic/mixed capture as channel profiles rather than Concept-subset variants.

# Composition carry-forward

If 012-I adopts an alternative/reduced variant, refine the natural Phase-011 synchronization owner where necessary rather than changing dependence to match the incumbent full-product workflow.

Known candidates include no-Division blinded judging, evaluation variants omitting Occurrence/Obligation, no-Division ranked recognition, lifecycle semantics for variants omitting Outcome Declaration, and release profiles that preserve source authority / representation / publication / transport separation.

# Current methodology handoff

```text
012-H  COMPLETE — PASS
012-I  NEXT — Product-Family Variants, Scope Selection & Variant-Specific Composition Revalidation
```

The next task is scope selection, not additional family-local edge discovery unless new evidence reveals a contradiction.

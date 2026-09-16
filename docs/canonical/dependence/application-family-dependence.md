---
type: Canonical Dependence Model
title: MUDAC Application-Family Concept Dependence
description: "Current accepted extrinsic Concept inclusion dependence and capability-conditioned co-inclusion for the MUDAC live student data competition judging-and-outcome family after whole-graph validation in Phase 012-H."
status: stable
tags: [canonical, dependence, product-family, subsets, phase-012]
sources:
  - resource: ../../012-concept-dependence-product-family-subset-scope/012-C-competition-actor-competitor-context-bias-control-dependence.md
  - resource: ../../012-concept-dependence-product-family-subset-scope/012-D-evaluation-structure-responsibility-basis-judgment-dependence.md
  - resource: ../../012-concept-dependence-product-family-subset-scope/012-E-authority-lineage-provenance-correctability-dependence.md
  - resource: ../../012-concept-dependence-product-family-subset-scope/012-F-outcome-recognition-official-authority-dependence.md
  - resource: ../../012-concept-dependence-product-family-subset-scope/012-G-external-representation-release-dependence.md
  - resource: ../../012-concept-dependence-product-family-subset-scope/012-H-whole-graph-transitivity-co-inclusion-optionality-minimal-unfamiliar-subsets.md
  - resource: whole-graph-subset-validation.md
  - resource: ../project/mandate-context.md
  - resource: ../project/purpose-needs-success-tensions.md
---

# Purpose

Own current **extrinsic Concept inclusion dependence** and material **capability-conditioned co-inclusion** for the MUDAC application family.

This owner is intentionally compact. Detailed rejected-edge/counterexample reasoning remains in numbered Phase-012 history; whole-graph closure, optionality and subset validation live in [Whole-Graph Dependence & Subset Validation](whole-graph-subset-validation.md).

This owner is separate from intrinsic Concept definitions, Phase-011 synchronization/composition, derived mechanisms/policies, and downstream implementation dependency.

# Application-family context

The analyzed family is:

> **MUDAC live student data competition judging and outcome formation**, including preparation, independent evaluation, correction, explicit outcome authority, and optional controlled external representation/release.

Every adopted in-scope MUDAC variant retains Competition as the application-family context. That is a **family-scope rule**, not `Competition → every Concept`.

# Relation semantics

```text
A → B
```

means every coherent MUDAC subset containing A also contains B because A otherwise loses the application role for which it is included.

```text
Capability X
  ⇒ Concept A + Concept B
```

means the named capability requires the listed Concepts, while those Concepts may still be independently meaningful in reduced roles outside that capability.

Neither relation implies intrinsic specification coupling, runtime call direction, storage ownership, UI order, deployment sequence or implementation architecture.

# Current methodology state

```text
012-A  COMPLETE — READY
012-B  COMPLETE — PASS
012-C  COMPLETE — PASS
012-D  COMPLETE — PASS
012-E  COMPLETE — PASS
012-F  COMPLETE — PASS
012-G  COMPLETE — PASS
012-H  COMPLETE — PASS
012-I  NEXT — product-family scope selection
```

# Current direct dependence

## Competition / actor / competitor

<a id="dep-c-001"></a>
### DEP-C-001 — Team → Competition

```text
Team → Competition
```

A MUDAC Team is a student competitor group inside one Competition.

<a id="dep-c-002"></a>
### DEP-C-002 — Participation → Competition

```text
Participation → Competition
```

MUDAC Participation is scoped Judge/Organizer involvement in one Competition.

<a id="dep-c-003"></a>
### DEP-C-003 — Participation → Identity

```text
Participation → Identity
```

Participation requires stable human continuity for attribution, recovery and historical authority.

<a id="dep-c-004"></a>
### DEP-C-004 — Division → Team

```text
Division → Team
```

Division partitions Team competitors into competitive cohorts.

<a id="dep-c-005"></a>
### DEP-C-005 — Alias → Team

```text
Alias → Team
```

Alias supplies alternate identity for a Team competitor.

<a id="dep-c-006"></a>
### DEP-C-006 — Panel → Participation

```text
Panel → Participation
```

Panel groups event-scoped Judge Participations rather than permanent human identities.

## Evaluation

<a id="dep-d-001"></a>
### DEP-D-001 — Evaluation Occurrence → Team

```text
Evaluation Occurrence → Team
```

<a id="dep-d-002"></a>
### DEP-D-002 — Evaluation Occurrence → Participation

```text
Evaluation Occurrence → Participation
```

<a id="dep-d-003"></a>
### DEP-D-003 — Evaluation Occurrence → Rubric

```text
Evaluation Occurrence → Rubric
```

<a id="dep-d-004"></a>
### DEP-D-004 — Evaluation Obligation → Team

```text
Evaluation Obligation → Team
```

<a id="dep-d-005"></a>
### DEP-D-005 — Evaluation Obligation → Participation

```text
Evaluation Obligation → Participation
```

<a id="dep-d-006"></a>
### DEP-D-006 — Evaluation Obligation → Rubric

```text
Evaluation Obligation → Rubric
```

<a id="dep-d-007"></a>
### DEP-D-007 — Scorecard → Team

```text
Scorecard → Team
```

<a id="dep-d-008"></a>
### DEP-D-008 — Scorecard → Participation

```text
Scorecard → Participation
```

<a id="dep-d-009"></a>
### DEP-D-009 — Scorecard → Rubric

```text
Scorecard → Rubric
```

Evaluation Occurrence, Evaluation Obligation and Scorecard share Team, Judge Participation and Rubric as role anchors without universally depending on one another.

## Outcome / recognition

<a id="dep-f-001"></a>
### DEP-F-001 — Award → Competition

```text
Award → Competition
```

Award recognition belongs to a Competition scope.

<a id="dep-f-002"></a>
### DEP-F-002 — Award → Team

```text
Award → Team
```

Current MUDAC Award recipients are Teams.

`Award → Competition` is intentionally retained even though Competition is also transitively reachable through Team: recognition scope and recipient type are distinct roles.

<a id="dep-f-005"></a>
### DEP-F-005 — Outcome Declaration → Competition

```text
Outcome Declaration → Competition
```

Outcome Declaration establishes official-result authority for one Competition scope.

## Externalization / release

<a id="dep-g-002"></a>
### DEP-G-002 — Publication → Export

```text
Publication → Export
```

Publication is intrinsically generic over Representation, but Export is the MUDAC Concept owning stable representation identity, exact SourceBasis, purpose/audience representation contract and representation currency.

# Minimal direct graph

```text
Participation ─────→ Identity
       │
       └───────────→ Competition

Team ──────────────→ Competition
  ▲
  ├──────── Division
  ├──────── Alias
  └──────── Award

Panel ─────────────→ Participation

Evaluation Occurrence ─────→ Team
          │                 → Participation
          └────────────────→ Rubric

Evaluation Obligation ─────→ Team
          │                 → Participation
          └────────────────→ Rubric

Scorecard ─────────────────→ Team
          │                 → Participation
          └────────────────→ Rubric

Award ─────────────────────→ Competition
Outcome Declaration ───────→ Competition
Publication ────────────────→ Export
```

012-H validates this graph as acyclic with no mutual-dependence/co-inclusion group and no additional direct edge required by closure.

# Current universal non-edges

## Actor / competition

```text
Competition ↛ Division
Competition ↛ Panel
Team        ↛ Alias
Identity    ↛ Competition
Identity    ↛ Participation
Access      ↛ Participation
Access      ↛ Identity
```

Protected Judge/Organizer actions may still compose Participation context plus Access.

## Evaluation non-cycle

```text
Evaluation Occurrence ↛ Evaluation Obligation
Evaluation Obligation ↛ Evaluation Occurrence
Evaluation Occurrence ↛ Scorecard
Scorecard             ↛ Evaluation Occurrence
Evaluation Obligation ↛ Scorecard
Scorecard             ↛ Evaluation Obligation
```

## Authority-support separation

```text
Versioning ↛ Provenance
Provenance ↛ Versioning
Rubric     ↛ Versioning
Rubric     ↛ Provenance
Scorecard  ↛ Versioning
Scorecard  ↛ Provenance
Outcome Declaration ↛ Versioning
Outcome Declaration ↛ Provenance
Award ↛ Versioning
Award ↛ Provenance
```

Meaningful history alone does not make generic support Concepts universal sinks.

## Recognition / official-authority separation

```text
Award               ↛ Outcome Declaration
Outcome Declaration ↛ Award
Award               ↛ Division
Competition         ↛ Award
Competition         ↛ Outcome Declaration
Outcome Declaration ↛ Team
Outcome Declaration ↛ Scorecard
Outcome Declaration ↛ Evaluation Obligation
Outcome Declaration ↛ Evaluation Occurrence
Outcome Declaration ↛ Rubric
```

OutcomeBasis traceability is not direct inclusion dependence.

## Representation / release separation

```text
Export              ↛ Publication
Outcome Declaration ↛ Export
Outcome Declaration ↛ Publication
Export              ↛ Competition
Export              ↛ Outcome Declaration
Export              ↛ Award
Publication         ↛ Competition
Publication         ↛ Outcome Declaration
Publication         ↛ Award
```

Official authority may remain non-public and non-official material may be legitimately represented/released under applicable policy.

# Capability-conditioned authority rules

<a id="dep-e-003"></a>
## DEP-E-003 — Authoritative Rubric Basis

```text
Authoritative Rubric Basis
  ⇒ Versioning + Provenance
```

<a id="dep-e-004"></a>
## DEP-E-004 — Authoritative Scorecard Evidence

```text
Authoritative Scorecard Evidence
  ⇒ Versioning + Provenance
```

<a id="dep-e-005"></a>
## DEP-E-005 — Authoritative evaluation correction

```text
Rubric authoritative supersession/invalidation
  ⇒ Versioning + Provenance

Scorecard semantic amendment/capture correction/invalidation
  ⇒ Versioning + Provenance
```

<a id="dep-e-007"></a>
## DEP-E-007 — Outcome-affecting Evaluation Policy history

Once judging begins, outcome-affecting Evaluation Policy must remain reconstructible/versioned/provenanced under current MUDAC authority semantics.

Evaluation Policy remains a Policy, not a Concept graph vertex.

# Capability-conditioned outcome rules

<a id="dep-f-003"></a>
## DEP-F-003 — Rank-derived Award

```text
Rank-Derived Award capability
  ⇒ Award + legitimate Ranking Ready Rank SelectionBasis
```

Current Rank is Division-scoped, so current rank-derived recognition also includes Division context without creating universal `Award → Division`.

<a id="dep-f-007"></a>
## DEP-F-007 — Ordinary Official Closeout

```text
Ordinary Official Closeout
  ⇒ Competition + Outcome Declaration
```

<a id="dep-f-008"></a>
## DEP-F-008 — Reconstructible OutcomeBasis

Any official Outcome Declaration requires a reconstructible accepted OutcomeBasis. The exact source Concept set is variant-specific.

# Capability-conditioned externalization rules

<a id="dep-g-004"></a>
## DEP-G-004 — External Representation

```text
External Representation
  ⇒ Export
  + exact reconstructible SourceBasis
  + RepresentationProfile
  + AudienceProfile
```

No one source Concept is a universal Export dependency.

<a id="dep-g-005"></a>
## DEP-G-005 — Public Official-Result Release

```text
Public Official-Result Release
  ⇒ Outcome Declaration + Export + Publication
```

The release also requires legitimate disclosure and publishing authority.

<a id="dep-g-006"></a>
## DEP-G-006 — Corrected successor release

A replacement release requires a successor/current Export plus explicit Publication successor action. Source correction never silently retargets an existing Publication.

<a id="dep-g-007"></a>
## DEP-G-007 — Paper continuity is not Export dependence

Paper/electronic/mixed capture is a channel profile. Export becomes required only when stable printable/external representation is itself part of the capability.

# Whole-graph validation

Current closure, optionality, minimal meaningful subsets, unfamiliar-subset results and invalid whole-model claims are owned by [Whole-Graph Dependence & Subset Validation](whole-graph-subset-validation.md).

Key result:

```text
whole direct graph: ACYCLIC
co-inclusion cycles: NONE
new direct edge required: NONE
Competition: only universal in-scope family anchor
all other Concepts: globally optional / capability-conditionally required
```

# Scope-selection handoff

```text
dependence-valid
  != meaningful MUDAC family member
  != adopted in-scope variant
```

Phase 012-I now owns deliberate product-family scope selection and any variant-specific Phase-011 synchronization/policy revalidation required by adopted alternatives.

No Phase-010 reopening or immediate Phase-011 repair is required by the current graph.

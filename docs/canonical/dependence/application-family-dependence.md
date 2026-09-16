---
type: Canonical Dependence Model
title: MUDAC Application-Family Concept Dependence
description: "Current accepted extrinsic Concept inclusion dependence and capability-conditioned co-inclusion for the MUDAC live student data competition judging-and-outcome family. Complete through Phase 012-G concept-family analysis; whole-graph/subset validation continues in 012-H."
status: stable
tags: [canonical, dependence, product-family, subsets, phase-012]
sources:
  - resource: ../../012-concept-dependence-product-family-subset-scope/012-A-dependence-scope-subset-semantics-product-family-questions-subphase-planning.md
  - resource: ../../012-concept-dependence-product-family-subset-scope/012-B-application-family-boundary-concept-inclusion-roles-candidate-dependence-inventory.md
  - resource: ../../012-concept-dependence-product-family-subset-scope/012-C-competition-actor-competitor-context-bias-control-dependence.md
  - resource: ../../012-concept-dependence-product-family-subset-scope/012-D-evaluation-structure-responsibility-basis-judgment-dependence.md
  - resource: ../../012-concept-dependence-product-family-subset-scope/012-E-authority-lineage-provenance-correctability-dependence.md
  - resource: ../../012-concept-dependence-product-family-subset-scope/012-F-outcome-recognition-official-authority-dependence.md
  - resource: ../../012-concept-dependence-product-family-subset-scope/012-G-external-representation-release-dependence.md
  - resource: ../project/mandate-context.md
  - resource: ../project/purpose-needs-success-tensions.md
  - resource: ../concepts/
  - resource: ../synchronizations/
---

# Purpose

Own current **extrinsic Concept inclusion dependence** and material **capability-conditioned co-inclusion** for the MUDAC application family.

This owner is distinct from intrinsic Concept definitions, Phase-011 synchronization/composition, derived mechanisms/policies, and downstream implementation dependency.

# Application-family context

The analyzed family is:

> **MUDAC live student data competition judging and outcome formation**, including preparation, independent evaluation, correction, explicit outcome authority, and optional controlled external representation/release.

Every adopted in-scope MUDAC variant retains Competition as the application-family context. That scope rule is not a blanket `Competition → every capability` edge.

# Dependence forms

## Direct Concept edge

```text
A → B
```

means every coherent MUDAC subset containing A also contains B because A otherwise loses the application role for which it is included.

## Capability-conditioned co-inclusion

```text
Capability X
  ⇒ include Concept A + Concept B
```

means the named capability is invalid without those Concepts, while the underlying Concepts may still serve meaningful reduced roles outside that capability.

Neither form implies intrinsic specification coupling, runtime call direction, persistence ownership, UI ordering, deployment sequencing, or implementation architecture.

# Current methodology state

```text
012-A  COMPLETE — READY
012-B  COMPLETE — PASS
012-C  COMPLETE — PASS
012-D  COMPLETE — PASS
012-E  COMPLETE — PASS
012-F  COMPLETE — PASS
012-G  COMPLETE — PASS
012-H  NEXT — whole graph / transitivity / co-inclusion / minimal subsets
```

All Concept-family dependence questions are now resolved through 012-G. 012-H must validate the graph as a whole rather than adding family-local assumptions by default.

# Current direct dependence graph

## Competition / actor / competitor

<a id="dep-c-001"></a>
### DEP-C-001 — Team → Competition

```text
Team → Competition
```

Team's MUDAC role is a student group competing in one Competition.

<a id="dep-c-002"></a>
### DEP-C-002 — Participation → Competition

```text
Participation → Competition
```

Participation is time-bounded Judge/Organizer involvement in one Competition scope.

<a id="dep-c-003"></a>
### DEP-C-003 — Participation → Identity

```text
Participation → Identity
```

Participation requires stable human continuity for attribution, recovery, authority separation, and historical correctness.

<a id="dep-c-004"></a>
### DEP-C-004 — Division → Team

```text
Division → Team
```

Division partitions Team competitors into cohorts.

<a id="dep-c-005"></a>
### DEP-C-005 — Alias → Team

```text
Alias → Team
```

Alias supplies alternate Judge-facing identity for Team competitors.

<a id="dep-c-006"></a>
### DEP-C-006 — Panel → Participation

```text
Panel → Participation
```

Panel groups event-scoped Judge Participations rather than permanent human roles.

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

The three evaluation-work Concepts share Team, Judge Participation, and Rubric as their MUDAC role anchors without depending universally on one another.

## Outcome / recognition

<a id="dep-f-001"></a>
### DEP-F-001 — Award → Competition

```text
Award → Competition
```

Award's MUDAC role is recognized achievement within a Competition scope.

<a id="dep-f-002"></a>
### DEP-F-002 — Award → Team

```text
Award → Team
```

Current MUDAC Award recipients are Teams.

<a id="dep-f-005"></a>
### DEP-F-005 — Outcome Declaration → Competition

```text
Outcome Declaration → Competition
```

Outcome Declaration establishes explicit official-result authority for one Competition scope.

## Externalization / release

<a id="dep-g-002"></a>
### DEP-G-002 — Publication → Export

```text
Publication → Export
```

Publication is intrinsically generic over a supplied Representation, but within MUDAC Export is the only Concept that owns stable representation identity, exact SourceBasis, purpose/audience representation contract, and representation currency.

A MUDAC Publication without Export would therefore lose the representation role required for deliberate release.

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

# Key transitive consequences

```text
Division → Team → Competition
Alias    → Team → Competition
Panel    → Participation → Competition
Panel    → Participation → Identity
Award    → Team → Competition
```

Each Evaluation Occurrence, Evaluation Obligation, and Scorecard reaches Competition through Team/Participation and Identity through Participation.

`Publication → Export` currently has no further fixed source-Concept consequence because Export SourceBasis is variant-specific.

Do not duplicate transitive reachability as direct edges without a distinct application-role rationale.

# Current universal non-edges

## Competition / actor / competitor

```text
Competition ↛ Division
Competition ↛ Panel
Team        ↛ Alias
Identity    ↛ Competition
Identity    ↛ Participation
Access      ↛ Participation
Access      ↛ Identity
```

Protected Judge/Organizer actions still use Participation-derived context plus Access through composition.

## Evaluation non-cycle

```text
Evaluation Occurrence ↛ Evaluation Obligation
Evaluation Obligation ↛ Evaluation Occurrence
Evaluation Occurrence ↛ Scorecard
Scorecard             ↛ Evaluation Occurrence
Evaluation Obligation ↛ Scorecard
Scorecard             ↛ Evaluation Obligation
```

Rubric remains meaningful as reusable instrument definition outside full evaluation execution.

## Authority-support non-edges

```text
Versioning ↛ Provenance
Provenance ↛ Versioning
Rubric     ↛ Versioning
Rubric     ↛ Provenance
Scorecard  ↛ Versioning
Scorecard  ↛ Provenance
Competition ↛ Versioning
Competition ↛ Provenance
Evaluation Occurrence ↛ Versioning
Evaluation Occurrence ↛ Provenance
Evaluation Obligation ↛ Versioning
Evaluation Obligation ↛ Provenance
Outcome Declaration ↛ Versioning
Outcome Declaration ↛ Provenance
Award ↛ Versioning
Award ↛ Provenance
```

Meaningful history alone does not make Versioning or Provenance universal graph sinks.

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

Traceability into an OutcomeBasis is not direct inclusion dependence.

## Representation / release separation

<a id="dep-g-001"></a>
### DEP-G-001 — Export does not require Publication

```text
Export ↛ Publication
```

Generation/representation remains meaningful for print, download, preview, review, archival use, and prepared-but-unreleased material.

<a id="dep-g-003"></a>
### DEP-G-003 — Official authority may remain non-public

```text
Outcome Declaration ↛ Export
Outcome Declaration ↛ Publication
```

Official authority does not require externalization.

Additional current non-edges are:

```text
Export      ↛ Competition
Export      ↛ Outcome Declaration
Export      ↛ Award
Publication ↛ Competition
Publication ↛ Outcome Declaration
Publication ↛ Award
```

Export and Publication may operate over different legitimate source/representation purposes; neither is fixed to official-result release.

# Capability-conditioned authority rules

<a id="dep-e-003"></a>
## DEP-E-003 — Authoritative Rubric Basis

```text
Authoritative Rubric Basis
  ⇒ Versioning + Provenance
```

Working/preparation Rubric use does not trigger this profile.

<a id="dep-e-004"></a>
## DEP-E-004 — Authoritative Scorecard Evidence

```text
Authoritative Scorecard Evidence
  ⇒ Versioning + Provenance
```

Working non-authoritative Scorecard capture does not trigger this profile.

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

Evaluation Policy is not a Concept graph vertex.

# Capability-conditioned outcome rules

<a id="dep-f-003"></a>
## DEP-F-003 — Rank-derived Award

```text
Rank-Derived Award capability
  ⇒ Award + legitimate Ranking Ready Rank SelectionBasis
```

Coverage, Aggregate, Rank, Ranking Readiness, and Finalization Readiness remain mechanisms/policy facts rather than Concept vertices.

<a id="dep-f-004"></a>
## DEP-F-004 — Current rank-derived Award is Division-contextual

Current Rank is Division-scoped, so a variant claiming current rank-derived Award capability includes Division as ranking context.

This does not establish `Award → Division` because discretionary and competition-wide recognition remain coherent without Division.

<a id="dep-f-007"></a>
## DEP-F-007 — Ordinary official closeout

```text
Ordinary Official Closeout
  ⇒ Competition + Outcome Declaration
```

Current ordinary closeout coordinates `Competition.finalize + OutcomeDeclaration.declare` without making Outcome Declaration mandatory for every Competition capability.

<a id="dep-f-008"></a>
## DEP-F-008 — Reconstructible OutcomeBasis

Any variant claiming official Outcome Declaration must provide a reconstructible accepted OutcomeBasis.

The exact source Concept set is variant-specific. Exceptional/no-result declarations are a counterexample to one fixed evaluation-source bundle.

# Capability-conditioned externalization rules

<a id="dep-g-004"></a>
## DEP-G-004 — Export requires an exact valid SourceBasis

```text
External Representation capability
  ⇒ Export
  + exact reconstructible SourceBasis
  + RepresentationProfile
  + AudienceProfile
```

SourceBasis may come from different current/historical source capabilities. No one source Concept is universally required by Export.

<a id="dep-g-005"></a>
## DEP-G-005 — Public official-result release

```text
Public Official-Result Release
  ⇒ Outcome Declaration + Export + Publication
```

The representation must be legitimately releasable for the intended Public/Ceremony audience and Publication must have explicit publishing authority.

This does not create either `Outcome Declaration → Publication` or `Publication → Outcome Declaration` as universal edges.

<a id="dep-g-006"></a>
## DEP-G-006 — Corrected successor release

If corrected/current source meaning requires a replacement release:

```text
successor/current Export
+ explicit Publication successor action
```

are required.

Historical Publication remains bound to its original exact Export; source correction never silently retargets or republishes it.

<a id="dep-g-007"></a>
## DEP-G-007 — Paper continuity is not Export dependence

Paper capture/fallback uses the same evaluation semantics and may preserve physical source evidence without Export.

Export is required when a stable printable/external representation is itself needed, not merely because paper is involved.

# Representative dependence-valid subsets

These examples explain the model; they are **not yet adopted product variants**.

## Competition structure only

```text
Competition + Team
```

with optional Division/Alias according to the selected capability profile.

## Evaluation occurrence history

```text
Competition + Team + Identity + Participation + Rubric + Evaluation Occurrence
```

without mandatory Obligation/Scorecard.

## Responsibility tracking

```text
Competition + Team + Identity + Participation + Rubric + Evaluation Obligation
```

without mandatory Occurrence/Scorecard.

## Working judgment capture

```text
Competition + Team + Identity + Participation + Rubric + Scorecard
```

without authoritative-evidence claim and without mandatory Occurrence/Obligation.

## Authoritative judgment capability

The corresponding Scorecard/Rubric subset plus:

```text
Versioning + Provenance
```

under the authority-profile rules.

## Recognition without official declaration

```text
Competition + Team + Award
```

## Official declaration without Award

```text
Competition + Outcome Declaration
```

plus whatever source/policy capability provides the accepted reconstructible OutcomeBasis.

## Export without Publication

```text
Export + valid SourceBasis capability
```

Coherent for internal/download/print/preview representation.

## Official but non-public

```text
Competition + Outcome Declaration
without Export
without Publication
```

## Official representation prepared but unreleased

```text
Competition + Outcome Declaration + Export
without Publication
```

## Public non-official representation

```text
Export + Publication
without Outcome Declaration
```

coherent when source authority/disclosure policy legitimately permit the released claim.

## Public official result

```text
Competition + Outcome Declaration + Export + Publication
```

plus the appropriate accepted OutcomeBasis/disclosure/publishing-authority capabilities.

# Invalid inclusion/capability claims

Direct-dependence violations include:

```text
Team without Competition
Participation without Competition
Participation without Identity
Division without Team
Alias without Team
Panel without Participation
Evaluation Occurrence without Team / Participation / Rubric
Evaluation Obligation without Team / Participation / Rubric
Scorecard without Team / Participation / Rubric
Award without Competition
Award without Team
Outcome Declaration without Competition
Publication without Export
```

Capability-level invalid claims include:

```text
Authoritative Rubric Basis without Versioning or Provenance
Authoritative Scorecard Evidence without Versioning or Provenance
rank-derived Award without a legitimate Ranking Ready basis
ordinary official closeout without Outcome Declaration
official Outcome Declaration without reconstructible accepted OutcomeBasis
Export without exact valid SourceBasis/representation/audience contract
public official-result release without Outcome Declaration
public official-result release without a legitimately releasable Export
Publication treated as proof of delivery
Export generation treated as Publication
```

# Optionality and scope discipline

Dependence-valid does not mean adopted.

Current coherent reductions that 012-I must later accept/reject explicitly include:

- single-cohort operation without Division;
- ad-hoc Judge assignment without Panel;
- evaluation variants omitting Occurrence and/or Obligation;
- working-only Rubric/Scorecard capability without Versioning/Provenance;
- judging/operation without Award;
- judging/operation without Outcome Declaration;
- recognition without official declaration;
- official declaration without Award;
- Export without Publication;
- official-but-non-public operation;
- public non-official material;
- no-Division rank-derived recognition if Rank/Award policy is generalized.

# Cross-cutting composition carry-forward

If 012-I adopts a reduced or alternative variant, refine the natural Phase-011 synchronization owner where necessary rather than changing dependence merely to fit the incumbent full-product workflow.

Known carry-forwards include:

1. no-Division blinded judging → anonymity/disclosure and occurrence-presentation revalidation;
2. evaluation variants omitting Occurrence and/or Obligation → evaluation synchronization revalidation;
3. authoritative evaluation → retain Versioning + Provenance and reconstructible outcome-affecting Evaluation Policy history;
4. no-Division rank-derived Award → Rank/Award policy/composition revalidation;
5. judging/operation without Outcome Declaration → explicit lifecycle/closeout semantics that do not claim ordinary official closeout;
6. externalization variants → preserve source authority ≠ Export representation ≠ Publication release ≠ transport delivery;
7. public official-result release → explicit Outcome Declaration + Export + Publication composition;
8. paper continuity → do not manufacture Export dependence unless a stable printable representation is actually part of the capability.

# No hidden coordinator or transport Concept

Do not introduce Result, Outcome Aggregate, Closeout Coordinator, Workflow, History, Audit, Correction, Representation, Artifact, Document, Release Manager, Delivery, Distribution, Channel Delivery, or similar catch-all Concepts merely to connect existing owners.

Current ownership remains:

```text
Competition          = lifecycle context/closure
Coverage/Aggregate/Rank = derived facts
Award                = recognition
Outcome Declaration  = official authority
Export                = stable source-bound representation + currency
Publication           = deliberate release + distribution history
transport/delivery    = downstream realization
```

# Upstream integrity

No accepted Phase-012 edge or capability rule exposes intrinsic Concept coupling.

No Phase-010 reopening is currently required.

Phase-011 composition remains authoritative and no immediate repair is required before whole-graph/subset analysis.

# Phase 012-H handoff

012-H must now treat the direct graph and capability rules above as one complete candidate family model and analyze:

- transitive closure;
- any genuine co-inclusion groups/cycles;
- optionality;
- minimal meaningful subsets;
- unfamiliar but coherent subsets;
- redundant direct edges;
- direct-edge versus capability-rule consistency;
- whether any whole-graph contradiction forces Phase-010/011 reopening.

The next subgroup is:

> **012-H — Whole-Graph Transitivity, Co-Inclusion, Optionality & Minimal/Unfamiliar Subsets**

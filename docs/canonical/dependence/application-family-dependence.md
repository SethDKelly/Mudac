---
type: Canonical Dependence Model
title: MUDAC Application-Family Concept Dependence
description: "Current accepted extrinsic Concept inclusion dependence and capability-conditioned co-inclusion for the MUDAC live student data competition judging-and-outcome family after Phase 012 consolidation."
status: stable
tags: [canonical, dependence, product-family, subsets, phase-012]
sources:
  - resource: ../../012-concept-dependence-product-family-subset-scope/012-C-competition-actor-competitor-context-bias-control-dependence.md
  - resource: ../../012-concept-dependence-product-family-subset-scope/012-D-evaluation-structure-responsibility-basis-judgment-dependence.md
  - resource: ../../012-concept-dependence-product-family-subset-scope/012-E-authority-lineage-provenance-correctability-dependence.md
  - resource: ../../012-concept-dependence-product-family-subset-scope/012-F-outcome-recognition-official-authority-dependence.md
  - resource: ../../012-concept-dependence-product-family-subset-scope/012-G-external-representation-release-dependence.md
  - resource: ../../012-concept-dependence-product-family-subset-scope/012-H-whole-graph-transitivity-co-inclusion-optionality-minimal-unfamiliar-subsets.md
  - resource: ../../012-concept-dependence-product-family-subset-scope/012-J-counterexample-upstream-reopen-explanation-order-phase-013-mapping-handoff-audit.md
  - resource: ../../012-concept-dependence-product-family-subset-scope/012-K-canonical-dependence-reconciliation-phase-012-consolidation-phase-013-handoff.md
  - resource: whole-graph-subset-validation.md
  - resource: product-family-scope.md
---

# Purpose

Own current **extrinsic Concept inclusion dependence** and material **capability-conditioned co-inclusion** for the MUDAC application family.

This owner is intentionally compact. Detailed rejected-edge/counterexample reasoning remains in numbered Phase-012 records; whole-graph closure lives in [Whole-Graph Dependence & Subset Validation](whole-graph-subset-validation.md), and adopted scope lives in [MUDAC Product-Family Scope](product-family-scope.md).

This owner is separate from intrinsic Concept definitions, Phase-011 synchronization/composition, Phase-013 mapping, and downstream implementation dependency.

# Relation semantics

```text
A → B
```

means every coherent MUDAC subset containing A also contains B because A otherwise loses the application role for which it is included.

```text
Capability X
  ⇒ Concept A + Concept B
```

means the named capability requires the listed Concepts while those Concepts may remain independently meaningful in reduced roles.

Neither relation implies intrinsic specification coupling, workflow order, UI/navigation order, runtime call direction, storage ownership, deployment sequence, or implementation architecture.

# Current direct dependence

## Competition / actor / competitor

```text
Team          → Competition
Participation → Competition
Participation → Identity
Division      → Team
Alias         → Team
Panel         → Participation
```

Interpretation:

- Team is a competitor group inside one Competition;
- Participation is event-scoped human involvement and requires stable Identity;
- Division partitions Team competitors;
- Alias is alternate identity for Team;
- Panel groups event-scoped Judge Participations.

## Evaluation

```text
Evaluation Occurrence → Team
Evaluation Occurrence → Participation
Evaluation Occurrence → Rubric

Evaluation Obligation → Team
Evaluation Obligation → Participation
Evaluation Obligation → Rubric

Scorecard → Team
Scorecard → Participation
Scorecard → Rubric
```

Evaluation Occurrence, Evaluation Obligation and Scorecard share Team, Judge Participation and Rubric role anchors without universally depending on one another.

## Outcome / recognition

```text
Award               → Competition
Award               → Team
Outcome Declaration → Competition
```

`Award → Competition` remains intentionally retained even though Competition is transitively reachable through `Award → Team → Competition`: recognition scope and recipient type are distinct semantic reasons.

## Externalization / release

```text
Publication → Export
```

Within MUDAC, Export owns stable representation identity, exact SourceBasis, representation purpose/audience and representation currency. Publication owns deliberate release/distribution history.

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

Evaluation Occurrence ─────→ Team / Participation / Rubric
Evaluation Obligation ─────→ Team / Participation / Rubric
Scorecard ─────────────────→ Team / Participation / Rubric

Outcome Declaration ───────→ Competition
Publication ────────────────→ Export
```

Phase 012-H/J/K validate this relation as acyclic with no mutual-dependence/co-inclusion group and no additional direct edge required.

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

Official authority may remain non-public and legitimate non-official material may be represented/released under applicable policy.

# Capability-conditioned authority rules

## DEP-E-003 — Authoritative Rubric Basis

```text
Authoritative Rubric Basis
  ⇒ Versioning + Provenance
```

## DEP-E-004 — Authoritative Scorecard Evidence

```text
Authoritative Scorecard Evidence
  ⇒ Versioning + Provenance
```

## DEP-E-005 — Authoritative evaluation correction

```text
Rubric authoritative supersession/invalidation
  ⇒ Versioning + Provenance

Scorecard semantic amendment/capture correction/invalidation
  ⇒ Versioning + Provenance
```

## DEP-E-007 — Outcome-affecting Evaluation Policy history

Once judging begins, outcome-affecting Evaluation Policy must remain reconstructible/versioned/provenanced under current MUDAC authority semantics. Evaluation Policy remains a Policy, not a Concept graph vertex.

# Capability-conditioned outcome rules

## DEP-F-003 — Rank-derived Award

```text
Rank-Derived Award capability
  ⇒ Award + legitimate Ranking Ready Rank SelectionBasis
```

Current Rank is Division-scoped, so current rank-derived recognition also includes Division context without creating universal `Award → Division`.

## DEP-F-007 — Ordinary Official Closeout

```text
Ordinary Official Closeout
  ⇒ Competition + Outcome Declaration
```

## DEP-F-008 — Reconstructible OutcomeBasis

Any official Outcome Declaration requires a reconstructible accepted OutcomeBasis. The exact source Concept set is variant-specific.

# Capability-conditioned externalization rules

## DEP-G-004 — External Representation

```text
External Representation
  ⇒ Export
  + exact reconstructible SourceBasis
  + RepresentationProfile
  + AudienceProfile
```

No one source Concept is a universal Export dependency.

## DEP-G-005 — Public Official-Result Release

```text
Public Official-Result Release
  ⇒ Outcome Declaration + Export + Publication
```

The release also requires legitimate disclosure and publishing authority.

## DEP-G-006 — Corrected successor release

A replacement release requires a successor/current Export plus explicit Publication successor action. Source correction never silently retargets an existing Publication.

## DEP-G-007 — Paper continuity is not Export dependence

Paper/electronic/mixed capture is a channel profile. Export becomes required only when stable printable/external representation is itself part of the capability.

# Whole-graph and scope results

[Whole-Graph Dependence & Subset Validation](whole-graph-subset-validation.md) owns closure/optionality. [MUDAC Product-Family Scope](product-family-scope.md) owns adoption.

Current result:

```text
whole direct graph: ACYCLIC
co-inclusion cycles: NONE
new direct edge required: NONE
Competition: only universal in-scope family anchor
all other Concepts: globally optional across the mathematical family
PF-01: sole adopted current product variant
```

Global optionality does not mean omission from PF-01 or low importance.

# Final Phase-012 audit

Phase 012 re-challenged the direct graph and capability rules with product/state/profile, Access, authoritative-history, exceptional-outcome, paper, correction and externalization counterexamples and then reconciled all current canonical owners.

Result:

```text
new direct edge required: NO
existing edge removal required: NO
capability-rule change required: NO
PF-01 scope change required: NO
Phase-010 reopen required: NO
Phase-011 reopen required: NO
Phase-012 repair required: NO
```

The material carry-forward is Phase-013 mapping revalidation of pre-convergence Experience language. That does not change dependence semantics.

# Mapping boundary

Dependence may inform explanation/context, but:

```text
dependence order != navigation order
synchronization chain != mandatory wizard
```

See [Phase 013 Mapping Entry Authority](../experience/phase-013-entry-handoff.md).

# Current methodology state

```text
Phase 012  COMPLETE — PASS
Phase 013  COMPLETE — PASS
Phase 014  COMPLETE — PASS
Phase 015  COMPLETE — PASS WITH CARRY-FORWARD
Phase 016  COMPLETE — PASS WITH CLOSURE HANDOFF
Phase 017  IN PROGRESS — 017-B
```

This dependence model remains current authority. User-visible mapping is owned by [Experience](../experience/); methodology closure is owned by Phase 017.

No Phase-010 reopening, Phase-011 reopening or Phase-012 repair is required by the current dependence model.

---
type: Canonical Dependence Model
title: MUDAC Application-Family Concept Dependence
description: "Current accepted extrinsic Concept inclusion dependence and capability-conditioned co-inclusion for the MUDAC live student data competition judging-and-outcome family. Partial through Phase 012-F."
status: stable
tags: [canonical, dependence, product-family, subsets, phase-012]
sources:
  - resource: ../../012-concept-dependence-product-family-subset-scope/012-A-dependence-scope-subset-semantics-product-family-questions-subphase-planning.md
  - resource: ../../012-concept-dependence-product-family-subset-scope/012-B-application-family-boundary-concept-inclusion-roles-candidate-dependence-inventory.md
  - resource: ../../012-concept-dependence-product-family-subset-scope/012-C-competition-actor-competitor-context-bias-control-dependence.md
  - resource: ../../012-concept-dependence-product-family-subset-scope/012-D-evaluation-structure-responsibility-basis-judgment-dependence.md
  - resource: ../../012-concept-dependence-product-family-subset-scope/012-E-authority-lineage-provenance-correctability-dependence.md
  - resource: ../../012-concept-dependence-product-family-subset-scope/012-F-outcome-recognition-official-authority-dependence.md
  - resource: ../project/mandate-context.md
  - resource: ../project/purpose-needs-success-tensions.md
  - resource: ../concepts/
  - resource: ../synchronizations/
generated: { by: openai/gpt-5.6-sol, at: 2026-09-15T14:11:00-05:00 }
---

# Purpose

Own current **extrinsic Concept inclusion dependence** and material **capability-conditioned co-inclusion** for the MUDAC application family.

This owner is separate from intrinsic Concept definitions, Phase-011 synchronization/composition, derived mechanisms/policies, and downstream implementation dependency.

# Application-family context

The analyzed family is:

> **MUDAC live student data competition judging and outcome formation**, including preparation, independent evaluation, correction, explicit outcome authority, and optional controlled external representation/release.

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

means the named capability is invalid without those Concepts, while the Concepts may still have meaningful reduced roles outside that capability.

Do not flatten capability rules into false universal arrows.

Neither form implies intrinsic specification coupling, implementation call direction, persistence ownership, UI ordering, deployment sequencing, or runtime choreography.

# Current completion state

```text
012-A  COMPLETE — start gate
012-B  COMPLETE — candidate inventory
012-C  COMPLETE — Competition / actor / competitor / bias-control
012-D  COMPLETE — evaluation structure / responsibility / basis / judgment
012-E  COMPLETE — authority lineage / Provenance / correctability
012-F  COMPLETE — outcome / recognition / official authority
012-G  NEXT
```

This owner is **partial through 012-F**. External representation/release dependence remains unresolved until 012-G.

# Family scope

<a id="dep-family-001"></a>
## DEP-FAMILY-001 — Competition anchors in-scope MUDAC variants

Every in-scope MUDAC product/application variant retains Competition as the live student-competition context.

This is a product-family scope rule, not:

```text
Competition → every other Concept
```

A dependence-valid reusable subset may be coherent outside adopted MUDAC scope without becoming an in-scope variant.

# Accepted direct edges — Competition / actor / competitor

<a id="dep-c-001"></a>
## DEP-C-001 — Team → Competition

```text
Team → Competition
```

Team's MUDAC role is a student group competing in one Competition.

<a id="dep-c-002"></a>
## DEP-C-002 — Participation → Competition

```text
Participation → Competition
```

Participation is time-bounded Judge/Organizer involvement in one Competition scope.

<a id="dep-c-003"></a>
## DEP-C-003 — Participation → Identity

```text
Participation → Identity
```

Participation requires stable human continuity for attribution, recovery, authority separation, and historical correctness.

<a id="dep-c-004"></a>
## DEP-C-004 — Division → Team

```text
Division → Team
```

Division partitions Team competitors into cohorts.

<a id="dep-c-005"></a>
## DEP-C-005 — Alias → Team

```text
Alias → Team
```

Alias supplies alternate Judge-facing identity for Team competitors.

<a id="dep-c-006"></a>
## DEP-C-006 — Panel → Participation

```text
Panel → Participation
```

Panel groups event-scoped Judge Participations rather than permanent human roles.

# Accepted direct edges — evaluation

<a id="dep-d-001"></a>
## DEP-D-001 — Evaluation Occurrence → Team

```text
Evaluation Occurrence → Team
```

Occurrence preserves presentation/evaluation truth for one Team.

<a id="dep-d-002"></a>
## DEP-D-002 — Evaluation Occurrence → Participation

```text
Evaluation Occurrence → Participation
```

Occurrence evaluator identities are event-scoped Judge Participations.

<a id="dep-d-003"></a>
## DEP-D-003 — Evaluation Occurrence → Rubric

```text
Evaluation Occurrence → Rubric
```

MUDAC evaluation occurrences use Rubric-owned evaluation-basis semantics.

<a id="dep-d-004"></a>
## DEP-D-004 — Evaluation Obligation → Team

```text
Evaluation Obligation → Team
```

The responsibility concerns evaluation of one Team.

<a id="dep-d-005"></a>
## DEP-D-005 — Evaluation Obligation → Participation

```text
Evaluation Obligation → Participation
```

The responsible evaluator is an event-scoped Judge Participation.

<a id="dep-d-006"></a>
## DEP-D-006 — Evaluation Obligation → Rubric

```text
Evaluation Obligation → Rubric
```

MUDAC evaluation responsibility is defined against Rubric-owned evaluation semantics.

<a id="dep-d-007"></a>
## DEP-D-007 — Scorecard → Team

```text
Scorecard → Team
```

A MUDAC Scorecard records one Judge's judgment of one Team.

<a id="dep-d-008"></a>
## DEP-D-008 — Scorecard → Participation

```text
Scorecard → Participation
```

Scorecard semantic authorship is attributable to an event-scoped Judge Participation.

<a id="dep-d-009"></a>
## DEP-D-009 — Scorecard → Rubric

```text
Scorecard → Rubric
```

Rubric supplies response interpretation, validation, completeness, and scoring semantics.

# Accepted direct edges — outcome / recognition

<a id="dep-f-001"></a>
## DEP-F-001 — Award → Competition

```text
Award → Competition
```

Award's MUDAC role is recognized achievement within a Competition scope.

<a id="dep-f-002"></a>
## DEP-F-002 — Award → Team

```text
Award → Team
```

Current MUDAC Award recipients are Teams.

The direct Competition edge is retained alongside this edge because recognition scope and recipient identity are distinct application-role reasons.

<a id="dep-f-005"></a>
## DEP-F-005 — Outcome Declaration → Competition

```text
Outcome Declaration → Competition
```

Outcome Declaration establishes explicit official-result authority for one Competition scope.

# Current minimal direct graph

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
```

No Phase-012-E direct edge was added; 012-E establishes capability profiles instead. 012-F adds only the three outcome/recognition edges above.

# Transitive consequences

Current reachability includes:

```text
Division → Team → Competition
Alias    → Team → Competition
Panel    → Participation → Competition
Panel    → Participation → Identity
Award    → Team → Competition
```

Each Evaluation Occurrence, Evaluation Obligation, and Scorecard reaches Competition through Team/Participation and Identity through Participation.

Do not duplicate transitive reachability as direct edges without a distinct role rationale.

# Explicit universal non-edges — 012-C

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

# Explicit universal non-edges — 012-D

Evaluation Occurrence, Evaluation Obligation, and Scorecard are not a mandatory co-inclusion group:

```text
Evaluation Occurrence ↛ Evaluation Obligation
Evaluation Obligation ↛ Evaluation Occurrence
Evaluation Occurrence ↛ Scorecard
Scorecard             ↛ Evaluation Occurrence
Evaluation Obligation ↛ Scorecard
Scorecard             ↛ Evaluation Obligation
```

Rubric also remains meaningful as reusable instrument definition outside a full evaluation execution subset.

# Authority-support rules — 012-E

<a id="dep-e-001"></a>
## DEP-E-001 — Versioning and Provenance are not graph-wide sinks

Meaningful history does not automatically create a Versioning or Provenance edge.

Current universal non-edges include:

```text
Rubric                ↛ Versioning
Rubric                ↛ Provenance
Scorecard             ↛ Versioning
Scorecard             ↛ Provenance
Competition           ↛ Versioning
Competition           ↛ Provenance
Evaluation Occurrence ↛ Versioning
Evaluation Occurrence ↛ Provenance
Evaluation Obligation ↛ Versioning
Evaluation Obligation ↛ Provenance
```

<a id="dep-e-002"></a>
## DEP-E-002 — Versioning and Provenance do not universally require one another

```text
Versioning ↛ Provenance
Provenance ↛ Versioning
```

They own distinct purposes even when they co-participate in high-assurance actions.

<a id="dep-e-003"></a>
## DEP-E-003 — Authoritative Rubric Basis requires Versioning + Provenance

```text
Authoritative Rubric Basis
  ⇒ Versioning + Provenance
```

Working/preparation Rubric use does not trigger this profile.

<a id="dep-e-004"></a>
## DEP-E-004 — Authoritative Scorecard Evidence requires Versioning + Provenance

```text
Authoritative Scorecard Evidence
  ⇒ Versioning + Provenance
```

Working non-authoritative Scorecard capture does not trigger this profile.

<a id="dep-e-005"></a>
## DEP-E-005 — Authoritative evaluation correction keeps both support roles

```text
Rubric authoritative supersession/invalidation
  ⇒ Versioning + Provenance

Scorecard semantic amendment/capture correction/invalidation
  ⇒ Versioning + Provenance
```

<a id="dep-e-006"></a>
## DEP-E-006 — Outcome Declaration owns its own authority lineage

```text
Outcome Declaration ↛ Versioning
Outcome Declaration ↛ Provenance
```

Outcome Declaration intrinsically owns immutable OutcomeBasis, DeclaringAuthority, Current/Affected/Superseded meaning, predecessor/successor declarations, affected reason/basis, and reconstructible declaration history.

<a id="dep-e-007"></a>
## DEP-E-007 — Outcome-affecting Evaluation Policy history is cross-cutting

Evaluation Policy is not a Concept graph vertex.

Once judging begins, outcome-affecting policy must remain reconstructible/versioned/provenanced under current MUDAC authority semantics.

# Outcome / recognition rules — 012-F

<a id="dep-f-003"></a>
## DEP-F-003 — Rank-derived Award requires a Ranking Ready supplied basis

```text
Rank-Derived Award capability
  ⇒ Award + legitimate Ranking Ready Rank SelectionBasis
```

Coverage, Aggregate, Rank, Ranking Readiness, and Finalization Readiness remain derived mechanisms/policy facts rather than Concept vertices.

<a id="dep-f-004"></a>
## DEP-F-004 — Current rank-derived Award is Division-contextual, not universally Award-dependent

Current Rank is Division-scoped. Therefore a variant claiming current rank-derived Award capability includes Division as part of the ranking context.

This does **not** establish:

```text
Award → Division
```

because discretionary and competition-wide recognition remain coherent without Division.

If 012-I adopts a no-Division ranked variant, Rank/Award policy and synchronization must be revalidated/generalized rather than manufacturing a placeholder Division.

<a id="dep-f-006"></a>
## DEP-F-006 — Award and Outcome Declaration are not a co-inclusion cycle

```text
Award               ↛ Outcome Declaration
Outcome Declaration ↛ Award
```

Recognition and official declaration may synchronize in the full product while remaining independently meaningful application layers.

<a id="dep-f-007"></a>
## DEP-F-007 — Ordinary official closeout includes Outcome Declaration

```text
Ordinary Official Closeout
  ⇒ Competition + Outcome Declaration
```

Current ordinary closeout coordinates `Competition.finalize + OutcomeDeclaration.declare`.

This does not establish `Competition → Outcome Declaration`, because Competition remains meaningful before closeout and in reduced judging/operation variants.

<a id="dep-f-008"></a>
## DEP-F-008 — Official OutcomeBasis is reconstructible without one fixed source-Concept bundle

Any variant claiming official Outcome Declaration must supply a reconstructible accepted OutcomeBasis.

The exact source Concepts vary by outcome profile. Therefore do not add fixed direct edges from Outcome Declaration to every traceable source.

Current universal non-edges include:

```text
Outcome Declaration ↛ Team
Outcome Declaration ↛ Scorecard
Outcome Declaration ↛ Evaluation Obligation
Outcome Declaration ↛ Evaluation Occurrence
Outcome Declaration ↛ Rubric
```

Authoritative judged-result variants may still include authoritative Scorecard evidence and therefore inherit the 012-E Versioning + Provenance profile.

Exceptional/no-result declarations provide a counterexample to a fixed evaluation-source bundle.

# Additional Award non-edges — 012-F

```text
Award ↛ Outcome Declaration
Award ↛ Division
Award ↛ Versioning
Award ↛ Provenance
```

Award owns attributable recognition definition/conferral/revocation/correction history sufficient for its current Concept role.

# Competition does not universally require outcome layers

012-F does not add:

```text
Competition → Award
Competition → Outcome Declaration
```

Competition can coherently support preparation/live judging/operation without those layers at the dependence level.

Scope adoption belongs to 012-I.

# Conditional product-family rules retained from 012-C

## Blinded judging

A variant claiming the current blinded-judging baseline includes Alias.

Current disclosure policy also names Division in Judge-facing representation. A single-cohort no-Division variant remains dependence-coherent but requires policy/composition revalidation before adoption.

## Multi-cohort competition

A variant supporting multiple competitive cohorts includes Division.

## Reusable evaluator grouping

A variant supporting reusable intended Judge groups includes Panel. Ad-hoc evaluator assignment may omit Panel.

## Protected Judge/Organizer operations

Protected Judge/Organizer operations use Participation context plus Access. Access itself has no universal outgoing edge to Participation or Identity.

# Evaluation contractions retained from 012-D

Dependence-valid capability contractions include:

```text
Evaluation Occurrence + Team + Participation + Rubric
without Evaluation Obligation / Scorecard
```

```text
Evaluation Obligation + Team + Participation + Rubric
without Evaluation Occurrence / Scorecard
```

```text
Scorecard + Team + Participation + Rubric
without Evaluation Occurrence / Evaluation Obligation
```

These remain scope candidates until 012-I.

# Authority-profile contractions retained from 012-E

## Working Rubric preparation

```text
Rubric
without Versioning
without Provenance
```

Coherent only without claiming immutable authoritative judging basis.

## Working Scorecard capture

```text
Scorecard + Team + Participation + Rubric
without Versioning
without Provenance
```

Coherent only without claiming authoritative evidence/current eligible lineage.

## Invalid authority claims

```text
Authoritative Rubric Basis without Versioning
Authoritative Rubric Basis without Provenance
Authoritative Scorecard Evidence without Versioning
Authoritative Scorecard Evidence without Provenance
```

# Outcome subsets introduced by 012-F

## Recognition without official declaration

```text
Competition + Team + Award
```

Coherent for discretionary recognition without Outcome Declaration.

## Official declaration without Award

```text
Competition + Outcome Declaration
```

This is the minimum 012-F Concept requirement for declaration authority itself. A real adopted variant must additionally provide the source/policy capability necessary for a reconstructible accepted OutcomeBasis.

## Full recognition + declaration

```text
Competition + Team + Award + Outcome Declaration
```

Award and Outcome Declaration remain independent authority owners even when Award state is included in the declared basis.

## Judging/operation without outcome layers

A Competition/evaluation subset may omit Award and Outcome Declaration at the dependence level. Scope adoption belongs to 012-I.

# Invalid outcome claims

```text
Award without Competition
Award without Team
Outcome Declaration without Competition
```

Capability-level invalid claims include:

```text
rank-derived Award without a legitimate Ranking Ready basis
ordinary official closeout without Outcome Declaration
official Outcome Declaration without a reconstructible accepted OutcomeBasis
```

# Correction boundary

Post-source correction may require Award review/correction and may make Outcome Declaration Affected.

That composition does not create Award↔Outcome Declaration dependence, and corrected calculation/recognition never becomes official automatically.

Outcome Declaration retains explicit successor-confirmation authority.

# No catch-all coordinator

Do not introduce Result, Outcome aggregate, Closeout, Winner, Finalization coordinator, Recognition coordinator, Official Result Version, Workflow, History, Audit, Correction, or Cascade as new semantic owners merely to connect existing concepts.

Current ownership remains:

```text
Coverage / Aggregate / Rank = derived facts
Award                       = recognition
Competition                 = lifecycle closure
Outcome Declaration         = official authority
Export / Publication        = externalization, resolved next
```

# Upstream integrity

No accepted Phase-012-C/D/F direct edge or 012-E/F capability rule exposes intrinsic Concept coupling.

No Phase-010 reopening is required.

# Composition boundary

Dependence does not replace Phase-011 synchronization.

Current full-product composition remains authoritative, including:

- occurrence/responsibility/evaluation coordination;
- authoritative Rubric/Scorecard support through Versioning + Provenance;
- Coverage/Aggregate/Rank derivation;
- explicit Award conferral/correction;
- coordinated Competition Finalization + initial Outcome Declaration;
- Affected/successor declaration handling after source correction.

No immediate Phase-011 repair is required.

# Policy/composition carry-forward

1. A no-Division blinded variant, if adopted by 012-I, requires anonymity/disclosure and occurrence-presentation revalidation.
2. A variant omitting Occurrence and/or Obligation requires its natural Phase-011 composition revalidation before adoption.
3. Any authoritative-evaluation variant must preserve Versioning + Provenance for authoritative Rubric/Scorecard and outcome-affecting Evaluation Policy history.
4. Outcome Declaration must not be routed through generic Versioning merely because it is authoritative.
5. A no-Division rank-derived Award variant, if adopted, requires Rank/Award policy/composition revalidation.
6. A judging/operation variant omitting Outcome Declaration must define its lifecycle/closeout scope explicitly rather than silently claiming ordinary official closeout.
7. Official outcome variants must provide reconstructible OutcomeBasis support without assuming one fixed upstream Concept bundle.

# Next unresolved family

Phase 012-G owns Export, Publication, external-representation, and release dependence.

It must preserve these current results:

- official does not imply public;
- Award and Outcome Declaration remain separate;
- Outcome Declaration does not depend on Export/Publication merely because official state may later be represented/released;
- current source authority must never be confused with Export representation or Publication release;
- `Publication → Export` remains the strongest candidate from 012-B and must be tested rather than assumed.

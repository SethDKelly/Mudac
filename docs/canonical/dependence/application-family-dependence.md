---
type: Canonical Dependence Model
title: MUDAC Application-Family Concept Dependence
description: "Current accepted extrinsic Concept inclusion dependence and capability-conditioned co-inclusion for the MUDAC live student data competition judging-and-outcome family. Partial through Phase 012-E."
status: stable
tags: [canonical, dependence, product-family, subsets, phase-012]
sources:
  - resource: ../../012-concept-dependence-product-family-subset-scope/012-A-dependence-scope-subset-semantics-product-family-questions-subphase-planning.md
  - resource: ../../012-concept-dependence-product-family-subset-scope/012-B-application-family-boundary-concept-inclusion-roles-candidate-dependence-inventory.md
  - resource: ../../012-concept-dependence-product-family-subset-scope/012-C-competition-actor-competitor-context-bias-control-dependence.md
  - resource: ../../012-concept-dependence-product-family-subset-scope/012-D-evaluation-structure-responsibility-basis-judgment-dependence.md
  - resource: ../../012-concept-dependence-product-family-subset-scope/012-E-authority-lineage-provenance-correctability-dependence.md
  - resource: ../project/mandate-context.md
  - resource: ../project/purpose-needs-success-tensions.md
  - resource: ../concepts/
  - resource: ../synchronizations/
generated: { by: openai/gpt-5.6-sol, at: 2026-09-15T14:11:00-05:00 }
---

# Purpose

Own current **extrinsic Concept inclusion dependence** and material **capability-conditioned co-inclusion** for the MUDAC application family.

This owner is separate from:

- intrinsic Concept specifications under [`../concepts/`](../concepts/);
- interaction/composition under [`../synchronizations/`](../synchronizations/);
- policies/mechanisms that are not Concept graph vertices;
- downstream implementation dependencies.

# Application-family context

The analyzed family is:

> **MUDAC live student data competition judging and outcome formation**, including preparation, independent evaluation, operational correction, explicit outcome authority, and optional controlled external representation/release.

# Edge meaning

For Concepts `A` and `B`:

```text
A → B
```

means every coherent MUDAC subset containing A also contains B because A otherwise loses the application role for which it is included.

An edge does **not** imply intrinsic specification coupling, state ownership, synchronization of every action, implementation call direction, storage relation, module layering, UI ordering, or implementation sequence.

# Capability-conditioned co-inclusion

Not every durable inclusion rule is honestly expressible as a universal binary Concept edge.

Phase 012-E introduces this second form:

```text
Capability X
  ⇒ include Concept A + Concept B
```

This means the named application capability is invalid without the listed Concepts, while the underlying Concepts may still appear meaningfully in reduced capabilities without that support.

Do not flatten capability-conditioned rules into false universal arrows.

# Current completion state

```text
012-A  COMPLETE — start gate
012-B  COMPLETE — candidate inventory
012-C  COMPLETE — Competition / actor / competitor / bias-control
012-D  COMPLETE — evaluation structure / responsibility / basis / judgment
012-E  COMPLETE — authority lineage / Provenance / correctability
012-F  NEXT
```

This owner is **partial through 012-E**. Absence of an unresolved outcome/externalization edge is not yet a canonical non-edge unless explicitly stated below.

# Family scope

<a id="dep-family-001"></a>
## DEP-FAMILY-001 — Competition anchors in-scope MUDAC variants

Every **in-scope MUDAC product/application variant** retains Competition as the live student-competition context.

This is a product-family scope rule, not:

```text
Competition → every other Concept
```

A dependence-valid generic subset may be coherent outside the adopted MUDAC product scope without becoming an in-scope variant.

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

MUDAC Participation is time-bounded Judge/Organizer involvement in one Competition scope.

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

Division's MUDAC role is partitioning Team competitors into cohorts.

<a id="dep-c-005"></a>
## DEP-C-005 — Alias → Team

```text
Alias → Team
```

Alias's MUDAC role is alternate Judge-facing identity for Team competitors.

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

The bounded occurrence preserves presentation/evaluation truth for one student Team.

<a id="dep-d-002"></a>
## DEP-D-002 — Evaluation Occurrence → Participation

```text
Evaluation Occurrence → Participation
```

Occurrence evaluators are event-scoped Judge Participations.

<a id="dep-d-003"></a>
## DEP-D-003 — Evaluation Occurrence → Rubric

```text
Evaluation Occurrence → Rubric
```

A MUDAC evaluation occurrence is governed by Rubric-owned evaluation-basis semantics.

<a id="dep-d-004"></a>
## DEP-D-004 — Evaluation Obligation → Team

```text
Evaluation Obligation → Team
```

The responsibility concerns evaluation of one MUDAC Team.

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

MUDAC responsibility is defined against declared Rubric-owned evaluation semantics.

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

# Current minimal direct graph

```text
Participation ─────→ Identity
       │
       └───────────→ Competition

Team ──────────────→ Competition
  ▲
  ├──────── Division
  └──────── Alias

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
```

No Phase 012-E universal edge is added to this direct graph.

# Transitive consequences

Current reachability includes:

```text
Division → Team → Competition
Alias    → Team → Competition
Panel    → Participation → Competition
Panel    → Participation → Identity
```

Each Evaluation Occurrence, Evaluation Obligation, and Scorecard also reaches:

```text
→ Team → Competition
→ Participation → Competition
→ Participation → Identity
```

Do not duplicate transitive reachability as direct edges without a distinct application-role rationale.

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

Access non-edges do not remove protected-operation composition. Judge/Organizer protected actions still use Participation-derived context plus Access.

# Explicit universal non-edges — 012-D

The evaluation Concepts are not a mandatory co-inclusion cycle:

```text
Evaluation Occurrence ↛ Evaluation Obligation
Evaluation Obligation ↛ Evaluation Occurrence
Evaluation Occurrence ↛ Scorecard
Scorecard             ↛ Evaluation Occurrence
Evaluation Obligation ↛ Scorecard
Scorecard             ↛ Evaluation Obligation
```

The full application may include and synchronize all three while smaller coherent capability subsets omit one or more.

# Authority-support non-edges — 012-E

<a id="dep-e-001"></a>
## DEP-E-001 — Versioning and Provenance are not graph-wide sinks

The existence of meaningful history does not automatically create a Versioning or Provenance dependency.

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

Working/preparation variants provide counterexamples, while Competition/Occurrence/Obligation already own history intrinsic to their purposes.

<a id="dep-e-002"></a>
## DEP-E-002 — Versioning and Provenance do not universally depend on one another

```text
Versioning ↛ Provenance
Provenance ↛ Versioning
```

They frequently co-participate in high-assurance authority actions but own distinct purposes.

Versioning preserves immutable authoritative snapshots/current eligibility.

Provenance explains meaningful actor, represented-authority, source, reason, and correction history.

# Authority-capability co-inclusion — 012-E

<a id="dep-e-003"></a>
## DEP-E-003 — Authoritative Rubric Basis requires Versioning + Provenance

```text
Authoritative Rubric Basis
  ⇒ Versioning + Provenance
```

Versioning is required to identify exact immutable/current basis authority and preserve successor/invalidation semantics.

Provenance is required to explain meaningful establishment/correction/invalidation authority.

A working/preparation Rubric does not trigger this rule.

<a id="dep-e-004"></a>
## DEP-E-004 — Authoritative Scorecard Evidence requires Versioning + Provenance

```text
Authoritative Scorecard Evidence
  ⇒ Versioning + Provenance
```

Versioning is required for immutable/current authoritative evidence, successor correction, and invalidation without predecessor revival.

Provenance is required for Judge authorship, capture actor versus represented authority, source/channel, and correction explanation.

Working non-authoritative Scorecard capture does not trigger this rule.

<a id="dep-e-005"></a>
## DEP-E-005 — Authoritative evaluation correction keeps both support roles

```text
Rubric authoritative supersession/invalidation
  ⇒ Versioning + Provenance

Scorecard semantic amendment/capture correction/invalidation
  ⇒ Versioning + Provenance
```

This rule preserves current Phase-011 correction semantics without converting support participation into universal Concept edges.

<a id="dep-e-006"></a>
## DEP-E-006 — Outcome Declaration owns its own authority lineage

```text
Outcome Declaration ↛ Versioning
Outcome Declaration ↛ Provenance
```

Outcome Declaration intrinsically owns immutable OutcomeBasis, DeclaringAuthority, Current/Affected/Superseded meaning, predecessor/successor declarations, affected reason/basis, and reconstructible declaration history.

Generic Versioning would duplicate declaration-owned lineage. Generic Provenance may enrich particular variants but is not universally required for the Concept's MUDAC role.

012-F still owns Outcome Declaration's actual outcome-family dependencies.

<a id="dep-e-007"></a>
## DEP-E-007 — Outcome-affecting Evaluation Policy history is a cross-cutting authority rule

Evaluation Policy is not a Concept graph vertex.

Once judging begins, outcome-affecting policy must remain reconstructible/versioned/provenanced under current MUDAC authority semantics.

Any adopted variant supporting authoritative judging/outcome formation must preserve that policy-history capability.

Do not invent a Policy Concept edge merely to encode this requirement.

# Conditional product-family rules retained from 012-C

## Blinded judging

A variant claiming the current blinded-judging baseline includes Alias.

Current disclosure policy also names Division in Judge-facing representation. A single-cohort no-Division variant remains dependence-coherent but requires later policy/composition revalidation before adoption. Do not fabricate a placeholder Division.

## Multi-cohort competition

A variant supporting multiple competitive cohorts includes Division.

Competition does not universally depend on Division.

## Reusable evaluator grouping

A variant supporting reusable intended Judge groups includes Panel.

Ad-hoc evaluator assignment may omit Panel.

## Protected Judge/Organizer operations

Protected Judge/Organizer operations use Participation context plus Access.

Access itself has no universal outgoing edge to Participation or Identity.

# Evaluation contractions retained from 012-D

Dependence-valid capability contractions include:

```text
Evaluation Occurrence + Team + Participation + Rubric
without Evaluation Obligation / Scorecard
```

bounded occurrence-history capability.

```text
Evaluation Obligation + Team + Participation + Rubric
without Evaluation Occurrence / Scorecard
```

responsibility/remaining-work capability.

```text
Scorecard + Team + Participation + Rubric
without Evaluation Occurrence / Evaluation Obligation
```

lightweight judgment-capture capability.

012-E further distinguishes whether the last two layers claim authoritative state.

# Authority-profile contractions retained from 012-E

## Working Rubric preparation

```text
Rubric
without Versioning
without Provenance
```

Coherent for working instrument definition/validation with no claim of immutable authoritative judging basis.

## Working Scorecard capture

```text
Scorecard + Team + Participation + Rubric
without Versioning
without Provenance
```

Coherent for working judgment capture with no claim of authoritative evidence/current eligible lineage.

## Invalid authority claims

The following capability claims are invalid:

```text
Authoritative Rubric Basis without Versioning
Authoritative Rubric Basis without Provenance
Authoritative Scorecard Evidence without Versioning
Authoritative Scorecard Evidence without Provenance
```

Whether working-only contractions are adopted into product scope belongs to 012-I.

# Correction boundary

Correction remains owner-specific.

Reject a generic model such as:

```text
any correction
  → History / Audit / Workflow / Revision coordinator
```

Versioning and Provenance participate only where their distinct purposes are required.

No new Workflow, History, Audit, Correction, Change, Revision, Authority, or Cascade Concept is justified.

# Upstream integrity

No accepted Phase 012-C/D edge or 012-E capability rule exposes intrinsic Concept coupling.

Current Concepts remain independently specified.

No Phase-010 reopening is required.

# Composition boundary

Dependence does not replace Phase-011 synchronization.

Current full-product composition remains:

- Establish Authoritative Rubric Version → Rubric + Versioning + Provenance;
- Finalize Evaluation → Scorecard + Versioning + Provenance + Evaluation Obligation satisfaction;
- Judge amendment → Scorecard + Versioning + Provenance;
- authoritative paper capture → Provenance distinguishes capture actor from Judge represented authority;
- Rubric/Scorecard invalidation → Versioning + meaningful Provenance;
- Evaluation Occurrence/Obligation remain separate history/responsibility owners.

Phase 012 states **which capabilities require co-inclusion**; Phase 011 states **how included Concepts coordinate**.

# Policy/composition carry-forward

1. A no-Division blinded variant, if adopted by 012-I, requires anonymity/disclosure and occurrence-presentation revalidation.
2. A variant omitting Occurrence and/or Obligation requires corresponding Phase-011 composition revalidation before adoption.
3. Any adopted authoritative-evaluation variant must include Versioning + Provenance for authoritative Rubric/Scorecard and outcome-affecting Evaluation Policy history.
4. Outcome Declaration must not be routed through generic Versioning merely because it is authoritative.

# Next unresolved family

Phase 012-F owns Award, Outcome Declaration, and official-outcome inclusion dependence.

It must preserve these current results:

- Award recognition and official declaration are distinct;
- Outcome Declaration already owns its own declaration lineage/currentness;
- authoritative Scorecards used as outcome evidence already carry the Versioning + Provenance authority-profile rule;
- outcome-affecting Evaluation Policy must remain reconstructible;
- evidence traceability must not be converted mechanically into dense direct Concept edges.

---
type: Canonical Dependence Model
title: MUDAC Application-Family Concept Dependence
description: "Current accepted extrinsic Concept inclusion dependence for the MUDAC live student data competition judging-and-outcome family. Partial through Phase 012-D; later Phase 012 subgroups extend this owner as additional concept families are resolved."
status: stable
tags: [canonical, dependence, product-family, subsets, phase-012]
sources:
  - resource: ../../012-concept-dependence-product-family-subset-scope/012-A-dependence-scope-subset-semantics-product-family-questions-subphase-planning.md
  - resource: ../../012-concept-dependence-product-family-subset-scope/012-B-application-family-boundary-concept-inclusion-roles-candidate-dependence-inventory.md
  - resource: ../../012-concept-dependence-product-family-subset-scope/012-C-competition-actor-competitor-context-bias-control-dependence.md
  - resource: ../../012-concept-dependence-product-family-subset-scope/012-D-evaluation-structure-responsibility-basis-judgment-dependence.md
  - resource: ../project/mandate-context.md
  - resource: ../project/purpose-needs-success-tensions.md
  - resource: ../concepts/
  - resource: ../synchronizations/
generated: { by: openai/gpt-5.6-sol, at: 2026-09-15T14:11:00-05:00 }
---

# Purpose

Own current **extrinsic Concept inclusion dependence** for the MUDAC application family.

This document is intentionally separate from:

- intrinsic Concept specifications under [`../concepts/`](../concepts/);
- interaction/composition under [`../synchronizations/`](../synchronizations/);
- implementation/module/service dependencies, which remain out of scope.

# Application-family context

The analyzed family is:

> **MUDAC live student data competition judging and outcome formation**, including preparation, independent evaluation, operational correction, explicit outcome authority, and optional controlled external representation/release.

Dependence is contextual to this family.

# Edge meaning

For current Concepts `A` and `B`:

```text
A → B
```

means:

> every coherent MUDAC subset containing A also contains B because A otherwise loses the application role for which it is included.

An edge does not imply intrinsic specification coupling, state ownership, synchronization of every action, implementation call direction, storage/schema relation, module layering, or UI ordering.

# Current completion state

```text
012-A  COMPLETE — start gate
012-B  COMPLETE — candidate inventory
012-C  COMPLETE — Competition / actor / competitor / bias-control dependence
012-D  COMPLETE — evaluation structure / responsibility / basis / judgment dependence
012-E  NEXT
```

This owner is therefore **partial through 012-D**. Absence of an edge involving unresolved authority-history/outcome/externalization Concepts is not yet a canonical non-edge unless explicitly stated by the owning Phase 012 subgroup.

# Family-scope rule

<a id="dep-family-001"></a>
## DEP-FAMILY-001 — Competition anchors in-scope MUDAC variants

Every **in-scope MUDAC product/application variant** retains a Competition context because the project mandate is specifically live student competition judging/outcome operation.

This is a product-family scope rule, not a blanket graph edge:

```text
Competition → every other Concept   // NOT the model
```

A dependence-valid subset of reusable generic Concepts can be coherent outside this product-family commitment without becoming an adopted MUDAC variant.

# Accepted direct edges through 012-C

<a id="dep-c-001"></a>
## DEP-C-001 — Team → Competition

```text
Team → Competition
```

Within MUDAC, Team serves as one student group acting as a competing unit inside a Competition. Generic cross-event roster semantics would be a different application role.

<a id="dep-c-002"></a>
## DEP-C-002 — Participation → Competition

```text
Participation → Competition
```

MUDAC Participation is one human's time-bounded Judge/Organizer involvement in one Competition scope.

<a id="dep-c-003"></a>
## DEP-C-003 — Participation → Identity

```text
Participation → Identity
```

MUDAC requires event participation to remain attributable to stable human continuity for authority separation, recovery and historical correctness.

<a id="dep-c-004"></a>
## DEP-C-004 — Division → Team

```text
Division → Team
```

Division's MUDAC role is partitioning Team competitors into competitive cohorts.

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

Panel's MUDAC role is reusable grouping of event-scoped Judge Participations rather than permanent human role assignment.

# Accepted direct evaluation edges through 012-D

<a id="dep-d-001"></a>
## DEP-D-001 — Evaluation Occurrence → Team

```text
Evaluation Occurrence → Team
```

Within MUDAC, the bounded occurrence preserves presentation/evaluation truth for one student Team.

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

A meaningful MUDAC evaluation occurrence is governed by declared evaluation-basis semantics owned by Rubric.

<a id="dep-d-004"></a>
## DEP-D-004 — Evaluation Obligation → Team

```text
Evaluation Obligation → Team
```

The responsibility exists to produce an evaluation of one MUDAC Team.

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

MUDAC evaluation responsibility is defined against declared Rubric-owned evaluation semantics.

<a id="dep-d-007"></a>
## DEP-D-007 — Scorecard → Team

```text
Scorecard → Team
```

A MUDAC Scorecard records one Judge's judgment of one student Team.

<a id="dep-d-008"></a>
## DEP-D-008 — Scorecard → Participation

```text
Scorecard → Participation
```

MUDAC Scorecard authorship is attributable to an event-scoped Judge Participation.

<a id="dep-d-009"></a>
## DEP-D-009 — Scorecard → Rubric

```text
Scorecard → Rubric
```

Rubric supplies the response interpretation, validation, completeness, and scoring semantics that give Scorecard its current MUDAC evaluation role.

# Minimal direct graph through 012-D

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

There is intentionally no direct inclusion edge among Evaluation Occurrence, Evaluation Obligation, and Scorecard.

# Transitive consequences

Current reachability includes:

```text
Division → Team → Competition
Alias    → Team → Competition
Panel    → Participation → Competition
Panel    → Participation → Identity
```

Every Evaluation Occurrence, Evaluation Obligation, and Scorecard now also reaches:

```text
→ Team → Competition
→ Participation → Competition
→ Participation → Identity
→ Rubric
```

Do not duplicate the Competition/Identity consequences as direct edges merely because the transitive statement is true.

# Explicit non-edges through 012-D

## Competition / actor / competitor non-edges

```text
Competition ↛ Division
Competition ↛ Panel
Team        ↛ Alias
Identity    ↛ Competition
Identity    ↛ Participation
Access      ↛ Participation
Access      ↛ Identity
```

The last two mean no **universal Concept-inclusion edge**. Protected Judge/Organizer operations still use Participation-derived context for Access under current synchronization authority.

## Evaluation-structure non-edges

```text
Evaluation Occurrence ↛ Evaluation Obligation
Evaluation Obligation ↛ Evaluation Occurrence
Evaluation Occurrence ↛ Scorecard
Scorecard             ↛ Evaluation Occurrence
Evaluation Obligation ↛ Scorecard
Scorecard             ↛ Evaluation Obligation

Rubric ↛ Competition
Rubric ↛ Evaluation Occurrence
Rubric ↛ Evaluation Obligation
Rubric ↛ Scorecard
```

These non-edges are deliberate. Ordinary Phase-011 synchronization among these Concepts does not make them an inseparable product-family bundle.

# Redundant candidate edges intentionally omitted

These are not represented as direct edges because current accepted paths already establish the same reachability:

```text
Division → Competition
Alias    → Competition
Panel    → Competition
Panel    → Identity

Evaluation Occurrence → Competition
Evaluation Occurrence → Identity
Evaluation Obligation → Competition
Evaluation Obligation → Identity
Scorecard             → Competition
Scorecard             → Identity
```

# Conditional capability/scope rules

## Protected Judge/Organizer operations

A protected operation performed in Judge or Organizer Competition capacity uses:

```text
Participation context
  + Access decision
```

Participation already requires Identity and Competition. Access itself remains reusable for support/exception/disclosure contexts and therefore has no universal outgoing peer dependency here.

012-D does not add dense direct edges from every protected evaluation Concept to Access. Protected operations remain governed by this capability rule.

## Blinded judging

A variant that claims the current blinded-judging baseline includes Alias as the alternate-identity owner.

Current disclosure policy also names Division in the Judge-facing representation. A single-cohort no-Division variant is dependence-coherent but requires later variant-specific policy/composition revalidation before adoption; the application must not fabricate a placeholder Division merely to satisfy historical wording.

## Multi-cohort competition

A variant supporting multiple competitive cohorts includes Division.

Competition does not universally depend on Division.

## Reusable evaluator grouping

A variant supporting reusable intended Judge groups includes Panel.

Ad-hoc evaluator assignment may omit Panel.

## Occurrence-backed responsibility

When a selected variant includes both Evaluation Occurrence and Evaluation Obligation, current full-product composition may establish obligations at occurrence begin.

The dependency graph does not require either Concept merely because the other is present.

## Responsibility-backed Scorecard

When a selected variant includes both Evaluation Obligation and Scorecard, current full-product composition may bind one logical Scorecard to one obligation and satisfy that responsibility on authoritative Finalization.

The dependency graph does not require either Concept merely because the other is present.

## Occurrence-backed Scorecard context

When a selected variant includes Evaluation Occurrence and Scorecard, the occurrence can own the bounded historical context supplied to Scorecard.

A Scorecard-capable variant may instead use a sufficient supplied context snapshot when Evaluation Occurrence is intentionally omitted; adoption of that contraction would require composition revalidation.

# Representative subset consequences through 012-D

## Dependence-valid

- single-cohort Competition without Division;
- ad-hoc judging organization without Panel;
- Team without Alias where the claimed role does not require blinded Judge presentation;
- Identity without any current Participation;
- Competition during setup before any Team instance exists;
- reusable Rubric preparation/library capability without Competition;
- occurrence-history capability with Evaluation Occurrence but without Evaluation Obligation or Scorecard;
- responsibility/remaining-work capability with Evaluation Obligation but without Evaluation Occurrence or Scorecard;
- lightweight judgment-capture capability with Scorecard but without Evaluation Occurrence or Evaluation Obligation;
- full evaluation capability containing Evaluation Occurrence + Evaluation Obligation + Scorecard.

These are dependence-valid statements only. Phase 012-I determines which coherent subsets become adopted MUDAC variants.

## Invalid

- Team without Competition;
- Participation without Competition or Identity;
- Division without Team;
- Alias without Team;
- Panel without Participation;
- Evaluation Occurrence without Team, Participation, or Rubric;
- Evaluation Obligation without Team, Participation, or Rubric;
- Scorecard without Team, Participation, or Rubric.

# Variant-specific composition carry-forward

012-D exposes three coherent contractions not represented as first-class current full-product paths in Phase 011:

1. Evaluation Occurrence without Evaluation Obligation;
2. Evaluation Obligation without Evaluation Occurrence;
3. Scorecard without Evaluation Obligation and/or Evaluation Occurrence.

No current synchronization is rewritten merely because those contractions are dependence-valid.

If Phase 012-I adopts any of them into scope, the natural Phase-011 owner must be revalidated/refined while preserving:

- Judge authorship;
- missing-versus-zero truth;
- enough context for correction/explanation;
- no duplicate semantic judgment;
- owner-safe authority establishment.

# Authority-history support remains unresolved

Current full MUDAC authoritative Rubric/Scorecard composition uses Versioning and Provenance.

Whether Rubric and/or Scorecard universally or conditionally require those support Concepts belongs to **012-E — Authority Lineage, Provenance & Correctability Dependence**.

Absence of such edges here is not a non-edge conclusion.

# Upstream integrity result

No accepted edge indicates intrinsic Concept coupling.

Current Concepts remain independently specified:

```text
Team<Scope>
Participation<Participant, Scope, Capacity>
Division<Scope, Member>
Alias<Subject, Scope, AliasValue>
Panel<Scope, Member, CapacityLabel>
Access<Principal, Capability, Resource, ContextFacts, Rule>
EvaluationOccurrence<Scope, Subject, Evaluator, PresentedContext, BasisRef>
EvaluationObligation<Scope, Evaluator, Subject, Basis, OccurrenceRef, EvidenceRef>
Rubric
Scorecard<Evaluator, Subject, OccurrenceContext, EvaluationBasis>
```

The accepted relationships are contextual application dependence only.

# Next unresolved family

Phase 012-E owns authority-lineage, Provenance, correctability, and the conditional inclusion role of Versioning/Provenance around authoritative Rubric/Scorecard state.

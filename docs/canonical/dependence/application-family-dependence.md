---
type: Canonical Dependence Model
title: MUDAC Application-Family Concept Dependence
description: "Current accepted extrinsic Concept inclusion dependence for the MUDAC live student data competition judging-and-outcome family. Partial through Phase 012-C; later Phase 012 subgroups extend this owner as additional concept families are resolved."
status: stable
tags: [canonical, dependence, product-family, subsets, phase-012]
sources:
  - resource: ../../012-concept-dependence-product-family-subset-scope/012-A-dependence-scope-subset-semantics-product-family-questions-subphase-planning.md
  - resource: ../../012-concept-dependence-product-family-subset-scope/012-B-application-family-boundary-concept-inclusion-roles-candidate-dependence-inventory.md
  - resource: ../../012-concept-dependence-product-family-subset-scope/012-C-competition-actor-competitor-context-bias-control-dependence.md
  - resource: ../project/mandate-context.md
  - resource: ../project/purpose-needs-success-tensions.md
  - resource: ../concepts/
  - resource: ../synchronizations/
generated: { by: openai/gpt-5.6-sol, at: 2026-09-15T11:26:00-05:00 }
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
012-C  COMPLETE — first accepted dependence family
012-D  NEXT
```

This owner is therefore **partial through 012-C**. Absence of an edge involving unresolved evaluation/outcome/externalization Concepts is not yet a canonical non-edge unless explicitly stated by the owning Phase 012 subgroup.

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

# Minimal direct graph

```text
Participation ─────→ Identity
       │
       └───────────→ Competition

Team ──────────────→ Competition
  ▲
  ├──────── Division
  └──────── Alias

Panel ─────────────→ Participation
```

# Transitive consequences

Current transitive reachability includes:

```text
Division → Team → Competition
Alias    → Team → Competition
Panel    → Participation → Competition
Panel    → Participation → Identity
```

Do not duplicate these as direct edges merely because the transitive statement is also true.

A later phase may add a direct edge only if it establishes a distinct application-role rationale that should remain meaningful independently of the intermediate edge.

# Explicit non-edges through 012-C

The following are current **universal non-edge conclusions**:

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

# Redundant candidate edges intentionally omitted

These are not represented as direct edges because current accepted paths already establish the same reachability:

```text
Division → Competition
Alias    → Competition
Panel    → Competition
Panel    → Identity
```

# Conditional capability/scope rules

These rules are meaningful inclusion constraints but are not universal binary graph edges.

## Protected Judge/Organizer operations

A protected operation performed in Judge or Organizer Competition capacity uses:

```text
Participation context
  + Access decision
```

Participation already requires Identity and Competition. Access itself remains reusable for support/exception/disclosure contexts and therefore has no universal outgoing peer dependency here.

## Blinded judging

A variant that claims the current blinded-judging baseline includes Alias as the alternate-identity owner.

Current disclosure policy also names Division in the Judge-facing representation. A single-cohort no-Division variant is dependence-coherent but requires later variant-specific policy/composition revalidation before adoption; the application must not fabricate a placeholder Division merely to satisfy historical wording.

## Multi-cohort competition

A variant supporting multiple competitive cohorts includes Division.

Competition does not universally depend on Division.

## Reusable evaluator grouping

A variant supporting reusable intended Judge groups includes Panel.

Ad-hoc evaluator assignment may omit Panel.

# Representative subset consequences

## Dependence-valid with respect to 012-C

- single-cohort Competition without Division;
- ad-hoc judging organization without Panel;
- Team without Alias where the claimed role does not require blinded Judge presentation;
- Identity without any current Participation;
- Competition during setup before any Team instance exists.

These statements concern 012-C edges only. Later 012-D through 012-G dependencies may add additional required Concepts for complete variants.

## Invalid with respect to 012-C

- Team without Competition;
- Participation without Competition;
- Participation without Identity;
- Division without Team;
- Alias without Team;
- Panel without Participation.

# Policy/composition carry-forward

Current Anonymity and Disclosure policy states that blinded Judge-facing Team representation is `Alias + Division`.

Phase 012-C establishes that Division is not a universal Competition dependency. Therefore, if Phase 012-I adopts a single-cohort no-Division variant, the natural policy/composition owner must be generalized to preserve blinded identity without manufacturing a fake Division.

This carry-forward does not reopen Phase 010 and does not yet require Phase 011 repair.

# Upstream integrity result

No accepted edge indicates intrinsic Concept coupling.

Current Concepts remain independently specified:

```text
Team          <Scope>
Participation <Participant, Scope, Capacity>
Division      <Scope, Member>
Alias         <Subject, Scope, AliasValue>
Panel         <Scope, Member, CapacityLabel>
Access        <Principal, Capability, Resource, ContextFacts, Rule>
```

The accepted relationships are contextual application dependence only.

# Next unresolved family

Phase 012-D owns Evaluation Occurrence, Evaluation Obligation, Rubric and Scorecard dependence.

It must use this graph transitively. For example, an accepted future edge to Participation already implies Identity + Competition, and an accepted future edge to Team already implies Competition.

---
type: Experience Contract
title: Organizer Competition Preparation & Readiness Mapping
description: Current Organizer preparation mapping for Competition setup, competitor structure, Judge/Panel planning, Rubric/evaluation-basis preparation, source-derived readiness, explicit Ready lifecycle commitment and Judge-safe preview.
status: stable
tags: [experience, mapping, organizer, preparation, competition, team, division, alias, panel, rubric, readiness, phase-013]
sources:
  - resource: ../../013-concept-mapping-interaction-semantics-user-visible-representation/013-D-competition-preparation-competitor-panel-rubric-setup-readiness-organizer-configuration-mapping.md
  - resource: ../concepts/competition.md
  - resource: ../concepts/team.md
  - resource: ../concepts/division.md
  - resource: ../concepts/alias.md
  - resource: ../concepts/panel.md
  - resource: ../concepts/rubric.md
  - resource: ../concepts/participation.md
  - resource: ../synchronizations/competition-participation-access.md
  - resource: ../synchronizations/evaluation-basis-scorecard-authority.md
  - resource: ../mechanisms/readiness.md
  - resource: ../policies/evaluation-policy.md
  - resource: ../policies/panel-composition.md
  - resource: ../policies/anonymity-disclosure.md
---

# Purpose

Define the user-visible semantic obligations for preparing one MUDAC Competition without turning setup, readiness, navigation or aggregated preparation views into independent domain authority.

# Preparation is a view over source truth

Organizer preparation composes visibility over independent authoritative sources such as:

- Competition;
- Team;
- Division;
- Alias;
- Judge Participation;
- Panel;
- Rubric / authoritative Rubric Version;
- Evaluation Policy and other applicable policy/configuration;
- optional Award/material preparation where the Competition profile uses it.

A preparation workspace may summarize these sources, but it owns none of them.

```text
source configuration
  → derived Competition Readiness
  → explicit Mark Competition Ready
  → Competition lifecycle = Ready
```

This is a semantic relationship, not a mandatory interface sequence.

# Non-linear preparation

Preparation is deliberately non-linear.

Organizers may work on legitimate source configuration in the order the Competition requires. The experience may use explanation order, grouping, progressive disclosure or recommendations, but must not imply that a fixed wizard sequence is itself domain truth.

```text
dependence order != navigation order
preparation completeness != wizard completion
```

When an action requires another source condition, explain the semantic precondition rather than inventing an artificial setup-step state.

# Competition context and lifecycle

The current Competition occurrence and lifecycle must be clear enough to prevent cross-event or lifecycle ambiguity during consequential configuration.

`Competition.create` and `Competition.updateDetails` are direct application actions.

Preparation must preserve:

```text
configuration sources sufficient
  != Competition lifecycle Ready

Competition Ready
  != Competition Active
```

The Competition becomes `Ready` only after the separate coordinated `Mark Competition Ready` action succeeds.

# Competitor structure

## Team

Team is the Organizer-facing administrative competing unit.

Preparation may show Team status and necessary administrative/descriptive attributes under current disclosure rules.

Team administrative identity and optional Team Name are not Judge-facing Alias.

## Division

Division owns competitive cohort definition and current Team assignment.

Where Division applies to the configured Competition, preparation must distinguish Team existence from valid current Division assignment.

Division correction is a semantic correction rather than a harmless visual regrouping. Detailed temporal/correction mapping belongs to 013-F.

## Alias

Alias owns the scoped Judge-facing alternate identity.

Under blinded judging, preparation must make it possible to determine whether each applicable Team has a valid active Judge-facing Alias and whether scope/uniqueness requirements are satisfied.

Preserve:

```text
Team administrative identity
  != Team Name
  != Alias
```

# Judge Participation and Panel planning

Preparation may expose expected/current Judge Participation and event-specific attributes such as expertise where useful for staffing/planning.

It must preserve:

```text
Identity
  != Judge Participation
  != checked-in/active Participation
  != Panel membership
```

Panel represents intended reusable evaluator grouping and optional composition-capacity assignment.

Showing Panel membership must not imply:

- actual Evaluation Occurrence participation;
- Evaluation Obligation responsibility;
- Team-specific judging work;
- Scorecard existence;
- Access to protected evaluation material.

Panel composition may be `Compliant`, `Degraded` or `Noncompliant` under policy. A governed exception preserves the actual shortfall rather than making a degraded Panel appear compliant.

Final event-day staffing is operational readiness rather than a universal structural gate for Competition Ready unless current Competition policy explicitly makes the condition blocking.

# Rubric and authoritative Evaluation Basis

Preparation must distinguish working Rubric state from the exact authoritative basis used for evaluation.

```text
working Rubric definition
  != validated definition
  != prepareForUse alone
  != authoritative immutable Rubric Version
  != occurrence-bound Evaluation Basis
```

Rubric configuration/validation actions remain direct application actions.

**Establish Authoritative Rubric Version** is a coordinated application action that establishes an immutable authoritative snapshot with Versioning/Provenance participation.

The representation must make clear when an Organizer is changing working definition versus establishing/succeeding authoritative basis. Generic Versioning or Provenance administration is not exposed.

Detailed Judge use of the exact Evaluation Basis belongs to the evaluation mapping.

# Evaluation Policy and configuration

Evaluation Policy may materially affect evidence eligibility, Rubric compatibility, Coverage, aggregation, ranking and tie semantics.

Preparation should expose enough current policy/configuration context for an Organizer to understand setup coherence and readiness consequences.

A policy edit changes source truth. It does not directly write readiness.

# Optional preparation capabilities

Award definition, materials, Export or Publication preparation are not universal Competition Ready gates merely because PF-01 supports those capabilities.

Where policy/profile makes one required, it may contribute to readiness. Otherwise absence means optional capability unused, not setup failure.

Award definition remains distinct from Award conferral or official outcome authority.

# Competition Readiness

Competition Readiness is a derived projection answering:

> **Do current authoritative preparation sources satisfy the conditions required to permit `Competition.markReady`?**

It is not editable state.

Relevant source categories may include, according to Competition configuration/policy:

- required Competition details;
- valid active Teams;
- current Division assignment where Division applies;
- active Judge-facing Aliases under blinded policy;
- legitimate authoritative Evaluation Basis;
- required Evaluation Policy/configuration;
- required participation/grouping preparation conditions;
- explicitly required optional/profile configuration;
- absence of blocking contradictions or incomplete source conditions.

A readiness representation must distinguish:

```text
blocking condition
warning / operational caution
optional capability not configured
not applicable for this Competition profile
unknown / stale source knowledge
```

A warning may coexist with readiness when policy permits proceeding.

Acknowledging, hiding or dismissing a blocker does not repair source truth.

# Source-directed remediation

When readiness is false, the experience should identify the authoritative source condition and legitimate source action where current authority permits one.

Examples:

```text
required Alias missing
  → act on Alias
  ≠ check off "Alias ready"

Rubric definition invalid
  → act on Rubric
  ≠ override readiness

Panel composition shortfall
  → change Panel/composition facts or invoke a specifically permitted governed exception
  ≠ mark the Panel compliant
```

Readiness items therefore remain projections, not manually closable tasks.

# Explicit Mark Competition Ready

Readiness becoming true makes `Mark Competition Ready` semantically eligible; it does not invoke it automatically.

```text
Competition Readiness = satisfied
  → Mark Competition Ready may be available

Organizer invokes Mark Competition Ready
  → deliberate lifecycle commitment

successful Competition.markReady
  → Competition = Ready
```

The action should be named/explained so its lifecycle consequence is clear rather than hidden behind generic language such as `Complete setup`.

Successful feedback confirms that the Competition is now `Ready`, not merely that preparation appears complete.

# Ready-state invalidation

While Competition is `Ready`, a source change that introduces a blocking readiness condition causes readiness to recompute and current composition system-triggers `Competition.returnToDraft`.

The representation must explain this as source-driven lifecycle invalidation:

```text
source changed
  → readiness became blocking
  → Competition returned to Draft
```

It is not a manually cleared checkbox, deletion of prior preparation or claim that prior Ready state never existed.

Warning-only changes do not force the transition.

After Competition becomes Active, readiness degradation does not roll lifecycle back to Draft; later workstreams own live operational/correction mapping.

# Ready is not Active

The experience must preserve the separate lifecycle commitments:

```text
Draft
  → markReady
  → Ready
  → activate
  → Active
```

Activation remains a distinct coordinated action with its own current authority/readiness conditions.

# Judge-safe preview

Preparation may provide a Judge-safe preview to validate intended blinded representation before live judging.

The preview represents what a Judge would be permitted to perceive, not the Organizer's ordinary sensitive visibility.

It may include, where appropriate:

- Alias + Division;
- explicitly Judge-safe Team attributes;
- Judge-facing instructions;
- the relevant working/authoritative Rubric context with currentness identified when material.

It must not:

- create Judge Participation;
- grant Judge Access;
- begin an Evaluation Occurrence;
- establish an Evaluation Obligation;
- create a Scorecard;
- expose peer results/standings;
- make a working Rubric appear authoritative.

# Preparation action mapping

Current application-action classes remain authoritative:

| Subject | Preparation-facing mapping |
| --- | --- |
| Competition | create/update direct; markReady coordinated; returnToDraft direct/system reaction; activate remains separate coordinated action |
| Team | create/update direct; withdraw/restore controlled direct |
| Division | define/update/assign direct; retire/correct controlled direct |
| Alias | assign/replace/retire controlled direct |
| Participation | enroll/checkIn/update/withdraw direct; activate coordinated; restore exceptional coordinated |
| Panel | planning/membership/capacity direct; retire/restore controlled direct |
| Rubric | working configuration/validation direct; authoritative Version establishment coordinated |
| Versioning / Provenance | composition-only participants; no generic administration |
| Access | composition-only/system guard |
| Readiness | derived only; no write action |
| Award | definition direct; recognition/conferral mapped later |

No composition-only or intentionally unavailable action becomes a setup control for interface convenience.

# Availability and feedback

Preparation must preserve materially different unavailability causes where they change the legitimate next action, such as:

- wrong Competition/Participation context;
- denied Access;
- incompatible Competition lifecycle;
- missing dependent source state;
- invalid Rubric definition;
- stale expected-current authority for consequential version/correction work;
- intentionally unavailable generic administration.

Feedback should confirm the semantic result actually established.

Preserve examples such as:

```text
Team created != competitor fully ready
Judge added to Panel != evaluation responsibility established
Rubric validated != authoritative basis established
authoritative Rubric Version established != Competition Ready
readiness satisfied != lifecycle Ready
lifecycle Ready != Active
```

# Structural representation obligations

Any downstream representation must preserve these properties:

1. current Competition/lifecycle is intelligible where configuration meaning depends on it;
2. independent source ownership remains distinguishable;
3. preparation may proceed non-linearly;
4. blockers, warnings, optional and not-applicable states are distinguishable;
5. readiness appears derived rather than writable;
6. `Mark Competition Ready` remains separate from readiness calculation;
7. Ready remains separate from Active;
8. Team identity / Team Name / Alias do not collapse;
9. Panel planning does not imply judging responsibility;
10. working Rubric does not appear authoritative merely because it is saved/previewed;
11. Judge-safe preview does not create Judge authority;
12. remediation points to natural source owners rather than mutable checklist rows.

These obligations do not prescribe dashboards, steppers, tabs, routes, page hierarchy, components or implementation technology.

# Boundaries / handoff

Operating-context and multi-capacity semantics remain owned by [Experience Context and Participation Modes](context-role-modes.md).

Judge-entry readiness remains owned by [Judge Entry, Participation & Readiness Mapping](judge-onboarding.md).

Detailed Evaluation Occurrence / Evaluation Obligation / Scorecard action, availability and feedback mapping belongs to **013-E**.

Temporal correction/history mapping belongs to 013-F; live operations to 013-G; official outcome mapping to 013-H; external representation/release to 013-I; accessibility/degraded parity to 013-J.

See [Phase 013 Mapping Authority Baseline](mapping-authority-baseline.md), [Readiness](../mechanisms/readiness.md), and [Application Action Surface](../synchronizations/application-action-surface-composition.md).

---
type: Project Context Reconciliation
title: 010-B — Current Project Mandate, Actors, Outcomes, Scope, Constraints & Evidence Reconciliation
description: Reconciles MUDAC's current project/intake truth independently of the incumbent Concept catalog, preserving evidenced live-competition context while separating product decisions, assumptions, open questions, downstream delivery constraints and historical solution structure.
status: stable
tags: [phase-010, jackson, project-context, intake, actors, scope, constraints, evidence]
sources:
  - resource: 010-A-phase-intent-evidence-reuse-gap-closure-subphase-planning.md
  - resource: ../001-concept-design/001-A-purpose-boundary-success.md
  - resource: ../001-concept-design/001-B-actors-roles-authorities-participation.md
  - resource: ../001-concept-design/001-C-lifecycle-critical-scenarios.md
  - resource: ../001-concept-design/001-D-judging-anonymity-evaluation-semantics.md
  - resource: ../001-concept-design/001-G-experience-accessibility-resilience.md
  - resource: ../007-design-refinement/007-B-concept-completeness-independence-genericity-audit.md
  - resource: ../007-design-refinement/007-H-cross-layer-design-completeness-residual-semantic-risk-jackson-methodology-exit-readiness-audit.md
  - resource: ../canonical/governance/design-implementation-boundary.md
  - resource: ../canonical/governance/downstream-authority-quarantine.md
generated: { by: openai/gpt-5.6-sol, at: 2026-09-11T13:33:00-05:00 }
---

# Purpose

Establish one current project/intake baseline for MUDAC before Phase 010-C revalidates purpose, need, success and tension.

010-B deliberately asks a pre-Concept question:

> What project is MUDAC currently trying to design, for whom, in what environment, with what intended outcomes, boundaries and constraints, independent of whether the current sixteen-Concept catalog is ultimately retained?

The objective is not to recreate Phase 001. It is to reconcile the strongest existing evidence into current truth while removing accidental authority from solution-shaped language, later architecture and implementation planning.

# Evidence classification used by this reconciliation

Material claims are classified as one of:

- **Evidenced context** — stable facts about the competition setting or affected parties supported by repeated design evidence.
- **Current product decision** — an explicit project boundary or product-position choice currently intended to govern design.
- **External / operational constraint** — a condition the product must tolerate or respect without implying a Concept or implementation mechanism.
- **Working assumption / hypothesis** — plausible current framing that remains challengeable by later design work.
- **Open question** — unresolved matter that later methodology work must answer or preserve as uncertainty.
- **Historical/downstream candidate** — prior architecture, implementation or solution structure that may inform later work but cannot establish Concept Design truth.

# Reconciled project mandate

MUDAC is a design-governed software effort supporting the **operational judging and outcome lifecycle of a live student data competition**.

The current project boundary centers on enabling volunteer Judges and competition Organizers to conduct, preserve, reconcile and explain independent evaluation under real event-day constraints, while protecting bias-sensitive identity information and maintaining trustworthy historical evidence.

This mandate includes operational preparation, live evaluation, paper/electronic continuity, correction, result formation and controlled external representation. It does **not** imply that the current nouns used to implement that capability—such as Panel, Judging Encounter, Scorecard, Access, Export or Publication—must survive candidate rediscovery as Concepts.

# Competition context that survives reconciliation

The following are retained as **evidenced context** rather than as Concept decisions:

- the product is for a live academic/student data competition;
- student Teams present work that volunteer Judges evaluate;
- evaluation is multi-perspective and individual Judge judgment matters independently;
- Organizers coordinate the event, observe operational state and establish official outcomes;
- institutional identity can bias judging and therefore needs controlled disclosure;
- judging may occur repeatedly across multiple evaluator/Team situations during an event;
- the event is time-bounded and operationally dynamic;
- event conditions may include first-time users, personal phones, interruptions, poor connectivity, unsuitable devices and accessibility needs;
- paper must remain a supported continuity/accommodation path rather than an invalid second-class source;
- authoritative evaluation and official outcomes may need correction without destroying historical truth;
- external/print representations can matter operationally and after result finalization.

# Actors, stakeholders and materially affected parties

## Direct application actors

### Judge

A Judge is a human evaluator participating in a particular competition context.

Current intake-level facts:

- Judges may be first-time or returning volunteers;
- they need very low administrative friction during the event;
- they must be able to form and record their own judgment independently;
- their evaluation records and notes are privacy-sensitive;
- expertise/perspective may matter to competition composition but does not automatically imply different software authority.

010-B does not freeze a `Participation`, `Identity`, `Access`, session or role model. Those are later conceptual/realization questions.

### Organizer

An Organizer is a human responsible for competition preparation, live operation, exception handling, reconciliation and official closeout.

Current intake-level facts:

- Organizers need broad situational awareness across the event;
- they need to recover from incomplete or exceptional judging without silently inventing evidence;
- they need to explain how outcomes were formed;
- they may capture or verify paper-originated information without thereby becoming the original evaluator;
- Organizer authority is competition-operational rather than a synonym for unlimited technical privilege.

### Technical administrator / support operator

A technical administrator or support operator may operate the application environment.

Current intake-level fact:

- technical operational power must not automatically become authority to alter competition judgments or outcomes.

010-B does not freeze any authentication, infrastructure or operator-authorization mechanism.

## Materially affected non-actors

### Student Team

Student Teams are currently materially affected competition participants but not direct application users in the initial product boundary.

They depend on:

- fair evaluation;
- protection from inappropriate identity bias;
- sufficient and comparable judging treatment;
- corrections that do not erase the evidentiary history supporting their outcome.

The current project does not require student accounts, dashboards, registration or submission workflows.

### External recipients of released material

People who receive printable or deliberately released competition material are affected by whether representations are accurate, appropriately disclosed and tied to an identifiable source state.

They are not currently modeled as direct application actors, and 010-B does not assume a rich public-results application.

## Organizational stakeholders not yet established as separate software roles

The repository does not currently establish a distinct sponsor, faculty-advisor, institutional representative or event-leadership software actor beyond the Organizer/technical-operator boundary.

If 010-C identifies independent needs for such parties, they should be introduced as affected-party evidence rather than inferred from organizational titles.

# Intended outcomes retained for purpose revalidation

010-B retains the following as **outcome directions**, not yet as final Jackson purpose decomposition:

1. volunteer evaluators can record independent judgment without the software becoming the center of the judging interaction;
2. Organizers can coordinate a live competition with less manual reconciliation and uncertainty;
3. official competition outcomes can be traced back to the evaluation evidence and rules that produced them;
4. bias-sensitive Team identity is not exposed to Judges merely for operational convenience;
5. missing or incomplete evaluation is distinguishable from a deliberate low score;
6. paper and electronic judging can converge on the same evaluation meaning;
7. interruption, poor connectivity or device problems do not unnecessarily destroy valid judging work;
8. corrections preserve authorship, provenance and historical truth rather than silently rewriting the past;
9. live/provisional information remains distinguishable from official/finalized information;
10. printable or released representations do not silently promote provisional or unauthorized information into official truth.

010-C must turn these directions into need-focused, evaluable purpose obligations and expose tensions among them.

# Current capability scope

The following capability areas remain **inside the current project boundary** at intake level:

- establish and govern a competition's judging context and policies;
- establish competitor entries and appropriate competition-facing identity;
- prepare and admit volunteer evaluators into the current event context;
- organize evaluators for live judging activity;
- define the evaluation basis/rubric used for judgment;
- record independent evaluator judgments and qualitative evidence;
- preserve incomplete/draft work without confusing it with authoritative evaluation;
- support electronic and paper-originated judging under compatible semantics;
- expose live operational completion, gaps and exceptions to authorized organizers;
- preserve correction, replacement and historical evidence where competition meaning changes;
- derive and reconcile competition-level evaluation, coverage and ordering information;
- support organizer-defined recognition/awards in addition to simple ordering;
- establish an official competition outcome after reconciliation;
- generate stable printable/external representations from identified source state;
- deliberately release or withdraw external representations where the product's disclosure rules permit it.

This scope describes required capability. It does not assign those responsibilities to the incumbent Concepts.

# Explicit current non-goals

The following remain outside the current baseline unless a later design change reopens scope:

- student registration or student account experience;
- student submission management;
- dataset hosting/distribution;
- notebook, analytics or ML execution infrastructure;
- faculty-advisor management;
- general event ticketing or marketing;
- prize-payment/disbursement;
- general-purpose competition-management software beyond the judging/outcome boundary;
- advanced Judge calibration/normalization as a default product function;
- formal room/time-slot scheduling optimization;
- notification systems as a required core capability;
- a rich public-results portal distinct from controlled representation/release capability.

Formal Stage/Round abstractions and other competition-format extensions remain possible future scope; Phase 012 will determine coherent product-family/subset implications rather than 010-B assuming them.

# Pre-Concept terminology retained for communication

Some domain terms are stable enough to use descriptively before candidate selection:

- **Team** — the student competitor/group being evaluated;
- **Judge** — a human evaluator;
- **Organizer** — a human operating/governing the competition;
- **Panel** — ordinary competition language for Judges evaluating together;
- **Rubric** — the declared basis/criteria for evaluation;
- **Scorecard** — ordinary repository language for one Judge's recorded evaluation;
- **Division** — an organizer-defined competitive grouping where the competition uses one.

The current repository term **Judging Encounter** is useful shorthand for a bounded occurrence in which evaluators judge a Team, but its status as a distinct Concept is not an intake fact and remains challengeable in 010-D–G.

Likewise `Identity`, `Participation`, `Alias`, `Access`, `Versioning`, `Provenance`, `Export` and `Publication` are incumbent Concept names, not prerequisites of the project definition.

# Genuine product and operational constraints

## Live-event constraint

The product must function in a time-bounded event where delays, substitutions, incomplete work and rapid exception handling matter.

## Independent-judgment constraint

The product must not require Judges to consume peer scores/notes or live competition standings in order to perform their own evaluation.

## Bias-sensitive disclosure constraint

Institutional/administrative Team identity must be controllable so ordinary judging does not reveal information the competition intends to shield.

## Accessibility constraint

The electronic path must not assume perfect vision, color perception, fine motor control, hearing, one specific device or touch-only interaction.

## Degraded-connectivity/device constraint

Poor or absent connectivity, interruption and device failure are expected environmental conditions rather than impossible edge cases.

## Paper-continuity constraint

The event must be able to continue through a paper-supported judging path while preserving the same underlying evaluation meaning and later traceability.

## Historical-truth constraint

Meaningful corrections must not require destructive rewrite of prior authoritative evaluation/outcome history.

## Explainability/traceability constraint

Competition-level outcomes must remain explainable from their underlying evaluation evidence and declared rules rather than existing only as opaque totals.

## Authority-separation constraint

Technical system privilege must not silently become authority to author or revise competition judgment.

# Downstream delivery constraint that does not constrain Concept Design

Prior project intent states an eventual delivery environment of:

```text
GitHub → GitHub Actions → AWS ecosystem
```

010-B retains this only as a **downstream project/delivery constraint**. It does not justify or require any Concept, Concept boundary, state machine, UI mapping, authentication mechanism, database shape, service topology or AWS service.

The previously selected Node/TypeScript/Fastify/React/PostgreSQL/OpenTofu substrate is historical executable fact under the 006-D freeze, not project-intake authority.

# Historical assumptions demoted from intake truth

The following kinds of earlier statements are not accepted as project-context facts merely because they appear in Phase 001 or downstream work:

- exact lifecycle-state names;
- exact one-record-per-X cardinalities that arise from the incumbent Concept model;
- exact equal-weight aggregation arithmetic;
- exact Panel/Team repeat limits;
- exact authentication/session/invitation mechanisms;
- QR-code, magic-link or provider choices;
- database/version/outbox/projection structures;
- frontend routes, page modes, cache/offline technologies or component structure;
- source/package/service boundaries;
- specific AWS resources;
- any claim that a mechanism is a Concept because implementation has state for it.

These may later be re-established by the appropriate methodology phase, but 010-B does not inherit them as intake truth.

# Working assumptions carried forward explicitly

The following remain useful but challengeable assumptions for later phases:

- Organizer and Judge are the only principal direct product-user modes required by the baseline, apart from narrow technical operation/support;
- Student Teams remain non-user participants in the current product boundary;
- competitive grouping/division structure is configurable rather than universal in exact form;
- judging commonly involves multiple perspectives, but specific expertise categories and quotas are policy choices rather than permanent product truth;
- controlled external release is part of the present boundary, while a rich public portal is not;
- event scheduling may exist outside the product or remain lightweight unless later purpose/dependence work establishes a stronger need.

# Open questions intentionally handed forward

010-B does not resolve:

- the final decomposition of product purpose and affected-party need;
- whether any additional affected party has a distinct software-relevant purpose;
- whether every current capability area belongs in one minimal product variant;
- which incumbent Concepts survive rediscovery;
- whether Panel, Judging Encounter, Division, Alias, Award, Export or Publication are optional in coherent application variants;
- how purposes should be distributed across Concepts;
- detailed aggregation, coverage, tie, award or disclosure policies;
- exact retention periods or regulatory requirements not currently evidenced;
- final interaction mappings;
- architecture or implementation realization.

These are assigned to 010-C onward rather than being guessed here.

# Evidence reconciliation summary

| Prior material | 010-B treatment |
| --- | --- |
| 001-A product boundary and live judging context | **Retain**, but strip Concept-shaped implementation from intake authority. |
| 001-B actor/role evidence | **Retain** Judge/Organizer/technical-operator/Team distinctions as context; do not freeze Identity/Participation/Access realization. |
| 001-C lifecycle/critical scenarios | **Reuse as evidence** of event dynamics, correction, paper and outcome needs; exact lifecycle model is later design. |
| 001-D evaluation/anonymity evidence | **Retain** independent judgment, missing≠zero, disclosure and explainability needs; exact scoring policy is later policy/design. |
| 001-G accessibility/resilience | **Retain strongly** as operational/environmental constraints; implementation mechanisms remain deferred. |
| Current sixteen-Concept catalog | **Incumbent hypothesis only**; not evidence that intake requires those boundaries. |
| 007-B/007-H later audits | **Reuse for discovered scope pressure/counterexamples**, not as proof that closure/catalog is final. |
| Phase 005 architecture | **Quarantined downstream candidate**. |
| Phase 006/008 implementation planning | **Historical/downstream candidate**; not current project-definition authority. |
| 006-D executable substrate | **Frozen historical fact** only. |

# Canonical reconciliation

010-B creates one natural current owner for this material:

- [`../canonical/project/mandate-context.md`](../canonical/project/mandate-context.md)

The phase record preserves the detailed reconciliation rationale. The canonical Project Context owner remains concise current truth and should be updated when later design evidence changes the project framing.

# 010-B exit test

010-B may pass only if:

- MUDAC can be described without relying on the incumbent Concept catalog;
- principal direct actors and materially affected parties are explicit;
- intended outcomes are visible without prematurely completing Phase 010-C purpose analysis;
- current scope and non-goals are explicit;
- operational/product constraints are distinguished from downstream realization choices;
- assumptions and open questions are visible;
- historical architecture/implementation cannot masquerade as intake truth;
- 010-C can begin from current repository knowledge alone.

All conditions are satisfied.

# Decision

**PASS — 010-B is complete.**

The current project/intake baseline is sufficiently reconciled for purpose revalidation. No Concept is added, removed, retained or rejected by this subgroup merely because of the project context reconciliation.

# Handoff

Proceed to:

> **010-C — Purpose, Need, Success, Tension & Purpose-to-Concept Traceability Revalidation**

010-C should use the canonical Project Context owner as its starting context and treat the incumbent Concept catalog only as a traceability target to be tested, not as the source from which purposes are derived.

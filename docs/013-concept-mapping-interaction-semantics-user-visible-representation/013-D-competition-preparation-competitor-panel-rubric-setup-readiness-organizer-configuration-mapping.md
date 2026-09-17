---
type: Phase Design Record
title: 013-D — Competition Preparation, Competitor/Panel/Rubric Setup, Readiness & Organizer Configuration Mapping
description: "Maps MUDAC Organizer preparation into user-visible configuration, source-state, readiness, preview, action-availability and lifecycle-commitment semantics without turning preparation into a wizard, checklist state machine, hidden coordinator or implementation architecture."
status: stable
tags: [phase-013, jackson, mapping, organizer, preparation, competition, team, division, alias, panel, rubric, readiness]
sources:
  - resource: 013-C-context-identity-participation-access-bias-control-judge-entry-mapping.md
  - resource: ../canonical/experience/mapping-authority-baseline.md
  - resource: ../canonical/experience/organizer-preparation.md
  - resource: ../canonical/concepts/competition.md
  - resource: ../canonical/concepts/team.md
  - resource: ../canonical/concepts/division.md
  - resource: ../canonical/concepts/alias.md
  - resource: ../canonical/concepts/panel.md
  - resource: ../canonical/concepts/rubric.md
  - resource: ../canonical/concepts/participation.md
  - resource: ../canonical/synchronizations/competition-participation-access.md
  - resource: ../canonical/synchronizations/evaluation-occurrence-obligation.md
  - resource: ../canonical/synchronizations/evaluation-basis-scorecard-authority.md
  - resource: ../canonical/synchronizations/application-action-surface-composition.md
  - resource: ../canonical/mechanisms/readiness.md
  - resource: ../canonical/policies/evaluation-policy.md
  - resource: ../canonical/policies/panel-composition.md
  - resource: ../canonical/policies/anonymity-disclosure.md
  - resource: ../canonical/policies/operational-exception-governance.md
  - resource: https://github.com/SethDKelly/Base/blob/main/docs/phases/007/concept-mapping-contract.md
---

# Purpose

Map how an Organizer can understand and prepare a MUDAC Competition before live evaluation begins while preserving the current Concept model.

013-D focuses on:

- Competition setup and lifecycle context;
- competitor establishment through Team, Division and Alias;
- Judge Participation and Panel planning where preparation needs them;
- Rubric and authoritative Evaluation Basis preparation;
- Evaluation Policy and other configuration that materially affects readiness;
- source-derived Competition Readiness;
- explicit `Mark Competition Ready` lifecycle commitment;
- readiness invalidation and return-to-Draft meaning;
- Judge-safe preview of prepared competitor/evaluation context;
- action availability and result/feedback semantics for preparation work.

The workstream does **not** prescribe a setup wizard, page tree, component layout, form implementation, validation library, autosave behavior, API, persistence model, event bus, or runtime orchestration.

# Decision

**COMPLETE — PASS. Proceed to 013-E.**

```text
013-A START GATE                              COMPLETE — READY
013-B AUTHORITY / CORPUS BASELINE            COMPLETE — PASS
013-C CONTEXT / JUDGE ENTRY MAPPING          COMPLETE — PASS
013-D ORGANIZER PREPARATION MAPPING          COMPLETE — PASS
ORGANIZER-PREPARATION OWNER REWRITTEN        YES
PREPARATION AS MANDATORY WIZARD              PROHIBITED
READINESS AS EDITABLE CHECKLIST STATE        PROHIBITED
READINESS == COMPETITION READY LIFECYCLE     PROHIBITED
READY == ACTIVE                              PROHIBITED
PANEL MEMBERSHIP == RESPONSIBILITY           PROHIBITED
WORKING RUBRIC == AUTHORITATIVE BASIS         PROHIBITED
JUDGE-SAFE PREVIEW GRANTS JUDGE AUTHORITY    PROHIBITED
NEW COORDINATOR / WORKFLOW CONCEPT REQUIRED  NO
PHASE-010 REOPEN REQUIRED                    NO
PHASE-011 REOPEN REQUIRED                    NO
PHASE-012 REOPEN REQUIRED                    NO
NEXT                                          013-E
ARCHITECTURE / IMPLEMENTATION                SUSPENDED
```

# 1. Governing preparation model

Preparation is a **view over independent authoritative sources plus legitimate actions on those sources**.

It is not a hidden `Setup`, `Workflow`, `Checklist`, `Draft Configuration`, or `Competition Builder` Concept.

The mapping model is:

```text
Competition context
  + competitor sources
  + evaluator/grouping sources
  + evaluation-basis / policy sources
  + other policy-required preparation sources
    ↓
source-derived Competition Readiness
    ↓
explicit Organizer Mark Competition Ready
    ↓
Competition lifecycle = Ready
```

The arrows mean explanation/composition, not ownership transfer or required navigation sequence.

The Organizer may prepare sources in any legitimate order. Dependencies constrain semantic validity, not a mandatory screen sequence.

# 2. Preparation context and scope

Before consequential configuration work, the Organizer must be able to determine which Competition is being prepared and which Organizer Participation context is active when ambiguity could change authority or disclosure.

013-C remains authoritative for Identity / Participation / Access context mapping.

013-D adds the preparation-specific rule:

> **A preparation representation may aggregate many source domains, but every consequential edit or lifecycle action must remain attributable to its natural semantic owner and current Competition scope.**

A preparation area may therefore summarize Teams, Divisions, Aliases, Judges, Panels, Rubric basis, policies and readiness without becoming the owner of those states.

# 3. Non-linear preparation

MUDAC preparation is deliberately non-linear.

The experience must not imply that a valid Competition can only be configured through one fixed sequence such as:

```text
Competition → Teams → Judges → Panels → Rubric → Awards → Ready
```

An Organizer may legitimately establish sources in a different order while the Competition remains Draft.

A representation may use explanation order, grouping, progressive disclosure, recommendations or dependency-aware prompts, but:

```text
dependence order != navigation order
preparation completeness != wizard completion
```

If one action genuinely requires another source fact, the unavailable action should explain the relevant semantic precondition rather than inventing an artificial step number.

# 4. Competition setup mapping

Competition configuration must make the current Competition occurrence and lifecycle state intelligible.

Material preparation questions include:

```text
Which Competition occurrence am I configuring?
What descriptive/scheduled event context is current?
Is the Competition Draft or Ready?
Which lifecycle action is currently legitimate?
What changed since the Competition was marked Ready, if anything?
```

`Competition.create` and `Competition.updateDetails` remain direct application actions.

Updating Competition details does not itself mark the Competition Ready, activate it, change Team/Panel/Rubric state, or create judging work.

Historical lifecycle transitions must not be flattened into a generic setup-complete indicator.

# 5. Competitor preparation: Team, Division and Alias

The Organizer needs a truthful preparation view of competitor structure without collapsing its owners.

## Team

Team owns the stable administrative competing unit and its current participation status.

Preparation may expose:

- Team existence/current status;
- necessary Organizer-facing administrative attributes;
- disclosure-controlled descriptive attributes;
- whether the Team is Active or Withdrawn.

Team Name remains descriptive metadata and must not be presented as the Judge-facing Alias.

## Division

Division owns competitive cohort definition and current Team assignment.

Preparation must make it possible to distinguish:

```text
Team exists
  != Team has valid current Division assignment
```

where Division is part of the configured PF-01 competition profile.

A correction to Division assignment is a semantic correction, not merely moving a row between visual groups. Detailed post-use correction/history representation belongs to 013-F.

## Alias

Alias owns the scoped Judge-facing alternate identity.

For blinded judging, preparation must make clear whether an active Judge-facing Alias exists for each Team where policy requires one and whether scope/uniqueness requirements are satisfied.

Preparation must preserve:

```text
Team administrative identity
  != Team Name
  != Alias
```

An Alias replacement/retirement after use has historical consequences; 013-D may signal that the action is consequential but defers detailed temporal mapping to 013-F.

# 6. Judge Participation and Panel planning

Preparation may include expected/current Judge Participation and Panel planning, but must preserve the separations established in 013-C and Phase 011.

## Judge Participation

Organizer preparation may need to know whether expected Judges have current Competition-scoped Judge Participations and relevant event-specific attributes such as expertise.

However:

```text
Identity exists
  != Judge Participation exists
  != Participation is checked in/active
  != Panel membership
```

Preparation must not treat technical user/account existence as Judge enrollment.

## Panel

Panel owns reusable intended evaluator grouping and optional composition-capacity assignments.

Panel planning may answer:

```text
Which Judges are intended to work together?
Which current composition capacities are represented?
Is the planned composition Compliant, Degraded or Noncompliant under policy?
```

But Panel membership does **not** establish:

- actual Evaluation Occurrence participation;
- Evaluation Obligation responsibility;
- Team-specific evaluation assignment;
- Scorecard existence;
- current Access to evaluation material.

Final day-of-event staffing is operational readiness rather than a universal structural prerequisite for `Competition.markReady`. A competition may legitimately be Ready while later event-day Panel adjustments are still expected, where current policy permits that profile.

A governed Panel-composition exception preserves the shortfall. It must not be represented as though the Panel became objectively compliant.

# 7. Rubric preparation and authoritative Evaluation Basis

Organizer preparation must distinguish **working Rubric definition** from **authoritative Evaluation Basis**.

A Rubric may move through working definition/configuration and validation actions without yet becoming the exact authoritative Version used for evaluation.

Preserve:

```text
Rubric Draft / working definition
  != validated definition
  != prepareForUse result by itself
  != authoritative immutable Rubric Version
  != occurrence-bound Evaluation Basis
```

The coordinated **Establish Authoritative Rubric Version** action is the application mapping for committing an immutable authoritative Rubric basis with Versioning/Provenance participation.

Preparation must make the semantic consequence intelligible:

- an authoritative snapshot is being established;
- later semantic Rubric changes require a successor Version rather than rewriting the authoritative snapshot;
- historical evaluation remains bound to the exact basis actually used.

Generic Versioning or Provenance controls remain unavailable.

Detailed Judge interaction with the selected basis belongs to 013-E.

# 8. Evaluation Policy and preparation policy state

Evaluation Policy configures evidence eligibility, Coverage, aggregation, ranking, precision, tie behavior, Rubric compatibility and related interpretation used downstream.

Preparation must expose enough policy context for an Organizer to understand whether current setup is coherent and what policy choices materially affect readiness or later evaluation/outcome interpretation.

This does not require every policy to be rendered as one monolithic configuration object.

A policy edit is not a readiness edit. Readiness recomputes from the changed authoritative source.

Once judging begins, outcome-affecting policy must remain reconstructible/versioned/provenanced under its canonical policy contract. 013-D does not define that storage/implementation mechanism.

# 9. Award definitions and other optional preparation capabilities

Award definitions may be prepared before judging, but Award presence is not universal to PF-01 and Award definition is not Award conferral.

Therefore:

```text
Award definition configured
  != Award conferred
  != result recognized
  != Competition official
```

Whether an Award definition is required for readiness depends on declared Competition policy/profile, not on the mere existence of the Award Concept in PF-01.

Similarly, materials/Export/Publication capabilities may be prepared or absent without becoming universal `Competition Ready` gates unless current policy explicitly makes a particular artifact a prerequisite. Detailed external-representation mapping belongs to 013-I.

# 10. Competition Readiness mapping

`Competition Readiness` is a derived projection answering:

> **Do the current authoritative preparation sources satisfy the application/policy conditions required to permit `Competition.markReady`?**

It is not Competition lifecycle state and is not writable.

Material source categories may include, according to current Competition configuration/policy:

- Competition details required for the occurrence;
- valid active Team structure;
- current Division assignments where Division applies;
- active Judge-facing Aliases under blinded-judging policy;
- legitimate evaluation basis / authoritative Rubric Version;
- required Evaluation Policy/configuration;
- required Participation/grouping preparation conditions;
- policy-required Award or operational configuration where explicitly applicable;
- absence of blocking contradictions/incomplete source conditions.

The representation must distinguish:

```text
blocking condition
warning / operational caution
optional capability not configured
not applicable under this Competition profile
unknown / stale source knowledge
```

A warning may remain while readiness is satisfied when policy allows proceeding.

Acknowledging, hiding or dismissing a blocker does not make readiness true.

# 11. Readiness explanation and source-directed remediation

A readiness representation should answer at least:

```text
Is Mark Competition Ready currently permitted?
If no, which authoritative source condition is blocking it?
What legitimate source action could resolve that condition, if one exists for this Organizer?
Which conditions are warnings rather than blockers?
Which optional capabilities are simply unused?
```

A blocker is therefore a **projection of source truth**, not an independently closable task.

Examples:

```text
missing required Alias
  → act on Alias source
  ≠ check off "Alias ready"

invalid Rubric definition
  → act on Rubric source
  ≠ override readiness

Panel composition shortfall
  → change Panel/composition facts or invoke a specifically permitted governed exception
  ≠ mark composition compliant
```

This closes MAP-R14 for Competition preparation: readiness must not become editable workflow state.

# 12. Explicit `Mark Competition Ready`

When Competition Readiness is satisfied, the Organizer may deliberately invoke the coordinated application action **Mark Competition Ready**.

The mapping must preserve:

```text
readiness true
  = action may legitimately be available

Organizer invokes Mark Competition Ready
  = lifecycle commitment intent

successful Competition.markReady
  = Competition lifecycle becomes Ready
```

Readiness becoming true does **not** automatically mark the Competition Ready.

A preparation representation must not use a generic `Complete setup` action if that wording obscures the actual lifecycle consequence.

Success feedback must confirm the Competition is now `Ready`, not merely that a checklist finished.

Failure/unavailability feedback should identify the semantic cause category without inventing authority or leaking protected information.

# 13. Ready-state invalidation

When a Competition is `Ready`, a source change may cause current Competition Readiness to become blocking.

Current composition then system-triggers `Competition.returnToDraft`.

The user-visible semantics are:

```text
source changed
  → current readiness recomputed
  → blocking condition now exists
  → Competition returns from Ready to Draft
```

This must not be represented as:

- an Organizer forgetting to re-check a box;
- a generic workflow rollback;
- the system deleting prior preparation;
- historical `Ready` never having occurred.

The experience should make the source reason intelligible enough for an Organizer to understand what invalidated readiness and what current action is legitimate.

A warning-only change does not force return to Draft.

After Competition activation, later readiness degradation does not roll Competition backward to Draft; it becomes live operational/correction pressure handled in later workstreams.

# 14. Ready is not Active

`Competition = Ready` means preparation has been explicitly committed under satisfied readiness conditions.

It does not mean live judging has begun.

Preserve:

```text
Draft
  → explicit markReady
  → Ready
  → separate coordinated activate
  → Active
```

`Activate Competition` is a distinct coordinated action with its own live-activation readiness and authority conditions.

013-D must not collapse `Ready` and `Active` for convenience. Detailed event-day activation/live-operations representation is completed in 013-G.

# 15. Judge-safe preview

Preparation should support a **Judge-safe preview** when useful for validating blinded representation and evaluation context before live judging.

The preview answers a representation question such as:

> **What would a Judge be permitted to perceive under the intended Judge-safe disclosure posture?**

It may include, as appropriate:

- Alias + Division competitor presentation;
- disclosure-safe Team attributes explicitly permitted for Judge use;
- relevant Rubric/evaluation instructions or exact intended authoritative basis;
- omission of protected administrative Team identity and optional Team Name by default.

Preview must not:

- create Judge Participation;
- grant Judge Access;
- start an Evaluation Occurrence;
- establish an Evaluation Obligation;
- create a Scorecard;
- expose peer scores/standings;
- imply that a working Rubric draft is already authoritative.

The preview should clearly represent which source/basis state it reflects when currentness matters.

# 16. Action-surface mapping for preparation

013-D maps only current application actions already established by Phase 011.

| Preparation subject | Material application-action mapping |
| --- | --- |
| Competition | `create`, `updateDetails` direct; `markReady` coordinated; `returnToDraft` direct/system-triggered; `activate` remains distinct coordinated action |
| Team | create/update direct; withdraw/restore controlled direct |
| Division | define/update/assign direct; retire/correctAssignment controlled direct |
| Alias | assign/replace/retire controlled direct |
| Participation | enroll/checkIn/update/withdraw direct; activate readiness-gated coordinated; restore exceptional coordinated |
| Panel | create/membership/capacity planning direct; retire/restore controlled direct |
| Rubric | working definition/configuration/validation/prepare-for-use direct; authoritative Version establishment coordinated |
| Versioning / Provenance | composition-only participants in authoritative basis establishment; no generic administration |
| Access | composition-only/system guard for protected configuration/disclosure |
| Readiness | derived only; no write action |
| Award | definition actions direct; conferral/revocation/outcome use deferred to 013-H |

No `P` or `X` action becomes a preparation control merely because it could make a UI convenient.

# 17. Availability mapping

A preparation action should be represented as available only when its current semantic preconditions can legitimately be satisfied.

Where an action is unavailable, the experience should distinguish reasons that lead to materially different next actions, for example:

- wrong Competition/Participation context;
- denied Access;
- incompatible Competition lifecycle;
- missing dependent source state;
- invalid working Rubric definition;
- stale expected-current authority for a consequential Version/correction action;
- action intentionally unavailable because the underlying Concept action is composition-only or not generically exposed.

A hidden route or disabled control alone must not be relied upon to explain a consequential semantic distinction.

# 18. Feedback and confirmation semantics

Preparation feedback must identify the semantic result actually established.

Examples:

```text
Team created
  ≠ competitor fully ready

Division assigned
  ≠ historical evaluation context rewritten

Judge added to Panel
  ≠ Judge assigned evaluation responsibility

Rubric validated
  ≠ authoritative basis established

Authoritative Rubric Version established
  ≠ Competition marked Ready

Competition Readiness true
  ≠ Competition lifecycle Ready

Competition marked Ready
  ≠ Competition Active
```

High-consequence corrective actions such as withdrawal, Alias replacement, Division correction or authoritative basis succession must not be made to look like ordinary harmless field edits merely because preparation provides access to them. Detailed correction/history mapping belongs to 013-F.

# 19. Structural mapping obligations

013-D requires only semantic structural constraints, not exact interface structure.

A valid downstream representation must ensure that:

1. Competition scope/lifecycle is intelligible where configuration meaning depends on it.
2. independent source domains remain distinguishable enough to preserve ownership.
3. preparation can be non-linear.
4. blockers, warnings, optional capabilities and not-applicable conditions are distinguishable.
5. readiness appears derived rather than editable.
6. the explicit lifecycle action `Mark Competition Ready` remains distinguishable from readiness calculation.
7. `Ready` remains distinguishable from `Active`.
8. Team administrative identity, Team Name and Alias are not conflated.
9. Panel planning does not imply occurrence participation or responsibility.
10. working Rubric state does not appear authoritative merely because it is previewable.
11. Judge-safe preview does not grant Judge authority.
12. source-directed remediation remains traceable to the actual semantic owner.

No exact dashboard, stepper, cards, tabs, pages, navigation order or component system is authorized by these constraints.

# 20. Mapping-risk closure

013-D materially addresses these Phase-013 risks:

| Risk | 013-D result |
| --- | --- |
| MAP-R03 raw Concept action appears as app action | preparation maps only the established D/C/P/S/X surface |
| MAP-R04 Identity / Participation / Access collapse | 013-C boundary preserved for Organizer preparation |
| MAP-R05 Panel membership / actual participation / responsibility / evidence collapse | Panel preparation explicitly limited to intended grouping |
| MAP-R11 PF-01 profiles appear as separate products | optional Awards/materials/staffing treated as profile/configuration conditions, not products |
| MAP-R13 navigation/role mode appears to create authority | Organizer preparation remains within explicit Participation/Access context |
| MAP-R14 Readiness/Reconciliation/exception projections appear editable | Competition Readiness explicitly derived and source-directed |
| MAP-R15 support/technical privilege appears domain authority | no setup/control path bypasses semantic authority |
| MAP-R16 old Experience boundaries dictate semantic grouping | organizer-preparation owner is rewritten from current Concepts/composition rather than retained verbatim |

Risks concerning active evaluation, correction/history, live reconciliation, officiality, external release and degraded-mode parity remain assigned to 013-E through 013-J.

# 21. Counterexample probes

013-D rejects the following misleading mappings:

## "Setup is 100% complete"

Rejected when the percentage is treated as authoritative source truth or implies a universal ordered checklist. A summary may exist only if its basis and readiness meaning remain explicit.

## "Panel complete" means judging responsibility exists

Rejected. Panel is intended grouping; responsibility is established through Evaluation Occurrence / Evaluation Obligation composition later.

## "Rubric saved" means judges will use it

Rejected. Working Rubric persistence/validity is not an authoritative immutable Evaluation Basis.

## "All green" automatically marks Ready

Rejected. Readiness may enable the explicit Organizer lifecycle commitment but does not perform it.

## Editing after Ready leaves Ready state unchanged

Rejected when the source change creates a blocking readiness condition. Current composition returns Competition to Draft while preserving lifecycle history.

## Judge preview uses Organizer-sensitive identity because Organizer is previewing it

Rejected. A Judge-safe preview represents the intended Judge disclosure posture, not the previewing Organizer's normal visibility.

# 22. Upstream reopen audit

013-D found no missing Concept, action family, synchronization or PF-01 scope rule required to represent preparation faithfully.

```text
Phase 010 Concept-boundary reopen:        NO
Phase 011 synchronization/action reopen:  NO
Phase 012 dependence/scope reopen:        NO
new Workflow/Setup Concept:               NO
new editable Readiness Concept:           NO
new generic Version/Access admin action:  NO
```

The current model is sufficiently specific for preparation mapping.

# 23. Durable canonical output

013-D rewrites:

- `docs/canonical/experience/organizer-preparation.md`

into current Phase-013 mapping authority for Organizer preparation, setup/readiness explanation, readiness-to-lifecycle distinction, source-directed remediation and Judge-safe preview semantics.

Concept definitions, application actions, Readiness truth and policy remain in their existing natural owners and are referenced rather than duplicated as new authority.

# 24. Handoff to 013-E

013-E now receives a prepared mapping context in which:

- Competition/capacity context is already explicit;
- Judge-safe competitor disclosure is already defined;
- Team / Division / Alias distinctions are preserved;
- Panel is understood as intended grouping only;
- authoritative Rubric Version is distinguishable from working Rubric state;
- Competition readiness/lifecycle does not masquerade as evaluation responsibility;
- no Scorecard/evaluation authority has been invented during preparation.

013-E should therefore map the next semantic boundary:

```text
prepared competitor/evaluation context
  → Evaluation Occurrence
  → Evaluation Obligation
  → Judge-visible responsibility/work
  → exact Evaluation Basis
  → Scorecard Draft
  → explicit Finalization
  → truthful availability and feedback
```

without restoring the deprecated `Encounter` abstraction.

# 25. Non-goals retained

013-D does not define:

- setup routes or page hierarchy;
- a wizard/stepper implementation;
- frontend components/forms;
- client state or autosave behavior;
- API/endpoints/messages;
- persistence/schema;
- notification transport;
- authentication/authorization implementation;
- AWS/runtime topology;
- executable UI tests or source code.

# Current state

```text
013-A  COMPLETE — READY
013-B  COMPLETE — PASS
013-C  COMPLETE — PASS
013-D  COMPLETE — PASS
013-E  NEXT
architecture authority: SUSPENDED
implementation planning: SUSPENDED
implementation readiness: NOT READY
implementation authorization: NOT YET
```

---
type: Synchronization Contract
title: Competition Lifecycle, Participation & Contextual Access Composition
description: "Current cross-Concept composition for Identity continuity, Competition-scoped Participation, contextual Access, Competition readiness/activation/completion/resume, Team/Division/Alias readiness contribution, and operating-context isolation after Phase 011-C, with the event-completion Access seam corrected by 014-C."
status: stable
tags: [synchronization, competition, identity, participation, access, readiness, context, phase-011]
sources:
  - resource: ../../011-concept-composition-synchronization/011-C-competition-lifecycle-identity-participation-access-operating-context-composition.md
  - resource: ../../014-familiarity-reuse-genericity/014-C-competition-competitor-grouping-identity-participation-alias-access-familiarity-reuse-audit.md
  - resource: ../concepts/competition.md
  - resource: ../concepts/identity.md
  - resource: ../concepts/participation.md
  - resource: ../concepts/access.md
  - resource: ../mechanisms/readiness.md
  - resource: ../policies/anonymity-disclosure.md
  - resource: ../policies/operational-exception-governance.md
  - resource: ../invariants/judge-independence.md
  - resource: ../experience/judge-onboarding.md
  - resource: ../experience/judge-evaluation.md
  - resource: ../experience/organizer-preparation.md
  - resource: ../experience/context-role-modes.md
  - resource: ../experience/action-authority-traceability.md
generated: { by: openai/gpt-5.6-sol, at: 2026-09-14T01:13:00-05:00 }
---

# Purpose

Define current MUDAC application composition among [Competition](../concepts/competition.md), [Identity](../concepts/identity.md), [Participation](../concepts/participation.md), [Access](../concepts/access.md), and derived [Readiness](../mechanisms/readiness.md) without collapsing their independent ownership.

This document supersedes the current-authority meaning of legacy synchronization contracts 01–04, the readiness half of legacy 05, and the semantic Access-context half of legacy 16. The remaining legacy synchronization body stays pre-011 evidence until its owning Phase 011 subgroup establishes replacement semantics.

014-C later corrected one over-strong Phase-011 composition statement: Event Completed closes broad ordinary live-event Judge capability, but it is **not** a universal prohibition on completing the same already-established Outstanding Evaluation Obligation when current policy and a fresh Access decision permit narrow continuation.

# Authority boundary

- **Identity** owns stable human continuity, verification/reverification state and human-identity lifecycle.
- **Participation** owns one Participant's scoped, time-bounded capacity and participation lifecycle.
- **Access** owns current capability/disclosure decisions from supplied context plus explicit exceptional-grant state where such a grant exists.
- **Competition** owns the lifecycle of one Competition occurrence.
- **Readiness** is derived permission-to-proceed state and never owns a lifecycle transition.

Authentication/session/navigation/runtime state owns none of these meanings.

# Human continuity → Competition Participation

A Competition Participation is established separately from Identity continuity.

Application binding:

```text
Participation.Participant = stable Identity reference
Participation.Scope       = Competition reference
Participation.Capacity    = requested Competition capacity
```

Conditions for `Participation.enroll` include legitimate current Identity continuity, any required current verification/reverification, Competition acceptance of the requested capacity, and one intended current Participation per Identity × Competition × Capacity rather than duplicate authority from repeated enrollment intent.

A returning Identity may be reused, but a later Competition uses a new Participation. Enrollment does not grant Access, Panel membership, occurrence participation, evaluation responsibility or authorship.

Disabling/restoring Identity never rewrites Participation history. Current Access simply receives the current Identity/context facts; Identity restoration alone does not restore Participation or capability.

# Participation lifecycle and Access

`Participation.checkIn`, declared-attribute maintenance and Participation preparation remain independent from Competition activation.

`Participation.activate` is available when the application supplies the capacity-specific readiness/eligibility conditions required for that Participation. Competition activation does not automatically activate every Participation, and Participation activation does not activate Competition.

`Participation.withdraw` changes Participation truth. It is not an Access edit. `Participation.restore` is governed by current policy/context and does not restore whatever capability existed previously.

A Participation in `Completed` state no longer represents ordinary live-event involvement. That does not erase the relationship/history needed to evaluate a narrowly scoped protected action on an already-established responsibility.

# Semantic operating context

Each protected MUDAC operation is evaluated under exactly one explicit current Participation context containing the relevant semantic facts, including:

- Identity reference;
- Participation reference;
- Competition/Scope reference;
- Capacity;
- current Participation state;
- current Competition lifecycle facts;
- resource/relationship/purpose facts needed by the applicable Access rule.

The Participation must belong to the supplied Identity and Competition scope and be legitimate for the requested operation. `Legitimate` is operation-specific: an Active Judge Participation may be required for ordinary new live-event work, while a completed Participation may still supply attributable context for a narrowly permitted action on an existing Outstanding Evaluation Obligation.

If one Identity holds multiple Participations, their capabilities are **not unioned**. Judge context does not inherit Organizer disclosure/decision capability, and Organizer context cannot rewrite Judge authorship.

The visible act of choosing/switching role mode is Phase 013 mapping unless it changes Concept state. Navigation, session state, cached mode, URL/QR possession and device state create no semantic authority.

# Access-check composition

`Access.check` is composition-only guard behavior for protected reads/actions, not a standalone MUDAC business action.

A protected owner action may proceed only when:

1. Access permits the requested capability/disclosure under current supplied context; and
2. the owning Concept action's own semantic authority/preconditions are satisfied.

Access permission never transfers semantic authorship or decision authority.

Generic `grant`, `temporarilyGrant`, `revoke`, and `expire` are not generic direct MUDAC administration actions. They require purpose-specific composition before exposure. Ordinary Judge live-event capability may be derived from current context and therefore does not require a persisted grant/expiry transition merely to appear or disappear.

# Competition readiness and `markReady`

Application action: **Mark Competition Ready**.

Participant:

- `Competition.markReady`.

Condition:

- current Competition Readiness has no blocking condition for the transition.

Readiness is derived from authoritative source state and policy; it has no write action in this synchronization.

Current competitor-structure readiness includes, where applicable to the configured competition:

- a valid non-withdrawn Team;
- a valid current Division assignment;
- an active Judge-facing Alias under blinded-judging policy;
- intrinsic Alias uniqueness/reservation constraints.

Additional preparation/evaluation-basis sources may be refined by later Phase 011 subgroups without changing the non-authoritative role of Readiness.

# Ready-state invalidation

If a source change while Competition is `Ready` introduces a blocking Competition-readiness condition, MUDAC system-triggers `Competition.returnToDraft`.

A warning that policy permits does not trigger this reaction.

An Organizer may also deliberately invoke `returnToDraft` while Ready when valid Competition semantics permit it.

After Competition is `Active`, later readiness degradation does **not** roll lifecycle backward. The Competition remains Active until its own lifecycle action, while the new problem becomes current operational/correction pressure. Historical live operation is not rewritten.

# Competition activation

Application action: **Activate Competition**.

Participant:

- `Competition.activate`.

Conditions:

- Competition is Ready under its intrinsic lifecycle;
- current live-activation readiness has no blocking condition;
- the acting authority is legitimate.

Activation does not automatically activate Participations, create Panel membership, prepare/begin Evaluation Occurrences, establish Evaluation Obligations or create Scorecards.

# Event completion

Application action: **Complete Live Event**.

Initiating participant:

- authorized `Competition.completeEvent` from Active.

Coordinated Participation consequence:

- each currently Active Judge-capacity Participation representing ordinary live-event involvement in that Competition completes through `Participation.complete`;
- already Completed/Withdrawn/non-live Participations require no duplicate transition;
- Organizer Participation may remain current for reconciliation/outcome work.

Outstanding Evaluation Obligations do **not** block event completion merely because judging work remains incomplete. Event completion does not finalize/delete Scorecards or erase responsibility history.

## Broad live-event capability closes

After Event Completed, completed Judge Participations no longer support ordinary **new live-event judging** simply because they were previously active.

Without an explicit permitted continuation/resume path, Access denies actions such as:

- beginning new ordinary Evaluation Occurrences from the ended live event;
- treating completed Judge Participation as still Active;
- manufacturing new ordinary Evaluation Obligations from prior live context;
- regaining broad event-day capability merely through navigation/session history.

No ordinary persisted `Access.expire` action is required for this broad capability change.

## Existing responsibility may continue narrowly

Event Completed is not a universal hidden Access revocation.

An already-established Outstanding Evaluation Obligation may remain actionable when all of the following are true:

- the obligation already existed under a legitimate begun occurrence;
- the same evaluator/subject/occurrence/basis binding remains legitimate;
- governing policy permits finishing that pre-existing responsibility after live-event end;
- the current Participation record remains attributable to the Judge/Competition/capacity even though ordinary live Participation is Completed;
- fresh `Access.check` permits the specific obligation-scoped read/write/finalize capability;
- no correction/invalidation condition independently blocks the work.

In that case the Judge may start/resume/finalize the **same logical evaluation**. This does not reactivate Participation, reopen Competition, create another obligation or restore general event-day capability.

If genuinely new live-event participation or ordinary new occurrence/responsibility is needed, use explicit event-resume/Participation-restoration composition. If later correction requires genuinely new responsibility, use the established successor-work semantics rather than reopening the terminal predecessor.

# Exceptional event resume

Application action: **Resume Live Event**.

Participant:

- `Competition.resumeEvent`.

Conditions:

- Competition is Event Completed and not Finalized;
- legitimate Organizer authority and attributable exceptional reason exist;
- governing policy/invariants permit resumption.

`resumeEvent` restores **no** Judge Participation, Panel membership, occurrence/obligation state, session or Access by itself.

After a legitimate resume, an Organizer may separately restore selected Judge Participations through `Participation.restore` when current policy and Identity/eligibility facts permit it. Restoration does not grant Access directly; protected actions use fresh `Access.check` results from current context.

Panel/Evaluation Occurrence/Evaluation Obligation consequences of resumed judging belong to the current 011-D composition family.

# Historical presented context

Current Team/Division/Alias state participates in readiness. It does not own or rewrite historical presented judging context.

When judging begins, the applicable presented context must be preserved by the Evaluation Occurrence composition established by 011-D. A later current Team/Division/Alias correction may affect current readiness/derived outcomes but cannot silently alter what was historically shown.

# Current action-surface classification for this family

| Concept action family | Current MUDAC composition status |
| --- | --- |
| Identity continuity/verification/recovery actions | direct application actions under their own authority |
| Identity disable/restore | exceptional direct actions; no Participation/Access restoration side effect |
| Participation `enroll`, `checkIn`, `updateDeclaredAttributes`, `withdraw` | direct application actions |
| Participation `activate` | readiness-gated coordinated action |
| Participation `complete` | direct individually; system participant in Complete Live Event for active Judges |
| Participation `restore` | coordinated exceptional action |
| Access `check` | composition-only/system guard |
| Access generic grant/revoke family | not generically exposed; purpose-specific composition required |
| Competition `create`, `updateDetails` | direct application actions |
| Competition `markReady`, `activate`, `completeEvent`, `resumeEvent` | coordinated application actions |
| Competition `returnToDraft` | direct + system-triggered on Ready-state invalidation |
| Competition `finalize` | owned by 011-G; not settled here |

# Composition invariants

1. Identity continuity is not Participation authority.
2. Participation capacity is not Access permission.
3. Access permission is not semantic authorship or decision authority.
4. Readiness is not lifecycle authority.
5. Competition activation is not mass Participation activation.
6. Event completion is not evaluation-responsibility completion and is not a universal Access revocation.
7. Completed live Participation does not authorize new ordinary live-event work, while an existing Outstanding obligation may remain narrowly actionable when current policy and Access permit it.
8. Active Competition history is not rolled back by later readiness degradation.
9. Exceptional resume cannot resurrect prior capability automatically.
10. One protected operation uses one explicit Participation context; capabilities never union across role contexts.
11. Team/Division/Alias current corrections do not rewrite historical presented judging context.

# Chaining summary

```text
Identity continuity
  → Participation actions as separately invoked
  → one current operating context
  → Access.check for each protected operation
```

```text
blocking source change while Ready
  → derived Readiness becomes blocking
  → Competition.returnToDraft
```

```text
Competition.completeEvent
  → active live Judge Participations complete
  → broad/new ordinary live-event Judge capability closes
  → existing Outstanding obligation may still continue narrowly when policy + fresh Access permit
```

```text
Competition.resumeEvent
  → no automatic capability restoration
  → selected Participation.restore may occur separately
  → Access uses fresh current facts
```

These are conceptual relationships, not event/queue/transaction/session/workflow implementation designs.

# Deferred composition

This owner intentionally defers:

- Panel membership, actual occurrence participants and Evaluation Obligation establishment → 011-D;
- Rubric basis/Scorecard/Versioning/Provenance/paper authority → 011-E;
- correction/invalidation/replacement/successor work → 011-F;
- Coverage/Aggregate/Rank/Award/Competition Finalization/Outcome Declaration → 011-G;
- Export/Publication → 011-H;
- whole-application action-surface/chaining/synergy closure → 011-I;
- user-visible role/context-switch representation → Phase 013.

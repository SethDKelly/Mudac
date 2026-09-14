---
type: Concept Composition Revalidation
title: 011-C — Competition Lifecycle, Identity, Participation, Access & Operating-Context Composition
description: "Establishes current MUDAC composition semantics for Identity continuity, Competition-scoped Participation, contextual Access, Competition readiness/activation/completion/resume, the readiness contribution of Team/Division/Alias state, and semantic operating-context isolation without introducing session/UI/runtime authority."
status: stable
tags: [phase-011, composition, synchronization, competition, identity, participation, access, readiness, context]
sources:
  - resource: 011-A-composition-scope-evidence-reuse-synchronization-risk-subphase-planning.md
  - resource: 011-B-legacy-synchronization-inventory-composition-obligation-map-application-action-baseline.md
  - resource: ../canonical/concepts/competition.md
  - resource: ../canonical/concepts/identity.md
  - resource: ../canonical/concepts/participation.md
  - resource: ../canonical/concepts/access.md
  - resource: ../canonical/mechanisms/readiness.md
  - resource: ../canonical/policies/anonymity-disclosure.md
  - resource: ../canonical/policies/operational-exception-governance.md
  - resource: ../canonical/invariants/judge-independence.md
  - resource: ../canonical/experience/judge-onboarding.md
  - resource: ../canonical/experience/organizer-preparation.md
  - resource: ../canonical/experience/context-role-modes.md
  - resource: ../canonical/experience/action-authority-traceability.md
  - resource: ../canonical/synchronizations/concept-synchronizations.md
  - resource: https://github.com/SethDKelly/Base/blob/main/docs/phases/005/composition-synchronization-contract.md
generated: { by: openai/gpt-5.6-sol, at: 2026-09-14T01:13:00-05:00 }
---

# Purpose

Replace the actor/lifecycle/access portion of the pre-011 synchronization model with current composition semantics over the Phase 010 eighteen-Concept catalog.

011-C owns:

- legacy synchronization 01 — Identity continuity, Participation enrollment and operating context;
- legacy 02 — Competition readiness and activation;
- legacy 03 — event completion, Judge Participation and ordinary Access closure;
- legacy 04 — exceptional event resume;
- the **readiness** portion of legacy 05 — Team/Division/Alias current-state contribution;
- the **semantic Access-context** portion of legacy 16 — one current Participation context without capability union;
- CO-01 and CO-02, plus the readiness slice of CO-03;
- the owning action-surface decisions for Competition, Identity, Participation and Access, except Competition `finalize`, which remains 011-G work.

This subgroup does not own Panel/Evaluation Occurrence/Evaluation Obligation establishment, Scorecard authority, correction propagation, Competition Finalization/Outcome Declaration, external representation/release, or user-visible role-mode mapping.

# Decision summary

**PASS — 011-C is complete.**

The current composition can be reconstructed without reopening Phase 010 and without adding a new Actor Context, Session, Resume Permission, Readiness, or workflow Concept.

The key results are:

1. Identity continuity and Competition Participation remain separate. A stable Identity may be reused; a later Competition still requires a new Participation.
2. Participation enrollment/activation never grants Access by itself. Access always evaluates supplied current context.
3. Competition readiness gates `markReady`/`activate` without Readiness becoming authority.
4. A blocking source change while Competition is `Ready` system-triggers `Competition.returnToDraft`; an `Active` Competition never rolls back merely because current readiness later degrades.
5. `Competition.completeEvent` coordinates normal completion of live Judge Participations, while outstanding Evaluation Obligations and retained evaluation evidence remain untouched.
6. Ordinary Judge private-evaluation Access becomes unavailable after Event Completed through current-context evaluation; no persisted Access-expiry action is required for ordinary capability.
7. Exceptional `Competition.resumeEvent` restores **no** Judge Participation, Panel membership, session, or Access by itself. Selected Judge Participations must be explicitly restored under current conditions.
8. Every protected operation is evaluated against exactly one supplied current Participation context; capabilities from multiple Participations held by one Identity are never unioned.
9. Team/Division/Alias current state contributes to Competition readiness; historical judging presentation remains 011-D/Evaluation Occurrence work.

The durable current synchronization rules are promoted to [Competition Lifecycle, Participation & Contextual Access Composition](../canonical/synchronizations/competition-participation-access.md).

# 1. Composition discipline

011-C applies the Base/Jackson composition rule:

> synchronize existing Concept actions at application level without redefining their intrinsic meaning.

The current owners remain:

- [Identity](../canonical/concepts/identity.md) — stable human continuity;
- [Participation](../canonical/concepts/participation.md) — scoped, time-bounded involvement in one capacity;
- [Access](../canonical/concepts/access.md) — current contextual capability/disclosure decision;
- [Competition](../canonical/concepts/competition.md) — Competition occurrence lifecycle;
- [Readiness](../canonical/mechanisms/readiness.md) — derived permission-to-proceed projection.

No synchronization below turns one owner into another.

# 2. Identity continuity and Competition Participation

## 2.1 Identity resolution is not Participation authority

MUDAC may establish, verify, reverify, recover or recognize a returning Identity. Those actions establish continuity only.

A Participation is established separately through `Participation.enroll` with semantic bindings:

```text
Participant = stable Identity reference
Scope       = current Competition reference
Capacity    = requested Competition capacity
```

Application conditions include:

- the Identity is legitimate for the requested enrollment and not disabled;
- verification/reverification is sufficient where governing policy requires it;
- the Competition currently permits the requested capacity;
- repeated intent for the same Identity × Competition × Capacity resolves one intended current Participation rather than multiplying event authority.

A returning Identity does **not** resume a prior Competition Participation. A new Competition uses a new Participation.

## 2.2 Enrollment does not grant Access

Successful `Participation.enroll` establishes scoped capacity history. It does not:

- grant protected capability;
- create Panel membership;
- create Evaluation Occurrence participation;
- establish an Evaluation Obligation;
- grant Judge authorship;
- restore an old operating context.

Those meanings remain separate.

## 2.3 Identity disable/restore does not rewrite Participation history

If Identity becomes disabled, historical/current Participation records are not deleted or silently rewritten. Current protected operations become unavailable because Access receives current Identity/context facts.

Restoring Identity continuity does not automatically restore Participation state or Access. Each still follows its own current semantics.

# 3. Participation lifecycle and readiness

## 3.1 Check-in and capacity preparation remain independent from Competition activation

`Participation.checkIn`, declared-attribute maintenance and other preparation actions may occur while the Competition is being prepared.

`Participation.activate` is available only when the application supplies the capacity-specific readiness/eligibility conditions required for that Participation.

Competition `activate` does **not** automatically activate every Participation, and Participation activation does not activate Competition.

This avoids recreating a catch-all event Actor Context state.

## 3.2 Withdraw/restore are Participation actions, not Access edits

`Participation.withdraw` changes Participation truth. Current Access may consequently deny capabilities, but Access is not the owner of the withdrawal.

`Participation.restore` is governed by current application conditions. Restoration never means “restore whatever the user could do before.” Access is freshly evaluated from current facts.

# 4. Operating-context binding and Access isolation

## 4.1 Semantic operating context

For a protected MUDAC operation, the application supplies one explicit operating context containing at least the semantic relationship:

```text
IdentityRef
ParticipationRef
CompetitionRef / Scope
Capacity
current Participation state
current Competition lifecycle facts
resource/relationship/purpose facts relevant to the protected operation
```

The Participation reference must belong to the supplied Identity and Competition scope and must be current/legitimate for the requested action.

This is semantic composition input. It is not a Session Concept and does not prescribe how the application remembers or presents the selected context.

## 4.2 No capability union

If one Identity has multiple Participations—for example Judge and Organizer—each protected operation is evaluated under **one** explicitly selected Participation context.

MUDAC does not union capabilities merely because one human owns both Participations.

Therefore:

- Judge context does not inherit Organizer protected-identity/result authority;
- Organizer context does not rewrite Judge authorship;
- prior-context visibility/navigation state is not current authority;
- changing visible role mode does not itself create or modify Access authority.

The user-visible choice/switching representation remains Phase 013 mapping work.

## 4.3 `Access.check` is composition-only guard behavior

`Access.check` is not a generic MUDAC business action offered independently. It participates conceptually whenever a protected read/action is attempted.

The owning business action proceeds only when both:

- Access permits the requested capability/disclosure under supplied current facts; and
- the owning Concept action's own semantic authority/preconditions are satisfied.

Access permission cannot transfer authorship or substitute for Organizer/Judge/domain authority.

## 4.4 Explicit Access grants remain purpose-specific

Generic `grant`, `temporarilyGrant`, `revoke`, and `expire` are **not** promoted as generic direct MUDAC administration actions by 011-C.

They may participate in a later purpose-specific synchronization—for example narrow post-event correction access—only when that subgroup/policy establishes the semantic reason, scope, authority and lifetime.

Ordinary Judge live-event capability is derived from current context and does not require a persisted grant merely to exist or expire.

# 5. Competition readiness and lifecycle composition

## 5.1 `markReady` consumes Readiness; it does not set it

Application action: **Mark Competition Ready**.

Participant:

- `Competition.markReady`.

Application-level condition:

- current Competition Readiness has no blocking conditions for this transition.

Readiness is derived from current authoritative source state and policy. It has no write action that participates in the synchronization.

The derived source set includes, as applicable, Competition details, competitor structure, blinded representation, evaluation configuration/basis and other preparation state. 011-C confirms only the actor/lifecycle and Team/Division/Alias readiness slice; later 011-D/E work may refine additional composition sources without changing the rule that Readiness is non-authoritative.

## 5.2 Ready-state invalidation returns Competition to Draft

If a source change while Competition is `Ready` introduces a blocking Competition-readiness condition, MUDAC system-triggers `Competition.returnToDraft`.

This preserves the meaning of Ready as a current commitment backed by valid source configuration rather than a stale manually retained flag.

A warning that policy permits does not trigger this reaction.

The reaction is one-way and bounded:

- source change → Readiness becomes blocking → `returnToDraft`;
- `returnToDraft` is not itself treated as a source correction that recursively triggers another lifecycle action.

An Organizer may also deliberately invoke `returnToDraft` while Ready when valid Competition semantics permit it.

## 5.3 Active Competition never rolls back because readiness degrades

After `Competition.activate`, later configuration/correction problems do not rewrite the fact that live Competition operation occurred.

An `Active` Competition therefore remains Active until its own next lifecycle action. A new blocking/degraded condition is represented as current operational/correction pressure, not as automatic rollback to Draft or Ready.

This preserves current versus historical truth.

## 5.4 Competition activation

Application action: **Activate Competition**.

Participant:

- `Competition.activate`.

Conditions:

- Competition is Ready under its intrinsic lifecycle;
- current live-activation readiness has no blocking conditions;
- the acting authority is legitimate for activation.

Activation does not automatically:

- activate every Participation;
- create Panel membership;
- prepare/begin every Evaluation Occurrence;
- establish Evaluation Obligations;
- create Scorecards.

Those are independent later composition actions.

# 6. Team/Division/Alias readiness contribution

The readiness half of legacy synchronization 05 is retained with corrected boundaries.

For the current MUDAC competition model, current non-withdrawn competitor setup contributes to readiness through source facts such as:

- a valid Team in the Competition scope;
- a valid current Division assignment where the configured competition model uses Division;
- one active Judge-facing Alias under the applicable blinded-judging policy;
- Alias uniqueness/reservation constraints required by Alias itself.

A blocking competitor-structure defect prevents `markReady`/`activate` as applicable.

If current structure is corrected after judging has begun, that does **not** rewrite the context actually presented in historical evaluation. The snapshot/binding of presented Team/Division/Alias context to [Evaluation Occurrence](../canonical/concepts/evaluation-occurrence.md) belongs to 011-D.

# 7. Event completion composition

## 7.1 Complete event is not complete evaluation work

Application action: **Complete Live Event**.

Trigger/initiating participant:

- authorized `Competition.completeEvent` from Active.

Coordinated Participation consequence:

- each currently Active **Judge-capacity Participation** whose ordinary live-event involvement belongs to that Competition is completed through `Participation.complete`;
- already Completed/Withdrawn/non-live Participations require no duplicate transition;
- Organizer Participation may remain current for reconciliation/outcome work.

This coordinated completion is intentional: leaving Judge Participation Active would allow exceptional `resumeEvent` to resurrect ordinary capability merely by changing Competition lifecycle back to Active.

## 7.2 Outstanding responsibility does not block event completion

`completeEvent` does not require every Evaluation Obligation to be satisfied and does not finalize or delete any Scorecard.

After event completion:

- outstanding obligations remain outstanding until separately excused/cancelled/satisfied or otherwise handled by later composition;
- Draft/authoritative evaluation evidence remains retained under its own owner;
- event completion records that live operation ended, not that all judging work is semantically resolved.

This preserves the Phase 010 occurrence/responsibility distinction.

## 7.3 Ordinary Judge Access closes from current context

Once Competition is Event Completed and live Judge Participations are completed, ordinary Judge private-evaluation capability is denied by current `Access.check` rules.

No ordinary persisted `Access.expire` action is necessary merely to cause this denial.

A later narrowly authorized correction path may use a purpose-specific exceptional Access composition without restoring broad historical Judge mode.

# 8. Exceptional event resume

## 8.1 `resumeEvent` changes Competition only

Application action: **Resume Live Event**.

Participant:

- `Competition.resumeEvent`.

Conditions:

- Competition is Event Completed and not Finalized;
- legitimate Organizer authority and an attributable exceptional reason exist;
- no policy/invariant forbids resumption.

`resumeEvent` returns Competition to Active but does **not** itself:

- restore any completed/withdrawn Judge Participation;
- restore Panel membership;
- recreate Evaluation Occurrences/Obligations;
- restore sessions or cached context;
- grant Access.

## 8.2 Judge reactivation is explicit and selective

After a legitimate resume, an Organizer may separately invoke a purpose-specific application action that uses `Participation.restore` for each Judge who should resume live involvement.

Application conditions include:

- same Competition and Judge capacity;
- the historical Participation is eligible for restoration under governing policy;
- current Identity/eligibility facts remain legitimate;
- no independent withdrawal/disqualification condition is being silently overridden.

Restoring Participation does not grant Access directly. Ordinary capability becomes available only if the subsequently supplied current operating context passes `Access.check` and all protected-action preconditions.

Panel/occurrence/obligation consequences of a resumed Judge are deferred to 011-D.

# 9. Identity/Participation/Access action-surface decision

011-C refines the provisional 011-B classifications for this family.

| Concept action | 011-C application classification | Rationale |
| --- | --- | --- |
| `Identity.establish`, `verify`, `reverify`, `updateNecessaryIdentityInformation`, `recover`, `recognizeReturningIdentity` | **Direct application actions** | human-continuity behavior is useful independently; no Participation/Access state is implied |
| `Identity.disable`, `restore` | **Exceptional direct actions with current-context consequences** | Identity owns the transition; Participation history remains; Access re-evaluates current facts |
| `Participation.enroll`, `checkIn`, `updateDeclaredAttributes`, `withdraw` | **Direct application actions** | each changes scoped participation truth directly |
| `Participation.activate` | **Coordinated/readiness-gated application action** | application supplies current capacity readiness |
| `Participation.complete` | **Direct when intentionally completing one Participation; system participant in Complete Live Event for active Judges** | normal individual completion remains meaningful; event completion supplies the coordinated case |
| `Participation.restore` | **Coordinated exceptional action** | current policy/identity/context must permit restoration; resume does not invoke it automatically |
| `Access.check` | **Composition-only/system guard** | protected operations consume it; not a standalone business action |
| `Access.grant`, `temporarilyGrant`, `revoke` | **Intentionally unavailable as generic direct actions** | require purpose-specific composition before exposure |
| `Access.expire` | **System-triggered/composition-only for explicit grants** | ordinary derived capability needs no persisted expiry transition |
| `Competition.create`, `updateDetails` | **Direct application actions** | ordinary Competition lifecycle/context ownership |
| `Competition.markReady`, `activate`, `completeEvent`, `resumeEvent` | **Coordinated application actions** | each has application-level readiness/participation/authority consequences |
| `Competition.returnToDraft` | **Direct + system-triggered** | Organizer may deliberately return; blocking Ready-state invalidation also requires it |
| `Competition.finalize` | **Unresolved here / owned by 011-G** | must coordinate with finalization readiness and Outcome Declaration |

011-I will still perform the whole-application action-surface closure, but this family has no remaining unresolved item except the intentionally deferred `Competition.finalize`.

# 10. Chaining and automation

The material conceptual chains established here are:

```text
Identity continuity resolved
  → Participation enrollment/check-in/activation as separately invoked
  → protected operation supplies one current Participation context
  → Access.check permits/denies
```

```text
source configuration change while Competition Ready
  → Competition Readiness becomes blocking
  → system-trigger Competition.returnToDraft
```

```text
Competition.completeEvent
  → active live Judge Participations complete
  → subsequent ordinary Judge Access checks deny live private-evaluation capability
```

```text
Competition.resumeEvent
  → no capability resurrection
  → selected Participation.restore actions may later occur
  → subsequent Access checks use fresh current facts
```

No chain here requires a runtime queue, transaction, session propagation mechanism, event bus, retry scheme or workflow engine.

# 11. Over-synchronization and under-synchronization audit

## Rejected over-synchronization — verify Identity + enroll Participation as one mandatory action

Identity may already exist and may be verified/reverified at a different time. Mandatory fusion would collapse reusable human continuity into event participation.

**Rejected.** Identity legitimacy is an enrollment condition; Identity action participation is conditional, not universal.

## Rejected over-synchronization — activate Competition + activate all Participations

A Competition can legitimately become Active while some expected participants are absent, late, withdrawn or not yet individually ready.

**Rejected.** Competition and Participation activation remain independent actions with related conditions.

## Rejected under-synchronization — complete Competition but leave ordinary Judge Participations Active

That would make exceptional resume silently resurrect capability when Competition returns Active.

**Rejected.** Complete Live Event coordinates completion of active live Judge Participations.

## Rejected over-synchronization — complete event only when every evaluation obligation is satisfied

Live-event completion and evaluator responsibility are independent meanings; unfinished work may remain visible after the event ends.

**Rejected.** Evaluation Obligation state does not gate `completeEvent` merely because judging work is incomplete.

## Rejected under-synchronization — resume event automatically restores prior capability

A resume may occur after Judge withdrawal, identity/eligibility change, Panel change or other conditions that make prior authority unsafe.

**Rejected.** Participation restoration is selective and explicit; Access is re-evaluated.

## Rejected false synchronization — role-mode switch mutates Access

The visible context switch is a mapping concern. Access evaluates supplied context but does not own a “current mode” state merely because the interface has one.

**Rejected.** Semantic context binding stays in 011-C; representation stays in Phase 013.

# 12. Authority compatibility

011-C preserves the following boundaries:

- Identity proof/continuity does not grant Competition authority;
- Participation capacity does not itself permit a protected operation;
- Access permission does not transfer semantic authorship/decision authority;
- technical/session/navigation state does not grant Access;
- Readiness does not own Competition lifecycle transitions;
- Competition lifecycle does not own Participation history except through explicit application synchronization;
- event completion does not resolve evaluation obligations;
- exceptional resume does not waive unrelated policies or invariants.

[Operational Exception Governance](../canonical/policies/operational-exception-governance.md) continues to apply: an exceptional resume preserves source truth and cannot act as a generic override.

# 13. Purpose trace

011-C principally advances:

- **P-03 — Low-friction and accessible participation:** stable Identity can be reused while Participation remains event-scoped;
- **P-04 — Live operational coordination and completion:** readiness, activation, event completion and selective resume are explicit;
- **P-08 — Contextual confidentiality and authority separation:** one current Participation context feeds Access, with no role union or technical-authority leakage;
- **P-01 — Independent human judgment:** ordinary Judge access closes after live judging and peer/protected information remains governed by current context;
- **P-07 — Correctable authority and historical truth:** Active history is not rolled back by later readiness defects, and resume does not rewrite prior completion history.

# 14. Phase 012 and Phase 013 carry-forwards

## Phase 012

011-C does not decide whether every coherent product variant requires:

- Division;
- Alias/blinded judging;
- persistent Identity reuse;
- explicit Access grant state;
- every capacity represented by Participation.

Those are inclusion/product-family questions.

## Phase 013

Carry forward:

- how Judge/Organizer Participation context is selected or displayed;
- role-mode navigation;
- how Ready/degraded/completed/resumed states are represented;
- how context changes are communicated without implying new authority;
- interaction affordances for direct/coordinated/exceptional actions.

No UI route, component, browser state or session design is established here.

# 15. Legacy-contract closure

For current authority after 011-C:

- legacy 01 — **replaced** by the Identity→Participation binding plus contextual Access rules above;
- legacy 02 — **revalidated/replaced** by current Competition readiness/activation composition;
- legacy 03 — **reframed/replaced** by explicit Judge Participation completion + derived ordinary Access closure;
- legacy 04 — **revalidated/replaced** by no-resurrection exceptional resume + selective Participation restore;
- legacy 05 readiness half — **revalidated** as current Team/Division/Alias readiness contribution; historical presented context remains 011-D;
- legacy 16 semantic half — **revalidated/replaced** by one-Participation operating-context isolation; visible context switching remains Phase 013.

The old synchronization body remains historical evidence for contracts not yet replaced by later 011 subgroups.

# 16. Exit criteria

| Exit criterion | Result |
| --- | --- |
| CO-01 human continuity/Participation/Access composition established | **PASS** |
| CO-02 lifecycle/readiness/completion/resume composition established | **PASS** |
| CO-03 readiness slice established without claiming occurrence snapshot ownership | **PASS** |
| legacy 01–04 current semantics replaced/revalidated | **PASS** |
| legacy 05 readiness slice revalidated | **PASS** |
| legacy 16 semantic Access-context slice revalidated | **PASS** |
| ordinary Judge Access closure does not require session/runtime semantics | **PASS** |
| exceptional resume cannot resurrect authority automatically | **PASS** |
| completion does not collapse Evaluation Obligation semantics | **PASS** |
| no capability union across Participations | **PASS** |
| current action-surface decisions made for owned family | **PASS** |
| no Phase 010 boundary/spec defect discovered | **PASS** |
| Phase 012 inclusion questions preserved | **PASS** |
| Phase 013 mapping questions preserved | **PASS** |
| runtime/implementation mechanism avoided | **PASS** |

# Decision

**PASS — 011-C is complete.**

No upstream Concept rework is required. Current composition knowledge is promoted canonically for this family, and the dependency-safe next subgroup is 011-D.

# Handoff

Proceed to:

> **011-D — Team/Division/Alias/Panel, Evaluation Occurrence & Evaluation Obligation Establishment**

011-D should start from the now-current lifecycle/context assumptions established here, especially:

- Competition must be Active for ordinary live occurrence begin;
- intended Panel grouping, current Participation eligibility, actual occurrence participation and Evaluation Obligation responsibility remain distinct;
- Team/Division/Alias current readiness does not rewrite historical presented context;
- operating-context Access permission does not establish occurrence participation or evaluation responsibility;
- exceptional Competition resume restores no Panel/occurrence/obligation state automatically.

# Implementation state

```text
Jackson Concept Design: REOPENED / IN PROGRESS
Phase 009: COMPLETE — PASS
Phase 010: COMPLETE — PASS
Phase 011: IN PROGRESS
011-A: COMPLETE — READY
011-B: COMPLETE — PASS
011-C: COMPLETE — PASS
011-D: NEXT
architecture authority: SUSPENDED
implementation-planning authority: SUSPENDED
006-D bootstrap: FROZEN HISTORICAL NON-DOMAIN SUBSTRATE
new domain implementation: NOT STARTED
implementation readiness: NOT READY
implementation authorization: NOT YET
production readiness: NOT ESTABLISHED
```
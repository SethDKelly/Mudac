---
type: Experience Contract
title: Judge Entry, Participation & Readiness Mapping
description: Current Judge-entry mapping for Competition context, Identity continuity, Competition-specific Participation, event attributes/check-in, contextual Access, Panel planning context and derived Ready-to-Judge explanation.
status: stable
tags: [experience, mapping, judge, onboarding, identity, participation, access, readiness, phase-013]
sources:
  - resource: ../../013-concept-mapping-interaction-semantics-user-visible-representation/013-C-context-identity-participation-access-bias-control-judge-entry-mapping.md
  - resource: ../concepts/identity.md
  - resource: ../concepts/participation.md
  - resource: ../concepts/access.md
  - resource: ../concepts/panel.md
  - resource: ../synchronizations/competition-participation-access.md
  - resource: ../synchronizations/evaluation-occurrence-obligation.md
  - resource: ../policies/anonymity-disclosure.md
---

# Purpose

Define the semantic information and action mapping required for a Judge to enter the correct Competition context and become prepared for ordinary judging without conflating identity, event participation, grouping, Access or evaluation responsibility.

# Judge-entry questions

Judge entry must let the person understand, as applicable:

```text
Which Competition am I entering?
Which human Identity is being used?
Is current verification/reverification sufficient?
Do I have a current Judge Participation for this Competition?
What current Participation state or event-specific attributes require attention?
Am I checked in / active as required by current policy?
Is there current Panel/grouping information relevant to me?
Am I presently prepared to enter ordinary judging work?
If not, which source condition blocks preparation and what legitimate next action exists?
```

These questions need not appear as a wizard or fixed sequence.

# Competition context precedes authority interpretation

The current Competition must be unambiguous before event-scoped Participation or readiness is interpreted.

An event code, QR code, invitation, deep link or bookmarked route may identify/navigate toward a Competition, but it does not establish Identity, Participation, Panel membership, Access or evaluation responsibility.

A non-camera path remains required at the semantic level because QR/camera is an optional navigation mechanism rather than authority.

# Identity continuity

A first-time volunteer may establish and verify Identity. A returning volunteer may reuse recognized Identity continuity and reverify as required.

Entry feedback must distinguish successful Identity continuity from current event authority.

```text
recognized Identity
  != Judge Participation
  != checked-in / active Participation
  != Panel membership
  != Access
  != Evaluation Obligation
```

Prior Competition history must never be represented as though it automatically resumes current authority.

# Competition-specific Judge Participation

Every Competition uses a distinct Judge Participation even when Identity is reused.

Judge entry may expose current Participation facts such as:

- Judge capacity and Competition scope;
- enrollment/current status;
- check-in state;
- current-event declared expertise/profile attributes where relevant;
- Active/Completed/Withdrawn state;
- an exceptional restoration requirement where policy permits restoration.

Participation actions retain their Phase-011 application semantics:

- `enroll`, `checkIn`, `updateDeclaredAttributes`, `withdraw` are direct application actions;
- `activate` is coordinated/readiness-gated;
- `restore` is exceptional/coordinated;
- completion may occur directly or as a composed consequence of live-event completion.

The mapping must make the target Competition and Judge capacity clear for any consequential Participation action.

# Event-specific profile / expertise

Expertise or similar Judge attributes are current Participation metadata where used by MUDAC.

Reusing a returning Identity does not silently carry event-specific participation attributes forward as current truth unless current Participation semantics explicitly establish them.

Confirming expertise does not grant Access, create Panel membership or establish responsibility.

# Panel assignment at entry

Panel assignment may be useful operational context, but Panel represents intended reusable evaluator grouping.

Showing a Judge that they are assigned to a Panel must not imply that:

- they will participate in every Evaluation Occurrence associated with that Panel;
- an occurrence has already begun;
- they currently have an Evaluation Obligation;
- a Scorecard exists;
- they can access a specific Team/evaluation artifact.

Likewise, absence of a Panel assignment must not be represented as a universal blocker unless current competition policy/readiness actually requires one for the relevant PF-01 profile.

# Derived `Ready to Judge`

`Ready to Judge` is an explanatory projection over current source facts.

Its question is:

> **Is this Judge currently prepared to enter ordinary judging work for this Competition?**

It may summarize relevant current conditions such as:

- legitimate Identity continuity/reverification;
- current Competition-specific Judge Participation;
- required check-in/activation state;
- required event-specific declared attributes;
- Organizer-governed grouping/preparation facts where current policy makes them relevant;
- Competition lifecycle/readiness facts relevant to Judge entry;
- current contextual capability/disclosure expectations.

`Ready to Judge` is not:

```text
Participation lifecycle state
Panel membership
Evaluation Occurrence participation
Evaluation Obligation
Scorecard existence
persisted Access grant
a manually editable checklist item
```

There is no generic `Set Ready`, `Mark Ready to Judge` or readiness override action.

When the projection is not satisfied, the representation should identify the authoritative source condition and legitimate next action where the current actor can perform one. A displayed ready result never substitutes for a fresh Access decision when a protected operation is attempted.

# Judge-safe disclosure during entry

Judge entry adopts the Judge-safe disclosure posture.

During blinded judging, competitor-facing context uses **Alias + Division** and withholds institution/administrative identity and optional Team Name by default.

The same human having an Organizer Participation does not make Organizer-sensitive information visible in Judge context. Capability/disclosure does not union across Participations.

Detailed Team/evaluation task presentation is owned by later evaluation mapping; 013-C establishes only the entry/context disclosure boundary.

# Availability and feedback

Judge entry should distinguish semantically different reasons that change the legitimate next action, including:

- Identity needs establishment/reverification;
- no Judge Participation exists for this Competition;
- Participation exists but needs check-in or another required state transition;
- Participation is Withdrawn/Completed;
- current Competition lifecycle does not permit ordinary live Judge work;
- an expected grouping/preparation source is incomplete;
- the Judge is entry-ready but has no current evaluation responsibility/work;
- a protected operation is denied by current Access.

A generic `Unauthorized`, disabled control or hidden route is insufficient when it would cause the person to infer the wrong source condition. Denial explanation must still avoid leaking protected information.

For direct/coordinated entry actions, successful feedback should confirm the semantic result actually established—Identity continuity, Participation enrollment/check-in/activation, or current readiness—without implying downstream authority not established by that action.

# Multi-capacity Judge / Organizer identities

If one Identity has both Judge and Organizer Participations, Judge entry selects the Judge Participation context only.

Switching to/from Organizer context does not mutate either Participation and does not merge Access.

The destination Competition/capacity and materially different disclosure posture must be intelligible before protected information/action meaning changes.

See [Experience Context and Participation Modes](context-role-modes.md).

# Event completion / later access

Ordinary live Judge Participation completes as part of live-event completion where current composition applies, and ordinary private-evaluation Access is then denied by current context.

Historical Participation/evaluation records may remain inspectable where separately permitted, but history does not restore ordinary live Judge mode or capability.

A later legitimate correction path uses narrow current authority rather than pretending the event-day Participation never ended.

Detailed correction/history mapping belongs to 013-F.

# Support and recovery boundary

Technical support may help re-establish technical access or legitimate context but cannot mark a Judge ready, create Participation, assign domain authority, expose protected competitor identity or author evaluation merely through support privilege.

If technical recovery restores a session, the application must still evaluate current Identity/Participation/Competition/Access facts.

# Structural mapping constraints

Judge entry must preserve these semantics regardless of downstream interface design:

1. Competition context is clear enough to avoid cross-event authority confusion.
2. Identity continuity is visibly distinct from Competition-specific Participation.
3. Participation state/required source conditions can be understood without treating Access as a role flag.
4. Panel assignment is visibly planning/grouping context rather than responsibility.
5. `Ready to Judge` is presented as derived/explanatory rather than writable authority.
6. Judge-safe disclosure applies before detailed evaluation work begins.
7. entry mechanisms such as QR/deep links do not appear to grant authority.
8. historical participation does not appear current.

No exact page order, component, route, account/session provider or authentication workflow is prescribed.

# Related mapping

Operating-context/multi-capacity rules are owned by [Experience Context and Participation Modes](context-role-modes.md).

Detailed occurrence/obligation/judgment/Scorecard action mapping belongs to 013-E.

Accessibility/degraded interaction parity is re-audited in 013-J.

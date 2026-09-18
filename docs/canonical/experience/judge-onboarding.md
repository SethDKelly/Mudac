---
type: Experience Contract
title: Judge Entry, Participation & Readiness Mapping
description: Current Judge-entry mapping for Competition context, Identity continuity, Competition-specific Participation, event attributes/check-in, contextual Access, Panel planning context and derived Ready-to-Judge explanation.
status: stable
tags: [experience, mapping, judge, onboarding, identity, participation, access, readiness, phase-013]
sources:
  - resource: ../../013-concept-mapping-interaction-semantics-user-visible-representation/013-C-context-identity-participation-access-bias-control-judge-entry-mapping.md
  - resource: ../../013-concept-mapping-interaction-semantics-user-visible-representation/013-K-whole-experience-explanation-order-cross-role-profile-consistency-mapping-integrity-audit.md
  - resource: ../concepts/identity.md
  - resource: ../concepts/participation.md
  - resource: ../concepts/access.md
  - resource: ../concepts/panel.md
  - resource: ../synchronizations/competition-participation-access.md
  - resource: ../synchronizations/evaluation-occurrence-obligation.md
  - resource: ../policies/anonymity-disclosure.md
---

# Purpose

Define the semantic information and action mapping required for a Judge to enter the correct Competition context and become prepared for ordinary judging without conflating Identity, Participation, grouping, Access or evaluation responsibility.

# Judge-entry questions

Judge entry should make these questions answerable where applicable:

```text
Which Competition am I entering?
Which human Identity is being used?
Is verification/reverification sufficient?
Do I have a current Judge Participation for this Competition?
What Participation state or event attributes need attention?
Am I checked in / active where policy requires it?
What current Panel/grouping context is relevant?
Am I prepared to enter ordinary judging work?
If not, which authoritative source condition blocks me?
```

This is an explanation set, not a required wizard.

# Competition context before authority interpretation

The current Competition must be unambiguous before Competition-scoped Participation or readiness is interpreted.

An invitation, event code, QR, deep link or bookmark may identify/navigate toward a Competition, but it does not establish:

- Identity;
- Judge Participation;
- Panel membership;
- Access;
- Evaluation Occurrence participation;
- Evaluation Obligation;
- Scorecard authority.

A non-camera path remains required semantically because QR/camera is navigation convenience rather than authority.

# Identity continuity is not event authority

A first-time volunteer may establish/verify Identity; a returning volunteer may reuse recognized Identity continuity and reverify as required.

Preserve:

```text
recognized Identity
  != Judge Participation
  != checked-in / active Participation
  != Panel membership
  != Access
  != Evaluation Obligation
```

Historical Competition participation never resumes current authority automatically.

# Competition-specific Judge Participation

Each Competition uses a distinct Judge Participation even when Identity is reused.

Judge entry may expose current Participation facts such as:

- Judge capacity and Competition scope;
- enrollment/current state;
- check-in state;
- current-event declared expertise/profile attributes;
- Active/Completed/Withdrawn state;
- exceptional restoration requirements where policy permits restoration.

Application actions retain Phase-011 semantics:

- `enroll`, `checkIn`, `updateDeclaredAttributes`, `withdraw` — direct;
- `activate` — coordinated/readiness-gated;
- `restore` — exceptional/coordinated;
- completion — direct or composed/system consequence where current synchronization defines it.

Consequential Participation actions must make target Competition and Judge capacity clear.

# Event-specific profile / expertise

Expertise or similar Judge attributes are current Participation metadata where used.

Returning Identity continuity does not silently carry prior event-specific attributes forward as current truth.

Confirming expertise does not grant Access, create Panel membership or establish evaluation responsibility.

# Panel assignment is planning context

Panel represents intended reusable evaluator grouping.

Showing a Judge's Panel assignment must not imply:

- actual participation in every Evaluation Occurrence;
- an occurrence has begun;
- an Evaluation Obligation exists;
- a Scorecard exists;
- Access to a Team/evaluation artifact exists.

Absence of Panel assignment is not a universal blocker unless current Competition policy/readiness makes it one.

# Derived Ready to Judge

`Ready to Judge` is an explanatory projection answering:

> Is this Judge currently prepared to enter ordinary judging work for this Competition?

It may summarize current facts such as:

- legitimate Identity continuity/reverification;
- current Judge Participation;
- required check-in/activation state;
- required event-specific attributes;
- Organizer-governed grouping/preparation facts where policy makes them relevant;
- Competition lifecycle facts relevant to entry;
- contextual capability/disclosure expectations.

It is not:

```text
Participation lifecycle state
Panel membership
Evaluation Occurrence participation
Evaluation Obligation
Scorecard existence
persisted Access grant
manually editable checklist state
```

There is no generic `Set Ready` or readiness override.

When readiness is false, identify the authoritative source condition and legitimate next action where doing so does not leak protected information. A displayed ready result never substitutes for a fresh Access decision on a protected operation.

# Judge-safe disclosure

Judge entry adopts Judge-safe disclosure.

During blinded judging, competitor context uses **Alias + Division** and withholds institution/administrative identity and optional Team Name by default.

The same Identity holding Organizer Participation does not make Organizer-sensitive information visible in Judge context. Capabilities/disclosure never union across Participations.

Detailed evaluation subject/basis presentation is owned by [Judge Active Evaluation Mapping](judge-evaluation.md).

# Availability and feedback

Entry should distinguish materially different causes when they imply different legitimate next actions, including:

- Identity establishment/reverification required;
- no Judge Participation for this Competition;
- check-in/activation or another Participation transition required;
- Participation Withdrawn/Completed;
- Competition lifecycle does not permit ordinary live Judge entry;
- required grouping/preparation source incomplete;
- Judge is entry-ready but has no current Evaluation Obligation;
- protected action denied by current Access.

A generic `Unauthorized`, hidden route or disabled control is insufficient where it would imply the wrong source condition. Explanation must still preserve disclosure/privacy.

Successful feedback confirms only the semantic result actually established—such as Identity continuity, Participation enrollment/check-in/activation or current readiness—without implying downstream responsibility or judgment authority.

# Multi-capacity Identity

If one Identity has both Judge and Organizer Participations, Judge entry selects only the Judge Participation context.

Switching context does not mutate either Participation and does not merge Access.

The destination Competition/capacity and materially different disclosure posture must be intelligible before protected meaning changes.

See [Experience Context and Participation Modes](context-role-modes.md).

# Event completion and remaining Judge work

Competition `Event Completed` ends the ordinary live-event entry/readiness context. It does **not** by itself prove that every Judge obligation is terminal or universally revoke every form of permitted Judge work.

Preserve:

```text
Event Completed
  != all Evaluation Obligations terminal
  != all Scorecards Finalized
  != universal hidden Access revocation
```

If an Outstanding Evaluation Obligation remains after Event Completed and current policy plus current Access permit continuation, the Judge may continue the **same logical evaluation** under [Judge Active Evaluation Mapping](judge-evaluation.md).

Historical Participation/evaluation records may also remain inspectable where separately permitted. History does not restore ordinary live-event entry mode.

Later amendment, correction or other exceptional historical action uses narrow current authority under [Authority Lineage, Capture & Correction Mapping](authority-lineage-correction.md), rather than pretending event-day authority never ended.

# Support and recovery boundary

Technical support may help re-establish operation or legitimate context but cannot mark a Judge ready, create Participation, create evaluation responsibility, expose protected competitor identity or author judgment through support privilege.

Recovery still evaluates current Identity, Participation, Competition, target resource and Access facts.

See [Accessibility, Responsive & Degraded-Operation Mapping](accessibility-resilience.md) and [Status, Feedback & Recovery Mapping](status-feedback-recovery.md).

# Structural mapping constraints

Judge entry preserves these semantics regardless of downstream interface design:

1. Competition context is clear enough to avoid cross-event confusion.
2. Identity continuity is distinct from Competition-specific Participation.
3. Participation state is understandable without treating Access as a role flag.
4. Panel assignment is planning/grouping context rather than responsibility.
5. `Ready to Judge` is derived/explanatory rather than writable authority.
6. Judge-safe disclosure applies before detailed evaluation work begins.
7. QR/deep links/navigation do not grant authority.
8. historical Participation does not appear current.
9. Event Completed ends ordinary live entry context without silently erasing legitimate remaining work.

No page order, component, route, account/session provider or authentication workflow is prescribed.

# Related mapping

- operating context / multi-capacity → [Experience Context and Participation Modes](context-role-modes.md);
- active occurrence/obligation/judgment → [Judge Active Evaluation Mapping](judge-evaluation.md);
- correction/history → [Authority Lineage, Capture & Correction Mapping](authority-lineage-correction.md);
- live remaining-work semantics → [Organizer Live Operations & Remaining Work Mapping](live-operations.md);
- accessibility/recovery parity → [Accessibility, Responsive & Degraded-Operation Mapping](accessibility-resilience.md) and [Status, Feedback & Recovery Mapping](status-feedback-recovery.md);
- whole-experience integrity → [Whole-Experience Action, Explanation & Authority Traceability](action-authority-traceability.md).

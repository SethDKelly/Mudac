# Phase 003 — Conceptual UX Architecture, Information Architecture & Interaction Model

Status: **In Progress**

## Purpose

Phase 001 discovered the application Concepts. Phase 002 specified how those Concepts behave and compose. Phase 003 translates that stable behavioral model into an actor-centered experience architecture before visual design, component design, front-end framework selection, routing implementation, persistence design, or AWS topology.

The governing question is:

> How should Judges and Organizers experience the specified concepts and workflows so that Competition state, authority, privacy, judging context, exceptions, recovery, and official outcomes remain understandable under live-event conditions?

Phase 003 is still conceptual design. It may define experience regions, navigation relationships, role modes, journeys, task states, information hierarchy, interaction contracts, and responsive/degraded behavior. It should not prematurely define React components, URL structures, CSS systems, backend APIs, database tables, or AWS services.

## Why ten subgroupings

Ten groups provide enough separation to keep the two primary actor experiences and cross-cutting operational concerns coherent:

1. establish overall experience architecture, role modes, Competition context, and navigation;
2. design low-friction Judge arrival/participation/Panel onboarding;
3. design the core Judge Encounter, Rubric, Scorecard, finalization, and amendment experience;
4. design Organizer Competition setup and readiness;
5. design Organizer Judge/Panel/Encounter live operations and exception response;
6. design reconciliation, Coverage/Ranking review, Awards, and Finalization;
7. design paper capture, Export/print, and publication workflows;
8. define accessibility, mobile/responsive, interruption, degraded-network, and fallback interaction requirements;
9. consolidate cross-cutting status language, feedback, disclosure/privacy, confirmation, and recovery patterns;
10. reconcile the full experience architecture and determine readiness for visual/system architecture.

## Phase plan

| Group | Topic | Status |
| --- | --- | --- |
| 003-A | [Experience Architecture, Role Modes & Navigation Model](003-A-experience-architecture-role-modes-navigation-model.md) | **Complete** |
| 003-B | [Judge Entry, Identity, Participation & Panel Onboarding](003-B-judge-entry-identity-participation-panel-onboarding.md) | **Complete** |
| 003-C | [Judge Encounter, Rubric, Scorecard & Amendment Experience](003-C-judge-encounter-rubric-scorecard-amendment-experience.md) | **Complete** |
| 003-D | [Organizer Competition Setup, Configuration & Readiness Experience](003-D-organizer-competition-setup-configuration-readiness-experience.md) | **Complete** |
| 003-E | Organizer Judge, Panel, Encounter & Live Operations Experience | **Next** |
| 003-F | Reconciliation, Coverage, Ranking, Awards & Finalization Experience | Planned |
| 003-G | Paper Capture, Export, Print & Publication Experience | Planned |
| 003-H | Accessibility, Mobile, Responsive & Degraded-Mode Interaction Architecture | Planned |
| 003-I | Cross-Cutting Status, Feedback, Privacy, Disclosure & Recovery Patterns | Planned |
| 003-J | Phase 003 Consolidation & UX Architecture Exit Review | Planned |

## Phase 002 input contract

Phase 003 treats the following semantics as authoritative inputs rather than UX choices:

- Competition lifecycle is `Draft → Ready → Active → Event Completed → Finalized`.
- Identity, Participation, Access, and semantic authority remain distinct.
- Judge and Organizer are Participation roles.
- Team administrative identity and Judge-facing Alias are distinct.
- Team supports extensible descriptive attributes; `teamName` is a standard optional attribute with no competitive effect by default.
- Team attributes have explicit disclosure posture; student-created Team names are not Judge-visible by default while blinded judging is active.
- Panel current membership and historical Encounter participation are distinct.
- Effective Encounter participation creates Scorecard obligations.
- One Judge Participation × one Encounter yields one logical Scorecard.
- Scorecards remain bound to one exact Rubric Version.
- Draft, Finalized, and Amendment Draft have distinct authority semantics.
- Judge Notes are private evaluation evidence.
- ordinary Judge private evaluation Access expires at Event Completed.
- Versioning preserves authoritative states; Provenance explains origin/authority.
- Coverage and Aggregate are independent.
- Ranking is Division-scoped and derived.
- Awards are distinct from Rank.
- Finalization creates a reconstructible Official Outcome Revision.
- Finalization is separate from publication.
- paper and electronic capture share Scorecard semantics.
- operational fallback may change capture channel but never evaluation meaning/weight.

The UX may explain or expose these semantics differently by role, but it must not redefine them.

## 003-A baseline

003-A establishes the experience context stack:

```text
Identity
   ↓
Participation / role mode
   ↓
Competition
   ↓
role-specific operational context
   ↓
current task / artifact
```

Judge and Organizer are explicit experience modes rather than one blended navigation tree. Judge experience remains narrow and task-oriented around event context, Panel context, current judging, and temporary own judging history. Organizer experience is organized around Competition operating modes: preparation, live operations, reconciliation, outcomes, and materials/external representations. Current state, historical snapshots, authoritative Versions, and superseded Versions must never be visually conflated. Organizer situational awareness is exception-first and drillable to source evidence.

## 003-B baseline

Judge onboarding is a state-driven event journey:

```text
entry mechanism
    ↓
Competition context
    ↓
Identity establish/reverify
    ↓
current Judge Participation
    ↓
current-event expertise/profile
    ↓
check-in
    ↓
Organizer-governed Panel context
    ↓
derived Ready-to-Judge state
```

QRs, links, event codes, and Panel codes accelerate context but do not grant authority. Returning Judges receive new Competition Participation, check-in remains distinct from registration/authentication, and Panel membership remains Organizer-governed by default. Dual-role people enter explicit Judge mode; shared devices clear prior Judge context; ordinary onboarding closes at Event Completed.

## 003-C baseline

The Judge's live evaluation loop is:

```text
Ready to Judge
      ↓
resolve / confirm current Encounter
      ↓
confirm Team Alias + Division
      ↓
Scorecard Draft
      ↓
score + Notes
      ↓
finish / review
      ↓
explicit Finalize
      ↓
authoritative Scorecard Version
      ↓
return to Panel work
```

Same-Panel/same-Team entry converges on one Encounter. Alias remains canonical and `teamName` is hidden by default during blinded judging. Draft changes are lightweight thought formation with truthful persistence feedback. Presentation end does not finalize the Scorecard; unfinished Drafts may be retained if live operations need to proceed. Finalization is explicit and retry-safe. Amendment is a separate mode with the prior Version authoritative until a successor is finalized. Peer scores, aggregates, Coverage, Rank, and standings remain hidden.

## 003-D baseline

003-D defines Organizer preparation as parallel workstreams coordinated by one derived readiness model:

```text
Competition Draft
      ↓
Competition details
Divisions
Teams + Team attributes / Team Names
Aliases
Rubric
Evaluation Policy
Awards
Judge / Panel preparation
Materials / continuity preparation
      ↓
continuous validation
      ↓
Configuration readiness + Operational warnings
      ↓
Organizer `Mark Ready`
      ↓
Competition Ready
```

Preparation is non-linear rather than a mandatory one-pass wizard. Readiness may look checklist-like but is derived from actual authoritative source state; manually checking a task never substitutes for Team/Division/Alias coherence, a usable authoritative Rubric, valid Evaluation Policy, or other configured gates.

Blocking conditions and operational warnings remain distinct. Structural/evaluation blockers prevent `markReady`; day-of-event risks such as incomplete expected Judge expertise, provisional Panel staffing, or ungenerated paper materials remain warnings unless explicit Competition policy promotes them into hard gates. Configuration readiness and operational staffing readiness are therefore visible together without being conflated.

Team preparation supports bulk intake with preview/validation/exception handling. Extensible Team attributes remain typed/disclosure-controlled metadata; `teamName` is optional, non-unique, non-competitive, and hidden from Judges by default. Alias setup supports safe generation/validation and may surface stale Export impact after corrections. A Judge-safe preview lets Organizers inspect what Judges would see without impersonating Judge authority.

Rubric Drafts and authoritative Rubric Versions remain visually distinct. Evaluation Policy is first-class visible configuration with clear standard defaults, Coverage requirements, ranking precision, and tie semantics rather than hidden constants. Award definitions distinguish rank-derived versus discretionary behavior. Expected Judge preparation and actual event-day check-in remain separate, and final Panel staffing may legitimately remain a live-operation concern.

`Mark Ready` is an explicit lifecycle action only after derived hard gates pass. Non-blocking warnings carry into live-operation handoff. Ready-state changes trigger readiness reassessment; changes that would make readiness invalid explicitly return the Competition to Draft rather than silently leaving a stale Ready state. Working future Draft configurations do not replace the authoritative configuration that Ready currently depends upon.

## Team attribute refinement

The Phase 002 refinement [002-A1 — Team Extensible Attributes & Team Name](../002-concept-specification/002-A1-team-extensible-attributes-team-name-refinement.md) makes descriptive Team metadata extensible without changing the Concept catalog. `teamName` is optional, need not be unique, is distinct from Alias, and has no scoring/ranking effect by default. Judge-facing display is disabled by default during blinded judging because student-created names may inadvertently reveal identity.

## Phase exit target

Phase 003 should end with:

- a coherent role-aware experience architecture;
- explicit Competition and Participation context behavior;
- Judge and Organizer task journeys mapped to the Concept model;
- lifecycle-aware navigation and action availability;
- information-disclosure boundaries expressed in experience terms;
- Organizer exception-first operational patterns;
- clear current-versus-historical presentation rules;
- paper/export/publication workflows mapped into the application experience;
- accessibility/resilience requirements applied across journeys;
- a canonical status/feedback/recovery vocabulary;
- enough stability for visual design/component architecture and system/API/persistence design to proceed without inventing new domain semantics.

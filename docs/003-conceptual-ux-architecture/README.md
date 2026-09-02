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

Combining these further would mix very different cognitive modes such as live Judge scoring and Organizer reconciliation. Splitting them further would create screen/control micro-phases before the information architecture is stable.

## Phase plan

| Group | Topic | Status |
| --- | --- | --- |
| 003-A | [Experience Architecture, Role Modes & Navigation Model](003-A-experience-architecture-role-modes-navigation-model.md) | **Complete** |
| 003-B | [Judge Entry, Identity, Participation & Panel Onboarding](003-B-judge-entry-identity-participation-panel-onboarding.md) | **Complete** |
| 003-C | Judge Encounter, Rubric, Scorecard & Amendment Experience | **Next** |
| 003-D | Organizer Competition Setup, Configuration & Readiness Experience | Planned |
| 003-E | Organizer Judge, Panel, Encounter & Live Operations Experience | Planned |
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

Judge and Organizer are explicit experience modes rather than one blended navigation tree. If an Identity has multiple Participations, switching mode is deliberate and changes disclosure posture as well as available tasks.

Judge experience remains narrow and task-oriented around event context, Panel context, current judging, and temporary own judging history. Organizer experience is organized around Competition operating modes: preparation, live operations, reconciliation, outcomes, and materials/external representations. Domain collections remain available contextually but do not define the whole application as one navigation item per Concept.

Competition lifecycle changes which work is foregrounded. Historical Finalized Competitions default to inspect/trace/export, while exceptional correction is intentionally distinct from ordinary editing. Current state, historical snapshots, authoritative Versions, and superseded Versions must never be visually conflated.

Organizer situational awareness should be exception-first and drillable to source evidence. Competition and role context remain unambiguous for consequential work; deep links or QR codes still resolve Identity/Participation/Access before disclosure. Navigation visibility never substitutes for Access enforcement, and changing context must not silently destroy meaningful working state.

## 003-B baseline

003-B defines Judge onboarding as a state-driven event journey:

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

QRs, links, event codes, and Panel codes are context/navigation accelerators rather than authority. Returning Judges reuse/reverify Identity but receive a new Competition Participation and reconfirm current-event expertise. Check-in is distinct from registration or authentication, and device changes recover the same Participation rather than creating another Judge.

Panel membership remains Organizer-governed by default. A Panel QR/code may confirm or request an intended Panel context but cannot silently self-reassign a Judge. `Ready to Judge` is derived from verified Identity, valid Participation, check-in, required current-event profile information, resolved Panel membership, active Access, and Competition lifecycle; a successful login alone is insufficient.

Dual-role people enter an explicit Judge mode with Judge-safe disclosure rather than a blended Organizer/Judge interface. Shared devices clear prior Judge context. Ordinary onboarding closes at Event Completed; post-event amendments use the narrow correction-access path rather than reopening the event experience. QR/camera use always has an accessible alternative, and degraded connectivity must never cause the UI to falsely claim authoritative Identity/check-in/Access state.

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

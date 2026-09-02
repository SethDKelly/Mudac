# Phase 003 — Conceptual UX Architecture, Information Architecture & Interaction Model

Status: **In Progress**

## Purpose

Phase 001 discovered the application Concepts. Phase 002 specified how those Concepts behave and compose. Phase 003 translates that stable behavioral model into an actor-centered experience architecture before visual design, component design, front-end framework selection, routing implementation, persistence design, or AWS topology.

The governing question is:

> How should Judges and Organizers experience the specified concepts and workflows so that Competition state, authority, privacy, judging context, exceptions, recovery, and official outcomes remain understandable under live-event conditions?

Phase 003 is still conceptual design. It may define experience regions, navigation relationships, role modes, journeys, task states, information hierarchy, interaction contracts, and responsive/degraded behavior. It should not prematurely define React components, URL structures, CSS systems, backend APIs, database tables, or AWS services.

## Why ten subgroupings

Ten groups provide enough separation to keep the two primary actor experiences and the cross-cutting operational concerns coherent:

1. establish the overall experience architecture, role modes, Competition context, and navigation model;
2. design low-friction Judge arrival/participation/Panel onboarding;
3. design the core Judge Encounter, Rubric, Scorecard, finalization, and amendment experience;
4. design Organizer Competition setup and readiness;
5. design Organizer Judge/Panel/Encounter live operations and exception response;
6. design reconciliation, Coverage/Ranking review, Awards, and Finalization;
7. design paper capture, Export/print, and publication workflows;
8. define accessibility, mobile/responsive, interruption, degraded-network, and fallback interaction requirements;
9. consolidate cross-cutting status language, feedback, disclosure/privacy, confirmation, and recovery patterns;
10. reconcile the full experience architecture and determine readiness for visual/system architecture.

Combining these further would mix very different cognitive modes such as live Judge scoring and Organizer reconciliation. Splitting them further would create micro-phases around individual screens or controls before the information architecture is stable.

## Phase plan

| Group | Topic | Status |
| --- | --- | --- |
| 003-A | Experience Architecture, Role Modes & Navigation Model | **Next** |
| 003-B | Judge Entry, Identity, Participation & Panel Onboarding | Planned |
| 003-C | Judge Encounter, Rubric, Scorecard & Amendment Experience | Planned |
| 003-D | Organizer Competition Setup, Configuration & Readiness Experience | Planned |
| 003-E | Organizer Judge, Panel, Encounter & Live Operations Experience | Planned |
| 003-F | Reconciliation, Coverage, Ranking, Awards & Finalization Experience | Planned |
| 003-G | Paper Capture, Export, Print & Publication Experience | Planned |
| 003-H | Accessibility, Mobile, Responsive & Degraded-Mode Interaction Architecture | Planned |
| 003-I | Cross-Cutting Status, Feedback, Privacy, Disclosure & Recovery Patterns | Planned |
| 003-J | Phase 003 Consolidation & UX Architecture Exit Review | Planned |

## Phase 002 input contract

Phase 003 treats the following Phase 002 semantics as authoritative inputs rather than UX choices:

- Competition lifecycle is `Draft → Ready → Active → Event Completed → Finalized`.
- Identity, Participation, Access, and semantic authority remain distinct.
- Judge and Organizer are Participation roles.
- Team administrative identity and Judge-facing Alias are distinct.
- Panel current membership and historical Encounter participation are distinct.
- Effective Encounter participation creates Scorecard obligations.
- One Judge Participation × one Encounter yields one logical Scorecard.
- Scorecards remain bound to one exact Rubric Version.
- Draft, Finalized, and Amendment Draft have distinct authority semantics.
- Judge Notes are private evaluation evidence.
- ordinary Judge private evaluation Access expires at Event Completed.
- Versioning preserves authoritative states; Provenance explains their origin/authority.
- Coverage and Aggregate are independent.
- Ranking is Division-scoped and derived.
- Awards are distinct from Rank.
- Finalization creates a reconstructible Official Outcome Revision.
- Finalization is separate from publication.
- paper and electronic capture share Scorecard semantics.
- operational fallback may change capture channel but never evaluation meaning/weight.

The UX may explain or expose these semantics differently by role, but it must not redefine them.

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

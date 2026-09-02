# Phase 003 — Conceptual UX Architecture, Information Architecture & Interaction Model

Status: **In Progress**

## Purpose

Phase 001 discovered the application Concepts. Phase 002 specified how those Concepts behave and compose. Phase 003 translates that stable behavioral model into an actor-centered experience architecture before visual design, component design, front-end framework selection, routing implementation, persistence design, or AWS topology.

The governing question is:

> How should Judges and Organizers experience the specified concepts and workflows so that Competition state, authority, privacy, judging context, exceptions, recovery, and official outcomes remain understandable under live-event conditions?

Phase 003 remains conceptual design. It may define experience regions, navigation relationships, role modes, journeys, task states, information hierarchy, interaction contracts, and responsive/degraded behavior. It should not prematurely define React components, URL structures, CSS systems, backend APIs, database tables, or AWS services.

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
| 003-E | [Organizer Judge, Panel, Encounter & Live Operations Experience](003-E-organizer-judge-panel-encounter-live-operations-experience.md) | **Complete** |
| 003-F | Reconciliation, Coverage, Ranking, Awards & Finalization Experience | **Next** |
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

Judge onboarding is a state-driven event journey from Competition entry through Identity/reverification, current Judge Participation, expertise/profile confirmation, check-in, Organizer-governed Panel context, and derived `Ready to Judge`. QR/link/code mechanisms accelerate context but never grant authority. Device changes recover the same Participation, Panel membership remains Organizer-governed, dual-role people enter explicit Judge mode, and ordinary onboarding closes at Event Completed.

## 003-C baseline

The Judge live evaluation loop confirms Team Alias + Division before scoring, preserves one Scorecard Draft through criterion scoring and Notes, separates presentation end from evaluation completion, and requires explicit Finalization. Draft persistence is automatic-feeling but truthful; unfinished Drafts may remain while the schedule proceeds. Finalization is retry-safe, amendment is a separate mode, structural attribution errors are escalated rather than edited, and peer scoring/aggregates/Rank remain hidden.

## 003-D baseline

Organizer preparation is a non-linear workspace spanning Competition details, Divisions, Teams and Team attributes, Aliases, Rubric, Evaluation Policy, Awards, Judge/Panel preparation, and materials. Readiness is derived from authoritative source state. Hard configuration blockers remain distinct from operational warnings. `Mark Ready` is explicit after hard gates pass; operational warnings may carry forward. Team Name remains optional/non-competitive and disclosure-controlled, Judge-safe preview supports anonymity review, and working future configuration does not silently replace the authoritative configuration Ready depends upon.

## 003-E baseline

003-E defines Organizer live operations as an exception-first command model:

```text
Competition Ready
      ↓
Judge arrival + readiness
      ↓
Panel formation / composition review
      ↓
Organizer Activate
      ↓
Judge + Panel + Encounter + evaluation operations
      ↓
exception management / degraded-mode continuity
      ↓
Organizer Complete Event
      ↓
Event Completed / reconciliation handoff
```

The default operational surface prioritizes Judge readiness, Panel composition, Encounter state, Scorecard obligation status, recusal/substitution, uncertain Finalization, paper fallback, and other process-integrity exceptions rather than live Ranking. Judge readiness remains derived. Permanent Panel reassignment and one-off Encounter substitution remain distinct, and current roster edits never rewrite historical Encounter participation or silently change already-open Encounter obligations.

Encounter operations preserve starting participants plus explicit adjustments. Recusal is non-zero, finalized evidence cannot disappear through roster edits, duplicate Encounters are prevented, and cancellation remains distinct from invalidation. Organizer evaluation views prioritize status before score content: `Draft — incomplete`, `Draft — complete`, `Finalized`, `Amendment Draft`, `Finalization uncertain`, and `Paper fallback / capture pending` are operationally distinct.

Organizer authority coordinates the process rather than replacing Judge judgment. Organizers may prompt, reassign, record valid absence/recusal, manage Encounter state, support recovery, capture paper evidence, and use governed correction/invalidation paths, but cannot casually edit or Finalize an electronic Judge evaluation as though they authored it. Judge Notes and detailed score content remain deeper investigation material rather than default room-status data.

Mixed electronic/paper operation is permitted by Panel or Judge. Existing electronic Draft plus paper fallback is treated as duplicate-risk to reconcile, not two votes. Live exception alerts drill to source state, consequence, and legitimate action; acknowledging a warning does not erase the underlying condition. `completeEvent` explicitly ends live judging and ordinary Judge private access without implying that paper capture, Coverage, Rank, Awards, or Finalization are complete. Unresolved permitted items carry into reconciliation visibly.

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

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
| 003-F | [Reconciliation, Coverage, Ranking, Awards & Finalization Experience](003-F-reconciliation-coverage-ranking-awards-finalization-experience.md) | **Complete** |
| 003-G | Paper Capture, Export, Print & Publication Experience | **Next** |
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

The default operational surface prioritizes Judge readiness, Panel composition, Encounter state, Scorecard obligation status, recusal/substitution, uncertain Finalization, paper fallback, and other process-integrity exceptions rather than live Ranking. Organizer authority coordinates process integrity without becoming Judge authorship. Mixed paper/electronic operation preserves one logical Judge × Encounter evaluation, and unresolved permitted work carries into reconciliation visibly.

## 003-F baseline

003-F defines the post-event closeout experience as:

```text
Event Completed
      ↓
reconcile authoritative evidence
      ↓
resolve Coverage / eligibility
      ↓
review Division Ranking readiness
      ↓
resolve declared tie requirements
      ↓
confirm / confer Awards
      ↓
Finalization readiness
      ↓
Organizer Finalize
      ↓
Official Outcome Revision
```

Reconciliation remains an Organizer work mode, not a new Competition state, and reconciliation items are projections from underlying source state rather than generic manually-resolved tasks. Evidence authority is resolved before outcome confidence is implied: uncertain Finalization, paper verification, Scorecard amendments, Encounter invalidation/replacement, electronic/paper duplication, and exclusion reasons remain inspectable.

Coverage remains a first-class dimension separate from Aggregate. Coverage exceptions preserve the actual shortfall and require explicit fairness authority; accepted exceptions never fabricate Scorecards. Current corrected Division may differ from historical presented Division, Rubric incompatibility is not silently normalized, and withdrawn Teams retain history while rank eligibility remains explicit.

Ranking may be continuously calculated while a Division remains `not ranking ready`. Ranking readiness is derived from resolved source state, Rank remains non-editable, and every displayed ordering can drill to eligible Scorecards, Criterion responses, Rubric Version, Coverage/exceptions, Provenance, and Evaluation Policy. True ties remain ties unless a predeclared resolver applies; post-hoc tiebreak selection is prohibited.

Rank-derived Awards follow ready Ranking and Organizer confirmation cannot contradict their declared rule. Discretionary Awards remain visibly human decisions, Award cardinality controls tie handling, and required versus optional Awards remain explicit. A source correction that changes Rank makes prior Award confirmation affected/stale rather than silently migrating the recipient.

Finalization readiness is derived from reconciled authoritative state. Finalization is explicit, high consequence, all-or-nothing in domain meaning, and creates an inspectable Official Outcome Revision without publishing results. Post-finalization correction uses an exceptional path in which latest corrected calculations remain distinct from the current official outcome until a successor Official Outcome Revision and any affected Award corrections are explicitly confirmed. Prior official revisions remain historical and external-representation impacts are handed to 003-G.

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

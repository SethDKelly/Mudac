# Phase 003 — Conceptual UX Architecture, Information Architecture & Interaction Model

Status: **In Progress**

## Purpose

Phase 001 discovered the application Concepts. Phase 002 specified how those Concepts behave and compose. Phase 003 translates that stable behavioral model into an actor-centered experience architecture before visual design, component design, front-end framework selection, routing implementation, persistence design, or AWS topology.

The governing question is:

> How should Judges and Organizers experience the specified concepts and workflows so that Competition state, authority, privacy, judging context, exceptions, recovery, physical evidence, and official outcomes remain understandable under live-event conditions?

Phase 003 remains conceptual design. It may define experience regions, navigation relationships, role modes, journeys, task states, information hierarchy, interaction contracts, disclosure, responsive/degraded behavior, and external-representation semantics. It does not yet define React components, URL structures, CSS systems, backend APIs, database tables, artifact technology, or AWS services.

## Why ten subgroupings

Ten groups provide enough separation to keep the primary actor experiences and cross-cutting operational concerns coherent:

1. overall experience architecture, role modes, Competition context, and navigation;
2. low-friction Judge arrival/Participation/Panel onboarding;
3. Judge Encounter, Rubric, Scorecard, Finalization, and amendment;
4. Organizer Competition setup and readiness;
5. Organizer Judge/Panel/Encounter live operations and exception response;
6. reconciliation, Coverage/Ranking review, Awards, and Finalization;
7. paper capture, Export/print, and publication;
8. accessibility, mobile/responsive, interruption, degraded-network, and fallback interaction requirements;
9. cross-cutting status language, feedback, disclosure/privacy, confirmation, and recovery patterns;
10. full UX-architecture consolidation and exit review.

## Phase plan

| Group | Topic | Status |
| --- | --- | --- |
| 003-A | [Experience Architecture, Role Modes & Navigation Model](003-A-experience-architecture-role-modes-navigation-model.md) | **Complete** |
| 003-B | [Judge Entry, Identity, Participation & Panel Onboarding](003-B-judge-entry-identity-participation-panel-onboarding.md) | **Complete** |
| 003-C | [Judge Encounter, Rubric, Scorecard & Amendment Experience](003-C-judge-encounter-rubric-scorecard-amendment-experience.md) | **Complete** |
| 003-D | [Organizer Competition Setup, Configuration & Readiness Experience](003-D-organizer-competition-setup-configuration-readiness-experience.md) | **Complete** |
| 003-E | [Organizer Judge, Panel, Encounter & Live Operations Experience](003-E-organizer-judge-panel-encounter-live-operations-experience.md) | **Complete** |
| 003-F | [Reconciliation, Coverage, Ranking, Awards & Finalization Experience](003-F-reconciliation-coverage-ranking-awards-finalization-experience.md) | **Complete** |
| 003-G | [Paper Capture, Export, Print & Publication Experience](003-G-paper-capture-export-print-publication-experience.md) | **Complete** |
| 003-H | Accessibility, Mobile, Responsive & Degraded-Mode Interaction Architecture | **Next** |
| 003-I | Cross-Cutting Status, Feedback, Privacy, Disclosure & Recovery Patterns | Planned |
| 003-J | Phase 003 Consolidation & UX Architecture Exit Review | Planned |

## Phase 002 input contract

Phase 003 treats the following semantics as authoritative inputs rather than UX choices:

- Competition lifecycle is `Draft → Ready → Active → Event Completed → Finalized`.
- Identity, Participation, Access, and semantic authority remain distinct.
- Judge and Organizer are Competition-scoped Participation roles.
- Team administrative identity and Judge-facing Alias remain distinct.
- Team supports extensible descriptive attributes; `teamName` is optional and non-competitive by default.
- Team attributes have explicit disclosure posture; student-created Team names are hidden from Judges by default during blinded judging.
- Panel current membership and historical Encounter participation remain distinct.
- effective Encounter participants create Scorecard obligations.
- one Judge Participation × one Encounter yields at most one logical Scorecard.
- Scorecards remain bound to one exact Rubric Version.
- Draft, Finalized, and Amendment Draft have distinct authority semantics.
- Judge Notes are private evaluation evidence.
- ordinary Judge private-evaluation Access expires at Event Completed.
- Versioning preserves authoritative states; Provenance explains origin and authority.
- Coverage and Aggregate are independent.
- Ranking is Division-scoped and derived.
- Awards are distinct from Rank.
- Finalization creates a reconstructible Official Outcome Revision.
- Finalization is separate from publication.
- paper and electronic capture share Scorecard semantics.
- operational fallback may change capture channel but never evaluation meaning or weight.
- Export represents identified source state and never becomes source truth merely because it was printed or published.

## Authoritative UX baseline through 003-G

### Experience architecture — 003-A

The experience context stack is:

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

Judge and Organizer are explicit experience modes rather than one blended navigation tree. Current state, historical snapshots, authoritative Versions, and superseded Versions must never be visually conflated. Organizer situational awareness is exception-first and drillable to source evidence.

### Judge onboarding — 003-B

Judge onboarding is a state-driven journey from Competition entry through Identity/reverification, current Judge Participation, expertise/profile confirmation, check-in, Organizer-governed Panel context, and derived `Ready to Judge`. QR/link/code mechanisms accelerate context but never grant authority. Device changes recover the same Participation, and ordinary onboarding closes at Event Completed.

### Judge evaluation — 003-C

The Judge live evaluation loop confirms Team Alias + Division before scoring, preserves one Scorecard Draft through Criterion scoring and Notes, separates presentation completion from evaluation completion, and requires explicit Finalization. Draft persistence is automatic-feeling but truthful; unfinished Drafts may remain while the schedule proceeds. Finalization is retry-safe, amendment is a separate mode, structural attribution errors are escalated rather than edited, and peer scoring/Aggregate/Rank remain hidden.

### Organizer preparation — 003-D

Organizer preparation is a non-linear workspace spanning Competition details, Divisions, Teams and Team attributes, Aliases, Rubric, Evaluation Policy, Awards, Judge/Panel preparation, and materials. Readiness is derived from authoritative source state. Hard configuration blockers remain distinct from operational warnings. Team Name remains optional/non-competitive and disclosure-controlled, and working future configuration never silently replaces the authoritative configuration Ready depends upon.

### Organizer live operations — 003-E

Live operations are exception-first rather than leaderboard-first:

```text
Competition Ready
      ↓
Judge arrival + readiness
      ↓
Panel formation
      ↓
Organizer Activate
      ↓
Encounter / evaluation operations
      ↓
exception and degraded-mode management
      ↓
Organizer Complete Event
      ↓
Event Completed
```

Judge readiness is derived. Permanent Panel reassignment and one-off Encounter substitution are distinct. Current roster edits never rewrite historical Encounter participants. Organizer authority manages process integrity rather than becoming Judge authorship. Mixed paper/electronic operation preserves one logical Judge × Encounter evaluation.

### Reconciliation and Finalization — 003-F

Post-event closeout is:

```text
Event Completed
      ↓
reconcile authoritative evidence
      ↓
resolve Coverage / eligibility
      ↓
review Division Ranking readiness
      ↓
resolve declared ties
      ↓
confirm / confer Awards
      ↓
Finalization readiness
      ↓
Organizer Finalize
      ↓
Official Outcome Revision
```

Reconciliation is an Organizer work mode, not another Competition lifecycle state. Coverage remains separate from Aggregate; accepted Coverage exceptions retain the actual shortfall. Ranking may be continuously calculated without being ranking-ready, Ranking readiness is derived, and Rank is never directly editable. Rank-derived Awards follow ready Ranking while discretionary Awards remain explicit human decisions. Finalization creates an Official Outcome Revision but does not publish it. Corrected latest calculations remain distinct from the current official outcome until a successor Official Outcome Revision is explicitly confirmed.

### Paper capture and external representation — 003-G

Paper intake preserves one authority chain:

```text
physical paper source
      ↓
unique source identity
      ↓
capture Draft
      ↓
verification against physical source
      ↓
authoritative paper-origin Scorecard Version
```

Source collection, transcription, and verification are distinct. The Judge remains evaluation author while the Organizer is capture actor. Capture Draft edits are non-authoritative; after verification, a transcription mistake requires a provenance-preserving capture correction rather than an in-place rewrite. Ambiguous physical Judge intent cannot be resolved by Organizer guesswork. Electronic and paper artifacts for one Judge × Encounter converge onto one logical Scorecard.

Outbound representation preserves a parallel chain:

```text
authoritative source Version/revision
      +
audience / disclosure profile
      +
representation purpose
      ↓
Export
      ↓
preview / validation
      ↓
print / distribute / publish
```

Export represents source truth; it does not replace it. Artifacts can be `Current`, `Stale`, `Superseded`, or withdrawn from current distribution without altering the source. Old artifacts remain attributable to the exact Rubric Version or Official Outcome Revision they represented. Generation and release/publication are separate actions, and Organizer internal visibility does not automatically authorize inclusion in Judge/public representations.

Official-result publication requires an Official Outcome Revision. Ceremony/public disclosure is explicit and may differ; optional Team Name can be used post-event only under an approved disclosure profile. Judge Notes and Judge-linked score detail are not public defaults. A corrected Official Outcome marks dependent publications affected rather than silently rewriting them; a successor publication is deliberately generated/released and the prior publication remains historical.

## Team attribute refinement

[002-A1 — Team Extensible Attributes & Team Name](../002-concept-specification/002-A1-team-extensible-attributes-team-name-refinement.md) makes descriptive Team metadata extensible without changing the Concept catalog. `teamName` is optional, need not be unique, is distinct from Alias, and has no scoring/ranking effect by default. Judge-facing display is disabled by default during blinded judging because student-created names may inadvertently reveal identity.

## Phase exit target

Phase 003 should end with:

- coherent role-aware experience architecture;
- explicit Competition and Participation context behavior;
- Judge and Organizer journeys mapped to the Concept model;
- lifecycle-aware action availability;
- disclosure boundaries expressed in experience terms;
- exception-first operational/reconciliation patterns;
- clear current-versus-historical presentation rules;
- paper capture and external-representation workflows tied to authoritative source state;
- accessibility/resilience requirements applied across all journeys and media;
- canonical status/feedback/recovery vocabulary;
- enough stability for visual/component architecture and system/API/persistence design to proceed without inventing new domain semantics.

# Phase 003 — Conceptual UX Architecture, Information Architecture & Interaction Model

Status: **In Progress**

## Purpose

Phase 003 translates the stable Concept and behavioral model from Phases 001–002 into an actor-centered experience architecture before visual/component, persistence, API, or AWS architecture.

The governing question is:

> How should Judges and Organizers experience the specified concepts and workflows so that Competition state, authority, privacy, judging context, exceptions, recovery, physical evidence, accessibility, and official outcomes remain understandable under real live-event conditions?

Phase 003 may define experience regions, navigation relationships, journeys, task states, information hierarchy, interaction contracts, disclosure, responsive/degraded behavior, accessibility posture, external-representation semantics, and cross-cutting feedback/recovery language. It does not yet choose React components, route structures, CSS systems, persistence technology, synchronization protocols, authentication technology, artifact infrastructure, or AWS services.

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
| 003-H | [Accessibility, Mobile, Responsive & Degraded-Mode Interaction Architecture](003-H-accessibility-mobile-responsive-degraded-mode-interaction-architecture.md) | **Complete** |
| 003-I | [Cross-Cutting Status, Feedback, Privacy, Disclosure & Recovery Patterns](003-I-cross-cutting-status-feedback-privacy-disclosure-recovery-patterns.md) | **Complete** |
| 003-J | Phase 003 Consolidation & UX Architecture Exit Review | **Next** |

## Phase 002 input contract

Phase 003 treats these semantics as authoritative rather than UX choices:

- Competition lifecycle is `Draft → Ready → Active → Event Completed → Finalized`.
- Identity, Participation, Access, and semantic authority remain distinct.
- Team administrative identity and Judge-facing Alias remain distinct.
- Team supports disclosure-controlled extensible descriptive attributes; optional `teamName` is non-competitive by default.
- Panel current membership and historical Encounter participation remain distinct.
- effective Encounter participants create Scorecard obligations.
- one Judge Participation × one Encounter yields at most one logical Scorecard.
- Scorecards use one exact Rubric Version.
- Draft, Finalized, and Amendment Draft have distinct authority semantics.
- Judge Notes are private evaluation evidence.
- ordinary Judge private-evaluation Access expires at Event Completed.
- Versioning preserves authoritative states; Provenance explains origin and authority.
- Coverage and Aggregate are independent; Rank is Division-scoped and derived.
- Awards remain distinct from Rank.
- Finalization creates an Official Outcome Revision and remains separate from publication.
- paper and electronic capture share Scorecard semantics.
- Export represents identified source state and never becomes source truth merely because it was printed or published.
- degraded operation may change interaction/capture channel but never evaluation meaning or weight.

## Authoritative UX baseline through 003-I

### 003-A — experience context

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

Judge and Organizer are explicit modes. Current state, historical snapshots, authoritative Versions, and superseded Versions are never visually conflated. Organizer situational awareness is exception-first and drillable to source evidence.

### 003-B — Judge onboarding

Judge onboarding resolves Competition context, Identity/reverification, current Competition Participation, current-event expertise/profile, check-in, Organizer-governed Panel context, and derived `Ready to Judge`. QR/link/code mechanisms accelerate context but never grant authority. Device changes recover the same Participation, and ordinary onboarding closes at Event Completed.

### 003-C — Judge evaluation

The Judge confirms Team Alias + Division, works in one safely preserved Scorecard Draft, reviews and explicitly Finalizes, and uses a separate amendment mode afterward. Presentation completion does not imply evaluation completion. Unfinished Drafts may persist while the schedule proceeds. Peer scores, Aggregate, Coverage, Rank, and standings remain hidden.

### 003-D — Organizer preparation

Organizer preparation is non-linear and spans Competition details, Divisions, Teams/attributes, Aliases, Rubric, Evaluation Policy, Awards, Judge/Panel preparation, and materials. Readiness is derived from source truth; hard blockers remain distinct from operational warnings. Working future configuration never silently replaces the authoritative configuration that Ready depends upon.

### 003-E — Organizer live operations

Live operations are exception-first rather than leaderboard-first. Judge readiness is derived; Panel composition and Encounter obligations are explainable; permanent Panel reassignment remains distinct from one-off substitution; current roster edits never rewrite historical participants. Organizer authority manages process integrity without becoming Judge authorship. Mixed electronic/paper operation preserves one logical Judge × Encounter evaluation.

### 003-F — reconciliation and Finalization

```text
Event Completed
      ↓
reconcile evidence
      ↓
Coverage / eligibility
      ↓
Ranking readiness
      ↓
tie resolution
      ↓
Awards
      ↓
Finalization readiness
      ↓
Official Outcome Revision
```

Reconciliation remains a work mode, not a lifecycle state. Coverage remains separate from Aggregate. Ranking may be calculable without being ranking-ready, Rank is never manually edited, and true ties use only declared policy. Finalization is explicit, high consequence, reconstructible, and separate from publication. Post-finalization corrected calculations remain distinct from the current official outcome until a successor revision is explicitly confirmed.

### 003-G — paper and external representation

Paper intake preserves `physical source → unique source identity → capture Draft → verification → authoritative paper-origin Scorecard Version`. The Judge remains evaluation author while the Organizer is capture actor. Ambiguous physical intent cannot be guessed, and electronic/paper traces converge onto one logical Scorecard.

External representation preserves `authoritative source Version/revision + audience/disclosure + purpose → Export → preview/validation → print/distribute/publish`. Artifacts can become Current, Stale, Superseded, or withdrawn without changing source history. Generation and publication remain separate, and corrected official outcomes require deliberate successor publication rather than silent rewrite.

### 003-H — accessibility, responsive and degraded operation

Accessibility is semantic parity rather than a separate mode. A reasonable future implementation target is WCAG 2.2 AA across core journeys. Essential work must be operable without mouse, camera, hover, fine-pointer precision, gesture-only interaction, color-only status, or required orientation.

Judge work is phone-primary. Organizer wide-screen density may adapt on narrow screens into `summary → exception → detail → legitimate action`. Interruption/session/device changes recover the same Competition/Participation/resource context instead of duplicating records. Shared-device handoff clears prior private context.

Persistence confidence is truthful. Where later architecture supports disconnected Draft continuation, local working state remains distinct from confirmed authoritative persistence. Finalization and other high-consequence actions require authoritative confirmation; uncertainty never becomes a false `Finalized`, `Completed`, `Invalidated`, `Published`, or similar state. Safe retries converge and stale-state conflicts are surfaced.

Normal electronic, partially degraded, and full-paper operation remain one Competition model. Full fallback preserves Team Alias/Division, Judge, Encounter, exact Rubric Version, scores, Notes, and evaluation weight through an identified paper capture channel.

### 003-I — cross-cutting UX grammar

Status is multidimensional. Domain/workflow state, authority, persistence confidence, readiness, validity/eligibility, version/freshness relationship, issue consequence, disclosure posture, and publication state remain independent even when visually summarized.

Ambiguous words are qualified by subject: `Draft — complete` is not `Scorecard Finalized`; `Encounter Complete` is not `Event Completed`; `Ranking ready` is not `Official`; `Competition Finalized` is not `Published`. `Official` is reserved for declared Competition outcome semantics rather than any authoritative record.

Readiness uses a consistent semantic vocabulary of `Ready`, `Needs attention`, `Warning`, and `Optional / Not configured`, qualified by subject. Issue consequence is separately expressed as Informational, Warning, Blocking, or Critical. Acknowledging an issue never resolves the source state.

Authority feedback distinguishes confirmed, pending/unconfirmed, unknown/could-not-confirm, and stale/conflicting conditions. High-consequence success is reflected persistently in subject state rather than only transient notification. Optimistic UI never invents authoritative success.

Current versus historical information is explicitly labeled. Generated-artifact freshness (`Current`, `Stale`, `Superseded`, `Withdrawn from current distribution`) describes the representation rather than rewriting source history. `Affected` identifies a dependency that requires review without automatically applying a correction.

Missing, recused/excused, invalidated, excluded, superseded, and withdrawn remain distinct. Accepted exceptions retain the actual shortfall/deviation. Confirmation friction scales from ordinary Draft edits through authoritative commitments to exceptional/post-finalization operations, and corrective domain verbs are preferred over ambiguous `Delete`, `Reset`, or `Undo` language.

Disclosure remains a projection of source + Identity/Participation/Access + target audience. Judge-safe, Organizer-sensitive, Ceremony-safe, and Public profiles are purpose-specific rather than one simple sensitivity ladder. Team attributes do not inherit visibility merely by existing; Judge private evaluation evidence remains non-public by default. Role switching changes disclosure context as well as navigation, and deep links/search/previews/exports obey the same boundary.

Recovery messaging identifies attempted action, definitely known state, uncertainty, preserved work, safest next action, and escalation path. Stale-base conflicts never silently overwrite newer authority; session/device recovery re-establishes current Access; wrong-context recovery never relabels meaningful work; paper/electronic duplicate-risk is presented as convergence onto one evaluation; and publication failure never weakens Competition Finalization.

## Team attribute refinement

[002-A1 — Team Extensible Attributes & Team Name](../002-concept-specification/002-A1-team-extensible-attributes-team-name-refinement.md) makes descriptive Team metadata extensible without changing the Concept catalog. `teamName` remains optional, distinct from Alias, non-competitive by default, and hidden from Judges during blinded judging unless disclosure policy explicitly says otherwise.

## Phase exit target

Phase 003 should end with:

- coherent role-aware experience architecture;
- explicit Competition and Participation context behavior;
- Judge and Organizer journeys mapped to the Concept model;
- lifecycle-aware action availability;
- disclosure boundaries expressed in experience terms;
- exception-first operational/reconciliation patterns;
- clear current-versus-historical presentation rules;
- paper capture and external representations tied to authoritative source state;
- accessibility/resilience requirements applied across journeys, devices, and media;
- canonical status, feedback, privacy, confirmation, and recovery vocabulary;
- enough stability for visual/component architecture and system/API/persistence design to proceed without inventing new domain semantics.

003-J performs the final contradiction/coverage review and determines whether those exit conditions have been met.

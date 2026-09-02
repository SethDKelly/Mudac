# Phase 003 — Conceptual UX Architecture, Information Architecture & Interaction Model

Status: **In Progress**

## Purpose

Phase 003 translates the stable Concept and behavioral model from Phases 001–002 into an actor-centered experience architecture before visual/component, persistence, API, or AWS architecture.

The governing question is:

> How should Judges and Organizers experience the specified concepts and workflows so that Competition state, authority, privacy, judging context, exceptions, recovery, physical evidence, accessibility, and official outcomes remain understandable under real live-event conditions?

Phase 003 may define experience regions, navigation relationships, journeys, task states, information hierarchy, interaction contracts, disclosure, responsive/degraded behavior, accessibility posture, and external-representation semantics. It does not yet choose React components, route structures, CSS systems, persistence technology, offline protocols, authentication technology, artifact infrastructure, or AWS services.

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
| 003-I | Cross-Cutting Status, Feedback, Privacy, Disclosure & Recovery Patterns | **Next** |
| 003-J | Phase 003 Consolidation & UX Architecture Exit Review | Planned |

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

## Authoritative UX baseline through 003-H

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

Paper intake preserves:

```text
physical source
      ↓
unique source identity
      ↓
capture Draft
      ↓
verification
      ↓
authoritative paper-origin Scorecard Version
```

The Judge remains evaluation author while the Organizer is capture actor. Ambiguous physical intent cannot be guessed. Electronic and paper traces converge onto one logical Scorecard.

External representation preserves:

```text
authoritative source Version/revision
      +
audience / disclosure profile
      +
purpose
      ↓
Export
      ↓
preview / validation
      ↓
print / distribute / publish
```

Artifacts can become Current, Stale, Superseded, or withdrawn without changing source history. Generation and publication are separate. Corrected official outcomes mark dependent publications affected and require deliberate successor release.

### 003-H — accessibility, responsive and degraded operation

Accessibility is semantic parity rather than a separate mode. A reasonable future implementation target is WCAG 2.2 AA across core journeys. Essential work must be operable without mouse, camera, hover, fine-pointer precision, gesture-only interaction, color-only status, or a required device orientation. QR-dependent flows require non-camera alternatives.

Judge work is phone-primary and must be fully usable on small touch screens. Organizer work may use higher wide-screen density, but narrow views retain a coherent `summary → exception → detail → legitimate action` path rather than becoming unusable miniature tables. Text enlargement, logical structure, keyboard interaction, focus management, meaningful dynamic-status announcements, reduced-motion compatibility, and non-color-only status are cross-role requirements.

Interruption is expected. Returning users re-establish Competition, role, resource, and authority context before consequential continuation. Validation/session changes do not silently erase, finalize, or duplicate work. Device identity never substitutes for Identity/Participation; replacement devices recover the same Participation/Scorecard, shared-device handoff clears prior private context, and lost-device recovery revokes compromised session state without deleting records.

Persistence confidence is truthful. Where later architecture safely supports disconnected Draft continuation, local working state remains distinguishable from server-confirmed persistence. Finalization and Organizer high-consequence actions require authoritative confirmation; connectivity uncertainty never becomes a false `Finalized`, `Completed`, `Invalidated`, `Published`, or similar state. Safe retries converge on the same logical operation and stale-base conflicts are surfaced rather than silently overwritten.

Normal electronic, partially degraded, and full-paper operation remain one Competition model. Full fallback uses the same Team Alias/Division, Judge, Encounter, Rubric Version, Criteria, scores, Notes, and evaluation weight through an identified paper capture channel. Paper and digital external representations must themselves remain accessible/readable and must not rely on color alone. Publication infrastructure failure may leave a Competition Finalized with publication pending; it never weakens Finalization semantics.

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

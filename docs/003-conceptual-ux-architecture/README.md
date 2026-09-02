# Phase 003 — Conceptual UX Architecture, Information Architecture & Interaction Model

Status: **Complete**

Canonical exit baseline: [003-J — Phase 003 Consolidation & UX Architecture Exit Review](003-J-phase-consolidation-ux-architecture-exit-review.md).

## Purpose

Phase 003 translates the stable Concept and behavioral model from Phases 001–002 into an actor-centered experience architecture before visual/component, persistence, API, or AWS architecture.

The governing question is:

> How should Judges and Organizers experience the specified concepts and workflows so that Competition state, authority, privacy, judging context, exceptions, recovery, physical evidence, accessibility, and official outcomes remain understandable under real live-event conditions?

Phase 003 defines experience regions, navigation relationships, journeys, task states, information hierarchy, interaction contracts, disclosure, responsive/degraded behavior, accessibility posture, external-representation semantics, and cross-cutting feedback/recovery language. It deliberately does not choose React components, route structures, CSS systems, persistence technology, synchronization protocols, authentication technology, artifact infrastructure, or AWS services.

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
| 003-J | [Phase 003 Consolidation & UX Architecture Exit Review](003-J-phase-consolidation-ux-architecture-exit-review.md) | **Complete** |

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

## Authoritative Phase 003 UX baseline

### Experience context

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

### Judge journey

```text
Competition entry
      ↓
Identity / current Participation
      ↓
current-event profile + check-in
      ↓
Organizer-governed Panel context
      ↓
Ready to Judge
      ↓
confirm Encounter + Team Alias/Division
      ↓
Scorecard Draft
      ↓
review
      ↓
explicit Finalize
      ↓
authoritative Scorecard Version
      ↓
optional controlled Amendment
```

QR/link/code mechanisms accelerate context but never grant authority. Presentation completion does not imply evaluation completion. Unfinished Drafts may persist while the schedule proceeds. Peer scores, Aggregate, Coverage, Rank, and standings remain hidden. Team Name is hidden by default during blinded judging.

### Organizer journey

```text
Preparation
      ↓
Live Operations
      ↓
Event Completed
      ↓
Reconciliation
      ↓
Coverage / eligibility
      ↓
Ranking readiness
      ↓
Awards
      ↓
Finalization
      ↓
Official Outcome Revision
      ↓
Export / publication / history
```

Preparation is non-linear with derived configuration readiness and separate operational warnings. Live operations and reconciliation are exception-first rather than leaderboard-first. Organizer authority manages process integrity without becoming Judge authorship.

### Evidence and result semantics

Panel current membership and historical Encounter participation remain distinct. Electronic and paper traces for one Judge × Encounter converge onto one logical Scorecard. Paper intake preserves `physical source → source identity → capture Draft → verification → authoritative Scorecard Version`, with Judge authorship distinct from Organizer capture.

Coverage remains separate from Aggregate. Ranking may be calculated without being ranking-ready, Rank is never manually edited, and true ties use only declared policy. Rank-derived Awards follow ready Ranking; discretionary Awards remain explicit human decisions.

Finalization is explicit, high consequence, reconstructible, and separate from publication. It creates an Official Outcome Revision. Post-finalization corrected calculations remain distinct from the current official outcome until a successor revision is explicitly confirmed.

### External representation

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

Artifacts can become Current, Stale, Superseded, Affected, or withdrawn from current distribution without changing source history. Organizer visibility does not imply Judge/public disclosure. Corrected official outcomes require deliberate successor publication rather than silent rewrite.

### Accessibility, responsive, and degraded operation

Accessibility is semantic parity rather than a separate mode. A reasonable future implementation target is WCAG 2.2 AA across core journeys. Essential work must be operable without mouse, camera, hover, fine-pointer precision, gesture-only interaction, color-only status, or required orientation.

Judge work is phone-primary. Organizer wide-screen density adapts on narrow screens into `summary → exception → detail → legitimate action`. Interruption/session/device changes recover the same Competition/Participation/resource context rather than duplicating records, and shared-device handoff clears prior Judge private context.

Persistence confidence is truthful. Disconnected Draft continuation may be supported later only if local working state remains distinct from confirmed authoritative persistence. Finalization and other high-consequence actions require authoritative confirmation; uncertainty never becomes false `Finalized`, `Completed`, `Invalidated`, `Official`, or `Published` state. Safe retries converge and stale-state conflicts are surfaced.

### Cross-cutting UX grammar

Status is multidimensional. Domain/workflow state, authority, persistence confidence, readiness, validity/eligibility, version/freshness relationship, issue consequence, disclosure posture, and publication state remain independent even when visually summarized.

Canonical distinctions include:

```text
Draft complete ≠ Scorecard Finalized
Encounter Complete ≠ Event Completed
Ranking Ready ≠ Official Outcome
Competition Finalized ≠ Published
Issue Acknowledged ≠ Source Resolved
```

Readiness uses `Ready`, `Needs attention`, `Warning`, and `Optional / Not configured`, qualified by subject. Issue consequence is separately Informational, Warning, Blocking, or Critical. `Official` is reserved for declared Competition outcome semantics.

Confirmation friction scales with consequence. Recovery messaging states attempted action, definitely known state, uncertainty, preserved work, safest next action, and escalation path. Disclosure remains a projection of source + current Participation/Access + target audience.

## Exit verdict

**PASS — Phase 003 is complete.**

003-J found no blocking contradiction, missing core journey, or need for another core Concept. The 15-Concept catalog remains stable.

Major seam tests all pass, including:

- current Team state versus historical Encounter presentation;
- current Panel membership versus historical Encounter participation;
- Judge Access expiry versus retained evaluation authorship;
- Amendment Draft versus prior authoritative Scorecard Version;
- Organizer paper capture versus Judge authorship;
- invalidation versus historical retention;
- Coverage versus Aggregate;
- calculated Ranking versus ranking-ready versus official Ranking;
- Finalized Competition versus affected/successor Official Outcome Revisions;
- official outcome versus public publication;
- accessibility versus disclosure;
- degraded operation versus authority certainty.

Known extensions such as formal Stage/Round, student application access/feedback, formal scheduling, notifications, advanced Judge calibration, richer public results, and advanced Award governance remain explicitly deferred rather than accidental gaps.

## Phase 004 handoff

The recommended next phase is **Phase 004 — System, Application, Data & Synchronization Architecture**.

Recommended decomposition:

| Group | Recommended topic |
| --- | --- |
| 004-A | Architectural Drivers, Quality Attributes, Trust Boundaries & Design Authority |
| 004-B | Application Boundaries, Modules, Domain Services & Dependency Architecture |
| 004-C | Data Model, Persistence, Versioning, Provenance & Derived-Projection Architecture |
| 004-D | Identity, Authentication, Participation, Access & Session Architecture |
| 004-E | Commands, Queries, API Contracts, Idempotency & Concurrency |
| 004-F | Draft Persistence, Synchronization, Offline/Degraded Operation & Conflict Recovery |
| 004-G | Export, Paper Capture, Artifact, Publication & External-Representation Architecture |
| 004-H | Front-End State, Navigation, Component-System & Responsive Interaction Architecture |
| 004-I | AWS Runtime, Deployment, Security, Observability, Backup & Operational Architecture |
| 004-J | Phase 004 Consolidation, Threat/Failure Review & Implementation-Readiness Exit |

Phase 004 may choose technologies and mechanisms, but it must not silently redefine the Phase 001–003 lifecycle, authority, one-logical-Scorecard, evidence, Coverage, Ranking, Finalization, disclosure, accessibility, or recovery contracts.

The governing handoff principle is:

> **The user experience may adapt to role, lifecycle, device, accessibility need, connectivity, capture channel, and audience, but those adaptations must never silently change Competition meaning, authority, privacy, evidence weight, or official-outcome semantics.**

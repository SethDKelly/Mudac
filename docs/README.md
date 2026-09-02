# MUDAC Design Documentation

This directory is the canonical design authority for the MUDAC competition application.

The project is being designed using Daniel Jackson's **Concept Design** methodology. Conversation history is working context; the repository is the durable source of truth.

## Phase 001 — Concept Design Foundation

**Status: Complete**

Canonical exit baseline: [001-H — Phase 001 Consolidation & Initial Concept Catalog](001-concept-design/001-H-phase-consolidation-initial-concept-catalog.md).

## Accepted concept catalog

### Core competition concepts

1. Competition
2. Division
3. Team
4. Panel
5. Judging Encounter
6. Rubric
7. Scorecard
8. Award

### Supporting concepts

9. Identity
10. Participation
11. Alias
12. Access
13. Versioning
14. Provenance
15. Export

Aggregation, Evaluation Coverage, Rank, Criterion, Note, Expertise, Panel Membership, Reconciliation, Evaluation Policy, Official Outcome Revision, Team Attribute Definitions, PDF, QR, dashboard/portal structures, status, recovery, and offline mode remain subordinate, derived, policy, process, metadata, representation, UX, or implementation mechanisms rather than standalone Concepts.

## Phase 002 — Concept Specification, Policy & Synchronization Refinement

**Status: Complete**

Canonical exit baseline: [002-I — Phase 002 Consolidation & Specification Exit Review](002-concept-specification/002-I-phase-consolidation-specification-exit-review.md).

Compatible post-exit refinement: [002-A1 — Team Extensible Attributes & Team Name](002-concept-specification/002-A1-team-extensible-attributes-team-name-refinement.md).

### Phase 002 authoritative baseline

- Competition lifecycle is `Draft → Ready → Active → Event Completed → Finalized`.
- Identity, Participation, Access, and semantic authority are distinct.
- Team supports disclosure-controlled extensible descriptive attributes; optional `teamName` remains distinct from Alias and non-competitive by default.
- Panel current membership and historical Encounter participation are distinct.
- effective Encounter participants create Scorecard obligations.
- one Judge Participation × one Encounter yields at most one logical Scorecard.
- every Scorecard uses one exact Rubric Version.
- Drafts are non-authoritative; committed Versions are immutable historical snapshots.
- Judge amendment, transcription correction, structural correction, supersession, and invalidation remain distinct.
- Coverage and Aggregate remain independent.
- default Team Aggregate equally weights eligible authoritative individual Judge Scorecards.
- Rank is Division-scoped and derived.
- Evaluation Policy is reconstructible once judging begins.
- Award remains distinct from Rank.
- Finalization creates an Official Outcome Revision and remains separate from publication.
- Export represents identified source state and does not replace source truth.
- paper and electronic judging share evaluation semantics.
- paper-origin capture is verified against its physical source before official eligibility.
- operational fallback changes capture channel, never evaluation meaning or weight.

## Phase 003 — Conceptual UX Architecture, Information Architecture & Interaction Model

**Status: Complete**

Canonical exit baseline: [003-J — Phase 003 Consolidation & UX Architecture Exit Review](003-conceptual-ux-architecture/003-J-phase-consolidation-ux-architecture-exit-review.md).

| Group | Topic | Status |
| --- | --- | --- |
| 003-A | [Experience Architecture, Role Modes & Navigation Model](003-conceptual-ux-architecture/003-A-experience-architecture-role-modes-navigation-model.md) | **Complete** |
| 003-B | [Judge Entry, Identity, Participation & Panel Onboarding](003-conceptual-ux-architecture/003-B-judge-entry-identity-participation-panel-onboarding.md) | **Complete** |
| 003-C | [Judge Encounter, Rubric, Scorecard & Amendment Experience](003-conceptual-ux-architecture/003-C-judge-encounter-rubric-scorecard-amendment-experience.md) | **Complete** |
| 003-D | [Organizer Competition Setup, Configuration & Readiness Experience](003-conceptual-ux-architecture/003-D-organizer-competition-setup-configuration-readiness-experience.md) | **Complete** |
| 003-E | [Organizer Judge, Panel, Encounter & Live Operations Experience](003-conceptual-ux-architecture/003-E-organizer-judge-panel-encounter-live-operations-experience.md) | **Complete** |
| 003-F | [Reconciliation, Coverage, Ranking, Awards & Finalization Experience](003-conceptual-ux-architecture/003-F-reconciliation-coverage-ranking-awards-finalization-experience.md) | **Complete** |
| 003-G | [Paper Capture, Export, Print & Publication Experience](003-conceptual-ux-architecture/003-G-paper-capture-export-print-publication-experience.md) | **Complete** |
| 003-H | [Accessibility, Mobile, Responsive & Degraded-Mode Interaction Architecture](003-conceptual-ux-architecture/003-H-accessibility-mobile-responsive-degraded-mode-interaction-architecture.md) | **Complete** |
| 003-I | [Cross-Cutting Status, Feedback, Privacy, Disclosure & Recovery Patterns](003-conceptual-ux-architecture/003-I-cross-cutting-status-feedback-privacy-disclosure-recovery-patterns.md) | **Complete** |
| 003-J | [Phase 003 Consolidation & UX Architecture Exit Review](003-conceptual-ux-architecture/003-J-phase-consolidation-ux-architecture-exit-review.md) | **Complete** |

### Phase 003 authoritative UX baseline

The experience context is:

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

Judge onboarding establishes current-event Participation, check-in, Organizer-governed Panel context, and derived readiness. Judge evaluation confirms Team Alias/Division, preserves one Draft through scoring/Notes, uses explicit Finalization, and treats amendment as a separate authority mode. Peer scores and standings remain hidden.

Organizer preparation is non-linear with derived configuration readiness and separate operational warnings. Live operations and reconciliation are exception-first rather than leaderboard-first. Organizer authority manages process integrity without becoming Judge authorship.

Panel membership and historical Encounter participation remain distinct. Paper and electronic traces for the same Judge × Encounter converge on one logical Scorecard. Paper capture preserves `physical source → capture Draft → verification → authoritative Scorecard Version` while Judge authorship remains distinct from Organizer capture.

Coverage remains independent from Aggregate. Ranking may be calculated without being ranking-ready; Rank is never directly edited. Rank-derived and discretionary Award semantics remain distinct. Finalization creates an Official Outcome Revision but does not publish it, and corrected calculations never silently replace a current official revision.

External representation preserves `source Version/revision + audience/disclosure + purpose → Export → preview → print/distribute/publish`. Artifacts may become stale, superseded, affected, or withdrawn without rewriting source history.

Accessibility is semantic parity. Judge work is phone-primary; Organizer work remains coherent on narrow screens through `summary → exception → detail → action`. Keyboard/nonvisual interaction, large text, non-color-only status, QR alternatives, predictable focus, accessible feedback, and a reasonable future WCAG 2.2 AA target are architectural requirements.

Persistence confidence is truthful. Disconnected Draft continuation may be supported later only if local working state remains distinct from authoritative confirmation. High-consequence actions cannot be presented as successful when authority state is unknown. Safe retries converge and stale state does not overwrite newer authority.

Status is multidimensional. Workflow/lifecycle, authority, persistence confidence, readiness, validity/eligibility, freshness, issue consequence, disclosure, and publication remain independent dimensions. Canonical distinctions include `Draft complete ≠ Scorecard Finalized`, `Encounter Complete ≠ Event Completed`, `Ranking Ready ≠ Official Outcome`, and `Competition Finalized ≠ Published`.

### Phase 003 exit result

003-J found no blocking contradiction, missing core journey, or need for another core Concept. Major seams between current/historical state, Panel/Encounter state, Judge Access/authorship, Draft/Finalized/amendment authority, paper capture, Coverage/Aggregate, calculated/official results, Finalization/publication, accessibility/disclosure, and degraded-operation/authority all pass.

Known extensions such as formal Stage/Round, student application access/feedback, formal scheduling, notifications, advanced Judge calibration, richer public results, and advanced Award governance remain explicit future work rather than baseline gaps.

## Recommended Phase 004

The next design layer is recommended as **Phase 004 — System, Application, Data & Synchronization Architecture**.

Proposed groups:

- 004-A — Architectural Drivers, Quality Attributes, Trust Boundaries & Design Authority
- 004-B — Application Boundaries, Modules, Domain Services & Dependency Architecture
- 004-C — Data Model, Persistence, Versioning, Provenance & Derived-Projection Architecture
- 004-D — Identity, Authentication, Participation, Access & Session Architecture
- 004-E — Commands, Queries, API Contracts, Idempotency & Concurrency
- 004-F — Draft Persistence, Synchronization, Offline/Degraded Operation & Conflict Recovery
- 004-G — Export, Paper Capture, Artifact, Publication & External-Representation Architecture
- 004-H — Front-End State, Navigation, Component-System & Responsive Interaction Architecture
- 004-I — AWS Runtime, Deployment, Security, Observability, Backup & Operational Architecture
- 004-J — Phase 004 Consolidation, Threat/Failure Review & Implementation-Readiness Exit

Phase 004 may choose technologies and mechanisms, but must treat the Phase 001–003 lifecycle, authority, evidence, disclosure, accessibility, finality, and recovery semantics as fixed architectural input unless deliberately revisited through the canonical design process.

## Canonical terminology

- **Team** — student group being evaluated; supports extensible descriptive attributes including optional `teamName`.
- **Team Name** — optional descriptive Team attribute; distinct from Alias and non-competitive by default.
- **Panel** — group of Judge Participations intended to evaluate together.
- **Judging Encounter** — one bounded actual Panel–Team evaluation occurrence.
- **Judge Participation** — Competition-scoped Judge capacity.
- **Rubric** — evaluation definition.
- **Scorecard** — one logical Judge evaluation for one Encounter under one Rubric Version.
- **Version** — immutable authoritative snapshot.
- **Provenance** — meaningful origin/authority/change history.
- **Coverage** — sufficiency of qualifying evaluation.
- **Aggregate** — numerical combination of eligible authoritative Scorecards.
- **Rank** — derived Division ordering.
- **Award** — explicit Competition recognition.
- **Official Outcome Revision** — reconstructible authoritative Competition outcome snapshot.
- **Export** — audience-specific external representation tied to identified source state.
- **Alias / Competition Identity** — Judge-facing Team identity used instead of administrative/institutional identity.

## Known architectural boundary

Target deployment remains **GitHub Actions → AWS**. Front-end framework, component/design system, identity provider, API style, database, offline persistence, synchronization/conflict strategy, artifact generation/storage, audit implementation, real-time transport, OCR/scanning, publication infrastructure, accessibility tooling, and AWS service choices follow the completed Concept and UX architecture rather than drive it.

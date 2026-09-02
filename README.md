# MUDAC Competition Demo

MUDAC is a documentation-first design effort for a web application that supports live student data competitions, with MinneMUDAC as the initial reference context. The product is intended to replace or augment paper-heavy judging operations while preserving fairness, judge independence, accessibility, auditability, and operational resilience.

The design is being developed using Daniel Jackson's **Concept Design** methodology. Product purpose, Concepts, behavioral specifications, and conceptual UX architecture are now stabilized before system, persistence, component, and cloud architecture.

## Product intent

Student Teams analyze a supplied dataset and present findings and methodology to Panels of volunteer Judges. Each Judge independently completes a Rubric-based Scorecard for a Team during a Judging Encounter. Eligible authoritative Scorecards are combined under explicit Evaluation Policy to support Coverage assessment, Division-scoped ranking, Awards, and controlled official closeout.

Judge and Organizer are Competition-scoped Participation roles rather than permanent Identity types. Students are currently Competition participants and beneficiaries, not application actors.

Teams may carry extensible descriptive attributes. The initial standard optional attribute is `teamName`, allowing students to choose a memorable name without changing stable Team identity, Division, Alias, evaluation, or ranking semantics. Student-created Team names are hidden from Judges by default during blinded judging; Alias remains the Judge-facing Competition Identity.

## Core design principles

- **Independent judgment** — each Judge authors an individual Scorecard; Panel and Team results are derived.
- **Traceable aggregation** — outcomes remain decomposable to eligible Scorecards, Criteria, Rubric Versions, Provenance, and Evaluation Policy.
- **Controlled identity disclosure** — Judge-visible identity uses Alias + Division; optional Team metadata remains separately disclosure-controlled.
- **Extensible Team metadata without hidden rules** — descriptive attributes do not automatically gain scoring/ranking semantics.
- **Configurable competition policy** — Divisions, Rubrics, Awards, Panel composition, Coverage, precision, and tie behavior are configuration rather than constants.
- **Controlled finality** — authoritative state is correctable through Versioning and Provenance instead of silent overwrite.
- **Authority preservation** — Organizer/system authority does not silently substitute for Judge judgment.
- **Process integrity over Organizer score control** — live administration coordinates operations without becoming Judge authorship.
- **Capture-channel parity** — paper and electronic judging share evaluation semantics and converge on one logical Judge × Encounter evaluation.
- **Coverage before outcome confidence** — Aggregate and sufficiency of judging remain separate.
- **Explainable ranking** — Rank is derived and never directly edited.
- **Calculated is not official** — a Ranking may exist while not ranking-ready; latest corrected calculations do not silently replace an official outcome.
- **Explicit official closeout** — Finalization produces a reconstructible Official Outcome Revision.
- **Official is not automatically public** — result publication remains a separate release action.
- **Traceable external representation** — printed/downloaded/published artifacts stay tied to exact source state and audience disclosure.
- **Accessibility as semantic parity** — alternate input, assistive technology, viewport, device, or capture channel preserves Competition meaning and authority.
- **Paper continuity** — paper is a first-class accessibility/continuity path and converges on the same Scorecard model.
- **Role-aware experience** — Participation context determines Judge/Organizer mode and disclosure posture.
- **Derived readiness** — Competition, Ranking, and Finalization readiness come from source state and policy, not checkboxes.
- **Exception-first operations** — Organizer live/reconciliation views prioritize unresolved process/evidence/fairness conditions over leaderboard spectacle.
- **Draft-safe judging** — evaluation remains a non-authoritative Draft until explicit Finalization; amendment is separate afterward.
- **Mobile-first judging** — Judge workflow targets personal smartphones under live-event conditions.
- **Truthful persistence and authority** — connectivity uncertainty is never presented as confirmed Finalization, lifecycle transition, correction, or publication.
- **Multidimensional status** — workflow, authority, readiness, validity, freshness, severity, disclosure, and publication remain distinct even when visually summarized.
- **Qualified finality language** — `Ready`, `Complete`, `Finalized`, `Current`, `Official`, `Published`, and `Resolved` are qualified by subject whenever ambiguity is possible.
- **Privacy by lifecycle and representation** — ordinary Judge private-evaluation access ends with live judging, and every view/export/search result applies its target disclosure context.
- **Recovery without semantic drift** — recovery preserves work and explains known state without silently overwriting newer authority, relabeling context, or creating duplicate evaluation weight.
- **Technology follows semantics** — frameworks, databases, offline libraries, APIs, and AWS services must satisfy the Concept/UX contracts rather than redefine them.

## Accepted concept catalog

### Core competition concepts

- Competition
- Division
- Team
- Panel
- Judging Encounter
- Rubric
- Scorecard
- Award

### Supporting concepts

- Identity
- Participation
- Alias
- Access
- Versioning
- Provenance
- Export

Aggregation, Coverage, Rank, Criterion, Note, Expertise, Panel Membership, Reconciliation, Evaluation Policy, Official Outcome Revision, Team Attribute Definitions, status, recovery, publication, QR/PDF, and offline mode remain subordinate/derived/policy/process/metadata/representation/implementation mechanisms rather than standalone Concepts.

## Design status

**Phase 001 — Concept Design Foundation: Complete.**

Canonical exit: [`001-H`](docs/001-concept-design/001-H-phase-consolidation-initial-concept-catalog.md).

**Phase 002 — Concept Specification, Policy & Synchronization Refinement: Complete.**

Canonical exit: [`002-I`](docs/002-concept-specification/002-I-phase-consolidation-specification-exit-review.md).

Compatible refinement: [`002-A1`](docs/002-concept-specification/002-A1-team-extensible-attributes-team-name-refinement.md).

**Phase 003 — Conceptual UX Architecture, Information Architecture & Interaction Model: Complete.**

Canonical exit: [`003-J`](docs/003-conceptual-ux-architecture/003-J-phase-consolidation-ux-architecture-exit-review.md).

| Group | Topic | Status |
| --- | --- | --- |
| 003-A | [Experience Architecture, Role Modes & Navigation Model](docs/003-conceptual-ux-architecture/003-A-experience-architecture-role-modes-navigation-model.md) | Complete |
| 003-B | [Judge Entry, Identity, Participation & Panel Onboarding](docs/003-conceptual-ux-architecture/003-B-judge-entry-identity-participation-panel-onboarding.md) | Complete |
| 003-C | [Judge Encounter, Rubric, Scorecard & Amendment Experience](docs/003-conceptual-ux-architecture/003-C-judge-encounter-rubric-scorecard-amendment-experience.md) | Complete |
| 003-D | [Organizer Competition Setup, Configuration & Readiness Experience](docs/003-conceptual-ux-architecture/003-D-organizer-competition-setup-configuration-readiness-experience.md) | Complete |
| 003-E | [Organizer Judge, Panel, Encounter & Live Operations Experience](docs/003-conceptual-ux-architecture/003-E-organizer-judge-panel-encounter-live-operations-experience.md) | Complete |
| 003-F | [Reconciliation, Coverage, Ranking, Awards & Finalization Experience](docs/003-conceptual-ux-architecture/003-F-reconciliation-coverage-ranking-awards-finalization-experience.md) | Complete |
| 003-G | [Paper Capture, Export, Print & Publication Experience](docs/003-conceptual-ux-architecture/003-G-paper-capture-export-print-publication-experience.md) | Complete |
| 003-H | [Accessibility, Mobile, Responsive & Degraded-Mode Interaction Architecture](docs/003-conceptual-ux-architecture/003-H-accessibility-mobile-responsive-degraded-mode-interaction-architecture.md) | Complete |
| 003-I | [Cross-Cutting Status, Feedback, Privacy, Disclosure & Recovery Patterns](docs/003-conceptual-ux-architecture/003-I-cross-cutting-status-feedback-privacy-disclosure-recovery-patterns.md) | Complete |
| 003-J | [Phase 003 Consolidation & UX Architecture Exit Review](docs/003-conceptual-ux-architecture/003-J-phase-consolidation-ux-architecture-exit-review.md) | Complete |

## Current experience baseline

Judge experience:

```text
Competition entry
      ↓
Identity / current Participation
      ↓
check-in / Panel context
      ↓
Ready to Judge
      ↓
Encounter + Team Alias/Division
      ↓
Scorecard Draft
      ↓
explicit Finalize
      ↓
optional controlled Amendment
```

Organizer experience:

```text
Preparation / derived readiness
      ↓
Live exception-first operations
      ↓
Event Completed
      ↓
Evidence reconciliation
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

Paper capture uses `physical source → unique source reference → capture Draft → verification → authoritative Scorecard Version`. External representation uses `authoritative source Version/Official Outcome Revision + audience/disclosure + purpose → Export → preview/validation → print/distribute/publish`.

Accessibility/resilience applies across those same journeys. Judge work is phone-primary; Organizer density adapts to narrow `summary → exception → detail → action` workflows. Keyboard/nonvisual interaction, large text, QR alternatives, non-color-only status, predictable focus, accessible feedback, and a reasonable future WCAG 2.2 AA target are architectural requirements.

Status is multidimensional: workflow, authority, persistence confidence, readiness, eligibility, freshness, severity, disclosure, and publication remain distinct. `Draft complete` does not imply `Scorecard Finalized`; `Ranking Ready` does not imply `Official`; `Competition Finalized` does not imply `Published`.

Phase 003 exit review found no blocking contradiction, missing core journey, or need for an additional Concept. Known extensions—formal Stage/Round, student application access/feedback, formal scheduling, notifications, advanced Judge calibration, richer public results, and advanced Award governance—remain explicitly deferred.

## Recommended next phase

**Phase 004 — System, Application, Data & Synchronization Architecture**

Recommended structure:

1. 004-A — Architectural Drivers, Quality Attributes, Trust Boundaries & Design Authority
2. 004-B — Application Boundaries, Modules, Domain Services & Dependency Architecture
3. 004-C — Data Model, Persistence, Versioning, Provenance & Derived-Projection Architecture
4. 004-D — Identity, Authentication, Participation, Access & Session Architecture
5. 004-E — Commands, Queries, API Contracts, Idempotency & Concurrency
6. 004-F — Draft Persistence, Synchronization, Offline/Degraded Operation & Conflict Recovery
7. 004-G — Export, Paper Capture, Artifact, Publication & External-Representation Architecture
8. 004-H — Front-End State, Navigation, Component-System & Responsive Interaction Architecture
9. 004-I — AWS Runtime, Deployment, Security, Observability, Backup & Operational Architecture
10. 004-J — Phase 004 Consolidation, Threat/Failure Review & Implementation-Readiness Exit

Phase 004 may select concrete mechanisms and technologies, but the lifecycle, authority, evidence, one-logical-Scorecard, Coverage/Ranking, Finalization, disclosure, accessibility, and recovery contracts from Phases 001–003 are architectural inputs rather than implementation suggestions.

## Repository documentation convention

The repository—not chat history—is the durable design baseline. See [`docs/README.md`](docs/README.md) for the canonical documentation authority.

## Architecture boundary condition

The intended deployment boundary remains **GitHub Actions → AWS**. Front-end framework, component/design system, identity provider, API style, database, offline persistence, synchronization/conflict strategy, artifact generation/storage, audit implementation, real-time transport, OCR/scanning, publication infrastructure, accessibility tooling, and AWS service choices follow the completed Concept and UX architecture rather than drive it.

## Status

This repository remains in **design**, not production implementation. **Phase 003 is complete; Phase 004 system/application architecture is the recommended next design layer.**

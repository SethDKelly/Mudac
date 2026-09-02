# MUDAC Competition Demo

MUDAC is a documentation-first design effort for a web application that supports live student data competitions, with MinneMUDAC as the initial reference context. The product is intended to replace or augment paper-heavy judging operations while preserving fairness, judge independence, accessibility, auditability, and operational resilience.

The design is being developed using Daniel Jackson's **Concept Design** methodology. Product purpose, Concepts, behavioral specifications, and experience architecture are being stabilized before component, persistence, and cloud architecture.

## Product intent

Student Teams analyze a supplied dataset and present findings and methodology to Panels of volunteer Judges. Each Judge independently completes a Rubric-based Scorecard for a Team during a Judging Encounter. Eligible authoritative Scorecards are combined under explicit Evaluation Policy to support Coverage assessment, Division-scoped ranking, competition Awards, and controlled official closeout.

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
- **Capture-channel parity** — paper and electronic judging share evaluation semantics.
- **Coverage before outcome confidence** — Aggregate and sufficiency of judging remain separate.
- **Explainable ranking** — Rank is derived and never directly edited.
- **Calculated is not official** — a Ranking may exist while not ranking-ready; latest corrected calculations do not silently replace an official outcome.
- **Explicit official closeout** — Finalization produces a reconstructible Official Outcome Revision.
- **Official is not automatically public** — result publication remains a separate release action.
- **Traceable external representation** — printed/downloaded/published artifacts stay tied to exact source state and audience disclosure.
- **Paper continuity** — paper is a first-class accessibility/continuity path and converges on the same Scorecard model.
- **Role-aware experience** — Participation context determines Judge/Organizer mode and disclosure posture.
- **Derived readiness** — Competition, Ranking, and Finalization readiness come from source state and policy, not checkboxes.
- **Exception-first operations** — Organizer live/reconciliation views prioritize unresolved process/evidence/fairness conditions over leaderboard spectacle.
- **Draft-safe judging** — evaluation remains a non-authoritative Draft until explicit Finalization; amendment is separate afterward.
- **Mobile-first judging** — Judge workflow targets personal smartphones under live-event conditions.
- **Privacy by lifecycle** — ordinary Judge private-evaluation access ends when live judging ends.
- **Operational resilience** — interruption, device/network loss, mixed-mode operation, unfinished Drafts, and paper fallback are expected conditions.
- **Technology independence during design** — AWS/GitHub Actions are boundary conditions; concrete services remain deferred.

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

Aggregation, Coverage, Rank, Criterion, Note, Expertise, Panel Membership, Reconciliation, Evaluation Policy, Official Outcome Revision, and Team Attribute Definitions remain subordinate/derived/policy/process/metadata mechanisms rather than standalone Concepts.

## Design status

**Phase 001 — Concept Design Foundation: Complete.**

Canonical exit: [`001-H`](docs/001-concept-design/001-H-phase-consolidation-initial-concept-catalog.md).

**Phase 002 — Concept Specification, Policy & Synchronization Refinement: Complete.**

Canonical exit: [`002-I`](docs/002-concept-specification/002-I-phase-consolidation-specification-exit-review.md).

Compatible refinement: [`002-A1`](docs/002-concept-specification/002-A1-team-extensible-attributes-team-name-refinement.md).

**Phase 003 — Conceptual UX Architecture, Information Architecture & Interaction Model: In Progress.**

| Group | Topic | Status |
| --- | --- | --- |
| 003-A | [Experience Architecture, Role Modes & Navigation Model](docs/003-conceptual-ux-architecture/003-A-experience-architecture-role-modes-navigation-model.md) | **Complete** |
| 003-B | [Judge Entry, Identity, Participation & Panel Onboarding](docs/003-conceptual-ux-architecture/003-B-judge-entry-identity-participation-panel-onboarding.md) | **Complete** |
| 003-C | [Judge Encounter, Rubric, Scorecard & Amendment Experience](docs/003-conceptual-ux-architecture/003-C-judge-encounter-rubric-scorecard-amendment-experience.md) | **Complete** |
| 003-D | [Organizer Competition Setup, Configuration & Readiness Experience](docs/003-conceptual-ux-architecture/003-D-organizer-competition-setup-configuration-readiness-experience.md) | **Complete** |
| 003-E | [Organizer Judge, Panel, Encounter & Live Operations Experience](docs/003-conceptual-ux-architecture/003-E-organizer-judge-panel-encounter-live-operations-experience.md) | **Complete** |
| 003-F | [Reconciliation, Coverage, Ranking, Awards & Finalization Experience](docs/003-conceptual-ux-architecture/003-F-reconciliation-coverage-ranking-awards-finalization-experience.md) | **Complete** |
| 003-G | [Paper Capture, Export, Print & Publication Experience](docs/003-conceptual-ux-architecture/003-G-paper-capture-export-print-publication-experience.md) | **Complete** |
| 003-H | Accessibility, Mobile, Responsive & Degraded-Mode Interaction Architecture | **Next** |
| 003-I | Cross-Cutting Status, Feedback, Privacy, Disclosure & Recovery Patterns | Planned |
| 003-J | Phase 003 Consolidation & UX Architecture Exit Review | Planned |

See [`docs/README.md`](docs/README.md) for the canonical documentation index and [`docs/003-conceptual-ux-architecture/README.md`](docs/003-conceptual-ux-architecture/README.md) for the Phase 003 plan.

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
Export / publication
```

Paper capture uses:

```text
physical source
      ↓
unique source reference
      ↓
capture Draft
      ↓
verification
      ↓
authoritative Scorecard Version
```

The Judge remains evaluation author while the Organizer is capture actor. Paper ambiguity is never resolved by Organizer guesswork, and electronic/paper artifacts for one Judge × Encounter converge onto one logical Scorecard.

External representation uses:

```text
authoritative source Version / Official Outcome Revision
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

Artifacts may become stale/superseded without changing source history. Generating an artifact is distinct from releasing or publishing it. Official result publication requires an Official Outcome Revision. Corrected official outcomes mark prior publications affected and require deliberate successor release rather than silent rewrite.

## Repository documentation convention

The repository—not chat history—is the durable design baseline. Each completed design grouping is added to `/docs` and canonical indexes are advanced immediately.

## Architecture boundary condition

The intended deployment boundary remains **GitHub Actions → AWS**. Front-end framework, component system, identity provider, API style, database, offline persistence, artifact generation/storage, audit implementation, real-time transport, OCR/scanning, publication infrastructure, and AWS service choices follow the behavioral and UX architecture rather than drive it.

## Status

This repository remains in **design**, not production implementation. **003-H — Accessibility, Mobile, Responsive & Degraded-Mode Interaction Architecture is next.**

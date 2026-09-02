# MUDAC Competition Demo

MUDAC is a documentation-first design effort for a web application that supports live student data competitions, with MinneMUDAC as the initial reference context. The product is intended to replace or augment paper-heavy judging operations while preserving fairness, judge independence, accessibility, auditability, and operational resilience.

The design is being developed using Daniel Jackson's **Concept Design** methodology. The repository intentionally establishes product purpose, Concepts, behavioral specifications, and experience architecture before component or cloud architecture so implementation choices are derived from stable behavior rather than screens, tables, or framework conventions.

## Product intent

Student Teams analyze a supplied dataset and present findings and methodology to Panels of volunteer Judges. Each Judge independently completes a Rubric-based Scorecard for a Team during a Judging Encounter. Eligible authoritative Scorecards are combined under explicit Evaluation Policy to support Coverage assessment, Division-scoped ranking, competition Awards, and controlled official closeout.

Primary human roles are Organizer, Judge, and technical Administrator. Judge and Organizer are Competition-scoped Participation roles rather than permanent Identity types. Students are currently Competition participants and beneficiaries, not application actors.

Teams may carry extensible descriptive attributes. The initial standard optional attribute is `teamName`, allowing students to choose a memorable Team name without changing the Team's stable identity, Division, Alias, evaluation, or ranking semantics. Student-created Team names are not Judge-visible by default during blinded judging because they may inadvertently reveal identity; Alias remains the Judge-facing Competition Identity.

## Core design principles

- **Independent judgment** — each Judge authors an individual Scorecard; Panel and Team results are derived.
- **Traceable aggregation** — official outcomes remain decomposable to eligible Scorecards, Rubric Criteria, Versions, Provenance, and policy.
- **Controlled identity disclosure** — Judges see Team Alias and Division rather than institutional identity; optional Team names remain separately disclosure-controlled.
- **Extensible Team metadata without hidden rules** — descriptive Team attributes can grow without automatically gaining scoring, ranking, or access semantics.
- **Configurable competition policy** — Divisions, Rubrics, Awards, Panel composition, scoring, Coverage, precision, and tie behavior are not hard-coded constants.
- **Controlled finality** — authoritative state may be corrected through explicit Versioning and Provenance rather than silent overwrite.
- **Authority preservation** — correction rights follow the meaning of the underlying fact; Organizer or technical authority does not silently replace Judge judgment.
- **Process integrity over Organizer score control** — live administration coordinates Judges, Panels, Encounters, obligations, and recovery without turning operational authority into Judge authorship.
- **Capture-channel parity** — paper and electronic judging share evaluation semantics while Provenance preserves capture differences.
- **Coverage before outcome confidence** — numerical Aggregate and sufficiency of judging remain separate.
- **Explainable ranking** — Ranking is derived from eligible evidence under identifiable Evaluation Policy, never directly edited.
- **Calculated is not official** — Rankings may be continuously derived while not ranking-ready; corrected latest calculations do not silently replace a previously official outcome.
- **Explicit official closeout** — Finalization is a reconciled Organizer decision producing a reconstructible Official Outcome Revision.
- **Official is not automatically public** — result publication/disclosure is separate from internal Finalization.
- **Traceable external representation** — printed/downloaded/published material stays tied to identified source state and audience disclosure rules.
- **Paper continuity** — paper judging is a first-class continuity/accessibility path and converges onto the same Scorecard/evaluation model.
- **Role-aware experience** — Identity is not a permanent role; Competition Participation determines Judge/Organizer experience context.
- **Derived readiness** — Competition, Ranking, and Finalization readiness are established from authoritative source state and explicit policy, not manually checked completion boxes.
- **Exception-first live operations and reconciliation** — Organizer experiences prioritize unresolved process/evidence/fairness conditions before leaderboard presentation.
- **Draft-safe judging** — a Judge's evaluation remains one safely preserved non-authoritative Draft until explicit Finalization; amendment is a separate controlled mode afterward.
- **Mobile-first judging** — the primary Judge workflow targets personal smartphones under live-event conditions.
- **Privacy by lifecycle** — ordinary Judge access to private Scorecards, Notes, and judging history ends when live judging ends while Organizer-governed records remain retained.
- **Operational resilience** — interruption, connectivity loss, device loss, mixed-mode judging, unfinished Drafts, and paper fallback are expected operating conditions.
- **Technology independence during design** — AWS and GitHub Actions are boundary conditions; specific infrastructure remains deferred.

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

Aggregation, Evaluation Coverage, Rank, Criterion, Note, Expertise, Panel Membership, Reconciliation, Evaluation Policy, Official Outcome Revision, and Team Attribute Definitions remain subordinate, derived, policy, process, metadata, or projection mechanisms rather than standalone Concepts.

## Design status

**Phase 001 — Concept Design Foundation: Complete.**

Canonical exit: [`001-H`](docs/001-concept-design/001-H-phase-consolidation-initial-concept-catalog.md).

**Phase 002 — Concept Specification, Policy & Synchronization Refinement: Complete.**

Canonical exit: [`002-I`](docs/002-concept-specification/002-I-phase-consolidation-specification-exit-review.md).

A compatible post-exit refinement, [`002-A1`](docs/002-concept-specification/002-A1-team-extensible-attributes-team-name-refinement.md), makes Team descriptive attributes explicitly extensible and introduces optional `teamName` while preserving the Phase 002 concept catalog and exit result.

**Phase 003 — Conceptual UX Architecture, Information Architecture & Interaction Model: In Progress.**

| Group | Topic | Status |
| --- | --- | --- |
| 003-A | [Experience Architecture, Role Modes & Navigation Model](docs/003-conceptual-ux-architecture/003-A-experience-architecture-role-modes-navigation-model.md) | **Complete** |
| 003-B | [Judge Entry, Identity, Participation & Panel Onboarding](docs/003-conceptual-ux-architecture/003-B-judge-entry-identity-participation-panel-onboarding.md) | **Complete** |
| 003-C | [Judge Encounter, Rubric, Scorecard & Amendment Experience](docs/003-conceptual-ux-architecture/003-C-judge-encounter-rubric-scorecard-amendment-experience.md) | **Complete** |
| 003-D | [Organizer Competition Setup, Configuration & Readiness Experience](docs/003-conceptual-ux-architecture/003-D-organizer-competition-setup-configuration-readiness-experience.md) | **Complete** |
| 003-E | [Organizer Judge, Panel, Encounter & Live Operations Experience](docs/003-conceptual-ux-architecture/003-E-organizer-judge-panel-encounter-live-operations-experience.md) | **Complete** |
| 003-F | [Reconciliation, Coverage, Ranking, Awards & Finalization Experience](docs/003-conceptual-ux-architecture/003-F-reconciliation-coverage-ranking-awards-finalization-experience.md) | **Complete** |
| 003-G | Paper Capture, Export, Print & Publication Experience | **Next** |
| 003-H | Accessibility, Mobile, Responsive & Degraded-Mode Interaction Architecture | Planned |
| 003-I | Cross-Cutting Status, Feedback, Privacy, Disclosure & Recovery Patterns | Planned |
| 003-J | Phase 003 Consolidation & UX Architecture Exit Review | Planned |

See [`docs/README.md`](docs/README.md) for the canonical documentation index and [`docs/003-conceptual-ux-architecture/README.md`](docs/003-conceptual-ux-architecture/README.md) for the Phase 003 plan.

## Current behavioral baseline

```text
Competition:
Draft → Ready → Active → Event Completed → Finalized

Identity → Participation → Access

Judge Participation → Panel
Panel + Team → Judging Encounter
Encounter → effective Judge obligations

Authoritative Rubric Version
        ↓
one Judge × one Encounter
        ↓
logical Scorecard
        ↓
Versioning + Provenance
        ↓
eligible authoritative evidence
        ↓
Coverage + Aggregate
        ↓
Division Ranking
        ↓
Organizer reconciliation
        ↓
Award decisions
        ↓
Competition Finalization
        ↓
Official Outcome Revision
        ↓
Export / approved external representation
```

## Current experience baseline

Judge onboarding establishes Competition context, Identity/reverification, current Judge Participation, expertise/profile, check-in, Organizer-governed Panel context, and derived `Ready to Judge`. The Judge evaluation experience then confirms Team Alias + Division, preserves one Draft through scoring/Notes, separates presentation end from evaluation completion, and requires explicit Finalization. Amendment is a separate controlled mode and peer scoring/standings remain hidden.

Organizer preparation is non-linear and uses derived readiness rather than manual checklist truth. Organizer live operations are exception-first and center Judge readiness, Panel composition, Encounter/obligation state, unfinished or uncertain Scorecards, recusal/substitution, recovery, and paper/degraded-mode continuity rather than live Rank. Organizer authority manages process integrity without becoming Judge authorship.

After Event Completed, Organizer reconciliation proceeds:

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
Finalize Competition
      ↓
Official Outcome Revision
```

Reconciliation is a work mode rather than another Competition lifecycle state, and closeout issues remain projections from source truth. Paper verification, Scorecard amendments, Finalization uncertainty, invalidation/replacement, duplicate electronic/paper artifacts, Coverage shortfalls, Division corrections, Rubric incompatibility, ties, and Awards remain semantically distinct.

Coverage remains separate from Aggregate. Accepted Coverage exceptions preserve the real shortfall instead of fabricating evidence. Ranking may be calculated before it is ranking-ready; ranking readiness is derived, Rank cannot be directly edited, and rankings remain explainable down to eligible Scorecards, Criteria, Rubric Versions, Provenance, Coverage/exceptions, and Evaluation Policy. Tie resolution uses only declared policy rather than post-hoc rules.

Rank-derived Awards follow ready Ranking; discretionary Awards remain explicit human decisions. Source changes make existing Award confirmations affected rather than silently migrating recipients. Finalization is a deliberate, high-consequence, all-or-nothing transition that creates an inspectable Official Outcome Revision but does not publish results.

Post-finalization correction retains prior official revisions. Corrected latest calculations and the current official outcome remain separately visible until the Organizer explicitly confirms a successor Official Outcome Revision and resolves any affected Awards. External-material regeneration/publication consequences are handed into 003-G.

## Repository documentation convention

The repository—not chat history—is the durable design baseline. Each completed design grouping is added to `/docs` and the canonical indexes are advanced immediately.

## Architecture boundary condition

The intended deployment boundary remains **GitHub Actions → AWS**. Front-end framework, component system, identity provider, API style, database, offline persistence, artifact generation/storage, audit implementation, real-time transport, and AWS service choices will follow the behavioral and UX architecture rather than drive it.

## Status

This repository remains in **design**, not production implementation. Phase 003 is translating the completed Concept specifications into actor-centered UX and information architecture; **003-G is next**.

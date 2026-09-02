# MUDAC Competition Demo

MUDAC is a documentation-first design effort for a web application that supports live student data competitions, with MinneMUDAC as the initial reference context. The product is intended to replace or augment paper-heavy judging operations while preserving fairness, judge independence, accessibility, auditability, and operational resilience.

The design is being developed using Daniel Jackson's **Concept Design** methodology. The repository intentionally begins with product and conceptual design before UI component design or cloud architecture so that implementation choices are derived from stable behavioral concepts rather than from screens, database tables, or framework conventions.

## Product intent

Student Teams analyze a supplied dataset, perform statistical and/or machine-learning work, and present their findings and methodology to Panels of volunteer Judges. Each Judge independently completes a Rubric-based Scorecard for a Team during a Judging Encounter. Those Scorecards are aggregated across repeated Encounters to support Division-scoped ranking and competition Awards.

Primary human roles are Organizer, Judge, and technical Administrator. Judge and Organizer are Competition-scoped Participation roles rather than permanent Identity types. Students are currently competition participants and beneficiaries, not application actors.

## Core design principles

- **Independent judgment** — each Judge authors an individual Scorecard; Panel and Team scores are derived.
- **Traceable aggregation** — official outcomes remain decomposable to Scorecards, Rubric criteria, revisions, and policy.
- **Controlled identity disclosure** — Judges see Team Alias and Division rather than institutional identity.
- **Configurable competition policy** — Divisions, Rubrics, Awards, Panel composition, scoring, coverage, and tie behavior are not hard-coded MinneMUDAC constants.
- **Controlled finality** — authoritative state may be corrected through explicit Versioning and Provenance rather than silent overwrite.
- **Capture-channel parity** — paper and electronic judging share evaluation semantics.
- **Mobile-first judging** — the primary Judge workflow targets personal smartphones under live-event conditions.
- **Privacy by lifecycle** — ordinary Judge access to private Scorecards, Notes, and judging history ends when live judging ends while Organizer-governed records remain retained.
- **Operational resilience** — interruption, connectivity loss, device loss, and paper fallback are expected operating conditions.
- **Technology independence during specification** — AWS and GitHub Actions are boundary conditions; specific infrastructure remains deferred.

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

Judge and Organizer are Participation roles; Expertise is Participation state; Criteria belong to Rubrics; Notes belong to Scorecards; Panel Membership belongs to Panel state; Aggregation, Evaluation Coverage, and Rank are derived mechanisms.

## Design status

**Phase 001 — Concept Design Foundation is complete.** Its canonical exit baseline is [`docs/001-concept-design/001-H-phase-consolidation-initial-concept-catalog.md`](docs/001-concept-design/001-H-phase-consolidation-initial-concept-catalog.md).

**Phase 002 — Concept Specification, Policy & Synchronization Refinement is in progress.**

| Group | Topic | Status |
| --- | --- | --- |
| 002-A | [Competition, Division, Team & Alias Specifications](docs/002-concept-specification/002-A-competition-division-team-alias-specifications.md) | **Complete** |
| 002-B | [Identity, Participation & Access Specifications](docs/002-concept-specification/002-B-identity-participation-access-specifications.md) | **Complete** |
| 002-C | [Panel, Membership & Judging Encounter Specifications](docs/002-concept-specification/002-C-panel-membership-judging-encounter-specifications.md) | **Complete** |
| 002-D | Rubric, Criterion, Scorecard & Notes Specifications | **Next** |
| 002-E | Versioning, Provenance, Correction & Authority Preservation | Planned |
| 002-F | Aggregation, Coverage, Ranking & Evaluation Policy | Planned |
| 002-G | Awards, Reconciliation, Finalization & Official Outcomes | Planned |
| 002-H | Export, Print, Operational Continuity & External Representations | Planned |
| 002-I | Phase 002 Consolidation & Specification Exit Review | Planned |

See [`docs/README.md`](docs/README.md) for the canonical documentation index and [`docs/002-concept-specification/README.md`](docs/002-concept-specification/README.md) for the Phase 002 plan.

## Current specification baseline

Competition lifecycle:

```text
Draft → Ready → Active → Event Completed → Finalized
```

Human-security model:

```text
Identity       → who the person is
Participation  → why/capacity in this Competition
Access         → what the current context may do or see
```

Judging-topology model:

```text
Judge Participation
        ↓
      Panel
        │
        │ intended grouping
        ▼
Panel + Team
        ↓
Judging Encounter
        │
        ├── presented Alias / Division snapshot
        ├── starting participant snapshot
        ├── explicit participant adjustments
        └── effective evaluation obligations
```

Panel membership may change without rewriting historical judging. Expertise and assigned Panel composition capacity are distinct. Encounter initiation is duplicate-safe, same Panel + same Team normally produces one valid Encounter, and legitimate rejudging creates an explicit replacement. Recusal or absence changes evaluation obligations without creating zero scores, while an already-authoritative Scorecard cannot be silently removed through participant adjustment.

## Repository documentation convention

The repository—not chat history—is the durable design baseline. Completed design groupings are added to `/docs` as they are completed.

```text
docs/
  README.md
  001-concept-design/
    ... Phase 001 records ...
  002-concept-specification/
    README.md
    002-A-competition-division-team-alias-specifications.md
    002-B-identity-participation-access-specifications.md
    002-C-panel-membership-judging-encounter-specifications.md
```

## Architecture boundary condition

The intended end state is deployment into an **AWS ecosystem** through **GitHub Actions**. This is an accepted constraint, not yet an architecture decision. Hosting model, identity provider, API style, database, offline persistence, audit implementation, and AWS service choices will follow the behavioral specifications.

## Status

This repository remains in **design**, not production implementation. Phase 002 is converting the accepted concept catalog into explicit behavioral and synchronization contracts before conceptual UX and cloud architecture are finalized.

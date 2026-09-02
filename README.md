# MUDAC Competition Demo

MUDAC is a documentation-first design effort for a web application that supports live student data competitions, with MinneMUDAC as the initial reference context. The product is intended to replace or augment paper-heavy judging operations while preserving fairness, judge independence, accessibility, auditability, and operational resilience.

The design is being developed using Daniel Jackson's **Concept Design** methodology. The repository intentionally begins with product and conceptual design before UI component design or cloud architecture so that implementation choices are derived from stable behavioral concepts rather than from screens, database tables, or framework conventions.

## Product intent

Student Teams analyze a supplied dataset, perform statistical and/or machine-learning work, and present their findings and methodology to Panels of volunteer Judges. Judges typically bring different perspectives such as academic, business, and technical expertise. Each Judge independently completes a Rubric-based Scorecard for a Team during a Judging Encounter. Those Scorecards are aggregated across repeated Encounters to support Division-scoped ranking and competition Awards.

The application is intended to support three primary human roles:

- **Organizer** — configures and operates a Competition, establishes Divisions and Teams, defines Rubrics and Awards, coordinates Judges and Panels, monitors judging, reconciles paper and electronic Scorecards, reviews scoring, and finalizes results.
- **Judge** — participates in a specific Competition, joins a Panel, evaluates Teams independently, records criterion scores and Notes, and finalizes their own Scorecards.
- **Administrator** — operates the technical system without automatically inheriting competition decision authority.

Students are currently **participants and beneficiaries, not application actors**. A Team is represented to Judges through a competition-safe identity rather than institutional identity so the application does not unnecessarily reveal school/college affiliation during judging.

## Core design principles

The current design baseline emphasizes:

- **Independent judgment** — each Judge authors an individual Scorecard; Panel and Team scores are derived.
- **Traceable aggregation** — official results remain decomposable to the Scorecards, Rubric criteria, revisions, and policies that produced them.
- **Controlled identity disclosure** — Judges see a Team's competition identity and Division, not administrative institutional identity.
- **Configurable competition policy** — Divisions, Rubrics, Awards, Panel composition, scoring, coverage, and tie behavior should not be hard-coded as MinneMUDAC constants.
- **Controlled finality** — Rubrics, Scorecards, Awards, and competition outcomes may become authoritative without making legitimate correction impossible; revisions preserve prior state and provenance.
- **Capture-channel parity** — paper and electronic judging use the same evaluation semantics. Paper is a supported accessibility and continuity path, not a second-class exception.
- **Mobile-first judging** — the primary Judge workflow is intended for a personal smartphone under live-event conditions.
- **Privacy by lifecycle** — Judge access to private Scorecards, Notes, and judging history exists for operational need during the event and expires after live participation; the authoritative competition record remains available to authorized Organizers.
- **Operational resilience** — interruptions, network degradation, device loss, and temporary system failure must not silently destroy valid judging work.
- **Technology independence during concept design** — AWS and GitHub Actions are known deployment boundary conditions, but specific AWS services, frameworks, databases, and authentication mechanisms remain intentionally deferred.

## Conceptual model

Phase 001 accepts the following initial concept catalog.

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

Several important domain ideas are intentionally **not** standalone concepts. Judge and Organizer are Participation roles; Expertise is Judge Participation state; Criteria belong to Rubrics; Notes belong to Scorecards; Panel Membership belongs to Panel state; Aggregation, Evaluation Coverage, and Rank are derived mechanisms; PDF and QR are representations; dashboards and portals are UI projections.

## Design status

**Phase 001 — Concept Design Foundation is complete.** Its canonical exit baseline is [`docs/001-concept-design/001-H-phase-consolidation-initial-concept-catalog.md`](docs/001-concept-design/001-H-phase-consolidation-initial-concept-catalog.md).

**Phase 002 — Concept Specification, Policy & Synchronization Refinement is in progress.** It is divided into nine groups so structural concepts, access, judging, evaluation, history, numerical policy, official outcomes, and continuity can be specified without collapsing their boundaries.

| Group | Topic | Status |
| --- | --- | --- |
| 002-A | [Competition, Division, Team & Alias Specifications](docs/002-concept-specification/002-A-competition-division-team-alias-specifications.md) | **Complete** |
| 002-B | [Identity, Participation & Access Specifications](docs/002-concept-specification/002-B-identity-participation-access-specifications.md) | **Complete** |
| 002-C | Panel, Membership & Judging Encounter Specifications | **Next** |
| 002-D | Rubric, Criterion, Scorecard & Notes Specifications | Planned |
| 002-E | Versioning, Provenance, Correction & Authority Preservation | Planned |
| 002-F | Aggregation, Coverage, Ranking & Evaluation Policy | Planned |
| 002-G | Awards, Reconciliation, Finalization & Official Outcomes | Planned |
| 002-H | Export, Print, Operational Continuity & External Representations | Planned |
| 002-I | Phase 002 Consolidation & Specification Exit Review | Planned |

See [`docs/README.md`](docs/README.md) for the canonical documentation index and [`docs/002-concept-specification/README.md`](docs/002-concept-specification/README.md) for the Phase 002 specification plan.

## Current structural and access specification

002-A standardizes the Competition lifecycle as:

```text
Draft → Ready → Active → Event Completed → Finalized
```

A Team may be temporarily incomplete while the Competition is Draft, but before Ready every non-withdrawn Team must have exactly one active Division and one unique active Alias. Division changes are corrections, Team identity remains stable across Division/Alias corrections, aliases already used operationally are not recycled to other Teams, and later Judging Encounters should retain the Alias representation used when the judging occurred.

002-B standardizes the human-security model as:

```text
Identity       → who the person is
Participation  → why/capacity in this Competition
Access         → what the current context may do or see
```

Judge and Organizer are Competition-scoped Participation roles. A returning Judge can reuse a reverified Identity but receives a new Participation for each Competition. Access is capability-oriented and sensitive to Competition lifecycle, resource ownership, scope, purpose, and time. Event Completed expires ordinary Judge access to Scorecards, Notes, and judging history without deleting those records; legitimate later corrections use narrow temporary access. Administrator technical authority does not automatically confer Competition decision authority.

## Repository documentation convention

Design work evolves phase by phase. The repository documentation is updated as each grouping is completed so that the repository—not chat history—remains the durable design baseline.

```text
docs/
  README.md
  001-concept-design/
    ... Phase 001 records ...
  002-concept-specification/
    README.md
    002-A-competition-division-team-alias-specifications.md
    002-B-identity-participation-access-specifications.md
```

## Architecture boundary condition

The intended end state is deployment into an **AWS ecosystem** through **GitHub Actions**. This is an accepted constraint, not yet an architecture decision. Specific choices such as hosting model, identity provider, API style, database, local/offline persistence, audit implementation, and AWS services will be selected after the conceptual and behavioral specifications are sufficiently stable.

## Status

This repository remains in **design**, not production implementation. Phase 001 established the conceptual baseline; Phase 002 is turning that baseline into explicit concept, policy, and synchronization specifications before conceptual UX and cloud architecture are finalized.

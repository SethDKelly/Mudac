# MUDAC Competition Demo

MUDAC is a documentation-first design effort for a web application that supports live student data competitions, with MinneMUDAC as the initial reference context. The product is intended to replace or augment paper-heavy judging operations while preserving fairness, judge independence, accessibility, auditability, and operational resilience.

The design is being developed using Daniel Jackson's **Concept Design** methodology. The repository intentionally begins with product and conceptual design before UI component design or cloud architecture so implementation choices are derived from stable behavioral concepts rather than screens, database tables, or framework conventions.

## Product intent

Student Teams analyze a supplied dataset and present findings and methodology to Panels of volunteer Judges. Each Judge independently completes a Rubric-based Scorecard for a Team during a Judging Encounter. Eligible authoritative Scorecards are combined under explicit Evaluation Policy to support Coverage assessment, Division-scoped ranking, and competition Awards.

Primary human roles are Organizer, Judge, and technical Administrator. Judge and Organizer are Competition-scoped Participation roles rather than permanent Identity types. Students are currently competition participants and beneficiaries, not application actors.

## Core design principles

- **Independent judgment** — each Judge authors an individual Scorecard; Panel and Team results are derived.
- **Traceable aggregation** — official outcomes remain decomposable to eligible Scorecards, Rubric Criteria, Versions, Provenance, and policy.
- **Controlled identity disclosure** — Judges see Team Alias and Division rather than institutional identity.
- **Configurable competition policy** — Divisions, Rubrics, Awards, Panel composition, scoring, Coverage, precision, and tie behavior are not hard-coded constants.
- **Controlled finality** — authoritative state may be corrected through explicit Versioning and Provenance rather than silent overwrite.
- **Authority preservation** — correction rights follow the meaning of the fact; Organizer or technical authority does not silently replace Judge evaluation authorship.
- **Capture-channel parity** — paper and electronic judging share evaluation semantics while Provenance preserves capture differences.
- **Coverage before outcome confidence** — numerical Aggregate and sufficiency of judging remain separate.
- **Explainable ranking** — Ranking is derived from eligible evidence under an identifiable Evaluation Policy, never directly edited.
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

Aggregation, Evaluation Coverage, Rank, Criterion, Note, Expertise, and Panel Membership remain subordinate or derived mechanisms rather than standalone concepts.

## Design status

**Phase 001 — Concept Design Foundation is complete.** Its canonical exit baseline is [`docs/001-concept-design/001-H-phase-consolidation-initial-concept-catalog.md`](docs/001-concept-design/001-H-phase-consolidation-initial-concept-catalog.md).

**Phase 002 — Concept Specification, Policy & Synchronization Refinement is in progress.**

| Group | Topic | Status |
| --- | --- | --- |
| 002-A | [Competition, Division, Team & Alias Specifications](docs/002-concept-specification/002-A-competition-division-team-alias-specifications.md) | **Complete** |
| 002-B | [Identity, Participation & Access Specifications](docs/002-concept-specification/002-B-identity-participation-access-specifications.md) | **Complete** |
| 002-C | [Panel, Membership & Judging Encounter Specifications](docs/002-concept-specification/002-C-panel-membership-judging-encounter-specifications.md) | **Complete** |
| 002-D | [Rubric, Criterion, Scorecard & Notes Specifications](docs/002-concept-specification/002-D-rubric-criterion-scorecard-notes-specifications.md) | **Complete** |
| 002-E | [Versioning, Provenance, Correction & Authority Preservation](docs/002-concept-specification/002-E-versioning-provenance-correction-authority-preservation.md) | **Complete** |
| 002-F | [Aggregation, Coverage, Ranking & Evaluation Policy](docs/002-concept-specification/002-F-aggregation-coverage-ranking-evaluation-policy.md) | **Complete** |
| 002-G | Awards, Reconciliation, Finalization & Official Outcomes | **Next** |
| 002-H | Export, Print, Operational Continuity & External Representations | Planned |
| 002-I | Phase 002 Consolidation & Specification Exit Review | Planned |

See [`docs/README.md`](docs/README.md) for the canonical documentation index and [`docs/002-concept-specification/README.md`](docs/002-concept-specification/README.md) for the Phase 002 plan.

## Current specification baseline

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
Rank eligibility
        ↓
Division Ranking
```

The default aggregation policy gives each eligible authoritative individual Judge Scorecard equal weight. Encounter means are analytical only. Missing judgments are never zero, Coverage exceptions never fabricate scores, outliers are not automatically discarded, Judges are not silently normalized, and incompatible Rubric Versions are not pooled or implicitly rescaled. Rank is Division-scoped and derived under explicit precision/tie rules. Evaluation Policy is itself authoritative/reconstructible once judging begins because changing the rules can change outcomes without changing Judge evidence.

## Repository documentation convention

The repository—not chat history—is the durable design baseline. Completed design groupings are added to `/docs` as they are completed.

## Architecture boundary condition

The intended end state is deployment into an **AWS ecosystem** through **GitHub Actions**. This is an accepted constraint, not yet an architecture decision. Hosting model, identity provider, API style, database, offline persistence, audit implementation, and AWS service choices will follow the behavioral specifications.

## Status

This repository remains in **design**, not production implementation. Phase 002 is converting the accepted concept catalog into explicit behavioral, policy, and synchronization contracts before conceptual UX and cloud architecture are finalized.

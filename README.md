# MUDAC Competition Demo

MUDAC is a documentation-first design effort for a web application that supports live student data competitions, with MinneMUDAC as the initial reference context. The product is intended to replace or augment paper-heavy judging operations while preserving fairness, judge independence, accessibility, auditability, and operational resilience.

The design is being developed using Daniel Jackson's **Concept Design** methodology. The repository intentionally begins with product and conceptual design before UI component design or cloud architecture so implementation choices are derived from stable behavioral concepts rather than screens, database tables, or framework conventions.

## Product intent

Student Teams analyze a supplied dataset and present findings and methodology to Panels of volunteer Judges. Each Judge independently completes a Rubric-based Scorecard for a Team during a Judging Encounter. Eligible authoritative Scorecards are combined under explicit Evaluation Policy to support Coverage assessment, Division-scoped ranking, competition Awards, and an explicit official closeout process.

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
- **Explicit official closeout** — Finalization is a reconciled Organizer decision producing a reconstructible Official Outcome Revision, not merely an event-end flag.
- **Official is not automatically public** — result publication/disclosure is separate from internal Finalization.
- **Traceable external representation** — printed/downloaded/published material remains tied to identified source state and audience disclosure rules rather than becoming an independent truth.
- **Paper continuity** — paper judging is a first-class continuity/accessibility path and converges onto the same Scorecard semantics and evaluation policy as electronic judging.
- **Mobile-first judging** — the primary Judge workflow targets personal smartphones under live-event conditions.
- **Privacy by lifecycle** — ordinary Judge access to private Scorecards, Notes, and judging history ends when live judging ends while Organizer-governed records remain retained.
- **Operational resilience** — interruption, connectivity loss, device loss, mixed-mode judging, and paper fallback are expected operating conditions.
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

Aggregation, Evaluation Coverage, Rank, Criterion, Note, Expertise, Panel Membership, Reconciliation, and Official Outcome remain subordinate/derived/process mechanisms rather than standalone concepts.

## Design status

**Phase 001 — Concept Design Foundation is complete.** Its canonical exit baseline is [`docs/001-concept-design/001-H-phase-consolidation-initial-concept-catalog.md`](docs/001-concept-design/001-H-phase-consolidation-initial-concept-catalog.md).

**Phase 002 — Concept Specification, Policy & Synchronization Refinement is in progress.** Eight of nine subgroupings are complete.

| Group | Topic | Status |
| --- | --- | --- |
| 002-A | [Competition, Division, Team & Alias Specifications](docs/002-concept-specification/002-A-competition-division-team-alias-specifications.md) | **Complete** |
| 002-B | [Identity, Participation & Access Specifications](docs/002-concept-specification/002-B-identity-participation-access-specifications.md) | **Complete** |
| 002-C | [Panel, Membership & Judging Encounter Specifications](docs/002-concept-specification/002-C-panel-membership-judging-encounter-specifications.md) | **Complete** |
| 002-D | [Rubric, Criterion, Scorecard & Notes Specifications](docs/002-concept-specification/002-D-rubric-criterion-scorecard-notes-specifications.md) | **Complete** |
| 002-E | [Versioning, Provenance, Correction & Authority Preservation](docs/002-concept-specification/002-E-versioning-provenance-correction-authority-preservation.md) | **Complete** |
| 002-F | [Aggregation, Coverage, Ranking & Evaluation Policy](docs/002-concept-specification/002-F-aggregation-coverage-ranking-evaluation-policy.md) | **Complete** |
| 002-G | [Awards, Reconciliation, Finalization & Official Outcomes](docs/002-concept-specification/002-G-awards-reconciliation-finalization-official-outcomes.md) | **Complete** |
| 002-H | [Export, Print, Operational Continuity & External Representations](docs/002-concept-specification/002-H-export-print-operational-continuity-external-representations.md) | **Complete** |
| 002-I | Phase 002 Consolidation & Specification Exit Review | **Next** |

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

The default aggregation policy gives each eligible authoritative Judge Scorecard equal weight. Encounter means are analytical only. Missing judgments are never zero, Coverage exceptions never fabricate scores, outliers are not automatically discarded, Judges are not silently normalized, and incompatible Rubric Versions are not pooled or implicitly rescaled. Rank is Division-scoped and derived under explicit precision/tie rules. Evaluation Policy is authoritative/reconstructible once judging begins because changing rules can change outcomes without changing Judge evidence.

After Event Completed, Organizers reconcile evidence, Coverage, policy, ties, and Awards. A computable Rank is not automatically ranking-ready. Finalization requires all mandatory closeout gates and creates a reconstructible Official Outcome Revision. Post-finalization corrections preserve prior official revisions and require explicit successor confirmation rather than silently migrating Rank or Awards. Finalization remains separate from later publication.

Export produces stable audience-specific representations of identified source state. Previously distributed forms/results do not silently change meaning when the source changes; newer source state produces a newer representation. Printable Rubrics and paper Scorecards are traceable to their Rubric Version, paper evaluations acquire unique source references and are checked against the physical source before eligibility, and QR/barcode mechanisms remain identification/navigation aids rather than authority.

Operational degradation may move judging from electronic to mixed or paper fallback and later recovery, but every path converges on the same logical Scorecard, Provenance, Coverage, Aggregation, and Ranking model. Recovery must be duplicate-safe, stale-state-safe, privacy-aware, and truthful about what has actually been saved or finalized.

## Repository documentation convention

The repository—not chat history—is the durable design baseline. Completed design groupings are added to `/docs` as they are completed.

## Architecture boundary condition

The intended end state is deployment into an **AWS ecosystem** through **GitHub Actions**. This is an accepted constraint, not yet an architecture decision. Hosting model, identity provider, API style, database, offline persistence, artifact generation/storage, audit implementation, and AWS service choices will follow the behavioral specifications.

## Status

This repository remains in **design**, not production implementation. Phase 002 now has only its consolidation/exit review remaining before the project advances into the next design layer.

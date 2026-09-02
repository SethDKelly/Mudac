# Phase 002 — Concept Specification, Policy & Synchronization Refinement

Status: **Complete**

## Purpose

Phase 002 converts the Phase 001 concept catalog into explicit behavioral, policy, synchronization, authority, closeout, and continuity specifications while remaining implementation-neutral.

The canonical Phase 002 exit baseline is **[002-I — Phase 002 Consolidation & Specification Exit Review](002-I-phase-consolidation-specification-exit-review.md)**.

## Phase plan

| Group | Topic | Status |
| --- | --- | --- |
| 002-A | [Competition, Division, Team & Alias Specifications](002-A-competition-division-team-alias-specifications.md) | **Complete** |
| 002-B | [Identity, Participation & Access Specifications](002-B-identity-participation-access-specifications.md) | **Complete** |
| 002-C | [Panel, Membership & Judging Encounter Specifications](002-C-panel-membership-judging-encounter-specifications.md) | **Complete** |
| 002-D | [Rubric, Criterion, Scorecard & Notes Specifications](002-D-rubric-criterion-scorecard-notes-specifications.md) | **Complete** |
| 002-E | [Versioning, Provenance, Correction & Authority Preservation](002-E-versioning-provenance-correction-authority-preservation.md) | **Complete** |
| 002-F | [Aggregation, Coverage, Ranking & Evaluation Policy](002-F-aggregation-coverage-ranking-evaluation-policy.md) | **Complete** |
| 002-G | [Awards, Reconciliation, Finalization & Official Outcomes](002-G-awards-reconciliation-finalization-official-outcomes.md) | **Complete** |
| 002-H | [Export, Print, Operational Continuity & External Representations](002-H-export-print-operational-continuity-external-representations.md) | **Complete** |
| 002-I | [Phase 002 Consolidation & Specification Exit Review](002-I-phase-consolidation-specification-exit-review.md) | **Complete** |

## Post-exit compatible refinement

[002-A1 — Team Extensible Attributes & Team Name Refinement](002-A1-team-extensible-attributes-team-name-refinement.md) extends the Team specification without changing the Phase 002 concept catalog or exit result.

Team now explicitly supports extensible descriptive attributes under Competition-defined metadata rules. `teamName` is the initial standard optional attribute. Team Name is distinct from Alias, need not be unique, and has no scoring, Coverage, Ranking, or Award effect by default. Attribute definitions carry explicit disclosure and competitive-significance posture so generic metadata cannot become a hidden rules engine. Because a student-created Team name could reveal school or identity clues, it is Organizer-visible but not Judge-visible by default while blinded judging is active; public/ceremony use is an explicit disclosure decision.

This refinement is compatible with 002-I because it adds subordinate Team state rather than a new Concept or synchronization dependency.

## Exit result

All 15 accepted Concepts now have sufficient behavioral specification for the next design layer:

### Core

- Competition
- Division
- Team
- Panel
- Judging Encounter
- Rubric
- Scorecard
- Award

### Supporting

- Identity
- Participation
- Alias
- Access
- Versioning
- Provenance
- Export

No additional Concept is required for the current product boundary.

Important non-concept mechanisms remain explicit rather than being promoted into domain objects:

- Evaluation Policy;
- Aggregation;
- Coverage;
- Rank;
- Reconciliation;
- Official Outcome Revision;
- paper verification;
- publication/disclosure;
- operational fallback/recovery;
- Team Attribute Definitions / descriptive metadata policy.

## Canonical behavioral chain

```text
Competition structure
        ↓
Identity / Participation / Access
        ↓
Panel + Team
        ↓
Judging Encounter
        ↓
Rubric Version + Judge obligation
        ↓
Scorecard
        ↓
Versioning + Provenance
        ↓
eligible authoritative evidence
        ↓
Coverage + Aggregate
        ↓
Division Ranking
        ↓
Reconciliation
        ↓
Awards
        ↓
Finalization
        ↓
Official Outcome Revision
        ↓
Export / external representation
```

## Major exit principles

- Competition lifecycle is `Draft → Ready → Active → Event Completed → Finalized`.
- Current operational state and historical observed state remain separately representable.
- Identity, Participation, Access, and semantic authority remain distinct.
- Panel current membership and actual historical Encounter participation remain distinct.
- One Judge Participation × one Encounter yields at most one logical Scorecard.
- Scorecards use one exact authoritative Rubric Version.
- Drafts are non-authoritative; committed Versions are immutable historical snapshots.
- Judge amendments, paper transcription corrections, structural corrections, supersession, and invalidation remain semantically distinct.
- Coverage and Aggregate remain independent.
- The default Aggregate gives equal weight to eligible authoritative individual Judge Scorecards.
- Missing evaluations are never zero; Coverage exceptions never fabricate evidence.
- Judges are not silently normalized and outliers are not automatically excluded.
- Incompatible Rubric Versions are not silently pooled or rescaled.
- Rank is Division-scoped and derived rather than manually edited.
- Evaluation Policy is reconstructible once judging begins.
- Award is distinct from Rank.
- Finalization is a reconciled Organizer action producing an Official Outcome Revision.
- Post-finalization correction preserves earlier official revisions.
- Finalization is separate from public publication.
- Export represents identified source state and does not become source truth.
- Paper and electronic capture share evaluation semantics.
- Operational degradation may change capture channel but never evaluation meaning or weight.
- Team descriptive attributes are extensible but do not acquire competitive effect or disclosure merely by existing.

## Deliberate extension points

Phase 002 intentionally leaves future expansion points for:

- formal Stage/Round advancement;
- student access/feedback;
- complex scheduling;
- notifications;
- advanced Judge calibration/normalization policy;
- advanced Award committee/nomination workflows;
- public result experience.

These are not blockers for the current product boundary.

## Next phase

The project now proceeds to **[Phase 003 — Conceptual UX Architecture, Information Architecture & Interaction Model](../003-conceptual-ux-architecture/README.md)**.

Phase 003 maps the authoritative behavioral model into actor-centered experiences without selecting React components, route structures, persistence technology, or AWS topology.

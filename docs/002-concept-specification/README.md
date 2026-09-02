# Phase 002 — Concept Specification, Policy & Synchronization Refinement

Status: **In Progress**

## Purpose

Phase 001 established MUDAC's initial 15-concept catalog and the principal invariants that shape competition judging. Phase 002 turns that conceptual baseline into explicit behavioral specifications.

The phase remains implementation-neutral. It defines concept state, actions, queries, operational principles, invariants, failure/exception behavior, policy boundaries, and synchronization contracts before UI architecture, persistence design, authentication technology, or AWS service selection.

## Why nine subgroupings

Nine groups provide enough separation to keep concept families singular while allowing tightly related behaviors to be specified together. The order follows the dependency of the problem domain rather than an implementation stack:

1. establish Competition structure and Team-facing identity;
2. establish human identity, participation, and access;
3. establish evaluator grouping and actual judging occurrences;
4. define evaluation instruments and individual judgments;
5. define authoritative history and provenance;
6. define derived numerical semantics and eligibility;
7. define recognition and official closeout;
8. define printable/external representations and operational continuity;
9. consolidate and test the whole specification.

## Phase plan

| Group | Topic | Status |
| --- | --- | --- |
| 002-A | [Competition, Division, Team & Alias Specifications](002-A-competition-division-team-alias-specifications.md) | **Complete** |
| 002-B | [Identity, Participation & Access Specifications](002-B-identity-participation-access-specifications.md) | **Complete** |
| 002-C | [Panel, Membership & Judging Encounter Specifications](002-C-panel-membership-judging-encounter-specifications.md) | **Complete** |
| 002-D | [Rubric, Criterion, Scorecard & Notes Specifications](002-D-rubric-criterion-scorecard-notes-specifications.md) | **Complete** |
| 002-E | [Versioning, Provenance, Correction & Authority Preservation](002-E-versioning-provenance-correction-authority-preservation.md) | **Complete** |
| 002-F | [Aggregation, Coverage, Ranking & Evaluation Policy](002-F-aggregation-coverage-ranking-evaluation-policy.md) | **Complete** |
| 002-G | Awards, Reconciliation, Finalization & Official Outcomes | **Next** |
| 002-H | Export, Print, Operational Continuity & External Representations | Planned |
| 002-I | Phase 002 Consolidation & Specification Exit Review | Planned |

## Specification template

Where applicable, each accepted concept is specified using:

- Purpose
- State
- Actions
- Queries
- Operational Principle
- Invariants
- Failure and exceptional behavior
- Synchronization boundaries
- Policy/configuration boundaries
- Explicit non-responsibilities

Subordinate state and derived mechanisms are specified only as required to make concept behavior unambiguous; they are not promoted into concepts without new behavioral evidence.

## 002-A structural baseline

Competition lifecycle is:

```text
Draft → Ready → Active → Event Completed → Finalized
```

`Historical` is a retained presentation/status rather than another business lifecycle state, and reconciliation is activity between Event Completed and Finalized. Team setup may be temporarily incomplete only during Draft. Before Ready, every non-withdrawn Team has exactly one active Division and one unique active Alias. Division changes are corrections, operationally used Alias values are never recycled, and Encounters snapshot the Alias/Division presented during judging.

## 002-B human-security baseline

```text
Identity       → who this person is
Participation  → why/capacity in this Competition
Access         → what this context may do or see now
```

Judge and Organizer are Competition-scoped Participation roles. Returning Judges may reuse/reverify Identity but receive new Competition Participation. Expertise is Participation state and does not grant authority. Access is capability-oriented and sensitive to lifecycle, ownership, resource sensitivity, scope, purpose, and time. Event Completed ends ordinary Judge access to private Scorecards, Notes, and judging history without deleting the records. Later Judge correction uses narrow temporary Access after re-verification. Administrator technical authority does not automatically confer Competition decision authority.

## 002-C judging-topology baseline

```text
Panel              → who is intended to judge together
Judging Encounter  → who actually evaluated this Team on this occurrence
```

Panel Membership is subordinate Panel state. Expertise and assigned Panel composition capacity are distinct. Encounter lifecycle is `Prepared → Open → Complete`, with Cancelled and Invalidated exceptional paths. When an Encounter opens it snapshots Team Alias, Division, Panel context, and starting Judge participants; later absence, recusal, or replacement is an explicit participant adjustment. Effective Encounter participants drive Scorecard obligations. Same Panel + same Team normally yields one valid Encounter, and legitimate rejudging creates an explicit replacement.

## 002-D evaluation-instrument baseline

```text
Rubric     → defines valid individual judgment
Scorecard  → records one Judge's judgment
```

Every authoritative Scorecard references one exact authoritative Rubric Version. Scored Criteria are required in the initial baseline; missing, zero, and N/A remain distinct. A Rubric uses one coherent scoring model and cannot hide double weighting. Scorecard lifecycle supports Draft, Finalized, and Amendment Draft while the prior finalized Version remains authoritative until a successor is committed. Notes are versioned private evaluation evidence. Paper/electronic capture share the same Scorecard semantics. Intra-Scorecard calculation is deterministic; cross-Judge aggregation is separate.

## 002-E authoritative-history baseline

```text
Versioning  → what authoritative states existed
Provenance  → how, why, and through whose authority they arose
```

Committed Versions are immutable reconstructible snapshots. Draft edits are not Versions. Correction authority follows semantic authority: Judges amend judgment, Organizers correct administration and verified capture, and technical Administrators do not inherit Competition or Judge semantic authority. Supersession and invalidation are distinct. Event Completed and Finalized progressively increase correction governance. Source changes cause dependent derived values to refresh or become explicitly affected; official post-finalization outcomes never silently migrate.

## 002-F derived-evaluation baseline

002-F formalizes the chain:

```text
Authoritative Scorecards
        ↓
Evidence Eligibility
        ↓
┌──────────────┬──────────────┐
│              │              │
▼              ▼              │
Coverage    Aggregate          │
│              │              │
└───────┬──────┘              │
        ▼                     │
 Rank Eligibility             │
        ↓                     │
 Division Ranking             │
```

Coverage and Aggregate remain independent. A Team may have a valid numerical Aggregate while still lacking enough qualifying judging to be rank-eligible. Coverage may consider minimum valid Encounters, minimum eligible Scorecards, and composition exceptions; accepted exceptions preserve the actual shortfall rather than fabricating scores.

The canonical initial aggregation basis gives every eligible authoritative Judge Scorecard equal weight. Encounter means are analytical projections and are not averaged again. Missing evaluations are never zero. There is no hidden Judge normalization or automatic outlier removal; unusual scores may be flagged for review but remain eligible unless a real error is established through correction/invalidation.

Scorecards may be pooled only when their Rubric Versions are aggregation-compatible. Scoring-semantic Rubric changes are incompatible by default and no implicit rescaling occurs. Ranking is Division-scoped, derived rather than editable, and uses explicit comparison precision distinct from display rounding. Ties are never broken by incidental implementation data; with no declared resolver, a true tie remains shared.

Evaluation Policy is authoritative Competition configuration and becomes another Versioning/Provenance consumer once judging begins. Changing aggregation, Coverage, compatibility, precision, or tie semantics after evidence exists is an outcome-affecting policy change that must remain reconstructible and trigger derived-result reconciliation.

The current baseline assumes one Competition-level judging/ranking scope per Division. A future formal advancement/finalist workflow may justify adding a Stage/Round scope without changing individual Scorecard semantics.

## Phase exit target

Phase 002 should end with:

- explicit behavioral contracts for all accepted concepts;
- explicit synchronization contracts across concepts;
- a defined evaluation/coverage/ranking policy model;
- clear correction and authority-preservation semantics;
- defined Competition finalization gates;
- print/paper continuity specifications;
- unresolved implementation choices isolated from behavioral requirements;
- enough stability to begin conceptual UX architecture and later AWS/system architecture without redefining core domain behavior.

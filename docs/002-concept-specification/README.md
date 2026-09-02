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
| 002-G | [Awards, Reconciliation, Finalization & Official Outcomes](002-G-awards-reconciliation-finalization-official-outcomes.md) | **Complete** |
| 002-H | [Export, Print, Operational Continuity & External Representations](002-H-export-print-operational-continuity-external-representations.md) | **Complete** |
| 002-I | Phase 002 Consolidation & Specification Exit Review | **Next** |

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

002-F formalizes:

```text
Authoritative Scorecards
        ↓
Evidence Eligibility
        ↓
Coverage + Aggregate
        ↓
Rank Eligibility
        ↓
Division Ranking
```

Coverage and Aggregate remain independent. A Team may have a valid Aggregate while lacking sufficient qualifying judging. The canonical initial aggregation basis gives every eligible authoritative Judge Scorecard equal weight; Encounter means remain analytical only. Missing evaluation is never zero, Coverage exceptions never fabricate scores, Judge normalization is absent, and statistical outliers are not automatically excluded.

Scorecards are pooled only across aggregation-compatible Rubric Versions; scoring-semantic revisions are incompatible by default and are not implicitly rescaled. Ranking is Division-scoped and derived, comparison precision is explicit and distinct from display rounding, and ties are never broken by incidental implementation data. Evaluation Policy itself becomes authoritative/reconstructible once judging begins because rule changes can alter outcomes without changing Judge evidence.

## 002-G official-outcome baseline

002-G formalizes:

```text
Event Completed
      ↓
Organizer Reconciliation
      ↓
Ranking Ready
      ↓
Award Decisions
      ↓
Finalization Ready
      ↓
Competition Finalized
      ↓
Official Outcome Revision
```

Reconciliation remains Organizer activity rather than a new lifecycle state or Concept. A computable Ranking is not automatically ranking ready: unresolved paper capture, Coverage, invalidation/replacement, Rubric compatibility, material corrections, Division assignment, tie resolution, and Award decisions may block official closeout.

Award remains distinct from Rank and supports rank-derived and discretionary selection. Rank-derived candidates follow authoritative Ranking and are Organizer-confirmed by default without permitting arbitrary deviation from the declared rule. Award scope, recipient cardinality, required/optional status, conferral, correction, and revocation remain explicit.

Finalization is a high-consequence Organizer action gated by reconciled authoritative evidence, ranking-ready Divisions, resolved required Awards, authoritative Evaluation Policy, and no unresolved outcome-affecting issue. Finalization creates an Official Outcome Revision: a reconstructible authoritative snapshot/projection of policy basis, resolved Coverage/exceptions, Division Rankings, Award conferrals, and sufficient source-version references.

Post-finalization correction preserves prior Official Outcome Revisions and requires explicit successor confirmation. Competition may remain lifecycle-Finalized while an exceptional outcome correction is pending. Official status is separate from publication: Finalization does not automatically disclose results publicly or restore Judge access.

## 002-H external-representation and continuity baseline

002-H specifies Export and closes the paper/operational-continuity loop:

```text
authoritative or explicitly identified source state
        ↓
      Export
        ↓
stable audience-safe external representation
```

Export remains distinct from Versioning and does not become the source of truth. Consequential representations remain traceable to the source authority/version they represented. A later source change generates a new representation rather than silently changing the historical meaning of previously distributed material. Disclosure profiles enforce least disclosure even when the Organizer generating the material has broader Access.

Printable Rubrics identify their exact Rubric Version. Paper Scorecards share identical evaluation semantics with electronic Scorecards and every physical evaluation accepted for official capture acquires a unique paper-source reference. Organizer transcription preserves Judge authorship and capture provenance. Paper data must be checked against its physical source before it becomes officially eligible evidence; second-person verification is optional unless Competition policy requires it.

QR/barcode mechanisms may accelerate navigation or source identification but do not grant authority. Sensitive identity information should not be embedded unnecessarily in visible or machine-readable representations.

Operational continuity follows a controlled progression from normal electronic operation through degraded/mixed operation and paper fallback to recovery/reconciliation. Connectivity state must be communicated truthfully, retries must be duplicate-safe, stale/offline Drafts cannot silently replace newer authoritative state, shared devices must clear prior Judge context, and recovery cannot create multiple official Scorecards for one Judge × Encounter obligation. Capture channel changes the operational path, never scoring semantics or evaluation weight.

Official/public representations reference one exact Official Outcome Revision. Finalization and publication remain separate, private Judge evidence is excluded from public publication by default, and corrected official outcomes generate new external representations while older distributed material remains historically identifiable as superseded.

## Phase exit target

Phase 002 should end with:

- explicit behavioral contracts for all 15 accepted concepts;
- explicit synchronization contracts across concepts;
- a defined evaluation/coverage/ranking policy model;
- clear correction and authority-preservation semantics;
- defined Competition finalization gates and official-outcome history;
- print/paper continuity and external-representation specifications;
- unresolved implementation choices isolated from behavioral requirements;
- enough stability to begin conceptual UX/application architecture and later AWS/system architecture without redefining core domain behavior.

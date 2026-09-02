# Phase 002 — Concept Specification, Policy & Synchronization Refinement

Status: **In Progress**

## Purpose

Phase 001 established MUDAC's initial 15-concept catalog and the principal invariants that shape competition judging. Phase 002 turns that conceptual baseline into explicit behavioral specifications.

The phase remains implementation-neutral. It should define concept state, actions, queries, operational principles, invariants, failure/exception behavior, policy boundaries, and synchronization contracts before UI architecture, persistence design, authentication technology, or AWS service selection.

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

Splitting further would create artificial micro-phases around subordinate state such as Criteria, Notes, or Panel Membership. Combining further would mix concept specification with derived scoring policy or operational continuity and make boundary testing harder.

## Phase plan

| Group | Topic | Status |
| --- | --- | --- |
| 002-A | [Competition, Division, Team & Alias Specifications](002-A-competition-division-team-alias-specifications.md) | **Complete** |
| 002-B | [Identity, Participation & Access Specifications](002-B-identity-participation-access-specifications.md) | **Complete** |
| 002-C | [Panel, Membership & Judging Encounter Specifications](002-C-panel-membership-judging-encounter-specifications.md) | **Complete** |
| 002-D | [Rubric, Criterion, Scorecard & Notes Specifications](002-D-rubric-criterion-scorecard-notes-specifications.md) | **Complete** |
| 002-E | [Versioning, Provenance, Correction & Authority Preservation](002-E-versioning-provenance-correction-authority-preservation.md) | **Complete** |
| 002-F | Aggregation, Coverage, Ranking & Evaluation Policy | **Next** |
| 002-G | Awards, Reconciliation, Finalization & Official Outcomes | Planned |
| 002-H | Export, Print, Operational Continuity & External Representations | Planned |
| 002-I | Phase 002 Consolidation & Specification Exit Review | Planned |

## Specification template

Where applicable, each accepted concept should be specified using:

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

Subordinate state and derived mechanisms should be specified only to the degree required to make concept behavior unambiguous; they should not be promoted into concepts without new behavioral evidence.

## 002-A structural baseline

002-A standardizes the Competition lifecycle as:

```text
Draft → Ready → Active → Event Completed → Finalized
```

`Historical` is a retained presentation/status rather than another business lifecycle state, and reconciliation is the Organizer activity between Event Completed and Finalized rather than a required lifecycle state.

Team setup may be temporarily incomplete only while a Competition is Draft. Before Ready, every non-withdrawn Team must have exactly one active Division assignment and one unique active Alias. Division changes are corrections, Alias values used operationally are never recycled to another Team in the same Competition, and later Encounters snapshot the Alias presented at judging time.

## 002-B human-security baseline

002-B formalizes three independent concerns:

```text
Identity       → who this person is
Participation  → why/capacity in this Competition
Access         → what this context may do or see now
```

Judge and Organizer are Competition-scoped Participation roles rather than permanent Identity types. Administrator remains primarily system-scoped authority. Returning Judges may reuse/reverify Identity but always receive a new Competition Participation. Expertise is Participation state and never independently grants authority.

Access is capability-oriented and may depend on role, Competition lifecycle, resource ownership, sensitivity, scope, purpose, and time. Event Completed ends ordinary Judge access to private Scorecards, Notes, and judging history without deleting the historical records. Legitimate post-event correction uses narrow temporary Access after Judge re-verification rather than restoring broad historical Judge access.

Dual-role identities are supported conceptually through separate Participation/Access contexts. Shared or loaner devices must clear the prior Judge's context, lost-device recovery revokes the compromised session rather than creating duplicate Participation, and system Administrator authority does not automatically imply Competition decision authority.

## 002-C judging-topology baseline

002-C formalizes the distinction:

```text
Panel              → who is intended to judge together
Judging Encounter  → who actually evaluated this Team on this occurrence
```

Panel Membership remains subordinate Panel state and retains historical start/end periods so Judges can be reassigned without rewriting prior judging. Expertise and assigned Panel composition capacity are distinct; by default one Judge satisfies at most one required capacity on a Panel. Panel-size and perspective requirements are configurable Competition policy rather than hard-coded Academic/Business/Technical roles.

Encounter lifecycle is:

```text
Prepared → Open → Complete
```

with `Cancelled` for a prepared occurrence that never meaningfully began and `Invalidated` for an occurrence that happened but must not contribute officially. Legitimate rejudging creates an explicit replacement Encounter rather than overwriting or duplicating the original.

When an Encounter opens it snapshots the Team Alias, Division, Panel context, and starting Judge participants. Later absence, recusal, or replacement is recorded as an explicit participant adjustment; the effective participant set drives Scorecard obligations. Recusal is never a zero or an unexplained missing Scorecard. A Judge who already created an authoritative Scorecard cannot have that evaluation silently removed through participant adjustment.

The same Panel-Team pair normally produces at most one valid Encounter per Competition, and duplicate/retried initiation must converge on one logical Encounter. Presentation completion is distinct from Encounter completion: an Encounter remains Open until all effective evaluation obligations are satisfied or explicitly excused.

## 002-D evaluation-instrument baseline

002-D formalizes:

```text
Rubric     → defines valid individual judgment
Scorecard  → records one Judge's judgment
```

Criterion and Note remain subordinate state. Every authoritative Scorecard references exactly one authoritative Rubric version, and later Rubric versions never silently rebind existing Scorecards. Scored Criteria are required in the initial baseline; missing, zero, and N/A remain distinct, and N/A has no implicit semantics.

A Rubric uses one coherent scoring model. The specification permits additive-points or weighted-rating semantics but prohibits accidental double weighting. Weighted scales must define an explicit rating-to-contribution mapping rather than relying on an unstated interpretation of a 1–5 or similar scale.

Scorecard lifecycle is:

```text
Draft → Finalized
           │
           ▼
     Amendment Draft
       ├── abandon → prior Finalized remains authoritative
       └── finalize → new Finalized version
```

One Judge Participation × one Encounter yields at most one logical Scorecard. Drafts do not contribute to official aggregation. Finalization creates authoritative judging evidence; an Amendment Draft does not displace the prior authoritative version until finalized. Scorecard author, Encounter, Team basis, and Rubric basis cannot be silently changed by amendment.

Criterion Notes and overall Notes are private evaluation evidence, do not independently alter numeric scoring, and are versioned with the Scorecard. Paper and electronic Scorecards share identical evaluation semantics; capture actor/channel differences belong to Provenance. Intra-Scorecard calculation is deterministic from Criterion responses plus the exact Rubric; cross-Judge aggregation remains for 002-F.

## 002-E authoritative-history baseline

002-E formalizes:

```text
Versioning  → what authoritative states existed
Provenance  → how, why, and through whose authority they arose
```

Committed Versions are immutable reconstructible snapshots. Draft/autosave activity is not version history. A lineage has one current authoritative Version, prior Versions remain historical, and stale-base successor commits must not silently fork authoritative history.

Correction authority follows the meaning of the change. A Judge may amend their own evaluation judgment when Access permits. An Organizer may correct Competition-administrative facts and verified paper transcription errors, but Organizer authority does not substitute for Judge evaluation authorship. Technical Administrator authority likewise does not substitute for Competition or Judge semantic authority.

002-E distinguishes working edits, author amendments, transcription corrections, structural corrections, and outcome-affecting administrative corrections. Supersession and invalidation are distinct: a newer Version supersedes an older state of the same logical subject, while invalidation means evidence should no longer count for an official purpose. Structural identity errors such as wrong Team, Judge, Encounter, or Rubric basis are not silently repaired by ordinary Scorecard amendment.

Event Completed raises correction requirements: post-event Judge amendments require Organizer-authorized temporary scoped Access, Judge re-verification, and a human-readable reason. Competition Finalized raises them further and requires explicit post-finalization governance plus affected-outcome review. Source changes cause dependent derived values to refresh or become marked affected; official Awards/outcomes never silently migrate after finalization.

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

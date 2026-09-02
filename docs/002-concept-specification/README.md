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
| 002-D | Rubric, Criterion, Scorecard & Notes Specifications | **Next** |
| 002-E | Versioning, Provenance, Correction & Authority Preservation | Planned |
| 002-F | Aggregation, Coverage, Ranking & Evaluation Policy | Planned |
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

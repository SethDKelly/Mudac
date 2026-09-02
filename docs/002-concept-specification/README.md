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
| 002-A | Competition, Division, Team & Alias Specifications | **In Progress** |
| 002-B | Identity, Participation & Access Specifications | Planned |
| 002-C | Panel, Membership & Judging Encounter Specifications | Planned |
| 002-D | Rubric, Criterion, Scorecard & Notes Specifications | Planned |
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

---
type: Canonical Mapping Authority Baseline
title: Phase 013 Mapping Authority, Evidence & Canonical Ownership Baseline
description: "Current Phase-013 authority/evidence classification and Experience-owner topology, advanced through 013-C context and Judge-entry mapping."
status: stable
tags: [canonical, experience, mapping, authority, evidence, terminology, ownership, phase-013]
sources:
  - resource: ../../013-concept-mapping-interaction-semantics-user-visible-representation/013-A-mapping-scope-representation-semantics-experience-risk-subphase-planning.md
  - resource: ../../013-concept-mapping-interaction-semantics-user-visible-representation/013-B-experience-corpus-reconciliation-terminology-mapping-authority-canonical-ownership-baseline.md
  - resource: ../../013-concept-mapping-interaction-semantics-user-visible-representation/013-C-context-identity-participation-access-bias-control-judge-entry-mapping.md
  - resource: phase-013-entry-handoff.md
  - resource: ../concepts/
  - resource: ../synchronizations/
  - resource: ../dependence/product-family-scope.md
  - resource: ../policies/
  - resource: ../invariants/
---

# Purpose

Provide the durable Phase-013 baseline for deciding **what mapping knowledge is current authority, what remains admitted evidence, and where later user-visible semantic knowledge belongs**.

This document prevents pre-convergence UX language or document structure from overriding the current MUDAC Concept model.

# Current authority order

```text
Project Purpose / Mandate
  ↓
Current Concepts
  ↓
Current Synchronizations / Application Action Surface
  ↓
Current Dependence / Capability Rules / PF-01 Scope
  ↓
Current mapping-relevant Policies + Invariants
  ↓
Phase 013 Mapping Entry Authority
  ↓
THIS Mapping Authority Baseline
  ↓
Experience owners explicitly accepted/reworked by completed Phase-013 workstreams
```

Architecture, implementation and incumbent interface structure are not mapping authority.

# Current mapping authority through 013-C

Current mapping authority now includes:

- `phase-013-entry-handoff.md`;
- this baseline;
- completed Phase-013 records 013-A through 013-C;
- [Experience Context and Participation Modes](context-role-modes.md) for operating-context, capacity-mode, multi-capacity, disclosure-context and historical-context mapping;
- [Judge Entry, Participation & Readiness Mapping](judge-onboarding.md) for Judge-entry, Identity continuity, Competition Participation, entry readiness and Panel-planning context mapping.

These two Experience owners were substantively rewritten in 013-C and are no longer merely pre-convergence candidates for their natural subjects.

# Remaining admitted Experience evidence

The following remain admitted evidence/candidates until their assigned workstream accepts or rewrites them:

- `action-authority-traceability.md` — cross-cutting, final acceptance audit in 013-K;
- `judge-evaluation.md` — 013-E/F;
- `organizer-preparation.md` — 013-D;
- `live-operations.md` — 013-G;
- `reconciliation-finalization.md` — 013-G/H then supersede;
- `paper-export-publication.md` — 013-F/I then supersede;
- `accessibility-resilience.md` — 013-J;
- `status-feedback-recovery.md` — 013-J.

If admitted evidence conflicts with current Concept, synchronization, dependence, policy, invariant or accepted Phase-013 mapping authority, the newer authority wins.

# Owner disposition and status

| Experience owner | Current authority status | Planned/accepted disposition |
| --- | --- | --- |
| `context-role-modes.md` | **current mapping authority** | rewritten/accepted 013-C |
| `judge-onboarding.md` | **current mapping authority** | rewritten/accepted 013-C |
| `action-authority-traceability.md` | admitted cross-cutting evidence | revalidate incrementally; final audit 013-K |
| `organizer-preparation.md` | admitted evidence | rewrite/revalidate 013-D |
| `judge-evaluation.md` | admitted evidence | active evaluation 013-E; correction/history split 013-F |
| `live-operations.md` | admitted evidence | rewrite/revalidate 013-G |
| `reconciliation-finalization.md` | admitted evidence | replace through 013-G/H owners then supersede |
| `paper-export-publication.md` | admitted evidence | split through 013-F/I owners then supersede |
| `accessibility-resilience.md` | admitted evidence | rewrite/revalidate 013-J |
| `status-feedback-recovery.md` | admitted evidence | rewrite/revalidate 013-J |

# Approved natural owner topology

Existing retained owners:

```text
context-role-modes.md              → current authority after 013-C
judge-onboarding.md                → current authority after 013-C
organizer-preparation.md           → 013-D
judge-evaluation.md                → 013-E active evaluation
live-operations.md                 → 013-G live-event operations
accessibility-resilience.md        → 013-J
status-feedback-recovery.md        → 013-J
action-authority-traceability.md   → cross-cutting, final audit 013-K
```

New owners are created only when substantive content exists:

```text
authority-lineage-correction.md       013-F
reconciliation-derived-state.md       013-G
outcome-officiality.md                013-H
external-representation-release.md    013-I
```

Owners to supersede after all valid rules migrate:

```text
reconciliation-finalization.md
paper-export-publication.md
```

# Terminology contract

`Judging Encounter` / `Encounter` is not a current Concept. Interpret older uses by actual meaning:

```text
bounded evaluation event/history/participants → Evaluation Occurrence
individual evaluator responsibility          → Evaluation Obligation
Judge-authored evaluation evidence            → Scorecard
planned evaluator grouping                    → Panel
actor-to-Competition relationship             → Participation
permission/disclosure decision                → Access
```

Mechanical replacement is prohibited.

`Official Outcome Revision` remains deprecated; current official authority/currentness/successor history is owned by Outcome Declaration.

Derived/projection terms such as `Ready to Judge`, `Competition Ready`, `Ranking Readiness`, `Finalization Readiness`, Coverage, Aggregate, Rank and reconciliation/exception projections do not become editable Concepts.

# 013-C context contract

013-C establishes:

```text
Identity != Participation != Access
role/capacity mode = representation of one current Participation context
mode/navigation != authority
multi-capacity capabilities are never unioned
Judge context carries Judge-safe disclosure posture
Panel membership != occurrence participation != responsibility != evidence
Ready to Judge = derived explanation, not writable state or responsibility
technical support privilege != Competition decision authority
```

One protected operation is interpreted under one explicit current Participation context. A context switch selects another legitimate Participation for representation; it does not mutate Participation or grant Access.

# Application-action rule

Map the established Phase-011 application action surface:

```text
D — direct application action
C — coordinated application action
P — composition-only participant
S — system-triggered conceptual reaction
X — intentionally unavailable generic application action
```

Do not expose `P` or `X` as generic user controls.

In particular, `Access.check` remains composition-only/system guard behavior and generic Access grant/revoke administration remains unavailable absent purpose-specific composition.

# Explanation-order rule

```text
dependence order != navigation order
synchronization chain != mandatory wizard
```

Represent enough upstream context, basis and authority for downstream state/action meaning to be interpreted correctly. Do not turn the dependence graph into interface architecture.

# PF-01 mapping scope

The sole current product/application variant remains:

> **PF-01 — MUDAC Live Competition Judging & Official Outcome**

Panel use/assignment, paper/electronic capture, Award presence, public/non-public operation and other supported conditions remain profiles/states unless a future product-family decision says otherwise.

013-C specifically prevents absence of a current Panel assignment from becoming a universal product blocker unless current policy/readiness actually requires it.

# Workstream-to-owner baseline

## Completed 013-C

Current destinations:

- `context-role-modes.md`;
- `judge-onboarding.md`.

## 013-D

Primary destination:

- `organizer-preparation.md`.

## 013-E

Primary destination:

- `judge-evaluation.md`.

## 013-F

Primary new destination:

- `authority-lineage-correction.md`.

## 013-G

Primary destinations:

- `live-operations.md`;
- `reconciliation-derived-state.md`.

## 013-H

Primary new destination:

- `outcome-officiality.md`.

## 013-I

Primary new destination:

- `external-representation-release.md`.

## 013-J

Primary destinations:

- `accessibility-resilience.md`;
- `status-feedback-recovery.md`.

## 013-K

Primary responsibilities:

- final cross-owner reconciliation;
- acceptance/rewrite of `action-authority-traceability.md`;
- terminology/authority consistency audit;
- duplicate/supersession cleanup.

# Retrieval discipline during Phase 013

For a mapping task:

1. load the active Phase-013 workstream record;
2. load this baseline;
3. load task-relevant current Concept/synchronization/dependence/policy/invariant owners;
4. load current accepted Experience owners relevant to the task;
5. load remaining admitted Experience candidates only as evidence;
6. write durable mapping truth only to the natural owner;
7. do not preload architecture/implementation unless explicitly analyzing contamination/history.

# Reopen routing

```text
purpose conflict → project-purpose authority
undefined Concept behavior/state/action → natural Concept owner / Phase 010 if boundary-level
missing/invalid application action or synchronization → Phase 011
incorrect dependence/scope/PF-01 assumption → Phase 012
stale wording/reference with clear current meaning → repair natural owner
mapping terminology/representation/ownership defect → Phase 013
```

# Current state

```text
013-A  COMPLETE — READY
013-B  COMPLETE — PASS
013-C  COMPLETE — PASS
013-D  NEXT
architecture authority: SUSPENDED
implementation planning: SUSPENDED
implementation readiness: NOT READY
implementation authorization: NOT YET
```

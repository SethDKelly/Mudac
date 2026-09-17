---
type: Canonical Mapping Authority Baseline
title: Phase 013 Mapping Authority, Evidence & Canonical Ownership Baseline
description: "Current Phase-013 authority/evidence classification and Experience-owner topology, advanced through 013-G live-operations/reconciliation/derived-state mapping."
status: stable
tags: [canonical, experience, mapping, authority, evidence, terminology, ownership, phase-013]
sources:
  - resource: ../../013-concept-mapping-interaction-semantics-user-visible-representation/013-A-mapping-scope-representation-semantics-experience-risk-subphase-planning.md
  - resource: ../../013-concept-mapping-interaction-semantics-user-visible-representation/013-B-experience-corpus-reconciliation-terminology-mapping-authority-canonical-ownership-baseline.md
  - resource: ../../013-concept-mapping-interaction-semantics-user-visible-representation/013-C-context-identity-participation-access-bias-control-judge-entry-mapping.md
  - resource: ../../013-concept-mapping-interaction-semantics-user-visible-representation/013-D-competition-preparation-competitor-panel-rubric-setup-readiness-organizer-configuration-mapping.md
  - resource: ../../013-concept-mapping-interaction-semantics-user-visible-representation/013-E-evaluation-occurrence-obligation-judgment-action-availability-feedback-mapping.md
  - resource: ../../013-concept-mapping-interaction-semantics-user-visible-representation/013-F-authority-lineage-paper-capture-amendment-correction-historical-state-mapping.md
  - resource: ../../013-concept-mapping-interaction-semantics-user-visible-representation/013-G-live-operations-remaining-work-exception-reconciliation-derived-outcome-state-mapping.md
  - resource: phase-013-entry-handoff.md
  - resource: ../concepts/
  - resource: ../synchronizations/
  - resource: ../dependence/product-family-scope.md
  - resource: ../policies/
  - resource: ../invariants/
---

# Purpose

Provide the durable Phase-013 baseline for deciding **what mapping knowledge is current authority, what remains admitted evidence, and where later user-visible semantic knowledge belongs**.

Architecture, implementation and incumbent interface structure are not mapping authority.

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

# Current mapping authority through 013-G

Current mapping authority includes:

- `phase-013-entry-handoff.md`;
- this baseline;
- completed Phase-013 records 013-A through 013-G;
- [Experience Context and Participation Modes](context-role-modes.md);
- [Judge Entry, Participation & Readiness Mapping](judge-onboarding.md);
- [Organizer Competition Preparation & Readiness Mapping](organizer-preparation.md);
- [Judge Active Evaluation Mapping](judge-evaluation.md);
- [Authority Lineage, Capture & Correction Mapping](authority-lineage-correction.md);
- [Organizer Live Operations & Remaining Work Mapping](live-operations.md);
- [Reconciliation & Derived Outcome-State Mapping](reconciliation-derived-state.md).

These owners are current mapping authority for their natural subjects.

# Remaining admitted Experience evidence

The following remain admitted evidence/candidates until their assigned workstream accepts, rewrites or supersedes them:

- `action-authority-traceability.md` — cross-cutting; final acceptance audit in 013-K;
- `reconciliation-finalization.md` — **historical evidence adapter only after 013-G**; reconciliation/derived-state mapping moved to `reconciliation-derived-state.md`, while Award/finalization/officiality evidence remains pending 013-H;
- `paper-export-publication.md` — historical evidence adapter only after 013-F; Export/Publication evidence remains pending 013-I;
- `accessibility-resilience.md` — 013-J;
- `status-feedback-recovery.md` — 013-J.

# Owner disposition and status

| Experience owner | Current authority status | Planned/accepted disposition |
| --- | --- | --- |
| `context-role-modes.md` | **current mapping authority** | rewritten/accepted 013-C |
| `judge-onboarding.md` | **current mapping authority** | rewritten/accepted 013-C |
| `organizer-preparation.md` | **current mapping authority** | rewritten/accepted 013-D |
| `judge-evaluation.md` | **current mapping authority** | rewritten/accepted 013-E |
| `authority-lineage-correction.md` | **current mapping authority** | created/accepted 013-F |
| `live-operations.md` | **current mapping authority** | rewritten/accepted 013-G |
| `reconciliation-derived-state.md` | **current mapping authority** | created/accepted 013-G |
| `action-authority-traceability.md` | admitted cross-cutting evidence | revalidate incrementally; final audit 013-K |
| `reconciliation-finalization.md` | historical/admitted evidence adapter | reconciliation migrated 013-G; Award/finalization/officiality migrate 013-H |
| `paper-export-publication.md` | historical/admitted evidence adapter | paper/correction migrated 013-F; Export/Publication migrate 013-I |
| `accessibility-resilience.md` | admitted evidence | rewrite/revalidate 013-J |
| `status-feedback-recovery.md` | admitted evidence | rewrite/revalidate 013-J |

# Natural owner topology

```text
context-role-modes.md              → current authority after 013-C
judge-onboarding.md                → current authority after 013-C
organizer-preparation.md           → current authority after 013-D
judge-evaluation.md                → current authority after 013-E
authority-lineage-correction.md    → current authority after 013-F
live-operations.md                 → current authority after 013-G
reconciliation-derived-state.md    → current authority after 013-G
accessibility-resilience.md        → 013-J
status-feedback-recovery.md        → 013-J
action-authority-traceability.md   → cross-cutting, final audit 013-K
```

Future owners are created only when substantive content exists:

```text
outcome-officiality.md                013-H
external-representation-release.md    013-I
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

Derived/projection terms such as `Ready to Judge`, `Competition Readiness`, Remaining Work, Coverage, Aggregate, Rank, `Ranking Readiness`, `Finalization Readiness`, reconciliation items and exception projections do not become editable Concepts.

# Current context / preparation / active-evaluation contracts

Preserve 013-C/D/E:

```text
Identity != Participation != Access
role/capacity mode = representation, not authority
multi-capacity capabilities are never unioned
Judge context carries Judge-safe disclosure posture
Ready to Judge = derived, not writable
preparation = composed source view, not workflow authority
Competition Readiness = derived, not editable
source sufficiency != Competition lifecycle Ready
Competition Ready != Active
Panel membership != occurrence participation != responsibility != evidence
Prepared occurrence != begun occurrence != responsibility
Occurrence Complete != obligation Satisfied != Scorecard Finalized
one Evaluation Obligation → at most one logical Scorecard
Scorecard Draft != authoritative judgment
Draft complete/valid != Finalized
exact bound Evaluation Basis != latest working Rubric
uncertain authoritative result != confirmed success
Organizer/support capability != Judge authorship
```

# 013-F authority-lineage contract

Preserve:

```text
paper / assisted / electronic capture = same evaluation model
capture Actor != Judge semantic author / RepresentedAuthority
initial Finalized authority != reopenable Draft
Judge semantic amendment != source-faithful capture correction
superseded != invalidated != replaced != affected != stale
structural Scorecard identity never silently changes through amendment/capture correction
historical obligation satisfaction != current evidence eligibility
terminal Evaluation Obligation never reopens
legitimate repeat responsibility = successor Evaluation Obligation + new logical Scorecard
replacement occurrence creates distinct history; no automatic participant/obligation/evidence cloning
current correction != silent historical rewrite
```

# 013-G live-operations / reconciliation contract

013-G establishes:

```text
Live Operations
  = Organizer work context, not Concept/lifecycle authority

Remaining Work
  = projection over current Outstanding Evaluation Obligations
  != manually maintained task state

Event Completed
  != all obligations terminal
  != all Scorecards Finalized
  != Coverage Satisfied
  != reconciliation complete

historically Satisfied obligation
  != current evidence eligibility

ineligible evidence
  != reopened predecessor obligation
  != automatic successor Judge work

warning
  != blocker
  != governed exception
  != correction
  != technical intervention

acknowledge / hide / suppress
  != source resolution

Reconciliation
  = source-directed Organizer work
  != Competition lifecycle state
  != generic ticket system

Coverage = Satisfied | Incomplete
Coverage exception disposition is separate

Aggregate existence
  != Coverage Satisfied
  != rank eligibility
  != Ranking Ready
  != official outcome

Rank
  = derived / non-editable
  != Ranking Readiness
  != Award authority
  != official outcome

Ranking Readiness / Finalization Readiness
  = derived permission-to-proceed projections
  != writable authority

calculated
  != recognized
  != official
  != public
```

A governed exception preserves the source shortfall and changes only the explicitly permitted consequence. It cannot rewrite Coverage, fabricate evidence, transfer Judge authorship or bypass unrelated policy.

Derived currentness follows source change → affected/non-current derivation → recomputation against current authoritative basis. Recalculation never edits source truth.

# Application-action rule

Phase 013 maps the established application action classes:

```text
D — direct application action
C — coordinated application action
P — composition-only participant
S — system-triggered conceptual reaction
X — intentionally unavailable generic application action
```

Do not expose `P` or `X` as generic user controls.

Generic Versioning/Provenance administration, manual Coverage/Rank editing, generic reconciliation `resolve`, and universal `override` remain unavailable.

Purpose-specific source actions, governed exceptions and owner-specific correction paths change the underlying state; derived projections then recompute.

# Explanation-order rule

```text
dependence order != navigation order
synchronization chain != mandatory wizard
preparation dependency != setup step number
```

Live Operations and Reconciliation may group source conditions for understanding without becoming source ownership or a mandatory workflow engine.

# PF-01 mapping scope

The sole current product/application variant remains:

> **PF-01 — MUDAC Live Competition Judging & Official Outcome**

Paper/electronic/mixed capture, optional Awards, public/non-public operation and other supported profiles remain states/capabilities rather than product variants.

# Workstream-to-owner baseline

## Completed 013-C
- `context-role-modes.md`;
- `judge-onboarding.md`.

## Completed 013-D
- `organizer-preparation.md`.

## Completed 013-E
- `judge-evaluation.md`.

## Completed 013-F
- `authority-lineage-correction.md`;
- `paper-export-publication.md` demoted to historical/evidence adapter.

## Completed 013-G
- `live-operations.md`;
- `reconciliation-derived-state.md`;
- `reconciliation-finalization.md` demoted to historical/evidence adapter for remaining 013-H material.

## 013-H
- `outcome-officiality.md`.

## 013-I
- `external-representation-release.md`.

## 013-J
- `accessibility-resilience.md`;
- `status-feedback-recovery.md`.

## 013-K
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
013-D  COMPLETE — PASS
013-E  COMPLETE — PASS
013-F  COMPLETE — PASS
013-G  COMPLETE — PASS
013-H  NEXT
architecture authority: SUSPENDED
implementation planning: SUSPENDED
implementation readiness: NOT READY
implementation authorization: NOT YET
```

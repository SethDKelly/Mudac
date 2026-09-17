---
type: Canonical Mapping Authority Baseline
title: Phase 013 Mapping Authority, Evidence & Canonical Ownership Baseline
description: "Current Phase-013 authority/evidence classification and Experience-owner topology, advanced through 013-H Award/finalization/outcome-officiality mapping."
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
  - resource: ../../013-concept-mapping-interaction-semantics-user-visible-representation/013-H-award-competition-finalization-outcome-declaration-officiality-successor-authority-mapping.md
  - resource: phase-013-entry-handoff.md
  - resource: ../concepts/
  - resource: ../synchronizations/
  - resource: ../dependence/product-family-scope.md
  - resource: ../policies/
  - resource: ../invariants/
---

# Purpose

Provide the durable Phase-013 baseline for deciding **what mapping knowledge is current authority, what remains admitted/historical evidence, and where later user-visible semantic knowledge belongs**.

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

# Current mapping authority through 013-H

Current accepted Experience owners are:

- [Experience Context and Participation Modes](context-role-modes.md) — 013-C;
- [Judge Entry, Participation & Readiness Mapping](judge-onboarding.md) — 013-C;
- [Organizer Competition Preparation & Readiness Mapping](organizer-preparation.md) — 013-D;
- [Judge Active Evaluation Mapping](judge-evaluation.md) — 013-E;
- [Authority Lineage, Capture & Correction Mapping](authority-lineage-correction.md) — 013-F;
- [Organizer Live Operations & Remaining Work Mapping](live-operations.md) — 013-G;
- [Reconciliation & Derived Outcome-State Mapping](reconciliation-derived-state.md) — 013-G;
- [Award, Finalization & Outcome Officiality Mapping](outcome-officiality.md) — 013-H.

Completed Phase-013 records 013-A through 013-H are current design evidence/decisions for their stated workstreams.

# Remaining admitted/historical Experience evidence

- `action-authority-traceability.md` — admitted cross-cutting evidence; final acceptance audit 013-K;
- `reconciliation-finalization.md` — **historical evidence only** after 013-G/H; all current subjects migrated;
- `paper-export-publication.md` — historical/admitted evidence adapter; only Export/Publication material remains pending 013-I;
- `accessibility-resilience.md` — admitted evidence pending 013-J;
- `status-feedback-recovery.md` — admitted evidence pending 013-J.

Historical `stable` metadata or file location under `canonical/experience/` does not override this baseline.

# Natural owner topology

```text
context-role-modes.md              → current authority after 013-C
judge-onboarding.md                → current authority after 013-C
organizer-preparation.md           → current authority after 013-D
judge-evaluation.md                → current authority after 013-E
authority-lineage-correction.md    → current authority after 013-F
live-operations.md                 → current authority after 013-G
reconciliation-derived-state.md    → current authority after 013-G
outcome-officiality.md             → current authority after 013-H
external-representation-release.md → 013-I
accessibility-resilience.md        → 013-J
status-feedback-recovery.md        → 013-J
action-authority-traceability.md   → cross-cutting, final audit 013-K
```

# Terminology contract

`Judging Encounter` / `Encounter` is not a current Concept. Route older use by meaning:

```text
bounded evaluation event/history/participants → Evaluation Occurrence
individual evaluator responsibility          → Evaluation Obligation
Judge-authored evaluation evidence            → Scorecard
planned evaluator grouping                    → Panel
actor-to-Competition relationship             → Participation
permission/disclosure decision                → Access
```

`Official Outcome Revision` is deprecated and must not be restored. Current official authority/currentness/history belongs to Outcome Declaration.

Derived/projection terms such as Ready to Judge, Competition Readiness, Remaining Work, Coverage, Aggregate, Rank, Ranking Readiness, Finalization Readiness, reconciliation items and exception projections are not editable Concepts.

# Core context / preparation / active-evaluation contract

Preserve 013-C/D/E:

```text
Identity != Participation != Access
role/capacity mode = representation, not authority
multi-capacity capabilities never union
Judge context carries Judge-safe disclosure posture
preparation = composed source view, not Workflow authority
Competition Readiness = derived, not editable
source sufficiency != Competition lifecycle Ready
Competition Ready != Active
Panel membership != occurrence participation != responsibility != evidence
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
Finalized initial Scorecard != reopenable Draft
Judge amendment != source-faithful capture correction
superseded != invalidated != replaced != affected != stale
structural Scorecard identity cannot silently change through amendment/capture correction
historical obligation satisfaction != current evidence eligibility
terminal Evaluation Obligation never reopens
legitimate repeat responsibility = successor Evaluation Obligation + new logical Scorecard
replacement occurrence does not clone participants/responsibility/evidence
current correction != silent historical rewrite
```

# 013-G live-operations / reconciliation contract

Preserve:

```text
Live Operations = Organizer work context, not Concept/lifecycle authority
Remaining Work = projection over current Outstanding Evaluation Obligations
Event Completed != all Judge work done
historically Satisfied obligation != current evidence eligibility
ineligible evidence != reopened predecessor obligation != automatic successor work
warning != blocker != governed exception != correction != technical intervention
acknowledgement / suppression != source resolution
Reconciliation = source-directed work, not lifecycle/ticket authority
Coverage = Satisfied | Incomplete
Coverage exception disposition is separate
Aggregate existence != Coverage Satisfied != rank eligibility != Ranking Ready
Rank = derived/non-editable
Ranking Readiness / Finalization Readiness = derived/non-editable
calculated != recognized != official != public
```

A governed exception preserves source truth and changes only a specifically permitted consequence.

# 013-H Award / officiality contract

013-H establishes:

```text
calculated
  != ranking ready
  != recognized
  != Competition Finalized
  != official
  != public
  != delivered

Ranking Ready candidate
  != Award conferral

rank-derived Award selection
  != discretionary Award selection

later Rank/source change
  != automatic Award transfer

Finalization Readiness = true
  != Competition Finalized
  != Outcome Declaration exists

ordinary closeout
  = coordinated Competition.finalize + OutcomeDeclaration.declare

ordinary closeout success
  = Competition Finalized + one current Outcome Declaration

Competition lifecycle ownership
  != Outcome Declaration content/currentness ownership

Outcome Declaration currentness
  = Current | Affected | Superseded

Affected
  != Superseded
  != corrected calculations are official

post-Finalization source correction
  → Competition remains Finalized
  → derived state recomputes as needed
  → Award reviewed/corrected explicitly if required
  → declaration becomes Affected when its basis materially depends on changed source

Affected declaration
  → explicit Confirm Successor Outcome Declaration
  → successor Current
  → predecessor Superseded

successor declaration
  != re-finalize Competition

same visible result
  != same declared basis

Outcome Declaration
  != Export
  != Publication
  != delivery
```

Only explicit Outcome Declaration establishes official outcome authority. A current/Affected declaration remains immutable as declared; new calculations do not silently rewrite it.

Official-but-non-public is a legitimate PF-01 profile/state.

# Application-action rule

Phase 013 maps the established application action classes:

```text
D — direct application action
C — coordinated application action
P — composition-only participant
S — system-triggered conceptual reaction
X — intentionally unavailable generic action
```

Do not expose `P` or `X` as generic controls.

Examples of purpose-specific application authority now mapped include:

- Start/Finalize Evaluation;
- Judge amendment and capture correction;
- purpose-specific invalidation/replacement/successor-responsibility actions;
- governed exception actions;
- Confer Rank-Derived Award;
- Confer Discretionary Award;
- Award revoke/correct-conferral actions;
- Finalize Competition & Declare Outcome;
- Identify Official Outcome Affected;
- Confirm Successor Outcome Declaration.

Generic Versioning/Provenance administration, manual Coverage/Rank editing, generic reconciliation `resolve`, universal override, generic declaration editing and automatic Publication remain unavailable.

# High-consequence explanation rule

Before/after a high-consequence mapped action, preserve enough meaning to understand:

- what authority is being created, succeeded, invalidated, revoked or corrected;
- the actor/declaring/represented authority where materially distinct;
- the source/basis being committed;
- what history remains;
- whether the action changes recognition, lifecycle, officiality, disclosure or only a subset;
- whether downstream actions are automatic (normally not unless current synchronization explicitly says so).

Unknown authoritative outcomes must never be represented as confirmed success.

# Explanation-order rule

```text
dependence order != navigation order
synchronization chain != mandatory wizard
preparation dependency != setup step number
```

Authority chains explain meaning; they do not prescribe screen order or implementation orchestration.

# PF-01 mapping scope

The sole current product/application variant remains:

> **PF-01 — MUDAC Live Competition Judging & Official Outcome**

Optional Awards, official-but-non-public operation, Export without Publication, paper/electronic/mixed capture and Affected/Superseded authority remain profiles/states within PF-01 rather than separate product variants.

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
- `paper-export-publication.md` demoted for paper/correction semantics.

## Completed 013-G
- `live-operations.md`;
- `reconciliation-derived-state.md`.

## Completed 013-H
- `outcome-officiality.md`;
- `reconciliation-finalization.md` retired to historical evidence only.

## 013-I
- `external-representation-release.md`;
- finish migration/retirement decision for `paper-export-publication.md`.

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
5. load remaining admitted/historical Experience only when useful as evidence;
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
013-H  COMPLETE — PASS
013-I  NEXT
architecture authority: SUSPENDED
implementation planning: SUSPENDED
implementation readiness: NOT READY
implementation authorization: NOT YET
```

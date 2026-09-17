---
type: Canonical Mapping Authority Baseline
title: Phase 013 Mapping Authority, Evidence & Canonical Ownership Baseline
description: "Current Phase-013 authority/evidence classification and Experience-owner topology, advanced through 013-F authority-lineage/correction mapping."
status: stable
tags: [canonical, experience, mapping, authority, evidence, terminology, ownership, phase-013]
sources:
  - resource: ../../013-concept-mapping-interaction-semantics-user-visible-representation/013-A-mapping-scope-representation-semantics-experience-risk-subphase-planning.md
  - resource: ../../013-concept-mapping-interaction-semantics-user-visible-representation/013-B-experience-corpus-reconciliation-terminology-mapping-authority-canonical-ownership-baseline.md
  - resource: ../../013-concept-mapping-interaction-semantics-user-visible-representation/013-C-context-identity-participation-access-bias-control-judge-entry-mapping.md
  - resource: ../../013-concept-mapping-interaction-semantics-user-visible-representation/013-D-competition-preparation-competitor-panel-rubric-setup-readiness-organizer-configuration-mapping.md
  - resource: ../../013-concept-mapping-interaction-semantics-user-visible-representation/013-E-evaluation-occurrence-obligation-judgment-action-availability-feedback-mapping.md
  - resource: ../../013-concept-mapping-interaction-semantics-user-visible-representation/013-F-authority-lineage-paper-capture-amendment-correction-historical-state-mapping.md
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

# Current mapping authority through 013-F

Current mapping authority includes:

- `phase-013-entry-handoff.md`;
- this baseline;
- completed Phase-013 records 013-A through 013-F;
- [Experience Context and Participation Modes](context-role-modes.md);
- [Judge Entry, Participation & Readiness Mapping](judge-onboarding.md);
- [Organizer Competition Preparation & Readiness Mapping](organizer-preparation.md);
- [Judge Active Evaluation Mapping](judge-evaluation.md);
- [Authority Lineage, Capture & Correction Mapping](authority-lineage-correction.md).

These owners are current mapping authority for their natural subjects.

# Remaining admitted Experience evidence

The following remain admitted evidence/candidates until their assigned workstream accepts, rewrites or supersedes them:

- `action-authority-traceability.md` — cross-cutting; final acceptance audit in 013-K;
- `live-operations.md` — 013-G;
- `reconciliation-finalization.md` — 013-G/H then supersede;
- `paper-export-publication.md` — **historical evidence adapter only** after 013-F; paper/correction mapping has moved to `authority-lineage-correction.md`, while Export/Publication evidence remains pending 013-I;
- `accessibility-resilience.md` — 013-J;
- `status-feedback-recovery.md` — 013-J.

# Owner disposition and status

| Experience owner | Current authority status | Planned/accepted disposition |
| --- | --- | --- |
| `context-role-modes.md` | **current mapping authority** | rewritten/accepted 013-C |
| `judge-onboarding.md` | **current mapping authority** | rewritten/accepted 013-C |
| `organizer-preparation.md` | **current mapping authority** | rewritten/accepted 013-D |
| `judge-evaluation.md` | **current mapping authority** | rewritten/accepted 013-E for ordinary active evaluation |
| `authority-lineage-correction.md` | **current mapping authority** | created/accepted 013-F |
| `action-authority-traceability.md` | admitted cross-cutting evidence | revalidate incrementally; final audit 013-K |
| `live-operations.md` | admitted evidence | rewrite/revalidate 013-G |
| `reconciliation-finalization.md` | admitted evidence | replace through 013-G/H owners then supersede |
| `paper-export-publication.md` | historical/admitted evidence adapter | paper/correction migrated 013-F; Export/Publication migrate 013-I |
| `accessibility-resilience.md` | admitted evidence | rewrite/revalidate 013-J |
| `status-feedback-recovery.md` | admitted evidence | rewrite/revalidate 013-J |

# Natural owner topology

```text
context-role-modes.md              → current authority after 013-C
judge-onboarding.md                → current authority after 013-C
organizer-preparation.md           → current authority after 013-D
judge-evaluation.md                → current authority after 013-E active evaluation
authority-lineage-correction.md    → current authority after 013-F
live-operations.md                 → 013-G live-event operations
accessibility-resilience.md        → 013-J
status-feedback-recovery.md        → 013-J
action-authority-traceability.md   → cross-cutting, final audit 013-K
```

Future owners are created only when substantive content exists:

```text
reconciliation-derived-state.md       013-G
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

Derived/projection terms such as `Ready to Judge`, `Competition Readiness`, `Ranking Readiness`, `Finalization Readiness`, Coverage, Aggregate, Rank and reconciliation/exception projections do not become editable Concepts.

# Current context / preparation / active-evaluation contracts

Preserve 013-C/D/E:

```text
Identity != Participation != Access
role/capacity mode = representation, not authority
multi-capacity capabilities are never unioned
Judge context carries Judge-safe disclosure posture
Ready to Judge = derived, not writable
preparation = composed source view, not owning Workflow/Setup state
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
presentation end / navigation / autosave != Judge Finalization
uncertain authoritative result != confirmed success
Organizer/support capability != Judge authorship
```

# 013-F authority-lineage contract

013-F establishes:

```text
paper / assisted / electronic capture
  = same evaluation semantics and one logical Scorecard

capture Actor
  != Judge semantic author / RepresentedAuthority

initial Finalized authority
  != reopenable Draft

Judge semantic amendment
  != source-faithful capture correction

superseded
  != invalidated
  != replaced
  != affected
  != stale

structural Scorecard identity
  = Evaluator + Subject + OccurrenceContext + EvaluationBasis
  → never silently changed through amendment/capture correction

historical obligation satisfaction
  != current evidence eligibility

terminal Evaluation Obligation
  → never reopened

legitimate repeat responsibility
  → successor Evaluation Obligation + new logical Scorecard

replacement occurrence
  → distinct history; no automatic participant/obligation/evidence cloning

current correction
  != silent historical rewrite
```

Paper-origin transcription is non-authoritative until source fidelity and Judge completed/committed intent are established. Ambiguous Judge intent remains ambiguous.

Judge amendment creates successor authority for the same logical Scorecard while preserving one vote. Capture correction similarly creates successor authority for the same logical Scorecard, but records unchanged Judge intent from a verified source and may have a different capture/correction Actor.

Invalidation retains history, does not revive older predecessors automatically, and does not itself create replacement or successor work.

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

Generic Versioning and Provenance administration remains intentionally unavailable. Purpose-specific actions such as Finalize Evaluation, Finalize Judge Amendment, Correct Authoritative Capture, evidence/occurrence invalidation and governed successor-work decisions compose those Concepts without exposing them as raw administration.

# Action / consequence explanation rule

For high-consequence authority actions, the mapping must make the semantic target and consequence intelligible without prescribing a particular UI control.

At minimum distinguish:

- what current authority will be succeeded or invalidated;
- whether history remains;
- whether Judge judgment changes;
- who acts versus whose authority/content is represented;
- whether structural identity is preserved;
- whether current eligibility changes;
- whether replacement or successor work is automatic (**it is not**).

Unknown authoritative outcomes must never be represented as confirmed success.

# Explanation-order rule

```text
dependence order != navigation order
synchronization chain != mandatory wizard
preparation dependency != setup step number
```

Authority lineage is explanatory history, not a required screen sequence or workflow engine.

# PF-01 mapping scope

The sole current product/application variant remains:

> **PF-01 — MUDAC Live Competition Judging & Official Outcome**

Paper/electronic/mixed capture remains a PF-01 profile, not a separate product. 013-F establishes semantic parity across those paths.

# Workstream-to-owner baseline

## Completed 013-C

- `context-role-modes.md`;
- `judge-onboarding.md`.

## Completed 013-D

- `organizer-preparation.md`.

## Completed 013-E

- `judge-evaluation.md` for ordinary active evaluation.

## Completed 013-F

- `authority-lineage-correction.md` for amendment, paper/assisted capture authority, source-faithful correction, invalidation, replacement, successor responsibility and current/historical authority;
- `paper-export-publication.md` demoted to a historical/evidence adapter; its remaining Export/Publication content is pending 013-I.

## 013-G

- `live-operations.md`;
- `reconciliation-derived-state.md`.

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
013-G  NEXT
architecture authority: SUSPENDED
implementation planning: SUSPENDED
implementation readiness: NOT READY
implementation authorization: NOT YET
```
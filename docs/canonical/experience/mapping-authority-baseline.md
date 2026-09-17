---
type: Canonical Mapping Authority Baseline
title: Phase 013 Mapping Authority, Evidence & Canonical Ownership Baseline
description: "Current Phase-013 authority/evidence classification and Experience-owner topology established by 013-B before substantive mapping begins."
status: stable
tags: [canonical, experience, mapping, authority, evidence, terminology, ownership, phase-013]
sources:
  - resource: ../../013-concept-mapping-interaction-semantics-user-visible-representation/013-A-mapping-scope-representation-semantics-experience-risk-subphase-planning.md
  - resource: ../../013-concept-mapping-interaction-semantics-user-visible-representation/013-B-experience-corpus-reconciliation-terminology-mapping-authority-canonical-ownership-baseline.md
  - resource: phase-013-entry-handoff.md
  - resource: ../concepts/
  - resource: ../synchronizations/
  - resource: ../dependence/product-family-scope.md
  - resource: ../policies/
  - resource: ../invariants/
---

# Purpose

Provide the durable Phase-013 baseline for deciding **what mapping knowledge is current authority, what is admitted evidence, and where later user-visible semantic knowledge belongs**.

This document prevents pre-convergence UX language or document structure from overriding the current MUDAC Concept model.

It is an authority/ownership baseline, not a finished UX specification.

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
Experience owners explicitly accepted/reworked by 013-C through 013-K
```

Architecture, implementation and incumbent interface structure are not mapping authority.

# Authority classes

## Current conceptual authority

Current meaning remains owned by:

- `docs/canonical/project/`;
- `docs/canonical/concepts/`;
- `docs/canonical/synchronizations/`;
- `docs/canonical/dependence/`;
- current `docs/canonical/policies/`;
- current `docs/canonical/invariants/`.

## Current mapping authority

Before later substantive work is accepted, current mapping authority consists of:

- `phase-013-entry-handoff.md`;
- this baseline;
- accepted rules in completed Phase-013 records.

As 013-C through 013-K complete, their reconciled canonical Experience owners become current mapping authority for their natural subjects.

## Admitted Experience evidence

The ten pre-convergence Experience contracts remain useful design evidence but **are not authoritative as-is**:

- `context-role-modes.md`;
- `action-authority-traceability.md`;
- `judge-onboarding.md`;
- `judge-evaluation.md`;
- `organizer-preparation.md`;
- `live-operations.md`;
- `reconciliation-finalization.md`;
- `paper-export-publication.md`;
- `accessibility-resilience.md`;
- `status-feedback-recovery.md`.

If one conflicts with a current Concept, synchronization, dependence, policy, invariant or this baseline, the newer conceptual authority wins.

# Corpus disposition

| Existing Experience owner | Authority now | Planned disposition | Subphase |
| --- | --- | --- | --- |
| `context-role-modes.md` | admitted evidence | rewrite/revalidate in place | 013-C |
| `action-authority-traceability.md` | admitted cross-cutting evidence | retain and revalidate across workstreams; final acceptance audit | 013-C–K |
| `judge-onboarding.md` | admitted evidence | rewrite/revalidate in place | 013-C |
| `judge-evaluation.md` | admitted evidence | retain active-evaluation mapping; move amendment/correction/history semantics to distinct owner | 013-E/F |
| `organizer-preparation.md` | admitted evidence | rewrite/revalidate in place | 013-D |
| `live-operations.md` | admitted evidence | rewrite/revalidate in place | 013-G |
| `reconciliation-finalization.md` | admitted evidence | replace through separate reconciliation-derived-state and outcome-officiality owners, then supersede | 013-G/H |
| `paper-export-publication.md` | admitted evidence | split paper/correction from external representation/release, then supersede | 013-F/I |
| `accessibility-resilience.md` | admitted evidence | rewrite/revalidate in place | 013-J |
| `status-feedback-recovery.md` | admitted evidence | rewrite/revalidate in place | 013-J |

No file becomes current mapping authority merely because its path contains `canonical` or its historical front matter says `stable`.

# Approved natural owner topology

## Existing owners retained

```text
context-role-modes.md
  context / role-mode / operating-context representation

judge-onboarding.md
  Judge entry / current Competition / Participation / readiness mapping

organizer-preparation.md
  preparation / configuration / derived readiness mapping

judge-evaluation.md
  active evaluation / basis / responsibility / Draft / Finalization mapping

live-operations.md
  event-day exception-first operational mapping

accessibility-resilience.md
  accessible / device / degraded semantic parity

status-feedback-recovery.md
  status dimensions / uncertainty / feedback / recovery grammar

action-authority-traceability.md
  cross-cutting mapping-to-semantic-owner traceability
```

## New owners created only when substantive content exists

```text
authority-lineage-correction.md       013-F
reconciliation-derived-state.md       013-G
outcome-officiality.md                013-H
external-representation-release.md    013-I
```

Do not create empty placeholders before their workstream produces durable mapping knowledge.

## Owners to supersede after migration

```text
reconciliation-finalization.md
paper-export-publication.md
```

They remain evidence until all still-valid rules have a current natural owner.

# Terminology contract

## Encounter is deprecated

`Judging Encounter` / `Encounter` is not a current Concept.

Interpret older uses by meaning:

```text
bounded evaluation event/history/participants
  → Evaluation Occurrence

individual evaluator responsibility/outstanding work
  → Evaluation Obligation

Judge-authored evaluation artifact/evidence
  → Scorecard

planned evaluator grouping
  → Panel

actor-to-Competition relationship
  → Participation

permission to perceive/invoke
  → Access
```

Mechanical replacement is prohibited.

## Official Outcome Revision is deprecated

Current declared official authority is **Outcome Declaration**.

```text
current declaration
Affected declaration
successor declaration
Superseded historical declaration
```

are Outcome Declaration meanings, not an `Official Outcome Revision` Concept.

## Derived/projection terms remain derived

The following may be represented and explained but do not become independently editable Concepts:

```text
Ready to Judge
Competition Ready
Ranking Readiness
Finalization Readiness
Coverage
Aggregate
Rank
reconciliation/exception projections
```

A user acts on authoritative sources or an explicitly governed exception/correction action, not on the projection as if it owned source truth.

## Role/navigation vocabulary does not create authority

A selected role mode, route, work area, tab, link, QR code or navigation context cannot create Identity, Participation, Access, responsibility or domain authority.

# Required conceptual distinctions

All later mappings preserve, where material:

```text
Identity != Participation != Access
Panel membership != occurrence participation != Evaluation Obligation != Scorecard evidence
Draft/preserved work != authoritative Scorecard
historical satisfaction != current evidence eligibility
missing != zero != incomplete != governed exception
Coverage/Aggregate/Rank != Award authority
Competition Finalization != Outcome Declaration
calculated != recognized != official != public != delivered
source authority != Export != Publication != transport delivery
supersession != invalidation != replacement != successor
technical privilege != competition decision authority
```

# Application-action rule

Map the established Phase-011 application action surface:

```text
D — direct application action
C — coordinated application action
P — composition-only participant
S — system-triggered conceptual reaction
X — intentionally unavailable generic action
```

Do not expose `P` or `X` as generic user controls merely because an intrinsic Concept action exists.

Cross-Concept composition questions route to the seven current synchronization owners. `concept-synchronizations.md` is historical routing evidence only.

# Explanation-order rule

```text
dependence order != navigation order
synchronization chain != mandatory wizard
```

Represent enough upstream context, basis and authority for downstream state/action meaning to be interpreted correctly. Do not turn the dependence graph into interface architecture.

# PF-01 mapping scope

The sole current product/application variant is:

> **PF-01 — MUDAC Live Competition Judging & Official Outcome**

The following remain profiles/states within PF-01 rather than separate products:

- Award present/absent;
- public/non-public;
- Export without Publication;
- paper/electronic/mixed capture;
- Draft/authoritative Scorecard;
- Event Completed/Finalized;
- current/Affected/Superseded declaration authority;
- ordinary/successor declaration;
- discretionary/rank-derived Award selection.

# Workstream-to-owner baseline

## 013-C

Primary destinations:

- `context-role-modes.md`;
- `judge-onboarding.md`;
- cross-cutting updates to `action-authority-traceability.md` where accepted.

## 013-D

Primary destination:

- `organizer-preparation.md`.

## 013-E

Primary destination:

- `judge-evaluation.md`.

Amendment/correction/history rules that are not ordinary active evaluation move to 013-F rather than remaining bundled here.

## 013-F

Primary new destination:

- `authority-lineage-correction.md`.

This owner absorbs current user-visible semantics for amendment, paper capture, represented authority, correction, invalidation/replacement, successor work and current/historical distinctions.

## 013-G

Primary destinations:

- `live-operations.md`;
- new `reconciliation-derived-state.md`.

The latter owns explanation of outstanding work, Coverage/Aggregate/Rank/Readiness and reconciliation projections without making them editable workflow state.

## 013-H

Primary new destination:

- `outcome-officiality.md`.

It owns user-visible distinctions among calculated result, Award/recognition, Competition Finalization, Outcome Declaration, affected authority and successor declaration.

## 013-I

Primary new destination:

- `external-representation-release.md`.

It owns Export source/currentness/audience semantics and Publication release/withdrawal/supersession/external-recipient meaning.

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

# Current policy terminology repairs

013-B repaired two bounded active-policy references whose meaning was already unambiguous:

- anonymity/disclosure exposure consequences now refer to affected **Evaluation Occurrence and/or dependent evaluation evidence** rather than `Encounter/evidence`;
- operational exception governance now preserves who actually participated in an **Evaluation Occurrence** rather than who participated in an `Encounter`.

Historical phase filenames and source links are provenance and remain unchanged.

# Retrieval discipline during Phase 013

For a mapping task:

1. load the active Phase-013 workstream record;
2. load this baseline;
3. load task-relevant current Concept/synchronization/dependence/policy/invariant owners;
4. load only the incoming Experience candidates relevant to that workstream;
5. treat their unreconciled claims as evidence, not as authority;
6. write durable new mapping truth only to the natural owner established here or explicitly justified by the workstream;
7. do not preload architecture/implementation unless the task is explicitly contamination/history analysis.

# Reopen routing

```text
purpose conflict
  → project-purpose authority

undefined Concept behavior/state/action
  → natural Concept owner / Phase 010 if boundary-level

missing/invalid application action or synchronization
  → Phase 011

incorrect dependence/scope/PF-01 assumption
  → Phase 012

stale wording/reference with clear current meaning
  → repair natural current owner

mapping terminology/representation/ownership defect
  → Phase 013
```

# Non-goals

This baseline does not define:

- exact screen/page hierarchy;
- route tree;
- frontend framework or component system;
- visual design tokens;
- view-model/client state architecture;
- API or transport behavior;
- persistence schema;
- runtime/AWS topology;
- executable UI implementation/tests.

# Current state

```text
013-A  COMPLETE — READY
013-B  COMPLETE — PASS
013-C  NEXT
architecture authority: SUSPENDED
implementation planning: SUSPENDED
implementation readiness: NOT READY
implementation authorization: NOT YET
```

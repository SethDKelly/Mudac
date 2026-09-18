---
type: Canonical Mapping Authority Baseline
title: Phase 013 Mapping Authority, Evidence & Canonical Ownership Baseline
description: "Current Phase-013 authority/evidence classification and Experience-owner topology, advanced through 013-J accessibility/degraded-operation/status/recovery semantic-parity mapping."
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
  - resource: ../../013-concept-mapping-interaction-semantics-user-visible-representation/013-I-export-publication-audience-disclosure-external-recipient-representation-release-mapping.md
  - resource: ../../013-concept-mapping-interaction-semantics-user-visible-representation/013-J-accessibility-degraded-operation-status-feedback-recovery-semantic-parity-mapping.md
  - resource: phase-013-entry-handoff.md
---

# Purpose

Provide the durable Phase-013 baseline for deciding what mapping knowledge is current authority, what remains historical/admitted evidence, and where later user-visible semantic knowledge belongs.

Architecture and implementation remain outside mapping authority.

# Authority order

```text
Project Purpose / Mandate
  ↓
Current Concepts
  ↓
Current Synchronizations / Application Action Surface
  ↓
Current Dependence / PF-01 Scope
  ↓
Policies + Invariants
  ↓
Phase 013 Entry Authority
  ↓
THIS baseline
  ↓
Experience owners accepted by completed Phase-013 workstreams
```

# Current accepted Experience owners through 013-J

- [Experience Context and Participation Modes](context-role-modes.md) — 013-C;
- [Judge Entry, Participation & Readiness Mapping](judge-onboarding.md) — 013-C;
- [Organizer Competition Preparation & Readiness Mapping](organizer-preparation.md) — 013-D;
- [Judge Active Evaluation Mapping](judge-evaluation.md) — 013-E;
- [Authority Lineage, Capture & Correction Mapping](authority-lineage-correction.md) — 013-F;
- [Organizer Live Operations & Remaining Work Mapping](live-operations.md) — 013-G;
- [Reconciliation & Derived Outcome-State Mapping](reconciliation-derived-state.md) — 013-G;
- [Award, Finalization & Outcome Officiality Mapping](outcome-officiality.md) — 013-H;
- [External Representation, Disclosure & Release Mapping](external-representation-release.md) — 013-I;
- [Accessibility, Responsive & Degraded-Operation Mapping](accessibility-resilience.md) — 013-J;
- [Status, Feedback & Recovery Mapping](status-feedback-recovery.md) — 013-J.

Completed Phase-013 records 013-A through 013-J are current design decisions for their workstreams.

# Remaining admitted / historical Experience material

- `action-authority-traceability.md` — admitted cross-cutting evidence; final acceptance/rewrite audit in 013-K;
- `reconciliation-finalization.md` — historical only; all current semantics migrated by 013-G/H;
- `paper-export-publication.md` — historical only; all current semantics migrated by 013-F/I.

No other pre-convergence Experience contract is current merely because it resides under `canonical/experience/`.

# Natural owner topology

```text
context-role-modes.md              → current after 013-C
judge-onboarding.md                → current after 013-C
organizer-preparation.md           → current after 013-D
judge-evaluation.md                → current after 013-E
authority-lineage-correction.md    → current after 013-F
live-operations.md                 → current after 013-G
reconciliation-derived-state.md    → current after 013-G
outcome-officiality.md             → current after 013-H
external-representation-release.md → current after 013-I
accessibility-resilience.md        → current after 013-J
status-feedback-recovery.md        → current after 013-J
action-authority-traceability.md   → final cross-owner audit 013-K
```

# Terminology contract

`Judging Encounter` / `Encounter` remains deprecated; route older wording by actual meaning.

`Official Outcome Revision` remains deprecated; official currentness/history belongs to Outcome Declaration.

Readiness, Remaining Work, Coverage, Aggregate, Rank, reconciliation projections and operational attention states remain derived/non-editable.

# Core preserved distinctions

```text
Identity != Participation != Access
Panel membership != occurrence participation != responsibility != evidence
Occurrence Complete != obligation Satisfied != Scorecard Finalized
one Evaluation Obligation → at most one logical Scorecard
Scorecard Draft != authoritative judgment
capture Actor != Judge semantic author
Judge amendment != capture correction
superseded != invalidated != replaced != affected != stale
historical obligation satisfaction != current evidence eligibility
Remaining Work = Outstanding-obligation projection
Coverage factual state != exception disposition
Aggregate existence != Coverage/rank readiness
Rank = derived/non-editable
calculated != recognized != Competition Finalized != official != public != delivered
Outcome Declaration != Export != Publication != delivery
```

# 013-I external representation / release contract

```text
source authority != Export representation != Publication release != delivery
actor Access != audience disclosure
Export SourceBasis = exact / historically stable
Export generation != Publication
Export currency = Current | Affected | Stale | Superseded | Retired
Export currency != Publication distribution state
new/corrected source → new Export, never rewrite historical Export
successor Outcome Declaration != successor Export != successor Publication
withdrawal/supersession != historical release or external-copy erasure
recipient possession != current release authority / interactive Access
Publication Published != delivery/viewing success
```

# 013-J semantic-parity / recovery contract

013-J establishes:

```text
accessible / responsive / degraded / paper paths
  = same domain semantics and authority boundaries

accessible path
  != alternate authority model

responsive layout
  != permission to hide material blocker/consequence

assistive actor
  != semantic author by assistance alone

device / route / session / QR possession
  != current Access

interruption / device change / retry
  → recover same logical work
  != duplicate semantic effect

local/device working state
  != confirmed persisted state
  != authoritative domain state

paper fallback
  != second evaluation model

result unknown
  != confirmed success
  != confirmed failure

retry/recovery
  → reconcile current authority first
  → converge on one legitimate result

stale local state
  != permission to overwrite newer authority

status
  = multidimensional / subject-qualified
  != one universal badge

working persistence feedback
  != semantic commitment

technical recovery capability
  != broader Access / disclosure / semantic authority
```

Unknown authority transitions remain explicit until resolved. High-consequence success requires authoritative confirmation.

# Application-action rule

```text
D — direct application action
C — coordinated application action
P — composition-only participant
S — system-triggered conceptual reaction
X — intentionally unavailable generic action
```

Do not expose `P` or `X` as generic controls. Alternate interaction/recovery paths do not create new application actions or weaker substitutes for unavailable authority.

# High-consequence explanation rule

Before/after consequential action, preserve enough meaning to understand:

- source/basis and authority being changed;
- actor versus represented authority where materially distinct;
- confirmed versus uncertain outcome;
- what local/Draft work remains;
- what history remains;
- what downstream meanings did not change;
- legitimate retry/recovery path if needed.

# Explanation-order rule

```text
dependence order != navigation order
synchronization chain != mandatory wizard
```

Accessible/responsive/degraded presentation may change presentation order for usability but cannot waive semantic prerequisites or consequences.

# PF-01 scope

The sole current product/application variant remains **PF-01 — MUDAC Live Competition Judging & Official Outcome**.

Accessibility, responsive presentation, degraded connectivity, paper operation, official-but-non-public operation and other supported profiles are not product variants.

# Remaining Phase-013 ownership

## 013-K
- whole-experience explanation-order audit;
- cross-role/profile consistency audit;
- acceptance/rewrite of `action-authority-traceability.md`;
- terminology/action/authority consistency audit;
- duplicate/supersession cleanup.

## 013-L
- canonical mapping reconciliation;
- Phase-013 exit review;
- Phase-014 handoff.

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
013-I  COMPLETE — PASS
013-J  COMPLETE — PASS
013-K  NEXT
architecture authority: SUSPENDED
implementation planning: SUSPENDED
implementation readiness: NOT READY
implementation authorization: NOT YET
```

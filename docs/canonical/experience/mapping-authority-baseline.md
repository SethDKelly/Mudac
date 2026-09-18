---
type: Canonical Mapping Authority Baseline
title: Phase 013 Mapping Authority, Evidence & Canonical Ownership Baseline
description: "Current Phase-013 authority/evidence classification and Experience-owner topology, advanced through 013-I external representation/disclosure/release mapping."
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

# Current accepted Experience owners through 013-I

- [Experience Context and Participation Modes](context-role-modes.md) — 013-C;
- [Judge Entry, Participation & Readiness Mapping](judge-onboarding.md) — 013-C;
- [Organizer Competition Preparation & Readiness Mapping](organizer-preparation.md) — 013-D;
- [Judge Active Evaluation Mapping](judge-evaluation.md) — 013-E;
- [Authority Lineage, Capture & Correction Mapping](authority-lineage-correction.md) — 013-F;
- [Organizer Live Operations & Remaining Work Mapping](live-operations.md) — 013-G;
- [Reconciliation & Derived Outcome-State Mapping](reconciliation-derived-state.md) — 013-G;
- [Award, Finalization & Outcome Officiality Mapping](outcome-officiality.md) — 013-H;
- [External Representation, Disclosure & Release Mapping](external-representation-release.md) — 013-I.

Completed Phase-013 records 013-A through 013-I are current design decisions for their workstreams.

# Remaining admitted / historical Experience material

- `action-authority-traceability.md` — admitted cross-cutting evidence; final acceptance audit in 013-K;
- `reconciliation-finalization.md` — historical evidence only; all current semantics migrated by 013-G/H;
- `paper-export-publication.md` — historical evidence only; all current semantics migrated by 013-F/I;
- `accessibility-resilience.md` — admitted evidence pending 013-J;
- `status-feedback-recovery.md` — admitted evidence pending 013-J.

Historical file location or `stable` metadata does not override this baseline.

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
accessibility-resilience.md        → 013-J
status-feedback-recovery.md        → 013-J
action-authority-traceability.md   → final audit 013-K
```

# Terminology contract

`Judging Encounter` / `Encounter` is deprecated. Route older usage by meaning to Evaluation Occurrence, Evaluation Obligation, Scorecard, Panel, Participation or Access.

`Official Outcome Revision` is deprecated. Current official authority/currentness/history belongs to Outcome Declaration.

Readiness, Remaining Work, Coverage, Aggregate, Rank, reconciliation projections and exception projections remain derived/non-editable.

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
terminal obligations never reopen
Remaining Work = Outstanding-obligation projection
Coverage factual state != exception disposition
Aggregate existence != Coverage/rank readiness
Rank = derived/non-editable
calculated != recognized != Competition Finalized != official != public != delivered
```

# 013-H officiality contract

```text
Ranking Ready candidate != Award conferral
rank-derived Award != discretionary Award
Finalization Readiness != Competition Finalized
ordinary closeout = Competition.finalize + OutcomeDeclaration.declare
ordinary closeout success = Competition Finalized + current Outcome Declaration
Outcome Declaration currentness = Current | Affected | Superseded
Affected != Superseded
corrected calculations != successor official authority
successor declaration != re-finalize Competition
Outcome Declaration != Export != Publication != delivery
```

Only Outcome Declaration establishes official result authority.

# 013-I external representation / release contract

013-I establishes:

```text
source authority
  != Export representation
  != Publication release
  != delivery / recipient possession

actor can inspect fact
  != fact may appear in Export
  != fact may be released to Audience

Export SourceBasis
  = exact and historically stable

Export generation
  != Publication

Export currency
  = Current | Affected | Stale | Superseded | Retired

Export currency
  != Publication distribution state

Affected Export
  may be revalidated only against unchanged exact SourceBasis

new/corrected source required
  → new Export
  != rewrite old Export

successor Outcome Declaration
  != successor Export
  != successor Publication

Publication Published
  != delivery/viewing success

withdrawal/supersession
  != erasure of historical release or external copies

recipient possession
  != Export Current
  != Publication currently Published
  != interactive Access
```

AudienceProfile and representation purpose are semantic inputs. Organizer/technical Access does not create disclosure permission or publishing authority.

Official-but-non-public and Export-without-Publication remain legitimate PF-01 states/profiles.

# Application-action rule

```text
D — direct application action
C — coordinated application action
P — composition-only participant
S — system-triggered conceptual reaction
X — intentionally unavailable generic action
```

Do not expose `P` or `X` as generic controls.

Purpose-specific actions now include Generate/Revalidate/Retire Export, Publish/Withdraw Publication and Publish Successor Representation. Automatic declaration→publication and correction→withdraw/regenerate/republish remain intentionally unavailable.

# High-consequence explanation rule

Before/after consequential action, preserve enough meaning to understand:

- source/basis and authority being represented or changed;
- intended purpose/audience;
- actor versus represented/publishing authority where materially distinct;
- what history remains;
- whether currentness, officiality, disclosure, release or delivery changed;
- which downstream transitions are not automatic.

Unknown authoritative outcomes must never be represented as confirmed success.

# Explanation-order rule

```text
dependence order != navigation order
synchronization chain != mandatory wizard
```

# PF-01 scope

The sole current product/application variant remains **PF-01 — MUDAC Live Competition Judging & Official Outcome**.

Optional Awards, official-but-non-public operation, Export without Publication, paper/electronic/mixed capture and current/Affected/Superseded authority remain profiles/states within PF-01.

# Remaining Phase-013 ownership

## 013-J
- `accessibility-resilience.md`;
- `status-feedback-recovery.md`.

## 013-K
- final cross-owner reconciliation;
- acceptance/rewrite of `action-authority-traceability.md`;
- terminology/authority consistency audit;
- duplicate/supersession cleanup.

## 013-L
- canonical mapping reconciliation;
- Phase-013 exit review and Phase-014 handoff.

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
013-J  NEXT
architecture authority: SUSPENDED
implementation planning: SUSPENDED
implementation readiness: NOT READY
implementation authorization: NOT YET
```

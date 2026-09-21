---
type: Canonical Mapping Authority Baseline
title: Phase 013 Mapping Authority, Evidence & Canonical Ownership Baseline
description: "Final reconciled Phase-013 authority/evidence classification and Experience-owner topology after 013-L exit review."
status: stable
tags: [canonical, experience, mapping, authority, evidence, terminology, ownership, phase-013]
sources:
  - resource: ../../013-concept-mapping-interaction-semantics-user-visible-representation/013-A-mapping-scope-representation-semantics-experience-risk-subphase-planning.md
  - resource: ../../013-concept-mapping-interaction-semantics-user-visible-representation/013-K-whole-experience-explanation-order-cross-role-profile-consistency-mapping-integrity-audit.md
  - resource: ../../013-concept-mapping-interaction-semantics-user-visible-representation/013-L-canonical-mapping-reconciliation-phase-013-consolidation-phase-014-handoff.md
  - resource: phase-013-entry-handoff.md
---

# Purpose

Provide the durable final Phase-013 baseline for deciding what mapping knowledge is current authority, what is historical evidence, and where user-visible semantics belong.

Phase 013 is **COMPLETE — PASS**. Architecture and implementation remain outside mapping authority and remain suspended pending later methodology closure.

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
Phase 013 Mapping Entry Authority
  ↓
THIS baseline
  ↓
accepted Experience owners
```

Experience mapping explains and exposes current semantics; it does not replace upstream ownership.

# Final accepted Experience owners

| Owner | Natural subject | Accepted |
| --- | --- | --- |
| [Experience Context and Participation Modes](context-role-modes.md) | Competition/capacity context, multi-capacity isolation, disclosure context | 013-C / reconciled 013-K |
| [Judge Entry, Participation & Readiness Mapping](judge-onboarding.md) | Judge entry, Participation, Panel context, Ready-to-Judge | 013-C / reconciled 013-K |
| [Organizer Competition Preparation & Readiness Mapping](organizer-preparation.md) | preparation, source setup, Competition Readiness | 013-D |
| [Judge Active Evaluation Mapping](judge-evaluation.md) | occurrence, obligation, Draft, initial Finalization | 013-E |
| [Authority Lineage, Capture & Correction Mapping](authority-lineage-correction.md) | paper/assisted capture, amendment, correction, invalidation, replacement, successor responsibility | 013-F |
| [Organizer Live Operations & Remaining Work Mapping](live-operations.md) | live coordination, actual work state, remaining responsibility, operational exceptions | 013-G |
| [Reconciliation & Derived Outcome-State Mapping](reconciliation-derived-state.md) | eligible evidence, Coverage, Aggregate, Rank, readiness, reconciliation | 013-G |
| [Award, Finalization & Outcome Officiality Mapping](outcome-officiality.md) | Award recognition, closeout, Outcome Declaration, successor officiality | 013-H |
| [External Representation, Disclosure & Release Mapping](external-representation-release.md) | Export, audience disclosure, currency, Publication and external-recipient semantics | 013-I |
| [Accessibility, Responsive & Degraded-Operation Mapping](accessibility-resilience.md) | accessible/responsive/degraded/paper semantic parity | 013-J |
| [Status, Feedback & Recovery Mapping](status-feedback-recovery.md) | multidimensional status, uncertainty, confirmation and recovery | 013-J |
| [Whole-Experience Action, Explanation & Authority Traceability](action-authority-traceability.md) | cross-owner explanation order, action traceability, role/profile consistency and mapping-integrity guardrails | 013-K |

This is the complete current Experience mapping corpus after Phase 013.

# Historical Experience evidence only

The following remain for provenance and must not compete with current owners:

- `reconciliation-finalization.md` — historical mixed adapter; current semantics migrated by 013-G/H;
- `paper-export-publication.md` — historical mixed adapter; current semantics migrated by 013-F/I.

Historical file location or `stable` metadata does not override this classification.

# Terminology contract

Current Experience authority uses:

```text
Evaluation Occurrence     not Judging Encounter
Evaluation Obligation     not generic assignment/task authority
Outcome Declaration       not Official Outcome Revision
```

Owner-qualified state vocabularies remain distinct:

```text
Outcome Declaration: Current | Affected | Superseded
Export currency:      Current | Affected | Stale | Superseded | Retired
Publication:          Published | Withdrawn | Superseded
Evaluation Obligation: Outstanding | Satisfied | Excused | Cancelled
```

`Complete`, `Finalized`, `Satisfied`, `Ready`, `Current`, `Published` and `Resolved` are subject-qualified meanings, not generic workflow status.

# Core context and authority distinctions

Preserve globally:

```text
Identity != Participation != Access
role/capacity mode != authority
multi-capacity capabilities never union
Panel membership != occurrence participation != responsibility != evidence
Occurrence Complete != obligation Satisfied != Scorecard Finalized
one Evaluation Obligation → at most one logical Scorecard
Scorecard Draft != authoritative judgment
capture Actor != Judge semantic author / RepresentedAuthority
Judge amendment != source-faithful capture correction
historical obligation satisfaction != current evidence eligibility
terminal obligations never reopen
```

# Event-completion reconciliation

013-K repaired an earlier Judge-entry overstatement:

```text
Event Completed
  → ordinary live-entry/readiness context ends
  != all obligations terminal
  != all Scorecards Finalized
  != universal hidden Access revocation
```

If an Outstanding obligation remains and current policy/Access permits continuation, the Judge may continue the same logical evaluation. Later amendment/correction/history actions still use their own narrow authority.

# Derived-state distinctions

```text
Remaining Work = projection over Outstanding obligations
Coverage factual state != exception disposition
Aggregate existence != Coverage satisfaction / rank eligibility
Rank = derived / non-editable
Rank != Award authority
Ranking Readiness / Finalization Readiness = derived / non-editable
acknowledgement != source resolution
```

Reconciliation and Live Operations remain work contexts, not lifecycle/ticket authorities.

# Officiality and externalization distinctions

```text
calculated
  != ranking ready
  != recognized
  != Competition Finalized
  != official
  != public
  != delivered

ordinary closeout
  = Competition.finalize + OutcomeDeclaration.declare

Outcome Declaration
  != Export
  != Publication
  != delivery

Export currency
  != Publication distribution state

successor Outcome Declaration
  != successor Export
  != successor Publication
```

Official-but-non-public and Export-without-Publication remain legitimate PF-01 states/profiles.

# Cross-role / profile contract

Judge, Organizer, support and external-recipient views interpret the same underlying source authority through different legitimate context/disclosure rules.

```text
Judge Participation capability
  + Organizer Participation capability
  != unioned capability

actor can inspect fact
  != fact may appear in Export
  != fact may be released to Audience
```

Judge-safe, Organizer-sensitive, Ceremony-safe, Public and internal history/audit profiles may omit or faithfully transform information. They may not invent/promote source truth or erase history.

# Accessibility / recovery contract

```text
ordinary-path semantics
  = accessible-path semantics
  = responsive-path semantics
  = degraded/recovery-path semantics
  = paper/assisted-path semantics
```

where the same operation is available.

Preserve:

```text
assistive actor != semantic author by assistance alone
device / route / session / QR possession != current Access
local working state != confirmed persistence != authoritative state
paper fallback != second evaluation model
result unknown != success != failure
stale local state cannot overwrite newer authority
technical recovery capability != broader Access/disclosure/authority
```

Safe unavailability is preferable to a degraded semantic shortcut.

# Whole-experience explanation grammar

Where materially relevant, explain:

```text
1. current Competition / capacity / audience context
2. subject or resource
3. current authoritative or working state
4. material qualification / blocker / uncertainty
5. legitimate purpose-specific action
6. consequence
7. confirmed result and retained history
```

This is an explanation order only.

```text
dependence order != navigation order
synchronization chain != mandatory wizard
explanation order != mandatory screen order
```

# Application-action rule

Phase 013 maps the Phase-011 action surface:

```text
D — direct application action
C — coordinated application action
P — composition-only participant
S — system-triggered conceptual reaction
X — intentionally unavailable generic action
```

`P` and `X` are never generic UI controls.

Screens, routes, work modes, checklists, confirmations, status badges and recovery states create no additional action class or semantic authority.

# High-consequence explanation and feedback

Before/after consequential action, preserve enough meaning to understand:

- target subject/source/basis;
- current actor/capacity and represented authority where distinct;
- current blockers/qualifications;
- authority/history consequence;
- what remains unchanged;
- downstream transitions that remain separate.

Preserve:

```text
working persistence != semantic commitment
request dispatched != authority established
result unknown != confirmed success != confirmed failure
```

# PF-01 scope

The sole current product/application variant remains:

> **PF-01 — MUDAC Live Competition Judging & Official Outcome**

Judge/Organizer profiles, Award absence/presence, official-but-non-public operation, Export without Publication, paper/electronic/mixed capture, accessible/degraded operation, and Current/Affected/Superseded history are profiles/states—not product variants.

# Phase-013 risk closure

MAP-R01 through MAP-R16 have no unresolved semantic blocker in the current Experience corpus.

Future defects reopen the natural semantic owner under change governance; Phase-013 closure does not make mapping immutable.

# Post-Phase-014 / Phase-015 handoff

Phase 014 — Familiarity, Reuse & Genericity is **COMPLETE — PASS**. Its vocabulary, genericity and reusable-knowledge refinements are now part of the current design baseline.

Phase 015 — Concept Integrity, Cross-Concept Coherence & Interference uses this Mapping Authority Baseline to test whether combined Experience mappings preserve each Concept's purpose under composition. Phase 015 may change mapping semantics only through an explicit integrity finding routed to the natural Experience owner.

# Reopen routing

```text
purpose conflict → Project Purpose authority
undefined Concept behavior/state/action → natural Concept owner / Phase 010 if boundary-level
missing/invalid application composition → Phase 011
incorrect dependence/PF-01 scope → Phase 012
mapping terminology/representation/ownership defect → current natural Experience owner
stale historical wording with clear current meaning → repair current owner, do not reopen upstream
```

# Final Phase-013 state

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
013-K  COMPLETE — PASS
013-L  COMPLETE — PASS
PHASE 013 COMPLETE — PASS
PHASE 014 COMPLETE — PASS
PHASE 015 IN PROGRESS — 015-A COMPLETE — READY; 015-B COMPLETE — PASS; 015-C COMPLETE — PASS
015-D COMPLETE — PASS
015-E COMPLETE — PASS
015-F COMPLETE — PASS
015-G COMPLETE — PASS
015-H COMPLETE — PASS
015-I NEXT
architecture authority: SUSPENDED
implementation planning: SUSPENDED
implementation readiness: NOT READY
implementation authorization: NOT YET
```

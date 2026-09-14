---
type: Synchronization Contract
title: Competitor Context, Evaluation Occurrence & Obligation Composition
description: "Current MUDAC composition for Team/Division/Alias presentation context, Panel intended grouping, actual Evaluation Occurrence participation, ordinary Evaluation Obligation establishment, participant adjustment, and occurrence completion after Phase 011-D."
status: stable
tags: [synchronization, team, division, alias, panel, evaluation-occurrence, evaluation-obligation, judging, phase-011]
sources:
  - resource: ../../011-concept-composition-synchronization/011-D-team-division-alias-panel-evaluation-occurrence-evaluation-obligation-establishment.md
  - resource: ../concepts/team.md
  - resource: ../concepts/division.md
  - resource: ../concepts/alias.md
  - resource: ../concepts/panel.md
  - resource: ../concepts/evaluation-occurrence.md
  - resource: ../concepts/evaluation-obligation.md
  - resource: ../concepts/participation.md
  - resource: ../concepts/access.md
  - resource: ../mechanisms/panel-membership-composition.md
  - resource: ../policies/panel-composition.md
  - resource: ../policies/evaluation-policy.md
  - resource: ../policies/operational-exception-governance.md
  - resource: ../invariants/current-vs-historical-truth.md
  - resource: ../invariants/missing-never-zero.md
  - resource: ../invariants/one-logical-scorecard.md
  - resource: competition-participation-access.md
generated: { by: openai/gpt-5.6-sol, at: 2026-09-14T01:13:00-05:00 }
---

# Purpose

Define current MUDAC application composition from current competitor/grouping state into one historical [Evaluation Occurrence](../concepts/evaluation-occurrence.md) and individual [Evaluation Obligations](../concepts/evaluation-obligation.md), while preserving independent ownership by [Team](../concepts/team.md), [Division](../concepts/division.md), [Alias](../concepts/alias.md), [Panel](../concepts/panel.md), Participation and Access.

This document supersedes the current-authority meaning of:

- legacy synchronization 05's historical presented-context half;
- legacy synchronization 06;
- legacy synchronization 08's responsibility-establishment half.

Scorecard/evaluation-basis authority remains 011-E work. Invalidation/replacement/successor re-evaluation remains 011-F work.

# Authority boundary

- **Team** owns current administrative competitor identity/status.
- **Division** owns current competitive cohort assignment and correction history.
- **Alias** owns current Judge-facing alternate identity and alias history.
- **Panel** owns reusable intended evaluator grouping/current membership history.
- **Participation** owns whether one Judge is currently participating in the Competition in Judge capacity.
- **Access** owns the current contextual capability/disclosure decision.
- **Evaluation Occurrence** owns the bounded historical occurrence, presented context, actual participant history, occurrence lifecycle/validity and replacement relation.
- **Evaluation Obligation** owns one evaluator's responsibility lifecycle.

Panel membership is not occurrence participation. Occurrence participation is not responsibility. Responsibility is not judgment evidence.

# Prepare Evaluation Occurrence

Application action: **Prepare Evaluation Occurrence**.

Primary participant:

- `EvaluationOccurrence.prepare`.

MUDAC normally binds:

```text
Scope            = current Competition
Subject          = stable Team identity
PresentedContext = Judge-facing competitor snapshot
BasisRef         = exact supplied evaluation-basis reference
```

The presented-context snapshot contains the disclosure-safe competitor facts whose historical value matters to what evaluators encounter, normally including the Alias and Division context used for that judging occurrence.

`prepare` creates **no Evaluation Obligation** and does not assert that every Panel member will judge.

If a material Team/Division/Alias change before begin makes the prepared presentation no longer legitimate, ordinary begin is blocked. A Prepared occurrence may be cancelled and a new one prepared rather than silently rewriting the snapshot.

# Panel supplies intended candidates only

For a Panel-backed path, current Panel members may supply candidate starting evaluators.

The application confirms the actual starting set using current facts such as:

- same Competition scope;
- active/eligible Judge Participation;
- current Access for judging;
- known absence/recusal;
- Panel Composition Policy and any governed exception.

Only the confirmed set is supplied to `EvaluationOccurrence.begin`.

A nominal Panel member known absent before begin does not become an occurrence participant or receive an Evaluation Obligation merely because the membership exists.

Panel-composition exceptions preserve the actual shortfall. They never create fictitious participants or evidence.

# Begin Evaluation Occurrence → establish initial responsibilities

Ordinary initial Evaluation Obligations are established at **occurrence begin**.

Application action: **Begin Evaluation Occurrence**.

Participants:

- `EvaluationOccurrence.begin`;
- `EvaluationObligation.establish` once for each confirmed starting evaluator expected to produce an independent judgment.

Initial obligation bindings are:

```text
Scope         = occurrence Scope
Evaluator     = starting Judge Participation identity
Subject       = occurrence Subject
Basis         = occurrence BasisRef
OccurrenceRef = occurrence identity
EvidenceRef   = none
state         = Outstanding
```

Conditions include:

- Competition is Active under [Competition Lifecycle, Participation & Contextual Access Composition](competition-participation-access.md);
- occurrence is Prepared and eligible to begin;
- the prepared competitor presentation remains legitimate;
- an exact applicable BasisRef is supplied;
- every starting evaluator is a current eligible Judge Participation in the same Competition and is permitted by current Access/context;
- Panel-composition conditions are satisfied or an explicitly allowed governed exception exists where Panel is used;
- no duplicate current initial responsibility already exists for the same evaluator/subject/basis/occurrence meaning.

Postconditions:

- occurrence is Open with the actual starting evaluator set;
- each responsible starting evaluator has one Outstanding Evaluation Obligation;
- no Scorecard is created merely by beginning the occurrence.

# Why begin is the establishment point

MUDAC deliberately rejects three alternatives:

- **Panel membership → obligation**: too early; nominal members may be absent or recused.
- **Prepared occurrence → obligation**: too early; actual starting participation is not yet confirmed and preparation may be abandoned.
- **Scorecard start → obligation**: too late; responsibility must remain visible even before a Judge starts a Scorecard.

Occurrence begin is the first point at which actual participation and current responsibility can be established truthfully together while remaining separate owners.

# Panel membership and occurrence history remain separate

After an occurrence begins, Panel membership/capacity changes affect the reusable grouping and future planning only.

They do not automatically:

- modify occurrence starting/effective participants;
- establish/excuse/reassign obligations;
- rewrite presented competitor context.

If the same operational decision should update both the reusable Panel and one live occurrence, the application may deliberately coordinate the relevant Panel action with the occurrence adjustment. Neither action is implied by the other.

# Participant adjustment requires an explicit responsibility decision

`EvaluationOccurrence.recordParticipantAdjustment` records actual participation change. Responsibility disposition is separately selected according to the real situation.

## Participant leaves but still owes evaluation

- record occurrence adjustment;
- leave the Evaluation Obligation Outstanding.

## Recusal/release with no replacement

- record occurrence adjustment;
- invoke `EvaluationObligation.excuse` with legitimate authority/reason.

Missing evidence remains missing; no zero or placeholder Scorecard is created.

## True substitution

- record outgoing/incoming occurrence adjustment;
- invoke `EvaluationObligation.reassignWithSuccessor` so predecessor responsibility history is preserved and the replacement receives the successor responsibility.

Optional `Panel.replaceMember` participates only when the reusable Panel should also change. One-off occurrence substitution does not force a Panel change.

## Late addition

Where policy permits late entry and the evaluator legitimately receives enough of the required presentation/context to produce a qualifying independent judgment:

- record the late participant adjustment;
- establish a new Outstanding Evaluation Obligation.

If the evaluator is taking over an existing responsibility, use `reassignWithSuccessor` rather than an unrelated new obligation.

If authoritative evidence already exists for the outgoing evaluator, participant adjustment cannot remove it; correction/invalidation belongs to 011-F.

# Complete Evaluation Occurrence

Application action: **Complete Evaluation Occurrence**.

Participant:

- `EvaluationOccurrence.completeOccurrence`.

Completion records that the bounded occurrence ended. It does not wait for or modify Evaluation Obligation state.

A valid current state is:

```text
Occurrence = Complete
Obligation A = Satisfied
Obligation B = Outstanding
Obligation C = Outstanding
```

Occurrence completion therefore does not invoke `satisfy`, `excuse`, `cancel`, Scorecard finalization, or derived outcome actions.

This rule supersedes the pre-Phase-010 Encounter behavior in which completion depended on all evaluation responsibilities being resolved.

# Prepared cancellation

A Prepared occurrence that never meaningfully begins may use `EvaluationOccurrence.cancel`.

Because ordinary initial obligations do not exist before begin, simple Prepared cancellation has no obligation cleanup consequence.

Once an occurrence has begun, later unusability is not represented as pre-begin cancellation. Invalidation/replacement/evidence/successor-work semantics belong to 011-F.

# Current action-surface classification

| Concept action family | Current MUDAC status |
| --- | --- |
| Team ordinary create/update | direct |
| Team withdraw/restore | direct/high-consequence; downstream correction effects 011-F |
| Division define/update/assign | direct |
| Division retire/correctAssignment | direct/high-consequence; downstream effects 011-F/G |
| Alias assign | direct |
| Alias replace/retire | direct/high-consequence; downstream effects 011-F |
| Panel membership/capacity planning actions | direct; no automatic occurrence/obligation effect |
| Panel retire/restore | direct/high-consequence; no historical occurrence rewrite |
| Evaluation Occurrence `prepare` | coordinated application action |
| Evaluation Occurrence `begin` | coordinated; establishes initial obligations |
| Evaluation Occurrence participant adjustment | coordinated; explicit responsibility disposition required |
| Evaluation Occurrence `completeOccurrence` | direct one-action application behavior |
| Evaluation Occurrence `cancel` | direct for Prepared occurrence |
| Evaluation Occurrence invalidation/replacement | deferred to 011-F |
| Evaluation Obligation `establish` | composition-only |
| Evaluation Obligation `excuse` | coordinated exceptional action |
| Evaluation Obligation `reassignWithSuccessor` | coordinated exceptional action |
| Evaluation Obligation `satisfy` | composition-only; 011-E |
| Evaluation Obligation `cancel` / `requireSuccessorEvaluation` | 011-F |

# Composition invariants

1. Current Team/Division/Alias state does not rewrite historical presented occurrence context.
2. Panel membership does not itself create occurrence participation or responsibility.
3. Only actual confirmed starting evaluators enter the starting evaluator set.
4. Ordinary initial obligations are established at occurrence begin, not at planning/preparation and not at Scorecard start.
5. Every initial responsible evaluator has one distinct Outstanding obligation; no placeholder judgment is created.
6. Participant adjustment does not determine responsibility disposition implicitly.
7. Panel changes do not rewrite an already-begun occurrence.
8. Occurrence completion is independent of obligation completion.
9. Missing/excused responsibility never becomes score zero or fabricated evidence.
10. Participant editing cannot erase already-authoritative evaluation evidence.
11. Organizer coordination never transfers Judge authorship.

# Chaining summary

```text
current competitor context
  → EvaluationOccurrence.prepare
```

```text
Panel candidates
 + Participation eligibility
 + Access
 + absence/recusal facts
 + composition policy/exception
      ↓
confirmed starting evaluators
      ↓
EvaluationOccurrence.begin
 + EvaluationObligation.establish × N
```

```text
participant adjustment
      ↓
EvaluationOccurrence.recordParticipantAdjustment
 + explicit responsibility disposition
```

```text
EvaluationOccurrence.completeOccurrence
      ↓
occurrence ends
obligations continue independently
```

These are conceptual composition relationships and prescribe no event bus, transaction, queue, worker, retry, database cascade or UI workflow.

# Deferred composition

- authoritative evaluation basis, Scorecard identity/authority, Versioning/Provenance and paper capture → 011-E;
- occurrence invalidation/replacement, obligation cancellation/successor re-evaluation after evidence invalidation, correction consequences → 011-F;
- Coverage/Aggregate/Rank/Award/Finalization/Outcome Declaration → 011-G;
- application-wide chaining/automation/over-under/synergy closure → 011-I;
- whether Panel is required in every coherent product variant → Phase 012;
- user-visible mapping of occurrence/obligation/participant state → Phase 013.

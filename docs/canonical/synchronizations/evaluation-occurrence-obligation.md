---
type: Synchronization Contract
title: Competitor Context, Evaluation Occurrence & Obligation Composition
description: "Current MUDAC composition for Team/Division/Alias presentation context, Panel intended grouping, actual Evaluation Occurrence participation, ordinary Evaluation Obligation establishment, participant adjustment, occurrence completion, and handoff into current correction/authority families."
status: stable
tags: [synchronization, team, division, alias, panel, evaluation-occurrence, evaluation-obligation, judging, phase-011]
sources:
  - resource: ../../011-concept-composition-synchronization/011-D-team-division-alias-panel-evaluation-occurrence-evaluation-obligation-establishment.md
  - resource: ../../011-concept-composition-synchronization/011-F-temporal-correction-invalidation-replacement-successor-work-affected-state-propagation.md
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
  - resource: temporal-truth-correction.md
generated: { by: openai/gpt-5.6-sol, at: 2026-09-14T13:36:00-05:00 }
---

# Purpose

Define current MUDAC application composition from current competitor/grouping state into one historical [Evaluation Occurrence](../concepts/evaluation-occurrence.md) and individual [Evaluation Obligations](../concepts/evaluation-obligation.md), while preserving independent ownership by Team, Division, Alias, Panel, Participation and Access.

This document supersedes legacy synchronization 05's historical presented-context half, legacy 06, and legacy 08's responsibility-establishment half.

Current Scorecard/evaluation-basis authority is owned by [Evaluation Basis, Scorecard Authority & Capture Composition](evaluation-basis-scorecard-authority.md). Current invalidation/replacement/successor-work semantics are owned by [Temporal Truth, Correction & Historical Authority](temporal-truth-correction.md).

# Authority boundary

- **Team** owns current administrative competitor identity/status.
- **Division** owns current competitive cohort assignment and correction history.
- **Alias** owns current Judge-facing alternate identity and alias history.
- **Panel** owns reusable intended evaluator grouping/current membership history.
- **Participation** owns whether one Judge is currently participating in the Competition in Judge capacity.
- **Access** owns current contextual capability/disclosure decisions.
- **Evaluation Occurrence** owns bounded historical occurrence, presented context, actual participant history, lifecycle/validity and replacement relation.
- **Evaluation Obligation** owns one evaluator's responsibility lifecycle.

Panel membership is not occurrence participation. Occurrence participation is not responsibility. Responsibility is not judgment evidence.

# Prepare Evaluation Occurrence

Application action: **Prepare Evaluation Occurrence**.

Primary participant: `EvaluationOccurrence.prepare`.

MUDAC normally binds:

```text
Scope            = current Competition
Subject          = stable Team identity
PresentedContext = Judge-facing competitor snapshot
BasisRef         = exact supplied evaluation-basis reference
```

The historical presented-context snapshot normally includes the Alias and Division context used for that occurrence.

`prepare` creates no Evaluation Obligation and does not assert that every Panel member will judge.

If material Team/Division/Alias change before begin makes the prepared presentation no longer legitimate, ordinary begin is blocked. A Prepared occurrence may be cancelled and a new one prepared rather than silently rewriting the snapshot.

# Panel supplies intended candidates only

For a Panel-backed path, current Panel members may supply candidate starting evaluators.

The application confirms the actual starting set using current facts such as same Competition scope, active/eligible Judge Participation, current Access, absence/recusal facts, Panel Composition Policy and governed exception state.

Only the confirmed set is supplied to `EvaluationOccurrence.begin`.

A nominal Panel member known absent before begin does not become an occurrence participant or receive an Evaluation Obligation merely because membership exists.

# Begin Evaluation Occurrence → establish initial responsibilities

Ordinary initial Evaluation Obligations are established at **occurrence begin**.

Application action: **Begin Evaluation Occurrence**.

Participants:

- `EvaluationOccurrence.begin`;
- `EvaluationObligation.establish` once for each confirmed starting evaluator expected to produce independent judgment.

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

- Competition Active under [Competition Lifecycle, Participation & Contextual Access Composition](competition-participation-access.md);
- occurrence Prepared and eligible to begin;
- prepared competitor presentation still legitimate;
- one exact applicable BasisRef;
- every starting evaluator is a current eligible Judge Participation with current Access;
- Panel-composition conditions satisfied or explicitly governed exception present where Panel is used;
- no duplicate current initial responsibility for the same evaluator/subject/basis/occurrence meaning.

Postconditions:

- occurrence Open with actual starting evaluator set;
- each responsible starting evaluator has one Outstanding Evaluation Obligation;
- no Scorecard exists merely because the occurrence began.

# Why begin is the establishment point

MUDAC rejects:

- Panel membership → obligation: too early;
- Prepared occurrence → obligation: too early;
- Scorecard start → obligation: too late.

Occurrence begin is the first point where actual participation and current responsibility can be established truthfully together while remaining independent meanings.

# Panel membership and occurrence history remain separate

After begin, Panel membership/capacity changes affect reusable grouping/future planning only.

They do not automatically modify occurrence participants, establish/excuse/reassign obligations, or rewrite presented context.

A deliberate operational decision may coordinate both Panel and occurrence actions, but neither implies the other.

# Participant adjustment requires explicit responsibility disposition

`EvaluationOccurrence.recordParticipantAdjustment` records actual participation change. Responsibility disposition is separate.

## Participant leaves but still owes evaluation

- record occurrence adjustment;
- leave obligation Outstanding.

## Recusal/release with no replacement

- record occurrence adjustment;
- `EvaluationObligation.excuse` with legitimate authority/reason.

## True substitution

- record outgoing/incoming occurrence adjustment;
- `EvaluationObligation.reassignWithSuccessor` preserves predecessor responsibility and creates successor responsibility.

`Panel.replaceMember` participates only when reusable Panel membership should also change.

## Late addition

If policy permits late entry and the evaluator legitimately receives enough presentation/context to produce qualifying independent judgment:

- record participant adjustment;
- establish a new Outstanding obligation.

If taking over an existing responsibility, use successor/reassignment semantics rather than an unrelated obligation.

If authoritative evidence already exists, participant editing cannot remove it. Use [Temporal Truth, Correction & Historical Authority](temporal-truth-correction.md) for correction/invalidation.

# Complete Evaluation Occurrence

Application action: **Complete Evaluation Occurrence** using `EvaluationOccurrence.completeOccurrence`.

Completion records that the bounded occurrence ended. It does not wait for or modify obligation state.

Valid state:

```text
Occurrence  = Complete
Obligation A = Satisfied
Obligation B = Outstanding
Obligation C = Outstanding
```

Occurrence completion does not invoke `satisfy`, `excuse`, `cancel`, Scorecard finalization or derived outcome actions.

# Prepared cancellation versus later invalidation

A Prepared occurrence that never meaningfully begins may use `EvaluationOccurrence.cancel`. Because ordinary initial obligations do not exist before begin, simple Prepared cancellation has no obligation cleanup consequence.

Once an occurrence has begun, later unusability is not represented as pre-begin cancellation. Current invalidation/replacement/responsibility consequences are defined by [Temporal Truth, Correction & Historical Authority](temporal-truth-correction.md): an invalidated occurrence remains historical; dependent evidence is not erased; Outstanding responsibilities tied to invalid context are explicitly ended; and legitimate re-evaluation uses a distinct replacement occurrence plus deliberate successor/new obligations.

# Current action-surface classification

| Concept action family | Current MUDAC status |
| --- | --- |
| Team ordinary create/update | direct |
| Team withdraw/restore | direct/high-consequence; temporal effects use current correction composition |
| Division define/update/assign | direct |
| Division retire/correctAssignment | direct/high-consequence; temporal/outcome effects use 011-F/G |
| Alias assign | direct |
| Alias replace/retire | direct/high-consequence; temporal effects use 011-F |
| Panel membership/capacity planning | direct; no automatic occurrence/obligation effect |
| Evaluation Occurrence `prepare` | coordinated application action |
| Evaluation Occurrence `begin` | coordinated; establishes initial obligations |
| participant adjustment | coordinated; explicit responsibility disposition required |
| `completeOccurrence` | direct one-action application behavior |
| Prepared `cancel` | direct |
| occurrence `invalidate` | high-consequence coordinated action under temporal correction owner |
| `linkReplacement` | composition-only within replacement action |
| Evaluation Obligation `establish` | composition-only |
| `excuse` / `reassignWithSuccessor` | coordinated exceptional actions |
| `satisfy` | composition-only through Scorecard Finalization |
| `cancel` after invalid occurrence | coordinated temporal consequence |
| `requireSuccessorEvaluation` | controlled composition-only temporal consequence; never automatic |

# Composition invariants

1. Current Team/Division/Alias state does not rewrite historical presented occurrence context.
2. Panel membership does not itself create occurrence participation or responsibility.
3. Only actual confirmed starting evaluators enter the starting set.
4. Ordinary initial obligations arise at occurrence begin.
5. No placeholder judgment is created from responsibility.
6. Participant adjustment does not implicitly decide responsibility state.
7. Panel changes do not rewrite begun occurrence history.
8. Occurrence completion is independent from obligation completion.
9. Missing/excused responsibility never becomes zero/fabricated evidence.
10. Participant editing cannot erase authoritative evidence.
11. Occurrence invalidation preserves authored evidence/history while current eligibility may change.
12. Terminal obligations never reopen; re-evaluation uses successor responsibility.
13. Organizer coordination never transfers Judge authorship.

# Chaining summary

```text
current competitor context
  → EvaluationOccurrence.prepare
```

```text
Panel candidates + Participation + Access + operating facts/policy
  → confirmed starting evaluators
  → EvaluationOccurrence.begin
  + EvaluationObligation.establish × N
```

```text
participant adjustment
  → occurrence history
  + explicit responsibility disposition
```

```text
completeOccurrence
  → occurrence ends
  → obligations continue independently
```

```text
later unusable occurrence
  → current temporal-correction owner
  → invalidation / explicit responsibility disposition / optional distinct replacement
```

These are conceptual relationships, not runtime orchestration designs.

# Remaining downstream composition

- Coverage/Aggregate/Rank/Award/Finalization/Outcome Declaration → 011-G;
- Export/Publication → [External Representation, Currency & Publication Release Composition](external-representation-publication-release.md);
- application-wide chaining/automation/over-under/synergy → [Application Action Surface, Chaining & Automation Composition](application-action-surface-composition.md);
- product-family inclusion dependence → [Dependence](../dependence/);
- user-visible mapping → [Experience](../experience/).

---
type: Experience Contract
title: Judge Active Evaluation Mapping
description: Current active-evaluation mapping for Evaluation Occurrence context, Evaluation Obligation responsibility, one logical Scorecard Draft, explicit Finalization, action availability, independence and truthful feedback.
status: stable
tags: [experience, mapping, judge, evaluation-occurrence, evaluation-obligation, scorecard, finalization, phase-013]
sources:
  - resource: ../../013-concept-mapping-interaction-semantics-user-visible-representation/013-E-evaluation-occurrence-obligation-judgment-action-availability-feedback-mapping.md
  - resource: ../concepts/evaluation-occurrence.md
  - resource: ../concepts/evaluation-obligation.md
  - resource: ../concepts/scorecard.md
  - resource: ../concepts/rubric.md
  - resource: ../synchronizations/evaluation-occurrence-obligation.md
  - resource: ../synchronizations/evaluation-basis-scorecard-authority.md
  - resource: ../invariants/judge-independence.md
  - resource: ../invariants/one-logical-scorecard.md
  - resource: ../invariants/organizer-not-judge-author.md
  - resource: ../invariants/truthful-authority-under-uncertainty.md
---

# Purpose

Define the current user-visible semantics for ordinary Judge evaluation from established responsibility through one non-authoritative Scorecard Draft and explicit authoritative Finalization.

This owner does not own amendment/correction/history after Finalization. Those semantics are mapped separately by Phase 013-F.

# Active evaluation semantic chain

```text
Evaluation Occurrence begins
  → confirmed actual evaluators
  → Evaluation Obligation established
  → Judge may Start Evaluation
  → one logical Scorecard Draft
  → Judge explicitly Finalizes
  → authoritative Scorecard established
  → Evaluation Obligation Satisfied
```

Do not collapse this chain into a generic `Encounter`, `Assignment`, `Session`, or `Score` state.

# Occurrence context is not responsibility

Evaluation Occurrence answers what evaluation event actually occurred: subject, Judge-facing presented context, exact basis, actual participant history, timing and occurrence state.

Panel membership is only planned grouping and does not prove occurrence participation.

Occurrence participation does not itself prove that the Judge has an outstanding Evaluation Obligation unless the current composition established one.

Occurrence completion means the event ended. It does not mean all Judge work is complete or Finalized.

# Responsibility is Evaluation Obligation

Judge work is grounded in an Evaluation Obligation rather than Panel membership or a generic assignment flag.

Ordinary active work distinguishes:

```text
Outstanding
Satisfied
Excused
Cancelled
```

Before Scorecard start:

```text
Evaluation Obligation = Outstanding
Scorecard = absent
```

The experience may describe that as `Not started`, but `Not started` is not a Scorecard lifecycle state.

Missing work remains missing/outstanding rather than zero-valued evidence or a fabricated Scorecard.

# Judge work context

Before consequential Judge action, enough stable context must be intelligible to avoid evaluating the wrong subject or basis.

Where relevant the Judge must be able to understand:

- current Competition/Judge Participation context;
- Judge-safe subject identity, normally Alias + Division during blinded judging;
- relevant Evaluation Occurrence/work context;
- that the current Judge owns the applicable Outstanding obligation;
- the exact bound Evaluation Basis/Rubric context;
- whether current Access permits the intended operation;
- whether work is Not Started, Draft or already Finalized/Satisfied.

This is a semantic obligation, not a prescribed layout.

# Exact Evaluation Basis

The Judge evaluates against the exact authoritative Rubric Version bound through the Evaluation Occurrence and Evaluation Obligation.

```text
current working/latest Rubric
  != exact bound Evaluation Basis
```

A later Rubric successor does not silently rebind an existing occurrence, obligation or Scorecard Draft.

The active experience must provide the criterion definitions, response domains, instructions/guidance and Note requirements belonging to the bound basis.

# Start Evaluation

`Start Evaluation` is available when the Judge has the applicable Outstanding obligation, the bound subject/context/basis is legitimate, and current Access permits Judge-authored work.

Successful start establishes or resumes the same logical Scorecard for that obligation.

```text
one Evaluation Obligation
  → at most one logical Scorecard
```

Repeated start/resume intent, reloads, device changes or recovery must not appear to create independent duplicate evaluations.

If the obligation is already terminal or the initial Scorecard has been authoritatively Finalized, ordinary Start Evaluation is unavailable.

# Scorecard Draft

A Scorecard Draft is working Judge judgment and is non-authoritative.

Preserve:

```text
Draft exists
  != Draft complete
  != Finalized
  != authoritative Scorecard Version
  != obligation Satisfied
```

Draft work may include criterion responses, criterion Notes, overall Notes and completeness/validation feedback supplied by the exact Rubric basis.

A complete Draft may be ready for review while still non-authoritative.

Leaving or deliberately deferring the Draft does not Finalize it, abandon the Evaluation Obligation, or fabricate missing evidence.

# Missing, zero and response semantics

Where the Rubric permits distinct values, the experience must preserve the difference among:

- unanswered/missing response;
- explicit zero response;
- not-applicable or other configured response meaning.

Clearing a response restores the appropriate missing state rather than silently writing zero.

# Judge Independence

During ordinary judging, a Judge may see their own evaluation work but not peer judgment or outcome signals that could anchor judgment.

Do not disclose ordinary-judging:

- peer Scorecards/Notes;
- Panel mean;
- Coverage;
- Aggregate;
- Rank;
- standings.

Finalizing one's own Scorecard does not by itself unlock those signals.

# Action availability

Action availability reflects semantic preconditions; the visual existence or absence of a control is not itself authority.

| Action | Ordinary availability meaning |
| --- | --- |
| Start Evaluation | applicable obligation Outstanding + legitimate bound context/basis + current Access |
| edit Draft responses/Notes | current Judge-authored Draft + current Access |
| review Draft | current Draft exists; representation may summarize completeness/validity |
| Finalize Evaluation | Draft complete/valid under exact basis + obligation Outstanding + explicit Judge intent + current Access/authority conditions |

When an action is unavailable, feedback should identify the source category when doing so does not leak protected information.

Relevant categories include:

```text
no Evaluation Obligation exists
obligation already Satisfied/Excused/Cancelled
occurrence has not begun / supplied context is not legitimate
current Competition/context does not permit work
current Access denies the action
bound Evaluation Basis is unavailable/ineligible
Draft is incomplete or invalid under the bound Rubric
current invalidation/correction condition blocks authority establishment
```

Avoid reducing semantically different conditions to one generic `disabled` or `unauthorized` message when the legitimate next action differs.

# Draft validation and review feedback

Draft feedback distinguishes:

```text
response recorded vs missing
valid vs invalid under bound Rubric
required Note missing vs optional Note absent
Draft complete/valid vs incomplete/invalid
working state preserved vs authoritative Finalization
```

A calculated total or subtotal, where represented, is working interpretation under the bound Rubric and not authoritative evidence by itself.

Review completion is not Finalization.

# Explicit Finalize Evaluation

Judge Finalization is an explicit semantic commitment.

The following do not Finalize an evaluation:

- presentation/occurrence ending;
- navigation away;
- all fields becoming complete;
- Draft persistence/autosave;
- inactivity;
- Organizer event control.

Successful Finalize Evaluation coordinates the Judge-owned Scorecard Finalization with authoritative Scorecard Version establishment, meaningful Provenance and Evaluation Obligation satisfaction.

The application should explain the domain result rather than expose generic Versioning or Provenance controls.

After confirmed success:

```text
Scorecard = authoritative finalized judgment
Evaluation Obligation = Satisfied
one logical evaluation weight = preserved
```

The ordinary initial Draft is no longer editable as if Finalization had not occurred.

# Truthful Finalization feedback

Feedback must distinguish:

```text
Draft preserved
Finalize in progress / authoritative result unknown
Finalize confirmed successful
Finalize rejected/failed with known reason
```

Uncertain authority must never be presented as confirmed success.

Retry/resume must converge on the same logical Scorecard/obligation rather than create a second independent submission.

Stale working state must not silently overwrite newer authoritative state.

The runtime mechanism for save/sync/offline recovery is deferred; cross-cutting degraded/status parity is re-audited in 013-J.

# Occurrence completion and unfinished work

A completed Evaluation Occurrence may coexist with an Outstanding obligation and absent or Draft Scorecard.

```text
Occurrence = Complete
Obligation = Outstanding
Scorecard  = absent or Draft
```

If current Access/policy still permits work, the Judge may continue/resume the same logical evaluation after occurrence completion.

Occurrence completion never auto-Finalizes Scorecards or auto-satisfies obligations.

# Organizer/support boundary

Organizer/support capability to coordinate or inspect process state does not make that actor the Judge semantic author.

Ordinary active evaluation must not expose an Organizer action that simply writes Judge responses or Finalizes the Judge's Scorecard as Organizer-authored judgment.

Paper/assisted capture, represented-authority capture and source-faithful correction are mapped in 013-F.

# Boundary with amendment/correction/history

This owner stops at confirmed initial Finalization.

After that point, later legitimate changes are not ordinary `Edit` or `Reopen` behavior.

Phase 013-F owns:

- Judge amendment;
- paper/assisted capture authority;
- source-faithful correction;
- invalidation and structural error;
- predecessor/successor authoritative states;
- replacement occurrence/evidence;
- successor evaluation responsibility;
- current versus historical authority presentation.

# Related mapping

Operating context/role isolation is owned by [Experience Context and Participation Modes](context-role-modes.md).

Judge entry/readiness is owned by [Judge Entry, Participation & Readiness Mapping](judge-onboarding.md).

Organizer preparation and occurrence/basis setup are owned by [Organizer Competition Preparation & Readiness Mapping](organizer-preparation.md).

See [One Logical Evaluation per Evaluation Obligation](../invariants/one-logical-scorecard.md), [Judge Independence](../invariants/judge-independence.md), and [Truthful Authority Under Uncertainty](../invariants/truthful-authority-under-uncertainty.md).
---
type: Synchronization Contract
title: Evaluation Basis, Scorecard Authority & Capture Composition
description: "Current MUDAC composition for authoritative Rubric Version establishment, one logical Scorecard per Evaluation Obligation, Scorecard Finalization/amendment, Versioning/Provenance participation, obligation satisfaction, and paper/electronic capture parity after Phase 011-E."
status: stable
tags: [synchronization, rubric, scorecard, versioning, provenance, evaluation-obligation, paper, authority, phase-011]
sources:
  - resource: ../../011-concept-composition-synchronization/011-E-evaluation-basis-scorecard-authority-versioning-provenance-paper-capture-composition.md
  - resource: ../concepts/rubric.md
  - resource: ../concepts/scorecard.md
  - resource: ../concepts/versioning.md
  - resource: ../concepts/provenance.md
  - resource: ../concepts/evaluation-obligation.md
  - resource: ../concepts/evaluation-occurrence.md
  - resource: ../mechanisms/criterion-notes.md
  - resource: ../policies/evaluation-policy.md
  - resource: ../policies/continuity-paper.md
  - resource: ../invariants/judge-independence.md
  - resource: ../invariants/one-logical-scorecard.md
  - resource: ../invariants/organizer-not-judge-author.md
  - resource: ../invariants/capture-channel-parity.md
  - resource: ../invariants/truthful-authority-under-uncertainty.md
  - resource: evaluation-occurrence-obligation.md
generated: { by: openai/gpt-5.6-sol, at: 2026-09-14T11:58:00-05:00 }
---

# Purpose

Define current MUDAC application composition by which an exact authoritative [Rubric](../concepts/rubric.md) Version becomes an Evaluation Basis and one [Evaluation Obligation](../concepts/evaluation-obligation.md) is satisfied by one logical Judge-authored [Scorecard](../concepts/scorecard.md), while [Versioning](../concepts/versioning.md) preserves authoritative snapshots, [Provenance](../concepts/provenance.md) preserves explanatory authority/source history, and paper/electronic capture remain semantically equivalent.

This document supersedes the current-authority meaning of:

- legacy synchronization 07;
- legacy synchronization 08's Scorecard/basis half, completing the 011-D replacement of that legacy rule;
- legacy synchronization 09's authority-establishment / Versioning / Provenance / obligation-satisfaction portion;
- legacy synchronization 10.

Invalidation/correction/successor-work remains 011-F. Coverage/Aggregate/Rank consequences remain 011-G.

# Authority boundary

- **Rubric** owns evaluation-instrument and response-interpretation semantics.
- **Versioning<Rubric>** owns immutable authoritative Rubric snapshots/currentness.
- **Evaluation Obligation** owns evaluator responsibility.
- **Scorecard** owns one evaluator's logical judgment, Draft/finalized/amendment semantics and semantic author identity.
- **Versioning<Scorecard>** owns immutable authoritative Scorecard snapshots/currentness.
- **Provenance** owns meaningful actor/represented-authority/source/reason/history explanation.
- **Access** permits operations under current context but does not transfer authorship.

Paper/electronic/assisted capture channels own none of these semantic meanings.

# Authoritative Rubric basis establishment

Application action: **Establish Authoritative Rubric Version**.

Participants:

- `Rubric.prepareForUse` when the working definition still needs to establish prepared/valid state;
- `Versioning.initializeLineage` + `commitInitialVersion`, or `commitSuccessor(expectedCurrent, snapshot)` for a later authoritative definition;
- `Provenance.record`.

Conditions include:

- Rubric definition is valid/coherent;
- legitimate configuration authority and current Access/context;
- lineage/applicability meaning is unambiguous;
- successor establishment is based on the actual expected current eligible Rubric Version.

Successful postconditions:

- one complete immutable authoritative Rubric snapshot exists as a Version;
- at most one Version is current eligible authority for the lineage;
- meaningful Provenance explains the establishment;
- historical occurrences/obligations/Scorecards remain bound to the exact Version they already used.

`Rubric.prepareForUse` by itself does not establish authoritative Versioning state.

# Evaluation Basis binding

For current MUDAC:

> **Evaluation Basis is the exact authoritative Rubric Version selected for the evaluation occurrence/responsibility.**

When an Evaluation Occurrence is prepared under [Competitor Context, Evaluation Occurrence & Obligation Composition](evaluation-occurrence-obligation.md), `BasisRef` resolves one exact authoritative Rubric Version.

The same basis is carried into each resulting Evaluation Obligation and Scorecard structural identity.

A later Rubric Version does not silently rebind existing occurrences, obligations, Scorecard Drafts or finalized judgments. Rubric-version invalidation consequences belong to 011-F.

# Start Evaluation → one logical Scorecard

Application action: **Start Evaluation**.

Participant:

- `Scorecard.start`.

Structural bindings are supplied from the already-established responsibility/context:

```text
Evaluator         = Evaluation Obligation Evaluator
Subject           = Evaluation Obligation Subject
OccurrenceContext = obligation OccurrenceRef / supplied occurrence context
EvaluationBasis   = obligation Basis / occurrence BasisRef
```

Conditions:

- obligation is Outstanding;
- current Access permits Judge-authored evaluation work;
- structural bindings are consistent;
- the bound basis remains legitimate for this responsibility;
- no distinct logical Scorecard already exists for the same obligation.

Repeated start/resume intent resolves the same logical Scorecard.

Occurrence completion does not itself prevent continuing an Outstanding responsibility; current Competition/Access policy still governs whether the Judge may act.

# Draft work remains non-authoritative

Scorecard Draft response/note edits do not:

- satisfy the Evaluation Obligation;
- establish authoritative Versions;
- create Provenance for every edit;
- contribute evaluation evidence downstream.

Rubric Version semantics validate response values and Finalization completeness.

# Finalize Evaluation

Application action: **Finalize Evaluation**.

Participants:

- `Scorecard.finalize`;
- Scorecard `Versioning.initializeLineage` + `commitInitialVersion`;
- `Provenance.record`;
- `EvaluationObligation.satisfy`.

Conditions include:

- Scorecard is the one logical evaluation for the intended Outstanding obligation;
- Evaluator, Subject, OccurrenceContext and EvaluationBasis match the established responsibility;
- required responses/Notes are complete and valid under the exact Rubric Version;
- Judge finalization intent is explicit through the applicable capture path;
- current Access/represented-authority path is legitimate;
- no authoritative initial Scorecard Version already exists;
- the obligation has not already been resolved through another legitimate terminal state;
- no invalidation/correction condition requires 011-F handling first.

Semantic success requires all of the following current truths:

1. Scorecard has authoritative finalized judgment state;
2. one immutable initial Scorecard Version is current eligible authority;
3. Provenance explains semantic author, actor/capture actor where different, source/channel and meaningful timing/reason;
4. Evaluation Obligation is Satisfied;
5. `EvidenceRef` identifies the **logical Scorecard identity**;
6. only one evaluation weight exists.

This is an authority-establishing conceptual synchronization, not a prescribed transaction or service boundary.

# Why obligation EvidenceRef points to the logical Scorecard

Evaluation responsibility is satisfied by one logical evaluation, while that evaluation may later have successor authoritative states.

Therefore MUDAC binds:

```text
EvaluationObligation.EvidenceRef = logical Scorecard identity
```

Versioning separately answers which immutable Scorecard Version is current eligible authority.

This preserves one-vote semantics across legitimate amendment without reopening responsibility.

# Judge amendment

`Scorecard.beginAmendment` creates non-authoritative amendment work while the predecessor authoritative state remains current.

Application action: **Finalize Judge Amendment**.

Participants:

- `Scorecard.finalizeAmendment`;
- `Versioning.commitSuccessor(expectedCurrent, snapshot)`;
- `Provenance.record`.

The already-Satisfied Evaluation Obligation remains Satisfied by the same logical Scorecard and does not call `satisfy` again.

Successful amendment:

- establishes one successor current authoritative Scorecard Version;
- preserves the predecessor as immutable historical authority;
- records Judge-authored amendment Provenance;
- preserves one logical evaluation weight.

Ordinary amendment cannot silently change Evaluator, Subject, OccurrenceContext or EvaluationBasis. Structural/capture correction and invalidation belong to 011-F.

# Versioning and Provenance are composition-only support actions

Versioning does not decide Rubric validity, Judge intent or correction legitimacy.

Provenance does not create judgment or Version authority; it explains meaningful origin/authority/source history.

Generic `Versioning.initializeLineage`, `commitInitialVersion`, `commitSuccessor`, `invalidateVersion`, and `Provenance.record` are not standalone MUDAC admin application actions. They participate through purpose-specific application actions.

`invalidateVersion` remains 011-F work.

# Paper / assisted capture

## Same logical Scorecard

Paper is a capture/source path for the same logical Scorecard, not a `PaperScorecard` Concept.

Capture channel does not change:

- Judge/evaluator identity;
- Team/Subject;
- Evaluation Occurrence/context;
- exact Rubric Version;
- response/note semantics;
- evaluation weight.

## Source identity and context

Before paper-origin authority can be established, MUDAC must unambiguously resolve:

- the intended Evaluation Obligation / Judge Participation;
- occurrence/context and Subject;
- exact Evaluation Basis;
- one identified physical source reference.

Machine-readable identifiers may help resolve references but create no semantic authority.

## Capture Paper Evaluation

Application action: **Capture Paper Evaluation**.

Organizer/capture actor transcribes the physical Judge source into the same logical Scorecard Draft.

Before verification/finalization:

- digital capture remains non-authoritative;
- obligation remains Outstanding;
- no authoritative Scorecard Version exists merely because transcription is complete;
- Judge remains evaluator/semantic author.

## Verify & Finalize Paper Evaluation

Application action: **Verify & Finalize Paper Evaluation**.

Conditions:

- source/context/author/basis are unambiguous;
- captured content was checked against the identified physical source;
- source is sufficiently legible to establish what the Judge recorded;
- the paper procedure/source provides unambiguous evidence that the Judge completed/committed the evaluation for authoritative use;
- Rubric validation succeeds;
- no other authoritative path already satisfied the logical responsibility;
- capture/verification actor has legitimate capability.

Successful paper Finalization establishes the same authority postconditions as electronic Finalization.

Provenance distinguishes:

```text
Actor                = Organizer / capture verifier
RepresentedAuthority = Judge / semantic evaluator
Source               = identified paper source
```

Occurrence/Judge-authorship time and later capture/verification time remain distinct where material.

Organizer capture authority cannot infer missing responses, ambiguous marks or Judge Finalization intent.

# Mixed paper/electronic traces

Electronic Draft + paper fallback for the same responsibility converge on one logical Scorecard.

They never create a second Scorecard, second obligation or second vote.

If no authoritative Scorecard exists yet, the legitimately verified source representing final Judge intent may establish the one authoritative Scorecard.

If authoritative evidence already exists and another source conflicts materially, ordinary capture does not silently supersede authority. That conflict enters 011-F correction/invalidation analysis.

Duplicate capture of the same physical source similarly converges rather than creating another evaluation.

# Authority uncertainty

MUDAC distinguishes Draft/captured state from confirmed Finalization/Satisfaction.

If the application cannot establish whether the authority-establishing postconditions hold, it must not claim Scorecard Finalized or Evaluation Obligation Satisfied.

Repeated semantic intent reconciles against current Scorecard, Versioning and obligation state before another authority effect can occur.

This is a conceptual truth/convergence requirement, not a runtime retry/idempotency design.

# Current action-surface classification

| Action family | Current MUDAC status |
| --- | --- |
| Rubric Draft/configuration actions | direct |
| Rubric validation / `prepareForUse` | direct preparation; non-authoritative alone |
| Establish Authoritative Rubric Version | coordinated authority-establishing application action |
| Versioning initial/successor commit actions | composition-only |
| Provenance `record` | composition-only |
| Scorecard `start` | direct Judge action, obligation-bound |
| Scorecard Draft edit actions | direct Judge actions |
| Scorecard `finalize` | coordinated authority-establishing application action |
| Evaluation Obligation `satisfy` | composition-only in initial Finalization |
| Scorecard begin/abandon amendment | controlled direct Judge actions |
| Scorecard `finalizeAmendment` | coordinated successor authority action |
| Capture Paper Evaluation | direct Organizer operational action producing non-authoritative Draft |
| Verify & Finalize Paper Evaluation | coordinated authority-establishing capture action; Judge remains author |
| post-authority transcription correction / Version invalidation | 011-F |

# Composition invariants

1. EvaluationBasis is one exact authoritative Rubric Version.
2. Later Rubric Version establishment never silently rebinds existing evaluation state.
3. One Evaluation Obligation maps to at most one logical Scorecard.
4. Draft completion is not authority.
5. Initial Finalization coherently establishes Scorecard authority, Version history, Provenance and obligation satisfaction.
6. Satisfied-obligation EvidenceRef identifies logical Scorecard identity; Versioning identifies current authoritative snapshot.
7. Amendment creates a successor Version of the same Scorecard, not another vote/responsibility.
8. Versioning does not transfer semantic authorship.
9. Provenance distinguishes actor, represented authority and source.
10. Organizer capture cannot manufacture Judge judgment or Finalization intent.
11. Paper/electronic paths preserve equivalent semantics and weight.
12. Mixed capture traces converge on one logical Scorecard.
13. Post-authority transcription mismatch is correction, not ordinary capture.
14. Uncertain authority cannot be represented as confirmed success.
15. Finalization does not unlock peer Scorecards or standings.

# Chaining summary

```text
valid prepared Rubric
  → authoritative Rubric Version + Provenance
  → exact Evaluation Basis
```

```text
Outstanding Evaluation Obligation
  → one logical Scorecard Draft
  → Finalize Evaluation
  → initial authoritative Scorecard Version + Provenance
  → obligation Satisfied by logical Scorecard
```

```text
Satisfied obligation / logical Scorecard
  → Judge amendment
  → successor Scorecard Version + Provenance
  → same obligation / one vote
```

```text
identified paper source
  → same logical Scorecard Draft
  → source verification + Judge commit intent
  → same Finalize Evaluation authority result
```

These are semantic compositions, not runtime orchestration designs.

# Deferred composition

- invalidation, correction, replacement, successor work and affected-state propagation → 011-F;
- Coverage/Aggregate/Rank/Award/Outcome Declaration consequences → 011-G;
- external representation/release → 011-H;
- whole-application action/chaining/automation audit → 011-I;
- physical/UI representation of paper Finalization intent, forms and assisted workflows → Phase 013.
---
type: Synchronization Contract
title: Evaluation Basis, Scorecard Authority & Capture Composition
description: "Current MUDAC composition for authoritative Rubric Version establishment, one logical Scorecard per Evaluation Obligation, Scorecard Finalization/amendment, Versioning/Provenance participation, obligation satisfaction, paper/electronic capture parity, and handoff into current temporal correction semantics."
status: stable
tags: [synchronization, rubric, scorecard, versioning, provenance, evaluation-obligation, paper, authority, phase-011]
sources:
  - resource: ../../011-concept-composition-synchronization/011-E-evaluation-basis-scorecard-authority-versioning-provenance-paper-capture-composition.md
  - resource: ../../011-concept-composition-synchronization/011-F-temporal-correction-invalidation-replacement-successor-work-affected-state-propagation.md
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
  - resource: temporal-truth-correction.md
generated: { by: openai/gpt-5.6-sol, at: 2026-09-14T13:36:00-05:00 }
---

# Purpose

Define current MUDAC application composition by which an exact authoritative [Rubric](../concepts/rubric.md) Version becomes an Evaluation Basis and one [Evaluation Obligation](../concepts/evaluation-obligation.md) is satisfied by one logical Judge-authored [Scorecard](../concepts/scorecard.md), while [Versioning](../concepts/versioning.md) preserves authoritative snapshots, [Provenance](../concepts/provenance.md) preserves explanatory authority/source history, and paper/electronic capture remain semantically equivalent.

This document supersedes legacy synchronization 07, legacy 08's Scorecard/basis half, legacy 09's authority-establishment/Versioning/Provenance/obligation-satisfaction portion, and legacy 10.

Current invalidation/correction/replacement/successor-work semantics are owned by [Temporal Truth, Correction & Historical Authority](temporal-truth-correction.md). Coverage/Aggregate/Rank consequences remain 011-G.

# Authority boundary

- **Rubric** owns evaluation-instrument and response-interpretation semantics.
- **Versioning<Rubric>** owns immutable authoritative Rubric snapshots/currentness.
- **Evaluation Obligation** owns evaluator responsibility.
- **Scorecard** owns one evaluator's logical judgment, Draft/finalized/successor-state semantics and semantic author identity.
- **Versioning<Scorecard>** owns immutable authoritative Scorecard snapshots/currentness.
- **Provenance** owns meaningful actor/represented-authority/source/reason/history explanation.
- **Access** permits operations under current context but does not transfer authorship.

Capture channels own none of these semantic meanings.

# Authoritative Rubric basis establishment

Application action: **Establish Authoritative Rubric Version**.

Participants:

- `Rubric.prepareForUse` when needed;
- `Versioning.initializeLineage` + `commitInitialVersion`, or `commitSuccessor(expectedCurrent, snapshot)`;
- `Provenance.record`.

Conditions include valid/coherent Rubric definition, legitimate configuration authority/current Access, unambiguous lineage/applicability, and correct expected-current predecessor for successor establishment.

Successful postconditions:

- one complete immutable authoritative Rubric snapshot exists;
- at most one Version is current eligible authority for the lineage;
- meaningful Provenance explains establishment;
- historical occurrences/obligations/Scorecards remain bound to exact earlier Versions already used.

`Rubric.prepareForUse` alone does not establish authoritative Versioning state.

# Evaluation Basis binding

For current MUDAC:

> **Evaluation Basis is the exact authoritative Rubric Version selected for the evaluation occurrence/responsibility.**

When an Evaluation Occurrence is prepared, `BasisRef` resolves one exact authoritative Rubric Version. The same basis flows into each resulting Evaluation Obligation and Scorecard structural identity.

A later Rubric Version never silently rebinds existing occurrences, obligations, Scorecard Drafts or finalized judgments. Supersession versus invalidation consequences are defined by [Temporal Truth, Correction & Historical Authority](temporal-truth-correction.md).

# Start Evaluation → one logical Scorecard

Application action: **Start Evaluation** using `Scorecard.start`.

Bindings:

```text
Evaluator         = Evaluation Obligation Evaluator
Subject           = Evaluation Obligation Subject
OccurrenceContext = obligation OccurrenceRef / supplied occurrence context
EvaluationBasis   = obligation Basis / occurrence BasisRef
```

Conditions:

- obligation Outstanding;
- current Access permits Judge-authored work;
- structural bindings consistent;
- bound basis legitimate;
- no distinct logical Scorecard already exists for that obligation.

Repeated start/resume intent resolves the same logical Scorecard.

Occurrence completion alone does not prevent continued work on an Outstanding responsibility; current Competition/Access policy controls capability.

# Draft work remains non-authoritative

Draft response/note edits do not satisfy the obligation, establish authoritative Versions, create Provenance for each edit, or contribute downstream evidence.

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
- structural identity matches responsibility;
- required responses/Notes valid under exact Rubric Version;
- Judge finalization intent explicit through applicable capture path;
- current Access/represented-authority path legitimate;
- no authoritative initial Scorecard Version already exists;
- obligation not already terminal through another legitimate path;
- no current invalidation/correction condition blocks authority establishment.

Semantic success requires:

1. authoritative finalized Scorecard state;
2. one immutable initial current eligible Scorecard Version;
3. meaningful Provenance explaining semantic author, actor/capture actor, source/channel and meaningful timing/reason;
4. Evaluation Obligation Satisfied;
5. `EvidenceRef` = logical Scorecard identity;
6. one evaluation weight only.

# Why EvidenceRef points to logical Scorecard

Responsibility is satisfied by one logical evaluation, while that evaluation may later have successor authoritative states.

```text
EvaluationObligation.EvidenceRef = logical Scorecard identity
```

Versioning separately identifies the current eligible authoritative Scorecard Version.

This preserves one-vote semantics across legitimate successor corrections.

# Judge semantic amendment

`Scorecard.beginAmendment` creates non-authoritative successor work while predecessor authority remains current.

Application action: **Finalize Judge Amendment**.

Participants:

- `Scorecard.finalizeAmendment`;
- `Versioning.commitSuccessor(expectedCurrent, snapshot)`;
- `Provenance.record`.

The Satisfied obligation remains Satisfied by the same logical Scorecard and is not satisfied again.

Successful amendment establishes one successor current Scorecard Version, preserves predecessor history, records Judge-authored amendment Provenance, and preserves one evaluation weight.

Structural identity cannot change. Source-faithful post-authority capture correction and invalidation use the current temporal-correction owner rather than being mislabeled as Judge semantic amendment.

# Versioning and Provenance remain composition-only

Versioning does not decide Rubric validity, Judge intent or correction legitimacy.

Provenance does not create judgment or Version authority; it explains meaningful origin/authority/source history.

Generic Versioning commit/invalidation actions and `Provenance.record` are not standalone MUDAC administrative controls. Purpose-specific application actions invoke them.

# Paper / assisted capture

Paper is a capture/source path for the same logical Scorecard, not a separate Concept.

Capture channel does not change Judge/evaluator identity, Team/Subject, Evaluation Occurrence/context, exact Rubric Version, response semantics or evaluation weight.

Before paper-origin authority can be established, MUDAC must resolve the intended Evaluation Obligation/Judge Participation, occurrence/context/Subject, exact Evaluation Basis and one identified physical source.

## Capture Paper Evaluation

Organizer/capture actor transcribes the physical Judge source into the same logical Scorecard Draft.

Before verification/finalization:

- digital capture remains non-authoritative;
- obligation remains Outstanding;
- no authoritative Scorecard Version exists from transcription alone;
- Judge remains evaluator/semantic author.

## Verify & Finalize Paper Evaluation

Conditions include unambiguous source/context/author/basis, checked transcription, sufficient legibility, unambiguous Judge completed/committed intent, Rubric validation, no competing authoritative path, and legitimate capture/verification capability.

Successful paper Finalization establishes the same authority postconditions as electronic Finalization.

Provenance distinguishes:

```text
Actor                = Organizer / capture verifier
RepresentedAuthority = Judge / semantic evaluator
Source               = identified paper source
```

Organizer capture authority cannot infer missing responses, ambiguous marks or Judge finalization intent.

# Mixed paper/electronic traces

Electronic Draft + paper fallback for the same responsibility converge on one logical Scorecard and never create a second Scorecard, obligation or vote.

If no authoritative Scorecard exists, legitimately verified final Judge intent may establish the one authority path.

If authority already exists and another source conflicts materially, ordinary capture does not silently supersede it. Current correction/invalidation handling is [Temporal Truth, Correction & Historical Authority](temporal-truth-correction.md).

# Authority uncertainty

Captured/Draft state remains distinct from confirmed Finalization/Satisfaction. Unknown authority outcome must never be reported as confirmed success.

Repeated semantic intent reconciles against current Scorecard, Versioning and obligation state before another authority effect can occur. This is conceptual convergence, not runtime retry design.

# Current action-surface classification

| Action family | Current MUDAC status |
| --- | --- |
| Rubric Draft/configuration | direct |
| Rubric validation / `prepareForUse` | direct preparation; non-authoritative alone |
| Establish Authoritative Rubric Version | coordinated authority-establishing action |
| Versioning initial/successor commit | composition-only |
| Provenance `record` | composition-only |
| Scorecard `start` | direct Judge action, obligation-bound |
| Scorecard Draft edits | direct Judge actions |
| Scorecard `finalize` | coordinated authority-establishing action |
| Evaluation Obligation `satisfy` | composition-only in initial Finalization |
| begin/abandon amendment | controlled direct Judge actions |
| Judge `finalizeAmendment` | coordinated successor authority action |
| Capture Paper Evaluation | direct Organizer operational action producing non-authoritative Draft |
| Verify & Finalize Paper Evaluation | coordinated authority-establishing capture action; Judge remains author |
| post-authority capture correction / Version invalidation | current temporal-correction owner |

# Composition invariants

1. EvaluationBasis is one exact authoritative Rubric Version.
2. Later Rubric Version establishment never silently rebinds existing evaluation state.
3. One Evaluation Obligation maps to at most one logical Scorecard.
4. Draft completion is not authority.
5. Initial Finalization coherently establishes Scorecard authority, Version history, Provenance and obligation satisfaction.
6. Satisfied-obligation EvidenceRef identifies logical Scorecard identity; Versioning identifies current authoritative snapshot.
7. Successor Scorecard state does not add evaluation weight.
8. Versioning never transfers semantic authorship.
9. Provenance distinguishes actor, represented authority and source.
10. Organizer capture cannot manufacture Judge judgment or commit intent.
11. Paper/electronic paths preserve equivalent semantics and weight.
12. Mixed traces converge on one logical Scorecard.
13. Post-authority transcription mismatch is correction, not ordinary capture.
14. Structural Scorecard identity is never silently rebound.
15. Uncertain authority cannot be represented as success.
16. Finalization does not unlock peer Scorecards/standings.

# Remaining downstream composition

- current temporal correction/invalidation/replacement/successor semantics → [Temporal Truth, Correction & Historical Authority](temporal-truth-correction.md);
- Coverage/Aggregate/Rank/Award/Outcome Declaration → 011-G;
- external representation/release → 011-H;
- whole-application action/chaining/automation audit → 011-I;
- physical/UI representation of capture/finalization/correction intent → Phase 013.

---
type: Experience Contract
title: Authority Lineage, Capture & Correction Mapping
description: Current user-visible mapping for paper/assisted capture, Judge amendment, source-faithful correction, invalidation, replacement, successor responsibility, Provenance and current-versus-historical authority.
status: stable
tags: [experience, mapping, authority, lineage, paper, amendment, correction, invalidation, replacement, history, phase-013]
sources:
  - resource: ../../013-concept-mapping-interaction-semantics-user-visible-representation/013-F-authority-lineage-paper-capture-amendment-correction-historical-state-mapping.md
  - resource: ../concepts/scorecard.md
  - resource: ../concepts/evaluation-occurrence.md
  - resource: ../concepts/evaluation-obligation.md
  - resource: ../concepts/versioning.md
  - resource: ../concepts/provenance.md
  - resource: ../synchronizations/evaluation-basis-scorecard-authority.md
  - resource: ../synchronizations/temporal-truth-correction.md
  - resource: ../policies/correction-authority.md
  - resource: ../policies/continuity-paper.md
  - resource: ../invariants/current-vs-historical-truth.md
  - resource: ../invariants/capture-channel-parity.md
  - resource: ../invariants/one-logical-scorecard.md
  - resource: ../invariants/organizer-not-judge-author.md
---

# Purpose

Define how MUDAC represents authoritative evaluation history and legitimate change without silently rewriting finalized judgment, transferring Judge authorship, reopening terminal responsibility, or collapsing supersession, invalidation and replacement.

# Authority-change classification

Correction begins with the semantic owner that is actually wrong.

```text
Judge changes judgment
  → Judge semantic amendment

recorded representation differs from unchanged source
  → source-faithful capture/transcription correction

Evaluator / Subject / OccurrenceContext / EvaluationBasis is wrong
  → structural invalidation / distinct correctly bound evidence if provable

occurrence itself is unusable
  → occurrence invalidation + optional distinct replacement occurrence

terminal historical responsibility must genuinely occur again
  → successor Evaluation Obligation + new logical Scorecard

recorded historical assertion is wrong
  → corrected historical assertion + separate owner-specific consequence if required
```

Do not represent these as interchangeable `Edit`, `Reopen`, `Fix`, or `Undo` operations.

# Temporal vocabulary

Preserve the following meanings:

```text
Draft
  = non-authoritative working state

Current authoritative Version
  = currently eligible committed authority for a logical lineage

Superseded Version
  = retained predecessor after an explicit successor became current

Invalidated Version
  = retained committed state no longer eligible for the authoritative purpose

Replacement
  = a distinct logical subject/occurrence standing in place of another

Affected / Stale
  = owner-specific dependency-currentness meaning
```

Therefore:

```text
superseded != invalidated != replaced != affected != stale
```

# Current and historical truth

Where correction changes the best-known/current state, the experience must preserve three distinct questions when relevant:

```text
What is current now?
What was considered authoritative at the earlier time?
What does MUDAC now believe actually happened at that earlier time after later evidence/correction?
```

History is attributable. Current correction does not erase what was previously recorded, authored, relied upon, declared or released.

# Paper and assisted capture

Paper/electronic/assisted capture are channels for the same evaluation semantics.

They preserve the same:

- Judge/evaluator;
- Team/subject;
- Evaluation Occurrence/context;
- Evaluation Obligation;
- exact Evaluation Basis;
- criterion/note semantics;
- logical Scorecard;
- Judge semantic authorship;
- evaluation weight.

A paper-origin path is:

```text
identified physical Judge source
  → capture/transcription Draft
  → source verification
  → authoritative paper-origin Scorecard Version
```

Before verification, transcription remains non-authoritative.

The physical/external source must be identifiable enough to explain what evidence supports the capture.

# Actor and represented authority

Capture/verification may legitimately distinguish:

```text
Actor                = Organizer / capture / verification actor
RepresentedAuthority = Judge
Semantic author      = Judge
Source               = identified physical/external source
```

The capture actor is never presented as the Judge author merely because they entered or verified the data.

Ambiguous Judge intent remains ambiguous. An Organizer/support actor cannot infer missing judgment or Finalization intent.

# Judge semantic amendment

A legitimate post-Finalization change in the Judge's own judgment uses a successor amendment path:

```text
current authoritative Scorecard Version
  → Begin Amendment
  → non-authoritative amendment Draft
  → explicit Finalize Amendment
  → successor authoritative Scorecard Version
```

While the amendment Draft exists, the predecessor remains current authority.

After confirmed successor Finalization:

- successor is current authority for the same logical Scorecard;
- predecessor remains Superseded historical authority;
- Judge remains semantic author;
- original Evaluation Obligation remains Satisfied by the same logical Scorecard;
- no additional evaluation weight is created.

Abandoning amendment work leaves predecessor authority unchanged.

# Source-faithful capture correction

A demonstrated mismatch between authoritative digital content and an identified unchanged source may be corrected when structural Scorecard identity remains correct.

```text
current authoritative Scorecard Version
  + verified capture mismatch
  → Correct Authoritative Capture
  → successor authoritative Scorecard Version
```

This preserves:

```text
same logical Scorecard
same Judge semantic author
same Evaluation Obligation
same evaluation weight
```

The correction Actor may differ from the Judge, and Provenance must retain that distinction.

Capture correction changes recorded representation to match source. It is not a Judge amendment.

# Amendment versus capture correction

| Meaning | Judge amendment | Capture correction |
| --- | --- | --- |
| Judge judgment changed | yes | no |
| semantic author | Judge | Judge |
| successor source | Judge's new intent | verified unchanged source |
| Organizer may act as correction actor | not as semantic author | yes, under capture-correction authority |
| logical Scorecard changes | no | no |
| obligation satisfied again | no | no |
| extra evaluation weight | no | no |

If the classification is uncertain, the experience must not silently choose one simply to make an edit possible.

# Structural Scorecard identity

Evaluator, Subject, OccurrenceContext and EvaluationBasis are structural identity and cannot be changed through ordinary amendment or capture correction.

When structural identity is wrong:

1. preserve the incorrect record/history;
2. invalidate the unusable current Version where warranted;
3. do not silently rebind the logical Scorecard;
4. establish distinct correctly bound evidence only when reliable source evidence proves correct binding and Judge-authored content without inference;
5. otherwise leave evidence ineligible and let policy determine whether new evaluation work is required.

# Supersession and invalidation

Supersession means a legitimate successor in the same logical lineage became current. The predecessor remains historical authority.

Invalidation means retained committed state is no longer eligible.

After invalidation:

- history remains inspectable under appropriate Access;
- an older predecessor does not silently revive;
- the lineage may have no current eligible Version;
- historical Evaluation Obligation satisfaction remains separate from current evidence eligibility;
- replacement/successor work is not implied automatically.

# Evaluation Occurrence invalidation

An invalidated Evaluation Occurrence happened but is no longer eligible for its intended evaluative use.

Preserve, as appropriate:

- occurrence identity;
- presented context;
- actual participant history;
- timing;
- Judge-authored Scorecards;
- obligation history;
- invalidation reason/authority;
- replacement relation if later established.

Invalidation is not cancellation and does not erase authentic Judge-authored evidence merely because that evidence becomes ineligible for current aggregation.

# Replacement occurrence

Re-evaluation uses a distinct replacement occurrence.

```text
Occurrence A = Invalidated
Occurrence B = distinct replacement occurrence
```

Replacement does not automatically copy participants, Panel membership, obligations, Scorecards, Access, presented context or Evaluation Basis.

The replacement is new historical truth rather than mutation of the predecessor.

# Responsibility after invalidation

An Outstanding obligation tied to invalid context cannot remain satisfiable against that invalid context. The predecessor responsibility is explicitly ended as appropriate.

A historically Satisfied obligation remains Satisfied even if its linked evidence later becomes ineligible.

```text
historical obligation satisfaction
  != current evidence eligibility
```

If another evaluation is legitimately required after a terminal predecessor, create a successor Evaluation Obligation. Do not reopen the predecessor.

The successor uses a new logical Scorecard.

Successor work is a governed decision and never an automatic side effect of evidence invalidation.

# Corrected historical assertions

Current Team/Division/Alias/Panel state never silently rewrites a past occurrence.

If later evidence proves the recorded historical assertion itself was inaccurate, preserve:

```text
as-recorded / as-known assertion
corrected best-known historical assertion
```

Provenance explains the correction.

If the corrected historical fact changes eligibility/validity, the natural domain owner must perform that separate transition. Provenance correction alone does not alter business validity.

# Provenance presentation

Provenance should be inspectable where needed to explain meaningful authority transitions, including:

- Actor;
- RepresentedAuthority / semantic author;
- source/capture channel/reference;
- reason/classification;
- predecessor and resulting authority references;
- occurrence/effective time versus later capture/correction time where materially different.

Generic Provenance/Versioning administration is not a user-facing application surface.

Do not expose generic `Record Provenance`, `Commit Version`, or `Invalidate Version` controls.

# High-consequence action understanding

Before a consequential authority action commits, the actor must be able to understand the material consequence without requiring a particular dialog/control implementation.

## Finalize Judge Amendment

Make clear:

- which current authority is being succeeded;
- the material amendment content;
- predecessor history remains;
- same logical Scorecard/one evaluation weight remains.

## Correct Authoritative Capture

Make clear:

- identified source;
- demonstrated mismatch;
- represented Judge authority;
- Judge semantic intent is not being changed;
- structural identity cannot be changed through this action.

## Invalidate evidence/occurrence

Make clear:

- exact target;
- reason/evidence basis;
- loss of current eligibility;
- history retained;
- no older predecessor automatically revives;
- no replacement or successor responsibility is automatically created.

# Feedback after authority change

Feedback must distinguish working/uncertain state from confirmed transitions.

Useful semantic categories include:

```text
amendment Draft started
amendment successor confirmed
capture correction under review
capture correction confirmed
Version invalidation confirmed
occurrence invalidation confirmed
replacement occurrence linked
successor responsibility established
corrected historical assertion recorded
authoritative result unknown / requires re-resolution
```

An uncertain high-consequence result must never be represented as confirmed success.

# Organizer/support boundary

Organizer/support capability may coordinate, capture, verify, invalidate or correct only within explicitly granted semantic authority.

It cannot:

- invent Judge judgment;
- infer ambiguous paper intent;
- use capture correction to change Judge semantic content;
- use technical privilege to manufacture domain correction authority;
- silently alter Scorecard structural identity;
- create successor responsibility without governing authority.

# Boundary with active evaluation

[Judge Active Evaluation Mapping](judge-evaluation.md) owns ordinary initial judging through confirmed initial Finalization.

After initial authority exists, a later change must use the amendment/correction/invalidation/replacement/successor semantics in this owner rather than generic `Edit` or `Reopen` behavior.

# Boundary with outcomes and externalization

This owner establishes evaluation-source authority/history and the beginning of affectedness.

It does not own the downstream representation of Coverage/Aggregate/Rank/reconciliation, Award/official outcome authority, or Export/Publication currentness/release. Those are mapped by later Phase-013 workstreams.

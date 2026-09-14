---
type: Design Policy
title: Awards and Finalization Policy
description: Governing rules for Award readiness/conferral, Competition Finalization, explicit Outcome Declaration authority and post-finalization correction without conflating calculated, official or public state.
status: stable
tags: [policy, awards, finalization, outcome-declaration, phase-011]
sources:
  - resource: ../../002-concept-specification/002-G-awards-reconciliation-finalization-official-outcomes.md
  - resource: ../../010-project-purpose-candidate-specification-modularity/010-H-concept-boundary-convergence-respecification-canonical-reconciliation.md
  - resource: ../../011-concept-composition-synchronization/011-G-coverage-aggregate-rank-award-competition-finalization-outcome-declaration-composition.md
  - resource: ../synchronizations/evaluation-outcome-finalization-declaration.md
generated: { by: openai/gpt-5.6-sol, at: 2026-09-14T13:55:00-05:00 }
---

# Canonical contract

## Awards

Rank-derived Awards consume a **current supplied Rank SelectionBasis** and may be conferred only when the recipient is consistent with the declared Award rule, scope, tie/cardinality semantics and eligibility requirements.

Rank does not own Award conferral. A recalculated Rank that produces a different candidate never silently moves an existing Award.

Discretionary Awards are authorized human decisions and must not be portrayed as mathematically implied unless their definition actually says so.

Source/Rank correction may require Award review, revocation or corrected conferral, but Award authority changes only through explicit Award actions.

## Factual Coverage and exceptions

Competition closeout must preserve both:

```text
Coverage factual sufficiency
and
any governed exception disposition
```

An accepted exception can permit a downstream consequence while Coverage remains factually `Incomplete`. It never fabricates evidence or rewrites `Incomplete` to `Satisfied`.

## Closeout basis

Ordinary MUDAC closeout requires a reconstructible current basis including, as applicable:

- Competition in `Event Completed`;
- applicable Evaluation Policy/evaluation basis;
- current factual Coverage plus any attributable exception dispositions;
- current Aggregate/Rank basis for required ranked outcomes;
- required tie resolution/policy result;
- required/current Award decisions;
- no unresolved correction/reconciliation condition that policy treats as blocking;
- exact accepted outcome basis intended for declaration.

## Coordinated Finalization and Outcome Declaration

Current MUDAC ordinary official closeout is the coordinated application action defined by [Evaluation Outcome, Award, Finalization & Declaration Composition](../synchronizations/evaluation-outcome-finalization-declaration.md):

```text
Competition.finalize
+
OutcomeDeclaration.declare
```

Semantic closeout success requires both:

```text
Competition = Finalized
AND
one explicit current Outcome Declaration exists over the accepted basis
```

This does not merge ownership:

- Competition owns lifecycle closure;
- Outcome Declaration owns declared official-result content/currentness/history.

A calculated/ranking-ready result is not official merely by existing.

## Official is not public

Outcome Declaration does not publish results. Export and Publication remain separate authority and are composed in 011-H.

## Post-Finalization correction

A legitimate post-Finalization source correction:

- leaves Competition `Finalized`;
- causes affected Coverage/Aggregate/Rank to be re-derived as appropriate;
- may require explicit Award review/correction;
- makes the current Outcome Declaration `Affected` when its immutable basis materially depends on the corrected source;
- does not silently establish a new official outcome.

An Affected declaration remains the latest declared official authority until an authorized actor explicitly confirms a successor under `OutcomeDeclaration.confirmSuccessor`.

The predecessor then becomes Superseded historical authority and remains reconstructible.

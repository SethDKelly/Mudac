---
type: Experience Contract
title: Reconciliation & Derived Outcome-State Mapping
description: Current mapping for source-directed reconciliation, current evidence eligibility, Coverage, Aggregate, rank eligibility, Rank, Ranking Readiness and Finalization Readiness without turning derived projections into editable authority.
status: stable
tags: [experience, mapping, reconciliation, coverage, aggregate, rank, readiness, phase-013]
sources:
  - resource: ../../013-concept-mapping-interaction-semantics-user-visible-representation/013-G-live-operations-remaining-work-exception-reconciliation-derived-outcome-state-mapping.md
  - resource: live-operations.md
  - resource: authority-lineage-correction.md
  - resource: ../mechanisms/coverage.md
  - resource: ../mechanisms/aggregate.md
  - resource: ../mechanisms/rank.md
  - resource: ../mechanisms/readiness.md
  - resource: ../mechanisms/reconciliation.md
  - resource: ../synchronizations/evaluation-outcome-finalization-declaration.md
  - resource: ../policies/evaluation-policy.md
  - resource: ../policies/operational-exception-governance.md
---

# Purpose

Define how MUDAC presents unresolved outcome-affecting conditions and derived outcome state before explicit Award/finalization/official-result authority is exercised.

This owner stops before Award conferral, Competition Finalization and Outcome Declaration authority; those semantics belong to 013-H.

# Reconciliation is source-directed work

Reconciliation is an Organizer work context/process, not a Concept, Competition lifecycle state or generic issue/ticket system.

A reconciliation representation may group unresolved conditions, but each condition remains owned by its natural source or governing policy.

Typical categories include:

- Outstanding Evaluation Obligations;
- paper/assisted capture not yet authoritative;
- uncertain Scorecard Finalization/capture state;
- Scorecard/Occurrence/basis invalidation or correction;
- successor responsibility deliberately established;
- Team/Division eligibility;
- Evaluation Basis/Rubric compatibility;
- Coverage shortfall;
- governed exception disposition;
- tie/policy conditions;
- required Award/closeout prerequisites that later phases map as authority actions.

A reconciliation item is not resolved by checking it off.

# Resolution semantics

A reconciliation condition becomes semantically resolved only when:

1. the authoritative source condition changes;
2. a specifically permitted governed exception changes the allowed consequence while preserving the source condition; or
3. another owner-defined semantic action establishes the required postcondition.

Acknowledging, dismissing, suppressing or hiding a presentation does not repair the source.

# Current eligible evidence

Derived outcome state consumes **current eligible authoritative evidence**, not merely all Scorecards that were once Finalized.

Preserve:

```text
historically Finalized Scorecard
  != currently eligible evidence

historically Satisfied Evaluation Obligation
  != current evidence eligibility
```

Current eligibility depends on the applicable current Version, structural binding, occurrence eligibility, exact Evaluation Basis eligibility and correction/invalidation state under current policy.

An authentic historical Scorecard may remain retained while being excluded from current outcome derivation.

# Ineligible evidence does not automatically create work

When historically satisfying evidence becomes ineligible:

```text
evidence ineligible
  → reconciliation / evidence-gap condition
  != predecessor obligation reopened
  != automatic successor obligation
```

New Judge work exists only when the proper authority explicitly establishes successor responsibility under 013-F semantics.

# Coverage

Coverage is derived factual sufficiency over qualifying current evidence and the applicable requirement basis.

Its factual state remains:

```text
Satisfied | Incomplete
```

Coverage should be explainable by the relevant requirement basis and observed qualifying evidence/shortfall.

Missing evidence remains missing. It is not zero and is not fabricated as present.

# Coverage exception disposition

A governed exception is separate from Coverage factual state.

The experience may legitimately show:

```text
Coverage = Incomplete
Exception = Accepted for ranking
```

or another specifically permitted consequence.

The exception must not relabel factual Coverage as `Satisfied`.

Exception scope matters: permission to proceed for one consequence does not silently authorize another.

# Aggregate

Aggregate is a numerical derivation over current eligible authoritative individual Judge Scorecards under Evaluation Policy.

Preserve:

```text
Aggregate exists
  != Coverage Satisfied
  != rank eligible
  != Ranking Ready
  != official outcome
```

A numeric Aggregate may exist while Coverage is Incomplete.

Missing evidence is excluded as missing rather than converted to zero.

Analytical Panel/occurrence means do not replace the declared individual-Scorecard weighting semantics.

# Rank eligibility

The application determines the supplied rank-eligible Team set from current evidence/eligibility facts, Coverage plus separately scoped exception dispositions, Division and policy conditions.

Rank does not determine its own eligibility.

The representation should make clear when a Team or result scope is excluded/not yet eligible without implying Rank itself owns that decision.

# Rank

Rank is a derived ordering under current Division scope and Evaluation Policy.

It is non-editable.

If an ordering is wrong, remediation targets the real source: evidence eligibility, Coverage/exception disposition, Division assignment, Aggregate input, policy, tie semantics or another governing basis.

Preserve:

```text
calculated Rank
  != Ranking Readiness
  != Award authority
  != official outcome authority
```

Hidden implementation ordering, display rounding or arbitrary tie-breaking must not appear to resolve a policy-level tie.

# Derived currentness

Coverage, Aggregate, Rank and readiness are basis-relative derived results.

When a material input changes:

```text
source changes
  → prior derivation becomes affected/non-current
  → recompute against current authoritative basis
  → new current derived result
```

Recomputation does not mutate the source.

Prior derivations may remain reconstructible when needed to explain historical decisions.

A stale result must not be displayed as current merely because a refresh has not happened or an Organizer has not acknowledged it.

# Ranking Readiness

Ranking Readiness asks whether the current result scope is fit for consequential rank-dependent use.

It is distinct from the existence of a calculated Rank.

Potential blocking categories include:

- unresolved Team/Division eligibility;
- evidence basis not reconstructible;
- Coverage Incomplete without an applicable accepted ranking exception;
- incompatible/ineligible Evaluation Basis;
- unresolved correction/invalidation/replacement/successor-work conditions expected to change the ranking basis;
- unavailable Aggregate/policy basis;
- unresolved tie semantics.

Ranking Readiness is derived and has no direct write action.

A calculated ordering may coexist with `Ranking Ready = false` if the representation clearly preserves the distinction.

# Finalization Readiness

Finalization Readiness is a derived explanation of whether current closeout inputs are sufficiently resolved for the later coordinated closeout action.

It may compose:

- current eligible evidence;
- Coverage plus separate exception dispositions;
- Ranking Readiness;
- Evaluation Policy;
- required Award decisions;
- unresolved correction/reconciliation conditions;
- reconstructible intended OutcomeBasis/Closeout Basis.

Preserve:

```text
Finalization Readiness = true
  != Competition Finalized
  != Outcome Declaration exists
```

013-H owns the later high-consequence Award/finalization/declaration authority mapping.

# Derived state is never editable source truth

The following are projections/explanations and must not be generic write targets:

- Remaining Work;
- Coverage;
- Aggregate;
- Rank;
- Ranking Readiness;
- Finalization Readiness;
- reconciliation issue/projection state.

A user action changes the appropriate source, invokes a specifically governed exception, or exercises an owner-defined authority action; the derived projection then changes accordingly.

# Calculated does not mean official

Organizer visibility of Aggregate or Rank does not itself establish recognition or official-result authority.

The experience may show calculated/reconciled state before official closeout, but must not present it as officially declared merely because no blockers remain.

```text
calculated
  != recognized
  != official
  != public
```

Award, Competition Finalization and Outcome Declaration mapping belongs to [013-H](../../013-concept-mapping-interaction-semantics-user-visible-representation/README.md).

# Related mapping

- live event coordination / remaining obligations → [Organizer Live Operations & Remaining Work Mapping](live-operations.md);
- correction/invalidation/replacement/successor work → [Authority Lineage, Capture & Correction Mapping](authority-lineage-correction.md);
- active Judge evaluation → [Judge Active Evaluation Mapping](judge-evaluation.md).

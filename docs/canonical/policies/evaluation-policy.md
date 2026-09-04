---
type: Design Policy
title: Evaluation Policy
description: Authoritative Competition configuration governing evidence eligibility, Coverage, aggregation, ranking, precision, ties, and Rubric compatibility.
status: stable
tags: [policy, evaluation, ranking]
sources:
  - resource: ../../002-concept-specification/002-F-aggregation-coverage-ranking-evaluation-policy.md
  - resource: ../../002-concept-specification/002-I-phase-consolidation-specification-exit-review.md
---

# Canonical contract

Evaluation Policy declares how authoritative evaluation evidence becomes eligible for [Coverage](../mechanisms/coverage.md), [Aggregate](../mechanisms/aggregate.md), and [Rank](../mechanisms/rank.md).

It governs evidence eligibility, minimum Coverage, composition exceptions, aggregation basis, Rubric-version compatibility, Team/rank eligibility, comparison precision, tie behavior, and any explicit alternative weighting.

<a id="eval-001"></a>
## EVAL-001 — Equal eligible individual Judge weighting

The baseline aggregation policy gives every eligible authoritative individual Judge Scorecard one equal unit of weight. An alternative weighting model must be explicit Evaluation Policy rather than an implementation side effect.

<a id="eval-002"></a>
## EVAL-002 — No silent Rubric pooling or rescaling

Rubric Versions with incompatible scoring semantics are not silently pooled, normalized, or rescaled into a common result. Compatibility must be explicit and reconstructible.

<a id="eval-003"></a>
## EVAL-003 — Outcome-affecting policy is reconstructible

Once judging begins, outcome-affecting Evaluation Policy must be reconstructible/versioned/provenanced so an official result can identify the policy under which it was produced.

Missing evaluation semantics are owned by [INV-003 — Missing Is Never Zero](../invariants/missing-never-zero.md#inv-003). Rank derivation and tie behavior are owned by [RANK-001](../mechanisms/rank.md#rank-001) and [RANK-002](../mechanisms/rank.md#rank-002).
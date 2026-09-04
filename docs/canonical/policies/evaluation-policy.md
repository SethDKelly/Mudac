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

Baseline policy: every eligible authoritative individual Judge Scorecard has equal weight; missing is never zero; incompatible Rubric semantics are not silently pooled/rescaled; Rank is Division-scoped; true ties use declared policy rather than hidden implementation order.

Once judging begins, outcome-affecting policy must be reconstructible/versioned/provenanced so an official result can identify the policy under which it was produced.
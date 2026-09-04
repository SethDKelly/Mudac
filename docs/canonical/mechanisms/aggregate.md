---
type: Derived Mechanism
title: Aggregate
description: Numerical combination of eligible authoritative individual Judge Scorecards under Evaluation Policy.
status: stable
tags: [mechanism, evaluation, aggregation]
sources:
  - resource: ../../002-concept-specification/002-F-aggregation-coverage-ranking-evaluation-policy.md
  - resource: ../../002-concept-specification/002-I-phase-consolidation-specification-exit-review.md
---

# Canonical contract

Aggregate is computed from eligible current authoritative [Scorecards](../concepts/scorecard.md) according to [Evaluation Policy](../policies/evaluation-policy.md).

The baseline Team Aggregate gives each eligible individual Judge Scorecard one equal unit of weight. Encounter/Panel means are analytical views and are not averaged again into the official Team Aggregate.

Missing evidence is excluded as missing, never converted to zero. Judges are not silently normalized and statistical outliers remain eligible unless an actual evaluation error is established.

Aggregate does not itself establish [Coverage](coverage.md) or Rank eligibility.
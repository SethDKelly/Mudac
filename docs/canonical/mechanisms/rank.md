---
type: Derived Mechanism
title: Rank
description: Derived Division-scoped ordering of rank-eligible Teams under declared comparison and tie policy.
status: stable
tags: [mechanism, ranking, outcome]
sources:
  - resource: ../../002-concept-specification/002-F-aggregation-coverage-ranking-evaluation-policy.md
  - resource: ../../002-concept-specification/002-I-phase-consolidation-specification-exit-review.md
---

# Canonical contract

Rank is derived from rank-eligible Teams and their [Aggregates](aggregate.md) within a [Division](../concepts/division.md), under [Evaluation Policy](../policies/evaluation-policy.md).

Rank is never directly edited. Full authoritative precision determines comparison unless policy explicitly says otherwise. Display rounding does not silently determine Rank.

True ties remain ties unless a predeclared resolver applies. Baseline shared-rank behavior is compatible with `1, 2, 2, 4`.

A calculated Rank may exist while Ranking readiness is blocked; calculated does not mean official.

See [Calculated Is Not Official](../invariants/calculated-not-official.md).
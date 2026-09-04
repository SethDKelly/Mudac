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

Rank consumes rank-eligible Teams, their [Aggregates](aggregate.md), Division scope, and [Evaluation Policy](../policies/evaluation-policy.md).

<a id="rank-001"></a>
## RANK-001 — Rank is derived and non-editable

Rank is calculated from authoritative inputs and is never directly authored or edited in normal operation. If an ordering is wrong, its evidence, eligibility, Division, or governing policy must be corrected.

<a id="rank-002"></a>
## RANK-002 — Precision and ties follow declared policy

Authoritative comparison precision and tie behavior come from Evaluation Policy. Display rounding, Team ID, insertion order, random order, or other hidden implementation behavior must not silently resolve a tie.

A calculated Rank may exist before ranking readiness or official outcome authority; that distinction is owned by [INV-006 — Calculated Is Not Official](../invariants/calculated-not-official.md#inv-006).
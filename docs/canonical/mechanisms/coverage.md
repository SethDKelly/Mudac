---
type: Derived Mechanism
title: Coverage
description: Derived factual sufficiency of qualifying evaluation evidence, kept distinct from governed exception disposition.
status: stable
tags: [mechanism, evaluation, eligibility, sufficiency]
sources:
  - resource: ../../002-concept-specification/002-F-aggregation-coverage-ranking-evaluation-policy.md
  - resource: ../../010-project-purpose-candidate-specification-modularity/010-F-specificity-purpose-singularity-concept-boundary-alternative-audit.md
  - resource: ../../010-project-purpose-candidate-specification-modularity/010-G-completeness-independence-genericity-for-boundary-audit.md
  - resource: ../../010-project-purpose-candidate-specification-modularity/010-H-concept-boundary-convergence-respecification-canonical-reconciliation.md
generated: { by: openai/gpt-5.6-sol, at: 2026-09-12T03:12:00Z }
---

# Canonical contract

Coverage is a **derived mechanism** answering whether the supplied set of qualifying evaluation evidence satisfies declared evaluation requirements.

## Factual sufficiency

The factual sufficiency dimension is at least:

- `Satisfied` — qualifying evidence meets the applicable requirement basis;
- `Incomplete` — qualifying evidence does not meet the applicable requirement basis.

Missing evidence remains missing. It is never converted to a zero value or represented as present merely to satisfy a threshold.

## Exception disposition is separate

A governed exception may permit a downstream consequence despite factual `Incomplete` Coverage. The exception disposition is **not another factual Coverage status**.

Therefore:

```text
factual sufficiency = Incomplete
exception disposition = Accepted
```

may both be true at the same time.

Exception acceptance never fabricates evidence, changes the observed evidence count/composition, or makes `Incomplete` read as `Satisfied`.

Material exception authority is governed by [Operational Exception & Override Governance](../policies/operational-exception-governance.md#opg-001).

# Inputs and outputs

Coverage may consider supplied eligible evidence, requirement/policy basis, composition requirements, exclusions, and declared thresholds. It returns reconstructible factual sufficiency and enough basis information to explain that result.

Coverage does not author or mutate [Evaluation Obligation](../concepts/evaluation-obligation.md), [Scorecard](../concepts/scorecard.md), or [Evaluation Occurrence](../concepts/evaluation-occurrence.md) state.

# Boundary with Aggregate and Rank

Coverage remains distinct from [Aggregate](aggregate.md). A competitor may have a calculable numeric Aggregate while Coverage is factually Incomplete.

Whether accepted exception disposition makes a subject eligible for a later result/rank/declaration is an application policy/synchronization question; Coverage does not silently change its factual answer.

See [Missing Is Never Zero](../invariants/missing-never-zero.md).
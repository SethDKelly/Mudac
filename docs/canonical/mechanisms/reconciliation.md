---
type: Derived Mechanism
title: Reconciliation
description: Organizer source-directed work that resolves outcome-affecting evidence, eligibility, policy, tie, Award and closeout conditions without becoming lifecycle or ticket authority.
status: stable
tags: [mechanism, reconciliation, outcomes]
sources:
  - resource: ../../002-concept-specification/002-G-awards-reconciliation-finalization-official-outcomes.md
  - resource: ../../003-conceptual-ux-architecture/003-F-reconciliation-coverage-ranking-awards-finalization-experience.md
  - resource: ../../007-design-refinement/007-G-policy-representation-outcome-disclosure-operational-governance-closure-audit.md
  - resource: ../../013-concept-mapping-interaction-semantics-user-visible-representation/013-G-live-operations-remaining-work-exception-reconciliation-derived-outcome-state-mapping.md
---

# Canonical contract

Reconciliation is an Organizer process/work context, not a Competition lifecycle state, independent Concept, or generic ticket system.

Organizers resolve or explicitly disposition authoritative source conditions involving paper capture, Scorecard correction, invalidation/replacement, current evidence eligibility, Coverage, Rubric compatibility, Division assignment, ties, Evaluation Policy, Awards and closeout prerequisites.

A reconciliation item is resolved only when its authoritative source changes, a specifically permitted governed exception changes the allowed consequence, or another owner-defined semantic action establishes the required postcondition.

Checking off, acknowledging, hiding, suppressing or dismissing a presentation cannot rewrite evidence or clear a semantic gate.

Governed exceptions follow [Operational Exception & Override Governance](../policies/operational-exception-governance.md#opg-001) and preserve the underlying source shortfall.

# Remaining-work boundary

Historically Satisfied responsibility does not become `remaining work` merely because its evidence later becomes ineligible.

```text
ineligible evidence
  → reconciliation/evidence-gap condition
  != reopened predecessor obligation
  != automatic successor Judge work
```

New Judge work exists only when an explicit successor Evaluation Obligation is legitimately established.

# Derived-state boundary

Reconciliation may expose Coverage, Aggregate, Rank, Ranking Readiness and Finalization Readiness, but none is editable source truth.

```text
Coverage fact != exception disposition
Aggregate != Coverage != Rank
calculated Rank != Ranking Readiness != official authority
Finalization Readiness != Competition Finalized != Outcome Declaration
```

See [Reconciliation & Derived Outcome-State Mapping](../experience/reconciliation-derived-state.md) and [Organizer Live Operations & Remaining Work Mapping](../experience/live-operations.md).

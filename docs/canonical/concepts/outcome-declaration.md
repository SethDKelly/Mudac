---
type: Design Concept
title: Outcome Declaration
description: Explicit authoritative declaration over an identified outcome basis, with affected and successor-declaration history.
status: stable
tags: [concept, outcome, authority, declaration]
sources:
  - resource: ../../002-concept-specification/002-G-awards-reconciliation-finalization-official-outcomes.md
  - resource: ../../007-design-refinement/007-D-temporal-state-correction-invalidation-supersession-historical-truth-closure.md
  - resource: ../../010-project-purpose-candidate-specification-modularity/010-E-retained-concept-purpose-operational-principle-state-action-behavioral-specification-current-truth-audit.md
  - resource: ../../010-project-purpose-candidate-specification-modularity/010-F-specificity-purpose-singularity-concept-boundary-alternative-audit.md
  - resource: ../../010-project-purpose-candidate-specification-modularity/010-G-completeness-independence-genericity-for-boundary-audit.md
  - resource: ../../010-project-purpose-candidate-specification-modularity/010-H-concept-boundary-convergence-respecification-canonical-reconciliation.md
  - resource: ../../011-concept-composition-synchronization/011-G-coverage-aggregate-rank-award-competition-finalization-outcome-declaration-composition.md
  - resource: ../synchronizations/evaluation-outcome-finalization-declaration.md
generated: { by: openai/gpt-5.6-sol, at: 2026-09-14T14:24:00-05:00 }
---

# Purpose

Establish and preserve an explicit authoritative declaration over an identified outcome basis, including honest currentness and successor history after legitimate correction.

# Abstract parameters

Conceptually:

`OutcomeDeclaration<Scope, OutcomeBasis, DeclaringAuthority>`

`OutcomeBasis` is supplied declaration content/basis. Outcome Declaration does not calculate or interpret the internal semantics of Coverage, Aggregate, Rank, Awards, or other result components.

# State

Outcome Declaration owns stable declaration identity, Scope, immutable declared OutcomeBasis sufficient for reconstruction, DeclaringAuthority reference, declaration time, currentness such as `Current`, `Affected`, or `Superseded`, predecessor/successor declaration relationship, and attributable affected reason/basis when material.

An Affected declaration remains the latest explicitly declared authority until a legitimate successor is explicitly confirmed. It is not silently replaced by newer calculations.

# Actions and queries

Conceptual actions are `declare`, `identifyAffected`, and `confirmSuccessor`.

Conceptual queries include `currentDeclaration`, `basis`, `isAffected`, `predecessor`, `successor`, `history`, and reconstructible declaration state as of a relevant time.

# Operational Principle

An authorized actor explicitly declares a supplied outcome basis. That immutable declaration becomes the current official authority for its Scope. If later source correction changes facts on which the declaration materially depended, the declaration becomes Affected while remaining the latest declared authority. After corrected source state is reconciled, an authorized actor may explicitly confirm a successor declaration. The predecessor becomes Superseded historical authority and remains reconstructible.

<a id="out-001"></a>
## OUT-001 — Explicit declaration establishes official outcome authority

Calculated, ranking-ready, lifecycle-finalized, rendered, or exported information does not become official merely by existing. Official outcome authority is established only by an explicit Outcome Declaration over an identified basis under the applicable declaring authority.

Competition Finalization may coordinate this action in MUDAC, but Competition does not own declaration content/history.

<a id="out-002"></a>
## OUT-002 — Affected declaration requires explicit successor confirmation

A source/policy correction may make the current declaration Affected and change latest calculations. The prior declaration remains the latest declared official authority until an explicit successor is confirmed. The predecessor then becomes Superseded historical authority and remains reconstructible.

If the materially corrected declared basis changes but the visible winner/rank/Award values happen to remain identical, an Affected predecessor is still not silently cleared. Explicit successor confirmation establishes official authority over the corrected basis.

# MUDAC composition binding

MUDAC normally binds Scope to a Competition context and supplies an OutcomeBasis identifying the accepted evidence/policy/Coverage/exception/Rank/Award state needed to explain the declared result.

Current [Evaluation Outcome, Award, Finalization & Declaration Composition](../synchronizations/evaluation-outcome-finalization-declaration.md) classifies:

- initial `declare` as composition-only inside ordinary **Finalize Competition & Declare Outcome** together with `Competition.finalize`;
- `identifyAffected` as a system-triggered/composition reaction when a material dependency of the immutable declared basis changes;
- `confirmSuccessor` as the explicit high-consequence declaration action after corrected source/derived/Award state has been reconciled.

A successor declaration does not re-finalize Competition. Declaration actions do not publish results.

# Boundaries

Outcome Declaration does not compute Coverage, Aggregate, or Rank; define/confer Awards; own Competition lifecycle; generate external representations; or release representations.

The former [Official Outcome Revision](../mechanisms/official-outcome-revision.md) path is retained only as a deprecated historical adapter.

See [Calculated Does Not Mean Official](../invariants/calculated-not-official.md#inv-006) and [Official Does Not Automatically Mean Public](../invariants/official-not-automatically-public.md#inv-007).
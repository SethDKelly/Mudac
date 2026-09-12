---
type: Design Policy
title: Awards and Finalization Policy
description: Governing rules for Award readiness/conferral, Competition Finalization, and the requirement for explicit Outcome Declaration authority without conflating declaration with publication.
status: stable
tags: [policy, awards, finalization, outcome-declaration]
sources:
  - resource: ../../002-concept-specification/002-G-awards-reconciliation-finalization-official-outcomes.md
  - resource: ../../010-project-purpose-candidate-specification-modularity/010-H-concept-boundary-convergence-respecification-canonical-reconciliation.md
generated: { by: openai/gpt-5.6-sol, at: 2026-09-12T03:12:00Z }
---

# Canonical contract

Rank-derived Awards consume a ranking-ready supplied selection basis and are confirmed without contradicting the declared Award rule. Discretionary Awards are authorized human decisions and must not be portrayed as mathematically implied unless their policy actually defines such derivation.

Competition Finalization is an explicit high-consequence lifecycle action gated by the applicable reconciled evidence, factual Coverage plus any governed exception disposition, evaluation-basis compatibility, ranking readiness, required tie resolution, authoritative evaluation policy, and required/consistent Award decisions.

**Declared official outcome authority belongs to [Outcome Declaration](../concepts/outcome-declaration.md), not to Competition lifecycle state.**

MUDAC official closeout must not represent a Competition as having a declared official result unless the applicable outcome basis has been explicitly declared under [OUT-001](../concepts/outcome-declaration.md#out-001). The precise trigger/transaction/retry relationship between `Competition.finalize` and `OutcomeDeclaration.declare` is a Phase 011 synchronization question and is not made intrinsic to either Concept by this policy.

Post-Finalization source corrections leave Competition Finalized. If the declared outcome basis is affected, the current declaration becomes Affected; official authority changes only through an explicitly confirmed successor under [OUT-002](../concepts/outcome-declaration.md#out-002).

Outcome Declaration does not publish results. External representation/release remain separate Export and Publication authority.
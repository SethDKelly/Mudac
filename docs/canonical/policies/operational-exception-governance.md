---
type: Design Policy
title: Operational Exception and Override Governance
description: Cross-cutting rules for governed exceptions, waivers, acknowledgements, suppression, escalation, and emergency operational intervention without falsifying source truth or transferring semantic authority.
status: stable
tags: [policy, exception, override, governance, authority]
sources:
  - resource: ../../002-concept-specification/002-F-aggregation-coverage-ranking-evaluation-policy.md
  - resource: ../../002-concept-specification/002-G-awards-reconciliation-finalization-official-outcomes.md
  - resource: ../../003-conceptual-ux-architecture/003-E-organizer-judge-panel-encounter-live-operations-experience.md
  - resource: ../../003-conceptual-ux-architecture/003-F-reconciliation-coverage-ranking-awards-finalization-experience.md
  - resource: ../../007-design-refinement/007-E-end-to-end-scenario-exception-failure-adversarial-authority-validation.md
  - resource: ../../007-design-refinement/007-F-judge-organizer-experience-concept-action-synchronization-authority-traceability-audit.md
  - resource: ../../007-design-refinement/007-G-policy-representation-outcome-disclosure-operational-governance-closure-audit.md
---

# Purpose

Govern cross-cutting operational exceptions without creating a generic override authority or rewriting the source facts that made an exception necessary.

This policy does not create an `Exception` Concept, ticket lifecycle, or universal override action. Specific exception permission remains subordinate to the policy/semantic context that permits it.

<a id="opg-001"></a>
## OPG-001 — Governed exceptions preserve source truth

An accepted exception may change a declared permission, eligibility, or proceed consequence of a known condition only where policy explicitly permits it.

It must preserve the underlying observed fact or shortfall. An exception cannot make missing evidence appear present, make a degraded Panel objectively compliant, rewrite who participated in an Encounter, or otherwise falsify historical/current source truth merely to clear a gate.

<a id="opg-002"></a>
## OPG-002 — Exception authority is explicit, scoped, attributable, and reasoned

A material governed exception must identify the Competition/resource/policy condition it affects, the permitted consequence, the acting Identity/Participation or exceptional authorizer as applicable, and a reason sufficient to reconstruct why proceeding was allowed.

Exception authority is limited to that declared consequence. It does not silently waive unrelated policies or invariants.

<a id="opg-003"></a>
## OPG-003 — Generic override cannot bypass semantic invariants

Operational labels such as `override`, `force`, `waive`, `accept`, `acknowledge`, or `resolve` do not create a universal authority path.

A governed exception cannot be used to:

- convert missing evaluation to zero or present evidence;
- transfer Judge authorship to Organizer/Administrator;
- create duplicate evaluation weight;
- turn calculated Rank into official authority;
- make official outcomes automatically public;
- assume success/failure when authoritative outcome is unknown;
- silently reactivate invalidated evidence;
- erase historical Publication or disclosure occurrence;
- convert system/break-glass privilege into Competition decision authority.

Changing one of these semantics requires explicit canonical redesign rather than an operational exception.

<a id="opg-004"></a>
## OPG-004 — Acknowledgement, suppression, and presentation state are not resolution

Acknowledging, dismissing, hiding, suppressing, or closing a warning/exception presentation does not repair its source condition or establish domain success.

An issue becomes resolved only when its authoritative source changes, a specific governed exception changes the permitted consequence, or another owner-defined semantic action establishes the required postcondition.

<a id="opg-005"></a>
## OPG-005 — Technical emergency capability does not create policy authority

System administration, support, infrastructure recovery, session revocation, or emergency/break-glass capability may restore or restrict technical operation where authorized, but does not itself grant authority to accept Competition policy exceptions, amend Judge judgment, finalize results, alter Award decisions, override disclosure, or publish Competition outcomes.

When a technical mechanism facilitates an authorized semantic action, actor/author/authorizer distinctions remain attributable through the relevant Access and Provenance rules.

# Operational taxonomy

MUDAC distinguishes:

- **warning** — informative condition that does not itself block authority;
- **blocking precondition** — required condition is false and the action cannot proceed;
- **governed exception** — policy explicitly permits a scoped consequence despite a preserved condition/shortfall;
- **correction** — source truth is wrong or requires legitimate successor/invalidation/replacement semantics;
- **technical emergency intervention** — operational capability is restored/restricted without substituting semantic authority.

These are governance meanings, not another Competition lifecycle.

# Composition rule

Policies compose. A permitted exception in one policy does not waive unrelated constraints.

Examples:

- a Panel-composition exception does not waive Scorecard authorship;
- a Coverage exception does not make incompatible Rubric Versions compatible;
- Finalization authority does not waive disclosure classification;
- paper continuity does not waive Evaluation Policy;
- Publication authority does not grant Access to private source evidence.

A contradiction between current canonical policies must return through canonical change governance rather than being resolved by whichever implementation path has an `override` control.

# Boundaries

This policy does not own warnings, reconciliation items, policy-specific exception data, source correction, Access, or Provenance. It governs the cross-cutting semantics those owners must preserve when an exception-like operational path exists.

See [Coverage](../mechanisms/coverage.md), [Panel Composition Policy](panel-composition.md), [Correction & Authority](correction-authority.md), [Access](../concepts/access.md#acc-002), [Experience Action, State & Authority Traceability](../experience/action-authority-traceability.md), and [Provenance](../concepts/provenance.md).

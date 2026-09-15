---
type: Phase Design Record
title: 012-E — Authority Lineage, Provenance & Correctability Dependence
description: "Resolves MUDAC inclusion dependence for Versioning and Provenance, distinguishes universal Concept dependence from authority-capability co-inclusion, prevents support Concepts from becoming graph-wide sinks, and establishes the authority-history rules that later outcome and release dependence must preserve."
status: stable
tags: [phase-012, jackson, dependence, versioning, provenance, correction, authority, history]
sources:
  - resource: 012-A-dependence-scope-subset-semantics-product-family-questions-subphase-planning.md
  - resource: 012-B-application-family-boundary-concept-inclusion-roles-candidate-dependence-inventory.md
  - resource: 012-C-competition-actor-competitor-context-bias-control-dependence.md
  - resource: 012-D-evaluation-structure-responsibility-basis-judgment-dependence.md
  - resource: ../canonical/dependence/application-family-dependence.md
  - resource: ../canonical/project/purpose-needs-success-tensions.md
  - resource: ../canonical/concepts/versioning.md
  - resource: ../canonical/concepts/provenance.md
  - resource: ../canonical/concepts/rubric.md
  - resource: ../canonical/concepts/scorecard.md
  - resource: ../canonical/concepts/outcome-declaration.md
  - resource: ../canonical/synchronizations/evaluation-basis-scorecard-authority.md
  - resource: ../canonical/synchronizations/temporal-truth-correction.md
  - resource: ../canonical/policies/correction-authority.md
  - resource: ../canonical/policies/evaluation-policy.md
  - resource: https://github.com/SethDKelly/Base/blob/main/docs/phases/006/dependence-subset-contract.md
generated: { by: openai/gpt-5.6-sol, at: 2026-09-15T14:11:00-05:00 }
---

# Purpose

Resolve how the generic support Concepts **Versioning** and **Provenance** participate in the MUDAC product family without turning every authoritative or historical Concept into a dependency on both.

012-E distinguishes three questions that are easy to collapse incorrectly:

1. Does the existence of Concept `A` universally require Versioning or Provenance?
2. Does a particular **authority capability** of `A` require Versioning and/or Provenance?
3. Does `A` already own enough intrinsic history that generic support would duplicate rather than clarify responsibility?

The phase also pressure-tests whether Versioning and Provenance depend on one another.

# Decision summary

**PASS — no new universal direct Concept-dependence edge is established; authority-capability co-inclusion rules are established.**

012-E rejects Versioning and Provenance as graph-wide dependency sinks.

The following are **not** universal Concept-dependence edges:

```text
Rubric                ↛ Versioning
Rubric                ↛ Provenance
Scorecard             ↛ Versioning
Scorecard             ↛ Provenance
Versioning            ↛ Provenance
Provenance            ↛ Versioning
Competition           ↛ Versioning
Competition           ↛ Provenance
Evaluation Occurrence ↛ Versioning
Evaluation Occurrence ↛ Provenance
Evaluation Obligation ↛ Versioning
Evaluation Obligation ↛ Provenance
Outcome Declaration   ↛ Versioning
Outcome Declaration   ↛ Provenance
```

Instead, current MUDAC authority semantics establish **capability-conditioned co-inclusion**:

```text
Authoritative Rubric Basis capability
  requires Versioning + Provenance

Authoritative Scorecard Evidence capability
  requires Versioning + Provenance

Scorecard authoritative correction / invalidation capability
  requires Versioning + Provenance

Rubric authoritative supersession / invalidation capability
  requires Versioning + Provenance
```

This is stronger than a loose recommendation and weaker than a universal binary edge from the Concept itself.

# 1. Why support Concepts are not universal graph sinks

Versioning and Provenance are independently specified generic Concepts.

Versioning answers:

> what authoritative states existed, which immutable committed state is current/eligible, and what was superseded or invalidated?

Provenance answers:

> how, why, from what source, by which actor, and under whose represented authority did meaningful state arise?

Those purposes are complementary but not identical.

A Concept can legitimately own its own lifecycle/history without needing either generic support owner. Conversely, Provenance can explain a meaningful authority event that is not represented as Versioning lineage, and Versioning can preserve snapshots even where richer actor/source explanation is not part of the included capability.

Therefore:

```text
historical state exists
  != Versioning required

meaningful actor/source explanation exists
  != every subject requires Provenance

Versioning included
  != Provenance universally included

Provenance included
  != Versioning universally included
```

# 2. Versioning ↛ Provenance

**Decision: reject universal edge.**

A coherent use of Versioning can preserve:

- initial authoritative snapshot;
- successor snapshot;
- predecessor/successor order;
- current eligible Version;
- superseded history;
- invalidated history.

That remains a meaningful application capability even if richer explanatory Provenance is supplied elsewhere or deliberately omitted in a reduced subset.

MUDAC's **high-assurance authoritative evaluation** capability does require Provenance alongside Versioning, but that is a capability rule over the supported authority profile, not intrinsic co-inclusion of the two Concepts.

# 3. Provenance ↛ Versioning

**Decision: reject universal edge.**

Provenance can explain authority/history for events that are not Version lineages, including:

- paper capture actor versus Judge represented authority;
- corrected historical assertions;
- exceptional reason/authorizer;
- source/capture-channel history;
- declaration or release events whose owning Concept already preserves predecessor/successor history.

Therefore Provenance retains a meaningful role without generic Versioning.

# 4. Rubric support dependence

## 4.1 Rubric ↛ Versioning

**Decision: reject universal edge.**

Rubric remains meaningful as a reusable working/preparation instrument:

```text
create Draft
configure criteria
validate definition
prepare for use
```

without establishing immutable authoritative basis lineage.

That coherent contraction was already preserved by 012-D.

## 4.2 Rubric ↛ Provenance

**Decision: reject universal edge.**

Working Rubric definition and validation can be meaningful without authority-origin history.

## 4.3 Authoritative Rubric Basis requires Versioning

**Accepted capability rule.**

When a MUDAC variant claims that a Rubric basis is authoritative for judging, the application must be able to identify one exact immutable basis and preserve later successor/invalidation semantics without silently reinterpreting prior evaluation.

Versioning owns this role.

Therefore:

```text
Authoritative Rubric Basis
  ⇒ include Versioning
```

## 4.4 Authoritative Rubric Basis requires Provenance

**Accepted capability rule.**

Authoritative basis establishment, successor establishment, or invalidation must remain attributable enough to explain meaningful authority and correction history.

Therefore:

```text
Authoritative Rubric Basis
  ⇒ include Provenance
```

Together:

```text
Authoritative Rubric Basis
  ⇒ Versioning + Provenance
```

This does not transform the generic Rubric Concept into `Rubric → Versioning` or `Rubric → Provenance`.

# 5. Scorecard support dependence

## 5.1 Scorecard ↛ Versioning

**Decision: reject universal edge.**

A reduced MUDAC judging subset may use Scorecard for non-authoritative working judgment capture without committing immutable authoritative snapshots.

Such a subset may be coherent even if later scope selection decides it is not an adopted product variant.

## 5.2 Scorecard ↛ Provenance

**Decision: reject universal edge.**

A reduced working-capture subset can preserve semantic Judge identity in Scorecard without richer actor/source/correction explanation.

## 5.3 Authoritative Scorecard Evidence requires Versioning

**Accepted capability rule.**

Once a Scorecard is permitted to become authoritative evaluation evidence, MUDAC's current historical-truth and correctability purpose requires:

- immutable authoritative snapshot identity;
- explicit current eligible authority;
- predecessor preservation;
- successor authority without destructive rewrite;
- invalidation without silent predecessor revival.

Versioning owns those semantics.

Therefore:

```text
Authoritative Scorecard Evidence
  ⇒ include Versioning
```

## 5.4 Authoritative Scorecard Evidence requires Provenance

**Accepted capability rule.**

Authoritative Scorecard use must preserve meaningful distinction among:

- Judge semantic author;
- capture actor;
- represented authority;
- paper/electronic/import source;
- meaningful finalization/correction reason;
- occurrence time versus later capture/verification time where material.

Provenance owns that explanation.

Therefore:

```text
Authoritative Scorecard Evidence
  ⇒ include Provenance
```

Together:

```text
Authoritative Scorecard Evidence
  ⇒ Versioning + Provenance
```

# 6. Correctability makes both support roles mandatory for authoritative evaluation

MUDAC purpose requires current authority to be correctable without destructive historical rewrite.

For Rubric and Scorecard authoritative state, current correction composition uses both support Concepts deliberately:

```text
semantic successor
  → Versioning commits successor
  + Provenance explains actor / represented authority / source / reason
```

```text
invalidation
  → Versioning preserves retained ineligible state
  + Provenance explains meaningful authority / reason / source
```

For Scorecard capture correction:

```text
same logical Scorecard
  + successor Version
  + capture-correction Provenance
  + Judge remains represented authority
```

For Rubric correction:

```text
new authoritative Rubric Version
  + Provenance
  + historical evaluation remains bound to prior exact Version
```

Thus a variant that claims **authoritative and correctable evaluation evidence** but omits either Versioning or Provenance is not a valid current authority profile.

# 7. Working-state and preparation contractions remain coherent

The following reduced capabilities remain dependence-coherent at this phase:

## Working Rubric preparation

```text
Rubric
without Versioning
without Provenance
```

Meaning:

- editable instrument definition;
- validation/preparation;
- no claim that a Draft/prepared state is the immutable authoritative basis used by judging.

## Working Scorecard capture

```text
Scorecard + Team + Participation + Rubric
without Versioning
without Provenance
```

Meaning:

- one Judge's working judgment capture;
- no claim of authoritative evaluation evidence/current eligible Version;
- no high-assurance correction lineage.

Whether these contractions become adopted MUDAC variants belongs to 012-I.

# 8. Outcome Declaration does not require generic Versioning

**Decision: reject universal `Outcome Declaration → Versioning`.**

Outcome Declaration already owns:

- immutable declared OutcomeBasis;
- declaration identity;
- Current/Affected/Superseded meaning;
- predecessor/successor declaration relation;
- reconstructible declaration history.

Routing that history through generic Versioning would duplicate rather than clarify the Concept boundary.

Therefore official-outcome history does not justify a generic Versioning edge merely because it is authoritative.

012-F still owns Outcome Declaration's dependencies on Competition, outcome capability, Award, and evidence/result context.

# 9. Outcome Declaration does not universally require Provenance

**Decision: reject universal `Outcome Declaration → Provenance`.**

Outcome Declaration intrinsically retains DeclaringAuthority, declaration time, immutable basis, affected reason/basis where material, and successor history.

That is sufficient to preserve its independent official-authority purpose without generic Provenance.

Provenance may still participate in an implementation/application variant where richer source/actor explanation is materially required, but Phase 012 does not make it a universal inclusion dependency of the declaration Concept.

# 10. Competition and domain-owned history do not imply support edges

012-E confirms the 012-B rejection of blanket:

```text
Competition → Versioning
Competition → Provenance
```

Competition owns lifecycle/history semantics relevant to its purpose.

The same principle applies to other domain owners whose meaningful histories are intrinsic:

```text
Evaluation Occurrence ↛ Versioning
Evaluation Occurrence ↛ Provenance

Evaluation Obligation ↛ Versioning
Evaluation Obligation ↛ Provenance
```

Occurrence owns bounded historical occurrence/validity/replacement truth.

Obligation owns responsibility state, reasons, predecessor/successor responsibility, and meaningful transition history.

Generic support is not required merely because history exists.

# 11. Corrected historical assertions are a Provenance capability, not a global edge

When later evidence proves that MUDAC's earlier recorded historical assertion was wrong, current correction semantics preserve:

1. the as-recorded/as-known assertion;
2. the later corrected best-known assertion;
3. attributable evidence explaining the correction.

Provenance is required for this **corrected-historical-assertion capability**.

But an application subset that never offers that correction capability does not thereby create a universal outgoing edge from Evaluation Occurrence, Team, Division, Alias, or Panel to Provenance.

# 12. Evaluation Policy history is a cross-cutting authority requirement

Evaluation Policy is not a Concept vertex in the dependence graph.

Current policy nevertheless requires that once judging begins, outcome-affecting policy be reconstructible/versioned/provenanced.

Therefore any adopted variant that permits authoritative judging/outcome formation must preserve authoritative policy history using the current authority-history support model.

This is a **cross-cutting product-family authority rule**, not a Concept edge.

Phase 012-F must carry this requirement into official-outcome dependence reasoning.

# 13. No co-inclusion cycle

012-E establishes no cycle:

```text
Versioning ↛ Provenance
Provenance ↛ Versioning
```

The two support Concepts frequently co-participate in high-assurance authoritative actions, but their independent purposes remain intact.

The application may require the pair for a particular capability without making either Concept universally meaningless without the other.

# 14. No global history/support bundle

Reject the following model:

```text
any stateful Concept
  → Versioning
  → Provenance
```

Also reject:

```text
any correction
  → generic history coordinator
```

Current MUDAC correction remains owner-specific.

Versioning and Provenance participate only where their distinct purposes are actually needed.

No new Workflow, History, Audit, Correction, Change, Revision, or Authority coordinator Concept is justified.

# 15. Representative subset consequences

## Dependence-coherent / capability-limited

```text
Rubric
```

Reusable working evaluation-instrument preparation without authoritative basis lineage.

```text
Scorecard + Team + Participation + Rubric
```

Working judgment capture without claiming authoritative evidence lineage.

```text
Outcome Declaration + its later 012-F prerequisites
```

Official declaration history without generic Versioning/Provenance merely for declaration succession.

## Invalid for the claimed capability

```text
Authoritative Rubric Basis
without Versioning
```

Cannot establish exact immutable/current authoritative basis lineage.

```text
Authoritative Rubric Basis
without Provenance
```

Cannot satisfy the current attributable authority-history profile.

```text
Authoritative Scorecard Evidence
without Versioning
```

Cannot satisfy current immutable/current/correctable evidence-history semantics.

```text
Authoritative Scorecard Evidence
without Provenance
```

Cannot preserve the current actor/semantic-author/source/correction explanation required by MUDAC.

# 16. Phase-011 composition remains correct

012-E does not alter current full-product composition:

- Establish Authoritative Rubric Version coordinates Rubric + Versioning + Provenance;
- Finalize Evaluation coordinates Scorecard + Versioning + Provenance + Evaluation Obligation satisfaction;
- Judge amendment coordinates Scorecard + Versioning + Provenance;
- authoritative paper capture uses Provenance to preserve capture actor versus Judge represented authority;
- Rubric/Scorecard invalidation uses Versioning plus meaningful Provenance;
- Versioning and Provenance remain composition-only support actions rather than generic administrative controls.

The dependence result explains **when the support Concepts must be included**, while Phase 011 still owns **how they synchronize**.

# 17. Phase-010 integrity result

No intrinsic Concept defect is exposed.

Versioning remains generic over `Subject, Snapshot`.

Provenance remains generic over `Subject, StateRef, Actor, RepresentedAuthority, Scope, Source`.

Rubric and Scorecard remain independently specified from both support Concepts.

Outcome Declaration's independent successor-history semantics remain justified.

No Phase-010 reopening is required.

# 18. Phase-012-F handoff

012-F must now resolve Award and Outcome Declaration inclusion dependence while preserving these 012-E constraints:

1. official authority does not automatically imply generic Versioning;
2. Outcome Declaration already owns declaration succession/currentness;
3. Outcome Declaration has no universal Provenance edge;
4. outcome-capable adopted variants must preserve reconstructible outcome-affecting Evaluation Policy authority history;
5. traceability back to authoritative Scorecards must not become a dense direct dependence graph merely because the evidence path is reconstructible;
6. any Scorecard treated as authoritative outcome evidence already carries the Versioning + Provenance authority-profile requirement from this phase.

# Exit decision

**PASS.**

012-E resolves Versioning/Provenance inclusion semantics without creating graph-wide support sinks or a Versioning↔Provenance co-inclusion cycle.

Current direct Concept-dependence graph edges remain those established by 012-C and 012-D.

012-E adds durable **authority-capability co-inclusion rules** rather than universal binary Concept edges.

Proceed to:

> **012-F — Outcome, Recognition & Official-Authority Dependence**

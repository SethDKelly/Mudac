---
type: Design Audit
title: 007-D — Temporal State, Correction, Invalidation, Supersession & Historical-Truth Closure
description: Audits MUDAC temporal semantics across current/historical authority, Draft/commit, amendment, invalidation, replacement, affected/stale state, official outcomes, Export/Publication and correction history.
status: stable
tags: [phase-007, jackson, temporal, correction, history, invalidation, supersession]
sources:
  - resource: ../007-design-refinement/007-C-cross-concept-synchronization-completeness-authority-seam-audit.md
  - resource: ../canonical/synchronizations/concept-synchronizations.md
  - resource: ../canonical/concepts/versioning.md
  - resource: ../canonical/concepts/provenance.md
  - resource: ../canonical/policies/correction-authority.md
  - resource: ../canonical/invariants/current-vs-historical-truth.md
  - resource: ../canonical/mechanisms/official-outcome-revision.md
  - resource: ../canonical/concepts/export.md
  - resource: ../canonical/concepts/publication.md
  - resource: ../canonical/governance/design-implementation-boundary.md
---

# Purpose

Close the temporal/correction portion of the renewed Jackson-methodology gate by proving that MUDAC can change current authority, correct errors, invalidate unusable evidence, supersede prior authoritative state, replace invalid occurrences, and revise official/public outcomes without destructive rewrite or ambiguous historical truth.

007-D tests whether later UX/architecture introduced temporal states that the Concept model never explicitly owned, and whether common words such as `historical`, `superseded`, `invalidated`, `affected`, `stale`, and `withdrawn` have accidentally been used as interchangeable status labels.

# Principal result

The temporal model is structurally sound and **does not require a new Concept**.

The main gap was vocabulary/composition closure. Current semantics are now consolidated under [Temporal Truth, Correction & Historical Authority](../canonical/synchronizations/temporal-truth-correction.md).

The audit finds that temporal meaning is inherently multi-dimensional. Lifecycle, working/committed authority, lineage currentness, validity/eligibility, dependency currency, replacement, release availability, and historical observation must remain distinguishable.

# Temporal axes confirmed

## 1. Domain lifecycle

Each Concept retains its own lifecycle where it has one. Competition, Participation and Encounter lifecycle are not generic history states.

`Historical` is not another Competition/Participation/Encounter lifecycle value.

## 2. Working versus authoritative state

Draft work may exist while a prior committed state remains authoritative. A complete Draft is still non-authoritative until its authority-establishing action succeeds.

Scorecard Amendment Draft is the canonical example: the prior finalized Version remains current authority until amendment finalization establishes a successor.

## 3. Current versus superseded lineage

Supersession occurs only when an explicit successor becomes current within the same logical lineage/release chain. Superseded state was not necessarily wrong; it is prior legitimate authority preserved as history.

Versioning successor and Publication successor are related temporal patterns but do not collapse their separate Concepts.

## 4. Validity / eligibility

Invalidation means retained state is no longer eligible for the purpose it had or might have served. It does not erase content and does not automatically create a successor.

The audit explicitly rejects a silent fallback rule such as “if the current Version is invalid, use the preceding Version.” If no valid successor/current state exists, the system must represent the absence of eligible current authority.

## 5. Affected versus stale

`Affected` means a dependency changed and review/recompute/reconfirmation is required. It does not yet assert the dependent result is wrong.

`Stale` means the dependent calculation/representation is known not to reflect the current applicable source basis.

Neither term is a lifecycle value or a synonym for invalidation.

## 6. Replacement

Replacement links a distinct logical subject/occurrence to the invalidated/cancelled subject it stands in place of.

This differs from Version supersession:

```text
same logical Scorecard
  Version 1 → Version 2
      = successor Version

distinct invalidated Encounter
  Encounter A → Encounter B
      = replacement occurrence
```

## 7. Distribution state

Published/Withdrawn/Superseded describe Publication availability/history rather than source authority.

A Publication may therefore legitimately be:

```text
Published + Affected
```

when source truth changes but the release has not yet been explicitly withdrawn or superseded.

## 8. Historical observation

Historical truth records what was observed, presented, authored, declared or released at the relevant occurrence/time. It is not merely “whatever is not current.”

# Correction taxonomy closure

007-D distinguishes six materially different correction families.

## Working-state edit

Non-authoritative work changes before commitment. No successor authoritative Version is required simply because Draft data changes.

## Semantic amendment

The semantic author changes already-authoritative content within the same logical subject. Prior authority remains until explicit successor finalization.

Primary case: Judge Scorecard amendment.

## Capture/transcription correction

The semantic source did not change; MUDAC's captured representation was wrong.

Before verification, correct the Draft. After authoritative capture, preserve the prior capture authority and establish attributable successor evidence. Organizer capture correction never becomes Judge-authored semantic amendment merely because the bytes/fields changed.

## Structural correction

The relationship/context/identity basis was wrong or changed: Division, Alias, Panel/Encounter participant structure and similar state.

Current owner state changes explicitly; historical Encounter snapshots remain unchanged unless the historical record itself is proven erroneous.

Where structural error makes existing authoritative evaluation semantically unusable, invalidate/replace the affected occurrence/evidence rather than pretending a Judge content amendment can repair structural identity.

## Provenance correction

An incorrect origin/actor/time/channel assertion is itself corrected append-stably. Provenance history may be corrected; it is not silently rewritten.

## Official/public correction

Correcting source state does not directly mutate official or public authority. Latest calculations may change first; existing official/public declarations become Affected where appropriate; explicit successor Official Outcome Revision and successor Publication are separate authority-establishing actions.

# Encounter and dependent Scorecard closure

007-D clarifies a subtle invalidation seam.

If an Encounter is invalidated, the Scorecards produced in it remain historical evidence of what the Judges authored. Their **eligibility for official aggregation** is lost because the authoritative Encounter basis is invalid.

The model should not need to mutate every Scorecard into a fictional state implying the Judge judgment itself never existed.

A Scorecard may also be invalidated directly when its own semantic basis is unusable. The invalidation target and reason must therefore be explicit.

A rejudge is a new replacement Encounter with new evaluation obligations, not a relabeling of the original invalidated Encounter.

# Historical-record correction closure

`INV-005` correctly states that current correction does not rewrite what happened. 007-D refines the difficult case where the stored historical assertion itself was wrong.

Two questions are distinct:

1. **What did MUDAC record/consider authoritative at the time?**
2. **What does MUDAC now conclude actually happened at that time after later verified evidence?**

A later correction may improve the second answer while preserving the first answer and the correction lineage.

Example:

```text
T1: Encounter record says Alias A was presented
T2: reliable evidence proves Alias B was actually presented

historical record at T1 remains attributable
corrected historical assertion records B as best-known occurrence truth
Provenance explains the correction
```

This is not permission for destructive rewrite.

# Occurrence time versus knowledge/authority time

The audit confirms that meaningful provenance sometimes needs two temporal notions:

- when the underlying event/source occurrence happened or was effective; and
- when MUDAC captured, verified, corrected or established authority for that information.

Examples include paper judging captured after the live Encounter, a Division correction discovered after Event Completed, and a post-Finalization source correction.

This is a semantic requirement only. 007-D does **not** prescribe a bitemporal database schema.

# Scorecard temporal closure

The accepted path remains:

```text
obligation
   ↓
Draft
   ↓ explicit finalize
Version 1 current
   ↓ begin amendment
Amendment Draft exists
Version 1 still current
   ↓ explicit finalize amendment
Version 2 current
Version 1 superseded historical
```

Abandoning the amendment leaves Version 1 current.

Invalidation differs from amendment: an invalidated Scorecard/Version may leave no eligible current evaluation until legitimate successor/replacement authority is established.

# Competition temporal closure

Competition lifecycle remains:

```text
Draft → Ready → Active → Event Completed → Finalized
```

Exceptional `resumeEvent` is a lifecycle correction before Finalization and does not auto-restore old Access/Participation capability as established by 007-C.

After Finalization, source correction does not roll Competition backward. It triggers reconciliation and possible successor official outcome authority while Competition remains Finalized.

# Official outcome temporal closure

The audit establishes the phrase **latest declared official revision** for the state between a source correction and a successor official confirmation.

```text
O1 declared official
source correction occurs
latest calculations may change
O1 = latest declared official + Affected
not silently replaced

explicit successor confirmation
O2 = latest declared official
O1 = Superseded official history
```

This prevents the system from implying either that the old official result vanished instantly or that known source corrections are irrelevant until someone republishes.

# Export / Publication temporal closure

Export and Publication retain separate timelines.

An Export is bound immutably to its original source basis. A source correction may make it Affected/Stale, but does not rewrite it.

Publication remains the historical act of release. Source correction does not silently change the released bytes or retarget the Publication.

Replacement path:

```text
corrected source
  → successor Export
  → explicit successor Publication
```

Withdrawal is also explicit and preserves that the prior Publication existed.

# Access/revocation closure

Access expiry/revocation ends current/future capability but does not retroactively invalidate actions that were legitimately authorized when performed.

Likewise, Award revocation preserves that a conferral occurred. Whether current official outcomes must change is handled through reconciliation and successor official authority rather than destructive deletion of the Award history.

# Historical query closure

The conceptual model can now distinguish six questions that an implementation must eventually support:

1. What is current/eligible now?
2. What did MUDAC consider authoritative at time T?
3. What does MUDAC now believe actually happened at time T after later corrections?
4. What context did an Encounter actually present/use?
5. What outcome revision was declared official at time T?
6. What representation was publicly/distributively released at time T?

These are design obligations, not API/database prescriptions.

# Hidden-state pressure test

The audit considered whether the following should become Concepts:

- Temporal State;
- Correction;
- Historical Record;
- Revision Status;
- Impact/Affectedness;
- Replacement.

None has an independent user purpose stronger than the coordination of existing Concepts, Versioning, Provenance, mechanisms and policies. They remain temporal/synchronization semantics.

# Canonical refinements

007-D updates current owners to align terminology:

- Versioning distinguishes successor supersession, invalidation and distinct-subject replacement;
- Provenance distinguishes occurrence/effective time from later capture/authority/correction time when materially different;
- Correction & Authority names the correction families explicitly;
- `INV-005` distinguishes current operational truth, as-known historical authority and later corrected best-known occurrence history;
- Official Outcome Revision exposes Affected latest-declared-official semantics;
- Export and Publication separate source currency from distribution state.

No existing stable rule identifier changes meaning.

# Implementation-freeze consequence

007-D does not authorize persistence fields, temporal tables, event sourcing, APIs, status enums or correction workflows in code.

In particular, the conceptual dual-time distinction must **not** be interpreted as authorization to implement a bitemporal database before the design exit.

The 006-D executable freeze remains fully active.

# Exit decision

**007-D passes the Temporal State, Correction, Invalidation, Supersession & Historical-Truth Closure audit.**

The fourth Jackson completion gate now has substantive evidence. Final methodology exit must still confirm these semantics survive scenario/adversarial and experience/policy pressure.

# Handoff

Proceed to **007-E — End-to-End Scenario, Exception, Failure & Adversarial Authority Validation**.

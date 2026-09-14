---
type: Synchronization Contract
title: Temporal Truth, Correction & Historical Authority
description: "Current MUDAC composition for supersession, invalidation, replacement, successor evaluation responsibility, source-faithful capture correction, corrected historical assertions, and non-destructive affected-state propagation after Phase 011-F."
status: stable
tags: [synchronization, temporal, correction, invalidation, replacement, successor, affected, versioning, provenance, phase-011]
sources:
  - resource: ../../011-concept-composition-synchronization/011-F-temporal-correction-invalidation-replacement-successor-work-affected-state-propagation.md
  - resource: ../concepts/evaluation-occurrence.md
  - resource: ../concepts/evaluation-obligation.md
  - resource: ../concepts/scorecard.md
  - resource: ../concepts/versioning.md
  - resource: ../concepts/provenance.md
  - resource: ../concepts/outcome-declaration.md
  - resource: ../concepts/export.md
  - resource: ../concepts/publication.md
  - resource: ../policies/correction-authority.md
  - resource: ../policies/continuity-paper.md
  - resource: ../invariants/current-vs-historical-truth.md
  - resource: ../invariants/one-logical-scorecard.md
  - resource: evaluation-occurrence-obligation.md
  - resource: evaluation-basis-scorecard-authority.md
generated: { by: openai/gpt-5.6-sol, at: 2026-09-14T13:36:00-05:00 }
---

# Purpose

Define current MUDAC temporal/correction composition so authoritative state can be corrected or invalidated without destructive rewrite, successor work can be created without reopening historical responsibility, and dependency currentness can propagate without silently changing declared or published authority.

This document is the current Phase 011-F temporal/correction owner. It replaces the pre-011 interpretation of the same path and supersedes the source-correction/invalidation/successor portions of legacy synchronization 09/12. Outcome-specific consequences remain 011-G; Export/Publication consequences remain 011-H.

# Governing rule — correct the smallest semantic owner

Correction begins by identifying **what fact is actually wrong**.

Do not route every defect through a generic workflow/cascade.

Examples:

- Judge changes judgment → Scorecard semantic amendment;
- digital paper transcription is wrong → same logical Scorecard capture correction;
- wrong evaluator/subject/occurrence/basis → structural evidence invalidation/replacement;
- occurrence unusable → Evaluation Occurrence invalidation/replacement;
- committed Version no longer eligible → Versioning invalidation;
- prior terminal responsibility must be done again → Evaluation Obligation successor;
- actor/source/time explanation wrong → Provenance correction;
- dependent currentness changed → downstream owner-specific Affected/Stale/recompute semantics.

# Temporal dimensions are independent

MUDAC does not flatten temporal meaning into one status field.

## Domain lifecycle

Concept-owned lifecycle such as Competition, Participation or Evaluation Occurrence progression.

## Working versus committed authority

Draft/correction work may exist while prior committed authority remains current.

## Lineage currentness

`Superseded` means an explicit successor of the **same logical lineage** became current. It does not imply the predecessor was erroneous.

## Validity / eligibility

`Invalidated` means retained state is no longer eligible for the relevant authoritative purpose. Invalidation does not imply a successor and never revives an older predecessor automatically.

## Replacement

`Replaced` links a **distinct logical subject/occurrence** to the prior one it stands in place of. Replacement is not Version supersession.

## Dependency currency

`Affected` means a dependency changed and review/recompute/reconfirmation is required.

`Stale` means the dependent is known not to reflect the applicable current source basis.

These are owner-specific currency meanings, not universal lifecycle states.

## Distribution state

Publication `Published`, `Withdrawn`, and `Superseded` remain release/distribution meanings. Source correction does not automatically change them.

## Historical observation

Historical state preserves what was recorded, presented, authored, declared or released at the time. A later corrected best-known account may coexist with the prior as-known record.

# Supersession versus invalidation versus replacement

```text
same logical Scorecard
  v1 → v2
  = Version supersession
```

```text
Scorecard current Version found unusable
  → invalidate Version
  = no current eligible Scorecard Version unless a legitimate successor exists
```

```text
Occurrence A invalidated
  → distinct Occurrence B
  = replacement occurrence
```

The three transitions must never be treated as synonyms.

# Scorecard semantic amendment

Judge-authored semantic amendment remains the 011-E successor path:

- amendment Draft is non-authoritative;
- predecessor Scorecard Version remains current until explicit finalization;
- `Versioning.commitSuccessor` establishes the successor;
- Provenance classifies the change as Judge-authored semantic amendment;
- the same logical Scorecard and same Satisfied obligation remain;
- no extra evaluation weight is created.

# Source-faithful capture correction

When authoritative digital Scorecard content demonstrably mismatches an identified unchanged external source, MUDAC uses **Correct Authoritative Capture**.

Conditions:

- structural Scorecard identity remains correct;
- source is unambiguous;
- corrected values are directly supported by that source;
- correction actor has capture-correction authority;
- no new Judge intent is inferred.

The same logical Scorecard establishes a successor authoritative Version.

Provenance distinguishes:

```text
Actor                = capture/correction actor
RepresentedAuthority = Judge
Source               = identified physical/external source
Classification       = capture/transcription correction
```

The predecessor remains immutable Superseded/as-known authority. The Evaluation Obligation remains Satisfied by the same logical Scorecard.

Capture correction never becomes a second vote and is never mislabeled as a Judge semantic amendment.

# Structural Scorecard misbinding

Evaluator, Subject, OccurrenceContext and EvaluationBasis are structural Scorecard identity.

They are not ordinary amendment content.

If one is wrong:

- preserve the incorrect record/history;
- invalidate the unusable current Scorecard Version for evaluation use;
- never rebind the old logical Scorecard silently.

If an identified authoritative source proves the correct structural binding and original Judge content without inference, a distinct correctly bound Scorecard may be established from that source with correction Provenance.

If the correct binding cannot be proven, no replacement judgment is invented. Current evidence remains ineligible and governing policy decides whether new evaluation work is required.

# Scorecard Version invalidation

A current Scorecard Version may be invalidated when it is no longer eligible and cannot be legitimately corrected as a successor state of the same logical evaluation.

Application composition uses:

- `Versioning.invalidateVersion(currentVersion, reasonRef)`;
- `Provenance.record`.

After invalidation:

- the Version remains retained/reconstructible;
- older Versions do not silently revive;
- the Scorecard lineage may have no current eligible Version;
- a previously Satisfied Evaluation Obligation remains historically Satisfied;
- current evidence eligibility is lost independently of historical satisfaction.

If another evaluation is genuinely required, use successor-obligation semantics. Do not reopen the predecessor obligation.

# Evaluation Occurrence invalidation

`EvaluationOccurrence.invalidate` means the occurrence happened but is no longer eligible for its intended evaluative use.

Occurrence invalidation preserves:

- occurrence identity;
- presented context;
- actual participant history;
- timing;
- Judge-authored Scorecards;
- obligation history.

It does **not** require mutating every dependent Scorecard Version into an invalid state. A Scorecard can remain authentic historical Judge evidence while being ineligible for current aggregation because its occurrence dependency is invalid.

This keeps authored-content truth separate from current evidence eligibility.

# Responsibility after occurrence invalidation

Obligation state is explicit rather than inferred from occurrence state.

## Outstanding obligation

An Outstanding obligation tied to an invalid occurrence can no longer be satisfied against that invalid context.

The application explicitly ends/cancels the responsibility for that occurrence. Missing evidence remains missing.

If replacement work is required, it is separately established against the replacement occurrence.

## Satisfied obligation

A Satisfied predecessor remains Satisfied historically by its logical Scorecard.

If that evidence becomes ineligible and policy requires another evaluation:

- `EvaluationObligation.requireSuccessorEvaluation` creates an Outstanding successor;
- the predecessor remains terminal/history-preserving;
- the successor must later be satisfied by a **new logical Scorecard**.

## Excused / Cancelled obligation

These remain terminal historical states. Replacement occurrence alone does not recreate responsibility.

# Replacement occurrence

A re-evaluation uses a distinct replacement Evaluation Occurrence.

```text
Occurrence A = Invalidated
Occurrence B = separately prepared/begun
A.linkReplacement(B)
```

Replacement does not copy participants, obligations, Scorecards, Access, Panel membership, presentation context or basis automatically.

At replacement begin:

- prior terminal responsibilities deliberately required again use successor-obligation semantics;
- genuinely new evaluator responsibilities use ordinary establishment;
- no obligation is cloned merely because a replacement link exists.

# Rubric Version supersession

Ordinary new Rubric Version establishment is prospective successor authority.

Existing occurrences, obligations and Scorecards remain bound to the exact Rubric Version they already used.

No historical re-interpretation occurs merely because a newer Rubric Version exists.

# Rubric Version invalidation

Rubric Version invalidation is a distinct high-consequence action.

Application composition uses:

- `Versioning.invalidateVersion(rubricVersion, reasonRef)`;
- `Provenance.record`.

No older Rubric Version silently becomes current.

Dependency impact is selective and reason-sensitive:

- Prepared occurrence with an ineligible basis cannot begin and is ordinarily cancelled/re-prepared;
- Open/Complete occurrence whose evaluative validity is materially undermined may require occurrence invalidation/replacement;
- a defect isolated to one Scorecard may require evidence invalidation rather than invalidating the whole occurrence;
- prospective/editorial change with no historical semantic impact must not be treated as retroactive invalidation.

A Rubric Version reference therefore creates a dependency to assess, not an automatic destructive cascade.

# Corrected historical assertions

Current Team/Division/Alias/Panel state does not rewrite past Evaluation Occurrence presentation/participants.

If reliable later evidence proves that MUDAC's **recorded historical assertion itself** was wrong, the application preserves two truths:

1. what MUDAC recorded/considered at the time;
2. the later corrected best-known account of what actually happened.

`Provenance.record` supplies attributable correction/successor evidence. The original occurrence snapshot remains the as-recorded historical state.

If the corrected historical fact changes evaluative validity, the owning occurrence/evidence invalidation action is still required separately. Provenance correction alone does not change business validity.

# Provenance correction

Incorrect Provenance is corrected append-stably through successor evidence.

Correcting actor/time/channel/source metadata does not silently mutate the domain subject. If the corrected provenance proves a structural/business defect, the natural domain owner must also transition.

# Successor work is conditional

Evidence invalidation does **not** automatically mean a new evaluation must occur.

The application/policy may instead permit an exception or another consequence while factual evidence remains missing/ineligible.

`requireSuccessorEvaluation` is therefore deliberate, attributable and policy-governed.

No generic invalidation action automatically creates new Judge work.

# Affected-state propagation

After an authoritative source transition, dependent currentness is reevaluated according to actual source-basis relationships.

Rules:

1. source correction/invalidation commits at the source owner first;
2. only actual dependents are considered affected;
3. each dependent keeps its own vocabulary/state owner;
4. `Affected` means review/recompute/reconfirmation, not automatically wrong;
5. `Stale` means known not to reflect the applicable current basis;
6. downstream recalculation/reconfirmation/replacement never rewrites the source transition;
7. downstream affectedness never rolls the source back automatically.

This is conceptual dependency propagation, not an event-bus/queue/transaction design.

# Downstream handoff

Phase 011-F establishes **why** downstream currentness must change or be reconsidered. The owner-specific actions remain dependency-safe work:

- Coverage/Aggregate/Rank, Award and Outcome Declaration → 011-G;
- Export currency and Publication release/replacement → 011-H.

In particular:

- an Award never silently moves recipients because Rank changed;
- an Outcome Declaration is never silently replaced by a new calculation;
- an Export never silently rewrites its SourceBasis;
- a Publication never silently retargets a new representation or withdraws itself.

# Post-Finalization correction

Source correction after Competition Finalized leaves Competition Finalized.

The corrected source/history may change current evidence/calculation support, but declared and public authority remain explicit successor decisions through their own Concepts.

Finalized closes ordinary operation; it does not require retention of known false source state.

# Action-surface classification

| Action | MUDAC classification |
| --- | --- |
| working-state edit | direct owner action |
| Judge semantic amendment | controlled direct/coordinated; current 011-E |
| Correct Authoritative Capture | controlled coordinated correction |
| `Versioning.invalidateVersion` | composition-only; purpose-specific invocation only |
| Invalidate Evaluation Evidence | high-consequence coordinated correction |
| `EvaluationOccurrence.invalidate` | high-consequence coordinated application action |
| `EvaluationOccurrence.linkReplacement` | composition-only within replacement action |
| ending Outstanding obligation after invalid occurrence | coordinated responsibility consequence |
| `EvaluationObligation.requireSuccessorEvaluation` | composition-only/controlled; never automatic |
| Correct Historical Assertion | controlled provenance/domain composition |
| Provenance correction | controlled explanatory correction |
| generic "cascade/recompute everything" | intentionally unavailable |

# Composition invariants

1. Correction preserves prior attributable authority/history.
2. Supersession is not invalidation.
3. Invalidation is not replacement.
4. Invalidation never silently revives an older Version.
5. Occurrence invalidation does not erase or rewrite Judge-authored Scorecards.
6. Current evidence eligibility may differ from historical obligation satisfaction.
7. Terminal obligations never reopen.
8. Re-evaluation after unusable evidence uses a successor obligation and new logical Scorecard.
9. Capture correction preserves the same Judge author and logical Scorecard when structural identity is unchanged.
10. Structural Scorecard identity never changes through ordinary amendment/capture correction.
11. Replacement occurrence is distinct and does not clone responsibilities/evidence automatically.
12. Rubric supersession never retroactively rebinds historical evaluation state.
13. Rubric invalidation impact is selective, not blanket destructive propagation.
14. Provenance correction never substitutes for a required domain correction.
15. Affected/Stale currentness does not silently alter declared/public authority.
16. Competition remains Finalized after post-Finalization source correction.
17. No correction path grants Organizer/Admin Judge semantic authorship.

# No temporal catch-all Concept

Correction, impact, replacement and affectedness coordinate existing owners. They still do not establish a singular independent user purpose requiring another Concept.

Implementations may later realize these semantics with fields, logs or workflows, but Phase 011-F defines no schema, transaction, event, queue, job, retry or service choreography.

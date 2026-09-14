---
type: Design Policy
title: Correction and Authority Policy
description: Authority-preserving rules for amendments, capture repair, structural correction, invalidation, obligation succession, historical-assertion correction, affected-state propagation, and post-finalization change.
status: stable
tags: [policy, correction, authority]
sources:
  - resource: ../../002-concept-specification/002-E-versioning-provenance-correction-authority-preservation.md
  - resource: ../../007-design-refinement/007-D-temporal-state-correction-invalidation-supersession-historical-truth-closure.md
  - resource: ../../010-project-purpose-candidate-specification-modularity/010-H-concept-boundary-convergence-respecification-canonical-reconciliation.md
  - resource: ../../011-concept-composition-synchronization/011-F-temporal-correction-invalidation-replacement-successor-work-affected-state-propagation.md
  - resource: ../synchronizations/temporal-truth-correction.md
generated: { by: openai/gpt-5.6-sol, at: 2026-09-14T13:36:00-05:00 }
---

# Canonical contract

Correction authority follows **semantic meaning** and targets the smallest owner that is actually wrong.

MUDAC distinguishes correction families rather than routing all changes through one generic edit/cascade:

- **working-state edit** — non-authoritative Draft change;
- **semantic amendment** — legitimate semantic author changes already-authoritative content through successor authoritative state;
- **capture/transcription correction** — recorded representation of an unchanged semantic source is repaired while preserving author/capture distinction;
- **structural correction** — relationship/context/identity basis such as Division, Alias, Panel, Evaluation Occurrence or Scorecard structural identity is corrected by its natural owner/invalidation path;
- **Version invalidation** — retained committed state is no longer eligible for the relevant authoritative purpose and no predecessor silently revives;
- **occurrence invalidation/replacement** — an occurrence that happened becomes ineligible and any re-evaluation uses a distinct replacement occurrence;
- **obligation succession** — a terminal historical Evaluation Obligation is preserved while legitimate new responsibility is established as a successor;
- **provenance/historical-assertion correction** — explanatory or best-known occurrence history is corrected append-stably rather than rewritten invisibly;
- **official/public correction** — corrected source state changes dependency currentness, but successor Outcome Declaration, Export and Publication authority remain explicit separate transitions.

## Scorecard authority

Judge judgment changes use Judge-authored Scorecard amendment.

A demonstrable post-authority paper/external transcription mismatch may use the same logical Scorecard's successor-authority mechanics when structural identity is unchanged and the retained source unambiguously proves the Judge-authored content. The Organizer remains capture/correction actor, the Judge remains RepresentedAuthority, and Provenance classifies the transition as capture/transcription correction rather than Judge amendment.

Wrong Evaluator, Subject, OccurrenceContext or EvaluationBasis is structural misbinding and cannot be repaired as ordinary amendment/capture correction. Preserve the incorrect record and use explicit invalidation/replacement or trustworthy source rebinding into a distinct correctly bound Scorecard.

## Occurrence and responsibility

If an Evaluation Occurrence becomes invalid, the occurrence remains historical and may link to a distinct replacement occurrence. Judge-authored Scorecards remain historical evidence even when they become ineligible because the occurrence dependency is invalid.

Outstanding obligations tied to the invalid occurrence are explicitly ended rather than left satisfiable against invalid context.

If a previously Satisfied Evaluation Obligation must be fulfilled again because its evidence is no longer eligible, the historical obligation is not reopened; `requireSuccessorEvaluation` creates a new Outstanding successor responsibility. A successor evaluation uses a new logical Scorecard.

Successor work is never automatic merely because evidence became ineligible. Governing policy may instead permit an exception or another consequence.

## Versioning

Supersession and invalidation are distinct.

- successor Version = newer authority of the same logical subject;
- invalidation = retained Version no longer eligible;
- replacement = distinct logical subject/occurrence.

Invalidation does not automatically revive an older predecessor or imply that a replacement exists. Versioning may legitimately report no current eligible Version.

Ordinary Rubric Version supersession never reinterprets historical Scorecards. Rubric invalidation affects only actual dependents whose eligibility/meaning is materially undermined.

## Historical truth

Current Team/Division/Alias/Panel correction never silently rewrites historical occurrence presentation or participants.

If later evidence proves that MUDAC's recorded historical assertion itself was inaccurate, preserve the earlier as-recorded/as-known state and append attributable corrected best-known historical evidence through Provenance. If the corrected fact changes evaluative validity, perform the appropriate owner-specific invalidation separately.

## Downstream affectedness

Source correction/invalidation may require dependent results/declarations/representations to become Affected, Stale, recomputed or explicitly replaced according to their own owners.

Affectedness never silently:

- moves an Award;
- replaces an Outcome Declaration;
- rewrites an Export SourceBasis;
- withdraws or retargets a Publication.

Outcome-specific composition belongs to 011-G; Export/Publication composition belongs to 011-H.

## Finalized Competition

Outcome-affecting post-Finalization correction leaves Competition Finalized. Corrected source authority/history may change, but declared/public authority changes only through explicit successor actions.

Organizer or Administrator technical capability never permits invention of Judge judgment or silent transfer of semantic authorship.

See [Temporal Truth, Correction & Historical Authority](../synchronizations/temporal-truth-correction.md), [Organizer Does Not Become Judge Author](../invariants/organizer-not-judge-author.md), and [Current and Historical Truth Remain Distinct](../invariants/current-vs-historical-truth.md).

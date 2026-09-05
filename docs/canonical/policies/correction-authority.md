---
type: Design Policy
title: Correction and Authority Policy
description: Authority-preserving rules for amendments, capture repair, structural correction, invalidation, and post-finalization change.
status: stable
tags: [policy, correction, authority]
sources:
  - resource: ../../002-concept-specification/002-E-versioning-provenance-correction-authority-preservation.md
  - resource: ../../002-concept-specification/002-I-phase-consolidation-specification-exit-review.md
  - resource: ../../007-design-refinement/007-D-temporal-state-correction-invalidation-supersession-historical-truth-closure.md
---

# Canonical contract

Correction authority follows semantic meaning.

MUDAC distinguishes these correction families rather than routing all changes through one generic edit operation:

- **working-state edit** — non-authoritative Draft change;
- **semantic amendment** — legitimate semantic author changes already-authoritative content through successor Versioning;
- **capture/transcription correction** — recorded representation of an unchanged semantic source is repaired while preserving author/capture distinction;
- **structural correction** — relationship/context/identity basis such as Division, Alias, Panel/Encounter structure is corrected by its owner;
- **provenance correction** — explanatory origin/time/actor/channel history is corrected append-stably;
- **official/public correction** — corrected source state affects downstream calculations/official/public truth, but successor official outcome and Publication authority remain explicit separate transitions.

Working Draft edits are ordinary. Judge judgment changes use Judge-authored amendment. Demonstrable paper transcription mismatch may be repaired by an authorized Organizer as capture correction while preserving Judge authorship. Structural errors use explicit correction/invalidation/replacement rather than mutating Scorecard identity. Outcome-affecting post-Finalization correction requires stronger governance and reconciliation.

Supersession and invalidation are distinct. Corrections preserve prior authoritative states and [Provenance](../concepts/provenance.md); destructive overwrite is not the ordinary recovery model.

Invalidation does not automatically revive an older predecessor or imply that a replacement exists. If no valid successor/replacement has been established, the system may legitimately have no current eligible authority for that purpose.

Organizer or Administrator technical capability does not permit invention of Judge judgment.

Current temporal meanings for superseded/invalidated/replaced/affected/stale/withdrawn state are owned by [Temporal Truth, Correction & Historical Authority](../synchronizations/temporal-truth-correction.md).

See [Organizer Does Not Become Judge Author](../invariants/organizer-not-judge-author.md).

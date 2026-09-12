---
type: Design Policy
title: Correction and Authority Policy
description: Authority-preserving rules for amendments, capture repair, structural correction, invalidation, obligation succession, and post-finalization change.
status: stable
tags: [policy, correction, authority]
sources:
  - resource: ../../002-concept-specification/002-E-versioning-provenance-correction-authority-preservation.md
  - resource: ../../007-design-refinement/007-D-temporal-state-correction-invalidation-supersession-historical-truth-closure.md
  - resource: ../../010-project-purpose-candidate-specification-modularity/010-H-concept-boundary-convergence-respecification-canonical-reconciliation.md
generated: { by: openai/gpt-5.6-sol, at: 2026-09-12T03:12:00Z }
---

# Canonical contract

Correction authority follows semantic meaning.

MUDAC distinguishes correction families rather than routing all changes through one generic edit operation:

- **working-state edit** — non-authoritative Draft change;
- **semantic amendment** — legitimate semantic author changes already-authoritative content through successor authoritative state;
- **capture/transcription correction** — recorded representation of an unchanged semantic source is repaired while preserving author/capture distinction;
- **structural correction** — relationship/context/identity basis such as Division, Alias, Panel or Evaluation Occurrence structure is corrected by its owner;
- **obligation succession** — a terminal historical Evaluation Obligation is preserved while a legitimate new responsibility is established as a successor;
- **provenance correction** — explanatory origin/time/actor/channel history is corrected append-stably;
- **official/public correction** — corrected source state affects calculations/declaration/representation/public truth, but successor Outcome Declaration and Publication authority remain explicit separate transitions.

Working Draft edits are ordinary. Judge judgment changes use Judge-authored Scorecard amendment. Demonstrable paper transcription mismatch may be repaired by an authorized Organizer as capture correction while preserving Judge authorship. Structural errors use explicit correction/invalidation/replacement rather than mutating semantic identity.

If an Evaluation Occurrence becomes invalid, the occurrence remains historical and may link to a distinct replacement occurrence. If a previously Satisfied Evaluation Obligation must be fulfilled again because its evidence is no longer eligible, the historical obligation is not reopened; a successor obligation is created.

Outcome-affecting post-Finalization correction leaves Competition Finalized. Calculated state may change and the current [Outcome Declaration](../concepts/outcome-declaration.md) may become Affected, but declared authority changes only through explicit successor confirmation.

Supersession and invalidation are distinct. Corrections preserve prior authoritative states and [Provenance](../concepts/provenance.md); destructive overwrite is not the ordinary recovery model.

Invalidation does not automatically revive an older predecessor or imply that a replacement exists. [Versioning](../concepts/versioning.md) may legitimately report no current eligible authoritative Version for a lineage.

Organizer or Administrator technical capability never permits invention of Judge judgment or silent transfer of semantic authorship.

Current temporal vocabulary remains recorded in [Temporal Truth, Correction & Historical Authority](../synchronizations/temporal-truth-correction.md) and will be revalidated as composition in Phase 011.

See [Organizer Does Not Become Judge Author](../invariants/organizer-not-judge-author.md).
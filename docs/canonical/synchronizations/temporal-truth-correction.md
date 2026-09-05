---
type: Synchronization Contract
title: Temporal Truth, Correction & Historical Authority
description: Defines MUDAC's cross-cutting temporal vocabulary for current, historical, superseded, invalidated, affected, stale, replaced, withdrawn and corrected state without collapsing independent lifecycle or authority dimensions.
status: stable
tags: [synchronization, temporal, correction, history, versioning, provenance, outcomes, publication]
sources:
  - resource: ../../007-design-refinement/007-D-temporal-state-correction-invalidation-supersession-historical-truth-closure.md
  - resource: concept-synchronizations.md
  - resource: ../concepts/versioning.md
  - resource: ../concepts/provenance.md
  - resource: ../policies/correction-authority.md
  - resource: ../invariants/current-vs-historical-truth.md
  - resource: ../mechanisms/official-outcome-revision.md
  - resource: ../concepts/export.md
  - resource: ../concepts/publication.md
---

# Purpose

Define how MUDAC reasons about change over time so correction can change current authority without destructive rewrite, historical claims remain explainable, and terms such as `Historical`, `Superseded`, `Invalidated`, `Affected`, `Stale`, and `Withdrawn` do not become one ambiguous status field.

# Temporal state is multi-dimensional

MUDAC does not model all temporal meaning as one universal lifecycle. Several independent dimensions may apply to the same subject at once.

## Domain lifecycle

Concept-owned lifecycle such as Competition `Draft → Ready → Active → Event Completed → Finalized`, Participation lifecycle, or Encounter lifecycle. Lifecycle state answers where the subject is in its own operational progression.

## Working versus committed authority

A Draft or pending correction may contain work while a previously committed state remains authoritative. Committing/finalizing establishes authority; merely editing or completing a Draft does not.

## Lineage currentness

For versioned authoritative state, one eligible committed Version may be current for a lineage. A predecessor becomes **Superseded** when an explicit successor becomes current. Supersession preserves predecessor validity as historical authority; it does not mean the predecessor was erroneous.

## Validity / eligibility

**Invalidated** means retained state/evidence is no longer eligible for the authoritative purpose for which it previously or potentially qualified. Invalidation preserves identity/content/history and does not imply that a replacement already exists.

Invalidation of an upstream subject may make dependent evidence ineligible without copying the invalidated state onto every dependent record. For example, invalidating an Encounter can disqualify Scorecards from official aggregation because their basis is invalid while preserving what each Judge actually authored.

## Dependency currency

**Affected** means a dependency changed and review/recalculation/reconfirmation is required; it does not yet assert that the dependent result is wrong.

**Stale** means the dependent representation/calculation is known not to reflect the current applicable source basis.

Affected/Stale are dependency-currency overlays, not lifecycle states and not destructive invalidation.

## Replacement

**Replaced** links one logical subject/occurrence to another distinct subject created to stand in its place, commonly after structural invalidation or a rejudge. Replacement differs from Version supersession: a successor Version is a new authoritative state of the same logical subject; a replacement is a different logical subject/occurrence.

## Distribution availability

For Publication, **Published**, **Withdrawn**, and **Superseded** describe release/distribution state. A Publication can remain historically Published while its bound Export/source basis is Affected. Withdrawal ends current distribution but does not erase the fact or content of the prior release.

## Historical observation

Historical state records what was observed, presented, authored, declared, or released at a past occurrence/time. `Historical` is not synonymous with invalid, superseded, archived, or inaccessible.

# Temporal vocabulary summary

| Term | Meaning | History retained? | Successor implied? |
| --- | --- | --- | --- |
| Draft | non-authoritative working state | prior authority remains | no |
| Current | presently selected eligible authority for the relevant lineage/purpose | yes | no |
| Historical | past observed/authoritative state retained for explanation | yes | no |
| Superseded | predecessor displaced by explicit successor within a lineage/release chain | yes | yes |
| Invalidated | retained state no longer eligible for its authoritative purpose | yes | no |
| Replaced | distinct logical subject/occurrence stands in place of prior one | yes | yes, distinct subject |
| Affected | dependency changed; review/recompute required | yes | no |
| Stale | known not to reflect current source basis | yes | no |
| Withdrawn | distribution/capability/recognition no longer active as applicable | yes | no |
| Revoked | previously granted capability/conferral ended by explicit authority | yes | no |
| Expired | time-bounded capability ended by time/lifecycle | yes | no |

# Correction families

Correction follows the semantic owner of what was wrong.

## Working-state edit

Edits before authority is established change Draft/current working state. They do not require a successor authoritative Version merely because keystrokes changed.

## Semantic amendment

A legitimate author changes the meaning/content of an already authoritative logical subject. The prior Version remains authoritative while amendment work is Draft; explicit amendment finalization commits a successor Version. Scorecard Judge judgment changes use this path.

## Capture / transcription correction

The semantic source is unchanged but MUDAC's captured representation of it is wrong. Before verification, the capture Draft is corrected. After a capture has become authoritative, correction preserves the prior authoritative capture and establishes attributable successor evidence without transferring semantic authorship. Paper transcription repair is the primary example.

## Structural correction

The wrong relationship/context/identity basis was recorded or current structure changed, such as Division assignment, Alias mapping, Panel membership or Encounter participant structure. The owning Concept is corrected explicitly. Historical Encounter presentation/participant snapshots do not silently rebind to current structural state.

If a structural error makes an already-created authoritative evaluation semantically unusable, the affected subject is invalidated/replaced rather than disguised as a content amendment.

## Provenance correction

If the explanatory record itself is wrong, Provenance adds attributable correction/successor evidence. Correcting who acted, when a fact was learned, or the capture channel must not rewrite the historical provenance statement invisibly.

## Official-outcome correction

A source correction may change latest Coverage/Aggregate/Rank and make the latest declared Official Outcome Revision **Affected**. It remains the latest declared official outcome until reconciliation and explicit successor confirmation. The Competition remains Finalized; no lifecycle rollback occurs.

## Publication correction

Source correction or a new Export does not retarget an existing Publication. The prior Publication remains historically attributable and may be Affected, Withdrawn or later Superseded. A corrected public release requires an explicit successor Export and successor Publication.

# Current authority after invalidation

An invalidated committed state was historically authoritative but is no longer eligible as current authority for the invalidated purpose.

If the invalidated state has no valid successor, the system must be able to represent **no current eligible authority** for that lineage/purpose rather than silently falling back to an older predecessor or treating invalidated state as still eligible.

A later replacement or successor becomes current only through its own valid authority-establishing transition.

# Historical snapshots and correction

Current source changes do not rewrite historical snapshots merely because current truth differs.

Examples include current Division versus Encounter-presented Division, current Alias versus Encounter-presented Alias, current Panel membership versus historical participants, current Scorecard Version versus prior Versions, current official outcome versus prior declared revisions, and current Publication versus prior releases.

However, MUDAC may later discover that its **historical record itself was inaccurate**. In that case the system records an attributable correction to the historical assertion while retaining the prior erroneous record and explaining why the corrected historical account is now preferred. `INV-005` prohibits silent rewrite, not evidence-based correction of a mistaken historical claim.

# Occurrence time and knowledge/authority time

When materially different, Provenance must preserve enough information to distinguish:

- when the underlying domain event/source occurrence happened or was effective; and
- when MUDAC captured, verified, corrected, or established authority for that information.

This supports paper judging captured digitally later, structural correction discovered after Event Completed, or post-Finalization correction about earlier evidence.

This is a conceptual requirement, not a mandate for a particular database bitemporal schema.

# Historical query obligations

The retained model must be capable of answering distinct questions without reconstructing them from mutable current state alone:

1. **Current operational truth** — what is eligible/current now?
2. **As-known authoritative truth** — what did MUDAC consider authoritative at a specified past time?
3. **Best-known occurrence history** — what does MUDAC now conclude actually happened at that past occurrence, including later attributable corrections?
4. **Historical presentation** — what Alias/Division/Rubric/participants were actually presented/used in an Encounter?
5. **Official-as-of truth** — which Official Outcome Revision had been explicitly declared at that time?
6. **Public-as-of truth** — which Publication was Published/Withdrawn/Superseded at that time and what exact Export did it bind?

# Correction propagation pattern

A source correction does not collapse source, calculated, official, and public truth into one instant mutable value.

```text
T0
source S1
  → calculated result C1
  → official revision O1
  → Export E1
  → Publication P1

T1 source correction
source S2 becomes current
  → C1 becomes Affected/Stale until recomputed
  → O1 remains latest declared official but becomes Affected
  → E1/P1 remain historical and may become Affected

T2 reconciliation + explicit official successor
  → calculated C2
  → official revision O2 becomes latest declared official
  → O1 becomes Superseded official history

T3 explicit external replacement if needed
  → Export E2
  → Publication P2
  → P1 may be Superseded/Withdrawn while remaining historical
```

At no stage does the new source silently rewrite O1, E1, or P1.

# Revocation and expiry do not invalidate prior authorized history

Revoking/expiring Access removes future/current capability. It does not retroactively invalidate actions that were legitimately authorized when performed.

Revoking an Award conferral preserves that a conferral occurred and records the revocation; whether the Award remains part of current official outcomes depends on subsequent reconciliation/official outcome authority.

# Cancellation versus invalidation

Where a lifecycle supports both terms, they are distinct:

- **Cancelled** — the intended occurrence was stopped before meaningful authoritative work from that occurrence should count;
- **Invalidated** — the occurrence/evidence happened or was established but later must no longer be eligible for official use.

For Judging Encounter, a rejudge after invalidation uses a distinct replacement Encounter rather than mutating the invalidated occurrence into the replacement.

# No temporal catch-all Concept

007-D finds no need for a `TemporalState`, `Correction`, `History`, `Case`, or `RevisionStatus` Concept. These semantics coordinate existing Concept-owned state, Versioning, Provenance, policies, invariants and synchronizations.

Implementations may encode status fields/timestamps, but those representations must preserve these independent dimensions rather than inventing one convenience enum that erases their distinctions.

---
type: Phase Design Record
title: 012-G — External Representation & Release Dependence
description: "Resolves MUDAC application-family inclusion dependence for Export and Publication, establishes Publication → Export as the minimum representation/release edge, rejects official/public and representation/release collapse, and records externalization capability rules for whole-graph subset analysis."
status: stable
tags: [phase-012, jackson, dependence, export, publication, representation, release, disclosure]
sources:
  - resource: 012-A-dependence-scope-subset-semantics-product-family-questions-subphase-planning.md
  - resource: 012-B-application-family-boundary-concept-inclusion-roles-candidate-dependence-inventory.md
  - resource: 012-F-outcome-recognition-official-authority-dependence.md
  - resource: ../canonical/dependence/application-family-dependence.md
  - resource: ../canonical/concepts/export.md
  - resource: ../canonical/concepts/publication.md
  - resource: ../canonical/concepts/outcome-declaration.md
  - resource: ../canonical/synchronizations/external-representation-publication-release.md
  - resource: ../canonical/policies/continuity-paper.md
  - resource: https://github.com/SethDKelly/Base/blob/main/docs/phases/006/dependence-subset-contract.md
---

# Purpose

Resolve the Phase 012 application-family inclusion dependence of the Concepts that own external representation and deliberate release:

- **Export**;
- **Publication**.

This subgroup determines whether either Concept requires Competition, Outcome Declaration, or the other Concept for its intended MUDAC application role, and distinguishes external representation, release authority, public disclosure, and transport/delivery.

The central separation remains:

```text
source authority
  != Export representation
  != Publication release
  != transport/delivery
```

and:

```text
official != public
```

# Decision summary

**PASS — externalization dependence resolved with one new direct edge.**

012-G accepts:

```text
Publication → Export
```

012-G rejects the reverse edge and rejects fixed source-authority edges from Export/Publication:

```text
Export      ↛ Publication
Export      ↛ Competition
Export      ↛ Outcome Declaration
Export      ↛ Award

Publication ↛ Competition
Publication ↛ Outcome Declaration
Publication ↛ Award
```

Outcome Declaration also remains independent of externalization:

```text
Outcome Declaration ↛ Export
Outcome Declaration ↛ Publication
```

The current full product may compose all three layers, but the dependence graph does not collapse them.

# 1. Incoming authority

012-F establishes:

```text
Outcome Declaration → Competition
```

and preserves:

```text
calculated != recognized != official
```

Phase 011-H establishes the representation/release composition:

```text
source authority
  ↓
Export representation + currency
  ↓ explicit release only
Publication distribution authority
  ↓
transport/delivery realization
```

012-G now asks which of those arrows are inclusion dependencies rather than synchronization.

# 2. Export application role

Export owns a stable external representation of an exact supplied SourceBasis under an explicit RepresentationProfile and AudienceProfile.

Its role is meaningful without Publication because MUDAC may need representations for:

- printing;
- download;
- review/preview;
- internal handoff;
- judging material;
- competition setup material;
- provisional/calculated information;
- official outcome representation;
- historical retrieval.

Generation does not imply release.

# 3. Export has no fixed source-Concept dependency

## 3.1 Export ↛ Outcome Declaration

**Decision: reject universal edge.**

Export may represent an Outcome Declaration, but it may also represent non-official material.

Therefore:

```text
Export ↛ Outcome Declaration
```

Official-result export is a capability profile, not Export's only application role.

## 3.2 Export ↛ Competition

**Decision: reject universal direct edge.**

Most in-scope MUDAC exports are competition-scoped, but Export itself remains meaningful for reusable or preparation material such as a Rubric representation.

The repository-level family rule still says every **adopted in-scope MUDAC product variant** retains Competition. That scope rule does not require a redundant direct edge from every optional capability to Competition.

Therefore:

```text
Export ↛ Competition
```

## 3.3 Export ↛ Award

**Decision: reject universal edge.**

Award state may be represented when relevant, but Export can serve many roles without Award.

# 4. Export ↛ Publication

<a id="dep-g-001"></a>
## DEP-G-001 — Representation does not require release

```text
Export ↛ Publication
```

A stable representation remains useful when it is never deliberately released.

Examples include:

- generated Judge material awaiting controlled use;
- Organizer review copy;
- printable continuity material;
- internal archival representation;
- public-safe artifact prepared before ceremony release;
- replacement Export prepared while existing Publication remains unchanged.

This preserves:

```text
generated != published
```

and prevents release authority from being inferred from artifact existence.

# 5. Publication application role

Publication owns deliberate release of an exact representation to an Audience/Channel under PublishingAuthority.

Publication does not own rendering, representation fidelity, source authority, or transport delivery.

Its application role is meaningful only when there is a stable representation to release.

# 6. Publication → Export

<a id="dep-g-002"></a>
## DEP-G-002 — Publication requires Export in the MUDAC application family

```text
Publication → Export
```

Publication is intrinsically generic over a supplied Representation, so this is not intrinsic Concept coupling.

Within the MUDAC application family, however, **Export is the only current Concept that owns stable external representation identity, exact SourceBasis, purpose/audience representation contract, and representation currency**.

No other current Concept can replace that role without either:

- duplicating Export semantics; or
- allowing Publication to release an unowned/unstable representation.

Therefore any coherent MUDAC subset containing Publication also contains Export.

This is the one direct edge added by 012-G.

# 7. Publication has no fixed source-authority edge

## 7.1 Publication ↛ Outcome Declaration

**Decision: reject universal edge.**

Publication can release non-official material when disclosure policy and publishing authority permit it.

Examples include:

- public event information;
- ceremony-safe non-result material;
- a reusable/public Rubric representation;
- other approved competition representations that do not claim official outcome authority.

Therefore:

```text
Publication ↛ Outcome Declaration
```

A **public official-result release** does require Outcome Declaration, but that is a capability-conditioned rule below.

## 7.2 Publication ↛ Competition

**Decision: reject universal direct edge.**

`Publication → Export` supplies the representation role. The current family-level scope rule separately keeps Competition in adopted MUDAC variants.

A direct `Publication → Competition` edge would conflate adopted product scope with Publication's representation/release role and would also block coherent reusable-material counterexamples.

## 7.3 Publication ↛ Award

Award state can be part of a published representation but is not universally required.

# 8. Outcome Declaration does not require externalization

<a id="dep-g-003"></a>
## DEP-G-003 — Official authority may remain non-public

```text
Outcome Declaration ↛ Export
Outcome Declaration ↛ Publication
```

A Competition may have a current official Outcome Declaration while:

- no external representation has yet been generated;
- a representation exists but release is delayed;
- publication is intentionally withheld;
- disclosure policy prevents ordinary public release.

This preserves:

```text
official != public
```

and keeps official authority independent from representation/distribution state.

# 9. External representation capability

<a id="dep-g-004"></a>
## DEP-G-004 — Export requires a valid exact SourceBasis, not one fixed Concept bundle

Any meaningful Export capability requires:

```text
Export
+ exact reconstructible SourceBasis
+ RepresentationProfile / purpose
+ AudienceProfile / disclosure class
```

But `SourceBasis` is alternative/variant-specific.

Examples can include:

- Competition/setup state;
- Rubric/evaluation material;
- Team/Division/Alias-safe judging material;
- calculated/provisional result state;
- Award state;
- Outcome Declaration;
- historical source state.

Therefore no one source Concept becomes a universal Export dependency.

# 10. Public official-result release

<a id="dep-g-005"></a>
## DEP-G-005 — Public official-result release is a capability-conditioned composition

A variant claiming ordinary **public official-result release** requires:

```text
Outcome Declaration
+ Export
+ Publication
```

with:

- a Current or otherwise legitimately releasable official Outcome Declaration under applicable policy;
- an Export bound to the exact official SourceBasis and appropriate Public/Ceremony AudienceProfile;
- explicit Publication authority for the selected Audience/Channel.

Because `Outcome Declaration → Competition` and `Publication → Export` are already current edges, do not duplicate those transitive/context relationships unnecessarily.

This capability rule is not:

```text
Outcome Declaration → Publication
```

and not:

```text
Publication → Outcome Declaration
```

because official-but-non-public and public-non-official representations are both coherent.

# 11. Publication successor/correction capability

<a id="dep-g-006"></a>
## DEP-G-006 — Corrected release requires a successor/current Export before successor Publication

When source authority changes materially:

```text
source correction
  → existing Export Affected/Stale/revalidated
  → if newer source must be represented: new Export
  → explicit Publication leave / withdraw / supersede decision
```

A corrected/current release cannot silently retarget the historical Publication.

If replacement release is required:

```text
successor/current Export
+ Publication successor action
```

are required.

This is composition/capability behavior, not an additional direct graph edge beyond `Publication → Export`.

# 12. Export currency does not create Publication state

Current Export states such as:

```text
Current
Affected
Stale
Superseded
Retired
```

are representation-currentness meanings.

Publication states such as:

```text
Published
Withdrawn
Superseded
```

are release/distribution meanings.

Neither state family determines the other automatically.

Therefore correction does not create a hidden dependency such as:

```text
Export affected → Publication must exist
```

or:

```text
Publication published → Export must remain Current forever
```

# 13. Paper continuity is not Export dependence

<a id="dep-g-007"></a>
## DEP-G-007 — Paper capture continuity does not universally require Export

The current continuity model treats paper as an alternate capture/source channel over the same evaluation semantics.

Therefore:

```text
Paper Evaluation Continuity
  ↛ Export as a universal Concept requirement
```

Export is required when the application needs a **stable printable/external representation** such as a prepared packet or form.

But retained physical Judge evidence and later verified transcription are source/capture semantics owned by Scorecard/Provenance/Versioning composition, not by Export merely because paper is involved.

This prevents “paper support” from forcing Export into every judging subset.

# 14. Transport/delivery remains outside Concept dependence

Publication means authorized release, not successful transport or recipient viewing.

Do not introduce:

- Delivery;
- Channel Delivery;
- File Transfer;
- Print Job;
- Email Dispatch;
- CDN Propagation;
- Receipt;
- Distribution Workflow

as Concept graph vertices merely to explain delivery mechanics.

Those remain downstream realization concerns unless later Concept evidence establishes an independent user-purpose owner.

# 15. Representative dependence-valid externalization subsets

## Export-only representation

```text
Export + a valid SourceBasis capability
without Publication
```

Coherent for internal/download/print/preview representation.

## Publication capability

```text
Publication + Export + a valid releasable SourceBasis capability
```

Dependence-valid because Publication includes Export.

## Official but non-public

```text
Competition + Outcome Declaration
without Export
without Publication
```

Coherent at the dependence level.

## Official representation prepared but unreleased

```text
Competition + Outcome Declaration + Export
without Publication
```

Coherent and explicitly supported by Phase-011 separation.

## Public official-result release

```text
Competition + Outcome Declaration + Export + Publication
```

plus applicable disclosure/publishing authority and reconstructible source basis.

## Public non-official material

```text
Export + Publication
without Outcome Declaration
```

Coherent when the Export SourceBasis and disclosure policy legitimately support the public claim being made.

Scope adoption of these variants belongs to 012-I.

# 16. Invalid externalization claims

```text
Publication without Export
```

is invalid in the current MUDAC family.

Capability-level invalid claims include:

```text
Export without a valid exact SourceBasis
Publication without an exact releasable Export
public official-result release without Outcome Declaration
public official-result release without a public/ceremony-safe Export
public release without legitimate publishing authority
Publication treated as proof of delivery
Export generation treated as Publication
```

# 17. No new Concept or upstream reopening

012-G finds no evidence that Export and Publication should merge.

Their purposes remain distinct:

```text
Export      = stable source-bound representation + currency
Publication = deliberate release + distribution history
```

`Publication → Export` is contextual co-inclusion, not intrinsic specification dependence.

No new Representation, Artifact, Document, Release, Delivery, Distribution, Public Result, or Disclosure Concept is justified.

No Phase-010 reopening is required.

# 18. Composition boundary

Phase-011 composition remains authoritative:

- Generate Export;
- Export Affected/Stale/revalidation/supersession;
- Publish Representation;
- Withdraw Publication;
- Publish Successor Representation;
- source correction never auto-withdraws or auto-republishes;
- official declaration never auto-publishes.

012-G states **which Concepts/capabilities must be co-included**. It does not redefine those synchronizations.

No immediate Phase-011 repair is required.

# 19. Carry-forward to 012-H / 012-I

012-H should now analyze the whole dependence model with externalization included and test:

- whether `Publication → Export` creates any unexpected transitive/co-inclusion effect;
- minimal meaningful subsets;
- official-but-non-public and public-non-official counterexamples;
- whether any other apparent cycles remain after all concept families are resolved;
- whether capability-conditioned rules interact coherently with the direct graph.

012-I must later decide which dependence-valid externalization variants are actually in scope.

Scope/composition carry-forwards include:

1. official-but-non-public operation is dependence-coherent;
2. Export-without-Publication is dependence-coherent;
3. Publication-without-Outcome-Declaration is dependence-coherent for legitimate non-official material;
4. Publication-without-Export is invalid in MUDAC;
5. paper capture continuity does not automatically require Export;
6. public official-result release requires Outcome Declaration + Export + Publication;
7. transport/delivery remains downstream realization.

# Exit decision

**PASS.**

012-G resolves the remaining concept-family dependence questions without intrinsic coupling, hidden coordinator Concepts, or implementation contamination.

The direct graph gains exactly one edge:

```text
Publication → Export
```

The next dependency-safe subgroup is:

> **012-H — Whole-Graph Transitivity, Co-Inclusion, Optionality & Minimal/Unfamiliar Subsets**

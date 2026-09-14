---
type: Concept Composition Revalidation
title: 011-H — Export, Publication, Representation Currency & Release Composition
description: "Establishes current MUDAC composition for source-bound Export generation and currency, audience/disclosure validation, explicit Publication release/withdrawal/succession, and non-destructive correction of already released representations without conflating official authority, representation, publication, or transport delivery."
status: stable
tags: [phase-011, composition, export, publication, representation, currency, release, disclosure, historical-truth]
sources:
  - resource: 011-A-composition-scope-evidence-reuse-synchronization-risk-subphase-planning.md
  - resource: 011-B-legacy-synchronization-inventory-composition-obligation-map-application-action-baseline.md
  - resource: 011-F-temporal-correction-invalidation-replacement-successor-work-affected-state-propagation.md
  - resource: 011-G-coverage-aggregate-rank-award-competition-finalization-outcome-declaration-composition.md
  - resource: ../canonical/concepts/export.md
  - resource: ../canonical/concepts/publication.md
  - resource: ../canonical/concepts/outcome-declaration.md
  - resource: ../canonical/policies/anonymity-disclosure.md
  - resource: ../canonical/policies/correction-authority.md
  - resource: ../canonical/invariants/official-not-automatically-public.md
  - resource: ../002-concept-specification/002-H-export-print-operational-continuity-external-representations.md
  - resource: ../canonical/synchronizations/temporal-truth-correction.md
  - resource: ../canonical/synchronizations/evaluation-outcome-finalization-declaration.md
  - resource: https://github.com/SethDKelly/Base/blob/main/docs/phases/005/composition-synchronization-contract.md
generated: { by: openai/gpt-5.6-sol, at: 2026-09-14T16:49:00-05:00 }
---

# Purpose

Establish how MUDAC externalizes current or explicitly historical source information and deliberately releases representations without allowing formatting, generation, distribution, transport or later correction to steal authority from the source Concepts they represent.

011-H consumes the temporal and official-outcome semantics established by 011-F/G. In particular:

- source correction never rewrites historical source authority;
- an Outcome Declaration may be `Current`, `Affected` or `Superseded` independently from Publication;
- official authority does not imply public release;
- dependent state must preserve owner-specific currentness rather than use a generic destructive cascade;
- already released physical/digital representations remain historical facts even after withdrawal or successor release.

011-H answers:

1. What exact source and disclosure context must an Export bind?
2. When is an Export `Current`, `Affected`, `Stale`, `Superseded` or `Retired`?
3. How is an Affected Export revalidated without rewriting its historical SourceBasis?
4. How does a new Export supersede an older representation without implying anything about Publication state?
5. What prerequisites must hold before MUDAC may publish a representation?
6. How do Publication `Published`, `Withdrawn` and `Superseded` remain distinct from Export currency?
7. What happens when the source of an already-published Export becomes affected or is corrected?
8. How are successor public materials released without retargeting the historical Publication?
9. How do physical copies, files, URLs and transport delivery remain historical/realization facts rather than semantic authority?
10. Which Export/Publication actions are direct, coordinated, system-triggered or composition-only in MUDAC?

# Decision summary

**PASS — 011-H is complete.**

No new `Document`, `Artifact`, `Release`, `Public Result`, `Delivery`, `Channel`, `Distribution`, `Disclosure`, `Representation Version`, or workflow Concept is required.

The existing Export and Publication Concepts are sufficient when application composition preserves these rules:

1. **Export is a stable representation of one exact SourceBasis for one declared purpose and AudienceProfile.** Generation never promotes source authority.
2. **Export disclosure is least-authority and audience-specific.** The generating actor's broad Access never implies that all information they can see may appear in the representation.
3. **Export currency is source-relative, not distribution state.** `Current`, `Affected`, `Stale`, `Superseded`, and `Retired` do not mean Published/Withdrawn.
4. **Affected means review is required, not known-wrong.** Existing `validateRepresentation` is the revalidation action and may reconfirm the same Export as Current only if the unchanged exact SourceBasis and representation contract remain applicable.
5. **Stale means known not to reflect the applicable current basis for the representation's intended current use.** Historical fidelity to the old source may still be perfect.
6. **A successor Export is a new stable representation.** `supersedeBy` links old to new; it never rewrites the predecessor's SourceBasis or Publication history.
7. **Generating an Export never publishes it.** Publication requires an explicit `publish` action under legitimate publishing/disclosure authority.
8. **Publication binds one exact Representation, Audience and Channel.** Later source or Export changes never retarget the historical Publication.
9. **Withdrawal ends current release authority without erasing that release occurred or proving every distributed copy disappeared.**
10. **Successor release is explicit.** A corrected/current successor Export must exist first; then a successor Publication may explicitly supersede the prior Publication.
11. **Source correction never automatically withdraws or republishes.** It may make an Export Affected/Stale and require release review, but Publication authority changes only through Publication actions.
12. **Official != public != delivered.** Outcome Declaration establishes official authority, Publication establishes deliberate release, and transport/delivery success remains downstream realization.

Durable current composition is promoted to [External Representation, Currency & Publication Release Composition](../canonical/synchronizations/external-representation-publication-release.md).

# Scope ownership

011-H closes:

- legacy synchronization 15 — Export representation to explicit Publication release;
- legacy synchronization 12's Export/Publication correction and affectedness consequences;
- CO-11 — external representation and release;
- the 011-B provisional action-surface decisions for Export and Publication;
- 011-F/G carry-forward for source correction → representation currency → explicit release consequence;
- the representation/release half of `official != public`.

011-H does **not** close:

- whole-application action exposure/chaining/cycle/automation coherence — 011-I;
- canonical Phase 011 corpus reconciliation — 011-J;
- inclusion/dependence such as whether every MUDAC Publication variant requires Export — Phase 012;
- UI/download/print/share interaction mapping — Phase 013;
- PDF/file/QR layout, storage, CDN, delivery, printing, transport or offline architecture;
- retention policy for every distributed physical copy or external recipient.

# 1. Representation source authority

An Export must bind an exact, reconstructible `SourceBasis`.

The source may be, for example:

- a specific authoritative Rubric Version;
- current Panel/Competition operational information at a defined point;
- a working/draft source explicitly represented as working/draft;
- a current Outcome Declaration;
- an Affected or Superseded declaration when the purpose is explicitly historical/audit representation rather than ordinary current public result;
- another supplied source state whose authority class is explicit enough for the representation purpose.

The Export never owns or upgrades the source's semantic authority.

Therefore:

```text
working source → working-labelled Export
current authoritative source → authoritative representation
Outcome Declaration → official-result representation
```

but:

```text
Export generation != source becomes authoritative
Export label       != source becomes official
Publication        != source becomes correct/current
```

# 2. Representation contract and disclosure

MUDAC's representation contract combines:

```text
exact SourceBasis
+ RepresentationProfile / purpose
+ AudienceProfile / disclosure class
```

`validateRepresentation` must establish that the representation is semantically faithful enough for its declared purpose and reveals no information outside the applicable audience/disclosure rules.

Examples include:

- Judge-safe;
- Organizer-sensitive;
- Ceremony-safe;
- Public;
- explicit archival/historical profiles where appropriate.

The generating actor's own Access is not the disclosure ceiling.

An Organizer who may inspect sensitive Team identity, Judge Notes or exception history does not gain authority to include those facts in a public or Judge-safe Export.

Disclosure applies to visible body content and material incidental representation surfaces such as labels/metadata or machine-readable encodings. Exact physical/file realization remains downstream.

# 3. Generate Export

Application action: **Generate Export**.

Concept participants:

- `Export.request`;
- `Export.validateRepresentation`;
- `Export.generate`.

Conditions include:

- exact SourceBasis is resolvable and permitted for the requested purpose;
- source authority/currentness is represented truthfully;
- RepresentationProfile is defined enough to evaluate semantic fidelity;
- AudienceProfile/disclosure class is explicit;
- current Access/authority permits requesting the representation;
- disclosure policy permits the selected fields/meaning for the AudienceProfile;
- generated representation cannot be reasonably mistaken for a stronger authority class than its SourceBasis.

Semantic success establishes one stable Export with:

- immutable identity of the represented SourceBasis;
- declared representation purpose/profile;
- intended AudienceProfile;
- generation time;
- generated representation reference;
- initial currency `Current` relative to the supplied basis/purpose at generation.

This is a conceptual application action, not a prescribed file renderer, storage transaction or download mechanism.

# 4. Export Current

An Export is `Current` when, for its declared purpose and audience:

- its exact SourceBasis remains the applicable source basis or remains explicitly valid for that use;
- the representation faithfully reflects that SourceBasis;
- applicable disclosure rules remain satisfied;
- no known source/currentness change makes the representation misleading for ordinary current use.

Current does not mean:

- published;
- publicly visible;
- officially declared unless its SourceBasis has that authority;
- delivered to anyone;
- the newest file by timestamp alone.

# 5. Export Affected

Application reaction: **Identify Export Affected**.

Participant:

- `Export.markAffected`.

Use when a material dependency of the representation changes such that review/reconfirmation is required, but the application has not yet established that the Export is unusable for its intended current purpose.

Examples:

- an Outcome Declaration represented by the Export becomes `Affected`;
- source correction changes a fact included in or potentially material to the representation;
- a disclosure classification changes and the Export requires review;
- an operational source relation changes and applicability is uncertain.

Affected means:

```text
review required
!= known wrong
!= withdrawn
!= unpublished
```

The Export's SourceBasis remains unchanged.

# 6. Revalidate an Affected Export

011-H clarifies the existing Export action `validateRepresentation` as the owner-safe revalidation action.

Application action/reaction: **Revalidate Export**.

Participant:

- `Export.validateRepresentation`.

For an Affected Export, revalidation compares the unchanged Export/SourceBasis/representation contract against the currently applicable purpose/disclosure context.

Possible semantic outcomes:

### Reconfirmed Current

Permitted only when the Export remains truthful and applicable for the intended current use without changing its historical SourceBasis or represented content.

This is a currency/currentness conclusion, not a rewrite.

### Stale

If the Export is known not to represent the applicable current basis for its intended current use, invoke `Export.markStale`.

### Successor required

If current use requires a new representation of newer/corrected source state, generate a distinct Export from that new SourceBasis and then use `Export.supersedeBy` where the relationship is semantically appropriate.

Revalidation cannot mutate an old Export so that it appears to have represented a different source at generation time.

# 7. Export Stale

Application reaction: **Identify Export Stale**.

Participant:

- `Export.markStale`.

`Stale` means the Export is known not to reflect the applicable current SourceBasis for its intended ordinary current use.

A Stale Export may still be a perfectly accurate historical representation of the source it actually bound.

Example:

```text
Outcome Declaration D1 Current
  → Export E1 Current

D1 becomes Affected and later D2 is confirmed Current
  → E1 no longer represents current official outcome
  → E1 Stale for current-result use
```

Stale is not deletion, withdrawal, publication state or historical falsity.

# 8. Export successor and supersession

Application action: **Generate Successor Export**.

Participants:

- a new `Generate Export` action over the new exact SourceBasis;
- predecessor `Export.supersedeBy(successor)`.

Conditions:

- successor representation is independently valid for its SourceBasis/purpose/audience;
- predecessor/successor serve a semantically comparable purpose such that explicit supersession is meaningful;
- predecessor historical SourceBasis remains retained.

Postconditions:

- successor Export is its own stable representation;
- predecessor becomes `Superseded` for that ordinary use;
- predecessor remains retrievable/history-preserving where policy allows;
- no Publication is automatically created, withdrawn or superseded.

Not every new Export must supersede every older Export. Different purposes/audiences may legitimately coexist.

# 9. Export retirement

`Export.retireFromOrdinaryUse` removes a representation from ordinary current use for an attributable reason without pretending it never existed.

Retirement may be appropriate when:

- the representation is no longer operationally useful;
- policy no longer permits routine reuse;
- a historical artifact must remain preserved but should not be selected for new ordinary distribution.

Retiring an Export does not withdraw a Publication that already released it. Publication must be handled explicitly.

# 10. Publication prerequisites

Publication is deliberate release authority over an exact Representation.

For ordinary MUDAC publication of an Export, prerequisites include:

- exact Export identity is selected;
- Export's RepresentationProfile and AudienceProfile are compatible with the intended Publication Audience/Channel;
- Export is suitable for the intended release purpose under current currency/source authority;
- applicable disclosure policy permits the release;
- current publishing authority is legitimate;
- source semantics are not promoted by release wording or context;
- no current condition known to make the representation misleading for the intended release remains unresolved.

For ordinary publication of official competition results, the Export should be based on the current Outcome Declaration and be `Current` for the intended public/ceremony profile.

An Affected official declaration remains official, but ordinary new publication that would present it as uncomplicated current result is blocked unless explicit governing authority/policy permits a clearly qualified release. 011-H does not invent a generic exception that erases the affected state.

# 11. Publish Representation

Application action: **Publish Representation**.

Participant:

- `Publication.publish`.

Supplied bindings:

- exact Representation = selected Export;
- Audience;
- Channel/destination meaning;
- PublishingAuthority.

Semantic success establishes one Publication in `Published` state tied to that exact Export.

It does not:

- make the Export Current if it was not;
- make the SourceBasis official if it was not;
- change Outcome Declaration;
- imply every intended recipient successfully received the representation;
- change transport/delivery infrastructure state.

# 12. Export generation is not Publication

The following may all exist without public release:

- a current official Outcome Declaration;
- a ceremony-safe/public-safe Export;
- a generated file/artifact reference.

Publication exists only after an explicit release action.

This supports legitimate sequences such as:

```text
Competition Finalized + Outcome Declaration Current
  → Generate public-safe Export
  → review/hold
  → ceremony occurs later
  → Publish Representation
```

No automatic declaration → publication synchronization is accepted.

# 13. Publication state is independent from Export currency

A Publication may remain historically `Published` even if its bound Export later becomes Affected or Stale.

This means:

```text
Publication state = Published
Export currency   = Stale
```

can coexist until an authorized release action changes Publication state.

That is not a contradiction. It truthfully records that an older/stale representation remains or remained released.

The application may surface a high-consequence review requirement, but it may not silently rewrite Publication history.

# 14. Source correction after publication

When a bound source changes materially:

1. source owner changes first under 011-F/G authority;
2. affected Export dependencies are identified;
3. relevant Export becomes `Affected` or `Stale` according to actual basis impact;
4. the existing Publication remains historically attributable to the exact Export it released;
5. governing authority determines whether to leave, withdraw, or supersede the release;
6. if corrected current release is required, generate a new Export from corrected/current source first;
7. explicitly publish/supersede through Publication authority.

There is no automatic source correction → withdraw → regenerate → republish workflow contract.

# 15. Withdraw Publication

Application action: **Withdraw Publication**.

Participant:

- `Publication.withdraw`.

Conditions include:

- Publication is currently Published;
- actor has legitimate publishing/withdrawal authority;
- reason is attributable where material.

Postconditions:

- Publication becomes `Withdrawn`;
- historical record of what was released, to which Audience/Channel, and when remains;
- bound Export is unchanged;
- SourceBasis is unchanged;
- already distributed physical/digital copies are not represented as erased.

Withdrawal means MUDAC no longer authorizes that Publication as a current release. It is not retroactive deletion.

# 16. Successor Publication

Application action: **Publish Successor Representation**.

Participants:

- a selected successor Export already generated and validated;
- `Publication.supersedeWith` using a new successor Publication bound to that exact successor Export.

Conditions include:

- predecessor Publication is identifiable;
- successor Export is suitable/current for the intended Audience/Channel and release purpose;
- publishing authority explicitly chooses successor release;
- disclosure prerequisites are satisfied;
- predecessor/successor relationship is semantically meaningful.

Postconditions:

- successor Publication becomes `Published`;
- predecessor Publication becomes `Superseded`;
- predecessor remains historical evidence of what was released;
- successor Publication points to the new exact Export;
- no historical Publication is retargeted to the new Export.

A successor Export does not automatically imply successor Publication. Release remains deliberate.

# 17. Published physical/external copies

Publication authority cannot guarantee remote deletion of already distributed physical pages, screenshots, downloaded files, copied URLs, or downstream external copies.

Therefore MUDAC distinguishes:

```text
current publication authority
from
historical fact of prior external release
```

Withdrawal/supersession changes MUDAC's current release authority and discoverability obligations. It cannot make the prior exposure not have happened.

Where continued possession or external caching has security/privacy implications, those are factual consequences for later risk/experience/architecture work; Publication history remains truthful.

# 18. Transport and delivery are not Publication authority

Publication answers:

> Did an authorized actor deliberately release this exact Representation to this declared Audience/Channel?

It does not answer:

- whether every email arrived;
- whether every browser/CDN node updated;
- whether every printer succeeded;
- whether every physical handout was collected;
- whether a third-party platform cached content;
- whether every recipient actually viewed the material.

Those are transport/delivery/realization concerns unless a future product requirement establishes independent semantic meaning.

No Delivery concept or transport synchronization is added in 011-H.

# 19. Official result publication

For ordinary public/ceremony official-result release:

```text
current Outcome Declaration
  → public/ceremony-safe Export bound to that declaration
  → explicit Publication
```

The Export may summarize or format the declared outcome, but it must not:

- introduce recipients/placements not supported by the declaration basis;
- convert calculated but undeclared state into official result;
- expose private Scorecards/Judge Notes by default;
- expose protected Team identity beyond the applicable disclosure policy;
- hide material affectedness when policy requires qualification.

Outcome Declaration remains official authority. Export remains representation. Publication remains release.

# 20. Operational/working material publication

Publication is not limited to official outcomes.

MUDAC may deliberately distribute representations such as:

- Judge-safe Rubric/forms;
- event instructions;
- Panel operational material;
- Organizer-sensitive archives;
- explicitly draft/review material to an appropriate limited Audience.

The representation must truthfully carry the source authority class appropriate to its purpose. Publication cannot turn Draft into Authoritative or Organizer-sensitive into Public-safe merely through release.

# 21. Mixed currency and distribution examples

Legitimate combinations include:

```text
Export Current      + no Publication
Export Current      + Publication Published
Export Affected     + Publication Published
Export Stale        + Publication Published
Export Superseded   + Publication Superseded
Export Retired      + historical Publication Withdrawn
```

These combinations demonstrate why one universal release/currentness status would be incorrect.

# 22. Action-surface decisions

| Action family | Current MUDAC status after 011-H |
| --- | --- |
| Export `request` | direct request candidate |
| Export `validateRepresentation` | composition participant; also revalidation owner for Affected Export |
| Export `generate` | coordinated `Generate Export` application action |
| Export `markAffected` | system/composition reaction after verified dependency change |
| Export `markStale` | system/composition reaction after current-use mismatch is established |
| Export `supersedeBy` | composition-only within successor Export establishment |
| Export `retireFromOrdinaryUse` | controlled direct administrative action |
| Publication `publish` | controlled explicit release action |
| Publication `withdraw` | controlled high-consequence release action |
| Publication `supersedeWith` | coordinated explicit successor release action |
| declaration → automatic publication | intentionally unavailable |
| source correction → automatic withdrawal/republication | intentionally unavailable |
| transport/delivery result as publication state | intentionally unavailable |

011-I will perform final whole-application exposure closure.

# 23. Over-synchronization checks

011-H rejects:

- treating any generated Export as automatically Published;
- automatically publishing when Competition Finalizes or Outcome Declaration becomes Current;
- rewriting an old Export's SourceBasis after source correction;
- automatically withdrawing Publication because Export becomes Affected or Stale;
- automatically publishing a successor because a successor Export exists;
- using Publication to upgrade working/calculated information into official authority;
- requiring every Export to be public-safe when its declared Audience is legitimately narrower;
- treating source actor Access as disclosure authorization for artifact contents;
- treating successful file generation/URL creation/print completion as Publication authority;
- treating withdrawal as proof distributed copies disappeared;
- collapsing Export currency and Publication distribution into one status.

# 24. Under-synchronization checks

011-H requires explicit handling for:

- exact source basis on each meaningful Export;
- audience/disclosure validation before generation/release;
- source changes that affect representation currency;
- a way to revalidate Affected Export without destructive rewrite;
- Stale representation detection for current-use selection;
- explicit successor Export relation where replacement is meaningful;
- explicit Publication release rather than generation side effect;
- explicit withdrawal/successor Publication after correction where governing authority requires it;
- historical record of previously released representations;
- official-result publication that remains bound to explicit Outcome Declaration authority.

# 25. Chaining and cycle pressure test

Representative chains are directional:

```text
exact source + purpose + audience
  → Generate Export
  → Export Current
  → optional explicit Publish Representation
  → Publication Published
```

```text
source correction
  → Export Affected
  → Revalidate Export
      → Current
      OR Stale
      OR Generate Successor Export
```

```text
Outcome Declaration D1 Current
  → Export E1 Current
  → Publication P1 Published

D1 Affected / successor D2 later Current
  → E1 Affected/Stale
  → E2 generated from D2
  → explicit Publish Successor Representation
  → P1 Superseded + P2 Published
```

No Publication action writes backward into Outcome Declaration or Export SourceBasis. No Export currency transition writes backward into source authority. No semantic cycle or hidden Release/Artifact coordinator is required.

# 26. Upstream-boundary audit

011-H finds the Phase 010 Export and Publication boundaries fundamentally sound.

One composition-facing clarification is required for Export: because `Affected` means review/reconfirmation rather than known-wrong, existing `validateRepresentation` must own revalidation of an Affected representation and may reconfirm it as `Current` when the unchanged exact SourceBasis and representation contract remain legitimately applicable. This is a clarification of an existing action/state relationship, not a new Concept or expanded Export purpose.

No Export SourceBasis may be changed during that revalidation. If newer/corrected source must be represented, a new Export is required.

Publication needs no boundary change.

# 27. Legacy-contract disposition after 011-H

Current Phase 011 authority now replaces/reframes:

- legacy 15 — Export generation/representation → deliberate Publication release;
- legacy 12's Export currency and Publication consequence portion after source correction.

With 011-H, the semantic families of legacy contracts 01–16 have all received current Phase 011 owners. 011-I now owns the whole-application action-surface/chaining/automation/over-under/authority/synergy closure, and 011-J owns canonical consolidation.

# 28. Exit test

011-H passes because:

- each Export has exact source/purpose/audience meaning;
- disclosure validation remains audience-specific and least-authority;
- Export currency remains distinct from Publication state;
- Affected versus Stale versus Superseded versus Retired are non-destructive and meaningful;
- Affected Export can be revalidated without rewriting historical basis;
- successor representation requires a new Export;
- Export generation cannot imply Publication;
- Publication release is explicit and source-authority-preserving;
- source correction cannot silently retarget historical release;
- withdrawal/supersession preserve historical external truth;
- official, public and delivered remain separate meanings;
- physical/external persistence does not force false deletion semantics;
- no new Release/Artifact/Delivery/Disclosure workflow concept is required;
- no hidden runtime transport/queue/storage mechanism enters Concept Design;
- 011-I receives a complete family-level synchronization surface for whole-composition closure.

# Decision

**PASS — 011-H is complete.**

# Handoff

Proceed to:

> **011-I — Application Action Surface, Chaining, Automation, Over/Under-Synchronization, Authority & Synergy Closure**

011-I must now consume all current family owners from 011-C through 011-H, finalize direct/coordinated/composition-only/system-triggered/intentionally-unavailable action exposure, trace material chains, detect hidden cycles or authority transfer, pressure-test over/under-synchronization and retain only purposeful automation/synergy claims before 011-J canonical reconciliation.
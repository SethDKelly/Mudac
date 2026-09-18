---
type: Phase Design Record
title: 013-I — Export, Publication, Audience Disclosure, External Recipient & Representation/Release Mapping
description: "Maps exact-source external representation, audience/disclosure-safe Export generation, representation currentness, deliberate Publication release, withdrawal/succession and external-recipient meaning without collapsing source authority, officiality, representation, release or delivery."
status: stable
tags: [phase-013, jackson, mapping, export, publication, disclosure, audience, release, external-recipient, currency]
sources:
  - resource: 013-H-award-competition-finalization-outcome-declaration-officiality-successor-authority-mapping.md
  - resource: ../canonical/experience/mapping-authority-baseline.md
  - resource: ../canonical/experience/outcome-officiality.md
  - resource: ../canonical/experience/paper-export-publication.md
  - resource: ../canonical/concepts/export.md
  - resource: ../canonical/concepts/publication.md
  - resource: ../canonical/concepts/outcome-declaration.md
  - resource: ../canonical/synchronizations/external-representation-publication-release.md
  - resource: ../canonical/policies/anonymity-disclosure.md
  - resource: ../canonical/invariants/official-not-automatically-public.md
  - resource: ../canonical/invariants/current-vs-historical-truth.md
---

# Purpose

Map how MUDAC turns an identified source basis into an audience-specific external representation and, only through a separate explicit authority act, releases that exact representation to an external audience/channel.

013-I defines user-visible semantics for:

- Export as stable representation of an exact SourceBasis;
- representation purpose and AudienceProfile;
- least-disclosure / audience-specific representation;
- Export validation and generation;
- Export currency: Current, Affected, Stale, Superseded and Retired;
- revalidation without historical source rewrite;
- Publication as deliberate release of an exact representation;
- audience/channel/publishing authority;
- official-but-non-public operation;
- Publication withdrawal and successor release;
- historical release persistence after correction/withdrawal;
- external-recipient possession versus current Publication authority;
- distinction between release and downstream transport/delivery.

013-I stops before cross-cutting accessibility/degraded-operation/status/recovery mapping, which belongs to 013-J.

It does not prescribe PDF engines, report layouts, print drivers, QR implementations, blob/file storage, CDN behavior, email/SMS systems, transport retry, recipient analytics, caching, browser behavior or frontend architecture.

# Decision

**COMPLETE — PASS. Proceed to 013-J.**

```text
013-A START GATE                                   COMPLETE — READY
013-B AUTHORITY / CORPUS BASELINE                 COMPLETE — PASS
013-C CONTEXT / JUDGE ENTRY MAPPING               COMPLETE — PASS
013-D ORGANIZER PREPARATION MAPPING               COMPLETE — PASS
013-E ACTIVE EVALUATION MAPPING                   COMPLETE — PASS
013-F AUTHORITY / CORRECTION MAPPING              COMPLETE — PASS
013-G LIVE OPS / RECONCILIATION MAPPING           COMPLETE — PASS
013-H AWARD / OFFICIALITY MAPPING                 COMPLETE — PASS
013-I REPRESENTATION / RELEASE MAPPING             COMPLETE — PASS
EXTERNAL-REPRESENTATION OWNER CREATED              YES
SOURCE AUTHORITY == EXPORT                         PROHIBITED
EXPORT GENERATED == PUBLICATION                    PROHIBITED
ACTOR ACCESS == AUDIENCE DISCLOSURE                PROHIBITED
EXPORT CURRENT == OFFICIAL                         PROHIBITED
PUBLICATION == DELIVERY                            PROHIBITED
SOURCE CORRECTION REWRITES OLD EXPORT              PROHIBITED
SOURCE CORRECTION AUTO-WITHDRAWS PUBLICATION       PROHIBITED
SUCCESSOR OUTCOME AUTO-REPUBLISHES                 PROHIBITED
WITHDRAWAL ERASES HISTORICAL RELEASE               PROHIBITED
EXTERNAL COPY POSSESSION == CURRENT RELEASE        PROHIBITED
PHASE-010 REOPEN REQUIRED                          NO
PHASE-011 REOPEN REQUIRED                          NO
PHASE-012 REOPEN REQUIRED                          NO
NEXT                                                013-J
ARCHITECTURE / IMPLEMENTATION                      SUSPENDED
```

# 1. Governing externalization model

013-H establishes internal authority. 013-I maps how selected authority or other legitimate source state becomes an external representation and then an authorized release.

```text
identified SourceBasis
  + RepresentationProfile / purpose
  + AudienceProfile / disclosure class
  → Generate Export
  → stable Export representation
  → optional explicit Publish Representation
  → Publication release authority
  → downstream transport / possession / delivery
```

Preserve throughout:

```text
source authority
  != Export representation
  != Publication release
  != transport/delivery
```

The arrows are composition and explanation, not ownership transfer.

# 2. Export represents exact source authority; it never promotes it

Export binds an exact reconstructible SourceBasis.

The experience must make enough of that relationship intelligible to avoid implying that rendering or formatting changes semantic authority.

```text
provisional/calculated source
  → provisional/calculated representation

current Outcome Declaration
  → official-result representation
```

An Export cannot make a provisional Rank official, make an Affected declaration Current, make incomplete evidence complete, or create publication authority.

Representation language should not imply stronger source status than the SourceBasis actually owns.

# 3. Representation purpose and AudienceProfile are semantic inputs

An Export is not merely a format choice.

It has a declared RepresentationProfile/purpose and AudienceProfile/disclosure class.

Examples may include:

- Judge-safe operational material;
- Organizer-sensitive operational material;
- Ceremony-safe result material;
- Public result material;
- internal audit/history material.

These are representation/disclosure profiles, not new product variants or new authority Concepts.

The experience should make the intended use/audience intelligible before generation when materially relevant.

# 4. Actor Access does not define audience disclosure

Preserve:

```text
actor may inspect fact
  != fact may appear in Export
  != fact may be released to selected Audience
```

An Organizer may possess broader interactive Access than a Public or Ceremony Export is allowed to disclose.

Disclosure rules apply to the whole representation surface, including where semantically material:

- visible body content;
- filenames/titles;
- QR/deep-link payloads;
- metadata;
- printed labels;
- embedded identifiers;
- search/indexable fields.

The mapping does not prescribe how those surfaces are technically generated.

# 5. Generate Export

`Generate Export` is a coordinated application action over an exact source, purpose and audience contract.

Before generation, the representation must be legitimate for the requested use:

- SourceBasis is valid for the intended representation claim;
- representation does not overstate source authority;
- AudienceProfile permits the disclosed information;
- materially sensitive incidental surfaces are compatible with disclosure rules;
- representation is semantically faithful enough for its purpose.

Successful generation establishes a distinct stable Export initially `Current` relative to its exact SourceBasis and representation contract.

Generation does **not** publish.

# 6. Export currentness is representation currency, not distribution

User-visible Export currency is:

```text
Current
Affected
Stale
Superseded
Retired
```

These meanings concern the relationship between the representation and current source/use context.

They do not answer whether the representation was released.

## Current

The unchanged Export remains truthful/applicable for its intended current purpose and audience.

`Current` does not mean official, Published or delivered.

## Affected

A material dependency changed and review/reconfirmation is required, but the representation is not yet known to be unsuitable.

```text
Affected != Stale
Affected != Withdrawn
```

## Stale

The Export is known not to reflect the applicable current basis for ordinary current use.

A Stale Export may remain historically faithful to the SourceBasis it actually represented.

## Superseded

A distinct successor Export explicitly replaced the predecessor for comparable ordinary use.

The predecessor remains historical representation truth.

## Retired

The Export remains historical but is no longer offered for ordinary use.

Retirement does not withdraw an existing Publication.

# 7. Revalidate without rewriting history

An Affected Export may be revalidated against its **unchanged exact SourceBasis** and representation contract.

Revalidation may restore `Current` only when that original basis/content remains legitimately applicable for the intended current use.

If current use requires corrected/new source state:

```text
old Export SourceBasis remains unchanged
new source basis
  → new Export
```

Revalidation cannot silently mutate the predecessor representation into newer source truth.

# 8. Successor source authority does not automatically create successor Export

A successor Outcome Declaration or other corrected source state changes the set of valid representation options; it does not itself generate a replacement artifact.

```text
successor source authority exists
  != successor Export exists
```

An authorized actor/application path must deliberately generate the new Export from the new exact SourceBasis.

Where comparable, the new Export may explicitly supersede the predecessor.

# 9. Publication is deliberate release authority

Publication owns whether an exact selected representation is deliberately released to a declared Audience/Channel under PublishingAuthority.

```text
Export exists
  != Publication exists
```

Ordinary publication requires the exact Export to be selected and compatible with:

- intended Audience/Channel;
- current release purpose;
- applicable source-authority claim;
- disclosure rules;
- current representation suitability;
- legitimate PublishingAuthority;
- absence of known materially misleading release conditions.

Publication cannot cure a disclosure-invalid or source-misrepresenting Export.

# 10. Publish Representation

`Publish Representation` is an explicit high-consequence release action.

Its semantic inputs include:

- exact selected Export;
- intended Audience;
- Channel/destination;
- PublishingAuthority.

Successful Publication establishes:

```text
Publication = Published
Representation = exact selected Export
Audience / Channel = attributable
```

Publication does not:

- promote the Export's SourceBasis;
- make an Export Current;
- create an Outcome Declaration;
- prove recipient delivery/viewing.

# 11. Official is not automatically public

013-H established internal officiality. 013-I preserves:

```text
Outcome Declaration Current
  != Public Export exists
  != Publication Published
```

Therefore an official-but-non-public Competition is legitimate.

A current public-safe Export may also exist without being Published.

This supports deliberate review/staging before release without weakening internal official authority.

# 12. Publication state and Export currency are independent

The experience must support combinations such as:

```text
Publication Published + Export Current
Publication Published + Export Affected
Publication Published + Export Stale
Publication Superseded + Export Superseded
Publication Withdrawn + historical Export retained
```

Do not collapse Export currency into Publication distribution state.

A representation becoming Stale does not mean it was never released.

# 13. Affected official authority and ordinary new release

An Affected Outcome Declaration remains official under 013-H but requires correction/review.

For ordinary new release, the experience must not present an Affected declaration as uncomplicated Current official truth.

Where policy permits a qualified exceptional disclosure, the representation/release must preserve the relevant qualification/authority rather than silently clearing affectedness.

013-I does not create a universal exception to publish Affected official state.

# 14. Source correction after publication

Source correction is represented as a sequence of independently owned consequences:

```text
source authority changes
  → dependent Export reviewed
  → Export may become Affected / Stale / remain Current after valid revalidation
  → existing Publication remains historically bound to exact released Export
  → publishing authority decides whether to leave, withdraw or supersede
```

There is no automatic:

```text
correction
  → withdraw
  → regenerate
  → republish
```

Each authority transition remains explicit.

# 15. Withdraw Publication

Withdrawal ends current MUDAC release authority for that Publication while preserving the fact that release occurred.

The experience should communicate, where relevant:

- which exact representation was released;
- Audience/Channel;
- prior publication time/authority;
- current Withdrawn state;
- that withdrawal does not rewrite SourceBasis or Export history.

Withdrawal must not imply that downloaded, printed, cached, screenshotted or otherwise externally retained copies ceased to exist.

# 16. Publish Successor Representation

When current release should be replaced:

```text
valid successor Export exists
  + publishing authority selects it
  → Publish Successor Representation
  → successor Publication = Published
  → predecessor Publication = Superseded
```

Each Publication remains bound to its own exact Export.

Preserve:

```text
successor Export != successor Publication
successor Outcome Declaration != successor Publication
```

Release replacement always requires explicit Publication authority.

# 17. External recipient meaning

An external recipient is an audience/recipient of a released representation; recipient possession is not another source of MUDAC authority.

The experience should preserve:

```text
recipient possesses artifact / URL / printed copy
  != Export is Current
  != Publication is currently Published
  != recipient has interactive Access
```

A recipient may legitimately retain a historical copy after MUDAC withdraws or supersedes current release authority.

The system must not represent historical recipient possession as if it can be retroactively erased.

# 18. Publication is not delivery

Publication means authorized release, not transport success.

Preserve:

```text
Publication Published
  != email delivered
  != browser/CDN propagated
  != printer succeeded
  != recipient viewed
```

No new Delivery Concept is required by current mapping.

Transport status may later be represented operationally if implementation requires it, but it must not redefine Publication authority.

# 19. Audience disclosure and external identity

External representations must respect audience-specific identity rules.

Examples:

- Judge-safe artifacts continue to use permitted blinded identity;
- Ceremony/Public material may disclose Team Name or institution only when current disclosure policy/profile permits it;
- private Judge evidence/Notes do not become public merely because the source actor can inspect them;
- internal provenance/history may require a different AudienceProfile than public result material.

Representation profile determines what the external recipient is legitimately shown; it does not rewrite underlying Team/Alias/Identity history.

# 20. Action availability and feedback

| Action | Semantic availability | Result |
| --- | --- | --- |
| Generate Export | legitimate exact SourceBasis + valid purpose/audience/disclosure + requesting authority | new stable Current Export |
| Revalidate Export | existing Affected Export + unchanged basis/content remains valid for current use | same Export Current, or review determines other currency |
| Generate Successor Export | newer/corrected SourceBasis required for current representation | distinct new Export |
| Retire Export | authority to remove representation from ordinary use | Export Retired; Publication unchanged |
| Publish Representation | exact suitable Export + Audience/Channel + PublishingAuthority + disclosure/release conditions | Publication Published |
| Withdraw Publication | current/relevant Publication + withdrawal authority | Publication Withdrawn; history retained |
| Publish Successor Representation | valid successor Export + successor release authority | new Publication Published; predecessor Superseded |

Unavailable actions should expose the semantic blocker when doing so is compatible with disclosure/privacy constraints.

# 21. Truthful feedback under uncertainty

The experience must not claim successful generation, revalidation, Publication, withdrawal or successor release when the authoritative result is unknown.

Where relevant distinguish:

```text
request pending / result unknown
confirmed Export generated/currentness established
confirmed Publication state transition
known rejection/failure and source reason
```

013-J re-audits cross-cutting status/recovery semantics.

# 22. Mapping risks closed or reduced

013-I closes/reduces:

- **MAP-R09** — official/Export/Publication/delivery collapse: fully separated;
- **MAP-R10** — successor representation/release flattened to edit: explicit new Export + successor Publication;
- **MAP-R11** — official-but-non-public and Export-without-Publication remain PF-01 profiles/states;
- **MAP-R13** — route/URL/QR possession does not create authority or disclosure permission;
- **MAP-R15** — broad technical/Organizer Access does not create audience disclosure or publishing authority;
- **MAP-R16** — old paper/export/publication boundary fully decomposed into natural owners.

No new Concept, synchronization or dependence defect requires upstream reopen.

# 23. 013-J handoff

013-J inherits:

```text
same semantic authority must survive accessible/degraded paths
unknown generation/publication result != success
Export currency != Publication state
withdrawal/supersession != external-copy disappearance
representation/disclosure semantics must hold across responsive/print/degraded surfaces
```

013-J must audit accessibility, degraded operation, status/feedback and recovery without creating alternate authority semantics for Export/Publication.

# Exit decision

```text
013-I: COMPLETE — PASS
external-representation mapping: CURRENT / ACCEPTED
audience/disclosure mapping: CURRENT / ACCEPTED
Export currency: EXPLICIT / OWNER-PRESERVING
Publication release: EXPLICIT / OWNER-PRESERVING
external recipient semantics: DISTINCT FROM ACCESS/AUTHORITY
historical release truth: PRESERVED
013-J: NEXT
architecture authority: SUSPENDED
implementation planning: SUSPENDED
implementation readiness: NOT READY
implementation authorization: NOT YET
```

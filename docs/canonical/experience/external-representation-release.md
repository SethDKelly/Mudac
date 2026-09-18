---
type: Experience Contract
title: External Representation, Disclosure & Release Mapping
description: Current mapping for exact-source Export generation, audience/disclosure-safe representation, Export currency, deliberate Publication release, withdrawal/succession and external-recipient semantics.
status: stable
tags: [experience, mapping, export, publication, disclosure, audience, release, external-recipient, currency, phase-013]
sources:
  - resource: ../../013-concept-mapping-interaction-semantics-user-visible-representation/013-I-export-publication-audience-disclosure-external-recipient-representation-release-mapping.md
  - resource: outcome-officiality.md
  - resource: ../concepts/export.md
  - resource: ../concepts/publication.md
  - resource: ../concepts/outcome-declaration.md
  - resource: ../synchronizations/external-representation-publication-release.md
  - resource: ../policies/anonymity-disclosure.md
  - resource: ../invariants/official-not-automatically-public.md
---

# Purpose

Define how MUDAC maps stable external representation and deliberate release while preserving the distinction between source authority, representation currency, audience disclosure, Publication state and downstream delivery.

# Governing separation

```text
source authority
  != Export representation
  != Publication release
  != transport / recipient possession
```

An Export represents an exact SourceBasis for a declared purpose and AudienceProfile. Publication deliberately releases an exact representation to a declared Audience/Channel. Transport/delivery does not create either authority.

# Export SourceBasis

Every meaningful Export binds an exact reconstructible SourceBasis.

The representation must not imply stronger semantic authority than that basis owns.

```text
calculated/provisional source
  → calculated/provisional representation

current Outcome Declaration
  → official-result representation
```

Rendering, summarizing, formatting or redacting does not promote source authority.

# Purpose and AudienceProfile

Export generation includes a RepresentationProfile/purpose and AudienceProfile/disclosure class.

Possible profiles may include Judge-safe, Organizer-sensitive, Ceremony-safe, Public or internal audit/history uses.

These are representation/disclosure profiles, not new Concepts or product variants.

The intended audience/purpose should be intelligible before generation where it materially affects disclosure or claim semantics.

# Actor Access versus audience disclosure

Preserve:

```text
actor can inspect fact
  != fact may appear in Export
  != fact may be released to selected Audience
```

Interactive Organizer Access does not authorize the same information in a public artifact.

Disclosure applies to material representation surfaces including content, metadata, filenames/titles, QR/deep-link payloads, printed labels and embedded identifiers.

# Generate Export

`Generate Export` is a coordinated application action over:

- exact legitimate SourceBasis;
- RepresentationProfile/purpose;
- AudienceProfile/disclosure class;
- requesting authority/context.

Generation requires semantic fidelity and compatible disclosure. A successful action establishes a distinct stable Export initially `Current` relative to its exact basis and representation contract.

```text
Export generated != Publication
```

# Export currency

Export owns representation currency:

```text
Current
Affected
Stale
Superseded
Retired
```

## Current

The unchanged Export remains applicable/truthful for its intended current purpose/audience.

Current does not mean official, Published or delivered.

## Affected

A material dependency changed and review/reconfirmation is required. Incorrectness is not yet established.

```text
Affected != Stale
Affected != Withdrawn
```

## Stale

The representation is known not to reflect the applicable current basis for ordinary current use, although it may remain historically faithful to what it represented.

## Superseded

A distinct successor Export replaced the predecessor for comparable ordinary use. The predecessor remains historical representation truth.

## Retired

The Export is removed from ordinary use while retained historically. Retirement does not alter Publication state.

# Revalidation preserves history

An Affected Export may be revalidated only against its unchanged exact SourceBasis and representation contract.

It may return to Current only if that original basis/content remains legitimately applicable.

If current use requires corrected/new source authority:

```text
new source basis
  → new Export
```

The historical Export is never rewritten to bind newer truth.

# Successor authority does not auto-generate representation

A successor Outcome Declaration or other corrected source state does not automatically create a successor Export.

```text
successor source authority != successor Export
```

The new representation must be generated deliberately from the new exact SourceBasis.

# Publication is explicit release

Publication owns deliberate release of an exact representation.

```text
Export exists != Publication exists
```

Ordinary release requires:

- exact selected Export;
- compatible Audience/Channel;
- representation current/suitable for the intended release purpose;
- source authority sufficient for the release claim;
- disclosure rules satisfied;
- legitimate PublishingAuthority;
- no known unresolved condition making release materially misleading.

Publication cannot cure a disclosure-invalid or source-misrepresenting Export.

# Publish Representation

Successful publication establishes:

```text
Publication = Published
Representation = exact selected Export
Audience / Channel / PublishingAuthority = attributable
```

Publication does not make the source official, make the Export Current or prove transport/delivery success.

# Official is not automatically public

Preserve:

```text
Outcome Declaration Current
  != Public Export exists
  != Publication Published
```

Official-but-non-public operation is legitimate.

A current public-safe Export may exist without being released.

# Export currency and Publication state are independent

Legitimate combinations include:

```text
Publication Published + Export Current
Publication Published + Export Affected
Publication Published + Export Stale
Publication Superseded + Export Superseded
Publication Withdrawn + historical Export retained
```

Representation currency and release authority must never collapse into one status.

# Affected official authority

An Affected Outcome Declaration remains official but requires correction/review under 013-H.

Ordinary new release must not present it as uncomplicated Current official truth. Any exceptional qualified release must use explicit governing authority and preserve the material qualification rather than clearing affectedness through representation.

# Source correction after release

A source change does not automatically withdraw or replace a Publication.

```text
source changes
  → dependent Export currentness reviewed
  → Export may remain Current / become Affected / become Stale / receive successor
  → existing Publication remains bound to exact historical Export
  → publishing authority explicitly leaves / withdraws / supersedes release
```

No automatic correction → withdraw → regenerate → republish behavior exists.

# Withdrawal

Withdrawal ends current MUDAC release authority while preserving historical release truth.

It does not erase:

- exact representation released;
- Audience/Channel;
- publishing authority/time;
- fact that the release occurred;
- external copies already obtained.

Withdrawal does not mutate Export SourceBasis or source authority.

# Successor release

A successor Publication requires an already legitimate successor representation plus explicit release authority.

```text
valid successor Export
  + Publish Successor Representation
  → successor Publication Published
  → predecessor Publication Superseded
```

Each Publication remains bound to its own exact Export.

```text
successor Outcome Declaration != successor Export != successor Publication
```

# External recipient semantics

Recipient possession is not current MUDAC authority.

```text
recipient has artifact / URL / printed copy
  != Export Current
  != Publication currently Published
  != interactive Access
```

Historical external copies may remain after withdrawal/supersession. The experience must not imply retroactive disappearance.

# Publication is not delivery

Publication means authorized release, not transport success.

```text
Publication Published
  != email delivered
  != CDN/browser propagation
  != printer success
  != recipient viewed
```

No Delivery Concept is introduced by this mapping.

# External identity and disclosure

Representation profile determines what external recipients may legitimately see.

Judge-safe outputs preserve blinded identity. Ceremony/Public outputs disclose Team Name/institution only where current policy/profile permits. Private Judge evidence/Notes do not become public merely because an Organizer can inspect them.

Representation never rewrites underlying Team/Alias/Identity history.

# Action availability

| Action | Ordinary semantic availability |
| --- | --- |
| Generate Export | legitimate exact SourceBasis + purpose/audience/disclosure + requesting authority |
| Revalidate Export | existing Affected Export + unchanged basis/content remains valid for use |
| Generate Successor Export | newer/corrected SourceBasis required for current representation |
| Retire Export | authority to remove representation from ordinary use |
| Publish Representation | exact suitable Export + Audience/Channel + PublishingAuthority + release conditions |
| Withdraw Publication | current/relevant Publication + withdrawal authority |
| Publish Successor Representation | valid successor Export + successor release authority |

Unavailable actions should explain the semantic blocker where disclosure/privacy permits.

# Truthful feedback

Do not claim generation, revalidation, Publication, withdrawal or successor release when the authoritative result is unknown.

Cross-cutting status/recovery grammar is re-audited in 013-J.

# 013-J boundary

013-J must preserve these semantics across accessible, degraded and recovery paths:

```text
Export currency != Publication state
unknown authority transition != confirmed success
withdrawal/supersession != external-copy disappearance
representation/disclosure rules apply across print/responsive/degraded surfaces
```

---
type: Synchronization Contract
title: External Representation, Currency & Publication Release Composition
description: "Current MUDAC composition for exact-source Export generation, representation currency/revalidation, audience/disclosure safety, and explicit Publication release/withdrawal/succession after Phase 011-H."
status: stable
tags: [synchronization, export, publication, representation, currency, release, disclosure, phase-011]
sources:
  - resource: ../../011-concept-composition-synchronization/011-H-export-publication-representation-currency-release-composition.md
  - resource: ../concepts/export.md
  - resource: ../concepts/publication.md
  - resource: ../concepts/outcome-declaration.md
  - resource: ../policies/anonymity-disclosure.md
  - resource: ../invariants/official-not-automatically-public.md
  - resource: temporal-truth-correction.md
  - resource: evaluation-outcome-finalization-declaration.md
generated: { by: openai/gpt-5.6-sol, at: 2026-09-14T16:49:00-05:00 }
---

# Purpose

Define current MUDAC application composition by which exact source authority becomes a stable audience-specific external representation and, only through a separate explicit act, an authorized release.

This contract is the current Phase 011-H owner for legacy synchronization 15 and the Export/Publication consequence portion of legacy synchronization 12.

# Governing separation

```text
source authority
  ↓
Export representation + currency
  ↓ explicit release only
Publication distribution authority
  ↓
transport/delivery realization
```

These layers must not collapse.

- source authority says what is semantically true/current/official;
- Export says what exact source was represented, for what purpose/audience, and whether that representation remains current for that use;
- Publication says whether that exact representation was deliberately released to a declared Audience/Channel;
- transport/delivery says nothing about domain release authority by itself.

# Generate Export

Application action: **Generate Export**.

Participants:

- `Export.request`;
- `Export.validateRepresentation`;
- `Export.generate`.

Required supplied semantics:

- exact reconstructible SourceBasis;
- RepresentationProfile / purpose;
- AudienceProfile / disclosure class;
- current requesting authority/context.

Conditions include:

- SourceBasis is legitimate for the requested purpose;
- representation does not imply stronger authority than SourceBasis owns;
- audience/disclosure rules permit the represented information;
- incidental representation surfaces do not defeat material disclosure protections;
- representation is semantically faithful enough for the declared purpose.

Success establishes a stable Export initially `Current` relative to its exact SourceBasis and representation contract.

Generation does not publish.

# Export currency

## Current

The Export remains truthful/applicable for its intended current purpose and audience against its unchanged exact SourceBasis and applicable current context.

`Current` does not mean Published, Official or Delivered.

## Affected

`Export.markAffected` is a system/composition reaction when a material source/disclosure dependency changes and review is required but current-use incorrectness is not yet established.

Affected means review/reconfirmation is required.

It does not mean withdrawn, unpublished or historically false.

## Revalidation

`Export.validateRepresentation` owns revalidation of an Affected Export.

The same Export may be reconfirmed `Current` only when:

- its exact SourceBasis remains unchanged;
- represented content remains faithful to that basis;
- that basis remains legitimately applicable for the intended purpose;
- audience/disclosure requirements remain satisfied.

If current use requires newer/corrected source state, revalidation cannot rewrite the old SourceBasis. A new Export is required.

## Stale

`Export.markStale` applies when the representation is known not to reflect the applicable current basis for its intended ordinary current use.

A Stale Export may remain a correct historical representation of its bound source.

## Superseded

A new independently valid Export may be related through `Export.supersedeBy` when it replaces the predecessor for a comparable ordinary use.

The predecessor SourceBasis remains immutable historical meaning.

Export supersession does not change Publication state.

## Retired

`retireFromOrdinaryUse` ends ordinary current selection/use while retaining representation history.

Retirement does not withdraw an existing Publication.

# Audience and disclosure

Representation authority is least-disclosure and purpose-specific.

The actor generating or publishing a representation may have broader Access than the representation's AudienceProfile permits.

Therefore:

```text
actor can inspect fact
  != fact may appear in Export
  != fact may be publicly released
```

Judge-safe, Organizer-sensitive, Ceremony-safe and Public profiles may legitimately expose different projections of the same underlying source authority.

Publication cannot cure a disclosure-invalid Export.

# Publication prerequisites

MUDAC ordinary publication of an Export requires:

- exact Export selected;
- Export profile compatible with intended Audience/Channel;
- Export suitable/current for the intended release purpose;
- source authority sufficient for the claim made by the release;
- disclosure rules satisfied;
- legitimate publishing authority;
- no unresolved condition known to make the release materially misleading.

For ordinary public official-result release, the Export is based on the current Outcome Declaration and is Current for the selected Public/Ceremony profile.

An Affected Outcome Declaration remains official, but ordinary new publication that presents it as uncomplicated current truth is not authorized by default. Any qualified exceptional release requires explicit governing authority without erasing affectedness.

# Publish Representation

Application action: **Publish Representation**.

Participant:

- `Publication.publish`.

Bindings:

- Representation = exact selected Export;
- Audience;
- Channel;
- PublishingAuthority.

Success establishes a Publication in `Published` state.

Publication does not:

- promote source authority;
- make Export Current;
- create Outcome Declaration authority;
- prove transport/delivery completion.

# Official does not automatically mean public

A current Outcome Declaration may exist with no public Publication.

A current public-safe Export may exist with no Publication.

Therefore MUDAC supports:

```text
Outcome Declaration Current
  → Export generated/reviewed
  → publication delayed
```

without changing official authority.

# Publication and Export currency remain independent

These states can coexist:

```text
Publication Published + Export Current
Publication Published + Export Affected
Publication Published + Export Stale
Publication Superseded + Export Superseded
Publication Withdrawn + historical Export retained
```

Source currentness and distribution authority are independent owner meanings.

# Source correction after release

Source correction follows this conceptual order:

1. source owner changes first;
2. actual dependent Export is identified;
3. Export becomes Affected/Stale or is revalidated;
4. existing Publication remains bound to the exact representation historically released;
5. publishing authority deliberately decides leave/withdraw/supersede;
6. corrected/current release requires a new/current Export first;
7. Publication action establishes the new release.

There is no automatic correction → withdraw → regenerate → republish synchronization.

# Withdraw Publication

Application action: **Withdraw Publication**.

Participant:

- `Publication.withdraw`.

Withdrawal ends current MUDAC release authority while preserving:

- exact Representation released;
- Audience/Channel;
- publishing authority/time;
- fact that release occurred.

Withdrawal does not erase external copies or change the Export/SourceBasis.

# Publish Successor Representation

Application action: **Publish Successor Representation**.

Participants:

- an already valid successor Export;
- `Publication.supersedeWith` creating/binding a successor Publication.

Success:

- successor Publication is Published;
- predecessor Publication is Superseded;
- predecessor release remains reconstructible;
- each Publication remains bound to its own exact Export.

A successor Export alone never creates a successor Publication.

# Physical/external persistence

A printed page, downloaded file, screenshot, copied URL or external cache may outlive current release authority.

MUDAC therefore never represents withdrawal/supersession as retroactive disappearance.

The historical fact of release and the current authority to distribute are separate.

# Transport boundary

Publication means authorized release, not delivery success.

Email arrival, browser/CDN propagation, printer success, external caching and recipient viewing are downstream realization concerns.

No Delivery concept or transport synchronization is established here.

# Current action-surface classification

| Action family | Current MUDAC status |
| --- | --- |
| Export `request` | direct request candidate |
| Export `validateRepresentation` | composition participant and Affected revalidation owner |
| Export `generate` | coordinated `Generate Export` action |
| Export `markAffected` | system/composition reaction |
| Export `markStale` | system/composition reaction |
| Export `supersedeBy` | composition-only successor relation |
| Export `retireFromOrdinaryUse` | controlled direct administrative action |
| Publication `publish` | controlled explicit release action |
| Publication `withdraw` | controlled high-consequence release action |
| Publication `supersedeWith` | coordinated explicit successor release |
| declaration → auto-publish | intentionally unavailable |
| correction → auto-withdraw/republish | intentionally unavailable |
| transport success → Publication state | intentionally unavailable |

011-I owns final whole-application action-surface closure.

# Composition invariants

1. Export never promotes SourceBasis authority.
2. Exact historical SourceBasis never changes after meaningful Export generation.
3. Audience/disclosure profile constrains representation independently from actor Access.
4. Export currency and Publication distribution state never collapse.
5. Affected is review-required, not known-wrong.
6. Revalidation may reconfirm Current only without changing SourceBasis/content authority.
7. Current representation of newer/corrected source requires a new Export.
8. New Export never implies Publication.
9. Publication always binds an exact Representation.
10. Source correction never retargets historical Publication.
11. Withdrawal/supersession preserves prior release history.
12. Publication cannot make calculated/working state official.
13. Official Outcome Declaration does not imply publication.
14. Publication does not imply transport delivery success.
15. Already distributed copies cannot be semantically erased by later withdrawal.

# Chaining summary

```text
exact source + purpose + audience
  → Generate Export
  → optional Publish Representation
```

```text
source dependency changes
  → Export Affected
  → Revalidate Export
      → Current
      OR Stale
      OR new successor Export
```

```text
old publication + corrected/current successor Export
  → explicit Publish Successor Representation
  → old Publication Superseded
  + new Publication Published
```

These are semantic compositions, not storage, rendering, CDN, queue, retry, or delivery designs.

# Current adjacent ownership

- whole-application action surface/chaining/automation → [Application Action Surface, Chaining & Automation Composition](application-action-surface-composition.md);
- product-family inclusion/dependence → [Dependence](../dependence/);
- user-visible download/share/print/publish interactions → [Experience](../experience/);
- representation and delivery realization → downstream architecture/engineering only after successful Concept Design closure and explicit re-entry authorization.

These owner boundaries are current; the earlier Phase-011/012/013 work is complete.
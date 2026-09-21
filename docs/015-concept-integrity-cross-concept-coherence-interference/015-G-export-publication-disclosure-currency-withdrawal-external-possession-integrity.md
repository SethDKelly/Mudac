---
type: Phase Design Record
title: 015-G — Export, Publication, Disclosure, Currency, Withdrawal & External-Possession Integrity
description: "Audits Cluster E purpose preservation across Outcome Declaration/source authority, exact-source Export representation, representation currency, audience/disclosure profiles, explicit Publication release, withdrawal/succession, and external possession, and dispositions DIR-035 through DIR-041."
status: stable
tags: [phase-015, integrity, export, publication, disclosure, currency, withdrawal, external-possession]
sources:
  - resource: 015-A-integrity-audit-scope-interference-surfaces-whole-system-coverage-subphase-planning.md
  - resource: 015-B-purpose-preservation-baseline-integrity-inventory-directional-interference-register.md
  - resource: 015-E-versioning-provenance-temporal-correction-successor-work-historical-truth-integrity.md
  - resource: 015-F-coverage-aggregate-rank-award-competition-finalization-outcome-declaration-integrity.md
  - resource: ../canonical/concepts/outcome-declaration.md
  - resource: ../canonical/concepts/export.md
  - resource: ../canonical/concepts/publication.md
  - resource: ../canonical/synchronizations/external-representation-publication-release.md
  - resource: ../canonical/experience/external-representation-release.md
  - resource: ../canonical/policies/anonymity-disclosure.md
  - resource: ../canonical/invariants/official-not-automatically-public.md
  - resource: ../canonical/invariants/current-vs-historical-truth.md
---

# Purpose

Audit whether MUDAC can externalize source information without collapsing:

```text
source authority
  != representation
  != representation currency
  != release authority
  != delivery / recipient possession
```

The Cluster-E chain under audit is:

```text
exact source authority
  + representation purpose
  + AudienceProfile
  → Export

Export currency/currentness
  + PublishingAuthority
  + Audience/Channel
  → optional Publication

Publication release
  → downstream transport / external possession

later source correction
  → Export currency review
  → explicit release review
  != historical rewrite
```

015-G dispositions DIR-035 through DIR-041.

# Decision

**015-G COMPLETE — PASS. Proceed to 015-H.**

```text
DIR-035 through DIR-041                 DISPOSITIONED
confirmed integrity violation           NONE
INT-F corrective finding opened         NONE
upstream semantic reopen                NONE
canonical semantic repair               NONE
purpose-preserved explicit limitations  4
cross-cluster rechecks retained         DIR-036 / 039 / 040 / 041
NEXT                                    015-H
```

The four explicit limitations are:

1. Export currency is relative to the unchanged exact SourceBasis, representation purpose and current-use applicability; it is not a generic statement about source authority or Publication state;
2. the actor generating/publishing an Export may legitimately inspect more information than the target AudienceProfile permits the representation to contain;
3. withdrawal/supersession changes current MUDAC release authority but cannot retroactively erase external copies or the historical fact of release;
4. a successor source/Outcome Declaration does not automatically create, retarget or publish a successor Export/Publication.

# 1. Purpose obligations exercised

015-G principally exercises:

- **P-07 — Correctable authority and historical truth**;
- **P-08 — Contextual confidentiality and authority separation**;
- **P-09 — Faithful external representation and controlled release**.

Supporting obligations include P-06 because external representations must faithfully convey the authority/currentness of the source they represent.

Primary invariants:

```text
INV-005 Current vs Historical Truth
INV-007 Official Is Not Automatically Public
INV-010 Truthful Authority Under Uncertainty
```

Material tensions:

```text
T-07 correctability vs immutability
T-08 continuity vs confidentiality
T-10 transparency vs controlled disclosure/currentness
```

# 2. Externalization model under audit

Current MUDAC deliberately separates four ownership layers.

## Source authority

Examples include:

- calculated/provisional state;
- current Outcome Declaration;
- affected Outcome Declaration;
- historical authoritative state.

The source owner determines semantic meaning.

## Export

Export owns:

- exact SourceBasis;
- representation purpose/profile;
- AudienceProfile;
- generated representation;
- representation currency/history.

Export does not promote the source.

## Publication

Publication owns:

- exact Representation released;
- Audience;
- Channel;
- PublishingAuthority;
- release time;
- Published/Withdrawn/Superseded history.

Publication does not change source or Export authority.

## External possession / delivery

Recipient possession and transport success remain downstream facts.

They do not become Access, Export, Publication or source authority.

# 3. Counterexample set

## G-P01 — Outcome Declaration becomes Affected after public Export exists

Attempt:

> Rewrite the existing Export to bind corrected declaration state.

Rejected.

The historical Export keeps its exact SourceBasis. Its currency may become Affected or Stale; corrected/current representation requires a distinct new Export when newer source authority is required.

## G-P02 — Export is marked Current

Attempt:

> Treat the source as official/current because the Export is Current.

Rejected.

Export Current means the representation remains applicable/truthful for its declared current use relative to its exact bound SourceBasis and representation contract.

It does not promote source authority.

## G-P03 — Export becomes Affected or Stale

Attempt:

> Automatically withdraw any Publication that used it.

Rejected.

Export currency and Publication distribution state remain independent. Release review may be required, but withdrawal is a separate deliberate Publication action.

## G-P04 — Publication is Published

Attempt:

> Treat the selected Export as Current or the represented source as official.

Rejected.

Publication cannot cure source or representation defects.

## G-P05 — Organizer can inspect Judge-sensitive data

Attempt:

> Include it in a public Export because the actor generating the Export had Access.

Rejected.

```text
actor can inspect fact
  != fact may appear in Export
  != fact may be released to Audience
```

AudienceProfile/disclosure independently constrains the representation.

## G-P06 — Publication is withdrawn

Attempt:

> Show that recipients no longer possess the representation.

Rejected.

Withdrawal ends current MUDAC release authority. It does not recall printed/downloaded/copied material.

## G-P07 — Successor Outcome Declaration confirmed

Attempt:

> Retarget the existing Export and Publication to the successor declaration.

Rejected.

```text
successor source authority
  != successor Export
  != successor Publication
```

Each predecessor remains bound to its exact historical source/representation.

# 4. DIR-035 — Outcome Declaration/source change → Export

**Disposition: PURPOSE PRESERVED WITH EXPLICIT CURRENCY LIMITATION.**

A material source dependency change does not rewrite an existing Export.

Current composition supports:

```text
source changes
  → dependent Export review

if applicability uncertain
  → Export Affected

if known mismatch for ordinary current use
  → Export Stale

if unchanged bound source remains legitimately applicable
  → revalidate same Export Current

if current use needs new/corrected source
  → new Export
```

The old Export's SourceBasis remains immutable historical meaning.

This preserves both source correction and representation history.

# 5. DIR-036 — Export generation/currentness → source authority

**Disposition: NO INTEGRITY VIOLATION; 015-I MAPPING RECHECK RETAINED.**

Export must faithfully represent the authority level of its bound source.

```text
calculated/provisional source
  → calculated/provisional representation

current official declaration
  → official-result representation

Affected declaration
  → qualified/affected representation if policy permits
```

Formatting, summarizing, rendering, naming or visual polish cannot promote source authority.

Likewise:

```text
Export Current
  != source official
  != Publication Published
  != delivered
```

015-I must recheck that user-visible labels/status do not make a polished/current Export appear more authoritative than SourceBasis.

# 6. DIR-037 — Export currentness → Publication

**Disposition: NO INTEGRITY VIOLATION.**

Export currentness may constrain ordinary release suitability, but it does not operate Publication.

Source/currentness changes never automatically:

- publish;
- withdraw;
- supersede;
- retarget.

Legitimate states include:

```text
Publication Published + Export Current
Publication Published + Export Affected
Publication Published + Export Stale
Publication Withdrawn + historical Export retained
```

If a representation becomes unsuitable for current release, publishing authority must explicitly decide the permitted release consequence.

This preserves Export currency and Publication distribution as independent owner meanings.

# 7. DIR-038 — Publication state → Export/source currentness

**Disposition: NO INTEGRITY VIOLATION.**

Publication state is release history/authority only.

```text
Published
  != Export Current
  != source Current
  != source official

Withdrawn
  != Export Stale
  != source invalid

Superseded Publication
  != predecessor Export/source historically false
```

A Publication cannot validate or invalidate the representation/source it carries.

# 8. DIR-039 — Publication withdrawal → external possession

**Disposition: PURPOSE PRESERVED WITH EXTERNAL-PERSISTENCE LIMITATION; 015-I RECHECK RETAINED.**

Withdrawal means:

> MUDAC no longer authorizes the Publication as a current release.

It does not mean:

- downloaded file deleted;
- printed copy recovered;
- screenshot erased;
- copied URL vanished;
- external cache purged;
- recipient never possessed the representation.

Preserve:

```text
current MUDAC release authority
  != external possession
```

The historical fact of release remains attributable.

015-I must ensure user-visible withdrawal/supersession language does not imply retroactive disappearance.

# 9. DIR-040 — actor Access → audience disclosure

**Disposition: PURPOSE PRESERVED WITH AUDIENCE-SPECIFIC DISCLOSURE LIMITATION; 015-I RECHECK RETAINED.**

Interactive Access and representation disclosure serve different purposes.

An Organizer may legitimately inspect information that a Public or Ceremony-safe Export must omit.

Therefore:

```text
actor Access
  → what the actor may inspect/do interactively

AudienceProfile
  → what the representation may disclose
```

The separation applies across:

- body content;
- metadata;
- filename/title;
- QR/deep-link payload;
- print labels;
- embedded identifiers.

Possession of a URL/route/device/previous rendering also does not create new disclosure authority.

015-I rechecks this distinction across profiles/accessibility/degraded presentation.

# 10. DIR-041 — successor Declaration → successor Export/Publication

**Disposition: NO INTEGRITY VIOLATION; 015-H CHAIN/AUTOMATION RECHECK RETAINED.**

A successor Outcome Declaration supplies new source authority.

It does not rewrite existing externalization history.

```text
successor Outcome Declaration
  → possible new SourceBasis

new/current representation needed
  → explicit Generate Export
  → distinct successor Export

successor release desired
  → explicit Publication successor action
```

Historical predecessor relationships remain:

```text
old Declaration
  != rewritten

old Export
  != retargeted

old Publication
  != silently replaced
```

A successor Export alone also does not create a successor Publication.

015-H rechecks the long correction chain to ensure system reactions stop before discretionary generation/release authority.

# 11. Official versus public integrity

015-F established official authority.

015-G confirms:

```text
Outcome Declaration Current
  != Public Export exists
  != Publication Published
  != recipient possesses artifact
```

Therefore these are all legitimate PF-01 states:

- official but non-public;
- public-safe Export generated but not released;
- internal/historical Export without Publication;
- Publication withdrawn while internal official declaration remains current;
- Affected official declaration with a historical still-published representation pending explicit release review.

Publication success/failure does not strengthen or weaken internal official authority.

# 12. Affected official authority and release integrity

015-F established that an Affected Outcome Declaration remains the latest declared official authority while requiring correction/review.

015-G preserves this without allowing representation to clear affectedness.

Ordinary new public release must not present an Affected declaration as uncomplicated current truth.

Where policy permits a qualified exceptional release:

- material affectedness remains represented;
- governing authority is explicit;
- representation does not clear the source state.

```text
qualified representation
  != source corrected
```

# 13. Export currency integrity

Export's five currentness meanings remain purpose-specific:

```text
Current
  = applicable/truthful for intended current use

Affected
  = dependency changed; review needed

Stale
  = known mismatch with applicable current basis

Superseded
  = explicit successor Export replaces comparable ordinary use

Retired
  = removed from ordinary use, retained historically
```

None is Publication state.

Revalidation of an Affected Export can return it to Current only without changing its historical SourceBasis/content contract.

If newer source is required:

```text
new source
  → new Export
```

# 14. Publication integrity

Publication remains explicit release.

Ordinary release requires:

- exact selected Export;
- compatible Audience/Channel;
- suitable representation for release purpose;
- source authority sufficient for the claim;
- disclosure rules satisfied;
- legitimate PublishingAuthority;
- no known unresolved condition making release materially misleading.

Publication cannot:

- make a source official;
- make an Export Current;
- change AudienceProfile;
- prove delivery success;
- erase earlier release history.

# 15. Withdrawal and successor-release integrity

Withdrawal:

```text
Published
  → Withdrawn
```

changes current release authority only.

Successor release:

```text
valid successor Export
+ explicit successor Publication action
  → new Publication Published
  → predecessor Publication Superseded
```

Each Publication remains bound to its own exact Export.

The predecessor does not become historically false merely because a successor is now preferred/current.

# 16. External recipient integrity

External recipient possession remains outside domain authority.

```text
recipient possesses artifact
  != interactive Access
  != Export Current
  != Publication currently Published
  != source currently official
```

This distinction is essential for printed materials, downloads, screenshots, copied URLs and external caches.

MUDAC can describe current authority truthfully without claiming control it does not possess over external copies.

# 17. Publication versus delivery integrity

Publication means deliberate authorized release.

It does not mean transport realization succeeded.

```text
Publication Published
  != email arrived
  != browser/CDN propagated
  != printer succeeded
  != recipient viewed
```

No Delivery Concept is introduced.

Transport failures may affect operational follow-up but cannot rewrite Publication authority/history.

# 18. Historical/current truth integrity

The complete externalization chain preserves:

```text
what source authority was then
what Export represented then
what Publication released then
what source/representation/release is current now
what external recipients may still possess
```

These may legitimately differ.

Correction operates through explicit currentness/successor relationships rather than historical rewrite.

# 19. Subject-purpose integrity summary

| Subject | Integrity result |
| --- | --- |
| Outcome Declaration | Purpose preserved; official authority remains independent from representation/release |
| Export | Purpose preserved with source-relative currency limitation |
| Publication | Purpose preserved; deliberate release remains independent from representation/source currentness |
| Audience disclosure | Purpose preserved with actor-Access separation |
| Withdrawal | Purpose preserved with external-persistence limitation |
| External possession | Correctly modeled as downstream fact, not authority |
| Successor externalization | Purpose preserved; successor source, Export and Publication remain independently deliberate |

# 20. Material finding result

015-G opens no corrective INT-F finding.

```text
INT-F corrective findings opened in 015-G = 0
```

Reason:

- source correction never rewrites historical Export SourceBasis;
- Export cannot promote source authority;
- Export currency and Publication state remain independent;
- Publication cannot validate source/representation currency;
- withdrawal cannot pretend external copies disappeared;
- actor Access cannot become audience-disclosure authority;
- successor source authority cannot silently regenerate/republish external representations.

# 21. Cross-cluster carry/recheck

These remain later rechecks, not unresolved Cluster-E defects:

- **DIR-036** → 015-I: representation labels/status must not promote source authority;
- **DIR-039** → 015-I: withdrawal/supersession mapping must not imply recall/disappearance;
- **DIR-040** → 015-I: cross-profile actor Access versus audience disclosure;
- **DIR-041** → 015-H: successor source → representation → release chain must not automate discretionary authority;
- full correction chain → 015-H under DIR-044.

015-H begins from the now-verified externalization boundary:

```text
system may propagate known affectedness/currentness
  != system may choose discretionary recognition/declaration/export/release authority
```

# 22. Implementation boundary

015-G does not prescribe:

- file formats;
- PDF generation;
- object storage;
- CDN behavior;
- QR implementation;
- email delivery;
- printer mechanics;
- cache invalidation;
- external-copy revocation;
- URL architecture;
- transport retries;
- publication job orchestration.

```text
Export
  != file-storage architecture

Publication
  != transport implementation

withdrawal
  != remote deletion

representation currency
  != cache state
```

# Exit

**015-G COMPLETE — PASS.**

No semantic correction or upstream reopen is required.

Proceed to **015-H — Cross-Family Application Actions, Chaining, Automation, Lifecycle & Authority Interference**.

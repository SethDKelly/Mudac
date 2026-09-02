# 002-H — Export, Print, Operational Continuity & External Representations

Status: **Complete**

## 1. Purpose

002-H specifies how authoritative or explicitly identified working Competition information is represented outside its source concept and how judging continues when ordinary electronic operation is degraded or unavailable.

The accepted supporting Concept specified here is:

1. Export

Cross-cutting behavior specified here includes:

- source/version traceability for generated representations;
- print-ready Rubrics and paper Scorecards;
- Event and Panel operational materials;
- QR and machine-readable identifiers;
- privacy-safe representation profiles;
- paper-source identification and capture verification;
- mixed paper/electronic operation;
- degraded connectivity and outage fallback;
- recovery and duplicate prevention;
- sensitive local-data requirements;
- regeneration after authoritative correction;
- external publication boundaries for official outcomes.

The central principle is:

```text
Authoritative or explicitly identified source state
        ↓
      Export
        ↓
stable external representation
        ↓
print / file / encoded identifier / publication surface
```

The representation is traceable to its source, but it does **not** become the source of truth merely because it was printed, downloaded, or distributed.

The specification remains implementation-neutral. PDF libraries, browser printing, object storage, CDN services, QR libraries, offline browser technology, local databases, synchronization protocols, and AWS services remain downstream architecture choices.

---

# 2. Export specification

## Purpose

> Produce a stable external representation of identified Competition information while preserving enough source, audience, and generation context to determine what the representation means.

Export exists because Competition information must leave the interactive application in controlled ways for purposes such as:

- printing a Rubric;
- producing paper judging forms;
- distributing Event information;
- producing Panel operational materials;
- generating join/access initiation material;
- preparing ceremony/Award materials;
- producing an external representation of an Official Outcome.

Export does not own the meaning of the source information.

Rubric defines evaluation semantics.

Panel defines current intended Judge grouping.

Official Outcome Revision defines what was officially established.

Export only represents those states externally.

---

# 3. Export state

Conceptually:

```text
Export
    stable export identity
    source subject
    source authority/version reference
    representation profile
    intended audience / disclosure class
    format
    generation time
    generated artifact or representation reference
    status
```

Where appropriate, an Export may also record:

```text
Competition
requested by
purpose
batch identity
paper-form/source references
superseding/replacement relationship
```

`format` may eventually be PDF, printable HTML, image, CSV, encoded QR payload, or another representation. Format is not itself a Concept.

---

# 4. Export actions

Conceptual actions include:

```text
request
validateDisclosure
generate
retrieve
regenerateFromCurrentSource
retireFromOrdinaryUse
```

`regenerateFromCurrentSource` creates a new representation of the newer source state. It does not mutate a previously distributed Export and pretend the earlier material never existed.

## Queries

Useful queries include:

```text
sourceReference
sourceAuthorityState
representationProfile
intendedAudience
generatedAt
isCurrentWithSource
isSafeForAudience
supersededBy
```

---

# 5. Operational principle

An Organizer chooses information to distribute or print. The application resolves the exact source state, validates that the selected representation is appropriate for the intended audience, generates a stable artifact, and preserves enough identity to explain later what source/version the artifact represented.

If the source later changes, previously generated material remains historically attributable to the older source and a new Export is generated for the newer state.

---

# 6. Source authority classes

Not every Export must originate from finalized Competition information, but every Export must make its source authority understandable.

Useful source classes include:

### Working / Draft

Example:

```text
Draft Event Information
    ↓
Organizer review PDF
```

A Draft representation must not masquerade as authoritative event material.

### Authoritative operational

Examples:

```text
Rubric Version 3
    ↓
Judge paper Rubric

Current Panel assignment
    ↓
Panel operational sheet
```

### Official

Example:

```text
Official Outcome Revision 2
    ↓
Award / result publication material
```

The representation profile should make materially different authority levels visible where confusion would be consequential.

---

# 7. Generated artifacts are stable historical representations

Once generated and distributed, an Export should be understood as a representation of a particular source state at a particular time.

Suppose:

```text
Rubric v1
    ↓
Export X
    ↓
50 paper forms printed
```

Then the Organizer creates Rubric v2.

The system must not reinterpret Export X as though it represented v2.

Instead:

```text
Rubric v1 → Export X
Rubric v2 → Export Y
```

This property matters because physical paper may remain in circulation after the source changes.

An implementation may replace an undelivered temporary file for convenience, but the domain cannot erase the identity of a representation once it has become operationally meaningful.

---

# 8. Export and Versioning remain distinct

Versioning answers:

> What authoritative source states existed?

Export answers:

> What external representation was generated from one of those states?

For example:

```text
Rubric lineage
    v1
    v2
    v3

Export lineage/use
    printable form from v1
    event packet from v2
    printable form from v3
```

Generating another PDF does not create another Rubric Version.

Changing the Rubric and committing it does.

---

# 9. Disclosure profile is part of representation semantics

An Export is not safe merely because its source data is valid.

It must also expose only information appropriate to the intended audience.

Conceptually:

```text
Source
   +
Audience / disclosure profile
   ↓
Export
```

This allows the same underlying Competition to produce different legitimate views without duplicating domain state.

Examples include:

### Judge-safe

May include:

```text
Team Alias
Division
Rubric
Panel/event logistics
```

Must exclude ordinary access to:

```text
institution identity
student administrative details
peer Scorecards
peer Notes
Team Aggregate
Rankings
```

### Organizer-sensitive

May include authorized administrative information, Team/Alias mapping, operational exceptions, or reconciliation details.

### Public / publication-safe

Contains only information deliberately approved for external publication.

Judge Notes and private Scorecards are excluded by default.

---

# 10. Least disclosure applies to physical materials

Access control cannot protect information after it has been printed.

Therefore print/export generation must itself enforce disclosure boundaries.

A Judge-facing paper form must not accidentally contain:

```text
School / university
student names
administrative Team label
private Organizer notes
other Judges' scores
```

simply because the Organizer who generated the form was allowed to see those fields.

The source actor's broad Access does not imply the artifact should expose everything they can see.

---

# 11. Metadata and incidental disclosure

Sensitive information should also be avoided in incidental representation surfaces where practical.

Examples include:

```text
file name
PDF title/metadata
print header/footer
QR payload
browser/page title
shared download label
```

For example:

```text
judge-form-university-of-x-team.pdf
```

would defeat identity shielding even if the visible form itself correctly says only `Team 014`.

This requirement should later be included in UX/security review.

---

# 12. Print-ready Rubric

A printable Rubric should be generated from one exact authoritative Rubric Version.

It should contain enough source identity to reconnect it later to the digital definition.

At minimum, this should include or encode:

```text
Competition identity
Rubric identity
Rubric Version
```

A score-bearing form additionally needs enough context to associate the completed paper with the intended evaluation.

Digital and paper layouts do not need to look identical.

They need equivalent **evaluation semantics**.

Paper may legitimately provide more handwriting space, different pagination, larger scoring areas, and print-optimized guidance.

---

# 13. Paper Scorecard representation

A paper Scorecard is a physical capture surface for the same logical Scorecard semantics defined in 002-D.

It should support:

```text
Team Alias
Division
Rubric Version
Criterion scores
Criterion Notes
Overall Note
Judge identification / attribution
Encounter / Panel context where available
paper-source reference
```

The physical form itself is not a separate `PaperScorecard` Concept.

Once captured, it produces the same logical Scorecard evidence as electronic judging while Provenance records the paper origin.

---

# 14. Paper-source identity

Every paper evaluation accepted into official digital capture must acquire a unique source reference sufficient to distinguish it from another physical evaluation.

The preferred path is to generate a unique paper-form/source reference before use.

Conceptually:

```text
Paper Form PF-000184
Rubric v3
Competition 2026
```

The Judge/Team/Encounter context may be pre-filled or completed when the form is issued or collected.

If emergency photocopies or generic blank forms are used, a unique source reference may instead be assigned during Organizer intake before transcription.

The important invariant is:

> Two physical evaluations must not become indistinguishable digital sources.

This supports duplicate detection and correction provenance without requiring every Competition to inventory every unused sheet of paper.

---

# 15. Blank versus pre-associated paper forms

Both patterns are allowed.

### Pre-associated

A form may already identify:

```text
Team 014
Panel 07
Judge J-041
Encounter E-022
```

This improves operational traceability but is less flexible.

### Blank / partially identified

A bulk form may identify only:

```text
Competition
Rubric Version
paper-source reference
```

and have Team/Judge/Encounter information completed at use or intake.

The system must not infer missing evaluation identity from page order or physical stack position.

Before official capture, the evaluation must be unambiguously associated with the correct Judge Participation and Encounter.

---

# 16. Machine-readable identifiers

QR codes or barcodes may improve speed and reduce transcription errors.

Examples include encoding/reference to:

```text
paper-form identity
Competition
Rubric Version
Panel
Team Alias
Encounter
join/access initiation
```

However:

> A machine-readable representation is an encoding mechanism, not authority.

Possessing or scanning a QR code does not itself prove that someone is an authorized Judge or Organizer.

Identity, Participation, and Access remain responsible for authorization.

---

# 17. QR payload privacy

Where practical, machine-readable codes should use opaque or minimally identifying references rather than embedding sensitive human-readable data directly.

For example, a Judge-facing Team QR should not need to encode:

```text
institution name
student names
Organizer-only identifiers
```

if a safe Team/Encounter reference can resolve the necessary context after Access checks.

This limits leakage from photographed, copied, or forwarded codes.

---

# 18. Paper capture workflow

The baseline paper workflow is:

```text
Authoritative printable Rubric/Scorecard
        ↓
Judge completes physical evaluation
        ↓
Organizer receives paper source
        ↓
identity/context verified
        ↓
Organizer transcribes Scorecard
        ↓
transcription checked against source
        ↓
Scorecard finalized as paper-origin evidence
        ↓
Versioning + Provenance
```

The Judge remains the evaluation author.

The Organizer is the capture actor.

---

# 19. Paper capture verification

Because transcription can alter Competition outcomes, a paper-origin Scorecard should not become official eligible evidence until its captured content has been checked against the physical source.

The baseline therefore distinguishes conceptually:

```text
Captured
    ↓
Verified against source
    ↓
eligible authoritative paper-origin Scorecard
```

This verification may be performed by the same Organizer through an explicit review step unless Competition policy requires independent second-person verification.

The specification does not mandate dual entry or two-person verification for every event.

It does require the system to distinguish:

> data has been entered

from:

> data has been checked against the paper source.

This distinction should feed Finalization readiness.

---

# 20. Paper transcription correction

If the physical source says:

```text
Criterion 3 = 9
```

but captured v1 says:

```text
Criterion 3 = 4
```

the Organizer may correct the transcription under 002-E authority rules.

Provenance records:

```text
evaluation author = Judge
capture/correction actor = Organizer
source = paper reference
classification = transcription correction
```

This must remain distinct from the Judge changing their evaluation from 4 to 9.

---

# 21. Paper source retention

002-H does not choose a universal physical-retention period.

It establishes the requirement that Competition policy/operations define how long authoritative paper sources remain available for verification and correction, particularly through Finalization.

The application may later support optional scanned images or attachments of paper Scorecards, but scanning every form is not required by the current Concept specification.

Whatever retention approach is chosen must preserve enough source evidence for the declared verification/correction process.

---

# 22. Event information export

Organizer-authored Event information may generate representations such as:

```text
Judge quick-start guide
Event schedule/instructions
room information
Competition rules summary
```

These should carry sufficient Competition identity and, where relevant, generation/source-date information so stale materials can be recognized.

Event Information remains Competition content rather than another Concept.

---

# 23. Panel operational materials

An Organizer may generate Panel materials containing things such as:

```text
Panel label
current Judge assignments
assigned composition capacities
room/logistics information
Team Alias list or encounter sequence where applicable
join/navigation references
```

These materials represent operational state at generation time.

If Panel membership later changes, previously printed sheets remain historically accurate representations of what was generated but may become operationally stale.

The application should make regenerated material distinguishable from earlier output where confusion is plausible.

---

# 24. Official-outcome representations

002-G established:

```text
Official Outcome Revision
```

as the authoritative internal projection established at Finalization.

002-H allows external representations such as:

```text
ceremony result sheet
Award certificates/list
public result file/page feed
Organizer archive export
```

These must reference one exact Official Outcome Revision.

If Official Outcome v2 later supersedes v1, previously generated v1 material remains historically identifiable rather than silently changing its source basis.

New publication material should be generated from v2.

---

# 25. Publication is separate from Finalization

The official/public boundary remains:

```text
Finalized internally
        ↓
Official Outcome Revision
        ↓
Organizer chooses approved disclosure
        ↓
external/public representation
```

Public disclosure is therefore an explicit action/synchronization, not an automatic side effect of `Competition.finalize`.

This supports:

```text
finalize before ceremony
prepare materials
announce later
```

without reopening the Competition or Judge access.

---

# 26. Public result disclosure defaults

The baseline public result representation should expose only intentionally publishable competition information such as:

```text
Award
winning Team identity appropriate for public release
Division
official placement where intended
```

It should not automatically expose:

```text
Judge identities
individual Scorecards
Judge Notes
Panel scoring patterns
private Team/Alias mapping before intended reveal
Organizer exception notes
administrative investigation history
```

If the Competition chooses to reveal institutional Team identity publicly after judging, that is a deliberate disclosure decision distinct from the Judge-facing anonymity rule that operated during evaluation.

---

# 27. External representation revocation/correction

A distributed physical artifact cannot be remotely erased.

Therefore the system must distinguish:

```text
current authoritative source
```

from:

```text
older external representations still physically existing
```

If an Official Outcome is corrected:

```text
Outcome v1 → Export X
Outcome v2 → Export Y
```

Export X may be marked superseded/obsolete in the system, but the system cannot pretend already printed copies vanished.

Where consequence warrants it, Organizer workflows should identify what replacement material needs regeneration or republication.

---

# 28. Operational continuity principle

Technology degradation must not invalidate judging already performed or force Organizers to improvise source-of-truth rules during the event.

The continuity hierarchy is:

```text
Normal electronic operation
        ↓
Degraded electronic operation
        ↓
Mixed electronic + paper operation
        ↓
Paper fallback
        ↓
Recovery / reconciliation
        ↓
normal authoritative evidence model
```

These are operational modes/processes rather than new Concepts.

---

# 29. Degraded connectivity is expected

A venue may experience:

```text
poor Wi-Fi
cellular congestion
brief device disconnects
partial service interruption
```

The eventual architecture must explicitly state what functions remain safe during each degraded condition.

The UI must always communicate persistence truthfully.

It may never display:

```text
Saved
Finalized
Synced
```

unless the corresponding durability/authority claim is actually true.

---

# 30. Draft durability requirement

002-H preserves the 001-G requirement:

> Reasonable interruption should not destroy already-entered Judge Draft work.

The architecture may eventually satisfy this through server-side rapid persistence, local persistence, offline queues, or another design.

002-H does not choose among them.

It does require the architecture to document:

- when Draft data is durably stored;
- what happens during connectivity loss;
- what the Judge sees while synchronization is pending;
- how conflicts are handled;
- how private locally retained data is later cleared.

---

# 31. Finalization under connectivity uncertainty

Suppose a Judge taps Finalize and the connection fails before the response returns.

The Judge may retry.

The system must converge onto:

```text
one logical Scorecard
one authoritative finalization effect
```

rather than duplicate evaluations.

Similarly, Encounter initiation and paper capture should be duplicate-safe where repeated submission is plausible.

This is a behavioral requirement for later idempotency/concurrency architecture.

---

# 32. Sensitive local data

If the eventual resilience architecture stores Scorecard Drafts or Notes on a Judge device, that local data is still private evaluation data.

The architecture must therefore address:

```text
storage scope
encryption/protection where appropriate
session binding
shared-device behavior
synchronization completion
local expiry/cleanup
Event Completed access cutoff
lost-device/session revocation
```

Event Completed must not leave the application intentionally exposing old private evaluation data merely because a local cache still exists.

The exact secure-storage mechanism remains deferred.

---

# 33. Shared and loaner devices

A shared/loaner device must establish a clean Judge context between users.

The required sequence is conceptually:

```text
Judge A ends / loses active session
        ↓
Judge A private state no longer accessible
        ↓
Judge B verifies
        ↓
Judge B Participation/Access context established
```

No previous Judge Scorecard or Note should remain casually recoverable through ordinary application navigation.

---

# 34. Outage fallback

For a significant outage:

```text
Electronic judging unavailable or unsafe
        ↓
Organizer declares/coordinates fallback
        ↓
authoritative paper materials used
        ↓
Judges continue evaluation
        ↓
paper sources collected
        ↓
later capture + verification
        ↓
same Scorecard model
```

The fallback should be documented operationally before the event rather than invented after an outage begins.

A Competition does not need to become a different Competition merely because it temporarily used paper.

---

# 35. Mixed-mode judging

Electronic and paper judging may coexist during the same Competition and even during the same operational period.

For example:

```text
Panel 01 → electronic
Panel 02 → paper
Panel 03 → mixed due to one device failure
```

All resulting evaluations converge on the same logical Scorecard and eligibility model after valid capture.

Capture channel never changes the mathematical weight of the judgment.

---

# 36. Duplicate prevention during recovery

Mixed-mode recovery creates a specific risk:

```text
Judge starts electronic Draft
connection fails
Judge completes paper form
later electronic Draft reconnects
```

The system must not accidentally create two official votes for the same:

```text
Judge Participation × Encounter
```

002-D already defines one logical Scorecard per obligation.

002-H requires recovery workflows to detect that both records may represent the same obligation and require reconciliation rather than automatically finalizing both.

The Organizer must be able to determine which source represents the Judge's authoritative completed evaluation.

The unused/abandoned source history may be retained as operational evidence where appropriate, but only one logical Scorecard becomes authoritative.

---

# 37. Conflict handling

If two independently edited Draft states exist for the same logical Scorecard, the system must not silently discard one merely because it synchronized last.

The exact conflict algorithm remains architectural, but the behavioral requirement is:

> A conflict that cannot be safely merged must be surfaced for deliberate resolution.

A finalized authoritative Scorecard must never be silently replaced by a stale offline Draft.

This follows the stale-base protection established in 002-E.

---

# 38. Operational health visibility

Organizers need Competition-relevant health rather than low-level infrastructure telemetry.

Potential operational indicators include:

```text
Judges currently unable to sync
pending paper capture
captured but unverified paper evaluations
Scorecards awaiting synchronization, where knowable
failed Export generation
recent service degradation
fallback mode in use
```

Exact observability architecture remains deferred.

The requirement is that Organizers can recognize operational risk before Finalization rather than discovering missing evidence during Award determination.

---

# 39. Continuity readiness before Competition Ready

Competition readiness should eventually include an operational-continuity check such as:

- authoritative Rubric available;
- printable fallback Rubric/Scorecard generation tested or available;
- Organizer understands paper intake/capture path;
- relevant source/version identifiers can be represented on paper;
- access/join fallback is understood;
- recovery responsibility is assigned operationally.

This need not mean that hundreds of forms must always be preprinted.

It means the Competition has a credible fallback path before live judging begins.

---

# 40. Export failure does not mutate source state

If PDF or other representation generation fails:

```text
Rubric v3
```

remains Rubric v3.

An Export-generation error cannot partially change:

```text
Rubric
Scorecard
Panel
Official Outcome
```

The failure is external-representation failure and should be retryable without corrupting the source.

---

# 41. Export regeneration after correction

When authoritative state changes, the system should be able to identify materially affected external representations.

Examples:

```text
Rubric v1 → v2
    ↓
old printable judging form becomes stale

Panel membership changed
    ↓
old Panel sheet becomes stale

Official Outcome v1 → v2
    ↓
old result/Award material becomes superseded
```

This does not require automatically destroying or regenerating everything.

It requires traceability so Organizers can understand which artifacts reflect older source state.

---

# 42. Export provenance

Generation of consequential operational or official external material should itself be meaningfully attributable.

Useful provenance includes:

```text
who requested/generated
what source/version was represented
which disclosure profile was used
when it was generated
what it superseded, where applicable
```

This is particularly valuable for:

- Rubric paper packets;
- paper Scorecard batches;
- Organizer-sensitive mappings;
- official Award/result publication artifacts.

Ordinary ephemeral screen rendering need not become a permanent Export/Provenance event.

---

# 43. Export is not every view

A normal application screen rendering is not automatically an Export.

Export applies when the application intentionally creates a stable external representation for distribution, printing, transfer, or publication.

Therefore:

```text
Judge Scorecard screen
```

is a UI projection.

```text
Generated printable Scorecard PDF
```

is an Export.

This avoids turning every web response into a historical artifact.

---

# 44. Download does not imply retention forever

The system may apply retention rules to generated digital artifacts independently of the authoritative source.

For example, an old generated temporary PDF may eventually be removed from object storage while the system retains:

```text
Export metadata
source/version relationship
regeneration ability where appropriate
```

The exact retention policy remains architectural/operational.

Deleting an expired generated file must not erase the authoritative Rubric, Scorecard, or Official Outcome history from which it came.

---

# 45. Operational continuity does not create another scoring model

A major invariant is:

```text
Electronic judging
Paper judging
Recovered offline judging
```

all converge to:

```text
one Scorecard model
one Rubric semantics
one eligibility model
one aggregation policy
```

Continuity changes **capture mechanics**, not evaluation meaning.

This prevents fallback operation from becoming a second informal competition system.

---

# 46. Explicit non-responsibilities

Export does not:

- define Rubric semantics;
- determine who may judge;
- authenticate QR possession;
- alter Scorecard authorship;
- calculate Aggregate or Rank;
- decide Award winners;
- finalize the Competition;
- make official data public automatically;
- guarantee that already distributed physical copies can be revoked;
- determine retention policy by itself.

Operational continuity does not:

- fabricate missing scores;
- bypass Scorecard finalization rules;
- bypass Access;
- turn stale local data into authoritative state automatically;
- allow duplicate votes during recovery.

---

# 47. 002-H invariants

002-H adds or confirms these major invariants:

1. Export represents identified source state; it does not become the source of truth.
2. Every consequential Export is traceable to its source authority/version where applicable.
3. Previously distributed Export content is not silently reinterpreted after source change.
4. New source state produces a new external representation rather than mutating historical meaning.
5. Export and Versioning remain distinct.
6. Representation disclosure is audience-specific and follows least disclosure.
7. Judge-facing external materials do not expose institutional/admin identity by default.
8. Sensitive data should not leak through filenames, metadata, headers, or encoded payloads where avoidable.
9. Printable Rubrics identify their Competition/Rubric Version basis.
10. Paper and electronic Scorecards share identical evaluation semantics.
11. Every paper evaluation accepted for official capture has a unique source reference.
12. Paper evaluation identity must be unambiguous before official capture.
13. QR/barcode possession never independently grants authority.
14. Paper-origin Scorecards preserve Judge authorship and Organizer capture actor.
15. Captured paper evaluation must be checked against the source before official eligibility.
16. Transcription correction remains distinct from Judge amendment.
17. Public result representation references one exact Official Outcome Revision.
18. Competition Finalization and public publication remain separate.
19. Judge Notes/individual private Scorecards are excluded from public publication by default.
20. Distributed physical artifacts cannot be treated as remotely revocable.
21. Technology degradation never changes evaluation semantics.
22. Draft persistence/synchronization state must be communicated truthfully.
23. Finalization retry cannot create duplicate logical Scorecards.
24. Sensitive local Judge data must respect access/session lifecycle requirements.
25. Shared-device transition cannot expose the previous Judge's ordinary private state.
26. Paper fallback is a supported continuity path, not a lower-weight evaluation channel.
27. Mixed paper/electronic operation is valid.
28. Recovery cannot create multiple official Scorecards for one Judge × Encounter obligation.
29. Unresolvable concurrent Draft conflicts are surfaced rather than silently discarded.
30. A stale Draft cannot silently replace a newer authoritative Scorecard.
31. Organizers need visibility into operational evidence/capture risks before Finalization.
32. Export failure never mutates authoritative source state.
33. Authoritative corrections can identify affected/stale external representations.
34. Export provenance records consequential generation context.
35. Normal UI rendering is not automatically an Export.
36. Retention/deletion of generated files never erases authoritative domain history.

---

# 48. Phase 002 operational chain after 002-H

The complete operational path can now be represented as:

```text
Competition configuration
        ↓
authoritative Rubric / Evaluation Policy
        ↓
Judge Participation + Panel
        ↓
Judging Encounter
        ↓
┌─────────────────────────────┐
│                             │
▼                             ▼
Electronic capture        Paper capture
│                             │
│                        source identity
│                             │
│                        transcription
│                             │
│                         verification
│                             │
└──────────────┬──────────────┘
               ▼
          Scorecard
               ↓
     Versioning + Provenance
               ↓
 eligible authoritative evidence
               ↓
      Coverage + Aggregate
               ↓
         Division Rank
               ↓
         Reconciliation
               ↓
            Awards
               ↓
         Finalization
               ↓
   Official Outcome Revision
               ↓
             Export
               ↓
  approved external representation
```

At any point during live judging:

```text
normal electronic operation
        ↓ degradation
safe degraded behavior / paper fallback
        ↓ recovery
same authoritative Scorecard model
```

The capture channel changes; the meaning of the judgment does not.

---

# 49. Open implementation questions preserved

002-H intentionally leaves these questions open for later architecture/UX work:

- whether the Judge application is a PWA;
- whether Drafts use browser-local persistence;
- whether locally persisted data is encrypted and how keys are managed;
- exact offline capability versus degradation-only support;
- synchronization queue/conflict technology;
- exact PDF generation library/service;
- object-storage and artifact-retention design;
- QR payload structure and signing/expiration;
- whether paper Scorecards are scanned/attached;
- whether some Competitions require two-person paper verification;
- exact physical paper-retention period;
- exact public publication channel;
- whether publication has an independent approval workflow;
- exact fallback kit/material quantity.

These are now bounded by behavioral requirements rather than left unconstrained.

---

# 50. 002-H Exit Position

002-H completes the specification of the fifteenth accepted Concept, Export, and closes the paper/continuity loop that began in Phase 001.

The central result is:

```text
SOURCE OF TRUTH
    remains internal authoritative state

EXTERNAL REPRESENTATION
    is stable, audience-safe, source-traceable output

CAPTURE CHANNEL
    may be electronic or paper

OPERATIONAL FAILURE
    changes the path, not the evaluation semantics
```

This means the Competition can survive:

- phone interruption;
- weak venue connectivity;
- an individual device failure;
- partial system degradation;
- full temporary electronic outage;
- mixed paper/electronic judging;
- later paper reconciliation;
- corrected Rubrics or Official Outcomes;

without inventing a second scoring model or losing historical traceability.

The remaining Phase 002 group is therefore **002-I — Phase 002 Consolidation & Specification Exit Review**.

002-I should reconcile 002-A through 002-H as one specification, test the concept and synchronization contracts for contradictions, enumerate the authoritative policy/configuration catalog, consolidate invariants and unresolved extension points, verify that all 15 accepted Concepts are sufficiently specified, and determine whether the design is ready to proceed into conceptual UX/application architecture without reopening core domain semantics.

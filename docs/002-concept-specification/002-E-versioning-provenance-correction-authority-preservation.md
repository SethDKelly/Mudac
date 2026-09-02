# 002-E — Versioning, Provenance, Correction & Authority Preservation

Status: **Complete**

## 1. Purpose

002-E specifies how MUDAC preserves authoritative history while still permitting legitimate correction.

Accepted supporting concepts specified here:

1. Versioning
2. Provenance

Cross-cutting behavior specified here:

- authoritative-version semantics;
- correction classification;
- authorship versus capture versus correction authority;
- amendment authority by Competition lifecycle;
- paper transcription correction;
- structural misattribution and invalidation;
- stale-update protection;
- downstream dependency invalidation;
- post-event and post-finalization correction discipline.

The central distinction is:

```text
Versioning
    What authoritative states existed?

Provenance
    How, why, and through whose authority did those states arise?
```

A third principle governs correction:

> Authority follows the semantic meaning of the change.

A Judge may revise their own evaluation judgment. An Organizer may correct a demonstrable paper transcription error. An Organizer may not create a new Judge judgment merely because the Organizer has broad Competition administration authority.

The specification remains implementation-neutral. Event sourcing, append-only tables, temporal databases, cryptographic hashing, database isolation levels, object storage, audit products, and AWS services remain downstream architecture choices.

---

## 2. Controlled finality model

MUDAC deliberately rejects both extremes:

```text
mutable current row
    where history disappears
```

and:

```text
absolute immutability
    where legitimate error cannot be corrected
```

The preferred model is controlled finality:

```text
Working state
      ↓
Authoritative version 1
      ↓
explicit correction / amendment
      ↓
Authoritative version 2
      ↓
prior version remains historical
```

Once an authoritative version is committed, that version is immutable as a historical fact. Correction creates a successor rather than editing the prior snapshot in place.

This does not mean every domain object must be versioned. Versioning is composed only where successive authoritative states are meaningful. Rubric and Scorecard are the first confirmed uses.

---

# 3. Versioning specification

## Purpose

> Preserve successive authoritative states of a subject that may legitimately change without erasing what was previously authoritative.

Versioning exists so an authorized user can answer:

- what is authoritative now?
- what was authoritative before?
- which version did a historical action use?
- what changed between two authoritative states?

## State

Conceptually:

```text
Version lineage
    stable subject / lineage reference
    committed versions
        version identity
        predecessor version
        immutable authoritative snapshot
        sequence / ordering
    current authoritative version
```

Commit metadata such as actor, reason, and capture source belongs primarily to Provenance rather than being duplicated as business meaning inside Versioning.

## Actions

Conceptual actions:

```text
initializeLineage
commitInitialVersion
commitSuccessor
currentVersion
versionByIdentity
history
compare
```

A commit takes a complete authoritative snapshot. It is not merely a patch that becomes unintelligible without replaying every prior edit.

Implementation may internally store deltas, but the conceptual contract is that any committed version can be reconstructed exactly.

## Operational principle

A user works with concept-owned Draft state. When that state is ready to become authoritative, the application commits an immutable Version. Later legitimate correction begins from the current authoritative state and, when completed, commits a successor. The previous Version remains addressable and unchanged.

---

## 4. Drafts are not authoritative versions

Versioning should not create a new historical Version for every keystroke or autosave.

For example:

```text
Scorecard Draft
    score 3
    score 4
    note edited
    score 5
```

remains one working Draft.

Only:

```text
Scorecard.finalize
```

creates an authoritative Scorecard Version.

Likewise a Rubric may undergo many Draft edits before an Organizer establishes an authoritative Rubric Version.

This keeps history meaningful instead of turning it into UI telemetry.

---

## 5. Committed versions are immutable

Once Version 1 exists:

```text
v1
```

its contents do not change.

Correction produces:

```text
v1
 ↓
v2
```

not:

```text
v1 edited in place
```

This invariant applies even if the correction appears trivial, because historical Scorecards, paper exports, ranking calculations, and Organizer decisions may have relied on the earlier state.

---

## 6. One current authoritative version

A Version lineage has at most one current authoritative committed Version.

Conceptually:

```text
v1 — historical
v2 — historical
v3 — current authoritative
```

Prior versions are not deleted and are not treated as additional current votes or policies.

For a Scorecard, only the current authoritative Scorecard Version may ordinarily contribute to downstream aggregation.

For a Rubric, historical Scorecards remain bound to the exact historical Rubric Version they used even after a later Rubric Version becomes current for future use.

---

## 7. Linear authoritative history and stale-update protection

The initial model uses a single authoritative lineage rather than branching authoritative histories.

Suppose two correction sessions both begin from Scorecard v1:

```text
Correction A based on v1
Correction B based on v1
```

If A commits v2 first, B must not later silently commit another successor as though v1 were still current.

Conceptually `commitSuccessor` therefore includes an expected-current precondition:

```text
commit successor
only if
expected current version == actual current version
```

If not, the later correction must reload/review the new authoritative state before proceeding.

This prevents lost updates without choosing a database locking technology.

---

## 8. Version numbers are identifiers, not semantic promises

A human-facing sequence such as:

```text
v1
v2
v3
```

is useful for explanation.

002-E does not require semantic-versioning rules such as `1.2.3`, nor does a version number itself say whether a change was editorial, scoring-semantic, corrective, or administrative.

That meaning belongs to Provenance and domain-specific change classification.

---

# 9. Provenance specification

## Purpose

> Preserve the meaningful origin, authority, and transformation history necessary to explain an authoritative Competition record.

Provenance exists because "who last edited this row" is insufficient for judging integrity.

The system may need to answer:

- Which Judge authored this evaluation?
- Who entered the paper form?
- Was this a Judge amendment or a transcription correction?
- Which source justified the correction?
- Who authorized post-event Judge access?
- Which Rubric Version was established, and by whom?
- Why was an Encounter invalidated?
- Why did an official outcome require reconsideration?

## State

Conceptually, a meaningful Provenance event contains enough of the following to explain the action:

```text
Provenance event
    target subject / version
    event classification
    acting Identity / Participation
    represented author or authority, if different
    timestamp
    Competition scope
    prior authoritative version, if applicable
    resulting authoritative version, if applicable
    capture / source channel, if applicable
    source reference, if applicable
    authorization / approver reference, if applicable
    reason or rationale, when required
    relationship to correction / replacement / invalidation
```

Not every field applies to every event.

## Actions

Conceptual actions:

```text
record
historyFor
originOf
traceVersion
traceCorrection
traceReplacement
```

A Provenance event is itself historical evidence and must not be silently rewritten. If a provenance statement is discovered to be incorrect, correction should append another attributable provenance event rather than editing the original history invisibly.

## Operational principle

When a meaningful domain action establishes, changes, invalidates, or replaces authoritative state, the application records enough provenance to reconstruct who acted, whose authority the resulting content represents, why the action occurred, and what prior state or source it depended on.

---

## 10. Provenance is not telemetry

MUDAC does not need domain provenance for every interaction.

Usually not provenance:

```text
Judge opened page
Judge expanded guidance
Judge typed then deleted Draft text
Organizer sorted a table
browser retried a GET request
```

Strong provenance candidates include:

```text
Rubric Version established
Scorecard finalized
Scorecard amended
paper evaluation captured
paper transcription corrected
Division corrected
Alias replaced
Panel membership changed during operation
Encounter participant obligation adjusted
Encounter invalidated / replacement established
coverage exception authorized
Award conferred or corrected
Competition finalized
post-finalization correction initiated
break-glass access used for Competition-sensitive data
```

Low-level security/audit telemetry may exist separately. Provenance is the human-meaningful history of domain authority.

---

# 11. Four authority roles in a change

002-E standardizes four roles that must not be conflated.

## Evaluation / content author

Whose substantive judgment or authored content does the record represent?

For a Scorecard:

```text
Judge Participation
```

## Acting actor

Who performed the application action?

For electronic judging this is normally the same Judge.

For paper transcription it is normally an Organizer.

## Capture actor / channel

Who converted an externally authored record into digital form, and through what channel?

For paper:

```text
capture actor = Organizer
capture channel = Paper
```

## Authorizer / approver

Who granted exceptional authority for an action that ordinary Access would not permit?

For example:

```text
Organizer authorizes temporary post-event Judge amendment access
```

These roles may coincide, but the model must not assume they always do.

---

# 12. Authority-preservation principle

The most important rule in 002-E is:

> A correction actor may correct only the kind of fact for which that actor has legitimate authority.

Examples:

### Judge authority

A Judge has semantic authority over their own evaluation judgment.

They may, when Access permits, change:

```text
Criterion scores
Criterion Notes
Overall Note
```

through a Scorecard amendment.

### Organizer authority

An Organizer has authority over Competition configuration and operational reconciliation.

They may correct:

```text
Division assignment
Alias assignment
Panel configuration
paper transcription
Encounter operational status
Award conferral
Competition lifecycle
```

subject to lifecycle and later policy.

### Organizer does not inherit Judge judgment authority

An Organizer does **not** ordinarily have authority to decide:

```text
Judge J-041 meant to score 5 instead of 3
```

on an electronic Scorecard.

If the Judge cannot be reached, the Organizer may later invalidate/exclude the evaluation according to policy, but should not synthesize a replacement Judge judgment.

### Administrator authority

Technical Administrator authority does not substitute for either Organizer or Judge semantic authority.

A break-glass technical action may repair system integrity, but it must not be represented as if an Administrator made the Competition or evaluation decision themselves.

---

# 13. Correction classification

002-E distinguishes at least five correction classes.

## 13.1 Working Draft edit

The authoritative record has not yet been established.

Examples:

```text
Judge changes Draft score 3 → 4
Organizer edits Draft Rubric wording
```

Behavior:

- no new authoritative Version;
- no domain correction Provenance required for each edit;
- normal Access applies.

## 13.2 Author amendment

The original author changes an already-authoritative substantive judgment/content.

Primary example:

```text
Judge changes finalized Scorecard
```

Behavior:

- previous Version remains historical;
- amendment is based on current authoritative Version;
- successor Version committed when finalized;
- Provenance classification = author amendment;
- downstream derived state refreshes.

## 13.3 Capture / transcription correction

The digital record does not accurately represent an external authoritative source.

Example:

```text
Paper says 9
Digital entry says 4
```

Behavior:

- this is **not** a Judge changing judgment;
- Organizer may correct against the retained/verifiable source;
- if the digital Scorecard was already finalized, correction creates a successor Scorecard Version;
- evaluation author remains the Judge;
- acting/capture actor remains attributable to Organizer;
- Provenance identifies the change as transcription correction and references the source where possible.

## 13.4 Structural correction

The record is bound to the wrong structural subject/context.

Examples:

```text
wrong Team
wrong Encounter
wrong Judge attribution
wrong Rubric basis
```

These are not ordinary Scorecard amendments because 002-D makes those bindings structural identity.

Behavior should preserve the incorrect historical record and use explicit invalidation/replacement/rebinding workflows appropriate to the affected concepts rather than silently mutating identity.

For example, a Scorecard attributed to the wrong Encounter may be invalidated for official use and a correctly bound replacement Scorecard established with provenance.

The exact eligibility consequences are specified in 002-F.

## 13.5 Outcome-affecting administrative correction

A legitimate administrative fact changes after it has already influenced derived or official outcomes.

Examples:

```text
Division corrected after scoring
Encounter invalidated after aggregation
paper transcription corrected after provisional ranking
```

Behavior:

- source correction is preserved through appropriate concept + Versioning/Provenance;
- affected derived values are marked for recomputation/review;
- already-conferred official recognition does not silently migrate to another Team;
- 002-G defines final outcome reconciliation and post-finalization handling.

---

# 14. Scorecard author amendment by lifecycle

## Competition Active

The authoring Judge may amend their own finalized Scorecard while ordinary Access remains active, subject to Competition policy.

Baseline behavior:

```text
Finalized v1
    ↓
beginAmendment
    ↓
Amendment Draft
    ↓
finalizeAmendment
    ↓
Finalized v2
```

The system records the change as an author amendment.

A free-text explanation may be optional during the Active event because differences between versions are themselves preserved and excessive friction can interfere with live judging.

## Event Completed

Ordinary Judge evaluation Access has expired under 002-B.

To amend:

```text
Organizer identifies legitimate need
        ↓
Organizer authorizes scoped correction
        ↓
Judge re-verifies Identity
        ↓
temporary Access to specific Scorecard
        ↓
Judge amends
        ↓
new Version + Provenance
        ↓
temporary Access expires
```

A human-readable correction reason is required at this stage.

## Competition Finalized

A Scorecard amendment is no longer an ordinary reconciliation action.

It requires an explicit post-finalization correction path with:

- authorized Organizer initiation;
- Judge re-verification where Judge judgment is changing;
- narrowly scoped Access;
- required reason;
- complete Provenance;
- identification of affected official outcomes;
- subsequent Organizer re-reconciliation under 002-G.

Finalization therefore increases authority requirements without making correction impossible.

---

# 15. Organizer handling of electronic Scorecards

For a finalized electronic Scorecard, the Organizer may inspect and facilitate correction but should not ordinarily edit the Judge's substantive evaluation content.

Preferred handling when a probable Judge mistake is identified:

```text
Organizer flags issue
       ↓
Judge amends own Scorecard
```

If the Judge cannot or will not amend:

```text
Organizer may leave evaluation intact
or
use an explicit invalidation/exclusion policy if justified
```

The Organizer should not replace the value with what they believe the Judge intended.

This preserves the principle that administrative authority does not substitute for evaluation authorship.

---

# 16. Paper transcription correction

Paper requires a distinct authority path because the Judge authored the physical evaluation while the Organizer may be responsible for digital capture.

Example:

```text
Paper source:
Criterion 2 = 5

Digital v1:
Criterion 2 = 3
```

The Organizer is authorized to correct the **capture fact** because the correction can be verified against the paper source.

Result:

```text
Scorecard v1
    historical digital transcription

Scorecard v2
    corrected transcription
```

Provenance explains:

```text
evaluation author = Judge
capture/correction actor = Organizer
classification = transcription correction
source = paper evaluation reference
change = 3 → 5
```

The system must never mislabel this as a Judge amendment.

If the paper source itself was changed by the Judge, that is a Judge evaluation amendment and must be represented accordingly.

---

# 17. Source evidence and verification

Where a correction claims that the previous digital record mismatched an external source, the source should be identifiable where practical.

Potential sources include:

```text
paper Scorecard
Organizer registration record
Competition configuration record
other retained authoritative artifact
```

002-E does not require a particular storage mechanism or mandate scanning every paper form.

The principle is:

> A correction whose authority depends on an external source should be explainable by reference to that source rather than by assertion alone.

---

# 18. Structural misattribution must not be disguised as content amendment

Suppose an evaluation was recorded as:

```text
Judge J-041
Encounter E-014
Team 014
Rubric v2
```

but it actually belongs to Encounter E-021.

Changing the Encounter reference inside a Scorecard Version would rewrite the identity of what the historical record represented.

Instead the system should preserve the mistake and create an explicit correction relationship, such as:

```text
incorrect record
    ↓ invalidated / superseded for official use
correctly bound replacement
```

with Provenance connecting the two.

The same principle applies to wrong-Team, wrong-Judge, or wrong-Rubric structural attribution.

Exact replacement mechanics can differ by affected concept; the important invariant is that structural identity is never silently rewritten.

---

# 19. Invalidation versus version supersession

These ideas must remain distinct.

## Supersession

Means:

> A newer authoritative Version of the same logical subject now replaces an earlier Version.

Example:

```text
Scorecard v1
   ↓ amended
Scorecard v2
```

The logical Scorecard remains valid; v2 is current.

## Invalidation

Means:

> This record or occurrence should no longer be treated as valid evidence for the relevant official purpose.

Example:

```text
Encounter E-014
   ↓
Invalidated
```

or an incorrectly attributed evaluation being excluded from official use.

Invalidation does not create a new version merely to hide the old state. The invalidated evidence remains historical.

002-F specifies how invalidation affects aggregation and coverage.

---

# 20. Versioning does not decide domain validity

The Versioning concept answers:

```text
what versions exist?
which version is current?
```

It does not answer:

```text
should this Scorecard count?
should this Encounter be valid?
is this Rubric version comparable?
```

Those are domain and policy questions handled by Scorecard/Encounter semantics and 002-F.

This prevents Versioning from becoming a generic business-state engine.

---

# 21. Rubric version authority

Rubric Draft editing remains ordinary working state.

When an Organizer establishes an authoritative Rubric version:

```text
Rubric Draft
    ↓
Versioning.commit
    ↓
Rubric v1 authoritative
    ↓
Provenance.record
```

A later change always creates another Version.

Existing Scorecards never rebind from v1 to v2.

## Before judging

New Rubric Versions may be established through normal Organizer authority while Competition readiness is re-evaluated as necessary.

## During Active judging

A scoring-semantic Rubric change becomes high consequence.

It must:

- create a new Version;
- preserve the previous Version;
- never alter existing Scorecards;
- use explicit Organizer authority;
- record a reason;
- surface that multiple Rubric versions may now exist in active judging;
- defer comparability/aggregation consequences to 002-F.

## Event Completed / Finalized

New Rubric Versions must not be used to reinterpret historical Scorecards retroactively.

Post-event corrections to Rubric metadata may be documented, but scoring meaning used by completed Scorecards remains the exact historical Version.

---

# 22. Meaningful change classification for Rubrics

Provenance should distinguish at least:

```text
editorial revision
scoring-semantic revision
```

Examples of scoring-semantic revision include:

- score range change;
- weight change;
- Criterion addition/removal;
- material scoring-anchor change;
- N/A behavior change;
- Scorecard calculation change.

This classification does not itself decide comparability. 002-F consumes it as evidence when determining whether mixed-version Scorecards can participate in the same aggregate.

---

# 23. Reason requirements scale with consequence

Not every change needs a free-text explanation.

002-E establishes the following baseline:

### Draft changes

No reason required.

### Active-event author amendment

Change classification and version difference are always recorded; free-text reason may remain optional.

### Active-event administrative correction to authoritative state

A reason is required when the correction is not self-evident from a verifiable source.

### Event Completed correction

Human-readable reason required.

### Competition Finalized correction

Human-readable reason required, plus explicit post-finalization classification and affected-outcome review.

This provides increasing governance without imposing unnecessary friction on every live-event edit.

---

# 24. Downstream dependency invalidation

When authoritative source state changes, derived state based on it must not remain silently stale.

Examples:

```text
Scorecard v1 → v2
    ↓
Team Aggregate must refresh
    ↓
Rank may change
```

```text
Division corrected
    ↓
ranking population changes
```

```text
Encounter invalidated
    ↓
Coverage and Aggregate change
```

Conceptually, meaningful authoritative changes emit a synchronization signal that causes dependent projections to be recomputed or marked affected.

The source concept does not calculate every downstream result itself.

---

# 25. Official outcomes must not silently mutate

Before Competition Finalized, derived values such as Aggregate and Rank may refresh automatically because they are provisional.

After Competition Finalized, a source correction may imply that official outcomes are no longer supported by the same evidence.

The system must not silently:

```text
move an Award to another Team
publish a different official winner
pretend prior finalization never happened
```

Instead the correction must cause the affected official outcome to enter an explicit review/reconciliation condition.

002-G specifies the exact finalization and official-outcome behavior.

---

# 26. Competition finalization does not erase correction capability

Finalized means:

```text
ordinary correction authority closed
```

not:

```text
all records physically immutable forever
```

A genuine post-finalization error can still be corrected through stronger governance.

At minimum, such correction requires:

- an authorized Organizer context;
- explicit correction purpose;
- required reason;
- preserved pre-correction state;
- appropriate author involvement when semantic authorship belongs to a Judge;
- complete Provenance;
- downstream impact review;
- official outcome re-confirmation where affected.

This preserves both practical recoverability and historical trust.

---

# 27. Temporary Access and correction authority remain separate

A temporary Access grant answers:

> May this Judge currently open and amend this Scorecard?

It does not itself answer:

> Is the resulting amendment legitimate or authoritative?

The amendment must still satisfy Scorecard rules, Versioning preconditions, and Provenance requirements.

Likewise Organizer Access to view all Scorecards does not automatically grant semantic authority to rewrite them.

This keeps 002-B Access and 002-E authority preservation complementary rather than redundant.

---

# 28. Break-glass actions

An exceptional technical or administrative action may sometimes be necessary to restore system integrity.

Examples might include:

```text
recovering from data corruption
revoking compromised access
restoring a failed authoritative reference
```

Break-glass behavior must:

- be narrowly scoped;
- be attributable;
- record purpose/reason;
- preserve prior state where possible;
- avoid representing technical action as Competition or Judge judgment;
- trigger review if Competition-sensitive authoritative content was affected.

002-E does not define a separate BreakGlass concept.

It is an exceptional Access + Provenance pattern.

---

# 29. Correction is not a new concept

Many concepts can be corrected:

```text
Division
Alias
Panel membership
Encounter participation
Rubric
Scorecard
Award
Competition outcome
```

But their correction purposes and semantic authorities differ.

A generic `Correction` concept would risk erasing these differences.

Therefore correction remains a **cross-concept behavioral pattern** composed from:

```text
domain concept
+
Access
+
Versioning where applicable
+
Provenance
+
policy
```

This preserves Concept Design singularity.

---

# 30. Versioning and Provenance synchronization contracts

## Scorecard initial finalization

```text
Scorecard.finalize
        ↓
Versioning.commitInitialVersion
        ↓
Provenance.record(
    evaluation author,
    acting/capture actor,
    channel,
    Rubric basis,
    Encounter
)
        ↓
derived evaluation state refreshes
```

## Scorecard author amendment

```text
begin from current authoritative Version
        ↓
Judge edits Amendment Draft
        ↓
Scorecard.finalizeAmendment
        ↓
Versioning.commitSuccessor(expected current)
        ↓
Provenance.record(author amendment)
        ↓
derived state refreshes
```

## Paper transcription correction

```text
verified paper source
        ↓
Organizer corrects captured Scorecard
        ↓
Versioning.commitSuccessor
        ↓
Provenance.record(
    evaluation author = Judge,
    correction actor = Organizer,
    classification = transcription correction,
    source reference
)
        ↓
derived state refreshes
```

## Rubric publication/revision

```text
valid Rubric working state
        ↓
Versioning.commit
        ↓
Provenance.record(
    Organizer,
    change classification,
    reason where required
)
```

## Structural invalidation/replacement

```text
misattribution or invalid occurrence identified
        ↓
Organizer-authorized invalidation/correction
        ↓
original evidence preserved
        ↓
replacement established if appropriate
        ↓
Provenance links original and replacement
        ↓
002-F eligibility/aggregation refresh
```

---

# 31. Queries the application must eventually support

From the Versioning/Provenance model, authorized Organizer workflows should eventually be able to answer questions such as:

```text
What is the current authoritative Scorecard version?
What did v1 contain?
What changed in v2?
Who authored the evaluation?
Who captured it?
Was the change a Judge amendment or transcription correction?
Why was the change made?
What source justified the correction?
Which Rubric version was used?
Was an Encounter later invalidated?
What replacement superseded it operationally?
Which derived outcomes may have been affected?
```

These are domain reconstruction requirements, not merely debugging conveniences.

---

# 32. 002-E invariants

1. Committed authoritative Versions are immutable historical snapshots.
2. Correction creates a successor Version rather than editing a committed Version in place.
3. Draft/autosave edits are not authoritative Versions.
4. A Version lineage has at most one current authoritative committed Version.
5. Authoritative Version history is linear in the initial model; stale-base commits cannot silently fork it.
6. Any committed Version must remain exactly reconstructible.
7. Versioning does not decide domain eligibility or validity.
8. Provenance records meaningful domain authority events rather than every UI interaction.
9. Provenance events cannot be silently rewritten; corrections to provenance are themselves attributable history.
10. Evaluation author, acting actor, capture actor, and authorizer are distinct roles even when one person fills several of them.
11. A correction actor may change only facts within that actor's semantic authority.
12. Organizer administration authority does not substitute for Judge evaluation authorship.
13. Technical Administrator authority does not substitute for Organizer or Judge semantic authority.
14. Judge amendments preserve the same logical Scorecard and create a successor authoritative Version.
15. Paper transcription correction preserves Judge authorship and identifies Organizer capture/correction authority.
16. Structural identity errors are not silently repaired through ordinary Scorecard amendment.
17. Supersession and invalidation are distinct.
18. An invalidated record remains historically preserved.
19. Existing Scorecards never silently rebind to a newer Rubric Version.
20. Scoring-semantic Rubric changes during Active judging require explicit attributable authority and do not alter prior evaluations.
21. Corrections after Event Completed require stronger authority and a human-readable reason.
22. Corrections after Competition Finalized require explicit post-finalization governance and affected-outcome review.
23. Temporary Access does not itself confer semantic authorship authority.
24. Authoritative source changes must cause affected derived state to recompute or become explicitly stale/affected.
25. Official post-finalization Awards/outcomes never silently migrate because an underlying source changed.
26. Break-glass actions are exceptional, scoped, attributable, and cannot masquerade as Competition judgment.

---

# 33. Questions intentionally deferred

002-E leaves the following for later groups or architecture:

- exact Scorecard invalidation/exclusion policy and its effect on Coverage/Aggregation — 002-F;
- mixed Rubric-version comparability — 002-F;
- exact official-outcome stale/reconciliation states — 002-G;
- whether post-finalization correction requires second-Organizer approval — policy refinement / 002-G;
- Award versioning versus provenance-only correction — 002-G;
- exact retention duration for historical Versions and Provenance;
- cryptographic integrity / hashes / signatures;
- storage representation for paper-source evidence;
- event-sourcing versus snapshot persistence;
- database concurrency/transaction mechanisms;
- infrastructure audit-log integration.

These are not blockers to the behavioral model.

---

# 002-E Exit Position

002-E establishes a complete authority-preserving correction model without adding another Concept.

The core pattern is:

```text
DOMAIN AUTHOR
      │
      │ creates meaningful content
      ▼
AUTHORITATIVE VERSION
      │
      ├──────────────► PROVENANCE
      │                   │
      │                   └── who / how / why / source
      │
      │ legitimate correction
      ▼
SUCCESSOR VERSION
```

And the semantic-authority boundary is:

```text
Judge
    may change Judge judgment

Organizer
    may change Competition-admin facts
    and verified capture facts

Administrator
    may maintain technical integrity

None automatically substitutes
for another's substantive authority
```

That distinction is particularly important for judging trust. The system can remain correctable without allowing an Organizer to silently rewrite a Judge's evaluation, and it can remain auditable without turning every ordinary Draft edit into permanent history.

002-F — **Aggregation, Coverage, Ranking & Evaluation Policy** can now consume a precise source model:

```text
current authoritative Scorecard Versions
+
Encounter validity / effective obligations
+
Rubric-version meaning
+
correction/invalidation Provenance
        ↓
Eligibility
Coverage
Aggregation
Ranking
```

002-F can therefore define competition mathematics and eligibility without having to guess which version of an evaluation counts or whether a correction represented Judge judgment, transcription repair, or structural invalidation.

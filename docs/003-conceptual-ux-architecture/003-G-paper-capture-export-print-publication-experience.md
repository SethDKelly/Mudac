# 003-G — Paper Capture, Export, Print & Publication Experience

Status: **Complete**

## 1. Purpose

003-G defines the Organizer experience at the boundary between MUDAC's authoritative internal state and physical/external representations.

It covers two related but distinct directions of travel:

```text
physical evidence
      ↓
Paper capture / verification
      ↓
authoritative internal Scorecard evidence
```

and:

```text
authoritative internal state
      ↓
Export / print / publication
      ↓
external representation
```

It translates the Phase 002 Export, Provenance, paper-continuity, disclosure, Versioning, Scorecard, Rubric, Finalization, and Official Outcome semantics—and the reconciliation/finalization experience from 003-F—into an Organizer-facing workflow without selecting PDF libraries, printers, OCR technology, object storage, content-delivery infrastructure, public-site framework, or AWS services.

The governing objective is:

> Physical judging and external communication should remain trustworthy extensions of the same Competition model: paper evidence must enter the system without changing authorship or evaluation meaning, and generated/published artifacts must disclose only their intended audience view while remaining traceable to the exact source state they represented.

The central model is:

```text
PAPER IN

physical Scorecard
      ↓
source identity
      ↓
capture Draft
      ↓
verification against source
      ↓
authoritative Scorecard Version
      ↓
reconciliation


REPRESENTATION OUT

authoritative source state
      ↓
audience + disclosure policy
      ↓
Export generation
      ↓
preview / validation
      ↓
print / distribute / publish
      ↓
traceable external artifact
```

---

# Part I — Paper capture experience

## 2. Paper is an evaluation capture channel, not a second evaluation model

The Organizer experience must reinforce:

```text
Electronic Judge evaluation
        and
Paper Judge evaluation
```

share the same:

- Team / Encounter context;
- Judge evaluation author;
- Rubric Version;
- Criterion scores;
- Note semantics;
- Scorecard calculation;
- eventual aggregation weight;
- Coverage semantics.

Paper changes the capture path and Provenance, not the meaning or weight of the judgment.

The UI should therefore avoid separate concepts such as:

```text
Paper Score
Electronic Score
```

when it really means two capture channels for the same logical Scorecard.

---

## 3. Paper source identity

Every physical evaluation accepted for capture must have a unique **paper source reference**.

Conceptually:

```text
Paper source
    source reference
    Competition
    Judge Participation, when resolved
    Encounter / Team context, when resolved
    Rubric Version
    collection status
    capture status
```

The source reference may have been printed onto a prepared form or assigned when an emergency/generic form is collected.

The exact barcode, human-readable identifier, label, storage method, or numbering format remains implementation policy.

The important requirement is:

> Two physical forms must not become indistinguishable merely because they contain similar scores.

---

## 4. Prepared versus emergency paper forms

The experience should support both.

### Prepared form

May already identify some or all of:

```text
Competition
Rubric Version
Panel / Encounter context
Team Alias
Judge context
paper source reference
```

according to operational policy.

### Generic / emergency form

May begin with only:

```text
Competition
Rubric Version
blank Judge / Team / Encounter context
```

and require the Judge or Organizer to record enough context during use/intake.

Generic fallback must not be rejected merely because it was not pre-generated, but unresolved identity/context prevents the captured evaluation from becoming authoritative until safely resolved.

---

## 5. Printable judging forms preserve blinded identity

Paper forms used by Judges follow the same disclosure rules as the electronic Judge experience.

Default Judge-facing content may include:

```text
Competition-safe event information
Team Alias
Division
Rubric / Criterion content
score choices
Note areas
Rubric Version / source traceability
```

It should not expose by default:

```text
institution identity
Organizer-only Team metadata
student personal information
Team Name during blinded judging
peer evaluations
Aggregate / Rank
```

A paper fallback cannot weaken anonymity simply because electronic disclosure controls are unavailable.

---

## 6. Team Name on physical judging material

The optional `teamName` attribute follows the same baseline as electronic judging:

```text
Judge-facing paper during blinded judging:
Hidden by default
```

If a future Competition deliberately permits Team Name disclosure during evaluation, the print profile may include it.

Alias remains the canonical competition identity and cannot be replaced structurally by a decorative Team Name.

---

## 7. Paper form must identify the evaluation basis

A Judge should be able to determine which Rubric they are using from the physical artifact.

The form must therefore retain enough source/version identity to distinguish:

```text
Rubric v3
```

from a later:

```text
Rubric v4
```

without depending solely on visual similarity.

The exact placement and format of version information remain a visual-design concern.

If Rubric v4 becomes authoritative after v3 forms were printed, the previously printed v3 forms become stale for new judging under v4 rather than silently transforming into v4 forms.

---

## 8. Paper intake workspace

The Organizer needs an intake-oriented view that answers:

> Which physical evaluations have we received, and what must happen before they are authoritative digital evidence?

Useful states include:

```text
Expected / not returned
Source collected
Context unresolved
Capture not started
Capture Draft
Verification pending
Verified / authoritative
Capture correction required
Duplicate-risk / convergence required
Source unavailable / needs investigation
```

These are workflow projections from paper source, Scorecard, and Provenance state rather than a new `PaperScorecard` Concept.

---

## 9. Paper source collection versus capture

The UX must distinguish:

```text
We possess the paper
```

from:

```text
The paper has been transcribed
```

and from:

```text
The transcription has been verified and is authoritative
```

For example:

```text
Paper PF-184
Team 014
Judge J-041

Source collected        ✓
Capture complete        ✓
Verified against paper  pending

Official eligibility:
Not yet eligible
```

This prevents data-entry completion from being mistaken for evidence authority.

---

## 10. Capture Draft

Entering a physical evaluation first creates a capture Draft or equivalent non-authoritative working state.

The Organizer enters the paper-authored content:

```text
Criterion scores
Criterion Notes
Overall Note
```

using the exact bound Rubric Version.

The capture experience should reproduce the paper's valid scoring semantics rather than presenting a generic data-entry grid that permits impossible values.

The Organizer is transcribing, not judging.

---

## 11. Evaluation author versus capture actor

The capture experience must keep these identities explicit:

```text
Evaluation author
Judge J-041

Capture actor
Organizer O-006

Capture channel
Paper

Paper source
PF-184
```

The Organizer should never appear as the Scorecard author merely because they typed the values.

This distinction must survive into Provenance and later audit views.

---

## 12. Paper source context confirmation

Before verification, the Organizer should confirm enough context to establish:

```text
correct Competition
correct Judge Participation
correct Encounter / Team
correct Rubric Version
correct paper source
```

If the form is pre-associated, the captured values should be checked against those associations.

If the form is generic, the Organizer resolves the context deliberately.

The system must not infer a Team or Judge from score patterns, Team Name, institution, or another weak clue.

---

## 13. Capture validation

The capture Draft uses the same domain validation as electronic Scorecards.

Examples:

```text
all required Criterion values present
values belong to allowed score domains
required Notes present
Scorecard result deterministic
Rubric Version exact
```

An invalid transcription cannot become authoritative merely because the physical paper exists.

If the paper itself contains an invalid or incomplete Judge response, the UX distinguishes:

```text
transcription mistake
```

from:

```text
source paper itself is incomplete / ambiguous
```

Those require different authority paths.

---

## 14. Verification against physical source

Before paper-origin evidence becomes officially eligible, the captured content must be checked against the physical source according to Competition policy.

Baseline flow:

```text
Capture Draft
      ↓
review side-by-side / source-to-capture
      ↓
confirm scores and Notes match source
      ↓
Verify capture
      ↓
authoritative paper-origin Scorecard Version
```

The baseline permits one authorized Organizer to perform verification.

A Competition may require dual-person verification, but two-person control is not a universal product requirement.

---

## 15. Verification should compare meaningfully

The verification experience should make it easy to compare:

```text
paper Criterion
↔ captured Criterion

paper Note
↔ captured Note
```

without requiring the verifier to reconstruct the entire Rubric manually.

Whether the UI shows a scan/image alongside fields, uses physical paper beside the screen, or another method remains an implementation choice.

003-G does **not** require OCR or scanning every paper form.

---

## 16. Source image / scan is optional, not the authority model

A Competition may choose to retain a digital image of paper evidence for operational convenience or auditability.

But:

```text
image exists
    ≠
transcription verified
```

and:

```text
no scan retained
    ≠
paper evaluation invalid
```

The authority model remains the physical-source/capture/provenance relationship unless later retention policy says otherwise.

Storage, image quality, retention duration, and privacy controls remain downstream policy/architecture decisions.

---

## 17. Ambiguous paper content

If the physical paper itself is ambiguous, the Organizer must not invent the Judge's intent.

Examples:

```text
two scores visibly selected
illegible corrected value
Note appears to contradict overwritten score
required Criterion left genuinely blank
```

The experience should support outcomes such as:

```text
Needs Judge clarification
Source unresolved
Request Judge amendment / clarification
Exclude or otherwise reconcile under declared policy
```

It should not offer:

```text
Choose what the Judge probably meant
```

as an ordinary Organizer action.

---

## 18. Capture correction before verification

Because a capture Draft is not authoritative, ordinary transcription mistakes can be fixed before verification without creating a chain of authoritative Scorecard Versions for every keystroke.

For example:

```text
paper = 4
capture Draft = 3
```

may simply be corrected to `4` before verification.

The source paper has not changed and no authoritative digital state has yet been established.

---

## 19. Transcription correction after verification

After a paper-origin Scorecard has become authoritative, a discovered mismatch requires an explicit capture/transcription correction.

Example:

```text
Paper PF-184
Criterion = 4

Verified digital v1
Criterion = 3
```

Correction produces:

```text
Scorecard v2
Criterion = 4
```

with Provenance identifying:

```text
Evaluation author: Judge
Correction actor: Organizer
Correction type: transcription correction
Source: PF-184
```

This is not labeled a Judge amendment.

The old verified Version remains historical.

---

## 20. Paper Judge amendment remains different

If the paper was transcribed correctly but the Judge later changes their substantive judgment, that is a Judge amendment.

Conceptually:

```text
Paper source accurately captured
      ↓
Judge later changes judgment
      ↓
Judge amendment
      ↓
new authoritative Scorecard Version
```

The Organizer cannot disguise a substantive change as a transcription correction merely because the original capture channel was paper.

---

## 21. Duplicate electronic/paper convergence

The paper intake workspace must detect or surface when the same:

```text
Judge Participation × Encounter
```

already has electronic work.

Example:

```text
Judge J-041 × Encounter E-022

Electronic:
Draft exists

Paper:
PF-184 returned
```

The UX should present this as:

```text
Convergence required — one logical Scorecard
```

not:

```text
Two evaluations received
```

The eventual authoritative path may preserve the abandoned electronic Draft historically where appropriate, but official weight remains one.

---

## 22. Paper intake completion

The Organizer should be able to distinguish:

```text
all expected paper sources accounted for
```

from:

```text
all paper-origin Scorecards authoritative
```

and from:

```text
all paper-origin evidence reconciled for Finalization
```

These may become true at different times.

003-F consumes the final authoritative/eligibility state; 003-G provides the capture workflow needed to reach it.

---

# Part II — Export and print experience

## 23. Export represents source state; it does not replace it

The central Export principle is:

> An Export is a stable representation of identified source state for an intended audience and purpose.

Conceptually:

```text
Authoritative source
      +
source Version / revision
      +
audience
      +
disclosure policy
      +
representation purpose
      ↓
Export
```

A PDF, printed sheet, downloadable file, ceremony list, or publication payload does not become authoritative simply because it exists outside the application.

---

## 24. Export metadata / traceability

The Organizer should be able to inspect enough information about an Export to answer:

```text
What is this?
What source state did it represent?
For whom was it intended?
When was it generated?
Who generated/released it?
Is it still current for its intended use?
Has it been superseded or withdrawn?
```

Conceptually an Export representation retains references such as:

```text
purpose / type
audience / disclosure profile
source subject
source Version or Official Outcome Revision
generation time
generating actor
freshness status
release/publication status where applicable
```

The exact file manifest/storage implementation is deferred.

---

## 25. Artifact status is not source status

An external artifact may be:

```text
Current
Stale
Superseded
Withdrawn from current distribution
```

without changing the authoritative source itself.

For example:

```text
Rubric v3 form
Generated Monday

Rubric v4 later becomes authoritative
```

means:

```text
v3 form
Stale for new judging
```

not:

```text
Rubric v3 no longer existed
```

Likewise a previous Official Outcome publication remains historically attributable to Outcome Revision 1 even after Revision 2 becomes current.

---

## 26. Stale does not mean historically false

An artifact can be stale for current operational use while remaining an accurate representation of what was authoritative at generation/distribution time.

This distinction should be visible.

For example:

```text
Judge Rubric packet
Rubric v3
Generated 8:10 AM

Status:
Superseded for new judging — Rubric v4 is current

Historical source:
Rubric v3 remains available
```

The experience should avoid language implying that the old artifact has magically changed contents or lost all historical meaning.

---

## 27. Export purpose profiles

Different external representations exist for different purposes.

Initial purpose categories may include conceptually:

```text
Judge evaluation materials
Panel / event operational materials
Organizer-sensitive operational exports
Reconciliation / audit exports
Ceremony / Award materials
Public result publication
Historical official-outcome representation
```

These categories are UX/policy profiles, not new domain Concepts.

The exact set can grow without changing Export's purpose.

---

## 28. Audience is part of Export intent

The Organizer's internal Access does not determine what the Export is allowed to contain.

The Export workflow should require or infer an explicit audience/disclosure profile such as:

```text
Judge-safe
Organizer-sensitive
Ceremony-safe
Public
```

The content is then derived through that disclosure posture.

The principle is:

```text
Organizer can see it
      ≠
Organizer may include it in every Export
```

---

## 29. Judge-safe materials

Judge-facing materials should ordinarily include only what Judges require to operate:

```text
Competition-safe event details
Panel / room context when appropriate
Team Alias + Division
Rubric / scoring guidance
Judge instructions
QR / navigation aids where useful
```

They should exclude:

```text
institution mapping
Organizer-only Team metadata
Team Name by default during blinded judging
peer Scorecards / Notes
Aggregate / Ranking
```

The same disclosure rules apply to visible content, filename/label choices, document metadata, and machine-readable payloads where practical.

---

## 30. Organizer-sensitive materials

Some operational or reconciliation artifacts may legitimately include:

```text
Team administrative identity
Alias mapping
Judge identities
Scorecard states
Coverage / exception state
Provenance references
```

Such artifacts should be visibly classified as Organizer-sensitive and not casually mixed into Judge/public material workflows.

A user should not need to inspect every column to discover that an export contains identity-sensitive information.

---

## 31. QR / machine-readable content

QRs, barcodes, and similar mechanisms may appear on:

```text
Competition entry materials
Panel materials
Team / Encounter materials
paper source forms
```

The experience must preserve the existing rule:

> Encoded possession does not grant authority.

Machine-readable content should prefer opaque/safe identifiers and avoid embedding institution identity, private Notes, raw credentials, or other sensitive data merely for convenience.

Scanning resolves requested context, after which Identity/Participation/Access is still enforced.

---

## 32. Print preview is a disclosure preview

Before producing a consequential external artifact, the Organizer should be able to inspect what the intended audience will actually receive.

The preview should answer:

```text
Which source Version/revision?
Which audience profile?
Which Teams/Divisions/Panel scope?
Which disclosed fields?
Is this artifact current?
Does it contain sensitive information?
```

This extends the Judge-safe preview from 003-D into a general external-representation review.

---

## 33. Representation validation

Before release/printing, the system should validate conditions appropriate to artifact purpose.

Examples:

```text
source Version still current for intended operation
required Alias present
Rubric Version identifiable
public result source is an Official Outcome Revision
no prohibited disclosure fields selected
Award recipient resolved
```

A representation can fail validation without mutating the source domain object.

---

## 34. Generation failure is non-destructive

If an Export fails to generate or print:

```text
source state remains unchanged
```

The UI should report generation failure and permit retry.

A failed PDF renderer or printer cannot alter a Rubric, Scorecard, Award, Rank, or Official Outcome.

---

## 35. Regeneration after source change

When source state changes, the Organizer should be able to see the affected artifacts.

Example:

```text
Alias Team 014 → Team 027
      ↓
Affected materials
• Panel 03 packet
• Team evaluation forms
• room assignment sheet
```

or:

```text
Official Outcome Revision 2 established
      ↓
Affected publications
• ceremony results PDF based on Revision 1
• public results page based on Revision 1
```

The system should recommend or require regeneration according to purpose/policy.

It must not silently edit already distributed physical artifacts.

---

## 36. Distribution awareness

Where operationally useful, the Export experience should distinguish:

```text
Generated
Printed / prepared
Released / distributed
Superseded / withdrawn
```

The exact tracking granularity can differ by artifact type.

For example, tracking that a single emergency blank Rubric was physically handed to one Judge may be excessive, while tracking which Official Outcome Revision was publicly released is high value.

003-G establishes the semantic need without requiring inventory-level tracking for every sheet of paper.

---

## 37. Physical artifact recall is imperfect

If a printed artifact becomes stale after distribution, the application can identify the issue and support replacement, but it cannot guarantee physical recall.

The Organizer experience should communicate realistically:

```text
This packet is stale.
Replace distributed copies where possible.
```

rather than implying that generating a new PDF invalidates every paper copy already in the room.

This matters especially for emergency Rubric or Alias corrections.

---

# Part III — Ceremony and publication experience

## 38. Finalized does not mean published

003-G carries forward the Phase 002/003-F rule:

```text
Competition Finalized
      ≠
Results Public
```

After Finalization, an Organizer may:

```text
prepare ceremony materials
review public disclosure
generate certificates / Award lists
stage publication
```

before public release.

This supports controlled event timing without reopening scoring authority.

---

## 39. Official Outcome Revision is the publication source

Public or ceremony results must be generated from an identified Official Outcome Revision.

Conceptually:

```text
Official Outcome Revision 1
      ↓
Ceremony Export A
Public Results Publication B
Award List C
```

The Organizer should never publish from an unmarked provisional Ranking simply because the values happen to look final.

If no Official Outcome Revision exists, official-results publication is blocked.

---

## 40. Ceremony-safe versus public disclosure

Ceremony and public audiences may have different disclosure profiles.

For example, ceremony material may intentionally reveal:

```text
Team Alias
Team Name
institution
Award
Division
```

while a public web result may use a different subset.

These choices must be explicit.

The existence of Team Name or institutional identity in the Organizer record does not automatically authorize its publication.

---

## 41. Team Name in public / ceremony representations

The optional `teamName` attribute becomes particularly useful after blinded judging.

A ceremony-safe/public profile may deliberately render:

```text
Bayes Brigade
Team 014
Undergraduate Champion
```

or another approved combination.

But publication of Team Name remains a disclosure decision rather than a consequence of storing it.

A Competition may choose to publish Alias only, Team Name only alongside Alias, institution, or another approved identity profile.

---

## 42. Judge private evidence is not a publication default

Public or ceremony result workflows must not casually expose:

```text
Judge private Notes
Judge-to-score attribution
individual Scorecard details
private Judge identity metadata
internal reconciliation reasons
break-glass/access history
```

Those may remain available to authorized Organizer/audit workflows but require a separate explicit disclosure basis to leave that boundary.

Public results should not become an accidental data dump of everything used to derive the outcome.

---

## 43. Publication preview

Before release, the Organizer should see a publication-specific preview such as:

```text
Source
Official Outcome Revision 1

Audience
Public

Includes
✓ Division
✓ Rank
✓ Award
✓ Team Alias
✓ Team Name
✕ Institution
✕ Aggregate score
✕ Judge information
```

The exact selectable fields may be policy-driven, but the disclosure posture must be understandable before publication.

---

## 44. Publishing is an explicit action

Generating an artifact does not automatically publish it.

Conceptually:

```text
Generate / stage
      ↓
preview
      ↓
Publish / release
```

This distinction allows Organizers to prepare ceremony or public materials early while retaining control over disclosure timing.

The application should not equate:

```text
file generated successfully
```

with:

```text
public audience can access it
```

---

## 45. Publication status

For public-facing representations it is useful to distinguish conceptually:

```text
Draft / staged
Published / current
Affected / stale
Superseded
Withdrawn
```

These describe publication state, not Competition lifecycle.

A Competition can remain Finalized while a publication is staged, current, affected, or withdrawn.

---

## 46. Publication links do not expand authorization

A public publication is deliberately public according to its disclosure profile.

A non-public Export link or Organizer-sensitive artifact must still enforce its intended Access rather than becoming public by URL possession.

Likewise, a QR printed on a public result sheet cannot be assumed safe merely because the sheet itself is public; the destination must enforce the appropriate disclosure context.

---

## 47. Corrected Official Outcome and publication impact

Suppose:

```text
Official Outcome Revision 1
Champion: Team 014
```

was published.

A later verified correction produces:

```text
Official Outcome Revision 2
Champion: Team 027
```

The existing Revision-1 publication becomes:

```text
Affected / stale relative to current official outcome
```

The system must not silently rewrite history or automatically claim the public already received Revision 2.

---

## 48. Corrected-result publication workflow

The Organizer experience should be:

```text
Official Outcome Revision 2 confirmed
      ↓
identify affected publications
      ↓
review corrected disclosure
      ↓
generate successor representation
      ↓
explicitly publish / release correction
      ↓
Revision-2 publication becomes current
```

The prior publication remains historically attributable to Revision 1.

If externally cached/downloaded copies exist, the application cannot erase them; it can only present the corrected current representation and, where appropriate, correction notice/history.

---

## 49. No automatic republication after outcome correction

A post-finalization evidence correction can change the latest official outcome, but it does not automatically republish public results.

Why:

- publication timing may matter;
- wording/disclosure may need review;
- ceremony materials may already have been distributed;
- external correction communication may need deliberate handling.

Therefore:

```text
Official Outcome Revision changes
      ↓
publication becomes affected
```

rather than:

```text
public content silently changes
```

unless a future Competition explicitly adopts an auto-publication policy with equivalent disclosure safeguards.

---

## 50. Publication withdrawal

An Organizer may need to withdraw a publication from current platform distribution because it is wrong, premature, or no longer intended for disclosure.

Withdrawal means:

```text
stop presenting this artifact as current/available through managed publication channels
```

It does not mean:

```text
pretend it was never published
```

Historical publication Provenance should remain available to authorized users.

The system also cannot guarantee deletion of copies already downloaded, printed, cached, or shared externally.

---

## 51. Historical official representations

For audit/history, an authorized Organizer should be able to inspect:

```text
Official Outcome Revision 1
    published artifact(s)

Official Outcome Revision 2
    corrected artifact(s)
```

with clear current/historical labeling.

Public experience may choose to expose only the current corrected outcome or may include a correction notice/history according to policy.

The internal historical record remains richer than public disclosure by default.

---

# Part IV — Cross-workflow externalization principles

## 52. Disclosure review applies beyond visible body content

Sensitive information can leak through:

```text
filename
document title
header/footer
embedded metadata
QR payload
spreadsheet sheet names
hidden columns
print annotations
```

The representation pipeline should apply audience/disclosure policy to these surfaces where practical.

For example, a Judge-safe file should not be named:

```text
St-Catherine-Team-014-Rubric.pdf
```

if institution identity is intentionally hidden from Judges.

---

## 53. Source correction propagates to representation status

A source change should trigger representation impact analysis.

Examples:

```text
Rubric Version changed
      ↓
Judge forms stale
```

```text
Alias corrected
      ↓
Team/Panel judging material affected
```

```text
Award corrected
      ↓
ceremony material affected
```

```text
Official Outcome Revision superseded
      ↓
public-result publication affected
```

The source Concept need not know every artifact implementation detail; the application synchronizes authoritative changes with Export freshness.

---

## 54. Export cannot hide source uncertainty

The application should not generate a representation that implies more authority than the source possesses.

Examples:

```text
provisional Ranking
```

must not be exported as:

```text
Official Final Results
```

and:

```text
paper capture verification pending
```

must not be represented as a verified authoritative Scorecard in an audit export.

The representation's language/status must follow source semantics.

---

## 55. Export generation should be reproducible enough to explain

For consequential artifacts, the Organizer should be able to identify the inputs needed to explain what was generated.

At minimum conceptually:

```text
source subject / revision
export purpose
audience/disclosure profile
relevant configuration
creation time
actor
```

Perfect byte-for-byte rendering reproducibility is an implementation decision, but semantic reproducibility is required:

> We must be able to explain what authoritative information this artifact represented and why it contained the fields it contained.

---

## 56. Print accessibility and operational usability are requirements

Printed materials remain a first-class accessibility/continuity path.

They should be designed so they do not depend on:

```text
color alone
very small text
fine visual distinctions
unlabeled numeric bubbles
camera access
```

They should preserve clear Team/Alias context, Rubric guidance, score entry affordances, and sufficient space for required Notes.

Detailed cross-channel accessibility rules are consolidated in 003-H.

---

## 57. Paper and digital state can coexist during recovery

The Organizer may encounter:

```text
physical paper source
+
partial digital capture
+
prior electronic Draft
```

The UX must represent these as related artifacts around one evaluation obligation, not force one to disappear before reconciliation.

The goal is convergence:

```text
multiple operational traces
      ↓
one authoritative logical Scorecard
      ↓
full Provenance
```

---

## 58. Physical-source disposition does not rewrite Provenance

A later retention policy may permit physical paper to be archived, transferred, or destroyed after the required retention period.

If that occurs, the system should preserve the fact that the evaluation originated from paper and the source reference that supported capture.

Physical disposition must not rewrite history so the Scorecard appears as though it originated electronically.

Exact retention schedules are deferred to governance/implementation policy.

---

## 59. Organizer task separation

The externalization experience should keep several high-consequence operations visibly distinct:

```text
Capture paper
Verify capture
Correct transcription
Generate artifact
Release / print artifact
Publish results
Withdraw publication
Republish corrected outcome
```

A single generic `Save/Publish` control would obscure meaningful authority boundaries.

---

## 60. Representative Organizer materials workspace

Conceptually:

```text
MATERIALS & PUBLICATION

Paper evaluations
12 expected
12 collected
10 verified
2 verification pending

Judge materials
Rubric packet — Rubric v3 — Current
Panel 04 packet — Current
Panel 06 packet — Stale: Alias correction

Official outcome
Revision 1 — Current

Ceremony materials
Award list — Revision 1 — Generated / not released

Public results
Not published

Needs attention
HIGH   2 paper captures need verification
WARN   Panel 06 packet is stale
```

After publication:

```text
Public results
Revision 1 — Published / Current
```

After corrected Outcome Revision 2:

```text
Public results
Revision 1 — Published / Affected

Current official outcome
Revision 2

Action
Prepare corrected publication
```

---

## 61. 003-G UX invariants

1. Paper and electronic evaluation use the same Scorecard/Rubric semantics.
2. Every accepted physical evaluation has a unique paper source reference.
3. Paper source possession, transcription completion, and verification are distinct states.
4. Generic emergency forms remain usable but unresolved context blocks authority.
5. Judge-facing paper obeys the same anonymity/disclosure boundary as electronic judging.
6. Team Name remains hidden by default on blinded Judge materials.
7. Paper forms retain the exact Rubric Version used.
8. Organizer capture preserves Judge evaluation authorship.
9. Capture actor and evaluation author remain separately visible.
10. Capture Draft edits are non-authoritative.
11. Paper-origin evidence becomes eligible only after required verification.
12. OCR/scanning is not required for paper validity.
13. Ambiguous physical Judge intent is not resolved by Organizer guesswork.
14. Post-verification transcription corrections create explicit successor history.
15. Transcription correction is distinct from Judge amendment.
16. Electronic + paper artifacts for one Judge × Encounter converge onto one logical Scorecard.
17. Export represents identified source state rather than replacing source truth.
18. Export purpose and audience/disclosure posture are explicit.
19. Organizer internal visibility does not imply export disclosure permission.
20. Artifact status and source status remain distinct.
21. Stale artifacts remain historically attributable to their original source state.
22. Regeneration creates a new representation rather than silently modifying distributed artifacts.
23. QR/barcode possession never grants authority.
24. Representation preview exposes source, audience, disclosure, and freshness before release.
25. Export/generation failure never mutates authoritative source state.
26. Finalization and publication remain separate.
27. Official result publication requires an Official Outcome Revision.
28. Ceremony/public disclosure may deliberately differ.
29. Team Name can be used after judging only through explicit disclosure policy.
30. Judge Notes and Judge-linked score detail are not public defaults.
31. Artifact generation and publication/release are distinct actions.
32. Post-finalization correction marks dependent publications affected rather than silently rewriting them.
33. Corrected official outcomes require deliberate successor publication/release.
34. Publication withdrawal does not erase historical publication Provenance or external copies.
35. Sensitive disclosure controls apply to metadata/payloads as well as visible body content where practical.
36. External representations cannot imply stronger authority than their source possesses.
37. Consequential Export semantics remain explainable from source revision + purpose + disclosure + actor + time.
38. Print remains a first-class accessible/degraded-operation path.
39. Multiple recovery artifacts may coexist until they converge onto one authoritative evaluation.
40. Physical-source retention/disposition never changes original capture Provenance.

---

## 62. 003-G exit position

The full physical/external boundary is now:

```text
                INTERNAL AUTHORITATIVE MODEL
                           │
             ┌─────────────┴─────────────┐
             │                           │
             ▼                           ▼
      PAPER CAPTURE                    EXPORT
             │                           │
physical source                 source Version/revision
             │                           +
source identity                 audience/disclosure
             │                           │
capture Draft                           ▼
             │                       artifact
verification                          preview
             │                           │
authoritative                          release
Scorecard Version                  / print / publish
             │                           │
             └─────────────┬─────────────┘
                           ▼
                    VERSION / PROVENANCE
```

The central principle is:

> **Physical and external representations must preserve the authority, identity, version, and disclosure semantics of the internal state they carry; changing media must never change meaning.**

003-G now hands the experience architecture to **003-H — Accessibility, Mobile, Responsive & Degraded-Mode Interaction Architecture**.

003-H can apply one coherent accessibility and resilience standard across:

- Judge onboarding;
- phone-first scoring;
- Organizer preparation;
- live operations;
- reconciliation/finalization;
- paper capture;
- print/export/publication;
- device/network interruption and fallback.

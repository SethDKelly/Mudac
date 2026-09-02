# 002-D — Rubric, Criterion, Scorecard & Notes Specifications

Status: **Complete**

## 1. Purpose

002-D specifies the evaluation instrument and the individual judgment produced from it.

Accepted concepts specified here:

1. Rubric
2. Scorecard

Subordinate state specified here:

- Criterion
- Criterion Score / Response
- Criterion Note
- Overall Scorecard Note

The central distinction is:

```text
Rubric
    defines how judgment may be expressed

Scorecard
    records one Judge's actual judgment
```

002-D also separates **intra-Scorecard calculation** from later Competition aggregation. A Rubric may deterministically derive one Judge's Scorecard value from that Judge's Criterion responses. 002-F will specify how authoritative Scorecards are combined across Judges and Encounters, how coverage affects eligibility, and how ranking is produced.

The specification remains implementation-neutral. UI controls, database structures, API representations, offline-storage mechanisms, text-editor technology, PDF layout, and AWS services remain downstream concerns.

---

## 2. Cross-concept model

```text
RUBRIC
   │
   ├── Criterion
   ├── Criterion
   └── Criterion
          │
          │ authoritative Rubric version
          ▼

JUDGING ENCOUNTER
   │
   └── effective Judge evaluation obligation
          │
          ▼
      SCORECARD
          │
          ├── Criterion response
          │      ├── score
          │      └── note
          │
          ├── Criterion response
          │      ├── score
          │      └── note
          │
          └── overall note
```

The Scorecard references the exact authoritative Rubric version under which the judgment was formed.

The Rubric does not know which Team or Judge is being evaluated.

The Scorecard does not decide which Judge should exist in an Encounter or how multiple Scorecards are aggregated.

---

# 3. Rubric specification

## Purpose

> Define a repeatable evaluation instrument that states what Judges should evaluate, what responses are valid, and how those responses form one individual evaluation.

A Rubric exists so Judges can make comparable judgments under an explicit evaluation model rather than interpreting an unconstrained score form independently.

## State

Conceptual state:

```text
Rubric
    stable rubric identity
    Competition scope or applicability context
    name
    description / instructions
    scoring model
    ordered criteria
    criterion-note policy
    overall-note policy
    working-definition state
```

The exact assignment of a Rubric to a Competition, Division, Round, or Encounter remains synchronization/policy rather than Rubric-owned behavior. Every Scorecard ultimately receives one exact authoritative Rubric version as its basis.

## Actions

Conceptual actions:

```text
createDraft
rename
updateInstructions
configureScoringModel
addCriterion
editCriterion
reorderCriterion
removeCriterion
configureCriterionNotePolicy
configureOverallNotePolicy
validate
prepareForUse
```

`prepareForUse` means the working Rubric is internally valid and may be committed as an authoritative version through Versioning. The detailed version-commit contract is specified in 002-E.

## Queries

Useful queries include:

```text
criteriaInOrder
scoringModel
validationIssues
isValidForUse
criterionByIdentity
scorecardValueFor(responses)
```

`scorecardValueFor` is deterministic for a complete valid response set and does not depend on other Judges or Teams.

## Operational principle

An Organizer creates a Rubric, defines its scoring model and Criteria, adds scoring guidance and note requirements, validates the Rubric, and establishes an authoritative version. A Judge later receives that exact version in a Judging Encounter and records one Scorecard under its rules.

---

# 4. Criterion specification

Criterion remains subordinate Rubric state rather than an independent concept.

## Purpose within Rubric

> Define one scored dimension of evaluation and the valid way a Judge expresses judgment for that dimension.

A Criterion should be understandable in context without forcing Judges to infer what a number means.

## State

Conceptually:

```text
Criterion
    stable identity within Rubric lineage
    display order
    title
    description
    scoring guidance
    valid score domain
    scoring contribution configuration
    note policy
```

`stable identity within Rubric lineage` allows later versions to distinguish an edited Criterion from a newly introduced Criterion without requiring a user-visible identifier.

## Criterion guidance

A Criterion should support enough guidance for the Judge to understand the intended distinction between scores.

For example:

```text
Statistical Methodology

Evaluate the appropriateness, rigor, and validation
of the team's statistical methods.

1 — major methodological weaknesses
2 — substantial concerns
3 — competent application
4 — strong application
5 — exceptional rigor
```

The exact presentation is a later UX concern.

## Valid score domain

A Judge may select only values explicitly allowed by the Criterion/Rubric scoring model.

A score domain is finite and ordered for the initial specification. Examples include:

```text
0, 1, 2, 3, 4, 5
```

or:

```text
1, 2, 3, 4, 5
```

or a configured point range expressed as discrete allowed values.

Arbitrary unconstrained numeric entry is not part of the initial model.

This supports predictable validation and mobile-friendly interaction while allowing competitions to choose their scale.

---

# 5. Missing, zero, and not-applicable semantics

These states must never be conflated.

```text
Missing
    no judgment recorded

0
    deliberate score of zero, if zero is allowed

N/A
    explicitly non-applicable response, only if the Rubric defines it
```

The initial specification does **not** provide implicit N/A behavior.

If N/A is introduced by later competition policy, the Rubric must explicitly define:

- which Criteria permit it;
- whether a Note is required;
- how it affects Scorecard completeness;
- how it affects the Scorecard value and denominator.

Until those semantics are defined, N/A must not appear as a generic option.

Similarly, optional numeric Criteria are not part of the initial baseline because they create denominator and comparability ambiguity. Scored Criteria are required for Scorecard finalization unless a later explicit policy extends the model.

---

# 6. Rubric scoring-model coherence

A Rubric must use one coherent scoring model.

The initial semantic model supports two families without allowing them to be casually mixed:

1. additive points;
2. weighted rating scale.

A Competition does not have to support both in its first implementation, but the concept specification permits either.

## Additive-points model

Each Criterion defines an allowed point domain.

Example:

```text
Methodology      0–30
Analysis         0–25
Communication    0–20
Innovation       0–15
Presentation     0–10
```

The Scorecard value is the deterministic sum of Criterion contributions.

The point allocation itself expresses relative importance; a second percentage weight must not be layered on top implicitly.

## Weighted-rating model

The Rubric defines a common ordered rating scale and a deterministic contribution mapping for that scale.

Each Criterion then defines a positive weight.

Conceptually:

```text
rating level
    ↓
configured contribution factor
    ×
Criterion weight
    ↓
Criterion contribution
```

The Scorecard value is the sum of weighted Criterion contributions.

The scale-to-contribution mapping must be explicit so the system does not silently assume whether a rating of `1` on a 1–5 scale means 0%, 20%, or some other contribution.

Weights must satisfy the Rubric's declared total-weight rule, normally 100% / 1.0.

## No accidental double weighting

A Rubric must not use both point maxima and independent percentage weights in a way that causes hidden double weighting.

The Rubric validation process must reject internally incoherent scoring configuration.

---

# 7. Rubric validation

A Rubric cannot become authoritative for judging unless it is valid.

At minimum, validation requires:

1. at least one scored Criterion;
2. unique Criterion identities within the Rubric;
3. deterministic Criterion ordering;
4. every Criterion has a non-empty valid score domain;
5. every allowed score has unambiguous scoring meaning;
6. every scored Criterion is finalization-required under the initial model;
7. note policies are internally valid;
8. the scoring model can derive one deterministic Scorecard value from a complete response set;
9. additive-points configuration has a coherent positive total range;
10. weighted-rating configuration has a valid rating-to-contribution mapping and valid total weight;
11. no Criterion is configured in a way that causes hidden or contradictory contribution behavior.

A working Draft may temporarily violate these conditions.

An authoritative version may not.

---

# 8. Criterion Notes

Each Criterion response may contain qualitative commentary associated specifically with that scored dimension.

Conceptually:

```text
Criterion Response
    score
    note
```

A Criterion Note:

- explains or supplements the Judge's judgment;
- belongs to the Scorecard;
- inherits the Scorecard's authorship and privacy boundary;
- does not independently modify the numeric score;
- is versioned with the Scorecard once finalized.

The baseline note policy is configurable as:

```text
Optional
Required
```

More complex conditional policies such as "required only for the lowest score" may be introduced later if event requirements justify them; they are not necessary for the initial contract.

---

# 9. Overall Scorecard Note

A Scorecard may also carry one overall qualitative Note about the Team's presentation or analysis.

This Note is distinct from Criterion Notes because it applies to the evaluation as a whole.

For example:

```text
"Strong analytical work and feature engineering;
presentation moved too quickly through limitations."
```

The overall-note policy is similarly:

```text
Optional
Required
```

for the initial specification.

An overall Note does not alter the numeric Scorecard value unless the Competition explicitly models the intended consideration as a scored Criterion instead.

---

# 10. Notes are evaluation evidence, not hidden scoring inputs

This is a canonical boundary.

```text
Score
    affects numeric evaluation

Note
    explains qualitative judgment
```

The system must not later derive secret numerical adjustments from words appearing in Notes unless a separate explicit Competition policy is intentionally introduced.

Likewise discretionary Awards may use Notes during Organizer deliberation, but that does not convert the Notes into hidden scoring components.

---

# 11. Notes are not automatically student feedback

Judge Notes are private judging records.

During ordinary live participation:

```text
Authoring Judge   → own Notes
Organizer         → authorized Notes
Peer Judges       → no access
Students          → no application access
```

At Event Completed, ordinary Judge retrieval access expires under 002-B.

If the product later introduces student feedback, that must be a deliberate disclosure/publication path rather than assuming all Judge Notes were written for student consumption.

Organizer commentary must also not be silently inserted into a Judge-authored Note. If later workflows require Organizer annotations, they should remain distinguishable from Judge-authored evaluation content.

---

# 12. Rubric authority and exact evaluation basis

A Scorecard always references one exact authoritative Rubric version.

Conceptually:

```text
Rubric identity
    │
    ├── version 1
    ├── version 2
    └── version 3
             │
             ▼
         Scorecard
```

The Scorecard's Rubric basis is fixed once the Scorecard is initialized.

A later Rubric version never silently rebinds an existing Scorecard.

This is true even if the later change appears editorial, because printed and electronic evaluation records must remain traceable to the exact instrument Judges saw.

002-E will specify version-history mechanics and 002-F will specify compatibility/aggregation consequences when multiple Rubric versions exist.

---

# 13. Scorecard specification

## Purpose

> Capture one Judge's independent evaluation of one Team within one Judging Encounter under one exact Rubric version.

A Scorecard is the smallest authoritative unit of judging evidence used by later aggregation.

## Identity

One logical Scorecard is uniquely associated with:

```text
Judge Participation
+
Judging Encounter
```

and has exactly one fixed Rubric-version basis.

Repeated creation/retry for the same obligation must converge on the same logical Scorecard rather than produce duplicate evaluation weight.

## State

Conceptually:

```text
Scorecard
    stable logical identity
    Judge Participation / evaluation author
    Judging Encounter
    Rubric version basis
    working response set
    current authoritative response version, if any
    amendment state, if any
```

Criterion responses contain:

```text
Criterion identity
score
Criterion Note
```

The Scorecard also contains its overall Note.

Capture actor/channel information is not Scorecard authorship state; it belongs to Provenance and is specified in 002-E.

---

# 14. Scorecard lifecycle

`Not Started` is an evaluation obligation with no Scorecard work yet; it is not a persisted Scorecard lifecycle state.

Once work begins, the logical lifecycle is:

```text
Draft
  ↓
Finalized
  │
  ├── begin amendment
  ▼
Amendment Draft
  │
  ├── abandon → Finalized
  │
  └── finalize amendment
          ↓
      Finalized
```

Versioning preserves the successive authoritative snapshots:

```text
Finalized v1
      ↓
Amendment Draft
      ↓
Finalized v2
```

While an Amendment Draft exists, v1 remains the authoritative evaluation for downstream use until v2 is finalized.

---

# 15. Scorecard actions

Conceptual actions include:

```text
start
setCriterionScore
clearCriterionScore
setCriterionNote
clearCriterionNote
setOverallNote
clearOverallNote
finalize
beginAmendment
abandonAmendment
finalizeAmendment
```

`saveDraft` need not be a user-significant domain action even if persistence technology internally performs saves. From the Judge's experience, Draft preservation should behave automatically.

## Queries

Useful queries include:

```text
criterionResponses
missingRequiredResponses
validationIssues
isCompleteForFinalization
currentCalculatedValue
currentAuthoritativeValue
hasAmendmentDraft
currentAuthoritativeVersion
```

---

# 16. Draft semantics

Draft exists so a Judge can form judgment incrementally without every interaction becoming official Competition evidence.

While Draft:

- scores may be entered, changed, or cleared;
- Notes may be entered, changed, or cleared;
- incomplete required Criteria are permitted;
- the calculated Scorecard value may be previewed if useful;
- the Scorecard does not yet contribute to official aggregation;
- ordinary Draft edits are not separate authoritative versions.

The experience should preserve Draft work automatically, but storage mechanics remain an architecture concern.

---

# 17. Finalization semantics

Finalization means:

> The evaluation author/capture process asserts that the Scorecard is complete under its Rubric and it becomes authoritative evidence eligible for downstream aggregation.

Finalization is not merely a Save button.

Before finalization, validation requires at least:

1. the Scorecard corresponds to a valid effective evaluation obligation;
2. the Judge Participation / evaluation author is fixed;
3. the Judging Encounter is the intended evaluation context;
4. the exact authoritative Rubric version is fixed;
5. every required Criterion has one valid score;
6. every required Criterion Note is present;
7. any required overall Note is present;
8. every score belongs to the Criterion's valid domain;
9. the Rubric can deterministically calculate the Scorecard value.

Authorization to perform finalization is evaluated through Access rather than hard-coded inside Scorecard.

---

# 18. One logical Scorecard per obligation

The canonical invariant remains:

```text
Judge Participation
        ×
Judging Encounter
        ↓
at most one logical Scorecard
```

A network retry, second browser request, or repeated user action must not create additional Scorecards.

An amendment changes the authoritative version of the same logical Scorecard.

It never creates another Judge vote.

---

# 19. Scorecard authorship versus capture actor

For ordinary electronic judging:

```text
Evaluation author = Judge
Capture actor      = Judge
Capture channel    = Electronic
```

For paper transcription:

```text
Evaluation author = Judge
Capture actor      = Organizer
Capture channel    = Paper
```

The Scorecard's evaluation author remains the Judge Participation whose judgment is represented.

Organizer data entry does not transfer authorship.

Likewise, an Organizer must not silently modify a Judge-authored electronic Scorecard merely because Organizer Access permits viewing or reconciliation.

002-E will specify the Provenance record that preserves author, actor, channel, reason, and change history.

---

# 20. Paper and electronic Scorecards share semantics

A paper-origin evaluation and an electronic evaluation create the same logical Scorecard semantics once captured.

They use the same:

- Rubric version;
- Criteria;
- valid score domains;
- Note semantics;
- completeness validation;
- deterministic Scorecard calculation;
- downstream aggregation eligibility.

Only capture provenance differs.

If paper transcription verification is required, it may gate finalization or downstream eligibility according to later Provenance/operational policy; it does not create a second type of Scorecard.

---

# 21. Scorecard calculated value

A Scorecard's numerical value is derived from:

```text
Criterion responses
        +
exact Rubric scoring model
        ↓
Scorecard calculated value
```

The Judge does not manually enter a second independent "overall numeric score" after already completing the Criteria.

If the Competition wants a holistic numeric judgment, it should be represented explicitly as another scored Criterion.

This ensures the numerical result is explainable and repeatable.

---

# 22. Calculation precision

The authoritative calculation should retain sufficient internal precision to reproduce the Rubric result deterministically.

Displayed rounding does not mutate the Scorecard.

For example:

```text
calculated value: 87.436666...
displayed value: 87.44
```

The exact numerical precision, comparison, and rounding rules used across Scorecards are specified in 002-F.

002-D only requires that Scorecard calculation not lose information through presentation rounding.

---

# 23. Amendment semantics

Once finalized, ordinary editing ends.

A legitimate correction begins an Amendment Draft.

Conceptually:

```text
Finalized v1
      │
      ├── authoritative downstream
      │
      ▼
Amendment Draft
      │
      ├── edit scores / Notes
      │
      ├── abandon → v1 remains authoritative
      │
      └── finalize
              ↓
         Finalized v2
```

When v2 becomes authoritative:

- v1 remains historical;
- downstream calculations may refresh;
- the amendment is attributable through Provenance.

The Scorecard does not itself decide whether the Judge is allowed to begin an amendment. That depends on Access, Competition lifecycle, and later correction policy.

---

# 24. Notes participate in amendments

Criterion Notes and the overall Note are part of the Scorecard version.

Changing a Note after finalization is an amendment just as changing a numeric score is.

The system must not maintain a mutable "current note" detached from the historical evaluation version, because doing so would make earlier finalized Scorecards impossible to reconstruct accurately.

---

# 25. Scorecard basis does not mutate during amendment

An amendment changes the Judge's responses under the same evaluation basis.

It does not silently change:

- Judge Participation;
- Judging Encounter;
- stable Team being evaluated;
- Rubric version.

If the original Scorecard was created against the wrong Encounter, wrong Judge, or wrong Rubric version, that is not an ordinary amendment. It is a structural/correction case requiring invalidation/replacement or another explicit correction workflow in 002-E/002-F.

This distinction prevents "editing" from becoming a mechanism for reassigning historical evidence.

---

# 26. Rubric changes after Scorecards exist

Once an authoritative Rubric version has been used by a Scorecard, that version remains historically addressable.

A later change creates another Rubric version.

Existing Scorecards continue to point to the earlier version.

The system must never behave as though:

```text
Rubric v1 edited in place
        ↓
old Scorecards now mean something different
```

Whether different Rubric versions are compatible for a single ranking population is explicitly deferred to 002-F.

---

# 27. Editorial versus scoring-semantic Rubric changes

002-D recognizes two broad forms of change:

## Editorial change

Changes wording/presentation without intending to change scoring meaning.

Example:

```text
"Clearly explains methodology"
→
"Clearly explains analytical methodology"
```

## Scoring-semantic change

Changes the mathematical or evaluative meaning.

Examples:

```text
10-point Criterion → 20-point Criterion
weight 10% → 25%
score anchor meaning changes materially
Criterion added/removed
```

Both still produce a new authoritative Rubric version once committed.

The semantic classification is important because 002-F may treat scoring-semantic changes as incompatible with existing Scorecards even where editorial changes are comparable.

---

# 28. Rubric changes during Active Competition

The Rubric concept itself does not decide Competition policy for mid-event changes.

However, the following invariant is mandatory:

> No change may silently alter the evaluation basis of an existing Scorecard.

A Competition may later choose policies such as:

- block any authoritative Rubric change after judging starts;
- allow editorial new versions with explicit impact review;
- allow scoring-semantic change only through exceptional reconciliation.

Those policy consequences are refined in 002-E and 002-F.

---

# 29. Encounter synchronization

002-C establishes effective evaluation obligations.

The synchronization into 002-D is:

```text
Encounter Open
    +
effective Judge participant
    +
applicable authoritative Rubric version
        ↓
Scorecard obligation / logical Scorecard
```

If a participant is legitimately excused before an authoritative Scorecard exists:

```text
Encounter participant adjustment
        ↓
Scorecard obligation removed/excused
```

If an authoritative Scorecard already exists, 002-C forbids silently deleting the evaluation through participant adjustment.

That case requires explicit correction/invalidation behavior later.

---

# 30. Encounter completion synchronization

Scorecard finalization contributes to the derived Encounter completion condition.

Conceptually:

```text
effective Encounter obligations
        +
authoritative Scorecards
        ↓
Encounter completion status
```

A Scorecard does not mark the Encounter Complete by itself.

The application derives whether all obligations are resolved.

---

# 31. Access synchronization

Access controls who may invoke Scorecard actions and who may read Scorecard content.

Examples:

```text
Active Judge Participation
    +
own Scorecard
    +
Competition Active
        ↓
may edit Draft / finalize according to policy
```

```text
Event Completed
        ↓
ordinary Judge Scorecard/Note read access expires
```

```text
Organizer-authorized correction
    +
Judge re-verification
        ↓
temporary access to amend specific Scorecard
```

Scorecard itself does not encode role-based authorization rules.

---

# 32. Provenance synchronization

Meaningful transitions synchronize with Provenance.

At minimum:

```text
Scorecard finalized
    ↓
record author / actor / channel / time / version
```

```text
Scorecard amendment finalized
    ↓
record changed fields / actor / time / reason as required
```

```text
paper capture corrected
    ↓
record capture correction without changing original evaluation authorship
```

Detailed Provenance contracts belong to 002-E.

---

# 33. Versioning synchronization

At authoritative transitions:

```text
Rubric prepared and committed for use
        ↓
Versioning commits Rubric snapshot
```

```text
Scorecard finalized
        ↓
Versioning commits Scorecard snapshot
```

```text
Scorecard amendment finalized
        ↓
Versioning commits new Scorecard snapshot
```

Working Draft edits do not each become separate authoritative versions.

002-E defines the generic version-history model.

---

# 34. Failure and exceptional behavior

## Incomplete Scorecard

A Draft may be incomplete.

Finalization is rejected with explicit validation issues identifying missing/invalid content.

No missing score is converted to zero.

## Score outside domain

Rejected as invalid input.

The application should never clamp an out-of-range value silently.

## Duplicate Scorecard start/finalize retry

Must converge on the existing logical Scorecard/current transition rather than create duplicate evaluation weight.

## Connection uncertainty during finalization

Retry must be safe. The eventual state must be unambiguous: either the authoritative finalization exists or it does not.

## Wrong Team / Encounter

The Scorecard must not be relabeled to another Team through ordinary edit/amendment after meaningful work. Structural correction is explicit.

## Wrong Rubric version

An existing Scorecard is not silently rebound. Structural correction/replacement is explicit.

## Judge becomes recused before finalization

If no authoritative Scorecard exists, the Encounter participant adjustment may excuse the obligation.

If an authoritative Scorecard exists, it remains historical and requires explicit invalidation/exclusion policy rather than deletion.

## Paper transcription discrepancy

Correct the capture with Provenance. Do not falsely attribute the correction as a change of Judge judgment when the source paper did not change.

---

# 35. Explicit non-responsibilities

## Rubric does not

- assign Judges to Panels;
- choose which Team is evaluated;
- aggregate across Judges;
- determine Coverage;
- calculate Rank;
- confer Awards;
- authorize access;
- implement version storage itself.

## Criterion does not

- become a reusable global concept in the initial model;
- independently own lifecycle or access;
- determine cross-Team ranking.

## Scorecard does not

- decide whether an Encounter should exist;
- decide which Judges are effective participants;
- expose peer Scorecards;
- calculate Panel/Team aggregate or Rank;
- decide whether an amendment is authorized;
- silently change evaluation author, Team/Encounter, or Rubric basis.

## Notes do not

- alter numeric scoring independently;
- become automatically public/student-facing feedback;
- become Organizer-authored text while still presented as Judge-authored Notes.

---

# 36. 002-D invariants

002-D establishes or strengthens the following invariants:

1. Rubric defines evaluation semantics; Scorecard records one application of them.
2. Criterion and Note remain subordinate state rather than independent concepts.
3. Every authoritative Scorecard references exactly one authoritative Rubric version.
4. Existing Scorecards never silently rebind to a later Rubric version.
5. Scored Criteria are finalization-required in the initial model.
6. Missing, zero, and N/A are distinct states.
7. N/A has no implicit semantics; it may exist only when explicitly defined by policy.
8. Arbitrary unconstrained numeric scores are not accepted.
9. Every Criterion score must belong to its valid domain.
10. A Rubric uses one coherent scoring model.
11. Additive points and independent percentage weights must not be accidentally double-applied.
12. Weighted scales must define an explicit rating-to-contribution mapping.
13. A complete valid response set deterministically produces one Scorecard calculated value.
14. The Judge does not enter a second unexplained overall numeric total.
15. Criterion Notes and overall Notes do not independently change numeric scoring.
16. Notes remain part of the Scorecard's private evaluation evidence.
17. Notes are versioned with finalized Scorecards.
18. One Judge Participation × one Encounter yields at most one logical Scorecard.
19. Scorecard retries/revisions never create additional evaluation weight.
20. Draft Scorecards do not contribute to official aggregation.
21. Finalized Scorecards are authoritative and eligible for later aggregation policy.
22. An Amendment Draft does not displace the prior authoritative version until finalized.
23. Abandoning an Amendment Draft leaves the previous authoritative version unchanged.
24. Scorecard amendment cannot silently change author, Encounter, Team basis, or Rubric version.
25. Paper and electronic Scorecards share evaluation semantics.
26. Capture actor may differ from evaluation author without transferring authorship.
27. Display rounding never mutates authoritative Scorecard calculation.
28. Rubric versions used by judging remain historically addressable.
29. Both editorial and scoring-semantic authoritative Rubric changes create new versions.
30. An authoritative Scorecard cannot be silently deleted because a participant is later adjusted or recused.
31. Organizer access does not imply authority to rewrite Judge-authored electronic judgment.
32. Scorecard/Note access remains governed by Access and Competition lifecycle.

---

# 37. Open questions carried into later Phase 002 groups

002-D intentionally leaves these questions for their correct specification owners.

## 002-E — Versioning / Provenance

- exact version identity model;
- how differences are represented;
- reason requirements for amendments;
- distinction between Judge amendment and paper capture correction;
- invalidation/supersession semantics;
- post-finalization correction authority.

## 002-F — Evaluation policy

- which scoring model(s) the initial competition implementation enables;
- exact decimal/rounding rules;
- compatibility rules across Rubric versions;
- cross-Scorecard aggregation;
- coverage requirements;
- outlier handling;
- tie policy;
- ranking eligibility.

## 002-H — Paper / external representations

- printable Rubric layout;
- how Judge/Team/Encounter identifiers appear on paper;
- paper verification workflow;
- machine-readable identifiers / QR usage;
- continuity during complete digital outage.

---

# 38. Exit position

002-D provides a stable evaluation contract:

```text
Authoritative Rubric Version
        │
        ├── Criterion definitions
        ├── valid score domains
        ├── scoring guidance
        ├── scoring model
        └── Note requirements
                 │
                 ▼

Effective Encounter Judge Obligation
                 │
                 ▼
             Scorecard
                 │
        ┌────────┴─────────┐
        │                  │
      Draft          Finalized v1
                           │
                           ▼
                    Amendment Draft
                           │
                           ▼
                      Finalized v2
```

The key boundary is:

```text
one Rubric
    defines one Judge's scoring semantics

one Scorecard
    records one Judge's judgment

002-F aggregation
    combines multiple authoritative judgments
```

No new concept is required.

The next group is **002-E — Versioning, Provenance, Correction & Authority Preservation**, which can now specify exactly how authoritative Rubrics and Scorecards retain history, how Judge judgment is distinguished from capture correction, and how legitimate correction occurs without erasing authorship or prior state.

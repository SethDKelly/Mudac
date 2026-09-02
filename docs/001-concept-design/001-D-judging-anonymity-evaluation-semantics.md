# 001-D — Judging Model, Anonymity & Evaluation Semantics

**Status:** Complete  
**Phase:** 001 — Concept Design Foundation

## Purpose

Define what evaluation means before formal concept acceptance or UI design. This includes Rubric semantics, Scorecard meaning, aggregation, evaluation coverage, ranking, anonymity, revision, and Award relationships.

## Fundamental unit of judgment

The smallest authoritative judgment is:

> One Judge's Scorecard for one Team in one Judging Encounter using one identified Rubric version.

A logical Scorecard may have revisions, but those revisions do not create multiple evaluations.

```text
Encounter E014
  Judge J032
    Scorecard S091
      v1
      v2
```

## Rubric versus Scorecard

- **Rubric** — defines how evaluation should occur.
- **Scorecard** — records one Judge actually performing that evaluation.

A Rubric may define Criteria, descriptions, valid score ranges, scoring guidance, weighting, completeness rules, and Note policy.

## Criterion semantics

A Criterion should communicate what is being judged and what the score scale means. Numeric values must be bounded by the Rubric.

Important distinction:

```text
Missing != 0
```

A missing response means no judgment has been supplied. Zero is a deliberate valid score only when allowed by the Rubric.

Scoring Criteria are required by default before Scorecard finalization. N/A must only exist when explicitly defined by Rubric semantics.

## Notes

A Criterion may contain an optional qualitative Note. The Scorecard may also contain an overall Note.

Notes provide evaluation evidence/context but do not secretly change numeric scoring. If something should affect the numeric result, it belongs in the Rubric or declared scoring policy.

Judge Notes are private evaluation records, initially visible only to the authoring Judge during the authorized event access window and to authorized Organizers.

## Scorecard total

A Scorecard total is derived from Criterion responses under one coherent scoring model. The system should avoid accidental double-weighting by mixing point maxima and independent percentage weights without explicit semantics.

Judges should not separately type an arbitrary overall total when it is already derivable from Criteria, unless the Rubric intentionally defines a holistic scored Criterion.

## Aggregation hierarchy

```text
Criterion score
  -> Scorecard total
      -> Encounter aggregate
          -> Team Competition aggregate
              -> Division rank
```

These are distinct perspectives and should not all be represented as one generic `score` field.

## Default aggregation

The working default is equal Judge weighting across all eligible finalized Scorecards for a Team.

Encounter averages are useful analytical projections but should not normally be re-averaged in a way that gives Judges on smaller Panels more implicit weight.

Aggregation policy should remain explicit/configurable rather than hidden in code.

## Evaluation coverage

Coverage is distinct from numeric aggregation.

- **Aggregation** asks: what do the valid judgments numerically produce?
- **Coverage** asks: did the Team receive enough qualifying judging to be treated as competition-complete/eligible?

A Team may have a mathematically valid average and still have incomplete judging coverage.

Missing Scorecards are never converted to zero. Temporary aggregates may be shown with clear incomplete/provisional state, but insufficient coverage requires explicit policy or Organizer resolution.

## Encounter participation and denominator

Expected Scorecards should follow actual Encounter participation, not blindly follow current Panel membership. Recusal or legitimate non-participation should be distinguishable from a forgotten/missing Scorecard.

## Coverage exception

If live-event circumstances make perfect coverage impossible, an Organizer may eventually authorize a documented exception. Such an exception should be explicit and provenance-preserving rather than silently changing arithmetic.

## Outliers and normalization

The system should not automatically discard unusual scores or normalize Judge tendencies by default.

Outlier or Judge/Panel scoring patterns may be surfaced to Organizers for investigation. Different perspectives are intentional in the Panel model; unusual judgment is not automatically invalid judgment.

## Anonymity boundary

The system should not claim absolute anonymity. The application can guarantee **system-enforced institutional identity shielding**.

```text
Team
  Administrative Identity
    institution
    members
    registration data

  Competition Identity
    anonymous Team ID
    Division
```

Judges receive Competition Identity and Division. Organizers can resolve the underlying Team as needed.

Printed materials must preserve the same shielding rules as digital judging.

## Judge information independence

During judging, a Judge may see:

- Team competition identity;
- Division;
- Rubric;
- own Scorecard;
- own Notes;
- necessary Panel/event context.

A Judge should not see:

- peer Scorecards;
- peer Criterion scores;
- peer Notes;
- Team/Panel aggregate;
- Division ranking;
- competition standings.

The working policy is that Judges also do not receive competition-wide standings through this UI after the event.

## Scorecard finalization and amendment

Finalization means the Judge asserts that the Scorecard is their completed judgment and it becomes eligible for aggregation.

Preferred amendment behavior:

```text
Finalized v1
  -> Amendment Draft
      -> Finalized v2
```

While the amendment Draft exists, v1 remains the authoritative version. Once v2 finalizes, v2 replaces v1 in derived scoring and v1 remains historical.

## Revision provenance

Revisions should preserve at least:

- prior version;
- new version;
- actor;
- time;
- changed fields;
- reason where policy requires it.

The system must distinguish Judge evaluation change from Organizer paper-transcription correction.

Organizers should not silently rewrite electronic Judge judgment. If a Judge can perform the correction, they should. Exceptional Organizer correction must retain explicit provenance.

## Rubric version compatibility

Rubric revisions may be editorial or scoring-semantic. Scoring-semantic changes after judging begins must not silently change prior Scorecard meaning or comparability.

Existing Scorecards always retain their original Rubric basis.

## Panel-Team repeat encounters

A Panel should normally evaluate a particular Team at most once in a Competition. Scorecard corrections remain revisions inside the existing Encounter. Extraordinary rejudging should be explicit and provenance-preserving.

## Ranking

Ranking is derived, not authored. By default it compares eligible Teams within their Division.

Live rank is provisional. Official rank exists only after reconciliation/finalization.

Tie behavior must be governed by declared policy; ties must not be broken by arbitrary implementation details such as Team ID or database order.

## Awards

Award and Rank are distinct:

- Rank expresses ordering.
- Award expresses recognition.

Rank-derived Awards may synchronize from official ranking. Alternative Awards such as Most Innovative or Best Applied Analysis may be Organizer-conferred after review of scores, Notes, and deliberation.

Discretionary Awards must not be represented as if they were mathematically derived when they were not.

## Evaluation layers

```text
1. Rubric semantics
2. Individual Judge judgment
3. Encounter/Panel analytical perspective
4. Competition aggregation and coverage
5. Competition outcome: Rank and Awards
```

## Fairness dimensions

- identity fairness;
- perspective fairness;
- judgment independence;
- coverage fairness;
- aggregation fairness.

## Explainability invariant

Every official result should be decomposable through:

```text
Rank
  -> Team Aggregate
      -> eligible Scorecards
          -> Criterion responses
              -> exact Rubric version
```

and horizontally through Judge, Panel, Encounter, Notes, and revision history.

## Behaviors the system must never perform silently

- treat missing scores as zero;
- expose institutional Team identity to Judges;
- expose peer scores/Notes to Judges;
- overwrite Scorecard history;
- count revisions as additional evaluations;
- mutate Rubric semantics beneath prior Scorecards;
- normalize Judge scoring without explicit policy;
- automatically discard statistical outliers;
- rank insufficiently evaluated Teams as though coverage were complete;
- obscure tie behavior;
- imply discretionary Awards were mathematical;
- replace Judge authorship with Organizer authorship during paper capture.

## Default working semantics

| Area | Default |
| --- | --- |
| Criterion response | Numeric, bounded by Rubric |
| Criterion completion | Required |
| Criterion Note | Optional |
| Overall Note | Optional |
| Logical Scorecard | One per Judge per Encounter |
| Scorecard weighting | Equal Judge weighting |
| Encounter aggregate | Mean of eligible finalized participant Scorecards |
| Team aggregate | Mean of all eligible finalized Judge Scorecards |
| Missing Scorecard | Incomplete; never zero |
| Automatic outlier removal | None |
| Automatic normalization | None |
| Ranking | Division-scoped |
| Tie | Explicit policy/resolution |
| Judge standings visibility | None through judging UI |
| Scorecard amendment | Versioned |
| Active amendment authority | Last finalized version remains authoritative |
| Paper evaluation | Same semantics as electronic |
| Awards | Rank-based or discretionary |

## Exit position

Judgment, Coverage, and Outcome are intentionally separate. This prevents missing Judges, uneven Panels, outliers, ties, paper scoring, discretionary Awards, and revisions from collapsing into special-case score arithmetic.

Next: **001-E — Candidate Concept Discovery**.

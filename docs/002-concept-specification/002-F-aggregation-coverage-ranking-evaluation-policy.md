# 002-F — Aggregation, Coverage, Ranking & Evaluation Policy

Status: **Complete**

## 1. Purpose

002-F specifies the derived evaluation-policy layer that consumes authoritative judging evidence and produces explainable Competition outcomes.

The principal mechanisms specified here are intentionally **not** promoted into standalone Concepts:

- Scorecard eligibility;
- Encounter analytical aggregation;
- Team Aggregation;
- Evaluation Coverage;
- Division Ranking;
- tie handling;
- outlier diagnostics;
- Rubric-version aggregation compatibility;
- provisional/result-readiness state.

These mechanisms are derived from accepted Concepts and authoritative policy.

The central separation is:

```text
Authoritative Evidence
        ↓
Eligibility
        ↓
┌──────────────────┬──────────────────┐
│                  │                  │
▼                  ▼                  │
Coverage        Aggregate             │
│                  │                  │
└──────────┬───────┘                  │
           ▼                          │
      Rank Eligibility                │
           │                          │
           ▼                          │
     Division Ranking                 │
```

A numerically valid Aggregate does not by itself mean a Team has received sufficient judging to be rank-eligible.

The specification remains implementation-neutral. Query engines, materialized views, cache strategy, event processing, database technology, numerical libraries, and AWS services remain downstream concerns.

---

# 2. Evaluation Policy

Evaluation Policy remains authoritative Competition configuration rather than a standalone Concept.

## Purpose

> Declare the rules by which authoritative individual judgments become eligible, sufficiently covered, comparable, aggregated, and ranked.

Evaluation Policy should be understandable independently of implementation code. Competition outcomes must not rely on hidden constants.

## Conceptual policy state

A policy snapshot may contain:

```text
Evaluation Policy
    aggregation basis
    coverage requirements
    Encounter/composition eligibility rules
    Team eligibility rules
    Rubric compatibility declarations
    outlier treatment
    ranking scope
    ranking comparison precision
    tie policy
```

The initial baseline fixes several defaults while leaving event-specific quantities configurable.

## Policy authority and versioning

Before a Competition becomes Ready, it must have one valid authoritative Evaluation Policy.

002-F confirms Evaluation Policy as another appropriate consumer of the Versioning/Provenance mechanisms defined in 002-E.

Once judging has begun, changing rules such as:

- aggregation basis;
- minimum Coverage;
- exclusion rules;
- ranking precision;
- tie-break rules;
- Rubric compatibility;

can change Competition outcomes without changing any Judge judgment.

Therefore an Active or later Competition must never silently mutate these semantics. A consequential policy change creates a new authoritative policy state/version with Organizer authority, reason, Provenance, and explicit downstream impact review.

An outcome must remain reconstructible against the policy state that produced it.

---

# 3. Eligible evaluation evidence

Aggregation starts from **current authoritative evaluation evidence**, not from every Scorecard row/version ever recorded.

A Scorecard is ordinarily eligible for official Team aggregation only when all of the following hold:

1. it is the current authoritative finalized Version of its logical Scorecard;
2. it belongs to the stable Team being evaluated by the relevant Encounter;
3. its Encounter is valid for official use;
4. its Judge Participation was an effective evaluation participant/obligation for that Encounter;
5. the Scorecard has not itself been explicitly invalidated or excluded through a legitimate correction process;
6. its Rubric Version is aggregation-compatible with the policy scope in which it is being combined;
7. the Team is eligible for the relevant derived calculation under Competition policy.

An Amendment Draft does not replace the current finalized Version and therefore does not temporarily remove the existing authoritative Scorecard from eligibility.

## Explicit exclusion reasons

Evidence exclusion must remain explainable. Examples include:

```text
Encounter invalidated
Scorecard structurally invalidated
superseded Scorecard Version
Judge obligation excused before authoritative evaluation
incompatible Rubric basis
Team withdrawn / not rank eligible
```

The system must never simply omit a Scorecard from official computation with no inspectable reason.

---

# 4. Invalidated and replacement Encounters

An invalidated Encounter contributes no official Scorecards to Coverage or Aggregate unless an exceptional policy explicitly states otherwise.

If:

```text
Encounter E-014
    Invalidated
        │
        ▼
Encounter E-052
    Replacement
```

then E-014 remains historically inspectable but E-052 is the candidate valid occurrence for Coverage and aggregation.

The original Scorecards and Notes are not deleted.

This is why invalidation is distinct from Scorecard Version supersession.

---

# 5. Evaluation Coverage

Coverage is a derived statement about the sufficiency of judging.

It answers:

> Has this Team received enough qualifying evaluation, under the Competition's declared policy, to participate in an official ranking?

Coverage is independent from the Team's numerical Aggregate.

## Coverage dimensions

The initial model supports three related dimensions.

### Valid Encounter coverage

How many valid Judging Encounters has the Team completed?

For example:

```text
required minimum: 5
valid completed: 4
```

### Eligible Scorecard coverage

How many eligible authoritative Judge evaluations exist?

For example:

```text
required minimum: 13
eligible Scorecards: 12
```

This allows Competition policy to tolerate legitimate variation in Panel size without converting missing Judges into zeroes.

### Composition coverage / exceptions

Did the Team's qualifying Encounters satisfy required Panel-composition policy, or were deviations explicitly accepted?

For example:

```text
Encounter E-014
    3 Judges
    Academic ✓
    Business ✓
    Technical ✗
    Organizer exception accepted
```

Composition exceptions are not silently equivalent to compliant composition. The exception remains visible and attributable.

## Configurable quantities

002-F does not hard-code values such as:

```text
5 Encounters
15 Scorecards
```

A Competition may declare:

```text
minimum valid Encounters
minimum eligible Scorecards
composition-exception behavior
```

according to its event rules.

---

# 6. Encounter completion versus Coverage

Encounter completion and Team Coverage are different.

An Encounter is Complete when all **effective obligations for that occurrence** are resolved.

A Team can therefore have:

```text
4 Complete Encounters
```

while Competition policy requires:

```text
5 Complete valid Encounters
```

The individual Encounters are complete, but Team Coverage remains incomplete.

Likewise an Encounter may legitimately contain two Scorecards because the third nominal Panel member was absent before judging; that does not create a missing Scorecard within that Encounter. Whether the Team still has enough overall Scorecard Coverage is a separate Competition-level question.

---

# 7. Coverage status

Coverage should expose both measured facts and policy interpretation.

The baseline derived states are:

### Satisfied

All required Coverage conditions are met normally.

### Incomplete

One or more required conditions are not met and no exception has made the Team rank-eligible.

### Exception Accepted

The raw Coverage requirement is not fully met, but an authorized Organizer has explicitly accepted the deviation according to Competition policy.

An accepted exception must preserve:

- actual Coverage values;
- expected values;
- actor/authority;
- reason;
- timestamp;
- affected Team/scope.

The UI must not transform:

```text
12 / 15 evaluations
```

into an apparently ordinary `15 / 15` merely because an exception was accepted.

---

# 8. Coverage exceptions

Live events sometimes cannot achieve perfectly symmetrical judging.

Examples include:

- Judge illness;
- unavoidable Panel disruption;
- technical/event interruption;
- legitimate recusal;
- scheduling failure.

The baseline permits an Organizer-governed Coverage exception when Competition policy allows it.

This is an **eligibility decision**, not a fabricated evaluation.

The system must never create placeholder scores or zeros to satisfy Coverage numerically.

A Coverage exception requires explicit Provenance and becomes increasingly consequential after Event Completed.

---

# 9. Default aggregation basis — equal Judge weighting

The canonical initial aggregation basis is:

> **Every eligible authoritative Judge Scorecard contributes one equal unit of judging weight.**

If a Team has eligible Scorecard values:

```text
84, 91, 88, 90, 86
```

its Team Aggregate is the arithmetic mean of those individual Scorecard values.

Conceptually:

```text
sum(eligible Scorecard values)
──────────────────────────────
number of eligible Scorecards
```

This directly reflects the Phase 001 model in which individual Judge judgments are the fundamental evidence units.

## Why Panel averages are not averaged again

Suppose:

```text
Encounter A: 3 Judges
Encounter B: 2 Judges
```

Averaging each Encounter first and then averaging the two Encounter means would give each Judge in the two-Judge Encounter greater effective weight.

The baseline therefore computes the Team Aggregate directly over eligible individual Scorecards.

Encounter means remain useful analytical projections but do not become intermediate official weighting units.

## Unequal Panel sizes

Under equal-Judge weighting, an Encounter with four eligible Judge Scorecards contributes four individual judgments while an Encounter with three contributes three.

That is deliberate in the initial policy: each Judge judgment receives equal weight.

If a future Competition deliberately wants every Encounter/Panel to contribute equal weight regardless of Judge count, that should be introduced as an explicit alternative aggregation policy rather than hidden inside the default calculation.

---

# 10. Encounter analytical aggregate

For Organizer analysis, a valid Encounter may expose:

```text
Encounter Aggregate
    = mean of eligible Scorecard values
      for that Encounter
```

This answers:

> How did the Judges participating in this particular Encounter collectively evaluate the Team?

It is useful for:

- Panel tendency analysis;
- investigating unusual results;
- comparing Encounters;
- tracing Team Aggregate provenance.

It is not an independently authored Panel score.

---

# 11. Team Aggregate

The Team Aggregate is derived from all eligible authoritative Scorecard values in the ranking scope under the active Evaluation Policy.

It must remain decomposable to:

```text
Team Aggregate
    ↓
eligible Scorecard values
    ↓
Scorecard Versions
    ↓
Criterion responses
    ↓
Rubric Versions
```

The Aggregate is never directly editable by an Organizer.

If the Aggregate is incorrect, the cause must be resolved in:

- source evidence;
- eligibility;
- Coverage/policy;
- Rubric compatibility;

and the Aggregate recomputed.

---

# 12. Missing evaluations

Missing evaluation is never converted into zero.

If an Encounter expects three effective Scorecards and has only two finalized:

```text
84
90
missing
```

then the Encounter remains incomplete.

It is not:

```text
(84 + 90 + 0) / 3
```

If the third obligation is legitimately excused through an Encounter participant adjustment before authoritative evaluation, the Encounter's effective obligation count changes explicitly.

At Competition scope, insufficient total judging appears as Coverage Incomplete or Exception Accepted rather than as fabricated scores.

---

# 13. No automatic Judge normalization

The baseline does not statistically adjust a Judge merely because they tend to score higher or lower than peers.

The system must not silently perform transformations such as:

```text
Judge J-041 is historically 6 points low
    ↓
add 6 points to all J-041 Scorecards
```

This would change the meaning of the Judge's expressed evaluation and make results harder to explain.

Panel- and Judge-level distributions may be surfaced to Organizers as diagnostics, but no normalization occurs unless a future Competition deliberately introduces an explicit, published policy.

---

# 14. Outlier treatment

Statistical outliers remain eligible by default.

An unusual score may represent:

- a legitimate evaluator perspective;
- an input/capture error;
- misunderstanding of the Rubric;
- genuine disagreement;
- some other operational concern.

Therefore:

> **Outlier status alone is not grounds for automatic exclusion.**

The application may flag an unusual Scorecard or Criterion pattern for Organizer review.

If investigation finds a real error, the correction/invalidation mechanisms from 002-E apply.

The outlier flag itself never changes the Aggregate.

---

# 15. Rubric-version aggregation compatibility

Every Scorecard is bound to one exact Rubric Version.

002-F establishes that Scorecards may only be pooled into one Aggregate when their Rubric bases are declared **aggregation-compatible**.

## Same Rubric Version

Always compatible with itself.

## Editorial successor

A newer Rubric Version may be aggregation-compatible when the scoring semantics are demonstrably unchanged.

Example:

```text
v1:
"Explain model validation"

v2:
"Clearly explain model validation"
```

if score domain, anchors, weights, Criteria, and calculation remain semantically equivalent.

Compatibility should be explicitly established rather than inferred from matching maximum score alone.

## Scoring-semantic successor

A Version that materially changes:

- Criteria;
- score domains;
- anchors;
- weights;
- contribution mapping;
- Scorecard calculation;

is **incompatible by default**.

The system must not silently combine such Scorecards into one Team Aggregate.

## No implicit score conversion

The baseline does not automatically rescale or transform incompatible Rubric results.

For example, a 90/100 evaluation is not silently converted to be equivalent to a 4.5/5 evaluation unless a future explicit and defensible policy defines such semantics.

If mixed incompatible versions have been used, Organizer reconciliation is required before rank readiness.

---

# 16. Team eligibility for ranking

The default rank-eligibility conditions are:

1. Team is not withdrawn from official Competition participation;
2. Team has an eligible numerical Aggregate;
3. Team Coverage is `Satisfied` or `Exception Accepted` according to policy;
4. no unresolved Rubric-compatibility issue affects its Aggregate;
5. no unresolved authoritative correction makes the result materially affected;
6. Team has one valid current Division assignment.

A withdrawn Team's historical evaluation remains visible but is excluded from official Division ranking by default.

If a Competition wants a different withdrawal rule, it must be explicit policy.

---

# 17. Ranking scope

The initial ranking scope is:

```text
Competition
    ×
current valid Division assignment
```

Teams are compared only against rank-eligible Teams in the same Division.

A historical Encounter's presented Division remains preserved for provenance, but if the Organizer legitimately corrects a Team's Division, official ranking uses the corrected current Division assignment.

There is no implicit cross-Division overall ranking.

A Competition-wide Award may later consume evidence across Divisions according to Award policy, but it must not emerge accidentally from a globally sorted score table.

---

# 18. Ranking calculation

Within a Division:

```text
rank-eligible Teams
        ↓
compare Team Aggregates
        ↓
apply declared comparison precision
        ↓
apply declared tie policy
        ↓
Rank
```

Rank is derived and never directly authored under ordinary operation.

An Organizer cannot simply type:

```text
Team 014 = Rank 1
```

while leaving contradictory Aggregate evidence underneath it.

---

# 19. Numerical precision and display rounding

Calculation precision, ranking comparison precision, and display precision are distinct.

For example:

```text
stored/reproducible Aggregate:
87.436666...

display:
87.44
```

The baseline should retain sufficient precision to reproduce all calculations.

Display rounding must never mutate the authoritative derived value.

## Ranking comparison precision

The Competition policy must explicitly define whether ranking compares:

- the full authoritative computed precision; or
- a declared rounded comparison precision.

The default is to compare full authoritative precision.

If the event deliberately wants values equal to two decimal places to count as a tie, that must be a declared ranking rule rather than inferred from how the UI happens to display scores.

---

# 20. Tie semantics

A tie exists only after applying the declared ranking comparison precision and any predeclared tie-break policy.

The system must never break a tie using incidental implementation data such as:

- Team ID;
- database insertion order;
- random ordering;
- current display sort;
- hidden extra precision when policy says comparison stops earlier.

## Tie policy options

The baseline permits declared tie behavior such as:

1. shared Rank;
2. ordered tie-break by one or more explicitly designated Criterion aggregates;
3. additional judging / adjudication if the Competition defines such a process;
4. explicit Organizer adjudication under a declared Competition rule.

If no tie-break rule exists, the default is to preserve a shared Rank rather than invent an ordering.

For shared ranking, standard competition ranking is preferred conceptually:

```text
1, 2, 2, 4
```

rather than pretending one tied Team is third.

The exact presentation can be refined later.

## Criterion tie-breakers

A Criterion may only be used as a tie-breaker when:

- it was declared by policy before use;
- the relevant Scorecards/Rubric Versions are compatible for that Criterion;
- the Criterion aggregate is derived consistently from eligible Scorecards.

A hidden post-hoc choice of whichever Criterion favors a desired Team is prohibited.

---

# 21. Provisional versus ranking-ready

A numeric Ranking can be calculated during Active judging for Organizer operational awareness, but it remains provisional.

A Division is not **ranking-ready** while material unresolved conditions remain, including for example:

- Coverage Incomplete Teams that require resolution;
- unprocessed paper evaluations;
- incompatible Rubric Version use;
- unresolved invalidated/replacement Encounter relationships;
- pending authoritative corrections that materially affect outcomes;
- unresolved ties where policy requires a tie-break;
- missing/invalid Division assignments.

An active Scorecard Amendment Draft does not automatically remove the prior finalized Scorecard, but it is an important reconciliation signal because an authoritative change may still be pending.

002-G will use ranking readiness as part of the Competition finalization gate.

---

# 22. Derived status should be explainable

For each Team, an Organizer should be able to inspect something conceptually like:

```text
Team 014

Division:
    Undergraduate

Coverage:
    5 / 5 valid Encounters
    14 eligible Scorecards
    Satisfied

Aggregate:
    87.4367

Rank:
    2 — Provisional
```

and drill down to:

```text
Aggregate
    ↓
Encounter / Scorecard contributions

Coverage
    ↓
valid Encounters / obligations / exceptions

Rank
    ↓
Division population / precision / tie policy
```

A derived status without an explainable source chain is not sufficient.

---

# 23. Panel and Judge diagnostics

Organizer diagnostics may compute descriptive statistics such as:

```text
Panel average
Judge average
score distribution
criterion distribution
variance
possible outlier
```

These are analytical projections, not official evaluation state.

They must not automatically:

- change Scorecards;
- normalize Judges;
- exclude evidence;
- accuse a Judge or Panel of bias;
- change Rank.

They exist to support investigation and operational awareness.

---

# 24. Policy changes after judging starts

Changing aggregation/ranking policy after evidence exists is high consequence.

For example:

```text
Equal Judge weighting
        ↓
Equal Encounter weighting
```

or:

```text
minimum 12 Scorecards
        ↓
minimum 15 Scorecards
```

could alter eligibility or winners without any Judge changing their judgment.

Therefore after Active:

- the prior policy remains reconstructible;
- the new policy state is explicit/versioned;
- Organizer authority and reason are recorded;
- affected Aggregates/Coverage/Ranks are recomputed;
- the Competition is marked as requiring reconciliation;
- post-Finalization outcomes never silently migrate.

This applies the authority-preservation model from 002-E to derived-result semantics.

---

# 25. No direct editing of derived results

The following are derived, not directly editable domain facts:

```text
Encounter Aggregate
Team Aggregate
Coverage status
Rank
```

An Organizer can:

- correct source data;
- resolve exceptions;
- change authorized policy;
- invalidate or replace evidence through proper workflows;

but cannot simply overwrite a derived number to obtain a desired outcome.

This is a major integrity requirement.

---

# 26. Current baseline and future policy extensions

The initial baseline deliberately favors a small, explainable rule set:

```text
aggregation basis:
    equal eligible Judge Scorecards

missing evaluation:
    never zero

outlier:
    included unless explicitly invalidated for a real reason

normalization:
    none

ranking scope:
    Division

ranking comparison precision:
    full authoritative precision by default

tie with no declared resolver:
    shared Rank
```

Potential future extensions such as:

- equal-Encounter weighting;
- statistical Judge normalization;
- trimmed means;
- dropped-high/dropped-low scoring;
- score transformations between genuinely different Rubrics;

must be introduced explicitly as Competition policy and should not be implemented as hidden convenience behavior.

---

# 27. Stage / Round extension point

The current Phase 002 baseline assumes one Competition-level judging/ranking scope per Division.

If MUDAC is later required to model formal advancement stages such as:

```text
Initial Round
    ↓
Finalist Round
```

with distinct Encounter sets, Rubrics, Coverage, or independent Rankings, `Stage` / `Round` should be revisited as a possible Concept or explicit ranking scope rather than overloading Division, Award, or Encounter.

The current formulas and evidence model are intentionally structured so an additional scope dimension can be introduced later without changing the meaning of individual Scorecards.

This extension is not required to complete the present single-scope specification.

---

# 28. Synchronization contracts

## Scorecard finalization/amendment

```text
current authoritative Scorecard changes
        ↓
re-evaluate evidence eligibility
        ↓
refresh Encounter analytical aggregate
        ↓
refresh Team Aggregate
        ↓
refresh Coverage if eligibility changed
        ↓
refresh provisional Rank
```

## Encounter invalidation/replacement

```text
Encounter validity changes
        ↓
Scorecard eligibility changes
        ↓
Coverage + Aggregate refresh
        ↓
Rank refresh
```

## Division correction

```text
Team Division corrected
        ↓
Team leaves old ranking population
        ↓
Team enters corrected ranking population
        ↓
both Division Rankings refresh
```

## Coverage exception

```text
Organizer accepts allowed Coverage deviation
        ↓
Provenance recorded
        ↓
Coverage status = Exception Accepted
        ↓
Team may become rank-eligible
```

## Evaluation Policy change

```text
new authoritative policy state
        ↓
re-evaluate eligibility / Coverage / Aggregate / Rank
        ↓
mark affected outcome state for reconciliation
```

---

# 29. 002-F invariants

002-F adds or confirms these invariants:

1. Aggregation, Coverage, and Rank remain derived mechanisms rather than independently editable Concepts.
2. Every derived outcome is reproducible from authoritative evidence plus an identifiable Evaluation Policy state.
3. Only the current authoritative finalized Scorecard Version can contribute for one logical Scorecard.
4. Invalidated Encounter/Scorecard evidence does not contribute officially but remains historical.
5. Excluded evidence has an inspectable reason.
6. Missing evaluation is never converted into zero.
7. Coverage and numerical Aggregate are independent derived dimensions.
8. Encounter completion does not guarantee Team Coverage satisfaction.
9. Coverage exceptions never fabricate missing scores or hide actual Coverage.
10. Coverage exceptions require authority, reason, and Provenance.
11. The default Team Aggregate gives equal weight to eligible individual Judge Scorecards.
12. Encounter aggregates are analytical projections rather than intermediate official weighting units.
13. Unequal Panel sizes do not trigger hidden average-of-averages behavior.
14. Judge/Panel normalization is absent by default.
15. Statistical outlier status alone never excludes a Scorecard.
16. Rubric Versions must be aggregation-compatible before their Scorecards are pooled.
17. Scoring-semantic Rubric changes are incompatible by default.
18. No implicit score transformation/rescaling occurs across incompatible Rubrics.
19. Team ranking is Division-scoped by default.
20. Withdrawn Teams are excluded from official ranking by default while history remains preserved.
21. Rank is derived rather than directly authored.
22. Display rounding never mutates the authoritative Aggregate.
23. Ranking comparison precision is explicit policy and is distinct from display precision.
24. Ties are never broken by incidental implementation data.
25. With no declared tie resolver, a true tie remains shared.
26. Tie-break Criteria must be declared in advance and computed from compatible eligible evidence.
27. Provisional Ranking may exist before finalization, but unresolved eligibility/reconciliation issues prevent ranking readiness.
28. Derived results never silently remain stale after authoritative source/policy changes.
29. Post-Finalization derived outcome changes require explicit reconciliation rather than silent migration.
30. Direct manual editing of Aggregate, Coverage, or Rank is prohibited.
31. Evaluation Policy changes after judging begins are consequential authoritative changes and remain reconstructible.

---

# 30. Exit position

002-F establishes the complete derived scoring chain:

```text
AUTHORITATIVE SCORECARDS
        │
        ▼
   EVIDENCE ELIGIBILITY
        │
        ├───────────────┐
        ▼               ▼
     COVERAGE         AGGREGATE
        │               │
        └───────┬───────┘
                ▼
         RANK ELIGIBILITY
                │
                ▼
        DIVISION RANKING
                │
                ▼
      PROVISIONAL / READY
```

The initial policy is intentionally simple and explainable:

- equal weighting of eligible individual Judge Scorecards;
- no missing-as-zero behavior;
- no hidden normalization;
- no automatic outlier removal;
- explicit Rubric compatibility;
- Division-scoped Ranking;
- explicit Coverage eligibility;
- explicit precision and tie semantics;
- no direct editing of derived outcomes.

This gives 002-G a clean input. **002-G — Awards, Reconciliation, Finalization & Official Outcomes** can now define how a Competition moves from a fully explainable provisional state to an official one, how rank-derived and discretionary Awards are conferred, what reconciliation gates must be satisfied, and how post-finalization corrections affect previously official outcomes.
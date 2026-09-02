# 003-D — Organizer Competition Setup, Configuration & Readiness Experience

Status: **Complete**

## 1. Purpose

003-D defines the Organizer's preparation experience from a newly created Draft Competition through an explicitly trustworthy **Ready** state.

It translates the Phase 002 Competition, Division, Team, Alias, Rubric, Evaluation Policy, Award, Participation, Panel-preparation, Access, Versioning, Provenance, and Export semantics into a coherent preparation workspace without choosing a front-end framework, component library, route structure, file-import technology, database design, identity provider, or AWS service.

The governing objective is:

> An Organizer should be able to prepare a Competition in whatever practical order the event requires while always understanding what is configured, what remains incomplete, what is merely an operational risk, what would affect fairness or authority, and exactly why the Competition can or cannot be marked Ready.

The central preparation flow is:

```text
Competition Draft
      ↓
configure parallel preparation workstreams
      ↓
continuous validation + readiness assessment
      ↓
resolve blocking conditions
      ↓
review remaining operational warnings
      ↓
Organizer explicitly marks Competition Ready
      ↓
Ready for live-operation handoff
```

Readiness must be derived from authoritative source state rather than from manually checked boxes.

---

## 2. Preparation is a workspace, not a linear wizard

Real competition setup is not strictly sequential.

An Organizer may legitimately:

- import Teams before all Divisions are finalized;
- draft a Rubric while Judge registration is still open;
- configure Awards before Alias generation;
- define Evaluation Policy while Team counts are still changing;
- prepare Judge materials before final Panel formation;
- return to unfinished areas repeatedly.

Therefore the baseline should **not** force every Organizer through one irreversible wizard.

The experience is better understood as parallel preparation workstreams coordinated by one readiness model:

```text
Preparation
   │
   ├── Competition details
   ├── Divisions & Teams
   ├── Team attributes & Aliases
   ├── Rubric
   ├── Evaluation Policy
   ├── Awards
   ├── Judge preparation
   ├── Panel / staffing preparation
   └── Materials / continuity preparation
           │
           ▼
      Readiness assessment
```

A first-run guided path may later help inexperienced Organizers, but guidance must not redefine the underlying non-linear information architecture.

---

## 3. Preparation work regions

Within Organizer **Preparation** mode, the information architecture should expose a small number of task-oriented regions rather than one top-level navigation item for every Concept.

A conceptual grouping is:

### Competition

Purpose, event details, lifecycle, Divisions, Teams, Team attributes, and Aliases.

### Evaluation

Rubric, scoring semantics, Evaluation Policy, Coverage requirements, ranking/tie behavior, and evaluation readiness.

### People & judging preparation

Expected Judges, current Competition Participations, expertise completeness, planned staffing/panel readiness, and entry/onboarding preparation.

### Recognition

Award definitions, scopes, selection semantics, recipient cardinality, and required/optional closeout status.

### Materials

Judge/event materials, Rubric/paper-form preparation, Panel/join materials, and continuity readiness.

### Readiness

Cross-workstream status, blockers, warnings, impact explanations, and the explicit `Mark Ready` action.

These are experience regions, not new domain Concepts and not necessarily literal route names.

---

## 4. Readiness is a derived projection

The preparation experience may visually resemble a checklist, but the system must preserve a critical distinction:

```text
Organizer checks a box
        ≠
Competition requirement is satisfied
```

For example, `Teams ready` is derived from actual Team/Division/Alias state.

Conceptually:

```text
Team state
+
Division assignments
+
Alias assignments
+
Team participation status
        ↓
Structural Team readiness
```

Likewise:

```text
Rubric Draft
        ≠
Authoritative usable Rubric
```

and:

```text
Evaluation Policy form visited
        ≠
valid authoritative Evaluation Policy
```

The readiness workspace reports source truth and links back to the source that must be fixed.

---

## 5. Blocking conditions versus operational warnings

003-D establishes two major classes of preparation issue.

### Blocking condition

A state that makes Competition Ready invalid under authoritative domain rules or configured Competition policy.

Examples:

```text
2 active Teams have no Division
1 active Team has no Alias
Alias collision exists
no usable authoritative Rubric exists
Evaluation Policy is invalid
required Award definition is incomplete
```

A blocking condition prevents `markReady`.

### Operational warning

A condition that creates event-day risk but does not necessarily make the Competition structurally invalid.

Examples:

```text
4 expected Judges have not confirmed expertise
planned Judge pool may not satisfy all preferred Panel capacities
paper Rubric has not yet been generated
2 Judge invitations have not been accepted
no Panels have been formed yet
```

A warning remains visible and actionable, but it is not silently treated as a blocker unless Competition policy explicitly promotes it into a readiness gate.

This distinction prevents the system from becoming either dangerously permissive or unnecessarily brittle.

---

## 6. Readiness status vocabulary

The preparation experience should use a small, stable status vocabulary.

Conceptually:

```text
Ready
Needs attention
Warning
Not configured / optional
```

The exact labels can be refined in 003-I, but the semantic distinction must remain.

Each status should answer:

1. What is true now?
2. Does it block Ready?
3. Why?
4. What is the next useful action?

A status such as:

```text
Teams — Needs attention
2 active Teams are missing Aliases
```

is preferable to:

```text
Teams — 94% complete
```

when the missing 6% is actually a hard structural requirement.

---

## 7. Competition details experience

The Organizer begins with one clear Competition context.

Useful descriptive information may include:

```text
Competition name
scheduled event period
venue / location information
Judge-facing event instructions
Organizer-facing operational details where appropriate
```

The experience should distinguish:

```text
public / Judge-safe event information
```

from:

```text
Organizer-only operational information
```

rather than assuming everything typed into Competition details is safe for every audience.

Descriptive completeness may be part of configured readiness policy, but Competition should not become a general-purpose content management system.

---

## 8. Division configuration

Divisions are edited as competitive populations, not as decorative labels.

The Organizer should be able to understand:

```text
Division
    name
    description
    active / retired status
    number of assigned active Teams
```

The experience should make it difficult to accidentally reinterpret an existing Division after meaningful Competition use.

During Draft, ordinary definition/correction is low friction.

Before Ready, the workspace should expose conditions such as:

```text
Graduate — 14 Teams
Undergraduate — 22 Teams
Novice — 9 Teams

Unassigned — 2 Teams  ← blocking
```

No active Team should disappear from structural review merely because it has not yet been assigned.

---

## 9. Team setup experience

Team preparation should support both individual and bulk-oriented work.

The Organizer needs to establish a stable Team record without being forced to simultaneously complete every cross-concept relationship.

During Draft, a Team may temporarily appear as:

```text
Team internal record      ✓
Division                  missing
Alias                     missing
Team Name                 optional
Status                    Active
```

This is legitimate setup state.

The readiness workspace then makes the missing required relationships impossible to overlook before Ready.

---

## 10. Bulk Team intake

A real event may have dozens or hundreds of Teams.

The conceptual UX must therefore support bulk intake without committing to CSV, spreadsheet upload, API import, or another specific mechanism.

The bulk flow should behave approximately as:

```text
source records
      ↓
map / interpret fields
      ↓
preview proposed Team changes
      ↓
validate
      ↓
apply
      ↓
show accepted records + exceptions
```

The Organizer should not discover after import that:

- Teams silently failed;
- Divisions were inferred incorrectly;
- Aliases collided;
- a Team Name was mistaken for stable identity;
- duplicate records were created because one optional field differed.

Bulk intake must therefore surface exceptions before or immediately after application with clear recovery paths.

---

## 11. Team attributes

The 002-A1 refinement makes Team descriptive metadata extensible.

Organizer setup should expose attributes through defined field semantics rather than an arbitrary untyped key/value dumping ground.

A Team attribute definition may conceptually express:

```text
label
value type
required / optional
disclosure classification
editability / lifecycle expectations
competitive significance
```

The initial standard field is:

```text
Team Name
```

Additional attributes may be introduced later without creating new Concepts.

However:

> An attribute cannot acquire scoring, ranking, eligibility, or authority meaning merely because someone created a field with that name.

Competitive significance must be represented through explicit domain/policy semantics rather than hidden metadata behavior.

---

## 12. Team Name experience

`teamName` should feel lightweight and fun.

An Organizer may enter or import names such as:

```text
Bayes Brigade
Data Dragons
Null Hypothesis Heroes
```

The setup experience should reinforce that Team Name is:

```text
optional
non-unique
non-competitive
not the Alias
```

A missing Team Name must not prevent Ready unless a Competition explicitly configures it as a required descriptive field for some non-competitive reason.

The Judge-disclosure default remains:

```text
Organizer: visible
Judge during blinded evaluation: hidden
Public/post-event: separate disclosure decision
```

The Organizer should be able to preview this distinction before the event.

---

## 13. Team attribute disclosure review

Because custom Team metadata may accidentally expose institutional or personal identity, the preparation experience should make disclosure classification visible when attributes are defined or reviewed.

For example:

```text
Team Name
Judge visibility: Hidden
Organizer visibility: Visible
Public visibility: Not yet published / separately controlled
```

A custom field such as:

```text
Faculty Advisor
```

should not quietly become Judge-visible merely because it exists on the Team record.

The baseline posture is least disclosure.

---

## 14. Alias setup

Alias preparation should support deliberate individual assignment and safe bulk generation.

The Organizer needs to see:

```text
stable Team
current Alias
Division
Alias readiness
```

without treating administrative identity as Judge-facing output.

A bulk Alias workflow should conceptually support:

```text
choose / apply format policy
      ↓
preview candidate values
      ↓
validate uniqueness + safety
      ↓
assign
```

Alias generation must not derive values from institution identity or Team Name in a way that defeats blinded judging.

---

## 15. Alias readiness and correction

Before Ready, every non-withdrawn Team requires one active valid Alias.

The experience should clearly surface:

```text
42 active Teams
40 valid Aliases
2 missing
0 collisions
```

Once Alias values have been used in operational materials, later replacement may also make generated materials stale.

The preparation experience should therefore connect structural correction with material impact:

```text
Team 014 Alias changed
      ↓
2 previously generated Judge materials are now stale
      ↓
regeneration recommended / required by policy
```

Old operationally used Alias values remain historically reserved.

---

## 16. Judge-safe preview

A particularly important Organizer preparation capability is a **Judge-safe preview**.

Its purpose is not to impersonate a Judge account.

It is to answer:

> What identity and evaluation information would a Judge be shown if judging began using this configuration?

A preview may expose:

```text
Team 014
Undergraduate
Rubric content
Judge-safe event instructions
```

while deliberately hiding:

```text
institution
student/admin details
Team Name by default
Organizer-only attributes
other Judge scores
Rank / Aggregate
```

This provides a practical pre-event anonymity/disclosure check without collapsing Organizer mode into Judge mode.

---

## 17. Rubric preparation

Rubric setup should make the evaluation definition understandable as a whole rather than as disconnected Criterion records.

The Organizer needs to author and review:

```text
Rubric purpose / instructions
scoring model
ordered Criteria
valid score domains
criterion guidance / anchors
weights or point allocations
Note requirements
calculation semantics
```

The UX should continuously surface validation problems such as:

```text
weights do not sum as required
Criterion has no valid scoring domain
double weighting appears configured
required Note policy is inconsistent
Rubric cannot calculate deterministically
```

A Rubric can remain Draft while these problems exist.

It cannot become the authoritative judging basis until validation passes.

---

## 18. Rubric preview

The Organizer should be able to preview the evaluation instrument in Judge-safe terms before it becomes operational.

The preview should help answer:

- Is guidance understandable on a phone-sized judging experience?
- Are score choices unambiguous?
- Are required Notes obvious?
- Is Criterion order sensible?
- Does any text accidentally expose Organizer-only information?
- Does the printable representation retain the same evaluation semantics?

This is a semantic preview requirement, not a commitment to one visual component design.

---

## 19. Authoritative Rubric versus working revision

The setup experience must visually distinguish:

```text
Rubric v1 — authoritative / selected for use
Rubric v2 Draft — working, not in use
```

Creating or editing a future Draft does not silently change what current readiness is based on.

If the Organizer promotes a successor Rubric before Active:

```text
Rubric v2 becomes authoritative
      ↓
readiness is reassessed
      ↓
source-dependent materials may become stale
```

The Organizer should never be left wondering which Rubric Judges will actually receive.

---

## 20. Evaluation Policy setup

Evaluation Policy can materially alter outcomes even when all Scorecards are unchanged.

Therefore Organizer setup must present it as first-class Competition configuration rather than a hidden collection of implementation constants.

The policy experience should make understandable at least:

```text
aggregation basis
Coverage requirements
composition-exception behavior
Team/rank eligibility rules
Rubric compatibility assumptions
ranking comparison precision
tie policy
```

The canonical baseline defaults should be visible rather than implicit.

For example:

```text
Aggregation
Each eligible Judge Scorecard has equal weight

Missing evaluation
Never treated as zero

Ranking scope
Within Division

Outlier handling
No automatic exclusion
```

An Organizer should not need to reverse-engineer the application to understand how winners will be determined.

---

## 21. Progressive policy complexity

The UX should not force an Organizer to confront every theoretical policy extension if the baseline rules are sufficient.

A useful conceptual approach is:

```text
clear standard policy
      ↓
explicit advanced adjustments where supported
```

But advanced settings must remain visible in the authoritative policy summary once changed.

For example, if the default comparison uses full precision and the Organizer deliberately changes tie comparison to two decimal places, that rule should become conspicuous in readiness review.

Progressive disclosure may reduce cognitive load; hidden outcome logic is prohibited.

---

## 22. Coverage policy preparation

Coverage deserves direct readiness visibility because insufficient judging is distinct from numerical scoring.

Organizer preparation may define:

```text
minimum valid Encounters
minimum eligible Scorecards
Panel-composition expectation
exception policy
```

The setup experience should explain consequences in plain terms.

For example:

```text
A Team needs at least 4 valid Encounters
and 12 eligible Judge Scorecards
before it can be ranked normally.
```

This is preferable to exposing only low-level numeric fields with no explanation of what they control.

---

## 23. Ranking and tie preparation

Before judging begins, the Organizer should be able to inspect the declared ranking semantics.

At minimum:

```text
Ranking scope: Division
Comparison precision: full calculated precision
Tie behavior: shared Rank unless declared resolver applies
```

If a Criterion tie-break is configured, the experience should identify the exact Criterion and ordering before Active judging.

The application must not create a post-hoc “choose a tiebreaker” setup pattern that encourages outcome-driven rule changes after scores are known.

---

## 24. Award preparation

Award setup should distinguish clearly between:

```text
Rank-derived
Discretionary
```

For each configured Award, the Organizer should understand:

```text
name
description
scope
selection method
eligibility
recipient cardinality
required / optional for closeout
```

Examples:

```text
Undergraduate Champion
Division: Undergraduate
Selection: Rank 1
Recipients: exactly one unless tie policy resolves otherwise
Required for closeout: yes
```

and:

```text
Most Innovative
Scope: Competition-wide
Selection: discretionary
Recipients: one
Required for closeout: no
```

Award semantics should be defined before judging wherever practical rather than invented after Organizers see results.

---

## 25. Award readiness

The baseline readiness rule is:

> Every Award already configured for the Competition must be internally valid, and every Award definition required by the Competition's declared setup policy must exist before Ready.

The system does not need to require an optional discretionary Award merely because the product supports Awards.

If a Competition deliberately permits later Award creation, adding one after Active should be treated as a consequential outcome-governance change rather than an innocuous text edit.

---

## 26. Judge preparation

Organizer preparation should support an expected Judge roster without confusing expected participation with event-day presence.

Useful states include:

```text
Expected / invited
Participation established
Profile/expertise complete
Needs information
Withdrawn / unavailable
```

`Checked in` belongs to event-day operation and must not be faked during preparation.

The Organizer should be able to understand the current Judge pool in terms useful for Panel planning, such as expertise distribution, without treating expertise as an access role.

---

## 27. Judge preparation is not a hard universal Ready gate

A Competition may legitimately become Ready before every Judge has checked in—or even before final Panel membership is known.

Therefore the baseline distinguishes:

```text
configuration readiness
```

from:

```text
operational staffing readiness
```

Examples such as:

```text
3 expected Judges have not confirmed expertise
```

or:

```text
current expected pool may be short one Technical capacity
```

are important warnings.

They do not automatically mean the Competition's structural/evaluation configuration is invalid.

A Competition may promote specific staffing thresholds into hard gates through explicit policy, but the product should not universally require every volunteer to be present before `Ready` can be established.

---

## 28. Panel preparation

Because Panel formation may occur before the event or dynamically on event day, `Ready` must not universally require all Panels to be permanently assembled.

Preparation may support:

```text
planned Panels
expected Panel count
composition targets
provisional Judge assignments
room/logistics planning
```

while leaving final current membership to 003-E live operations.

The readiness workspace should distinguish:

```text
Panel configuration policy is valid
```

from:

```text
all day-of-event Panels are currently staffed
```

The first may be a configuration gate.

The second is typically an operational readiness condition.

---

## 29. Materials preparation

Materials are operationally important but not always required before structural Ready.

The preparation experience may show items such as:

```text
Judge quick-start material
printable Rubric / paper Scorecard
Panel/join materials
Event instructions
continuity packet
```

Each generated artifact should identify its source authority/version under Export semantics.

The readiness workspace should surface:

```text
current
stale
not yet generated
```

where meaningful.

Whether a material is a blocker is Competition policy, not a universal assumption.

---

## 30. Configuration readiness versus operational readiness

003-D establishes a two-layer preparation model.

### Configuration readiness

Answers:

> Is the Competition domain configuration coherent enough that live judging may legitimately be activated?

Typical hard conditions include:

```text
valid Competition structure
active Teams have exactly one Division
active Teams have exactly one valid Alias
authoritative usable Rubric exists
authoritative valid Evaluation Policy exists
configured required Award definitions are valid
no unresolved blocking structural inconsistency
```

### Operational readiness

Answers:

> How prepared are we to run the event smoothly right now?

Examples include:

```text
Judge roster completeness
expected expertise distribution
Panel staffing
materials generated
rooms assigned
paper fallback prepared
```

Operational readiness may contain warnings while the Competition is lifecycle `Ready`.

This is intentional.

---

## 31. Readiness workspace

The Organizer should be able to inspect one summary such as:

```text
Competition readiness

Competition details                 Ready
Divisions                           Ready
Teams & Aliases                     Needs attention
  • 2 Teams missing Alias
Rubric                              Ready — v3
Evaluation Policy                   Ready — v1
Awards                              Ready

Operational preparation
Judges                              Warning
  • 4 expected Judges missing expertise
Panel planning                      Warning
  • Technical capacity may be short
Materials                           Warning
  • Paper Rubric not generated
```

Each issue drills directly to the relevant source context.

The summary should not require the Organizer to search through every Team, Judge, or Rubric to discover exceptions.

---

## 32. Readiness progress should not hide severity

A single percentage such as:

```text
92% ready
```

is insufficient by itself.

One missing Alias can be more consequential than ten optional Judge biographies.

If an overall progress indicator is eventually used, it must remain subordinate to explicit blocker/warning semantics.

The Organizer needs to know **what matters**, not merely how many fields are filled.

---

## 33. `Mark Ready`

When all hard configuration gates pass, the Organizer may deliberately perform:

```text
Mark Competition Ready
```

The action should summarize the basis of readiness in human terms.

For example:

```text
Ready to mark Competition Ready

✓ 45 active Teams have valid Divisions and Aliases
✓ Rubric v3 is authoritative
✓ Evaluation Policy v1 is valid
✓ Required Award definitions are valid

Operational warnings
• 4 Judges still need expertise confirmation
• Paper judging forms have not been generated

Mark Ready
```

The Organizer is confirming the lifecycle transition, not manually certifying every underlying fact.

---

## 34. Ready with warnings

If only non-blocking operational warnings remain, the system may allow Ready while making those warnings conspicuous.

The experience should not quietly discard them after the lifecycle transition.

They should continue into the live-operation handoff where relevant.

For example:

```text
Competition Ready

Before judging begins:
• confirm remaining Judge expertise
• complete Panel staffing
• generate paper fallback forms
```

This supports resilience without diluting the meaning of the Ready state.

---

## 35. Changes while Competition is Ready

`Ready` is not permission to silently mutate the configuration that readiness depended upon.

Changes fall into three UX categories.

### Readiness-neutral change

Example:

```text
fix venue parking instructions
edit optional Team Name
```

If no configured gate or authoritative evaluation meaning is affected, the Competition may remain Ready.

### Readiness-relevant change that remains valid

Example:

```text
replace one valid Alias with another valid unused Alias before operational use
```

The system reassesses readiness and any Export impact.

If all gates remain satisfied, Ready may remain valid, but affected materials may become stale.

### Readiness-invalidating change

Example:

```text
add active Team without Division/Alias
remove required Criterion from authoritative Rubric workflow
make Evaluation Policy invalid
retire a Division that still has active Teams
```

Before committing an intentional change, the Organizer should be told:

```text
This change will make the Competition no longer Ready
and return it to Draft.
```

The transition should never be a surprising side effect discovered later.

---

## 36. Ready state and working Draft configuration

Versioned domains allow a useful distinction.

For example:

```text
Rubric v3 — authoritative / current Ready basis
Rubric v4 Draft — not in use
```

Editing the v4 Draft does not itself invalidate Ready because Judges would still use v3.

Only when the Organizer commits/promotes a new authoritative source state does readiness reassess against that state.

This pattern prevents experimentation from accidentally changing live configuration while still keeping the active basis obvious.

The same principle can apply to other versioned policy/configuration where supported.

---

## 37. Returning Ready → Draft intentionally

An Organizer may deliberately reopen structural preparation before Active.

The UX should distinguish:

```text
Continue preparing a working Draft artifact
```

from:

```text
Return Competition to Draft
```

The latter is a lifecycle action and should explain consequences such as:

- judging cannot start;
- readiness must be re-established;
- previously generated materials may require review;
- current preparation warnings remain visible.

This should not be conflated with ordinary edits to non-authoritative working content.

---

## 38. Activation belongs to the live-operation handoff

003-D ends at a trustworthy `Ready` state.

It should make the next event-day transition understandable:

```text
Competition Ready
      ↓
Organizer live-operation context
      ↓
confirm day-of-event operational state
      ↓
activate judging
```

The detailed activation experience, Judge check-in monitoring, Panel formation, Encounter operation, and live exceptions belong to 003-E.

This keeps preparation from swallowing the entire Organizer lifecycle.

---

## 39. Validation layers

Organizer setup benefits from three conceptual validation layers.

### Local validity

Is one field/value valid?

Example:

```text
score domain must contain allowed values
```

### Concept validity

Is one Concept internally coherent?

Example:

```text
Rubric calculation is deterministic
```

### Cross-concept readiness

Do independent Concepts compose into a Competition that may be marked Ready?

Example:

```text
all active Teams have Division + Alias
and an authoritative Rubric/Policy exists
```

The UX should identify which level failed instead of reducing everything to generic form errors.

---

## 40. Bulk changes need impact preview

Bulk configuration is efficient but increases the consequence of mistakes.

For changes such as:

```text
assign Division to 20 Teams
generate 50 Aliases
change attribute disclosure policy
replace many Judge expectations
```

The experience should preview scope and detected exceptions before high-impact application where practical.

A bulk operation should never hide partial failure.

If 48 of 50 changes succeeded, the Organizer needs an explicit view of the two unresolved records and the resulting readiness impact.

---

## 41. Destructive setup behavior

During early Draft preparation, truly accidental unused records may be deleted where Phase 002 permits it.

The UX should become more conservative once a record participates in meaningful history.

Even during setup, the Organizer should understand why an operation is offered as:

```text
Delete accidental unused Team
```

versus:

```text
Withdraw Team
```

or:

```text
Retire Division
```

The experience should not normalize destructive deletion as the standard way to fix domain mistakes.

---

## 42. Copying prior Competition configuration

A future convenience may allow Organizers to initialize a new Competition from prior configuration.

If introduced, the UX must preserve the current domain boundaries.

Appropriate candidates for copying may include:

```text
Division definitions
Rubric as a new working basis
Evaluation Policy defaults
Award definitions
Team attribute definitions
```

It must not silently copy as current authority:

```text
prior Judge Participations
prior Panel memberships
prior Teams as current competitors
prior Scorecards
prior Awards/conferrals
prior Official Outcome
prior Access grants
```

Because this convenience is not required for the present product boundary, 003-D leaves it as an extension point rather than introducing a Template Concept.

---

## 43. Organizer authority and dual-role posture

Preparation is Organizer work.

A person who also has Judge Participation performs setup in explicit Organizer mode.

The system should not allow a Judge-mode context to expose:

```text
Team administrative identity
Alias mapping
Rubric editing
Evaluation Policy editing
Award configuration
```

merely because the same Identity also has Organizer authority elsewhere.

This preserves the role-mode information barrier established in 003-A.

---

## 44. Provenance and consequence

Not every Draft keystroke requires formal Provenance.

The preparation UX should increase attribution as changes become consequential.

For example:

```text
Draft Team Name correction
    low consequence

mark Competition Ready
    meaningful lifecycle event

replace authoritative Rubric basis
    meaningful authority event

change Evaluation Policy after meaningful operational use
    high consequence / later phase governance
```

The UX should not turn provenance into bureaucratic noise, but it must not obscure meaningful authority transitions.

---

## 45. Setup interruption and recovery

Organizer preparation may span days or weeks.

The application must therefore preserve meaningful Draft setup state across interruption and device changes according to future persistence design.

The Organizer should return to understandable context such as:

```text
Competition Draft

3 blockers
4 warnings

Last work:
Rubric v4 Draft
```

rather than relying on browser history to reconstruct where preparation stood.

Working Draft content and authoritative configuration must remain visually distinguishable after recovery.

---

## 46. Error language

Preparation errors should identify the domain consequence and recovery action.

Prefer:

```text
Team 027 cannot be counted as structurally ready because it has no Alias.
Assign an Alias or withdraw the Team before marking the Competition Ready.
```

rather than:

```text
Validation error.
```

Likewise:

```text
Rubric v4 is still a Draft and is not the judging basis.
Rubric v3 remains authoritative.
```

is better than ambiguous `Unsaved changes` language.

---

## 47. Accessibility and device posture

Organizer setup will often benefit from larger displays, but it must remain operable without assuming:

```text
hover
fine pointer control
color-only readiness states
wide tables as the only representation
```

Bulk-heavy workflows may reasonably be optimized for desktop/tablet while still providing accessible semantic alternatives.

Readiness blockers and warnings require text labels and navigable descriptions.

Detailed cross-phase accessibility requirements remain for 003-H.

---

## 48. 003-D UX invariants

003-D establishes or confirms the following experience invariants:

1. Organizer preparation is non-linear and workspace-oriented rather than a mandatory one-pass wizard.
2. Readiness is derived from source state, not manual checklist completion.
3. Blocking conditions and operational warnings remain distinct.
4. Every readiness issue identifies why it matters and where to fix it.
5. Active Teams may be temporarily incomplete only during Draft.
6. Team setup supports bulk operation and explicit exception handling.
7. Team Name remains optional, non-unique, non-competitive, and distinct from Alias.
8. Team attribute disclosure is explicit and Judge-safe by default.
9. Custom Team metadata does not acquire hidden scoring/ranking semantics.
10. Alias generation/assignment cannot expose institutional identity and must validate uniqueness.
11. Alias/material dependencies become visible when correction makes an Export stale.
12. Judge-safe preview exposes the disclosure a Judge would receive without impersonating Judge authority.
13. Rubric Draft and authoritative Rubric remain visually distinct.
14. Rubric validation prevents incoherent scoring semantics from becoming the judging basis.
15. Evaluation Policy is first-class visible Competition configuration.
16. Standard policy defaults are understandable rather than hidden constants.
17. Advanced policy changes remain visible in the authoritative summary.
18. Coverage rules are explained as eligibility requirements, not only numeric fields.
19. Tie behavior is declared before judging rather than improvised after results appear.
20. Award setup distinguishes rank-derived and discretionary recognition.
21. Configured required Award definitions must be valid before Ready.
22. Expected Judge registration and actual day-of-event check-in remain distinct.
23. Incomplete staffing may be a warning without universally blocking Competition Ready.
24. Panel policy readiness and current day-of-event Panel staffing remain distinct.
25. Materials may be current, stale, or missing and remain traceable to source state.
26. Configuration readiness and operational readiness are separate but visible together.
27. A percentage cannot replace blocker/warning semantics.
28. `Mark Ready` is an explicit Organizer lifecycle action after derived gates pass.
29. Non-blocking warnings remain visible after Ready.
30. Ready-state changes trigger explicit readiness reassessment.
31. Readiness-invalidating changes do not silently leave Competition marked Ready.
32. Working future Drafts do not silently replace authoritative Ready-basis configuration.
33. Returning Competition Ready → Draft is distinct from editing a working Draft artifact.
34. Bulk changes do not hide partial failure.
35. Destructive deletion is limited to appropriate unused setup records.
36. Organizer/dual-role context preserves Judge information barriers.
37. Preparation recovery preserves meaningful working context.
38. Setup error language identifies current truth and recovery action.
39. Activation remains a live-operation handoff rather than being conflated with setup completion.

---

## 49. 003-D exit position

The Organizer preparation experience now has a coherent operating model:

```text
COMPETITION DRAFT
      ↓
┌────────────────────────────────────────────┐
│ Competition details                       │
│ Divisions                                 │
│ Teams + Team attributes / Team Names      │
│ Aliases                                   │
│ Rubric                                    │
│ Evaluation Policy                         │
│ Awards                                    │
│ Judge / Panel preparation                 │
│ Materials / continuity preparation        │
└────────────────────────────────────────────┘
      ↓
continuous validation
      ↓
CONFIGURATION READINESS
      +
OPERATIONAL WARNINGS
      ↓
Organizer `Mark Ready`
      ↓
COMPETITION READY
      ↓
live-operation handoff
```

The important result is that `Ready` now has an understandable human experience without becoming a manually maintained checklist state.

The Organizer can work flexibly during Draft, but the application continuously reconciles that work against the authoritative Competition rules and exposes exactly what prevents legitimate activation.

The next subgroup is therefore:

**003-E — Organizer Judge, Panel, Encounter & Live Operations Experience**

003-E can begin from a Competition that is structurally/evaluatively Ready and focus on the event-day questions:

- Which expected Judges actually arrived?
- Which Judges are ready or need help?
- How should Panels be composed and adjusted?
- Which Teams/Encounters are currently in progress or complete?
- Which Scorecards are unfinished, uncertain, paper-fallback, or amended?
- Which recusal, staffing, device, connectivity, or wrong-context exceptions need Organizer action?
- How can the Organizer maintain situational awareness without exposing unnecessary live scoring spectacle?

# 002-C — Panel, Membership & Judging Encounter Specifications

Status: **Complete**

## 1. Purpose

002-C specifies the concepts and subordinate state that connect event-scoped Judge Participation to an actual Team evaluation occurrence.

Concepts specified here:

1. Panel
2. Judging Encounter

Panel Membership remains subordinate Panel state rather than an independent concept.

The central distinction is:

```text
Panel
    who is intended to judge together

Judging Encounter
    who actually evaluated this Team on this occurrence
```

This distinction must remain explicit because live competitions involve absence, late arrival, recusal, replacement, reassignment, uneven Panel sizes, and operational correction.

The specification remains implementation-neutral. Scheduling technology, QR mechanics, database relationships, concurrency primitives, UI routes, APIs, and AWS services remain downstream concerns.

---

## 2. Cross-concept model

```text
JUDGE PARTICIPATION
        │
        │ current membership
        ▼
      PANEL
        │
        │ intended judging group
        │
        ├───────────────┐
        │               │
        ▼               ▼
participant        composition
membership          evaluation
        │               │
        └──────┬────────┘
               │
               ▼
             TEAM
               │
               │ Panel + Team
               ▼
       JUDGING ENCOUNTER
               │
               ├── presented Team context snapshot
               ├── starting participant snapshot
               ├── participant adjustments
               └── evaluation obligations
```

Panel describes current intended grouping. Encounter preserves the historical evaluation context.

---

# 3. Panel specification

## Purpose

> Maintain a reusable grouping of active Judge Participations who are intended to evaluate Teams together during a Competition.

Panel exists so Organizers do not need to reconstruct a Judge group independently for every Team presentation.

Panel does not own Judge identity, expertise, Team assignment, Rubric semantics, Scorecards, aggregation, or ranking.

## State

Conceptual state:

```text
Panel
    id
    Competition scope
    human-facing label
    status
    membership history
```

Recommended status semantics:

```text
Active
Retired
```

`Active` means the Panel remains available for operational use subject to Competition state and composition policy.

`Retired` means it should not begin new Encounters. Retirement preserves historical membership and Encounter relationships.

Panel does not need Draft/Ready/Active lifecycle states parallel to Competition. Its readiness/composition quality is a derived policy evaluation.

## Actions

```text
create
rename
addMember
endMembership
replaceMember
assignCompositionCapacity
clearCompositionCapacity
retire
restore
```

## Queries

```text
currentMembers
membershipHistory
currentCapacityAssignments
compositionStatus
isAvailableForEncounter
encounters
```

`compositionStatus` and `isAvailableForEncounter` are evaluated with Competition policy and Participation state; Panel does not hard-code a particular judge count or expertise taxonomy.

## Operational Principle

An Organizer creates a Panel, adds available Judge Participations, assigns composition capacities where useful, checks whether the grouping satisfies the Competition's Panel-composition policy, and uses the Panel across repeated Team Judging Encounters. Membership may change during the event without rewriting the historical participant context of prior Encounters.

---

# 4. Panel Membership specification

Panel Membership remains relational state owned by Panel.

A membership should preserve enough information to represent sequential reassignment rather than only the current `panel_id` of a Judge.

Conceptual membership state:

```text
Panel Membership
    Judge Participation reference
    Panel reference
    effective start
    effective end, if ended
    assigned composition capacity, optional
    status
```

This is not promoted into an independent Concept because its purpose is fully explained by Panel composition.

## Membership invariants

1. Only a Judge Participation may be an ordinary Panel member.
2. The Judge Participation and Panel must be scoped to the same Competition.
3. An inactive, withdrawn, or completed Judge Participation cannot begin new judging through Panel membership.
4. A Judge Participation should have at most one overlapping active Panel membership in the same Competition by default.
5. Sequential reassignment between Panels is permitted and historical memberships remain retained.
6. Ending a Panel membership never rewrites prior Judging Encounters.
7. Membership does not itself create Scorecard authority; actual Encounter participation does.

The one-current-Panel rule is a strong default rather than an assertion that every future competition format must forbid floating judges. A future policy may deliberately support concurrent assignments, but the default live-event model should avoid ambiguity about where a Judge is expected to participate.

---

# 5. Expertise versus composition capacity

Judge Expertise remains Participation state.

Example:

```text
Judge J-041
Expertise:
    Academic
    Technical
```

A Panel may assign that Judge one composition capacity:

```text
Panel 07
Academic capacity → J-041
```

This distinction is important:

```text
Expertise
    what perspectives the Judge can credibly contribute

Composition capacity
    which perspective this membership is satisfying for this Panel
```

A composition capacity grants no additional application authority.

By default, one Judge should satisfy at most one required composition capacity within the same Panel. This prevents a multidisciplinary Judge from accidentally satisfying multiple required seats and making a nominal three-perspective Panel effectively one or two people.

Additional Judges may exist as at-large members if Competition policy permits.

---

# 6. Panel composition policy

Panel composition requirements are policy, not intrinsic Panel behavior.

For example, one Competition might express:

```text
minimum Judges: 3
preferred maximum: 4
required capacities:
    Academic: 1
    Business: 1
    Technical: 1
```

Another Competition may use entirely different requirements.

Panel therefore exposes current membership/capacity state, while a policy evaluation derives conditions such as:

```text
Compliant
Degraded
Noncompliant
```

The exact labels remain a later UX/policy concern.

A Panel that does not meet the ideal composition may still need to operate during a live event. The system should surface the deviation and, where policy requires, obtain an explicit Organizer exception rather than making the event brittle.

---

# 7. Panel changes during the event

Panel membership is intentionally mutable during Competition Active.

Example:

```text
09:00
Panel 07
    J-A
    J-B
    J-C

11:00
J-C leaves

11:10
Panel 07
    J-A
    J-B
    J-D
```

The membership history should preserve both configurations.

Prior Encounter:

```text
Encounter E-014
participants:
    J-A
    J-B
    J-C
```

Later Encounter:

```text
Encounter E-028
participants:
    J-A
    J-B
    J-D
```

Neither Panel nor Participation should attempt to rewrite E-014 when membership changes.

Membership changes during Competition Active are meaningful operational changes and should later synchronize with Provenance.

---

# 8. Participation changes and Panel membership

When Judge Participation becomes withdrawn, completed, or otherwise ineligible during an Active Competition, that Judge must no longer be treated as available for new Encounter participation.

The application may synchronize the Participation change by ending current Panel membership or by marking it operationally unavailable until the Organizer resolves membership. The implementation choice may vary, but the behavioral invariant is:

> An ineligible Judge Participation cannot silently remain an eligible participant for a new Encounter.

Existing Encounter history remains unaffected.

---

# 9. Judging Encounter specification

## Purpose

> Represent one bounded occurrence in which one Panel evaluates one Team within a Competition.

Judging Encounter is the historical anchor that prevents evaluations from being modeled as loose Scorecards attached directly to Teams.

It establishes:

- which Team was being judged;
- which Panel was involved;
- which Judges actually participated;
- which Team identity and Division context were presented;
- when the occurrence began and ended;
- which evaluation obligations were created;
- whether the occurrence is valid for official judging.

## State

Conceptual state:

```text
Judging Encounter
    id
    Competition reference
    Panel reference
    stable Team reference
    presented Team Alias snapshot
    presented Division snapshot
    lifecycle state
    created time
    begun time
    presentation-completed time, optional
    completed time, optional
    starting participant snapshot
    participant adjustments
    evaluation-obligation state
    replacement relationship, optional
    invalidation/cancellation reason, optional
```

The applicable Rubric/evaluation-basis reference will be completed in 002-D, but Encounter is the correct context in which that basis becomes fixed for judging.

---

# 10. Encounter lifecycle

002-C standardizes the Encounter lifecycle as:

```text
Prepared
   ↓
Open
   ↓
Complete
```

with exceptional terminal paths:

```text
Prepared → Cancelled
Open/Complete → Invalidated
```

A replacement is represented as an explicit relationship to another Encounter rather than as a generic lifecycle state.

## Prepared

The Panel and Team relationship has been established but judging has not begun.

Prepared supports both:

- pre-created/planned Encounter records; and
- a very short-lived state immediately before an ad hoc Encounter begins.

Participant obligations are not yet authoritative.

## Open

Judging has begun.

At transition to Open, the application captures the starting participant/context snapshot and creates the basis for individual evaluation obligations.

An Open Encounter may remain open after the Team presentation ends while one or more Judges finish their Scorecards.

Therefore `presentation completed` is recorded as event/context state rather than requiring another Encounter lifecycle state.

## Complete

The occurrence has satisfied its required evaluation obligations and is no longer awaiting ordinary Judge work.

Completion does not mean its Scorecards or the Encounter can never be corrected. Later correction/version policy still applies.

## Cancelled

A Prepared Encounter was abandoned before meaningful judging began.

Cancellation should not be used to erase a judging occurrence that actually happened.

## Invalidated

The Encounter occurred, but an authorized decision determines that it must not contribute to official evaluation.

Invalidation preserves:

- Encounter history;
- participant history;
- any Scorecards already produced;
- the reason and authority for invalidation.

002-F will determine how invalidated Encounters and their Scorecards are excluded from Coverage/Aggregation.

---

# 11. Encounter actions

Conceptual actions:

```text
prepare
begin
confirmPresentationComplete
recordParticipantAdjustment
complete
cancel
invalidate
linkReplacement
```

`complete` may normally occur through synchronization once required evaluation obligations are satisfied rather than through a free-form Organizer toggle.

## Queries

```text
currentState
presentedTeamContext
startingParticipants
participantHistory
effectiveEvaluationParticipants
outstandingEvaluationObligations
isValidForOfficialEvaluation
replacementEncounter
```

---

# 12. Encounter Operational Principle

A Panel is ready to judge a Team. An authorized Judge or Organizer selects/confirms the Team. The application prepares or resolves the corresponding Encounter. When judging begins, the Encounter snapshots the Team-facing context and the Panel participants expected to evaluate. Judges independently complete Scorecards. Any absence, recusal, or replacement is recorded as an explicit participant adjustment rather than silently changing history. Once all remaining required evaluation obligations are resolved, the Encounter becomes Complete.

---

# 13. Team context snapshot

002-A established that historical Encounters must preserve the Alias presented at judging time.

002-C extends this to the relevant Team context:

```text
Encounter E-014
    stable Team → Team X
    presented Alias → Team 014
    presented Division → Undergraduate
```

If the Organizer later corrects:

```text
current Alias → Team 027
current Division → Graduate
```

E-014 still records what the Judges actually saw:

```text
Team 014
Undergraduate
```

This does not prevent downstream policy from recalculating ranking eligibility using the corrected current Division. It simply preserves historical judging context.

---

# 14. Starting participant snapshot

When an Encounter becomes Open, the system captures the expected participating Judges at that moment.

Conceptually each starting participant entry contains at least:

```text
Judge Participation reference
Panel membership reference/context
assigned composition capacity, if any
start-of-Encounter inclusion
```

This is a historical snapshot, not a pointer to whatever the Panel happens to look like later.

The starting participant set normally derives from current eligible Panel members but must be confirmable so absence or recusal known before judging does not create false Scorecard obligations.

---

# 15. Participant adjustment model

A completely immutable participant set would not accurately model live judging.

Instead, Encounter preserves:

```text
starting participant snapshot
        +
explicit participant adjustments
        ↓
effective evaluation participants
```

Examples of adjustments include:

```text
recused
excused / absent
late-added replacement
removed before evaluation obligation
```

An adjustment never erases the fact that the Judge appeared in the starting snapshot if they were there at the beginning.

This gives the system truthful history and correct evaluation obligations simultaneously.

---

# 16. Recusal and non-participation

A Judge may need to recuse because they recognize a Team, have a conflict, or otherwise cannot fairly evaluate it.

Recusal must never be represented as:

```text
score = 0
```

or as an unexplained missing Scorecard.

Instead:

```text
Judge J-041
starting participant
        ↓
recused
        ↓
no Scorecard obligation
```

The Encounter retains the recusal/non-participation disposition and, where appropriate, a reason category or note.

The exact conflict taxonomy remains policy/configuration rather than a new concept.

---

# 17. Absence before Encounter start

If a Panel normally contains three Judges but only two are actually present when the Team presentation starts, the starting snapshot should contain the two actual participants.

Therefore:

```text
Panel current membership count
        ≠ necessarily
Encounter evaluation obligation count
```

This prevents an absent Judge from appearing forever as a missing Scorecard.

The degraded two-Judge composition may still trigger a composition-policy exception, but that is different from creating a nonexistent evaluation obligation.

---

# 18. Mid-Encounter departure or recusal

If a Judge begins an Encounter but then must leave or recuse before forming an authoritative evaluation, the Encounter records an adjustment.

The evaluation obligation may be excused according to policy.

If the Judge already finalized a Scorecard, removing that evaluation is no longer a simple participant correction.

The application must not silently delete or disregard the authoritative Scorecard. Any exclusion requires the later correction/invalidation and evaluation-policy mechanisms specified in 002-E/002-F.

---

# 19. Late replacement

A replacement Judge may occasionally join after an Encounter has begun.

The preferred operational path is:

```text
Organizer establishes/updates valid Panel membership
        ↓
Encounter records late participant adjustment
        ↓
new Judge becomes an evaluation participant
        ↓
Scorecard obligation created
```

The Encounter therefore preserves that the Judge was added after the initial snapshot.

Whether late entry is permitted after a particular point in the presentation is Competition policy, not Encounter's intrinsic behavior.

---

# 20. Encounter participant eligibility

An ordinary Encounter participant must satisfy all of the following:

```text
active Judge Participation
same Competition
appropriate current Access
ordinary Panel membership or explicit Organizer-authorized adjustment
```

A Person's Identity alone is insufficient.

A historical Judge Participation from a prior Competition is insufficient.

Expertise alone is insufficient.

This preserves the Identity → Participation → Access boundaries from 002-B.

---

# 21. Encounter initiation authority

The initial product requirement allows Judges to select the Team they are about to evaluate.

Therefore an authorized Panel Judge may be given a capability such as:

```text
beginEncounter
```

within their current Panel context.

Organizers may also begin or prepare Encounters operationally.

The important domain rule is that Panel members are joining one shared Encounter, not each creating independent encounters for the same Panel-Team presentation.

---

# 22. Duplicate-safe Encounter initiation

Multiple Judges on the same Panel may attempt to select/confirm the same Team at nearly the same time.

The application must converge on one logical Encounter.

Conceptually:

```text
Panel 07 + Team 014
Judge A begins
Judge B begins milliseconds later
        ↓
ONE Encounter
```

not:

```text
Encounter E-014A
Encounter E-014B
```

The eventual implementation must therefore make Encounter initiation safe under retry/concurrency, but the specific transaction/idempotency mechanism is deferred.

---

# 23. Repeat Panel-Team protection

The default Competition invariant is:

> One Panel should normally produce at most one valid Judging Encounter for the same Team in the same Competition.

Thus:

```text
Panel 07 × Team 014
        ↓
one valid Encounter
```

If a Judge later edits a Scorecard, that remains the same Encounter.

If a legitimate rejudging is required, it must be explicit rather than accidentally doubling the Panel's influence.

---

# 24. Replacement Encounter

When rejudging is necessary, the application should preserve the original occurrence and create a new Encounter linked as its replacement.

Example:

```text
Encounter E-014
    invalidated
        │
        │ replaced by
        ▼
Encounter E-052
```

The original Encounter and Scorecards remain historical.

002-F later determines which Encounter contributes to Coverage and Aggregation.

This is preferable to deleting E-014 and pretending it never happened.

---

# 25. Cancellation versus invalidation

The distinction is now canonical.

### Cancel

Use when meaningful judging never began.

```text
Prepared → Cancelled
```

### Invalidate

Use when a judging occurrence happened but should not count officially.

```text
Open/Complete → Invalidated
```

This protects historical truth and avoids using deletion as an operational correction mechanism.

---

# 26. Presentation completion versus Encounter completion

The Team presentation may end before every Judge finishes their Scorecard.

Therefore:

```text
presentation complete
        ≠
Encounter Complete
```

Example:

```text
10:20 presentation ends

Judge A finalized ✓
Judge B finalized ✓
Judge C still drafting

Encounter remains Open
presentationCompletedAt = 10:20
```

When Judge C resolves their evaluation obligation:

```text
Encounter → Complete
```

This gives Organizers accurate operational visibility without inventing another lifecycle state.

---

# 27. Encounter completion semantics

An Encounter becomes Complete when every effective evaluation participant has an evaluation obligation that is either:

```text
satisfied by an authoritative Scorecard
```

or:

```text
explicitly excused through a valid participant disposition/policy
```

A missing unresolved Scorecard cannot be silently treated as complete.

The exact Scorecard authority and finalization semantics are defined in 002-D/002-E.

---

# 28. Panel composition at Encounter time

Current Panel composition is useful for planning, but fairness analysis should also evaluate the people who actually participated in each Encounter.

Therefore the application should be able to derive both:

```text
Panel composition now
```

and:

```text
Encounter composition at judging time
```

Example:

```text
Panel 07 current:
    Academic
    Business
    Technical

Encounter E-014 actual:
    Academic
    Business
```

The Encounter can therefore carry a composition exception even if the Panel was nominally well formed before or after that occurrence.

---

# 29. Composition exceptions

If the actual Encounter participants fail Competition composition policy, the application should surface the issue.

Depending on policy, the Encounter may:

```text
be blocked from beginning
```

or:

```text
proceed under explicit Organizer exception
```

The initial MUDAC direction favors operational resilience: imperfect staffing should be visible and attributable rather than automatically making judging impossible.

A composition exception does not itself change numeric scoring. 002-F will define any effect on evaluation eligibility.

---

# 30. Panel and Encounter privacy

Judges may know:

- their Panel;
- the other Judges judging with them;
- current Team Alias;
- current Team Division;
- their own Encounter/Scorecard completion state.

They should not obtain peer Scorecards, peer Notes, Team aggregates, or Competition rankings simply because they share Panel membership.

Thus:

```text
Panel membership
    ≠
peer-evaluation access
```

002-B Access remains authoritative for disclosure.

---

# 31. Panel operational history

Organizer-facing Panel history should be reconstructable as:

```text
Panel 07
    membership periods
    capacity assignments
    Teams encountered
    actual participant sets
    composition exceptions
```

This is useful for understanding how judging operated without turning Panel into a scoring object.

Panel-level score statistics remain derived projections addressed in 002-F.

---

# 32. Encounter operational history

For any Encounter, an authorized Organizer should be able to reconstruct:

```text
which Team
which presented Alias
which presented Division
which Panel
who was expected at start
who actually remained eligible to evaluate
who recused/was excused/was added
when the presentation ended
whether evaluation obligations completed
whether Encounter was cancelled/invalidated/replaced
```

Scorecard details are added by 002-D and provenance details by 002-E.

---

# 33. Synchronization contracts

## Participation → Panel eligibility

```text
Judge Participation Active
        ↓
eligible for Panel membership
```

When Participation becomes ineligible:

```text
Participant cannot enter new Encounters
        +
current Panel membership must be operationally resolved
```

## Panel + Team → Encounter

```text
valid Panel
+
participating Team
+
authorized begin action
        ↓
Prepared/Open Judging Encounter
```

## Encounter begin → historical snapshots

```text
current Team Alias
+
current Team Division
+
current eligible Panel participants
+
current composition capacities
        ↓
Encounter starting context snapshot
```

## Encounter begin → Scorecard obligations

```text
Encounter Open
+
effective Judge participants
+
applicable Rubric basis
        ↓
one logical Scorecard obligation per Judge
```

The Rubric/Scorecard side is completed in 002-D.

## Participant adjustment → obligation update

```text
recusal / absence / late addition
        ↓
explicit participant adjustment
        ↓
evaluation obligation set recalculated
```

Existing authoritative Scorecards are never silently erased by this synchronization.

## Evaluation obligations → Encounter completion

```text
all obligations satisfied or explicitly excused
        ↓
Encounter Complete
```

## Encounter invalidation → derived evaluation

```text
Encounter Invalidated
        ↓
Coverage/Aggregation eligibility reassessed
```

002-F defines the numerical consequences.

---

# 34. Cross-concept invariants established by 002-C

1. Panel and Judging Encounter are distinct concepts.
2. Panel Membership is subordinate Panel state, not a separate Concept.
3. Only current Competition Judge Participations are ordinary Panel members.
4. A Judge Participation has at most one overlapping active Panel membership by default.
5. Panel membership changes never rewrite historical Encounter participant context.
6. Expertise and assigned composition capacity are distinct.
7. A Judge ordinarily satisfies at most one required composition capacity per Panel.
8. Panel composition rules are Competition policy, not hard-coded expertise roles.
9. A Judging Encounter joins exactly one stable Team and one Panel in one Competition.
10. Encounter start snapshots the Team Alias and Division presented to Judges.
11. Encounter start preserves the starting Judge participant context.
12. Participant changes after start are explicit adjustments rather than silent snapshot mutation.
13. Recusal, absence, and missing evaluation are distinct states.
14. Recusal never becomes a zero score.
15. Actual Encounter participants, not nominal Panel membership, determine ordinary Scorecard obligations.
16. A Judge who already produced an authoritative Scorecard cannot have that evaluation silently removed through participant adjustment.
17. Panel members share Encounter context but not one another's evaluations.
18. Same Panel + same Team normally yields at most one valid Encounter per Competition.
19. Legitimate rejudging creates an explicit replacement Encounter rather than duplicating or overwriting the original.
20. Cancellation applies before meaningful judging; invalidation preserves a judging occurrence that should not count.
21. Presentation completion and Encounter completion are distinct.
22. Encounter completion requires all effective evaluation obligations to be resolved.
23. Duplicate/retried Encounter initiation must converge on one logical Encounter.
24. Composition deviations are surfaced and policy-governed rather than silently ignored.
25. Invalidated Encounters and their Scorecards remain historical even when excluded from official scoring.

---

# 35. Deliberate non-concepts and deferrals

002-C does not introduce:

```text
Panel Seat concept
Panel Membership concept
Recusal concept
Schedule concept
Room concept
Presentation concept
Assignment concept
```

Composition capacity, membership, recusal disposition, and presentation-complete time are subordinate state or policy.

Formal event scheduling remains deferred because current behavior can support both planned and ad hoc Encounter creation without a dedicated Scheduling concept.

The following details are deferred:

- exact default minimum/maximum Panel size;
- exact expertise taxonomy;
- exact composition exception rules;
- whether late replacements are allowed after presentation start;
- whether simultaneous Encounters for one Team are blocked or warned;
- formal room/timetable management;
- exact conflict/recusal reason taxonomy;
- exact UI mechanics for Team selection or Encounter join;
- exact Scorecard creation/finalization behavior;
- exact effect of invalidation or replacement on Coverage/Aggregation.

These map to later specification groups rather than exposing a missing concept.

---

# 36. 002-C Exit Position

002-C confirms the core judging topology:

```text
JUDGE PARTICIPATION
        │
        ▼
      PANEL
        │
        │ current intended composition
        │
        └──────────┐
                   │
TEAM ──────────────┤
                   ▼
          JUDGING ENCOUNTER
                   │
                   ├── Team context at time of judging
                   ├── starting participant snapshot
                   ├── explicit participant adjustments
                   └── effective evaluation obligations
```

The most important refinement is that historical truth and operational flexibility coexist.

Panel membership may change. Judges may be absent, recuse, or be replaced. The Encounter does not freeze an inaccurate fiction and does not overwrite history. Instead it preserves the starting context and records explicit adjustments from which the effective evaluation obligations are derived.

This gives 002-D a stable foundation:

```text
Encounter
    determines
who is evaluating what, and under which historical context

Rubric + Scorecard
    will determine
how each of those Judges expresses an independent evaluation
```

No additional concept is required before proceeding to **002-D — Rubric, Criterion, Scorecard & Notes Specifications**.

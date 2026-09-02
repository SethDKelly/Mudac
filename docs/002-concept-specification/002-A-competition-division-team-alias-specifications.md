# 002-A — Competition, Division, Team & Alias Specifications

Status: **Complete**

## 1. Purpose

002-A turns the Phase 001 structural concepts into explicit behavioral specifications. It covers the concepts that establish the Competition context, partition Teams into competitive cohorts, represent competing Teams administratively, and expose Teams to Judges through bias-reducing competition identities.

Concepts specified here:

1. Competition
2. Division
3. Team
4. Alias

The specification remains implementation-neutral. Database tables, API shapes, UI routes, AWS services, authentication mechanisms, and concrete identifier formats remain downstream concerns.

---

## 2. Cross-concept structural model

```text
COMPETITION
    │
    ├── DIVISION
    │      │
    │      └── Team assignment
    │
    └── TEAM
           │
           └── ALIAS
                 │
                 └── Judge-facing Competition Identity
```

The diagram represents scope and synchronization rather than object ownership.

The four concepts retain independent purposes:

- Competition governs the lifecycle/context of one competition occurrence.
- Division owns competitive partition definitions and Team-to-Division assignment.
- Team owns the administrative representation and participation status of one competing student group.
- Alias owns a context-safe alternate identity and its mapping to an underlying subject.

---

# 3. Competition specification

## Purpose

> Establish the lifecycle and governing context of one competition occurrence.

Competition exists so that application behavior can be scoped to a particular event occurrence and can move through meaningful operational authority boundaries.

Competition does not own Team, Division, Panel, Rubric, Scorecard, Award, or access behavior. Those concepts are coordinated with Competition through synchronization and policy.

## State

Conceptual state:

```text
Competition
    id
    name
    event details
    lifecycle state
    scheduled event period
    lifecycle transition timestamps
```

`event details` may include Organizer-managed descriptive information such as venue, date/time, and instructions. It does not imply a separate Event Information concept.

### Lifecycle states

002-A standardizes the working lifecycle as:

```text
Draft
  ↓
Ready
  ↓
Active
  ↓
Event Completed
  ↓
Finalized
```

`Historical` is **not** a separate business lifecycle state. A completed/finalized Competition can be presented as historical after the event, but archival presentation does not change competition semantics.

`Reconciliation` is also **not** a separate required lifecycle state. Reconciliation is the Organizer activity occurring primarily between Event Completed and Finalized.

### State meanings

**Draft**
- Competition preparation is underway.
- Structural configuration may be incomplete.
- Teams may temporarily be missing a Division or Alias while Organizer setup/import is in progress.
- No official judging may occur.

**Ready**
- The Organizer has explicitly asserted readiness after application-level readiness checks pass.
- Required structural and later-phase evaluation configuration is coherent enough to activate the Competition.
- Changes capable of invalidating readiness must cause readiness to be reassessed and may return the Competition to Draft.

**Active**
- Live event/judging operation is open.
- Judge participation and judging behavior may occur according to later specifications.
- Changes with competition-impacting consequences require stronger controls and provenance.

**Event Completed**
- Live judging has ended.
- Ordinary Judge access to private Scorecards, Notes, and judging history should expire through Access synchronization.
- Organizer reconciliation, paper capture, authorized amendments, coverage resolution, ranking review, and Award determination may continue.

**Finalized**
- Scoring and Award outcomes have been accepted as official.
- Ordinary outcome-changing operations are closed.
- Legitimate corrections remain possible only through exceptional, strongly attributable workflows; Finalized does not mean the data is physically impossible to correct.

## Actions

### `create`
Creates a Competition in Draft state.

### `updateDetails`
Changes descriptive/event information without changing the Competition lifecycle.

Changes after information has been exported or published may later cause external artifacts to become stale; this is specified in 002-H.

### `markReady`
Moves Draft → Ready.

The Competition concept requires only the correct current state. The application synchronization may invoke this action only after readiness policies derived from related concepts pass.

### `returnToDraft`
Moves Ready → Draft before activation when configuration is intentionally reopened or a readiness-invalidating change occurs.

### `activate`
Moves Ready → Active.

### `completeEvent`
Moves Active → Event Completed.

This transition is operationally important because it signals that live Judge participation has ended and should synchronize with later Access rules.

### `resumeEvent`
Exceptional transition Event Completed → Active.

This exists to recover from an erroneous or premature event close or a genuine decision to resume live judging. It must be treated as a high-consequence operation and later synchronized with Access reactivation and Provenance.

It is not permitted after Competition Finalization.

### `finalize`
Moves Event Completed → Finalized after application-level reconciliation/finalization gates pass.

## Queries

Useful conceptual queries include:

- `state(competition)`
- `isDraft(competition)`
- `isReady(competition)`
- `isActive(competition)`
- `isEventCompleted(competition)`
- `isFinalized(competition)`
- `eventDetails(competition)`
- `scheduledPeriod(competition)`

`structuralReadiness` is a derived application query rather than Competition-owned state.

## Operational Principle

An Organizer creates a Competition and prepares its related Divisions, Teams, identities, judging configuration, and operational materials. Once readiness checks pass, the Organizer marks it Ready and activates it for the live event. When judging ends, the Organizer completes the event, causing ordinary Judge evaluation access to expire while Organizer reconciliation continues. Once scoring, eligibility, ranking, and Awards have been settled, the Organizer finalizes the Competition and the record remains available historically.

## Invariants

1. Official judging cannot occur while the Competition is Draft or Ready.
2. Finalized cannot transition back to Active through ordinary Competition behavior.
3. Event Completed and Finalized are distinct authority boundaries.
4. Competition finalization does not erase prior states, evaluations, or provenance.
5. Competition state does not determine Team identity disclosure by itself; Access and Alias composition do.
6. A Competition may be historically retained without introducing a separate Historical lifecycle state.

## Failure and exceptional behavior

- Invalid lifecycle transitions fail explicitly rather than being silently coerced.
- `markReady` must not succeed when application readiness checks fail.
- `activate` must not occur from Draft.
- `resumeEvent` is exceptional and requires stronger authorization/provenance than ordinary event completion.
- Finalization readiness is not owned solely by Competition; later specifications define unresolved Scorecard, Coverage, Ranking, and Award gates.

## Explicit non-responsibilities

Competition does not:

- define Divisions;
- create Teams;
- assign Team aliases;
- create Panels or Encounters;
- define Rubrics;
- create Scorecards;
- calculate Aggregation/Coverage/Rank;
- confer Awards;
- directly grant or revoke Access.

Those behaviors compose with Competition through application synchronization.

---

# 4. Division specification

## Purpose

> Partition competing Teams into mutually exclusive populations that should be compared against one another.

Division exists because teams at materially different academic/experience levels should not necessarily compete in the same ranking population.

Division names and counts are Competition configuration, not software constants. Examples such as Novice, Undergraduate, Graduate, or Post-Graduate are instances rather than enum values baked into the architecture.

## State

Conceptual state:

```text
Division
    definitions:
        division id
        competition scope
        name
        description
        status

    assignment:
        Team → Division
```

A Division definition can be Active or Retired.

Retirement preserves historical identity while preventing new assignment.

## Actions

### `define`
Creates a new active Division definition within a Competition scope.

### `updateDefinition`
Changes the human-facing name/description of a Division.

A semantic change that would effectively turn an existing Division into a different competitive category should be treated cautiously after judging begins; rename/correction is different from changing competitive meaning.

### `retire`
Prevents new Team assignments while preserving the Division definition historically.

A Division with active competing Teams should not be retired until those assignments are resolved.

### `assign`
Associates a Team with one Division.

During Competition Draft, setup/import may temporarily leave a Team unassigned. Before Ready/Active, every non-withdrawn Team must have exactly one active Division assignment.

### `correctAssignment`
Replaces a Team's Division assignment because the prior assignment was wrong.

This is explicitly a **correction**, not normal Team movement between competitive cohorts.

## Queries

- `divisionOf(team)`
- `teamsIn(division)`
- `activeDivisions(competition)`
- `isDivisionActive(division)`
- `isAssigned(team)`

Historical change explanation belongs to Provenance rather than Division itself.

## Operational Principle

An Organizer defines the Competition's Divisions and assigns each Team to the appropriate competitive cohort. The assignment remains stable during normal competition operation. If the Organizer discovers that a Team was misclassified, they explicitly correct the assignment; existing Judge evaluations remain evaluations of that Team while downstream Division-scoped calculations are recomputed according to policy.

## Invariants

1. A non-withdrawn Team may have **at most one** active Division assignment at any time.
2. Before Competition Ready/Active, each non-withdrawn Team must have **exactly one** active Division assignment.
3. New Teams cannot be assigned to a Retired Division.
4. Assignment correction does not mutate existing Scorecards.
5. Division is independent of Team Alias; changing Division does not require changing Team Competition Identity.
6. Ranking is expected to use Division assignment but remains a derived mechanism specified in 002-F.

## Correction behavior

### Before Active
A mistaken assignment can be corrected with low operational consequence. Provenance requirements may be lighter but the correction should still be distinguishable from original assignment when useful.

### During Active or Event Completed
A correction is high consequence because it may affect:

- ranking population;
- coverage policy;
- Award eligibility;
- Organizer analytics.

The change must be explicit, attributable, and trigger recalculation/reassessment of derived outputs. Completed Scorecards remain unchanged.

### After Finalized
Ordinary assignment correction is closed. A legitimate correction uses the exceptional post-finalization process defined later in 002-G and 002-E.

## Explicit non-responsibilities

Division does not:

- store Team administrative identity;
- generate aliases;
- score Teams;
- determine Team eligibility from judging coverage;
- calculate Rank;
- select Awards.

---

# 5. Team specification

## Purpose

> Maintain the administrative representation and competition participation status of one student group acting as a single competitor.

Team represents the entity that is evaluated. Students remain outside the application actor model in the current product boundary.

## State

Conceptual state:

```text
Team
    id
    competition scope
    administrative record
    participation status
```

The administrative record contains only information Organizers actually need to operate the Competition. It may include an internal label and institutional information, but Phase 002-A does **not** require individual student accounts or a detailed student-person model.

Data minimization should be preferred: do not collect student-level personally identifiable information merely because the system can store it.

### Team participation status

Working states:

```text
Active
Withdrawn
```

A Team may exist administratively during Competition Draft before all cross-concept readiness relationships (Division assignment/Alias) have been established.

## Actions

### `create`
Creates the administrative Team record in a Competition scope.

### `updateAdministrativeRecord`
Corrects or updates Organizer-facing Team information.

Judge-facing identity is not changed by this action because Judges consume Alias rather than administrative identity.

### `withdraw`
Marks the Team as no longer participating in future Competition judging.

Withdrawal preserves all existing Encounters, Scorecards, provenance, and prior identity mappings.

### `restore`
Returns a withdrawn Team to Active status when Competition policy still allows participation.

After Finalized, ordinary restoration is not allowed.

## Queries

- `status(team)`
- `isActive(team)`
- `isWithdrawn(team)`
- `administrativeRecord(team)`
- `competitionScope(team)`

Division, Alias, Encounters, Scorecards, Rank, and Awards are queried from their respective concepts/projections rather than through Team-owned state.

## Operational Principle

An Organizer establishes a Team as the administrative representation of a competing student group. The application separately associates the Team with a Division and a competition-safe Alias. Judges evaluate the Team through that Alias in repeated Encounters without receiving its institutional identity. If the Team withdraws, future judging is prevented while historical evaluations remain intact.

## Invariants

1. A Team belongs to exactly one Competition scope.
2. A Team's stable internal identity does not change when its Alias or Division is corrected.
3. Withdrawing a Team never deletes completed Encounters or Scorecards.
4. Judges should not require direct access to the Team administrative record to perform judging.
5. Team administrative identity and judge-facing Competition Identity remain separate concerns.
6. Student user accounts are not implied by Team existence.

## Deletion versus withdrawal

Physical/administrative deletion should be limited to accidental setup records before meaningful related activity exists.

Once a Team has been used by Encounters, exports, Scorecards, Awards, or other authoritative records, the conceptual lifecycle should use `withdraw`/historical retention rather than destructive deletion.

## Withdrawal consequences

Team itself records only withdrawal state.

Application synchronization/policy later determines consequences such as:

- preventing new Encounters;
- handling already-active Encounters;
- excluding or retaining the Team in derived Coverage/Rank;
- preserving or revoking Award eligibility.

These consequences do not belong inside Team.

---

# 6. Alias specification

## Purpose

> Provide a context-safe alternate identity for a subject so users can interact with it without unnecessarily exposing its underlying administrative identity.

In MUDAC, Alias provides the Team's Judge-facing Competition Identity.

The concept is intentionally named `Alias` rather than `AnonymousTeamNumber` because its mechanism is a familiar reusable identity pattern rather than a Team-specific formatting feature.

## State

Conceptual state:

```text
Alias
    subject
    scope
    value
    status
```

For MUDAC:

```text
subject = Team
scope   = Competition
value   = competition-facing Team identifier
```

Alias status may be Active or Retired/Superseded.

Prior Alias values must remain historically resolvable when they have been used operationally.

## Actions

### `assign`
Associates a unique Alias value with a subject in a scope.

The value may be Organizer-specified or generated according to later policy. The concept does not require a particular format.

### `replace`
Retires/supersedes the current Alias and establishes a new active value for the same subject/scope.

Replacement is a correction operation once judging or printed materials have begun using the old Alias.

### `retire`
Stops an Alias from being used as the current representation while preserving its historical mapping.

### `resolve`
Returns the underlying subject represented by an Alias.

Whether a caller is authorized to resolve the mapping is governed by Access; Alias itself does not know whether the caller is a Judge or Organizer.

## Queries

- `activeAlias(subject, scope)`
- `resolve(alias, scope)`
- `isAliasActive(alias, scope)`
- `aliasesFor(subject, scope)`

Authorization around these queries is an application composition concern.

## Operational Principle

A Team is assigned a short competition identity that reveals no unnecessary institutional information. Judges interact with that Alias while scoring. Authorized Organizer behavior may resolve the Alias back to the Team administrative record. If an Alias was wrong and must be replaced, the prior value remains reserved and historically traceable rather than silently being reused for another Team.

## Invariants

1. An active Alias value is unique within its scope.
2. Before Competition Ready/Active, every non-withdrawn Team must have exactly one active judging Alias.
3. A Team has at most one active judging Alias in a Competition scope.
4. Once an Alias has been used in a Judging Encounter or authoritative printed/exported judging material, it must never be reassigned to a different Team within the same Competition.
5. Replacing an Alias does not change the Team's stable internal identity.
6. Alias does not encode authorization; Access determines whether underlying identity can be resolved.
7. Competition Alias values must not intentionally expose institution/school identity or other information the blinded judging model is intended to withhold.
8. Division is modeled separately and must not be inferred by parsing Alias format.

## Alias format policy

Phase 002-A does not mandate sequential or random identifiers.

Good examples may include:

```text
Team 014
014
Team 8F2
```

The important requirements are:

- easy for Judges to distinguish;
- easy to reproduce on paper;
- unique within the Competition;
- not institution-derived;
- sufficiently resistant to transcription confusion;
- not relied upon as a secret credential.

Alias is an identifier, not authentication.

## Alias correction after judging begins

Alias replacement after operational use is high consequence because Judges, paper forms, and prior Encounters may refer to the old value.

Therefore:

1. the old Alias is superseded, not overwritten;
2. the old Alias remains reserved to the same Team;
3. existing Judging Encounters preserve the Alias representation used when they occurred;
4. existing Scorecards remain attached to the stable Team/Encounter identity;
5. Provenance records the correction;
6. printed/exported materials may become stale and require Organizer attention under 002-H.

This also explains why Division should not be encoded semantically into the Alias: a Division correction should not normally require changing the Team identifier Judges already know.

---

# 7. Cross-concept synchronization contracts

## 7.1 Competition structural readiness

`Ready` is an explicit Competition lifecycle state, but readiness is evaluated outside Competition from multiple concepts.

002-A contributes these readiness requirements:

```text
At least one active Division exists
        +
Every non-withdrawn Team has exactly one active Division
        +
Every non-withdrawn Team has exactly one active Alias
        +
All active Aliases are unique
        +
No Team is assigned to a retired Division
        ↓
002-A structural readiness satisfied
```

Later groups add Rubric, Judge-operation, evaluation-policy, and other readiness requirements.

When configuration changes after Ready in a way that violates readiness, the application should synchronize the Competition back to Draft or otherwise require readiness to be re-established before activation. The initial preferred behavior is explicit `returnToDraft` rather than allowing a stale Ready state.

## 7.2 Team setup workflow

Organizer-facing Team setup composes three independent concepts:

```text
Team.create
    +
Division.assign
    +
Alias.assign
        ↓
Team structurally ready for Competition participation
```

These actions do not have to be performed as one concept operation. During Competition Draft, temporary incomplete setup is permitted.

The application must prevent Competition Ready/Active while an active Team remains structurally incomplete.

## 7.3 Division correction

```text
Division.correctAssignment(team)
        ↓
Provenance records correction
        ↓
derived Coverage/Rank/Award eligibility reassessed
```

The correction does **not** mutate Team identity, existing Encounters, or Scorecards.

## 7.4 Alias assignment at Team setup

```text
Team exists
    +
blinded judging policy
        ↓
Alias.assign(team, competition)
```

Alias may be generated automatically or selected by an Organizer; format is later policy.

## 7.5 Alias snapshot at Encounter start

002-C should preserve the active Team Alias presented when an Encounter begins.

Conceptually:

```text
Judging Encounter begins
        +
active Alias for Team
        ↓
Encounter records presented Competition Identity
```

A later Alias replacement must not rewrite historical Encounter context.

## 7.6 Team withdrawal

```text
Team.withdraw
        ↓
prevent future Encounter initiation
        +
reassess derived eligibility
```

Historical Encounters and Scorecards remain.

## 7.7 Event completion

```text
Competition.completeEvent
        ↓
002-B Access synchronization:
ordinary Judge private evaluation access expires
```

Competition emits the lifecycle boundary; Access owns the actual authorization change.

## 7.8 Competition finalization

```text
application finalization gates satisfied
        ↓
Competition.finalize
        ↓
stronger mutation controls across related concepts
```

The exact gates are defined across later Phase 002 groups, especially 002-F and 002-G.

---

# 8. Cross-concept invariants established by 002-A

1. Every Team is scoped to exactly one Competition.
2. During Draft, Team setup may temporarily be structurally incomplete.
3. Before a Competition becomes Ready, every non-withdrawn Team has exactly one active Division assignment.
4. Before a Competition becomes Ready, every non-withdrawn Team has exactly one active Alias.
5. An active Team can never simultaneously belong to multiple active Divisions.
6. Alias uniqueness is enforced within Competition scope.
7. Alias replacement never changes Team stable identity.
8. Division correction never changes Team stable identity.
9. Division correction does not rewrite Scorecards.
10. Team withdrawal does not delete prior judging evidence.
11. Historical Alias values used operationally are never reassigned to another Team in the same Competition.
12. Division must be carried as explicit domain state rather than inferred from Alias text.
13. Administrative Team identity is not the Judge-facing representation.
14. Competition Event Completed is a distinct boundary from Competition Finalized.
15. Finalized does not imply destructive immutability; exceptional corrections remain possible with stronger authority/provenance.

---

# 9. High-consequence mutation classification

002-A establishes three practical mutation classes for later Access/Provenance specifications.

## Ordinary preparation changes

Typically low consequence while Competition is Draft:

- edit Competition details;
- define/rename an unused Division;
- create Team;
- assign initial Division;
- assign initial Alias;
- correct administrative Team information.

## Operational corrections

Higher consequence once Competition is Active or relevant information has been used:

- change Team Division;
- replace an Alias;
- withdraw/restore Team during live operation;
- complete/resume the event.

These require clear consequences and meaningful provenance.

## Post-finalization corrections

Exceptional:

- Division correction affecting official Rank/Awards;
- Team status correction affecting official eligibility;
- identity correction affecting historical operational material;
- Competition outcome-related structural correction.

The later Access, Provenance, and Finalization specifications determine the exact authority and reconciliation requirements.

---

# 10. User experience implications without screen design

002-A does not define screens, but it establishes several presentation requirements:

- Organizers need a clear distinction between administrative Team identity and Judge-facing Alias.
- A Team's Division should be shown as explicit data rather than inferred from its ID.
- Structural readiness problems should identify exactly which Team lacks a Division or Alias.
- A Division correction after judging begins should communicate downstream impact before confirmation.
- Alias replacement after operational use should warn that existing paper/exported material may contain the old value.
- Team withdrawal should explain that historical judging records remain.
- Event completion should clearly communicate that Judge access will be closed while Organizer reconciliation continues.
- Competition finalization should communicate that results become official and later changes move into exceptional correction behavior.

---

# 11. Questions intentionally carried forward

The following questions do not block 002-A completion:

### Competition readiness
- The complete Ready gate will be assembled from all Phase 002 specifications.
- Whether `markReady` is always Organizer-confirmed or may eventually be automatically suggested remains a UX decision; the conceptual transition is explicit.

### Team administrative data
- Exact Team administrative fields remain to be determined.
- Individual student records are not required by the current product boundary and should not be introduced without operational need.

### Division policy
- Whether different Divisions may use different Rubrics or scoring policy is deferred to 002-D/002-F.
- Whether a withdrawn Team remains rank/award eligible is deferred to 002-F/002-G.

### Alias policy
- Sequential numeric versus generated/non-sequential IDs remains configurable.
- Whether Alias assignment is manual, automatic, or both remains a UX/policy decision.
- Machine-readable forms of the Alias (for example QR representations) are deferred to 002-H and must not be treated as authentication.

### Resuming an event
- `resumeEvent` is accepted as an exceptional recovery action before Finalization; exact Access restoration and authority requirements are deferred to 002-B/002-E.

---

# 12. 002-A exit assessment

The four structural concepts remain independent and require no additional concept discovery.

The strongest refinements from 002-A are:

1. **Competition lifecycle is standardized as Draft → Ready → Active → Event Completed → Finalized.** Historical is a retained presentation/status, not another business lifecycle state.
2. **Reconciliation is an activity between Event Completed and Finalized rather than a required Competition state.**
3. **Team setup may be temporarily incomplete during Draft**, which avoids forcing Team, Division, and Alias into a single concept while preserving strict readiness invariants before activation.
4. **Division owns Team-to-Division assignment**, and changes after initial setup are modeled explicitly as corrections.
5. **Team owns administrative competitor identity/status only**; it does not own Division, Alias, Encounters, Scores, Rank, or Awards.
6. **Alias values used operationally are never recycled to another Team in the same Competition**, preserving paper and historical traceability.
7. **Historical Encounters should snapshot the Alias presented at judging time**, preventing later identity correction from rewriting what Judges actually saw.
8. **Division is never inferred from Alias text**, making Division correction independent from Team Competition Identity.

002-A is therefore complete and provides the structural contracts required by 002-B — Identity, Participation & Access Specifications.

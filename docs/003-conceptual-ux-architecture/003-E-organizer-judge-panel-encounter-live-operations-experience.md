# 003-E — Organizer Judge, Panel, Encounter & Live Operations Experience

Status: **Complete**

## 1. Purpose

003-E defines the Organizer's day-of-event experience from a Competition that is Ready through active judging and the transition to Event Completed.

It translates the Phase 002 Competition, Participation, Access, Panel, Judging Encounter, Scorecard, Provenance, operational-continuity, and correction semantics—and the Judge journeys from 003-B/003-C—into an exception-first live-operations workspace without choosing a component library, real-time transport, route model, database, queueing technology, offline protocol, or AWS service.

The governing objective is:

> An Organizer should be able to understand whether Judges, Panels, Encounters, and individual evaluation obligations are operating normally, intervene quickly when live-event conditions change, and preserve fairness and historical truth without turning operational administration into direct control over Judge judgment.

The central live-operation flow is:

```text
Competition Ready
      ↓
review day-of-event operational posture
      ↓
Judge arrival / check-in
      ↓
Panel formation / composition review
      ↓
Organizer explicitly activates Competition
      ↓
live judging + exception management
      ↓
resolve or preserve outstanding operational state
      ↓
Organizer completes event
      ↓
Event Completed / reconciliation handoff
```

---

## 2. Live operations is a command workspace, not a leaderboard

During Active judging, the Organizer's primary question is not:

> Who is winning right now?

It is:

> Is the Competition operating correctly, and where is intervention needed?

The default live workspace should therefore emphasize:

```text
Judge readiness
Panel staffing / composition
active Encounter state
unfinished evaluation obligations
recusals / absences / substitutions
uncertain Finalization
paper fallback / capture state
stale or conflicting operational state
connectivity / recovery issues
```

Derived score information may be available to authorized Organizers when required for investigation, but live Rank and raw score comparison should not dominate the event-day command surface.

This reduces outcome anchoring and keeps live administration focused on process integrity.

---

## 3. Organizer live-operation information architecture

A useful conceptual organization is:

### Event status

Competition lifecycle, operational warnings, event-wide incidents, and the primary activate/complete-event actions.

### Judges

Expected, arrived, checked-in, ready, unavailable, withdrawn, needs-attention, and recovery state.

### Panels

Current membership, assigned composition capacities, composition status, location/context, and staffing exceptions.

### Encounters

Prepared/open/complete/cancelled/invalidated occurrences, Team Alias/Division context, participant state, and evaluation completion.

### Evaluations

Scorecard-obligation state and capture channel without making Judge content the default operational view.

### Exceptions

A prioritized cross-domain queue of conditions requiring Organizer attention.

These are experience regions, not new Concepts.

---

## 4. Day-of-event posture before activation

A Competition can be Ready before every expected Judge is present or every Panel is fully staffed.

The Organizer therefore needs a day-of-event operational view before activation.

For example:

```text
Competition configuration
Ready

Judges
31 expected
26 checked in
24 ready to judge
2 awaiting Panel

Panels
7 planned
5 composition-ready
2 need attention

Materials
Paper fallback forms current

Operational warnings
• Technical capacity short on Panel 06
• 5 expected Judges not checked in
```

This does not reopen Draft configuration merely because staffing is still moving.

---

## 5. Activation experience

`Competition.activate` is an explicit Organizer action.

The experience should distinguish:

```text
Configuration readiness
```

from:

```text
current live-operational posture
```

Before activation, the Organizer should see:

- whether authoritative readiness gates still pass;
- current Judge/Panel operational warnings;
- what activation will enable;
- unresolved conditions that policy makes activation-blocking.

Example:

```text
Ready to open judging

Configuration
✓ Competition remains Ready
✓ Rubric v3 authoritative
✓ Evaluation Policy v1 authoritative

Operational warnings
• Panel 06 is missing preferred Technical capacity
• 3 expected Judges have not arrived

[ Activate Competition ]
```

If a configuration change has invalidated Ready, activation is unavailable until that structural problem is resolved.

Operational warnings do not automatically block activation unless policy explicitly says they do.

---

## 6. What activation changes

Activation should be understandable as an operational authority transition.

Conceptually:

```text
Ready
  ↓ Activate
Active
```

Afterward:

- eligible Ready-to-Judge Judges may begin official Encounters;
- Scorecard obligations can become official live work;
- operational changes acquire greater consequence;
- Organizer exception handling becomes the dominant mode.

The UX should not frame activation as merely making a dashboard green.

---

# Judge live operations

## 7. Judge state model for Organizers

The Organizer needs a current-event projection of Judge state that composes 003-B rather than inventing another Judge lifecycle.

Useful operational statuses include:

```text
Expected / registered
Checked in
Awaiting profile information
Awaiting Panel
Ready to Judge
Currently judging
Has unfinished evaluation work
Needs recovery
Unavailable / withdrawn
Completed for live event
```

One Judge may satisfy several underlying facts at once; the UI may prioritize the most operationally relevant state.

For example:

```text
Jordan Lee
Panel 04
Ready to Judge
1 unfinished Draft
```

is more useful than exposing only a raw Participation status code.

---

## 8. Judge status must be source-derived

Organizers should not manually click a generic `Ready` checkbox for a Judge.

`Ready to Judge` remains derived from:

```text
Identity verification
+
current Judge Participation
+
check-in
+
required event profile
+
resolved Panel context
+
Access
+
Competition state
```

If the Judge is not ready, the Organizer should see the actual blocker.

For example:

```text
Judge J-041
Needs attention

Reason:
Panel assignment not resolved

Next action:
Assign Panel
```

---

## 9. Organizer-assisted check-in

An Organizer may need to assist a Judge who cannot complete normal self-service check-in.

The experience must still preserve:

```text
Identity
Participation
check-in
```

as separate facts.

Organizer assistance should never create a second Participation merely because the Judge changed devices or could not use a QR code.

The application should search/resolve the existing current Competition Participation first and make duplicate-identity risk visible.

---

## 10. Walk-in Judge handling

Where Competition policy permits walk-ins, live operations may establish a new Judge Participation during the event.

The Organizer flow should collect only the minimum information needed to:

```text
establish/verify Identity
create current Judge Participation
capture current expertise
check in
assign Panel
```

A walk-in who completes the required process is not a lower-class Judge in later evaluation semantics.

---

## 11. Judge no-show and withdrawal

An expected Judge who never arrives should not become a phantom Scorecard obligation.

The Organizer may record them as unavailable/withdrawn from current live operation.

This should affect:

```text
current Panel staffing
future Encounter expectations
operational readiness
```

but it does not rewrite historical Encounters in which the Judge actually participated.

---

## 12. Judge device/session trouble

Organizer operations should distinguish:

```text
Judge Participation problem
```

from:

```text
device / session problem
```

For example:

```text
Judge J-041
Participation: valid
Panel: 04
Current device session: needs recovery
```

The recommended recovery remains:

```text
reverify Judge Identity
      ↓
recover same Participation
      ↓
recover same Panel / unfinished Scorecard state
```

rather than creating another Judge or resetting their work.

---

# Panel live operations

## 13. Panel composition view

The Organizer should see both current membership and composition interpretation.

For example:

```text
Panel 04

Jordan Lee      Academic capacity
Sam Patel       Business capacity
Alex Morgan     Technical capacity

Composition
Required Judge count        ✓
Academic capacity           ✓
Business capacity           ✓
Technical capacity          ✓
```

Expertise and assigned capacity remain distinct.

A Judge with Academic + Technical expertise still satisfies whichever Panel capacity they have been deliberately assigned for the composition model.

---

## 14. Composition status is explainable

Panel status should say why it is healthy or degraded.

Conceptually:

```text
Ready
Warning / degraded
Blocking under policy
```

Examples:

```text
Panel 06 — Warning
2 Judges ready
Technical capacity missing
Organizer exception allowed
```

or:

```text
Panel 02 — Needs attention
No eligible Judges currently assigned
Cannot begin Encounter
```

The Organizer should not need to infer this from colored avatars.

---

## 15. Panel reassignment

When a Judge permanently moves between Panels:

```text
Panel 03 membership ends
      ↓
Panel 07 membership begins
```

The experience should show the consequence before confirmation.

For example:

```text
Move Jordan Lee from Panel 03 to Panel 07?

Panel 03 will lose Academic capacity.
Panel 07 will satisfy all required capacities.

Historical Encounters will not change.
```

Current membership changes never rewrite earlier Encounter participant snapshots.

---

## 16. Reassignment while judging is active

If the Judge is currently part of an Open Encounter, reassignment has higher consequence.

The Organizer must be told that changing current Panel membership does not by itself remove the Judge from the already-open occurrence.

Conceptually:

```text
Current Panel membership
        ≠
Open Encounter participant state
```

The Organizer must separately resolve any active Encounter participant adjustment.

This prevents a Panel roster edit from silently changing Scorecard obligations underneath active judging.

---

## 17. Temporary substitute versus permanent reassignment

A one-off substitute may need to participate in an Encounter without becoming a permanent member of that Panel.

The experience should support this distinction clearly:

```text
Permanent move
    changes current Panel membership

Encounter substitute
    changes only this occurrence's participant set
```

This is important during absences, recusals, or scheduling collisions.

A substitute still requires a valid eligible Judge Participation.

---

# Encounter live operations

## 18. Encounter board

The Organizer needs an operational view of current and recent Encounter state.

Useful columns/status information may include conceptually:

```text
Panel
Team Alias
Division
Encounter state
actual/effective participants
evaluation obligation progress
exceptions
capture mode
```

For example:

```text
Panel 01  Team 014  Undergraduate  Open
3 participants
2 Finalized / 1 Draft

Panel 02  Team 027  Graduate       Complete
3 / 3 Finalized

Panel 03  Team 031  Undergraduate  Open
2 participants
1 recusal
paper fallback active
```

The view should not require showing current Team Rank or Aggregate.

---

## 19. Prepared versus Open Encounters

A Prepared Encounter represents intended future judging context.

The Organizer may see:

```text
Panel 04 → Team 018
Prepared
```

Once judging begins:

```text
Open
```

and actual participant state becomes operationally meaningful.

The experience should avoid treating a Prepared Encounter as though all Judges definitely participated.

---

## 20. Participant snapshot and adjustments

Once an Encounter opens, the Organizer should be able to inspect:

```text
starting participants
participant adjustments
current effective evaluation obligations
```

For example:

```text
Starting
Jordan     participating
Sam        participating
Alex       participating

Adjustment
Alex       recused
Morgan     substitute added

Effective obligations
Jordan     required
Sam        required
Morgan     required
Alex       excused
```

Historical truth and current obligation state are both visible.

---

## 21. Recusal handling

A Judge may initiate recusal from their own experience, or an Organizer may record/confirm an operational recusal when appropriate.

The Organizer sees:

```text
Encounter E-041
Alex Morgan — Recused
No Scorecard obligation
```

not:

```text
Alex Morgan — Missing score
```

If the Judge already finalized an authoritative Scorecard, the experience must warn:

```text
A finalized evaluation already exists.
Recusal cannot silently remove it.
```

The situation then becomes an explicit correction/invalidation investigation.

---

## 22. Absence / early departure

If a Judge never meaningfully participates, their obligation can be excused according to Encounter rules.

If a Judge leaves after meaningful participation has begun, the Organizer needs enough state to distinguish:

```text
never participated
started but did not complete evaluation
finalized evaluation before departure
```

The system should not collapse all three into `Absent`.

The appropriate obligation resolution remains explicit.

---

## 23. Encounter substitute handling

Adding a substitute should make the resulting obligation obvious:

```text
Morgan Chen added as substitute
        ↓
Morgan now has one Scorecard obligation
for Encounter E-041
```

If the substitution occurs after much of the presentation has elapsed, policy may require Organizer confirmation or prohibit the change.

The UI should explain the policy rather than silently accepting an operationally dubious evaluation.

---

## 24. Duplicate Encounter prevention

If two people attempt to establish:

```text
Panel 04 × Team 014
```

at nearly the same time, Organizer operations should converge on the same logical Encounter or clearly expose a duplicate conflict.

The Organizer must never be asked to decide which apparently identical duplicate to keep without enough provenance to understand what happened.

If an actual rejudge is needed, it is created through the explicit replacement/supplemental relationship rather than an accidental duplicate.

---

## 25. Cancelled versus Invalidated

Live operations must preserve the Phase 002 distinction.

### Cancelled

Meaningful judging never occurred.

### Invalidated

Judging occurred but the Encounter should not count officially.

The UI should explain the consequence before the Organizer acts.

For example:

```text
Invalidate Encounter E-041?

3 finalized Scorecards exist.
They will remain historically preserved
but become ineligible for official aggregation.

A replacement Encounter may be required.
```

Invalidation should require stronger confirmation and reason capture than cancelling an unused Prepared Encounter.

---

# Evaluation-obligation operations

## 26. Scorecard status for Organizer operations

The live workspace consumes the Judge-side states established in 003-C.

Useful statuses are:

```text
Not started
Draft — incomplete
Draft — complete, not finalized
Finalized
Amendment Draft open
Finalized successor amendment
Recusal / obligation excused
Finalization uncertain / recovery needed
Paper fallback / capture pending
```

These are operational projections over Scorecard/Encounter state rather than a new Scorecard lifecycle.

---

## 27. Status first, content second

The default Organizer live view should show:

```text
Judge
obligation status
timing / staleness
capture channel
exception state
```

rather than immediately showing:

```text
numeric scores
Judge Notes
```

For example:

```text
Team 014 / Panel 04

Jordan      Finalized
Sam         Draft — complete
Morgan      Draft — 3/5 Criteria
```

This tells the Organizer what needs intervention without unnecessarily exposing private qualitative evidence during ordinary operations.

Authorized deeper inspection remains possible when required for a legitimate investigation.

---

## 28. Unfinished Draft intervention

003-C permits the event schedule to continue while a Judge carries an unfinished Draft.

The Organizer therefore needs visibility such as:

```text
Jordan Lee
2 unfinished Scorecards
oldest: Team 014 — 27 minutes
```

The application may highlight growing backlog or stale Drafts without assuming they are errors.

Useful Organizer actions include:

```text
ask Judge to finish
open the Judge's operational context
confirm whether paper fallback occurred
resolve lost-device/session problem
```

The Organizer should not normally finish the Judge's electronic evaluation on their behalf.

---

## 29. Draft complete but not finalized

A completed Draft that remains unfinalized deserves distinct visibility because the Judge may simply have forgotten the commitment step.

For example:

```text
Sam Patel
Team 027
All required entries complete
Not finalized
```

The Organizer can prompt the Judge to review/finalize.

The Organizer cannot silently convert the Draft into a Judge-authored Finalized Scorecard merely because the content appears complete.

---

## 30. Finalization uncertainty

A Judge may receive an uncertain response because connectivity failed around Finalization.

Organizer operations should expose this as:

```text
Finalization status uncertain
```

not as either:

```text
Draft
```

or:

```text
Finalized
```

until the authoritative state is known.

Recovery should resolve the same logical Scorecard and safe retries must not create another evaluation.

Useful Organizer guidance may be:

```text
Authoritative state not confirmed.
Ask Judge to reopen Team 014 and check status.
Do not create a second evaluation.
```

---

## 31. Amendment during Active judging

If policy allows a Judge to amend a finalized Scorecard while the Competition is still Active, the Organizer may see:

```text
Finalized v1 — authoritative
Amendment Draft — open
```

The operational Aggregate continues using v1 until the successor is finalized.

The Organizer live view should not interpret `Amendment Draft open` as a missing Scorecard.

---

## 32. Wrong-Team / structural attribution report

If a Judge reports:

```text
I scored the wrong Team
```

Organizer operations must immediately treat this as a structural integrity issue rather than offering an ordinary edit form.

The experience should show:

```text
Current Scorecard identity
Judge J-041
Encounter E-041
Team 014
Rubric v3

Reported issue
Wrong Team / Encounter association
```

and route to explicit correction/invalidation/replacement behavior.

Judge scores cannot simply be copied to another Team with history erased.

---

# Paper and degraded-mode live operations

## 33. Operational mode may vary by Panel or Judge

A network problem does not necessarily require the entire Competition to switch modes.

The live workspace may show a mixed posture:

```text
Panel 01   Electronic
Panel 02   Electronic
Panel 03   Paper fallback
Panel 04   Electronic / one Judge on paper
```

Capture channel is operational state, not evaluation weight.

---

## 34. Entering paper fallback

When digital judging becomes unreliable, the Organizer should have a clear continuity action such as:

```text
Use paper fallback for Panel 03
```

The experience should remind the Organizer of the continuity consequences:

- use the correct Rubric Version;
- maintain Team Alias/Division context;
- preserve Judge attribution;
- assign/preserve unique paper source identity;
- avoid duplicate evaluation when an electronic Draft already exists;
- reconcile later.

This is not a new scoring mode.

---

## 35. Existing Draft plus paper fallback

If a Judge already has an electronic Draft for the Encounter, the Organizer should be warned before paper fallback produces another capture source.

Conceptually:

```text
Judge J-041
Team 014
Electronic Draft exists

Paper fallback source PF-00231
```

The recovery model must converge these onto the same logical Judge × Encounter evaluation rather than count both.

The live workspace should expose the potential duplicate-risk state until reconciliation resolves it.

---

## 36. Paper collection state

During the event, Organizers need a simple operational distinction such as:

```text
Paper form issued
Paper form returned
Capture pending
Captured
Verified against source
```

These are operational/capture projections, not new Scorecard authority states.

A returned paper form can prevent the Organizer from thinking the evaluation is simply missing even before transcription is complete.

Detailed capture workflow remains 003-G.

---

## 37. Connectivity incidents

The Organizer should be able to distinguish:

```text
isolated Judge device issue
Panel-local connectivity issue
event-wide service degradation
```

The application need not automatically diagnose network infrastructure perfectly.

It should, however, make repeated uncertain save/finalize or access failures visible enough that the Organizer can recognize a broader operational pattern.

This is an observability requirement for the UX, not a choice of monitoring technology.

---

# Exception-first command model

## 38. Live exception queue

Rather than requiring continuous manual inspection, the Organizer should receive a prioritized set of operational exceptions.

Examples:

```text
High
• Panel 02 has zero eligible Judges
• Encounter E-041 has Finalization uncertainty
• Judge J-017 reported wrong Team

Needs attention
• 3 Drafts older than 20 minutes
• Panel 06 missing preferred Technical capacity
• 2 paper forms returned, capture pending

Informational
• 4 expected Judges have not checked in
```

The exact prioritization vocabulary is refined later in 003-I, but urgency must reflect consequence rather than arbitrary color.

---

## 39. Exceptions drill to source evidence

Every operational alert should answer:

```text
What is wrong?
What source state proves it?
What is the consequence?
What can the Organizer legitimately do?
```

For example:

```text
Panel 06 composition warning

Required:
Academic 1
Business 1
Technical 1

Current:
Academic ✓
Business ✓
Technical ✗

Consequence:
New Encounters may proceed only under configured exception policy.

Actions:
Add/reassign eligible Judge
Accept allowed exception
```

This maintains explainability during time pressure.

---

## 40. Operational acknowledgements do not erase conditions

If an Organizer acknowledges a warning, the underlying fact remains.

For example:

```text
Technical capacity missing
Organizer acknowledged
```

is not:

```text
Technical capacity satisfied
```

Similarly, an accepted composition exception remains an exception in history and later Coverage/reconciliation.

---

# Organizer authority boundaries

## 41. Organizer can coordinate Judge judgment, not author it

The Organizer may legitimately:

```text
identify missing work
prompt a Judge
open amendment access under policy
record recusal/absence where authorized
manage Panel/Encounter state
capture paper-authored evaluation
investigate structural mistakes
invalidate evidence under governed rules
```

The Organizer does not ordinarily:

```text
change a Judge's electronic score
write a Judge's Note
Finalize an electronic Scorecard as though the Judge did it
```

Operational urgency cannot silently transfer semantic authorship.

---

## 42. Sensitive evaluation content

Organizer Access may permit reading Scorecards and Notes, but ordinary live operations should avoid casual exposure.

A deeper investigation path may deliberately reveal:

```text
Criterion scores
Judge Note content
Version history
Provenance
```

when necessary.

The experience should make this an intentional investigation transition rather than placing private Judge Notes in the main room-status grid.

---

## 43. Live score analytics

Organizer analytics may show distributions, unusual values, or other diagnostic information where authorized.

However:

- statistical outlier status does not invalidate a Scorecard;
- the system must not normalize or modify scores automatically;
- live Team Rank should not become the primary event-operations navigation;
- any score-based investigation must drill back to authoritative evidence and policy.

Detailed reconciliation/outcome review belongs to 003-F.

---

# Completing the event

## 44. Event completion is not Finalization

At the end of live judging, the Organizer transitions:

```text
Active
   ↓ completeEvent
Event Completed
```

This means live judging is over.

It does **not** mean:

```text
all paper capture finished
all Scorecards corrected
Coverage satisfied
Rank official
Awards decided
Competition Finalized
```

Those belong to reconciliation.

---

## 45. Pre-completion operational review

Before `completeEvent`, the Organizer should see unresolved live-operation facts such as:

```text
3 Encounters still Open
4 Judges have unfinished Drafts
1 Finalization uncertain
7 paper forms returned, capture pending
2 Panels still marked active
```

The Organizer may need to resolve some of these before completing the event, while others can legitimately flow into Event Completed reconciliation.

The UX should classify which conditions:

```text
must be resolved before live close
```

versus:

```text
will carry into reconciliation
```

according to domain rules and policy.

---

## 46. Open Encounter handling at event close

An Encounter representing live judging that is genuinely still occurring should normally block event completion or require deliberate resolution.

The Organizer may need to:

```text
allow it to finish
complete/cancel the occurrence appropriately
record interruption/exception
```

The system should not silently close every Open Encounter merely because the Competition is being completed.

---

## 47. Unfinished Scorecards may carry into reconciliation

Because presentation end and Scorecard Finalization are separate, the Organizer may intentionally complete the event with unresolved evaluation work under policy.

For example:

```text
2 Judges left with Drafts
```

may become Event Completed reconciliation issues requiring:

```text
post-event amendment/access workflow
paper-source capture
obligation resolution
Coverage exception
```

The presence of unfinished work must remain visible; event completion does not convert it into zero or silently discard it.

---

## 48. Event completion confirmation

The high-consequence transition should explain its immediate effect:

```text
Complete live judging?

This will:
• end ordinary live judging
• end ordinary Judge access to private evaluation history
• move unresolved capture/evaluation issues into reconciliation

It will NOT:
• finalize Competition results
• publish winners
• delete unfinished evidence
```

This makes the lifecycle boundary understandable to the Organizer.

---

## 49. Immediate post-completion handoff

After successful event completion, the Organizer should land in a reconciliation-oriented posture rather than the same live dashboard with disabled buttons.

Conceptually:

```text
Live Operations
      ↓ Event Completed
Reconciliation
```

The first view should summarize what carried forward:

```text
Judging ended

Needs reconciliation
• 7 paper forms awaiting capture
• 2 unfinished Judge evaluations
• 1 invalidated Encounter awaiting replacement decision
• 3 Teams currently Coverage-incomplete
```

Detailed reconciliation belongs to 003-F.

---

# Current versus historical truth

## 50. Live operations must preserve occurrence history

A current operational correction cannot rewrite what earlier Teams encountered.

Examples:

```text
Panel 04 now
Jordan, Sam, Morgan

Encounter E-031 earlier
Jordan, Sam, Alex
```

or:

```text
Team current Alias
Team 027

Encounter E-014 presented Alias
Team 014
```

The Organizer should be able to understand both without one masquerading as the other.

---

## 51. Timeline/history for consequential operations

For important live changes, an Organizer may need a compact operational history such as:

```text
09:05 Panel 04 formed
09:42 Alex recused from Encounter E-031
09:44 Morgan added as substitute
10:18 Jordan moved to Panel 06
```

This is a human-facing projection of authoritative/provenance state, not an exhaustive telemetry log.

It helps explain how current state arose under event-day pressure.

---

# Privacy and disclosure

## 52. Team identity shielding remains active

Organizers may have authority to resolve Team administrative identity, but Judge-facing screens, shared Panel displays, and operational materials must continue using Judge-safe Team representation unless a deliberate Organizer-only investigation requires otherwise.

A shared live-operations display visible to Judges should therefore not accidentally reveal:

```text
institution
student/admin information
Team Name when hidden
current Rank
other Judges' Scorecards
```

Organizer authority does not make every physical display Organizer-private.

---

## 53. Shared-room Organizer displays

If the Organizer uses a projector or shared monitor for event coordination, the experience needs a safe-display posture.

A shared display may show:

```text
Panel labels
rooms
Team Aliases
operational status
```

while suppressing:

```text
private Team identity mappings
Judge Notes
individual scores
Rankings
sensitive incident details
```

The exact presentation mechanism remains future visual design.

---

# 003-E invariants

003-E adds or reinforces these experience invariants:

1. Live operations are exception-first rather than leaderboard-first.
2. Competition activation is explicit and only occurs while authoritative readiness remains valid.
3. Operational warnings and configuration blockers remain distinct.
4. Judge readiness is derived, not manually asserted.
5. Device/session failure does not create a new Judge Participation.
6. Panel composition status is explainable from membership/capacity state.
7. Current Panel reassignment never rewrites historical Encounter participation.
8. Panel reassignment does not silently alter an already-open Encounter.
9. Permanent Panel movement and one-off Encounter substitution remain distinct.
10. Encounter participant adjustments preserve starting history and effective obligations.
11. Recusal is not a missing score and never becomes zero.
12. A finalized Scorecard cannot be silently removed through recusal or roster editing.
13. Encounter duplication is prevented; legitimate rejudging is explicit.
14. Cancellation and invalidation remain visibly distinct.
15. Organizer operational views prioritize Scorecard status over score content.
16. A complete Draft is not equivalent to a Finalized Scorecard.
17. Organizer prompting cannot substitute for Judge Finalization/authorship.
18. Finalization uncertainty remains explicitly uncertain until authoritative state is known.
19. Amendment Drafts do not make prior finalized Scorecards missing.
20. Structural Scorecard errors route to correction/invalidation rather than ordinary editing.
21. Mixed electronic/paper operation preserves identical evaluation semantics.
22. Existing electronic Draft plus paper fallback is treated as duplicate-risk, not two votes.
23. Paper collection/capture state is distinguishable from missing evaluation.
24. Operational warning acknowledgement never changes the underlying fact.
25. Accepted exceptions remain historically visible.
26. Organizer administration does not transfer Judge semantic authorship.
27. Private Judge Notes are not default live-dashboard content.
28. Live scoring analytics never automatically modify evidence.
29. Event Completed is distinct from Competition Finalized.
30. Event completion does not fabricate resolution of unfinished evaluation work.
31. Genuinely Open live Encounters require explicit close/interruption handling.
32. Event completion explains Judge-access cutoff and reconciliation handoff.
33. Current operational state and historical occurrence state remain separately legible.
34. Shared Organizer displays enforce their own disclosure posture.

---

# 54. Pressure tests

## Judge does not arrive

Expected Judge J-041 never checks in.

Correct experience:

```text
Expected / not arrived
      ↓
Organizer records unavailable if appropriate
      ↓
Panel composition updates
      ↓
future Encounter expectations adjust
```

No phantom zero Scorecards are created.

---

## Judge changes Panels after two Teams

Correct experience:

```text
prior Encounters retain old participant context
current Panel membership ends
new Panel membership begins
future Encounters use new Panel context
```

No historical rewriting.

---

## Judge recuses during a presentation

Correct experience:

```text
starting participant retained historically
recusal recorded
obligation excused if no authoritative Scorecard exists
substitute may be added under policy
```

No zero and no unexplained missing evaluation.

---

## Judge finished form but forgot Finalize

Correct experience:

```text
Draft — complete, not finalized
      ↓
Organizer prompts Judge
      ↓
Judge reviews / Finalizes
```

Organizer cannot silently click Finalize as the Judge.

---

## Network fails during Finalize

Correct experience:

```text
Finalization uncertain
      ↓
Organizer/Judge recover authoritative state
      ↓
safe retry same logical Scorecard
```

No duplicate vote.

---

## Entire Panel switches to paper

Correct experience:

```text
Panel marked paper fallback
correct Rubric Version used
paper sources tracked
existing electronic Drafts flagged for reconciliation
paper returned/capture state tracked
```

Evaluation weight is unchanged.

---

## Organizer sees an extreme score

Correct experience:

```text
may inspect/investigate if authorized
outlier alone remains valid
no automatic deletion/normalization
```

Operational dashboard does not silently alter the outcome.

---

## Event ends with unfinished work

Correct experience:

```text
Organizer sees outstanding state
      ↓
resolves live Encounters as required
      ↓
completeEvent
      ↓
unresolved permitted items carry into reconciliation
```

Nothing is silently set to zero or discarded.

---

# 55. Explicit deferrals

003-E does not decide:

- WebSocket/SSE/polling or other real-time transport;
- dashboard visual layout;
- notification/toast technology;
- drag-and-drop Panel UI;
- map/floor-plan tooling;
- exact incident-priority scoring;
- database concurrency strategy;
- device/session implementation;
- offline synchronization implementation;
- observability vendor/technology;
- AWS services;
- detailed paper transcription UI;
- Ranking/Award reconciliation presentation.

Those choices must implement the specified operational behavior rather than redefine it.

---

# 56. 003-E exit position

The experience architecture now covers the Organizer transition from preparation into real live operation:

```text
Competition Ready
      ↓
Judge arrival + readiness
      ↓
Panel formation
      ↓
Activate
      ↓
┌──────────────────────────────────────┐
│ Judge operations                     │
│ Panel operations                     │
│ Encounter operations                 │
│ Evaluation obligation tracking       │
│ Recusal / substitution               │
│ Paper / degraded-mode continuity     │
│ Exception-first intervention         │
└──────────────────────────────────────┘
      ↓
Complete Event
      ↓
Event Completed
      ↓
Reconciliation
```

The central UX principle is:

> **The Organizer runs the integrity of the judging process, not the Judges' judgments.**

The next subgroup, **003-F — Reconciliation, Coverage, Ranking, Awards & Finalization Experience**, can now begin from a precise handoff: live judging has ended, ordinary Judge access has closed, and every unresolved evaluation/capture/coverage/policy/outcome issue is available for explicit Organizer reconciliation before any result becomes official.

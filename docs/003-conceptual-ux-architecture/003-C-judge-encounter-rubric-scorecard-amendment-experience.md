# 003-C — Judge Encounter, Rubric, Scorecard & Amendment Experience

Status: **Complete**

## 1. Purpose

003-C defines the Judge's primary live-event experience after onboarding has produced a trustworthy **Ready to Judge** state.

It translates the Phase 002 Judging Encounter, Rubric, Scorecard, Versioning, Provenance, Access, and operational-continuity semantics into a phone-first judging workflow without choosing a front-end framework, route model, component system, persistence mechanism, synchronization protocol, or AWS service.

The governing objective is:

> A Judge should be able to confirm the correct Team and judging context, listen to the presentation, record criterion-level judgment and Notes with minimal distraction, safely preserve incomplete work, deliberately finalize one independent Scorecard, and continue to the next Team without exposure to peer scoring or Competition standings.

The central experience loop is:

```text
Ready to Judge
      ↓
resolve / confirm current Encounter
      ↓
confirm Team Alias + Division
      ↓
Scorecard Draft
      ↓
score + Notes while presentation occurs
      ↓
presentation ends
      ↓
finish / review own evaluation
      ↓
explicit Finalize
      ↓
authoritative Scorecard Version
      ↓
return to Panel judging context
```

Amendment is a separate controlled mode after Finalization; it is not ordinary continued editing of the authoritative Scorecard.

---

## 2. Judge work context

The Judge experience should always make the current evaluation context legible before and during scoring.

The minimal context stack is:

```text
Competition
   ↓
Judge mode
   ↓
Panel
   ↓
Judging Encounter
   ↓
Team Alias + Division
   ↓
my Scorecard
```

The Judge should not need to infer which Team is active from browser history, physical seating, a previous page title, or the last score they entered.

For consequential evaluation actions, Team context should remain visually persistent enough that the Judge can re-orient after interruption.

At minimum the active judging experience should keep readily available:

```text
Team Alias
Division
Panel / Encounter context where useful
my Scorecard state
save / synchronization confidence
```

The optional student-created `teamName` remains hidden by default during blinded judging under the 002-A1 disclosure baseline.

---

## 3. Entering a Judging Encounter

A Judge may arrive at a Team evaluation through several operational patterns:

```text
Organizer-prepared Encounter / assignment
Panel already opened an Encounter
Judge selects the Team Alias being presented
Judge scans a Team/Encounter QR or code
Organizer directs the Panel to a Team
```

These are different ways of resolving the same domain context.

The Judge should not be exposed to the implementation question of who technically created the Encounter record.

The experience contract is:

```text
requested Team / Encounter context
        ↓
current Panel + Competition validation
        ↓
existing matching Encounter if one exists
        ↓
or establish one logical Encounter safely
        ↓
confirm Judge is an effective participant
        ↓
open / resume one logical Scorecard
```

If multiple Judges on the same Panel choose the same Team nearly simultaneously, their experiences must converge on the same logical Judging Encounter rather than creating parallel Panel–Team occurrences.

---

## 4. Team selection and wrong-Team prevention

Wrong-Team scoring is one of the highest-consequence ordinary mistakes in the Judge workflow.

The design should therefore use **context confirmation rather than repetitive confirmation**.

A reasonable conceptual sequence is:

```text
Select / scan Team 014
        ↓
show:
    Team 014
    Undergraduate
    Panel 07
        ↓
Begin judging Team 014
```

Once confirmed, that context remains obvious while the Judge scores.

The Judge should not need to confirm the Team before every Criterion; excessive confirmation would create fatigue and encourage blind clicking.

A Team/Encounter QR may accelerate context selection, but scanning it does not itself grant evaluation authority and cannot bypass the Judge's current Panel/Participation/Access checks.

---

## 5. Team Name disclosure

`teamName` is optional descriptive Team metadata, not the blinded Competition identity.

The baseline Judge display is:

```text
Team 014
Undergraduate
```

not:

```text
Bayes Brigade
```

because a student-created Team name could accidentally reveal institution, individuals, or other identifying information.

If a future Competition explicitly authorizes Judge-visible Team Names, the display should remain structurally clear:

```text
Team 014
"Bayes Brigade"
Undergraduate
```

with Alias remaining the canonical Encounter identity.

Team Name must never replace Alias in paper/digital traceability or structural correction workflows.

---

## 6. Encounter already in progress

When a Panel has already started judging a Team, another effective Judge participant should enter the existing Encounter and see a clear current context rather than a second "start" experience.

Conceptually:

```text
Panel 07 is judging Team 014

Your Scorecard:
Not started
```

or:

```text
Your Scorecard:
Draft — 3 of 5 Criteria scored
```

The Judge should be able to resume directly.

---

## 7. Encounter participant mismatch

If the Judge attempts to enter an Encounter for which they are not an effective participant, the system should explain the mismatch rather than simply showing a generic authorization failure.

For example:

```text
Panel 07 is judging Team 014,
but you are currently assigned to Panel 04.

Ask an Organizer if your Panel assignment changed.
```

or:

```text
You are no longer an active participant in this Encounter
because a recusal was recorded.
```

This supports recovery without exposing unrelated evaluation data.

---

## 8. Recusal / conflict action

A Judge needs an obvious way to stop before creating an official evaluation when they recognize a conflict or otherwise should not judge the Team.

Conceptually:

```text
I need to recuse / cannot judge this Team
```

should be available near Encounter entry/current context rather than buried in account settings.

The action should:

1. identify the current Encounter clearly;
2. require deliberate confirmation because it changes an evaluation obligation;
3. capture an appropriate reason/category according to Competition policy;
4. remove the Judge from ordinary scoring for that Encounter once the recusal/participant adjustment is effective;
5. surface the change to Organizer live operations.

A recusal is never represented as a zero Scorecard.

If the Judge already has an authoritative finalized Scorecard, a simple recusal action cannot silently remove it from Competition evidence. That situation requires Organizer-governed correction/invalidation under the Phase 002 authority model.

---

## 9. Scorecard starts as Draft

When the Judge begins evaluation work, the application resolves the one logical Scorecard for:

```text
Judge Participation × Judging Encounter
```

and presents it in Draft state.

The Judge should not need to understand Scorecard identity or create a new artifact manually.

The experience should feel like:

```text
Judge Team 014
```

not:

```text
Create Scorecard
```

because the Scorecard is the consequence of the Judge's evaluation obligation, not a generic document-management task.

---

## 10. Rubric is embedded in the evaluation task

The Rubric should be experienced as the structure of judgment, not as a separate reference document the Judge must repeatedly leave the Scorecard to inspect.

For each Criterion, the Judge needs access to:

```text
Criterion title
what is being evaluated
valid score choices
score guidance / anchors
Criterion Note
```

Detailed instructions may be progressively disclosed when needed so guidance is available without overwhelming the phone screen.

The exact UI presentation—cards, sections, accordions, paged steps, or another pattern—remains a later visual/component decision.

The information architecture requirement is that score entry and the guidance explaining that score remain closely connected.

---

## 11. Phone-first scoring posture

During the presentation, the application should stay secondary to listening and observation.

The Judge should not be required to:

- navigate wide tables;
- type numeric values manually when a bounded choice exists;
- repeatedly open modal dialogs;
- traverse deep navigation between Criteria;
- scroll sideways;
- use hover;
- perform precision pointer actions.

Scoring controls should directly represent the Criterion's valid bounded score domain.

For example, a 1–5 Criterion should expose the valid 1–5 choices rather than an unrestricted number field that must later reject `7`.

Specific visual controls are deferred to later design.

---

## 12. Criterion completion state

The Judge should be able to understand progress without confusing progress with authority.

For example:

```text
3 of 5 Criteria scored
```

means only that three required scoring responses currently exist in the Draft.

It does **not** mean:

```text
60% finalized
```

or that any portion is already official.

The full Scorecard remains non-authoritative until explicit Finalization.

---

## 13. Criterion Notes

Criterion Notes should remain adjacent in meaning to the Criterion they explain.

A Judge should be able to score quickly and optionally/necessarily add a Note without navigating to a separate notes subsystem.

Conceptually:

```text
Statistical Methodology
Score: 4
Note: Strong validation; assumptions could be clearer.
```

If the Rubric requires a Criterion Note, the Draft may continue temporarily without one, but Finalization validation must identify the missing Note clearly.

Notes remain private Judge evaluation evidence and never appear to peer Judges through this experience.

---

## 14. Overall Note

The Judge also needs one clearly distinguished overall Note area for observations applying to the evaluation as a whole.

The experience should not blur:

```text
Criterion-specific Note
```

with:

```text
Overall Note
```

because their meaning and later review context differ.

If the overall Note is required by the Rubric, Finalization validation should enforce it.

---

## 15. Draft preservation should feel automatic

The Judge should not have to remember to press a Save button after every score or Note.

The experience target is:

> Meaningful Draft work is preserved automatically as the Judge works.

However, the interface must distinguish user intent from persistence certainty.

Conceptually useful persistence states include:

```text
Saving…
Saved
Changes not yet confirmed
Connection lost — Draft preserved only to the degree truthfully known
```

The exact offline/local persistence technology remains for later architecture.

The UX must never display `Saved` merely because a local interaction occurred if authoritative persistence has not actually been confirmed under the chosen architecture.

Detailed degraded-mode interaction patterns remain for 003-H/003-I.

---

## 16. Leaving and resuming a Draft

A browser refresh, accidental close, phone lock, navigation away, or device change should not ordinarily destroy acknowledged Draft work.

When the Judge returns to the same Encounter:

```text
Team 014
Your Scorecard: Draft
3 of 5 Criteria scored

Resume evaluation
```

is preferable to creating a new Scorecard.

A device change similarly resolves the same logical Scorecard after Identity/Participation re-establishment.

---

## 17. Presentation end versus Scorecard completion

The Team may finish presenting before the Judge finishes scoring or writing Notes.

Therefore:

```text
Presentation ended
        ≠
my Scorecard finalized
```

The Judge should be able to continue completing their own Draft after the presentation while the Encounter remains unresolved as necessary.

This distinction should be legible to both Judge and Organizer experiences.

---

## 18. Moving to the next Team with unfinished work

The preferred path is to finish and Finalize before beginning the next Team.

However, live event operation must not be hard-blocked by one Judge needing additional time.

If the Panel needs to proceed while the Judge still has an unfinished Draft, the application may allow a deliberate transition such as:

```text
Team 014 Scorecard is not finalized.

Finish now
or
Keep as Draft and continue
```

Choosing to continue:

- preserves the Draft;
- keeps it visible as unfinished work;
- does not fabricate completion;
- does not prevent the Panel's next Encounter from proceeding;
- gives the Judge an obvious way to return later.

The action should not be presented as casual dismissal because incomplete Scorecards affect Encounter completion and potentially Coverage.

---

## 19. Multiple unfinished Drafts

The experience should tolerate more than one unfinished Draft if live circumstances require it, but it should make the debt obvious.

For example:

```text
My judging

Current:
Team 027 — Draft

Needs completion:
Team 014 — 4/5 Criteria
Team 021 — Notes required
```

The system should not encourage a workflow in which Judges routinely accumulate many incomplete evaluations.

A Competition/Organizer may later choose stronger operational policy, but the baseline UX avoids both data loss and event-gridlock.

---

## 20. My judging history during the event

While ordinary Judge Access remains active, the Judge should have a compact operational history of their own work.

Useful information includes:

```text
Team Alias
Division
Scorecard state
Draft completion summary
Finalized time
Amendment state if any
```

This is not an analytics dashboard and should not contain:

```text
peer Judge scores
Panel means
Team Aggregate
Coverage
Rank
Competition standings
```

Its purpose is to help the Judge answer:

> What have I judged, and what do I still need to finish?

At Event Completed, this private history becomes unavailable under the existing lifecycle privacy rule.

---

## 21. Judge's own calculated Scorecard value

The Judge may see the deterministic value calculated from their own Criterion responses because it is part of their own evaluation and follows directly from the Rubric.

The experience should distinguish it clearly from any Team/Panel aggregate.

For example:

```text
Your calculated Scorecard value: 87.5
```

may be useful during final review.

It need not dominate the live scoring interface while the presentation is occurring, because criterion-level judgment should remain primary.

The Judge must never infer that this value is the Team's Competition score.

---

## 22. Review before Finalization

Finalization should be preceded by a compact review that answers:

```text
Am I evaluating the correct Team?
Did I answer every required Criterion?
Are required Notes present?
What scores did I enter?
What is my calculated Scorecard value?
Am I ready for this evaluation to become official?
```

The review should foreground missing requirements and unusual omissions without making the Judge hunt through the entire form.

Example conceptual summary:

```text
Team 014 — Undergraduate

Methodology       4
Analysis          5
Communication     3
Innovation        4
Presentation      4

Overall Note      ✓

Your calculated value: 82.5

Finalize evaluation
```

The visual form is deferred; the information requirement is not.

---

## 23. Finalization is explicit

`Finalize` means:

> I am committing this evaluation as my authoritative Competition judgment.

It must therefore be distinct from automatic Draft preservation.

The Judge should not be able to finalize accidentally through routine navigation or simply because the presentation ended.

Finalization should require one clear deliberate action after validation/review.

Repeated confirmation dialogs are unnecessary if the final review itself makes the consequence clear.

---

## 24. Finalization validation

If required information is missing, Finalization fails without losing work.

Prefer:

```text
Your Scorecard is still a Draft.

Complete these items before Finalizing:
• Analysis — score required
• Presentation — Note required
```

rather than a generic error or silent navigation to the first missing field.

The Judge should be able to move directly to each unresolved item.

---

## 25. Finalization success

Once authoritative Finalization is confirmed, the experience should make the transition unambiguous:

```text
Team 014
Evaluation finalized
```

and then offer a clear return to Panel work / next judging context.

The success state should not expose peer results or Team Aggregate as a reward for submitting.

The Judge's task is complete without needing to know how others scored.

---

## 26. Uncertain Finalization response

A network failure at Finalization is a high-risk ambiguity.

The application must not guess.

Possible truthful experience:

```text
We could not confirm whether Finalization completed.
Your evaluation has not been duplicated.

Check status / Try again
```

The eventual recovery must resolve the existing logical Scorecard and determine whether an authoritative Version already exists.

Retry must be safe and cannot create another Judge vote.

The UI must never show `Finalized` until authoritative success is known.

---

## 27. Finalized Scorecard during Active judging

While ordinary Judge Access remains active, the Judge may inspect their own finalized Scorecard through `My judging` or the relevant Encounter.

The experience should clearly indicate:

```text
Finalized
```

rather than making the fields look like an editable Draft.

If Competition policy allows self-service amendment during Active judging, the Judge is offered a separate action:

```text
Amend evaluation
```

not direct editing of the displayed finalized values.

---

## 28. Amendment is a separate mode

Beginning an amendment should make the authority boundary explicit:

```text
Current authoritative evaluation:
Finalized v1

You are creating an amendment.
Your existing finalized evaluation continues to count
until the amendment is finalized.
```

The experience then provides an editable Amendment Draft initialized from the current authoritative Version.

This prevents the dangerous impression that simply opening the form again has made the official Scorecard provisional.

---

## 29. Amendment editing

Within Amendment Draft, the Judge may change the fields that 002-D permits:

```text
Criterion scores
Criterion Notes
Overall Note
```

Structural identity remains fixed:

```text
Judge
Team / Encounter
Rubric Version
```

If the Judge discovers that the Scorecard belongs to the wrong Team, Encounter, Judge, or Rubric basis, the experience should direct them to report the structural problem rather than trying to fix it through ordinary amendment.

---

## 30. Amendment review

Before finalizing an amendment, the experience should make meaningful changes understandable.

A conceptual comparison may identify:

```text
Methodology
4 → 5

Overall Note
changed
```

The exact diff presentation is deferred, but the Judge should not have to rely on memory to understand what they are replacing.

If Competition policy requires a reason, it should be collected in this workflow.

During ordinary Active judging, a free-text reason may remain optional according to Phase 002 policy.

---

## 31. Abandoning an Amendment Draft

The Judge may abandon an Amendment Draft without affecting the current authoritative Version.

The experience should communicate:

```text
Discard amendment Draft?
Your finalized evaluation will remain unchanged.
```

This action is different from deleting the Scorecard.

---

## 32. Finalizing an amendment

When amendment Finalization succeeds:

```text
Finalized v1
      ↓
Finalized v2
```

v2 becomes the current authoritative Scorecard Version and v1 remains historical.

The Judge still has one logical Scorecard and one unit of evaluation weight.

The experience should not phrase this as "submitted another score."

A better human-facing status is:

```text
Evaluation updated
```

with history available where authorized.

---

## 33. Post-event amendment experience

At Event Completed, ordinary Judge access to private Scorecards and judging history expires.

The Judge therefore cannot simply return to `My judging` and amend an old Scorecard.

A legitimate post-event workflow is:

```text
Organizer authorizes specific correction
        ↓
Judge opens narrow correction entry
        ↓
Identity reverified
        ↓
only authorized Scorecard disclosed
        ↓
Amendment Draft
        ↓
required reason
        ↓
Finalize amendment
        ↓
temporary Access expires
```

This experience should look intentionally narrower than normal event Judge mode so the Judge understands that they are correcting a specific historical evaluation rather than re-entering the Competition.

---

## 34. Wrong-Team / structural error after Finalization

If the Judge realizes:

```text
I scored Team 014,
but this Scorecard is attached to Team 041
```

that is not an amendment to judgment.

The experience should provide an obvious `Report a problem` / Organizer-help path and avoid suggesting that the Judge fix the Team identifier while retaining the same Scorecard structure.

Structural correction/invalidation belongs to Organizer-governed workflows specified in Phase 002 and later Organizer UX phases.

---

## 35. No peer anchoring before or after Finalization

Throughout Draft, review, Finalization, and ordinary amendment, the Judge must not see:

```text
other Judge Criterion scores
other Judge totals
other Judge Notes
Panel mean
Team Aggregate
Division Rank
Competition standings
```

This remains true even after the Judge commits their own evaluation during the live event.

Finalizing one's own Scorecard is not a trigger to reveal peer judgment.

The Judge may know who their fellow Panel members are, but not how they scored.

---

## 36. Rubric Version transparency

A Judge does not need a technical version identifier dominating every Criterion, but the exact Rubric basis must be inspectable.

Conceptually the Judge can confirm:

```text
Rubric: 2026 Competition Rubric
Version: 3
```

or an equivalent human-readable representation.

If the Organizer has introduced a later Rubric Version during Active judging, the Judge's current Scorecard should never silently switch beneath them.

If mixed-version operation requires attention, the Organizer experience owns the reconciliation warning; the Judge should continue to see the exact instrument governing their Scorecard.

---

## 37. Rubric guidance should remain stable during one Scorecard

Once a Scorecard is bound to a Rubric Version, the Judge should not experience changing Criterion text, score anchors, weights, or instructions because another Rubric Version was published elsewhere.

This is an experience-level reflection of the Phase 002 exact-version invariant.

---

## 38. Score changes should not require punitive friction

Draft judgment naturally evolves while the Judge listens.

Changing:

```text
3 → 4
```

within Draft should be immediate and ordinary.

The system should not ask:

```text
Are you sure?
```

for every score change.

Higher friction belongs at semantic commitment boundaries such as Finalization, recusal, or abandoning an Amendment Draft—not ordinary thought formation.

---

## 39. Note editing should support interruption

A Judge may be typing a Note when:

- the presentation advances;
- another Judge asks a question;
- the phone locks;
- connectivity changes;
- the Judge switches Criteria.

The UX should not require explicit submission of each Note before leaving its field.

Draft preservation applies to Notes and scores consistently.

---

## 40. Error recovery preserves context

Errors should preserve the Judge's evaluation context whenever safe.

Prefer:

```text
We couldn't save your latest changes yet.
You're still judging Team 014.
Your confirmed Draft through 10:42 AM is safe.
```

rather than redirecting to generic event home or clearing the form.

The exact timestamp/synchronization language depends on the later persistence architecture, but the principle is that failure messages identify:

```text
what is known
what may be unsaved
which Team/Scorecard is affected
what the Judge should do next
```

---

## 41. Switching Competition or role with a Draft open

If a dual-role person attempts to switch from Judge mode or change Competition while meaningful Draft work is open, the application must not silently discard or hide that work.

Depending on confirmed persistence state, the experience should:

- safely preserve and allow the context switch;
- or warn that some work is not yet confirmed and provide a recovery choice.

The Judge should be able to return to the same Draft later while Access/lifecycle permits.

This extends the 003-A context-switching rule into the actual evaluation workflow.

---

## 42. Shared-device handoff with Scorecard work

A Judge using a shared/loaner device must have a safe way to finish or leave a Draft before ending their session.

The next Judge must never inherit the prior Judge's:

```text
Scorecard
Notes
Team history
current Team context
```

If the prior Judge's Draft is authoritatively preserved, device handoff can clear local exposure while the Draft remains recoverable through that Judge's Identity/Participation later.

If preservation is uncertain, the UI must say so before handoff rather than silently discarding possible work.

---

## 43. Accessibility requirements applied to scoring

The core judging flow must work without dependence on:

```text
hover
color alone
fine motor precision
camera
wide-screen layout
perfect vision
rapid scrolling
```

Conceptual requirements include:

- large/forgiving score targets;
- keyboard-operable scoring and navigation;
- clear selected/unselected score state beyond color;
- semantic labels for Criterion controls;
- logical screen-reader reading order;
- text-resize support without hiding scoring context;
- clear focus behavior when validation identifies missing content;
- accessible Notes entry;
- non-camera Team/Encounter selection alternative.

Detailed cross-journey accessibility architecture remains for 003-H.

---

## 44. Paper fallback from an electronic Draft

If electronic judging becomes impractical while a Judge has a Draft, the Judge may need to finish on paper.

The experience/operations must preserve the one-logical-Scorecard invariant.

Conceptually:

```text
electronic Draft exists
        ↓
Organizer/Judge switches capture path to paper
        ↓
paper source uniquely identified
        ↓
physical evaluation completed
        ↓
Organizer capture/reconciliation
        ↓
same Judge × Encounter logical evaluation
```

The electronic Draft must not later become a second authoritative evaluation merely because connectivity returns.

How the implementation reconciles field-level Draft differences is deferred, but the system must surface the mixed-capture situation explicitly rather than guessing.

---

## 45. Judge completion state after Finalization

After a successful Finalization, the Judge's operational history should show something like:

```text
Team 014
Finalized
```

If an Amendment Draft exists:

```text
Team 014
Finalized — amendment in progress
```

The prior authoritative Scorecard remains the official one until the amendment is finalized.

This status language prevents the Judge from thinking their evaluation has disappeared from Competition results during amendment.

---

## 46. Organizer-facing consequences established by 003-C

Detailed Organizer live operations belong to 003-E, but the Judge experience creates observable states that must be available operationally.

At minimum, Organizer projections need to distinguish:

```text
Scorecard not started
Draft / incomplete
Draft complete but not finalized
Finalized
Amendment Draft open
Finalized successor amendment
recusal / obligation excused
finalization status uncertain / recovery needed
paper fallback / capture pending
```

These states should be observable without requiring Organizer access to impersonate the Judge experience.

---

## 47. Privacy and secondary leakage

The Scorecard experience should avoid leaking private judging information through incidental surfaces where practical.

Examples include:

```text
browser/page title
lock-screen notification
recent-page label
shared-device history
file download name
```

A page title such as:

```text
Team 014 — Score 42 — Judge Jane Smith
```

would be unnecessarily revealing.

The cross-cutting disclosure rules will be consolidated in 003-I, but 003-C establishes that Judge-private evaluation content is sensitive beyond the visible main screen.

---

## 48. Experience state model

The Judge-facing evaluation states can be summarized as:

```text
Encounter available
      ↓
Scorecard not started
      ↓
Draft
  ├── incomplete
  └── complete-for-finalization
      ↓
Review
      ↓
Finalization pending / confirmation
      ↓
Finalized
      │
      └── optional Amendment Draft
             ├── abandon → Finalized unchanged
             └── finalize → Finalized successor Version
```

Operational side paths include:

```text
recusal
participant removal
paper fallback
uncertain persistence
structural-error report
post-event narrow correction
```

These are not all domain states; they are the experience interpretation of the underlying Concept and synchronization model.

---

## 49. Canonical Judge evaluation journey

The complete preferred live path is:

```text
Ready to Judge
      ↓
Panel is evaluating Team 014
      ↓
confirm Team 014 / Division
      ↓
open or resume my Draft
      ↓
Criterion 1..N
  score + Note as needed
      ↓
Overall Note
      ↓
presentation ends
      ↓
finish missing evaluation work
      ↓
review own Scorecard
      ↓
Finalize
      ↓
authoritative Version confirmed
      ↓
return to Panel work
      ↓
next Team
```

If unfinished work must be deferred:

```text
Draft preserved
      ↓
explicit unfinished status
      ↓
Panel proceeds
      ↓
Judge returns and finalizes later
```

If correction is needed:

```text
Finalized Scorecard
      ↓
explicit Amend action
      ↓
Amendment Draft
      ↓
review changes
      ↓
finalize successor Version
```

---

## 50. UX invariants established by 003-C

1. Team/Encounter context is confirmed before meaningful scoring and remains clear during evaluation.
2. Alias remains the canonical Judge-facing Team identity; Team Name is hidden by default during blinded judging.
3. Team/Encounter QR or code never grants evaluation authority by itself.
4. Concurrent same-Panel/same-Team entry converges on one logical Encounter.
5. One Judge Participation × Encounter exposes one logical Scorecard.
6. Rubric guidance and score entry remain closely connected.
7. Judges can select only valid Criterion score values through the ordinary UI.
8. Criterion Notes remain semantically attached to their Criteria.
9. Overall Note remains distinct from Criterion Notes.
10. Draft work is non-authoritative and may remain incomplete.
11. Draft preservation should feel automatic but persistence status must remain truthful.
12. Presentation completion never implies Scorecard Finalization.
13. An unfinished Scorecard does not hard-block the Panel's next live presentation.
14. Deferring an unfinished Scorecard is deliberate and keeps the Draft visibly outstanding.
15. My judging history exposes only the Judge's own operational work, not peer/Team aggregates or standings.
16. A Judge may inspect their own calculated Scorecard value without exposure to aggregate Competition scoring.
17. Finalization is explicit and cannot occur as a side effect of navigation/presentation end.
18. Finalization validation preserves the Draft and identifies missing requirements specifically.
19. Finalization success is shown only after authoritative confirmation.
20. Retried Finalization cannot create duplicate Scorecards or votes.
21. Finalized Scorecards are visually/read-only distinct from Drafts.
22. Amendment is a separate mode; opening an Amendment Draft does not displace the current authoritative Version.
23. Amendment cannot change structural Scorecard identity.
24. Abandoning an Amendment Draft leaves the authoritative Scorecard unchanged.
25. Finalizing an amendment creates a successor Version of the same logical Scorecard, not an extra vote.
26. Wrong-Team/wrong-Encounter/wrong-Rubric structural errors are escalated rather than edited as ordinary amendments.
27. Peer scores, Notes, Panel aggregates, Team Aggregate, Coverage, and Rank remain unavailable to Judges throughout live judging.
28. A Scorecard remains bound to one exact Rubric Version in the experience.
29. Ordinary Draft score/Note changes do not receive punitive confirmation friction.
30. Context switching or shared-device handoff never silently destroys meaningful Draft work.
31. Paper fallback must converge with an existing electronic Draft onto one logical evaluation.
32. Event Completed removes ordinary Judge history/amendment access; later correction uses the narrow authorized path.
33. Error states explain what is known, what is uncertain, which evaluation is affected, and the next recovery action.
34. The Judge experience remains phone-first and accessible without relying on hover, camera, fine motor control, or color alone.

---

## 51. Pressure-test scenarios

### Judge accidentally closes browser mid-presentation

Expected:

```text
return
  ↓
Identity/Participation context recovered
  ↓
Team 014 Draft recovered
  ↓
continue from confirmed work
```

No new Scorecard is created.

### Judge starts selecting the wrong Team

The Team confirmation step exposes Alias/Division before scoring begins. The Judge can cancel without creating meaningful evaluation history.

### Judge notices conflict after opening Draft but before Finalization

The Judge initiates recusal. No zero is created. The evaluation obligation is explicitly adjusted according to policy; the Draft never becomes official evidence.

### Presentation finishes but Judge needs two more minutes

Judge continues Draft completion. Panel may proceed operationally if necessary. If the Judge moves on, the unfinished Draft remains prominently outstanding.

### Judge loses network while typing Notes

The experience does not falsely say `Saved`. It states the known persistence condition and keeps Team/Scorecard context clear. Recovery converges on the same Draft.

### Finalize request times out

The interface does not assume failure or success. Retry/check resolves the same logical Scorecard and cannot create another authoritative vote.

### Judge changes score after Finalization

The displayed Finalized Scorecard is not directly editable. Judge explicitly enters Amendment mode, producing an Amendment Draft while prior Version remains authoritative.

### Judge discovers Scorecard is attached to wrong Team

The experience directs them to report the structural problem; it does not permit changing Team identity inside Amendment Draft.

### Event is completed while Judge has an unfinished Draft

Ordinary Judge access expires according to the lifecycle boundary. The unfinished obligation becomes an Organizer reconciliation issue. Any later Judge work requires explicitly authorized temporary correction Access rather than silently reopening live Judge history.

### Panel switches to paper after an electronic Draft exists

The switch is surfaced explicitly. Paper receives unique source identity; later capture reconciles to the same Judge × Encounter evaluation rather than creating a second Scorecard.

---

## 52. Explicit non-decisions

003-C intentionally does not choose:

- single-page versus stepped Scorecard UI;
- card/accordion/tab component patterns;
- sticky-header implementation;
- exact score-control visual widgets;
- autosave debounce timing;
- local/offline storage technology;
- client/server synchronization algorithm;
- optimistic-locking mechanism;
- HTTP/API design;
- front-end framework;
- browser/PWA/native packaging;
- accessibility library;
- notification mechanism;
- database schema;
- AWS service topology.

Those choices must satisfy the experience contracts above rather than redefining them.

---

## 53. Exit assessment

003-C completes the core Judge evaluation experience without introducing new domain Concepts or contradicting the Phase 002 behavioral model.

The principal UX result is:

> **The Judge's evaluation is one continuous, safely preserved thought-forming workflow until explicit Finalization; after Finalization, correction becomes a visibly separate amendment workflow.**

The second important result is operational:

> **Live-event continuity is prioritized without weakening evidence integrity: unfinished Judge work may be deferred, network uncertainty is represented truthfully, paper fallback is permitted, and every path still converges on one logical Judge × Encounter Scorecard.**

The Judge experience is now sufficiently defined for later visual/component architecture.

The next Phase 003 group is **003-D — Organizer Competition Setup, Configuration & Readiness Experience**, which can translate the already-specified Competition, Division, Team/attributes, Alias, Rubric, Evaluation Policy, Awards, Judge preparation, and readiness rules into an Organizer preparation workflow.
# 003-F — Reconciliation, Coverage, Ranking, Awards & Finalization Experience

Status: **Complete**

## 1. Purpose

003-F defines the Organizer's post-live-event experience from `Event Completed` through reconciled evidence, ranking-ready Divisions, resolved Awards, explicit Competition Finalization, and subsequent exceptional correction of an official outcome.

It translates the Phase 002 Versioning, Provenance, Evidence Eligibility, Coverage, Aggregate, Ranking, Award, Finalization, and Official Outcome semantics—and the operational handoff from 003-E—into an exception-first closeout experience without choosing a component library, reporting engine, route structure, query architecture, database, workflow framework, or AWS service.

The governing objective is:

> An Organizer should be able to determine whether the Competition's evidence is complete and trustworthy, understand exactly why any Team or Division is not outcome-ready, resolve legitimate exceptions without inventing evidence, review derived Rankings without directly editing them, confer Awards according to their declared semantics, and deliberately establish an official outcome whose complete basis remains reconstructible.

The central closeout flow is:

```text
Event Completed
      ↓
reconcile authoritative evidence
      ↓
resolve Coverage / eligibility
      ↓
review Division Ranking readiness
      ↓
resolve declared tie requirements
      ↓
confirm / confer Awards
      ↓
Finalization readiness review
      ↓
Organizer Finalize
      ↓
Official Outcome Revision
```

Publication/export remains a later and separate experience specified in 003-G.

---

## 2. Reconciliation is an Organizer work mode, not another Competition state

Phase 002 intentionally kept the Competition lifecycle:

```text
Draft → Ready → Active → Event Completed → Finalized
```

Therefore the UX should not invent a persisted Competition state named:

```text
Reconciling
```

Instead, once the event is completed, the Organizer experience foregrounds **Reconciliation** as the current work mode.

Conceptually:

```text
Competition state:
Event Completed

Organizer mode:
Reconciliation
```

This distinction matters because the Competition remains Event Completed throughout paper capture, Scorecard amendments, Coverage resolution, ranking review, and Award work until the Organizer explicitly finalizes it.

---

## 3. Reconciliation is exception-first

The default post-event question is not:

> What are the rankings?

It is:

> What evidence or policy issue still prevents us from trusting the rankings?

The default reconciliation workspace should therefore lead with unresolved state such as:

```text
Evidence
• 3 paper Scorecards awaiting verification
• 1 Judge amendment requested
• 1 Scorecard Finalization state unresolved

Encounters
• 1 invalidated Encounter needs replacement decision

Coverage
• 2 Teams below normal Coverage threshold

Rubric compatibility
• 1 Team has evidence across incompatible scoring semantics

Division / eligibility
• 1 Team Division correction affects ranking population

Ties
• Undergraduate Rank 1 tie requires declared resolver

Awards
• 2 required Awards unresolved
```

A provisional Ranking may be inspectable, but it should not displace these closeout conditions as the primary information architecture.

---

## 4. Reconciliation work regions

A useful conceptual organization is:

### Evidence

Scorecards, paper capture/verification, amendments, uncertain finalization, invalidation, replacement, and authoritative-version state.

### Coverage & eligibility

Team evaluation sufficiency, accepted exceptions, withdrawal, Division assignment, Rubric compatibility, and official eligibility.

### Rankings

Division-scoped derived ordering, readiness state, tie status, and explainability.

### Awards

Rank-derived candidates, discretionary Award work, recipient cardinality, conferral state, and required/optional status.

### Finalization

Cross-domain closeout readiness, authoritative policy basis, unresolved blockers, final confirmation, and Official Outcome Revision history.

These are experience regions, not new Concepts.

---

## 5. Reconciliation issue is a projection, not a new Concept

The application will likely need to present actionable closeout items, but 003-F does not introduce a generic `ReconciliationIssue` domain Concept.

A reconciliation item is a projection from source state, for example:

```text
Scorecard S-117
    Finalization uncertain
        ↓
Reconciliation item:
    Resolve Scorecard authority state
```

or:

```text
Team 014
    Coverage 10 / 12
        ↓
Reconciliation item:
    Coverage below normal threshold
```

Resolving the item means changing or explicitly accepting the underlying domain state through the legitimate action.

It does not mean clicking `Resolved` on an unrelated task object while the source problem remains.

---

## 6. Reconciliation status should preserve source semantics

The experience should not collapse materially different conditions into one generic `Incomplete` label.

Examples include:

```text
Paper capture pending
Paper verification pending
Judge amendment requested
Amendment Draft open
Finalization uncertain
Encounter invalidated
Replacement Encounter unresolved
Coverage incomplete
Coverage exception accepted
Rubric incompatible
Division correction pending
Tie unresolved
Required Award unresolved
```

The cross-cutting wording can be consolidated in 003-I, but these semantic differences must remain visible.

---

## 7. Evidence-first closeout

The first reconciliation objective is to establish what evaluation evidence is actually authoritative and eligible.

The Organizer should be able to understand the path from expected judging to usable evidence:

```text
Judging Encounter
      ↓
effective evaluation obligations
      ↓
logical Scorecards
      ↓
current authoritative Versions
      ↓
valid / invalidated evidence state
      ↓
eligible evaluation evidence
```

The experience should expose discrepancies before they are hidden inside Team Aggregates.

For example:

```text
Encounter E-041 — Team 014

Expected evaluation obligations: 3

Judge J-011   Finalized
Judge J-017   Finalized
Judge J-024   Paper capture pending

Encounter status:
Evaluation obligations not yet reconciled
```

---

## 8. Finalization uncertainty recovery

An unresolved electronic Finalization from live operations must be resolved before the application treats that evaluation as either missing or finalized.

The Organizer should see something like:

```text
Judge J-024 — Team 014
Finalization state uncertain

Last confirmed Draft: available
Authoritative Finalized Version: not confirmed

Resolve current server state
Contact Judge / recovery path if required
```

The UI must not offer:

```text
Count as finalized
```

as an Organizer convenience action.

Recovery determines the actual Scorecard authority state.

---

## 9. Judge amendment coordination after Event Completed

Post-event Judge corrections use the narrow authority path established in Phase 002.

Organizer experience:

```text
identify / receive correction need
        ↓
select exact Scorecard
        ↓
record required correction purpose
        ↓
authorize narrow temporary amendment Access
        ↓
Judge reverifies and amends
        ↓
new Scorecard Version
        ↓
Access expires
        ↓
dependent Coverage / Aggregate / Rank refresh
```

The Organizer should be able to see the correction's operational status without gaining the ability to author the Judge's revised judgment themselves.

Useful states include:

```text
Correction requested
Awaiting Judge
Amendment Draft open
Amendment finalized
Authorization expired
```

---

## 10. Organizer electronic-score correction boundary remains visible

If an Organizer believes an electronic Judge Scorecard is wrong, the experience should offer legitimate paths such as:

```text
Request Judge amendment
Investigate structural attribution
Invalidate under authorized policy
Leave evaluation unchanged
```

It should not offer a normal inline edit control over the Judge's finalized score.

Operational authority remains separate from evaluation authorship after the event just as it was during live judging.

---

## 11. Paper evidence handoff

Detailed paper capture mechanics are specified in 003-G, but 003-F establishes the reconciliation semantics that paper workflow must satisfy.

Paper-origin evidence may appear in states such as:

```text
Source collected
Capture pending
Captured / verification pending
Verified / authoritative
Transcription correction pending
```

Only evidence that has reached the policy-required verified authoritative state contributes as eligible paper-origin evaluation.

Reconciliation should therefore clearly distinguish:

```text
paper exists physically
```

from:

```text
paper evaluation is now authoritative digital evidence
```

---

## 12. Duplicate electronic/paper convergence

If a Judge began electronically and later used paper for the same Encounter, reconciliation must detect that both artifacts refer to one logical evaluation obligation.

Conceptually:

```text
Judge J-041 × Encounter E-022
       ├── electronic Draft
       └── paper source PF-184
                ↓
          reconciliation
                ↓
       one authoritative Scorecard
```

The Organizer should never solve this by accepting both because two artifacts exist.

The experience must guide the Organizer to the legitimate source/convergence workflow and preserve the non-authoritative or superseded artifact historically as appropriate.

---

## 13. Encounter invalidation and replacement

An invalidated Encounter stays visible in reconciliation.

For example:

```text
Encounter E-031
Team 027
Panel 04
Invalidated
Reason: wrong Team was presented

Replacement:
E-048 — Complete
```

or:

```text
Replacement:
Not established
```

The Organizer should be able to determine whether:

- replacement judging occurred;
- the replacement is valid;
- the original Scorecards are excluded from official evaluation;
- Coverage consequences remain.

Invalidation cannot silently delete the historical Encounter.

---

## 14. Evidence eligibility explanation

For any Scorecard excluded from official calculation, the Organizer should be able to see **why**.

Examples:

```text
Excluded — Encounter invalidated
Excluded — superseded historical Scorecard Version
Excluded — incompatible Rubric basis
Excluded — Team withdrawn under current policy
```

Where a relationship is indirect, the experience should still make the causal chain inspectable.

The principle is:

> No evidence should mysteriously disappear from an Aggregate.

---

# Coverage & eligibility experience

## 15. Coverage is a first-class closeout dimension

Coverage should not be buried beside the Team Aggregate as a small secondary number.

The Organizer needs to understand separately:

```text
How well did the Team score?
```

and:

```text
Did the Team receive enough qualifying evaluation to be ranked normally?
```

A Team reconciliation summary might therefore show:

```text
Team 014 — Undergraduate

Aggregate
87.4367

Coverage
Encounters: 4 / 4
Scorecards: 11 / 12
Status: Incomplete

Ranking eligibility
Not currently eligible
```

The valid Aggregate is not hidden, but it is not allowed to imply adequate Coverage.

---

## 16. Coverage drill-down

The Organizer should be able to move from Team Coverage to the source obligations that produced it.

Conceptually:

```text
Team Coverage
      ↓
Encounter Coverage
      ↓
effective Judge obligations
      ↓
eligible / missing / excused Scorecards
```

For example:

```text
Team 014
11 / 12 eligible Scorecards

Encounter E-021   3 / 3
Encounter E-033   3 / 3
Encounter E-044   2 / 3
    J-041 — Finalized
    J-052 — Finalized
    J-067 — missing / unresolved
Encounter E-052   3 / 3
```

This makes the shortage operationally explainable.

---

## 17. Coverage exception workflow

If Competition policy permits Organizer-governed Coverage exceptions, acceptance must be explicit.

Conceptually:

```text
Coverage requirement
12 eligible Scorecards

Actual
11 eligible Scorecards

Reason for shortfall
1 Judge became ill after presentation
No replacement evaluation was possible

[ Accept Coverage exception ]
```

Acceptance creates:

```text
Coverage status:
Exception Accepted

Actual evidence:
11 / 12
```

It does **not** create a twelfth Scorecard or rewrite the display to `12 / 12`.

---

## 18. Coverage exception consequence should be obvious

Before acceptance, the experience should explain the consequence:

```text
If accepted, Team 014 may become rank-eligible
with 11 qualifying Scorecards instead of the normal 12.

The shortfall will remain part of the Competition record.
```

The action should require the appropriate Organizer authority and human-readable reason where policy requires it.

This is materially different from acknowledging an informational warning.

---

## 19. Coverage exceptions should not be casual bulk overrides

The application may eventually support batch workflows where several Teams share a clearly identical event-wide cause, but the default should not encourage:

```text
Select all incomplete Teams
→ Mark exceptions accepted
```

without showing the actual evidence shortfall and consequences.

Coverage exception is a fairness decision, not clerical cleanup.

Any batch workflow must preserve Team-level resulting Coverage facts and attributable authority.

---

## 20. Composition exceptions remain separate from Scorecard Coverage

An Encounter may have complete evaluation obligations while operating under degraded Panel composition.

For example:

```text
Encounter E-041
2 expected effective Judges
2 finalized Scorecards

Encounter completeness:
Complete

Composition:
Exception Accepted — no Business capacity
```

The reconciliation experience must preserve both facts.

Depending on Evaluation Policy, the composition exception may or may not affect Team ranking eligibility.

It is not represented as a missing Scorecard.

---

## 21. Withdrawal and rank eligibility

A withdrawn Team retains all historical evidence but is excluded from official Ranking by baseline policy.

Organizer view should say:

```text
Team 031
Withdrawn

Evaluation history retained
Official Rank eligibility: Excluded
```

rather than deleting the Team or suppressing its evaluation history.

If policy permits a different consequence, that policy must be explicit.

---

## 22. Division correction during reconciliation

A Team's current corrected Division controls the official ranking population while Encounter history preserves what Judges saw.

The UX should make the distinction explicit:

```text
Team 014

Current Division:
Graduate

Encounter E-021 presented as:
Undergraduate

Division corrected after judging
Reason: registration classification error
```

The correction must show its downstream effect:

```text
Undergraduate Ranking affected
Graduate Ranking affected
Award eligibility may be affected
```

It cannot silently move the Team between lists with no explanation.

---

## 23. Rubric compatibility reconciliation

If evidence exists across multiple Rubric Versions, the Organizer should see whether they are aggregation-compatible.

For example:

```text
Team 014

Rubric v3
9 Scorecards
Compatible

Rubric v4
3 Scorecards
Scoring-semantic change
Incompatible by default
```

The UX should not offer a casual:

```text
Normalize and continue
```

button.

Legitimate resolution may involve:

- establishing that the revision was editorial and compatible;
- replacement judging where appropriate;
- excluding invalid evidence through governed policy;
- another explicitly supported reconciliation path.

The resolution and authority must remain attributable.

---

# Ranking experience

## 24. Ranking is continuously derivable but not continuously official

The system may calculate Division Rankings whenever authoritative eligible evidence changes.

That does not make them official.

The UX must distinguish at least:

```text
Calculated / provisional Ranking
Ranking-ready Division
Official Ranking in an Official Outcome Revision
```

A Division can have a visible calculated ordering while still carrying:

```text
Not ranking ready
```

because unresolved evidence or policy issues remain.

---

## 25. Ranking readiness is derived

The Organizer does not manually click:

```text
Mark Division Ranking Ready
```

as a substitute for source resolution.

Ranking readiness is derived from conditions such as:

```text
all relevant Teams resolved
Coverage resolved
Rubric compatibility resolved
Division assignments valid
material corrections settled
required tie policy applied
no unresolved outcome-affecting issue
```

The workspace may present this checklist-like, but the truth comes from underlying state.

---

## 26. Division status example

A useful reconciliation view might show:

```text
Undergraduate
Ranking status: Needs attention

✓ 18 Teams rank-eligible
✓ Coverage resolved
✓ Rubric compatibility resolved
✕ Rank 1 tie requires declared resolver

Graduate
Ranking status: Ready

✓ 12 Teams rank-eligible
✓ Coverage resolved
✓ No unresolved ties
```

The Organizer can inspect calculated rankings in either Division, but only Graduate is currently closeout-ready.

---

## 27. Ranking display keeps source condition visible

A Ranking list should not reduce each Team to:

```text
1. Team 014 — 87.44
```

without enough context to identify exceptions.

A conceptual Organizer view may show:

```text
Rank   Team      Aggregate   Coverage        Status
1      014       87.4367     12 / 12         Eligible
2      027       87.1121     11 / 12         Exception Accepted
3      008       85.9022     12 / 12         Eligible
```

The exact table/card presentation is deferred, but accepted exceptions should remain discoverable rather than disappearing once the Team becomes rank-eligible.

---

## 28. Team Name in Organizer Ranking views

Organizer-facing ranking/reconciliation views may include optional descriptive Team Name for human convenience, for example:

```text
Team 014 — Bayes Brigade
```

because Organizer disclosure permits it.

However:

- Alias remains the stable competition-facing identifier;
- Team Name remains non-competitive;
- duplicate Team Names remain valid;
- public disclosure of Team Name remains a separate 003-G concern.

No ranking formula may use Team Name.

---

## 29. Ranking explainability

Every displayed Rank should support drill-down through its derivation.

Conceptually:

```text
Rank 1 — Team 014
        ↓
Aggregate 87.4367
        ↓
12 eligible authoritative Scorecards
        ↓
Scorecard values
        ↓
Criterion responses
        ↓
Rubric Version / scoring semantics
```

Alongside that numerical path, the Organizer should also be able to inspect:

```text
Coverage
accepted exceptions
Encounter validity
Scorecard Version history
Provenance
Evaluation Policy Version
```

This is the UX realization of Phase 001's rule that no official result should be a number the system cannot explain.

---

## 30. Ranking cannot be edited

There is no ordinary:

```text
Edit Rank
```

or:

```text
Move Team up
```

control.

If the calculated ordering is wrong, the Organizer must correct the cause:

```text
Scorecard
Encounter eligibility
Coverage exception
Division assignment
Rubric compatibility
Evaluation Policy
Tie resolution
```

and allow Ranking to recompute.

---

## 31. Outlier diagnostics remain diagnostic

Organizer reconciliation may expose analytical aids such as:

```text
unusually high / low Judge score
high variance within Encounter
Criterion disagreement
```

These may help identify mistakes worth investigating.

They do not automatically exclude evidence or change Rank.

A diagnostic can lead to:

```text
Judge correction
structural investigation
invalidation under policy
no action
```

but never directly to hidden score normalization/removal.

---

## 32. Precision remains explicit

The Organizer should be able to understand both display and comparison semantics.

For example:

```text
Team 014
Displayed Aggregate: 87.44
Authoritative comparison value: 87.436666...
```

The UI may normally suppress excessive decimals, but where a close Rank or tie question exists, it must make the declared comparison policy inspectable.

Display rounding never silently becomes tie policy.

---

# Tie experience

## 33. Tie state is explicit

A declared tie is not an error in the ranking engine.

For example:

```text
Rank 1
Team 014
Team 027

Status:
Shared Rank under current policy
```

If shared Rank is allowed, no forced resolution is necessary merely because two Teams occupy first place.

---

## 34. Required tie resolution follows predeclared policy

If an exactly-one-recipient Award or Competition rule requires the tie to be resolved, the experience should present only the declared resolver.

For example:

```text
Rank 1 tie

Declared tie resolver:
Methodology Criterion Aggregate

Team 014: 4.62
Team 027: 4.71

Resolved Rank 1 candidate:
Team 027
```

The Organizer should not be invited to choose a new tiebreaker after seeing the results.

---

## 35. Additional judging as tie resolution

If Competition policy declares additional judging as the resolver, the post-event workflow may require a new legitimate Judging Encounter rather than a manual Rank edit.

The experience should make this operational consequence explicit:

```text
Tie requires additional judging
        ↓
new Encounter authorized / prepared
        ↓
new authoritative evidence
        ↓
Coverage / Aggregate / Rank recomputed
```

Whether this requires temporarily resuming live Competition operation or an exceptional post-event mechanism must follow the Competition lifecycle/policy rather than being invented by the Ranking screen.

---

# Award experience

## 36. Awards come after sufficiently reconciled result state

Award work should be available during reconciliation, but rank-derived Award confirmation should not be presented as settled while its underlying Division Ranking is not ready.

For example:

```text
Undergraduate Champion

Candidate:
Pending — Undergraduate Ranking not ready
```

rather than prematurely naming the current provisional Rank 1 Team as though the Award were ready for ceremony.

---

## 37. Rank-derived Award experience

Once its Ranking basis is ready:

```text
Undergraduate Champion
Selection: Rank 1

Derived candidate:
Team 014 — Bayes Brigade
Rank: 1
Aggregate: 87.4367
Coverage: 12 / 12

[ Confirm Award ]
```

Organizer confirmation means:

> I am conferring the Award according to its declared rank-derived rule.

It does not mean:

> I may choose a different Team while keeping the same rule label.

---

## 38. Rank-derived Award mismatch cannot be overridden casually

If the Organizer attempts to confer a rank-derived Award on a Team that is not its derived candidate, the application should not accept a generic override.

The Organizer must instead address the semantic cause:

```text
Ranking wrong → correct source
Award definition wrong → correct Award definition under governance
Tie unresolved → resolve declared tie requirement
```

Changing the recipient without changing the rule would make the record misleading.

---

## 39. Discretionary Award experience

A discretionary Award should look and feel different from a rank-derived Award.

For example:

```text
Most Innovative
Selection: Discretionary
Scope: Competition-wide
Recipients: one

Eligible Teams: 30

Organizer deliberation / selection required
```

The experience may support authorized review of relevant evidence such as Criterion scores, Scorecards, or Judge Notes when Competition policy permits.

But it must not present a hidden algorithmic `recommended winner` derived from private Notes and then describe the final choice as purely discretionary.

---

## 40. Sensitive evidence in Award deliberation

Judge Notes remain private evidence even during Organizer Award work.

If Notes are exposed for legitimate discretionary deliberation, the experience should make the sensitivity clear and avoid turning broad Note access into the default Award browsing mode.

A discretionary Award may also rely on non-Scorecard Organizer observations when policy allows; those should remain identifiable as human deliberation rather than mathematical Ranking evidence.

---

## 41. Award recipient cardinality

The UX must reflect Award cardinality.

Examples:

### One or more

```text
Rank 1 tie
Team 014
Team 027

Award allows multiple recipients
[ Confirm both ]
```

### Exactly one

```text
Rank 1 tie unresolved
Award requires exactly one recipient

Award cannot be confirmed yet
```

The system never silently chooses one tied Team based on incidental ordering.

---

## 42. Required versus optional Awards

Closeout should make required/optional status explicit.

For example:

```text
Required Awards
✓ Undergraduate Champion
✓ Graduate Champion
✕ Competition Champion — unresolved

Optional Awards
✓ Most Innovative
— Best Visualization — intentionally not conferred
```

An optional Award should have an explicit `not conferred` outcome where needed so the Organizer can distinguish deliberate omission from forgotten work.

---

## 43. Award change after source correction

If a Scorecard or other source change alters a Ranking after a rank-derived Award was already confirmed but before Finalization:

```text
Ranking changed
      ↓
existing Award confirmation becomes stale / affected
      ↓
new candidate derived
      ↓
Organizer must reconfirm
```

The Award must not silently jump to the new Team.

This same affected-state pattern becomes even more important after Finalization.

---

# Finalization experience

## 44. Finalization readiness is derived

Like Competition Ready and Ranking Ready, Finalization readiness is a projection from source state.

The Organizer does not make a Competition finalization-ready by checking boxes.

Derived gates include at least:

```text
Competition is Event Completed
structural Team/Division/Alias integrity resolved
Encounter validity/replacement resolved
Scorecard authority state reconciled
paper evidence reconciled
Rubric compatibility resolved
Coverage resolved
all relevant Divisions ranking ready
required tie requirements resolved
Evaluation Policy authoritative
required Awards resolved
rank-derived Awards consistent with current Ranking
no material outcome-affecting correction remains unresolved
```

Only then can the explicit Finalize action become available.

---

## 45. Finalization workspace

A useful conceptual final review is:

```text
FINALIZATION

Evidence
✓ 164 authoritative eligible Scorecards
✓ Paper capture / verification complete
✓ No unresolved Scorecard corrections

Coverage
✓ 30 Teams resolved
  • 28 Satisfied
  • 2 Exception Accepted

Rankings
✓ Undergraduate ready
✓ Graduate ready

Awards
✓ 4 required Awards resolved
✓ 2 optional Awards resolved / intentionally not conferred

Policy
✓ Evaluation Policy v3

No unresolved outcome-affecting issues

[ Finalize Competition ]
```

Accepted exceptions remain visible rather than being erased by the green status.

---

## 46. Finalization review surfaces the authoritative policy basis

Before Finalization, the Organizer should be able to see which Evaluation Policy will govern the declared outcome.

For example:

```text
Evaluation Policy v3

Aggregation:
Equal Judge Scorecard weight

Coverage:
4 Encounters / 12 Scorecards

Ranking:
Division-scoped

Tie comparison:
Full authoritative precision
```

This prevents Finalization from becoming detached from the rules that produced the Rankings.

---

## 47. Finalization confirmation uses proportional friction

Finalization is one of the highest-consequence Organizer actions.

It warrants a deliberate confirmation that communicates meaning.

For example:

```text
Finalize MinneMUDAC 2026?

This will:
• establish the current Rankings and Award conferrals as official
• create an Official Outcome Revision
• close ordinary outcome-changing workflows

This will NOT:
• publish results publicly
• delete historical evidence
• make legitimate future correction impossible
```

The exact interaction pattern remains a later visual-design choice.

---

## 48. Finalization must fail atomically in domain meaning

If source state changes or a blocker appears during the finalization attempt, the application must not create a partially official outcome.

The Organizer should receive a specific explanation such as:

```text
Competition was not finalized.

A Scorecard amendment was finalized during your review,
which changed Undergraduate Ranking.

Review the affected Ranking and Award before trying again.
```

The eventual transaction/concurrency implementation is deferred, but the domain UX contract is all-or-nothing.

---

## 49. Successful Finalization

On success, the experience should clearly establish:

```text
Competition
Finalized

Official Outcome Revision 1
Current

Finalized by:
Organizer Participation

Finalized at:
<timestamp>
```

The Organizer should be able to inspect the official revision and its source basis.

The UI should **not** immediately imply:

```text
Published
```

because external disclosure remains separate.

---

## 50. Official Outcome inspection

An Official Outcome Revision should be presented as a reconstructible snapshot/projection containing or referencing:

```text
Evaluation Policy Version
resolved Coverage and exceptions
Division Rankings
Award definitions / conferrals
source authority/version references
finalizing authority
time
```

The Organizer can drill from an official Rank/Award back into the source evidence that supported that revision.

This makes official status inspectable rather than ceremonial metadata.

---

## 51. Finalized is not public

Immediately after Finalization, the Organizer may legitimately see:

```text
Official Outcome Revision 1
Status: Official internally
Publication: Not published
```

This supports ceremony preparation, controlled release timing, and review of external materials without reopening judging.

003-G owns the publication/export experience.

---

# Post-finalization correction experience

## 52. Finalized Competition can still expose a correction path

Ordinary editing is closed after Finalization.

If a legitimate error is discovered, the Organizer enters an **Exceptional Correction** workflow rather than reopening normal reconciliation as though Finalization never occurred.

Conceptually:

```text
Official Outcome Revision 1
      ↓
verified correction need
      ↓
exceptional source correction workflow
      ↓
latest derived calculations change
      ↓
Official Outcome Revision 1 becomes affected
      ↓
Organizer reconciles corrected result
      ↓
confirm successor Official Outcome Revision 2
```

The Competition lifecycle may remain `Finalized` throughout.

---

## 53. Latest calculated result versus current official outcome

This distinction must be highly visible during exceptional correction.

For example:

```text
Current official outcome
Revision 1
Undergraduate Champion: Team 014

Corrected latest calculation
Rank 1: Team 027

Status
Official Outcome Revision 1 is affected and requires review
```

The application must not silently present Team 027 as the new official Champion before successor confirmation.

---

## 54. Affected official outcome state

When a post-finalization source correction changes something material, the current Official Outcome should become visibly affected.

Examples:

```text
Ranking affected
Award candidate affected
Coverage exception no longer applicable
Division population affected
```

The Organizer should be able to inspect the exact dependency chain:

```text
Paper transcription correction
      ↓
Scorecard v2
      ↓
Team Aggregate changed
      ↓
Division Rank changed
      ↓
Undergraduate Champion affected
```

This makes historical correction understandable rather than magical.

---

## 55. Successor official revision confirmation

After corrected evidence is reconciled, the Organizer explicitly establishes the successor outcome.

For example:

```text
Corrected outcome ready

Revision 1
Historical — superseded by correction

Proposed Revision 2
Undergraduate Champion: Team 027

Reason:
Verified paper transcription error in Scorecard S-118

[ Confirm Corrected Official Outcome ]
```

The new revision becomes current official state.

Revision 1 remains historical.

---

## 56. Award correction after Finalization

A rank-derived Award does not silently migrate when corrected Ranking changes.

The Organizer sees:

```text
Undergraduate Champion

Revision 1 recipient:
Team 014

Corrected rank-derived candidate:
Team 027

Award status:
Affected — confirmation required
```

The corrected conferral/revocation history is explicitly recorded before successor Official Outcome confirmation.

---

## 57. External-material impact after correction

003-F does not own regeneration/publication, but it must identify impact for 003-G.

For example:

```text
Official Outcome Revision 2 confirmed

Previously generated from Revision 1:
• ceremony result sheet
• Award certificate batch
• public results export

External representations may require replacement / republication
```

The old artifacts remain historically identifiable.

---

# Information disclosure and privacy

## 58. Organizer reconciliation visibility is broad but purposeful

Organizer mode legitimately requires deeper evidence access than Judge mode, but default reconciliation surfaces should still follow purpose limitation.

For example:

- Coverage reconciliation needs obligation/evidence state;
- Rank explanation needs Scorecard values and policy basis;
- discretionary Award deliberation may require selected private evidence;
- routine closeout does not require displaying all Judge Notes simultaneously.

Broad authority should not become indiscriminate exposure.

---

## 59. Judge access remains closed

Event Completed ended ordinary Judge access to private Scorecards, Notes, and judging history.

003-F does not reopen that access simply because Organizers are reconciling results.

Judge involvement occurs only through narrow authorized correction workflows.

Finalization likewise does not restore ordinary Judge history.

---

# Error, recovery, and concurrency posture

## 60. Reconciliation views must be freshness-aware

Because evidence may change while an Organizer is reviewing Rankings or Finalization, the experience should make stale assumptions visible.

For example:

```text
Ranking changed since you opened this review.

Scorecard S-117 amendment finalized 2 minutes ago.
Refresh affected result state before confirming Award.
```

The exact real-time/update mechanism remains deferred.

The UX requirement is that a consequential action cannot silently commit against materially stale source state.

---

## 61. Multi-Organizer operation

Multiple Organizers may legitimately reconcile different issues concurrently.

The system should support that without last-write-wins ambiguity on authoritative decisions.

Examples:

```text
Organizer A verifies paper evidence
Organizer B resolves a Coverage exception
Organizer C reviews Awards
```

If one change affects another Organizer's open decision context, that context becomes stale/affected and must be refreshed before consequential confirmation.

This is a future concurrency requirement, not a new Organizer locking Concept.

---

## 62. Reconciliation action consequence hierarchy

Not all actions require the same friction.

### Low consequence

```text
open detail
filter list
inspect provenance
```

### Moderate consequence

```text
request Judge correction
record paper verification
```

### High consequence

```text
accept Coverage exception
invalidate Encounter
change active Evaluation Policy after judging
confirm required Award
```

### Highest consequence

```text
Finalize Competition
confirm corrected Official Outcome
```

The UI should reserve stronger confirmations/reason requirements for semantic boundaries rather than interrupting ordinary review work.

---

# 63. Representative reconciliation workspace

A conceptual post-event summary might look like:

```text
RECONCILIATION

Evidence
2 need attention
• Scorecard S-117 — Judge amendment pending
• Paper PF-184 — verification pending

Coverage
1 needs decision
• Team 014 — 11 / 12 Scorecards

Divisions
Undergraduate — Needs attention
• Rank 1 tie requires declared resolver

Graduate — Ranking ready

Awards
3 / 4 required resolved
• Undergraduate Champion pending Ranking resolution

Finalization
Not ready
4 blocking conditions remain
```

The experience leads with decisions and unresolved evidence, not a celebratory leaderboard before those facts are settled.

---

# 64. Representative ready-to-finalize workspace

Once reconciled:

```text
RECONCILIATION COMPLETE

Evidence
✓ Reconciled

Coverage
✓ 30 Teams resolved
  28 Satisfied
  2 Exception Accepted

Rankings
✓ Undergraduate ready
✓ Graduate ready

Awards
✓ All required Awards resolved

Evaluation Policy
✓ v3 authoritative

Finalization
Ready

[ Finalize Competition ]
```

This is not a manually completed checklist.

Each line is backed by inspectable source state.

---

# 65. Core 003-F UX invariants

1. Reconciliation is Organizer activity, not a new Competition lifecycle state.
2. Reconciliation work items are projections from source state, not generic manually-resolved task truth.
3. Evidence authority is reconciled before outcome confidence is implied.
4. Finalization uncertainty cannot be manually converted into a finalized Scorecard.
5. Post-event Judge amendments use narrow temporary Access.
6. Organizer authority never substitutes for Judge judgment.
7. Paper existence and authoritative verified paper evidence remain distinct.
8. Electronic/paper duplicates converge to one logical Scorecard.
9. Invalidated Encounters remain visible historically.
10. Excluded Scorecards retain inspectable exclusion reasons.
11. Coverage and Aggregate remain separate in the UX.
12. Coverage drill-down reaches source obligations/evidence.
13. Coverage exceptions preserve the real shortfall.
14. Coverage exception acceptance is an explicit fairness decision.
15. Composition exceptions and missing Scorecards remain distinct.
16. Withdrawn Teams retain history while official rank eligibility is explicit.
17. Corrected current Division and historical presented Division can be shown together.
18. Incompatible Rubric Versions are never silently normalized.
19. Ranking may be calculated while not ranking ready.
20. Ranking readiness is derived from source state.
21. Ranking is never directly editable.
22. Rank explanation reaches eligible Scorecards, Criteria, Rubric Version, and Evaluation Policy.
23. Accepted exceptions remain discoverable beside ranked results.
24. Team Name may assist Organizer recognition but never affects Rank.
25. Outlier diagnostics do not automatically change evidence eligibility.
26. Display rounding never silently determines Rank.
27. True ties remain ties unless declared policy resolves them.
28. Post-hoc tiebreak selection is prohibited.
29. Rank-derived Award candidates follow ready Ranking.
30. Organizer confirmation cannot contradict a rank-derived Award rule.
31. Discretionary Awards remain visibly discretionary.
32. Sensitive Note access remains purposeful rather than default.
33. Award cardinality controls whether shared-rank recipients can be confirmed.
34. Required and optional Awards remain distinct.
35. Rank-derived Awards become affected rather than silently migrating after Ranking changes.
36. Finalization readiness is derived.
37. Finalization review exposes authoritative Evaluation Policy.
38. Finalization is explicit and high consequence.
39. Finalization is all-or-nothing in domain meaning.
40. Successful Finalization creates an inspectable Official Outcome Revision.
41. Finalized does not mean publicly published.
42. Post-finalization correction uses an exceptional workflow.
43. Latest corrected calculations remain distinct from current official outcome until successor confirmation.
44. Prior Official Outcome Revisions remain historical after correction.
45. Corrected Awards require explicit conferral/revocation handling.
46. Corrected outcomes surface external-representation impact for 003-G.
47. Event Completed and Finalized do not restore ordinary Judge private-data access.
48. Consequential review/confirmation cannot silently rely on materially stale source state.
49. Multiple Organizers can work concurrently without semantic last-write-wins behavior.
50. Confirmation friction scales with consequence.

---

# 66. 003-F Exit Position

The Organizer experience now spans the complete internal Competition lifecycle:

```text
Draft
  ↓
Preparation
  ↓
Ready
  ↓
Live Operations
  ↓
Active
  ↓
Event Completed
  ↓
Reconciliation
  ↓
Coverage / Ranking readiness
  ↓
Awards
  ↓
Finalization
  ↓
Official Outcome Revision
```

The critical experience principle is:

> **The system may continuously calculate outcomes, but it only declares an outcome official after the evidence, policy, eligibility, Rankings, and Awards have been explicitly reconciled and the Organizer deliberately finalizes the Competition.**

This gives the next subgroup a clean external-boundary problem.

**003-G — Paper Capture, Export, Print & Publication Experience** can now design:

```text
physical paper intake / verification
        ↓
Organizer capture workflows

and

authoritative internal source state
        ↓
Export / print / ceremony / public representation
```

without having to redefine evidence authority, Ranking readiness, Award semantics, or what `Official` means.
# 003-I — Cross-Cutting Status, Feedback, Privacy, Disclosure & Recovery Patterns

Status: **Complete**

## 1. Purpose

003-I defines the cross-cutting UX grammar used across Judge onboarding, judging, Organizer preparation, live operations, reconciliation, paper capture, Export/publication, accessibility, and degraded operation.

It consolidates status vocabulary, action feedback, authority/persistence confidence, readiness and severity language, current-versus-historical presentation, disclosure posture, confirmation proportionality, corrective-action language, and recovery patterns without selecting a component library, notification system, design system, routing architecture, persistence implementation, synchronization technology, or AWS service.

The governing objective is:

> The same underlying Competition condition should mean the same thing everywhere it appears, and the interface should never use ambiguous status, optimistic feedback, disclosure leakage, or generic recovery language to blur authority, lifecycle, privacy, or evidence state.

The central model is:

```text
source state
    +
context / audience
    +
authority confidence
    +
readiness / consequence
    +
version / freshness relationship
        ↓
clear human-facing status
        ↓
legitimate next action / recovery
```

No single generic `status` field or colored badge is expected to carry all of these meanings.

---

## 2. Status is multidimensional

MUDAC repeatedly needs to describe several independent facts about the same subject.

For example, a paper-origin Scorecard may simultaneously be:

```text
Capture workflow:
Captured

Verification:
Pending

Scorecard authority:
Not yet authoritative

Artifact/source relationship:
Current physical source

Disclosure:
Organizer-sensitive
```

Likewise, after a post-finalization correction:

```text
Competition lifecycle:
Finalized

Official Outcome Revision 1:
Current official outcome
Affected by later correction

Latest calculated Ranking:
Updated
Not yet official

Publication based on Revision 1:
Published
Affected / stale
```

The UX must not attempt to compress these into one ambiguous label such as:

```text
Pending
```

or:

```text
Updated
```

without identifying the dimension being described.

---

## 3. Canonical status dimensions

The experience architecture should distinguish at least these dimensions when relevant:

1. **Domain lifecycle / workflow state** — what state the underlying subject is in.
2. **Authority state** — whether a value is working, authoritative, official, or unknown.
3. **Persistence / synchronization confidence** — what storage state is actually confirmed.
4. **Readiness state** — whether a larger action may legitimately proceed.
5. **Validity / eligibility state** — whether evidence or a Team may contribute under policy.
6. **Version / freshness relationship** — whether an artifact or representation reflects current source state.
7. **Issue consequence / severity** — how urgently the condition matters and whether it blocks the current goal.
8. **Disclosure posture** — which audience/context may receive the information.
9. **Publication/release state** — whether an external representation has actually been released.

A component may visually summarize several dimensions, but the underlying meanings remain separate.

---

# Naming and state language

## 4. Qualify overloaded words

Words such as:

```text
Ready
Complete
Finalized
Current
Official
Published
Resolved
```

must normally be qualified by the subject they describe.

Prefer:

```text
Judge ready to judge
Competition Ready
Encounter Complete
Scorecard Finalized
Competition Finalized
Ranking ready
Current authoritative Rubric
Current official outcome
Results published
Coverage resolved
```

rather than context-free badges such as:

```text
Ready
Complete
Final
Current
Done
```

when multiple meanings are possible.

---

## 5. `Complete` is not `Finalized`

This distinction is particularly important for judging.

```text
Draft — complete
```

means all required Scorecard content is currently present.

It does **not** mean:

```text
Scorecard Finalized
```

Likewise:

```text
Encounter Complete
```

means Encounter evaluation obligations are resolved.

It does not mean:

```text
Event Completed
```

The interface must not shorten all of these to one generic `Complete` state in contexts where the subject is unclear.

---

## 6. `Finalized` is reserved for domain authority transitions

`Finalized` should not be used as decorative language for something that is merely finished in the user's mind.

Canonical examples are:

```text
Scorecard Finalized
Competition Finalized
```

A Rubric is instead described as an authoritative Rubric Version.

A Ranking can be calculated or ranking-ready.

An Award can be conferred.

A publication can be published/released.

Using each domain's actual verb keeps authority boundaries visible.

---

## 7. `Official` is narrower than `authoritative`

An authoritative Scorecard is not itself called the official Competition result.

The vocabulary should preserve:

```text
Scorecard Finalized
    → authoritative evaluation evidence

Ranking ready
    → trusted derived ordering, not yet official Competition outcome

Official Outcome Revision
    → official Competition declaration

Published result
    → external disclosure of an Official Outcome Revision
```

This helps prevent `authoritative`, `official`, and `public` from becoming synonyms.

---

## 8. `Resolved` means the source condition is actually resolved

A reconciliation or live-operation issue is a projection from source state.

Therefore an issue is not `Resolved` merely because an Organizer:

```text
opened it
read it
acknowledged it
dismissed a notification
```

For example:

```text
Coverage Incomplete
```

becomes resolved only when the actual source condition becomes one of the permitted resolved states, such as:

```text
Coverage Satisfied
```

or:

```text
Coverage Exception Accepted
```

Acknowledgement and resolution remain different concepts in the experience.

---

# Readiness and issue consequence

## 9. Canonical readiness vocabulary

For derived preparation/operation/closeout projections, the preferred semantic vocabulary is:

### Ready

The relevant derived conditions currently permit the intended action.

### Needs attention

A blocking condition exists and the intended action cannot legitimately proceed until source state changes or an authorized exception path is completed.

### Warning

A meaningful risk or incomplete operational condition exists, but the intended action is not automatically blocked under current policy.

### Optional / Not configured

The feature or workstream is not required under current Competition policy and its absence is not itself a defect.

These terms may be refined visually later, but their meanings should not drift by workflow.

---

## 10. Readiness is always qualified

Because MUDAC has several readiness projections, views should identify which one is being discussed:

```text
Competition Ready
Judge ready to judge
Panel composition ready / warning
Division ranking ready
Finalization ready
```

A Judge can be ready while the Competition is not Active yet.

A calculated Ranking can exist while the Division is not ranking-ready.

A Competition can be Finalized while publication is not ready.

No single global `Ready` badge should hide those differences.

---

## 11. Issue severity remains separate from workflow status

A condition can be in a particular workflow state and also carry a consequence level.

The initial cross-cutting severity vocabulary is:

### Informational

No intervention is currently required; the state is useful context.

### Warning

Attention is advisable, but the immediate workflow may proceed under current policy.

### Blocking

The intended operation cannot legitimately proceed until the source state is resolved or an explicit authorized exception applies.

### Critical

The condition presents an immediate integrity, privacy, authority, or duplicate-evidence risk and should be contained before normal operation continues where possible.

Examples of potential Critical conditions include:

```text
wrong Team actively being judged
Judge-sensitive identity disclosure to blinded Judge context
possible duplicate authoritative Scorecard
uncertain outcome-changing operation during Finalization
```

Severity never replaces the more precise source status.

---

## 12. Avoid false precision in readiness

The experience should not use percentage completion where it obscures semantic importance.

For example:

```text
Competition 98% ready
```

is misleading if the missing 2% is:

```text
no authoritative Evaluation Policy
```

Prefer source-aware status:

```text
Competition — Needs attention
Evaluation Policy is not valid for use
```

Counts can supplement this information but must not imply that all checklist items have equal consequence.

---

# Authority and persistence confidence

## 13. Authority confidence vocabulary

Where an operation depends on confirmation from authoritative state, the experience should distinguish:

### Confirmed

The authoritative system has confirmed the state.

### Pending confirmation

The operation has been initiated or local work exists, but authoritative completion is not yet known.

### Unknown / Could not confirm

The application cannot establish whether the authoritative transition occurred and must recover current state before making a claim.

### Conflict / Changed elsewhere

The action was based on stale state and cannot safely replace the newer authoritative state without review.

The exact labels may vary slightly by context, but the semantic states must remain distinguishable.

---

## 14. Persistence language is precise

For Draft work, the application may eventually need to distinguish:

```text
Saving…
Saved
Changes pending synchronization
Connection lost — local working copy preserved
Could not confirm persistence
```

`Saved` should mean the level of persistence the UI explicitly claims.

If only local preservation is known, the message must say so rather than implying server-authoritative persistence.

The UX should never use a reassuring generic checkmark when the level of persistence is actually unknown.

---

## 15. Authoritative action feedback persists in context

High-consequence outcomes should not exist only as disappearing transient notifications.

After Scorecard Finalization, for example, the enduring Scorecard state should read:

```text
Scorecard Finalized
```

not merely show a short-lived toast saying:

```text
Success
```

Likewise:

```text
Competition Finalized
Official Outcome Revision 1 — Current official outcome
```

should remain visible after the confirmation message disappears.

Transient feedback can supplement durable source state; it cannot replace it.

---

## 16. Uncertain actions remain uncertain

For an ambiguous Finalization response, prefer:

```text
We could not confirm Scorecard Finalization.
Your last confirmed state is Draft.
Check current status or try again safely.
```

rather than:

```text
Finalization probably succeeded.
```

The same rule applies to:

```text
Activate Competition
Complete Event
invalidate Encounter
accept Coverage exception
Finalize Competition
publish results
```

Authority uncertainty must survive into the next view until it is resolved.

---

# Version, history and freshness

## 17. Current versus historical state is explicitly labeled

Where current state differs from historical observed state, the interface should state both roles.

Examples:

```text
Current Division
Graduate

Presented at Encounter E-021
Undergraduate
```

```text
Current Panel members
J-A, J-B, J-D

Encounter E-014 participants
J-A, J-B, J-C
```

```text
Current authoritative Scorecard
v2

Historical Version
v1
```

The user should not have to infer temporal semantics from placement or font styling alone.

---

## 18. `Current` is qualified by authority context

Potential labels include:

```text
Current authoritative Rubric
Current authoritative Scorecard Version
Current official outcome
Current generated artifact
```

These are not interchangeable.

A stale artifact may still reference the current historical source it was generated from while no longer representing the current source state.

Qualifying `Current` prevents this ambiguity.

---

## 19. Artifact freshness vocabulary

Generated/printed/published representations use a separate freshness relationship to their source.

### Current

The artifact represents the source Version/revision currently intended for its purpose.

### Stale

The source state has changed in a way that means the artifact should normally be regenerated before future use.

### Superseded

A successor artifact has replaced it as the preferred/current representation.

### Withdrawn from current distribution

The artifact should no longer be actively distributed, while its historical existence remains recorded where appropriate.

These labels describe the representation, not the underlying Competition state.

---

## 20. `Affected` identifies downstream impact without pretending correction is complete

When a source correction may invalidate a dependent state, the interface may use a qualified `Affected` state.

Examples:

```text
Award confirmation affected by Ranking change
Official Outcome Revision 1 affected by corrected evidence
Published results affected by Official Outcome Revision 2
```

`Affected` means:

> This state requires review because one of its authoritative dependencies changed.

It does not automatically mean revoked, corrected, superseded, or republished.

---

# Validity, eligibility and exception language

## 21. Missing, invalidated and excluded remain distinct

The UI must not collapse:

```text
Missing
Invalidated
Excluded
Superseded
Withdrawn
Recused
```

into one generic `Not counted` state.

Examples:

### Missing

Expected evidence does not exist or is unresolved.

### Recused / obligation excused

The Judge no longer owes an evaluation under valid Encounter participation adjustment.

### Invalidated

The historical record exists but is not valid for official use under the governing decision.

### Superseded

An older Version exists historically but a successor is now authoritative.

### Excluded

The record exists but is not eligible for a particular derived calculation under policy.

### Withdrawn Team

The Team and its evaluation history remain, but baseline Rank eligibility is excluded.

These distinctions are essential for Coverage and auditability.

---

## 22. Exceptions never masquerade as normal satisfaction

When a policy exception is accepted, the original condition remains visible.

Prefer:

```text
Coverage
11 / 12
Exception Accepted
```

rather than:

```text
Coverage
12 / 12
```

Likewise:

```text
Panel composition
Warning
Exception Accepted — no Business capacity
```

is preferable to changing the Panel display to `Fully compliant`.

An exception changes what may proceed. It does not rewrite what happened.

---

# Action feedback and confirmation

## 23. Feedback contract

After a meaningful action, feedback should answer as many of these as are relevant:

1. **What action was attempted?**
2. **What state is now confirmed?**
3. **What remains uncertain or unchanged?**
4. **Was existing work preserved?**
5. **What downstream consequence occurred?**
6. **What can the user do next?**

For example:

```text
Coverage exception accepted for Team 014.
Coverage remains 11 / 12.
Team 014 is now rank-eligible under the current Evaluation Policy.
```

is more useful than:

```text
Success.
```

---

## 24. Feedback should be local to the affected context

Where possible, action feedback should appear with the subject whose state changed.

Examples:

```text
Scorecard → Finalized
Panel → composition warning accepted
Team → Division corrected
Export → Stale
Publication → Published
```

Global notifications may supplement this but should not force users to remember which of several concurrent Teams, Panels, or Scorecards a message referred to.

---

## 25. Confirmation friction tiers

Confirmation strength should scale with semantic consequence.

### Tier 0 — ordinary working edit

Examples:

```text
change Draft criterion score
edit Draft Note
change optional Team Name during Draft
filter / sort Organizer view
```

No confirmation is normally required.

### Tier 1 — recoverable workflow change

Examples:

```text
leave Scorecard unfinished and continue
abandon a non-authoritative working Draft
move between Organizer work regions with preserved changes
```

Use clear consequence messaging where needed, but avoid unnecessary modal friction.

### Tier 2 — authoritative or operational commitment

Examples:

```text
Finalize Scorecard
Recuse from Encounter
Activate Competition
Complete Event
invalidate Encounter
accept Coverage exception
confer discretionary Award
Finalize Competition
Publish official results
```

Require deliberate, accessible confirmation with the affected subject and consequence visible.

### Tier 3 — exceptional / post-finalization / break-glass action

Examples:

```text
post-finalization outcome-changing correction
break-glass sensitive Access
correct an official Award after publication
release corrected official results
```

Require stronger authority checks, explicit reason, clear before/after consequence, and any configured re-verification or dual-control policy.

Tier names are UX architecture vocabulary, not necessarily literal UI labels.

---

## 26. Confirmation shows the subject, not only the verb

Prefer:

```text
Finalize Team 014 evaluation?
```

or:

```text
Complete live judging for MinneMUDAC 2026?
```

rather than:

```text
Are you sure?
```

For high-consequence actions, the confirmation should identify:

```text
Competition
Team / Encounter / Award where relevant
current state
resulting state
important irreversible or downstream consequence
```

without requiring the user to reconstruct context from memory.

---

## 27. Corrective verbs are preferred to destructive ambiguity

Because MUDAC preserves history, the UI should use the domain verb that actually describes the consequence.

Prefer:

```text
Withdraw Team
Retire Division
End Panel membership
Recuse Judge
Cancel Encounter
Invalidate Encounter
Supersede Version
Revoke Award
Correct transcription
Abandon Amendment Draft
Withdraw publication
```

rather than generic:

```text
Delete
Remove
Reset
Undo
```

when the historical record is intentionally retained.

`Delete` is reserved for truly destructive removal cases permitted by domain policy, such as an unreferenced Draft setup mistake.

---

# Privacy and disclosure

## 28. Disclosure is context-specific projection

MUDAC does not maintain separate duplicate Team records for every audience.

Instead:

```text
source Team / evaluation state
      +
Identity / Participation / Access
      +
audience / disclosure profile
        ↓
representation
```

The same Team may therefore appear as:

```text
Organizer
Institution + Team Name + Alias + Division
```

and:

```text
Judge
Alias + Division
```

without creating different Teams.

Disclosure rules apply consistently across screens, search results, previews, exports, print, deep links, encoded identifiers, and publication.

---

## 29. Disclosure profiles are purpose-specific, not a simple sensitivity ladder

The principal representation profiles established so far are:

### Judge-safe

Provides only information permitted during blinded judging.

### Organizer-sensitive

May include administrative identity, internal operational context, private evaluation evidence where authorized, and source/provenance detail.

### Ceremony-safe

Contains only information approved for live announcement/display at the event.

### Public

Contains only information deliberately approved for public release.

These are not necessarily a strict hierarchy.

For example, a field may be ceremony-safe but intentionally omitted from a public archive, or public after Finalization but hidden from Judges during live evaluation.

---

## 30. Team attribute disclosure is explicit

Extensible Team attributes do not inherit visibility merely because they exist.

For `teamName`, the baseline remains:

```text
Organizer visibility:
Allowed

Judge visibility during blinded judging:
Hidden by default

Ceremony / Public visibility:
Explicit disclosure decision
```

A new attribute such as `Faculty Advisor` cannot silently become Judge-visible or public because a generic Team details renderer includes all fields.

---

## 31. Judge private evaluation evidence has a distinct posture

Judge Scorecards and Notes are not treated as ordinary Team metadata.

During the live access window:

```text
Judge
may access own authorized evaluation evidence

Peer Judge
cannot access another Judge's Scorecard/Notes

Organizer
may access according to Organizer authority and purpose
```

At Event Completed, ordinary Judge private-evaluation access expires while Organizer-governed records remain retained.

Public/Ceremony profiles do not include raw Judge Notes or Judge-linked individual scoring by default.

---

## 32. Role switching changes disclosure context, not merely navigation

For a dual-role Identity:

```text
Organizer mode
      ↓ explicit switch
Judge mode
```

must also change the information boundary.

Organizer-only Team identity, private Judge evidence, Coverage, Rank, and exception information must not remain visible merely because they were already loaded in the prior mode.

The implementation may later use re-fetching, cache partitioning, view reconstruction, or another mechanism; the UX contract is that the Judge-mode representation is Judge-safe.

---

## 33. Deep links do not leak hidden context

A deep link, QR code, bookmark, or copied URL identifies a requested destination.

The experience still resolves:

```text
Identity
Participation / role mode
Competition
Access
Disclosure
```

before rendering sensitive content.

If a user lacks access, error text, titles, previews, navigation breadcrumbs, and metadata should not unnecessarily reveal protected Team identity, Judge Notes, Rank, or other hidden information merely to explain the denial.

---

## 34. Search, filter and autocomplete obey disclosure too

Disclosure rules are not limited to detail pages.

A Judge-safe search must not reveal:

```text
institution names
hidden Team Names
Organizer notes
other Judges' Scorecards
Rank
```

through search suggestions, filters, counts, previews, or empty-state text.

Likewise, public publication tooling should preview the target public representation rather than merely showing what the Organizer can see internally.

---

## 35. Preview uses target disclosure, not actor privilege

Organizer preview of a Judge-safe, ceremony, or public artifact should answer:

> What will the target audience receive?

not:

> What can this Organizer see?

The preview should therefore apply the target disclosure profile even though the Organizer has broader internal authority.

This is a core defense against accidental leakage in Export/publication workflows.

---

# Recovery patterns

## 36. Canonical recovery message structure

Recovery messaging should answer, in order where relevant:

1. **What were you trying to do?**
2. **What state is definitely known now?**
3. **What did not happen or cannot be confirmed?**
4. **What work/data has been preserved?**
5. **What is the safest next action?**
6. **When should an Organizer or Administrator be involved?**

This structure applies across Judge and Organizer workflows.

---

## 37. Draft persistence recovery

Example pattern:

```text
Connection lost.
Your changes are preserved on this device but are not yet confirmed by the Competition system.
You can continue this Draft if permitted, or switch to paper if instructed.
Do not assume the evaluation is Finalized.
```

When reconnection occurs:

```text
checking current authoritative Scorecard state
      ↓
no conflict → synchronize / continue
conflict → preserve both views and require review
```

The system never silently discards one side merely to remove the warning.

---

## 38. Finalization uncertainty recovery

If a Scorecard Finalization response is ambiguous:

```text
Finalization could not be confirmed.
```

The next action is not to create another Scorecard.

Recovery resolves the same logical Judge × Encounter Scorecard and determines whether:

```text
Finalization already succeeded
Draft remains authoritative working state
stale-base conflict exists
```

Only then does the UI present the resulting state.

---

## 39. Stale-state conflict recovery

If an action was based on an older authoritative state, prefer:

```text
This Scorecard changed after you opened it.
Your pending changes have not overwritten the newer authoritative Version.
Review the current Version and reconcile your Draft.
```

or for Organizer work:

```text
This Team's Division changed while you were reviewing Finalization.
Finalization did not proceed.
Review the updated Ranking impact and try again.
```

The conflict message should make safe non-overwrite behavior explicit.

---

## 40. Session or Access expiry recovery

When authentication/session state expires, the application should distinguish:

```text
working state preserved where safely possible
```

from:

```text
current Access no longer confirmed
```

After re-verification, the user returns to the same Competition/Participation/resource where policy permits.

For Judge private evaluation after Event Completed, recovery must **not** restore access merely because the prior session existed. The lifecycle Access rule still applies.

---

## 41. Wrong-context recovery

If a user reaches the wrong Competition, Team, Panel, Encounter, or role mode, recovery should preserve any safe unrelated Draft work and explicitly re-establish context before new action.

For example:

```text
This link is for Panel 07.
You are currently assigned to Panel 04.
No Panel assignment was changed.
Ask an Organizer if you should switch.
```

or:

```text
This Encounter is for Team 027.
Your current Draft belongs to Team 014 and has been preserved.
Return to Team 014 or ask an Organizer for help.
```

The interface should never silently relabel meaningful existing work to match the requested destination.

---

## 42. Paper fallback recovery is explicit channel convergence

When electronic judging moves to paper, feedback should make the authority transition clear:

```text
Electronic Draft retained
Paper source PF-184 assigned
Continue evaluation on paper
```

After digital recovery:

```text
Paper source detected for this Judge + Encounter
Electronic Draft also exists
Reconciliation required before authoritative Scorecard is established
```

The system must not frame this as two completed evaluations.

---

## 43. Publication failure recovery preserves official state

If release fails after Competition Finalization:

```text
Competition Finalized
Official Outcome Revision 1 confirmed
Publication not confirmed
```

The retry applies to the publication operation, not to Competition Finalization.

Likewise, a stale/superseded publication can be replaced without altering the historical Official Outcome Revision it represented.

---

# Feedback accessibility and responsive behavior

## 44. Important feedback is perceivable through multiple interaction modes

The accessibility requirements from 003-H apply to all cross-cutting feedback.

Important status must be available through:

- text, not color alone;
- programmatically meaningful structure;
- sensible focus behavior;
- nonvisual notification when appropriate;
- readable responsive presentation;
- persistent context for high-consequence states.

Routine autosaves should not create an overwhelming stream of announcements, while meaningful transitions such as connection loss, Finalization confirmation, Panel reassignment, or publication failure must remain perceivable.

---

## 45. Narrow views preserve semantic dimensions

On small screens, status dimensions may be composed vertically rather than hidden.

For example:

```text
Team 014
Scorecard: Draft — complete
Persistence: Changes pending
Encounter: Open
```

is preferable to compressing those into one icon whose meaning changes depending on viewport.

Organizer narrow views follow:

```text
summary
   ↓
exception
   ↓
source status dimensions
   ↓
legitimate action / recovery
```

instead of dropping secondary-but-critical authority or disclosure information to save space.

---

# Canonical cross-cutting vocabulary

## 46. Preferred vocabulary table

| Dimension | Preferred language |
| --- | --- |
| Scorecard working state | `Draft — incomplete`, `Draft — complete`, `Amendment Draft` |
| Scorecard authority | `Scorecard Finalized`, `Current authoritative Scorecard Version`, `Historical Version` |
| Persistence | `Saving…`, `Saved`, `Changes pending`, `Could not confirm persistence` |
| Finalization ambiguity | `Finalization could not be confirmed` |
| Readiness | `Ready`, `Needs attention`, `Warning`, qualified by subject |
| Coverage | `Satisfied`, `Incomplete`, `Exception Accepted` with actual counts retained |
| Ranking | `Calculated / provisional`, `Ranking ready`, `Official` only through Official Outcome |
| Artifact freshness | `Current`, `Stale`, `Superseded`, `Withdrawn from current distribution` |
| Publication | `Not published`, `Staged / preview`, `Published`, `Affected` where source changed |
| Historical state | `Current …`, `Presented at Encounter …`, `Historical Version`, `Superseded Version` |
| Evidence validity | `Valid`, `Invalidated`, `Excluded`, with reason |
| Judge obligation | `Not started`, `Draft`, `Finalized`, `Recused / excused`, `Missing / unresolved` |
| Issue consequence | `Informational`, `Warning`, `Blocking`, `Critical` |
| Exception | `Exception Accepted` while original shortfall/deviation remains visible |

The exact capitalization and visual treatment remain for later design-system work. Semantic meaning is canonical here.

---

## 47. Words to avoid when they obscure semantics

Avoid context-free use of:

```text
Done
Finished
Complete
Final
Current
Fixed
Synced
Success
Failed
Error
Removed
Deleted
Resolved
```

when a more precise domain phrase exists.

For example:

```text
Encounter Complete
```

is better than:

```text
Done
```

and:

```text
Scorecard invalidated — Encounter invalidated
```

is better than:

```text
Removed
```

Precision is particularly important under interruption, accessibility use, and live-event stress.

---

# Cross-cutting anti-patterns

## 48. Anti-pattern: one global status badge

Do not attempt:

```text
Team 014 — Warning
```

when the Team may simultaneously have:

```text
Coverage: Satisfied
Ranking: ready
Publication: not applicable
1 historical Encounter composition exception
```

Summaries may prioritize one current concern, but drill-down must preserve the independent dimensions.

---

## 49. Anti-pattern: optimistic success

Do not convert:

```text
request sent
```

into:

```text
Finalized
```

or:

```text
Published
```

until authoritative confirmation exists.

This rule applies even when optimistic UI would make the interface feel faster.

---

## 50. Anti-pattern: permission by visibility

Hiding a button does not establish security.

Showing a value in one role mode does not authorize it in another.

The experience layer may hide unavailable actions to reduce noise, but Access and disclosure enforcement remain authoritative behind the representation.

---

## 51. Anti-pattern: error message that leaks sensitive data

A Judge denied access to an Organizer-only resource should not receive an error that unnecessarily reveals the institution, private Judge Note content, or live Rank simply to explain which resource was denied.

Recovery language should disclose enough to re-establish legitimate context, not more.

---

## 52. Anti-pattern: confirmation fatigue

Do not require confirmation for every Draft score change or low-consequence edit.

Excessive confirmation trains users to click through the exact prompts meant to protect high-consequence operations.

Confirmation remains proportional to semantic consequence.

---

## 53. Anti-pattern: destructive cleanup of inconvenient history

Do not solve operational confusion by deleting:

```text
invalidated Encounter
superseded Scorecard Version
prior Award conferral
stale publication
old Alias use
```

when the domain model requires historical preservation.

The UX should explain why the historical item remains and which current state supersedes or invalidates it.

---

# 003-I invariants

## 54. Cross-cutting UX invariants

1. Status dimensions remain semantically distinct even when visually summarized.
2. Readiness, authority, persistence, validity, freshness, severity, disclosure, and publication are never treated as one generic state.
3. `Ready`, `Complete`, `Finalized`, `Current`, `Official`, `Published`, and `Resolved` are qualified where ambiguity is possible.
4. `Draft — complete` never implies Scorecard Finalization.
5. `Encounter Complete` never implies Event Completed.
6. Ranking readiness never implies Official Outcome.
7. Competition Finalized never implies Published.
8. `Official` is reserved for declared Competition outcome semantics, not any authoritative record.
9. Reconciliation issues are resolved only through legitimate source-state resolution.
10. Manual acknowledgement never erases a source warning or exception.
11. Readiness derives from source state rather than manual checklist status.
12. Issue severity is separate from workflow state.
13. Authority uncertainty remains visible until resolved.
14. Optimistic UI never invents successful authoritative transitions.
15. High-consequence feedback persists in subject state rather than only transient notifications.
16. Current and historical facts are explicitly labeled.
17. Artifact freshness does not alter source history.
18. `Affected` indicates review need without silently applying a correction.
19. Missing, recused, invalidated, excluded, superseded, and withdrawn remain distinct.
20. Accepted exceptions preserve the underlying shortfall/deviation.
21. Confirmation friction scales with semantic consequence.
22. Exceptional/post-finalization actions require stronger authority/reason patterns.
23. Corrective domain verbs are preferred over ambiguous destructive language.
24. Disclosure is derived from source + context + Access + audience profile.
25. Role switching changes disclosure context as well as navigation.
26. Deep links, search, filters, previews, metadata, and exports obey disclosure boundaries.
27. Organizer privilege does not broaden Judge-safe/public preview output.
28. Team attributes do not inherit audience visibility merely by existing.
29. Judge private evaluation evidence never becomes public by default.
30. Recovery messages identify attempted action, known state, uncertainty, preserved work, and next safe action.
31. Stale-base conflicts never silently overwrite newer authority.
32. Session/device recovery re-establishes current Access rather than blindly restoring stale authority.
33. Wrong-context recovery never silently relabels meaningful existing work.
34. Paper/electronic duplicate-risk is presented as one-evaluation convergence.
35. Publication failure never weakens Competition Finalization.
36. Important status/feedback is accessible nonvisually and does not rely on color alone.
37. Narrow-screen presentation preserves authority, privacy, and recovery semantics.
38. No single global badge is expected to explain every dimension of a complex Competition subject.

---

## 55. Implementation deferrals

003-I does not yet choose:

- badge/component visual design;
- exact color tokens or iconography;
- toast/banner/dialog technology;
- notification persistence implementation;
- live-region implementation details;
- routing or deep-link URL syntax;
- permission enforcement framework;
- cache/session partitioning implementation;
- synchronization/conflict algorithm;
- telemetry/error-reporting infrastructure;
- design-system package;
- AWS services.

Those later choices must implement the semantics established here.

---

## 56. 003-I exit position

Phase 003 now has one cross-cutting language for the major experience dimensions:

```text
WHAT IS IT DOING?
    domain / workflow state

CAN IT COUNT OR PROCEED?
    validity / eligibility / readiness

IS THAT STATE AUTHORITATIVE?
    authority + persistence confidence

IS THIS THE CURRENT REPRESENTATION?
    Version / freshness relationship

HOW SERIOUS IS THE CONDITION?
    issue consequence

WHO MAY SEE IT?
    disclosure profile / Access context

WAS IT RELEASED?
    publication state

WHAT HAPPENS NEXT?
    legitimate action / recovery
```

This means 003-J can now evaluate Phase 003 as one coherent experience architecture rather than a collection of individually consistent journeys.

The next subgroup is **003-J — Phase 003 Consolidation & UX Architecture Exit Review**.

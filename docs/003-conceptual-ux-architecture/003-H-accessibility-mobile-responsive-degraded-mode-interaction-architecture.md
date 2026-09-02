# 003-H — Accessibility, Mobile, Responsive & Degraded-Mode Interaction Architecture

Status: **Complete**

## 1. Purpose

003-H defines the cross-journey interaction architecture required for MUDAC to remain understandable, operable, private, and semantically correct across accessibility needs, device sizes, interruptions, unreliable connectivity, shared or changed devices, and full digital degradation.

It applies the Phase 001–003 authority, lifecycle, judging, paper, Export, and recovery semantics to the actual conditions under which a live academic competition is likely to operate without selecting a component library, CSS framework, browser-storage mechanism, synchronization protocol, offline database, service worker strategy, real-time transport, authentication provider, printer technology, or AWS service.

The governing objective is:

> A change in sensory ability, input method, viewport, device, connectivity, or capture channel may change how a person interacts with the Competition, but it must not silently change what action they are taking, whose authority it represents, what evidence is authoritative, what information is disclosed, or how an evaluation contributes to official outcomes.

The central resilience model is:

```text
same Competition semantics
        ↓
┌──────────────────────────────────────────────┐
│ visual / nonvisual interaction              │
│ touch / keyboard / assistive input           │
│ small / large viewport                       │
│ online / interrupted / degraded connection  │
│ personal / replacement / shared device       │
│ electronic / paper capture                   │
└──────────────────────────────────────────────┘
        ↓
same authority + privacy + evidence meaning
```

Accessibility is therefore not a separate product mode, and degraded operation is not a second competition model.

---

## 2. Accessibility is semantic parity, not an accommodation fork

The application must not create a lower-fidelity workflow in which an accessible path has weaker semantics than the ordinary path.

For example, a Judge using keyboard navigation or screen-reader interaction still performs:

```text
confirm Encounter context
      ↓
edit one Scorecard Draft
      ↓
review
      ↓
explicitly Finalize
```

They do not receive a separate simplified Scorecard that loses Notes, guidance, validation, Versioning, or explicit Finalization semantics.

Likewise, an Organizer using a narrow viewport or keyboard navigation must still be able to:

- inspect source state;
- distinguish blockers from warnings;
- understand current versus historical information;
- invoke authorized corrections;
- review Finalization readiness;
- understand the effect of high-consequence actions.

The interaction mechanism may differ. The domain meaning must not.

---

## 3. Baseline accessibility posture

MUDAC should be designed so that a future implementation can reasonably target **WCAG 2.2 AA** across core user journeys rather than attempting to retrofit accessibility after component implementation.

003-H does not reproduce the standard as an implementation checklist. It establishes design requirements that the eventual implementation must satisfy, including:

- operability without a mouse;
- meaningful programmatic structure;
- logical reading and focus order;
- visible focus;
- text resizing and responsive reflow;
- sufficient contrast;
- status not communicated by color alone;
- understandable labels and errors;
- sufficiently large interaction targets;
- alternatives to camera/QR-only workflows;
- no gesture-only essential action;
- no hover-only essential information;
- reduced-motion compatibility;
- accessible authentication and recovery paths;
- preservation of context and work through interruption.

Accessibility validation remains an implementation and test responsibility in later phases, but the UX architecture may not depend on patterns that make those requirements impossible.

---

## 4. Accessibility does not imply disclosure expansion

Assistive technology does not change Access or disclosure rules.

A screen reader should receive the same authorized Judge-safe Team context that a visual Judge receives:

```text
Team 014
Undergraduate
```

not hidden administrative identity merely because more descriptive text exists internally.

Likewise, accessible alternatives to QR, visual charts, or color-coded statuses expose equivalent permitted information, not broader Organizer-sensitive data.

The principle is:

> Accessibility changes representation, not authorization.

---

# Responsive interaction architecture

## 5. Responsive means task-appropriate, not visually identical

MUDAC has different primary device assumptions by role.

### Judge

Primary live device posture:

```text
personal smartphone
portrait or landscape
one-handed / touch interaction likely
frequent attention shifts away from device
```

The complete ordinary Judge journey must therefore be fully usable on a small touch screen.

### Organizer

Likely primary posture:

```text
laptop / desktop / tablet
multiple concurrent operational conditions
higher information density
```

Organizer workflows may legitimately take advantage of wider displays.

However, the application must not become unusable on a narrow screen. A narrow Organizer experience may prioritize:

```text
summary
  ↓
exception list
  ↓
selected issue
  ↓
source detail / legitimate action
```

instead of attempting to reproduce a dense desktop command table at miniature scale.

Responsive adaptation may change composition and information density. It may not change underlying state or action meaning.

---

## 6. Judge phone-first hierarchy

During active judging, the small-screen information hierarchy should preserve approximately this priority:

```text
1. Team Alias + Division
2. Scorecard / Encounter state
3. current Criterion + valid score choices
4. Criterion guidance
5. Criterion Note
6. progress / missing requirements
7. save / synchronization confidence
8. supporting navigation
```

Persistent context should not consume so much screen area that the Judge cannot score effectively, but enough Team/Division context must remain available to prevent wrong-Team drift after interruption.

The exact sticky-header, card, accordion, tab, or step presentation remains deferred.

---

## 7. Small-screen scoring controls

Score controls must be suitable for touch while remaining semantically operable through keyboard and assistive technologies.

For a finite score domain such as:

```text
1 2 3 4 5
```

controls should expose the actual choices rather than requiring a tiny numeric input field.

Every choice must have an unambiguous accessible name and selected state.

The Judge must not need to:

- drag a slider precisely;
- swipe in one direction;
- perform a long press;
- distinguish score values by color alone;
- rely on hover text;
- tap very small targets.

A visual interaction may supplement these methods but cannot make them essential.

---

## 8. Device orientation

The Judge workflow must not require one device orientation.

Portrait may be the normal design posture, but rotating the device must not:

- erase Draft changes;
- change the current Criterion;
- close a Note field destructively;
- duplicate an action;
- lose Team context;
- trigger Finalization.

Organizer wide-screen layouts may benefit from landscape/desktop space, but orientation or viewport changes still preserve selected Competition, work mode, filters where reasonable, and unfinished state.

---

## 9. Text enlargement and reflow

Core interactions must tolerate enlarged text and browser/platform zoom without overlapping essential controls or making critical information unreachable.

A Judge increasing text size must still be able to identify:

```text
Team
Division
Criterion
score choices
Note requirement
Draft / Finalized state
```

without horizontally scrolling the entire application simply to complete one Criterion.

Dense Organizer tables may use horizontal scrolling where the tabular relationship itself genuinely requires it, but essential status, issue consequence, and next action should also be available through a responsive detail presentation.

---

## 10. Information density must degrade gracefully

Wide Organizer views may show multiple fields simultaneously:

```text
Panel | composition | current Team | Encounter | obligations | status
```

On smaller viewports, the same information can become:

```text
Panel 04
Composition: Warning
Current Team: 014
Encounter: Open
Evaluations: 2 finalized, 1 Draft
```

This is a representation change, not a different state model.

The narrow experience should prioritize actionable exceptions over preserving desktop column geometry.

---

# Nonvisual and keyboard interaction

## 11. Semantic structure

Page and task structure should communicate meaningful regions and headings programmatically.

For example, a Judge Scorecard should have an intelligible hierarchy such as:

```text
Team 014 — Undergraduate
    Scorecard Draft
        Methodology
        Analysis
        Communication
        Innovation
        Presentation
        Overall Note
        Final review
```

A screen-reader user should not encounter an undifferentiated sequence of generic buttons and unlabeled inputs.

Likewise, Organizer exception views should expose meaningful relationships between issue, source, severity, consequence, and action.

---

## 12. Keyboard operation

Every ordinary task must be completable without pointer interaction.

This includes at minimum:

- Competition/event entry;
- Identity and onboarding;
- Panel confirmation;
- Team/Encounter confirmation;
- score selection;
- Notes;
- Draft navigation;
- Finalization;
- amendment;
- Organizer readiness review;
- live-operation exception handling;
- reconciliation;
- paper capture;
- Export preview and release actions.

Keyboard order must follow task meaning rather than CSS/visual placement alone.

---

## 13. Focus management

Focus movement is part of state comprehension.

When an action changes context significantly, focus should move or remain in a predictable location.

Examples:

### Validation failure

```text
Finalize
  ↓
validation fails
  ↓
focus / announcement identifies first unresolved requirement
```

### Opening amendment

Focus should move into a clearly identified Amendment Draft context rather than leaving the user on a visually changed but semantically ambiguous page.

### Returning from interruption

Focus should not unexpectedly jump to `Finalize` or another high-consequence action.

Exact implementation remains deferred, but unpredictable focus is considered a functional integrity problem, not cosmetic polish.

---

## 14. Dynamic status announcements

Saving, synchronization, validation, and recovery state may change without a full page navigation.

Important status transitions should be perceivable nonvisually without producing a constant stream of distracting announcements.

Examples that may warrant accessible notification include:

```text
Draft saved
connection lost
changes not yet confirmed
Finalization confirmed
Finalization could not be confirmed
Panel assignment changed
```

Routine autosaves should not overwhelm assistive-technology users with repetitive messages.

The design requirement is meaningful change notification, not narration of every internal event.

---

# Visual presentation and status

## 15. Color is never the sole status carrier

Statuses such as:

```text
Ready
Warning
Needs attention
Finalized
Draft
Stale
Superseded
Coverage Incomplete
```

must have textual or structural differentiation in addition to color.

For example:

```text
WARNING — Panel 06 lacks Business capacity
```

is valid even if a warning icon/color is also used.

A red/green-only readiness dashboard is not sufficient.

---

## 16. Contrast and readability

Core text, controls, focus indication, disabled-state meaning, and status presentation must be designed for sufficient contrast under ordinary display conditions.

The application should also remain understandable when:

- a user enables system high-contrast settings;
- color rendering is poor;
- a projector or venue display washes colors out;
- materials are printed in grayscale.

This requirement applies to digital and paper representations.

---

## 17. Motion

No essential state meaning may depend on animation.

Motion should not be required to understand:

```text
save success
new exception
Ranking change
Finalization success
publication state
```

Animations, if used later, should respect reduced-motion preferences and avoid unnecessary movement during concentration-heavy judging.

---

# Errors, validation, and cognitive load

## 18. Error messages must preserve context

Errors should identify:

```text
what action was attempted
what state is currently known
what did / did not happen
what the user can do next
```

For example:

```text
We saved your Draft, but could not confirm Finalization.
Your evaluation is not shown as Finalized yet.
Check status or try Finalization again.
```

is preferable to:

```text
Network error.
```

The requirement benefits every user and is particularly important for cognitive accessibility and degraded operation.

---

## 19. Validation must not erase entered work

An accessibility-related correction, validation failure, or screen reflow cannot clear previously entered Scorecard data.

If Finalization fails because a required score is missing:

```text
Draft remains intact
missing item is identified
user can navigate to it
```

The user is never forced to re-enter the entire Scorecard merely because validation occurred.

The same principle applies to Organizer configuration and paper transcription Drafts.

---

## 20. Avoid unnecessary memory burden

The application should not require a user to remember opaque identifiers or values across screens when the system already knows the context.

For example, a Judge should not need to memorize:

```text
Encounter E-041
Rubric v3
```

to return to their Scorecard.

The system can preserve those structural identities while presenting human context such as:

```text
Team 014 — Undergraduate
Your Draft
```

Similarly, Organizer recovery should surface prior state and affected source rather than expecting the Organizer to reconstruct the incident from memory.

---

## 21. Confirmation friction remains proportional to consequence

Accessibility does not justify modal confirmation for every action.

Frequent Draft score changes should remain low-friction.

Higher-consequence actions such as:

```text
Finalize Scorecard
Recuse
Invalidate Encounter
Accept Coverage exception
Finalize Competition
Publish official results
```

receive stronger confirmation and consequence explanation.

The confirmation pattern must itself be keyboard/nonvisual accessible and must not rely on color or button position to distinguish safe from destructive/high-consequence choices.

---

# Authentication, QR, and accessible entry

## 22. QR is never the only entry path

Every QR-dependent workflow requires an alternative that does not require camera access.

Examples include:

```text
short code
accessible link
Organizer-assisted lookup
manual Team / Panel selection when authorized
```

The alternative must preserve the same Identity/Participation/Access checks.

A Judge unable to operate a camera is not placed into a weaker-trust participation model.

---

## 23. Authentication must not depend on one sensory/input capability

The eventual Identity mechanism must support the accessibility posture established here.

003-H does not select OTP, magic link, passkey, federation, or another mechanism.

It requires that the chosen mechanism not make ordinary Judge or Organizer access depend exclusively on:

- recognizing a visual puzzle;
- precise gesture interaction;
- camera access;
- inaccessible timeout behavior;
- a device feature with no reasonable alternative.

Recovery must likewise preserve Identity continuity rather than encouraging duplicate Participation records when the accessible path differs from the ordinary one.

---

# Interruption architecture

## 24. Interruption is an expected state transition

Judges will be interrupted by:

- presentation discussion;
- device lock;
- incoming calls;
- accidental browser navigation;
- room movement;
- battery or connectivity problems;
- accessibility-tool context changes.

Organizers will be interrupted by concurrent operational incidents.

The application must therefore treat interruption recovery as normal workflow behavior rather than an exceptional afterthought.

---

## 25. Judge interruption contract

When a Judge returns to an interrupted evaluation, the experience should re-establish:

```text
Competition
Judge mode
Panel
Encounter
Team Alias + Division
Scorecard state
Draft persistence confidence
```

before encouraging new scoring action.

If the authoritative system knows the Draft is safely persisted:

```text
Team 014
Your Scorecard — Draft
3 of 5 Criteria scored
Resume
```

is sufficient.

If persistence is uncertain, the uncertainty must be shown truthfully.

---

## 26. Organizer interruption contract

Returning to Organizer work should preserve enough operating context to avoid accidental action in the wrong Competition or lifecycle mode.

A user returning after interruption should be able to re-orient to:

```text
Competition
Preparation / Live Operations / Reconciliation / Outcomes
selected Panel / Team / issue where safe
current source status
```

High-consequence actions should revalidate current source state at invocation rather than relying solely on the stale screen the Organizer left open.

---

## 27. Session expiry cannot silently destroy work

Security session expiry may be necessary, but it must not be designed so that a Judge loses a meaningful Draft without warning merely because the authentication session changed.

The eventual implementation must separate, as appropriate:

```text
local working preservation
server-authoritative persistence
current authentication/access state
```

without pretending they are interchangeable.

After re-verification, the Judge should recover the same logical Scorecard where policy permits.

The exact storage/security implementation remains deferred.

---

# Connectivity and persistence confidence

## 28. Connectivity state is not binary UX decoration

The application must distinguish between:

```text
online and confirmed
working locally / synchronization pending
connection degraded
server state unknown
```

where the selected architecture supports such distinctions.

A small generic Wi-Fi icon cannot substitute for meaningful authority feedback when a Judge is Finalizing or an Organizer is performing a high-consequence correction.

---

## 29. Persistence confidence vocabulary

Judge Draft experiences should be able to express states conceptually such as:

```text
Saved
Saving…
Changes pending
Changes not yet confirmed
Connection lost — Draft status explained
```

The exact words are consolidated in 003-I.

The key semantic requirement is:

> The interface must not claim stronger persistence than the system can establish.

---

## 30. Draft editing under degraded connectivity

If the implementation later supports safe local Draft continuation while disconnected, that is acceptable provided the experience clearly distinguishes:

```text
local working state
```

from:

```text
server-confirmed authoritative persistence
```

The Judge may continue thought formation where safely supported.

The system must not silently promote disconnected working state into a Finalized Scorecard.

If safe offline Draft continuation is not supported by the chosen architecture, the application must say so and route to paper/Organizer-assisted fallback rather than simulate success.

---

## 31. Finalization requires authoritative confirmation

No degraded-mode design may weaken the Finalization contract.

A Judge tapping `Finalize` while disconnected may result in:

```text
Finalization pending / not confirmed
```

but not:

```text
Finalized ✓
```

unless the authoritative state can actually be established under the selected system architecture.

Safe retry later resolves the same logical Scorecard.

---

## 32. Organizer high-consequence actions require fresh state

Actions such as:

```text
activate Competition
complete Event
invalidate Encounter
accept Coverage exception
finalize Competition
publish corrected outcome
```

must not be represented as successful when server authority is unknown.

If the system cannot establish the transition, it communicates uncertainty and supports safe recovery/retry.

A cached Organizer screen cannot become an offline authority ledger by accident.

---

# Concurrency and stale-state protection

## 33. Responsive or degraded views do not weaken stale-state checks

A narrow-screen Organizer view, offline-capable Draft, or resumed browser session must still respect current authoritative state.

Examples:

- an Amendment Draft based on Scorecard v1 cannot silently overwrite v2;
- an Organizer cannot finalize a Competition from a stale readiness screen after new evidence changed;
- a Panel reassignment view cannot overwrite a newer live roster without detecting the conflict;
- a stale public-results preview cannot be released as though it represented the current Official Outcome Revision.

The interaction should explain the new current state and require re-evaluation rather than silently winning a last-write race.

---

## 34. Duplicate submission protection

Users may retry because they are uncertain whether an action succeeded.

The experience must assume this will occur.

Retrying:

```text
start Scorecard
Finalize Scorecard
begin Encounter
capture paper evaluation
Finalize Competition
publish artifact
```

must converge on the intended logical operation where appropriate or clearly report that the state already changed.

The user should not be punished for safe retry after an ambiguous network response.

---

# Shared, replaced, and lost devices

## 35. Device is not the principal

The security/experience model remains:

```text
Identity / Participation / Access
    = principal context

device
    = interaction surface
```

A new phone does not create a new Judge.

A shared tablet does not make all Judges one identity.

A lost phone does not erase the underlying Participation or Scorecard.

---

## 36. Replacement device recovery

When a Judge changes device:

```text
reverify Identity
      ↓
recover same Competition Participation
      ↓
recover Panel context
      ↓
recover same logical Draft / finalized state
```

where current Access permits it.

The system must not respond to device loss by creating duplicate Participation or duplicate Scorecards.

---

## 37. Shared-device handoff

A Judge-visible shared-device transition must provide a clear privacy boundary:

```text
Judge A ends / leaves context
      ↓
private Judge A state cleared from exposed UI/local session context
      ↓
neutral Competition entry
      ↓
Judge B establishes own Identity
```

The next Judge must not inherit:

- prior Judge Identity;
- Team history;
- Scorecards;
- Notes;
- incomplete form fields;
- authentication state that grants Judge A's Access.

If a device cannot be safely handed off under the selected implementation, it should not be presented as safe for shared judging.

---

## 38. Lost-device response

An Organizer or Judge should be able to recover from a lost/compromised device without destroying Competition records.

Conceptually:

```text
revoke compromised session/access token
      ↓
retain Identity + Participation + Scorecard history
      ↓
reverify on replacement device
```

The exact identity/session technology remains deferred.

---

# Full degraded-mode and paper continuity

## 39. Degraded-mode levels

003-H standardizes the need to distinguish at least three operational postures conceptually:

### Normal electronic operation

Authoritative services are available and state can be confirmed normally.

### Partial degradation

Some electronic work can continue while synchronization/availability is impaired.

Examples may include:

```text
one Judge cannot connect
one Panel changes to paper
Organizer dashboard delayed
artifact generation unavailable
```

### Full digital fallback

Electronic judging cannot be trusted for live operation and the event uses paper continuity.

These are experience/operational postures, not Competition lifecycle states.

---

## 40. No fake offline authority

The system must not create an insecure local-only version of authority merely to keep screens appearing functional.

If Identity, Panel membership, Rubric basis, or Finalization cannot be trusted electronically, the correct fallback may be:

```text
Organizer-controlled physical assignment
      +
identified paper Rubric / Scorecard
      +
physical provenance
      +
later reconciliation
```

rather than pretending that a disconnected browser established authoritative Competition state.

---

## 41. Paper fallback preserves evaluation semantics

Full fallback remains:

```text
same Team Alias + Division
same authoritative Rubric Version
same Judge
same Encounter context
same Criterion meanings
same score domains
same Notes semantics
        ↓
paper capture channel
```

When electronic operation returns:

```text
paper source
      ↓
capture Draft
      ↓
verification
      ↓
same logical Scorecard
```

The fallback changes capture medium, not judging meaning or weight.

---

## 42. Paper must be accessible too

Paper is a first-class accessibility/continuity path, but paper itself can introduce accessibility barriers.

Paper materials should therefore be designed for:

- readable typography;
- clear Criterion grouping;
- sufficient writing space;
- non-color-only status/instructions;
- unambiguous score choices;
- exact Team Alias/Division context;
- exact Rubric Version;
- large-print or other practical adapted representations where needed.

If paper is not usable for a particular Judge, Organizer-assisted or other accessible electronic/physical accommodation must preserve that Judge's authorship rather than converting the Organizer into the evaluator.

---

## 43. Accessibility fallback cannot change authorship

If a Judge needs assistance entering scores because of a disability or device limitation, assistance must preserve semantic authority.

For example:

```text
Judge makes evaluation
Organizer/assistant helps capture it
```

must remain distinguishable from:

```text
Organizer decides evaluation
```

The same author-versus-capture distinction used for paper provides the conceptual basis for accessible assisted capture if such a workflow is later required.

The exact accommodation protocol remains future design/policy work.

---

# Organizer degraded-mode command experience

## 44. Operational status must express confidence

During service degradation, Organizer views should distinguish confirmed from uncertain information.

For example:

```text
Panel 04
Last confirmed state: Encounter E-041 Open
Updated 2 minutes ago
Live synchronization unavailable
```

is better than showing an apparently real-time state with no indication that updates have stopped.

Exact timestamping/transport is an implementation concern; confidence in freshness is an experience requirement.

---

## 45. Incident response should preserve source state

If the Organizer switches a Panel to paper, the action should identify what is changing operationally without mutating Scorecards merely to make the dashboard look clean.

Conceptually:

```text
Panel 04 electronic judging degraded
      ↓
Organizer declares paper fallback for upcoming/current work
      ↓
identified paper sources used
      ↓
electronic Drafts preserved
      ↓
later duplicate/convergence reconciliation
```

The incident response is operational state, not authority to delete ambiguous electronic work.

---

## 46. Degraded dashboard should prioritize recovery work

When connectivity returns, the Organizer should be shown what requires reconciliation rather than assuming everything synchronized correctly.

Examples:

```text
3 local Drafts need synchronization confirmation
2 paper forms collected
1 Scorecard has electronic + paper artifacts
1 Encounter completion state needs refresh
```

The exact local/offline implementation may vary, but recovery must be explicit and source-oriented.

---

# Export, publication, and responsive/accessibility requirements

## 47. Accessible external representations

Where an Export is intended for digital human consumption, its representation should preserve an accessible structure appropriate to its format rather than relying solely on visual positioning.

For example, a results document should not communicate Rank solely through spatial placement or color.

A public webpage or digital artifact should preserve meaningful headings, reading order, labels, and text alternatives where applicable.

The exact PDF/document technology is deferred, but accessibility is part of the Export acceptance criteria rather than merely a website concern.

---

## 48. Print and grayscale resilience

Print artifacts must remain understandable when:

- printed in grayscale;
- copied;
- printed on ordinary office hardware;
- viewed under poor venue lighting.

Critical distinctions such as:

```text
Draft / Finalized
Current / Stale
Team / Division
score selections
instructions
```

cannot rely solely on subtle color differences.

---

## 49. Publication under degraded infrastructure

If public publication infrastructure is unavailable, the Organizer should not be forced to weaken Finalization semantics.

The Competition may remain:

```text
Finalized
Official Outcome Revision current
Publication pending
```

until the release mechanism is available.

Likewise, a failed publication attempt must not be presented as publicly released merely because the artifact was generated successfully.

Generation, release, and observed external availability remain distinct concerns.

---

# Timing, timeouts, and live-event pressure

## 50. Timing behavior must not create inaccessible failure

The system may eventually use session timeouts or event timing, but interaction time limits must not silently destroy Draft work or make high-consequence actions impossible for users who require more time.

The presentation schedule can continue independently of an individual Judge's unfinished Scorecard, as established in 003-C.

Therefore accessibility does not require forcing the entire Panel to wait for one Judge, and event pace does not justify silently finalizing or discarding that Judge's work.

---

## 51. Session timeout communication

Where security requires session expiry, the experience should warn appropriately when useful, preserve safe working state where architecture permits, and support re-verification into the same Participation/Scorecard context.

A timeout must not transform:

```text
Draft
```

into:

```text
Finalized
```

or:

```text
deleted
```

as a side effect.

---

# Cross-role accessibility and resilience invariants

## 52. 003-H invariants

003-H establishes the following interaction-level invariants:

1. Accessibility changes representation or input method, not domain semantics.
2. Accessible paths do not broaden disclosure or weaken authorization.
3. The core Judge journey is fully usable on a small touch device.
4. Organizer workflows may use wide-screen density but retain coherent narrow-screen summary → issue → detail access.
5. Essential actions never require hover, camera use, fine pointer precision, drag-only interaction, or one device orientation.
6. QR-dependent flows always have a non-camera alternative.
7. Color alone never communicates essential state.
8. Meaningful structure, labels, focus order, and keyboard operation are required across core journeys.
9. Dynamic persistence/authority changes must be perceivable without excessive notification noise.
10. Text enlargement and responsive reflow cannot hide essential judging or recovery controls.
11. Validation failures preserve entered work.
12. Errors identify known state and recovery action rather than only reporting technical failure.
13. Draft score changes remain low-friction; confirmation is concentrated at high-consequence boundaries.
14. Interruption recovery re-establishes Competition, role, resource, and authority context before consequential continuation.
15. Session expiry does not silently destroy, finalize, or duplicate Judge work.
16. Persistence confidence must never be overstated.
17. Disconnected working state, if supported, remains distinguishable from server-confirmed authoritative state.
18. Finalization requires authoritative confirmation; offline ambiguity cannot be displayed as Finalized.
19. Organizer high-consequence actions cannot succeed from unknown/stale authority state.
20. Stale-base conflicts are surfaced rather than silently overwritten.
21. Safe retries converge on the intended logical action and do not create duplicate Scorecards/Encounters/outcomes.
22. Device identity never substitutes for human Identity/Participation.
23. Replacement devices recover the same Participation/Scorecard rather than creating duplicates.
24. Shared-device handoff clears prior private Judge context before the next Identity enters.
25. Lost-device recovery revokes compromised session state without deleting Competition records.
26. Normal, partial-degradation, and full-paper postures share one Competition model.
27. Degraded operation never creates fake local authority merely to make the UI appear successful.
28. Paper fallback preserves Team, Encounter, Judge, Rubric, score, Note, and weight semantics.
29. Paper/accommodation assistance preserves Judge authorship even when capture actor differs.
30. Organizer degraded-mode views expose freshness/confidence rather than displaying stale data as real time.
31. Recovery after degradation surfaces unsynchronized/duplicate/paper work for reconciliation.
32. Accessible Export/print representations preserve meaningful structure and do not rely on color alone.
33. Publication infrastructure failure never weakens Finalization or falsely claims public release.
34. Timeouts/event pace cannot silently finalize or discard incomplete Judge evaluations.

---

## 53. Explicitly deferred implementation choices

003-H intentionally does not choose:

- React or another front-end framework;
- CSS/component system;
- exact breakpoints;
- specific target pixel dimensions;
- native versus web application;
- service workers;
- IndexedDB/local storage or another Draft persistence technology;
- optimistic/offline synchronization algorithm;
- real-time transport;
- conflict-resolution protocol;
- authentication provider;
- session/token mechanism;
- device registration model;
- PWA installation behavior;
- PDF accessibility library;
- OCR;
- printer integration;
- monitoring/observability stack;
- specific AWS connectivity/offline infrastructure.

Later architecture must satisfy the behavior and confidence contracts defined here rather than using a technology choice to redefine them.

---

# 54. Exit position

003-H establishes one cross-channel interaction architecture:

```text
AUTHORITATIVE COMPETITION MODEL
             ↓
      role + Access context
             ↓
┌──────────────────────────────────────────────┐
│ ACCESSIBLE REPRESENTATION                   │
│                                              │
│ touch / keyboard / screen reader            │
│ small / wide viewport                       │
│ normal / interrupted / degraded connection  │
│ personal / changed / shared device          │
│ electronic / paper                          │
└──────────────────────────────────────────────┘
             ↓
     truthful confidence state
             ↓
 safe action / recovery / fallback
             ↓
SAME AUTHORSHIP + AUTHORITY + EVIDENCE MEANING
```

The governing principle is:

> **The system may adapt interaction, density, device, and capture channel aggressively; it may not adapt away the meaning of the Competition.**

With accessibility/resilience applied across the actor journeys, Phase 003 can now move to **003-I — Cross-Cutting Status, Feedback, Privacy, Disclosure & Recovery Patterns**.

003-I should consolidate the common interaction vocabulary that has accumulated across the phase—Draft/Finalized/uncertain, Ready/Warning/Needs attention, Current/Stale/Superseded, private/public disclosure, confirmation levels, destructive versus corrective actions, and standard recovery messaging—so the final Phase 003 exit review can test one coherent experience language rather than ten locally invented vocabularies.
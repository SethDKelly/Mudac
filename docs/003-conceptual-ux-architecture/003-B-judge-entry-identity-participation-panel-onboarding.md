# 003-B — Judge Entry, Identity, Participation & Panel Onboarding

Status: **Complete**

## 1. Purpose

003-B defines the Judge's event-day entry experience from first arrival through a trustworthy **ready-to-judge** state.

It translates the Phase 002 Identity, Participation, Access, Panel, and Competition specifications into an actor-centered experience without choosing an authentication provider, account model, route structure, mobile framework, QR technology, or AWS service.

The governing objective is:

> A volunteer Judge, including a first-time participant arriving on the day of the event, should be able to establish trustworthy event participation, confirm the information needed for fair Panel formation, join the correct Panel context, and become ready to judge with minimal administrative friction.

The experience must preserve an equally important constraint:

> Low friction must not collapse Identity, Participation, Panel assignment, or Access into possession of a QR code or knowledge of a short event code.

---

## 2. Canonical onboarding journey

The primary flow is:

```text
Arrive / open event entry
        ↓
Competition context resolved
        ↓
Identity established or reverified
        ↓
Judge Participation established/confirmed
        ↓
Judge profile/expertise confirmed
        ↓
Check in
        ↓
Panel assignment resolved
        ↓
Panel context confirmed
        ↓
Ready to Judge
```

The application should not force every Judge through identical screens when some of these facts are already known.

The journey is state-driven rather than page-driven.

For example, a returning pre-registered Judge may move quickly through:

```text
recognize Identity
    ↓
reverify
    ↓
confirm current-event information
    ↓
check in
```

while a first-time walk-in Judge may need to establish more information.

---

## 3. Entry mechanisms are interchangeable accelerators

A Judge may enter the experience through mechanisms such as:

```text
Competition QR
short event code
email/message link
Organizer-provided link
manual Competition selection where appropriate
```

These are navigation mechanisms.

They may establish:

```text
intended Competition
possibly intended Panel
possibly intended event entry flow
```

They do not establish:

```text
human Identity
Judge Participation
evaluation authority
Panel membership by themselves
```

The experience contract is therefore:

```text
entry mechanism
      ↓
requested context
      ↓
Identity / Participation / Access resolution
      ↓
authorized destination
```

A Judge must always have a non-camera alternative to QR-based entry.

---

## 4. Competition context should be obvious immediately

A Judge arriving from a link or code should be able to confirm that they are joining the correct event before providing meaningful personal information.

The experience should clearly identify the Competition using safe event information such as:

```text
MinneMUDAC 2026
October 17, 2026
St. Catherine University
```

The exact information is Competition content.

The Judge should not need to infer context from a generic login page or opaque URL.

If a stale link points to a historical Competition, the system should say so rather than silently placing the Judge into the wrong event.

---

## 5. Identity establishment

The Judge entry flow should ask only for the Identity work required by the current situation.

Conceptually there are two common paths.

### First-time / unrecognized Judge

```text
Competition entry
      ↓
establish minimum human Identity
      ↓
perform required verification
      ↓
continue into current Competition Participation
```

### Returning / recognized Judge

```text
Competition entry
      ↓
recognize prior Identity
      ↓
lightweight re-verification
      ↓
new current Competition Participation
```

A returning Judge does **not** resume their prior year's Participation.

The experience should reinforce continuity without implying permanent authority.

---

## 6. No enterprise-account ceremony by default

The Judge experience should feel like event check-in rather than enterprise account provisioning.

The application should avoid unnecessary requirements such as:

```text
choose permanent username
create profile biography
configure unrelated preferences
navigate account administration
```

unless a later selected identity mechanism genuinely requires them.

The Judge's cognitive goal is:

> I am here to judge this Competition.

The identity experience should support that goal rather than becoming the product itself.

---

## 7. Judge Participation is current-event specific

Once Identity is sufficiently established, the experience resolves one current Competition Participation in Judge capacity.

The Judge should be able to understand the event-scoped relationship in human terms such as:

```text
You're judging MinneMUDAC 2026
```

rather than being exposed to implementation language such as:

```text
JudgeParticipation #7e28...
```

Participation state determines what onboarding remains.

Typical experience states include conceptually:

```text
Not enrolled
Enrolled / registered
Checked in
Active / ready for event operation
Completed
Withdrawn / unavailable
```

The precise persisted state model remains governed by the Phase 002 Participation specification.

---

## 8. Pre-registered and walk-in Judges

The experience should support both without creating different Judge semantics.

### Pre-registered

The system may already know:

```text
Identity association
expected Judge Participation
previously declared expertise/background
```

The Judge confirms/reverifies current information and checks in.

### Walk-in

An Organizer-approved event may allow a new Judge to establish Identity and create current Competition Participation at the event.

The system must not treat a walk-in as less legitimate once the required verification and Participation conditions are satisfied.

Whether walk-ins are permitted is Competition policy/Organizer authority rather than a hard-coded product assumption.

---

## 9. Current-event Judge profile

Panel formation needs enough information to understand the Judge's perspective.

The onboarding experience should collect or confirm event-scoped information such as:

```text
Expertise / perspective
    Academic
    Business
    Technical
    other Competition-defined values

optional current professional/background information
optional affiliation information where operationally useful
conflict-related information where Competition policy requires it
```

The application should collect only information that serves event operation.

A Judge's permanent Identity should not become a dumping ground for event-specific professional metadata.

---

## 10. Expertise confirmation

Returning Judge expertise must not silently carry forward as unquestioned current truth.

The experience may pre-populate prior values for convenience, but the Judge should confirm or update them for the current Competition.

For example:

```text
How would you describe the perspective(s) you can bring today?

[x] Academic
[x] Technical
[ ] Business
```

This is preferable to forcing the Judge to understand Panel composition terminology.

Expertise remains plural.

It still grants no special system authority.

---

## 11. Composition capacity is not an onboarding self-declaration

A Judge may say:

```text
I have Academic and Technical expertise
```

but the Organizer/Panel configuration may later use them to satisfy:

```text
Academic capacity
```

on a specific Panel.

Therefore onboarding collects expertise.

It should not normally ask:

```text
Which Panel composition seat do you want to occupy?
```

Composition capacity belongs to Panel assignment/Organizer operation.

The Judge can later be shown the capacity they are filling if useful.

---

## 12. Check-in

Check-in means:

> The Judge is physically/operationally present and available for today's Competition work.

It is distinct from:

```text
Identity exists
Judge Participation exists
```

A Judge may have been registered for weeks while not yet present.

The experience should make check-in a lightweight, explicit transition.

Possible entry mechanisms may accelerate it, but it must remain attributable to the correct Participation.

---

## 13. Check-in status should be recoverable

If the Judge closes the browser, changes device, or loses connectivity after successful check-in, they should not have to create another Participation.

After re-establishing Identity:

```text
same Identity
    ↓
same current Competition Participation
    ↓
existing checked-in state
```

should be recovered.

Device continuity is not Participation continuity.

---

## 14. Arrival before Competition activation

Judges may arrive before the Competition reaches Active.

The application should allow appropriate onboarding work such as:

```text
verify Identity
confirm Judge Participation
confirm expertise
check in
view safe event information
receive Panel assignment when available
```

while clearly communicating:

```text
Judging has not opened yet
```

The Judge cannot begin an official Encounter merely because onboarding is complete.

This keeps Competition lifecycle semantics intact.

---

## 15. Panel assignment states

After check-in, the Judge may be in one of several operational states:

### Panel assigned

```text
Panel 07
Academic capacity
Room 210
```

### Awaiting Panel assignment

```text
You're checked in.
An Organizer is assigning Panels.
```

### Panel assignment needs attention

Examples:

```text
Panel was changed
assignment conflicts with another current assignment
Organizer asked Judge to report to a different Panel
```

The Judge should not be forced to navigate the Panel catalog to resolve these situations.

---

## 16. Panel assignment authority

The baseline assumes the Organizer controls substantive Panel membership because Panel composition is a fairness/operations concern.

A Judge may **confirm** or **claim an Organizer-intended Panel context** through an approved mechanism, but should not ordinarily self-reassign between Panels simply because another Panel code is known.

This preserves the distinction:

```text
Panel code / QR
    identifies requested Panel context

Organizer-governed Panel membership
    establishes intended judging grouping
```

A Competition may later permit more self-service under explicit policy, but possession of a Panel code never overrides Panel membership authority.

---

## 17. Panel QR / join code experience

A practical day-of-event pattern may be:

```text
Organizer forms Panel 07
        ↓
physical table/room shows Panel 07 QR
        ↓
verified checked-in Judge scans
        ↓
application resolves Panel 07
        ↓
checks Judge's intended/current membership
        ↓
confirms or requests allowed join
```

Possible outcomes should be explicit:

```text
You're on Panel 07 — continue

You're assigned to Panel 04 — ask an Organizer before switching

You're not yet assigned — this Panel requires Organizer confirmation
```

The system should not silently move the Judge.

---

## 18. Panel confirmation

Once assigned, the Judge should receive a compact Panel context confirmation.

Useful information may include:

```text
Panel label
current fellow Judges
assigned composition capacity, if useful
room/location or logistical instructions
current judging readiness
```

It must not include peer Scorecards, peer Notes, Team Aggregate, or standings.

The Judge should have an obvious way to report:

```text
This is not my Panel
A listed Judge is missing
I need to recuse from a Team
```

without requiring them to understand the underlying data model.

---

## 19. Ready-to-judge is a derived experience state

`Ready to Judge` should not be another Concept or arbitrary flag.

It is derived from conditions such as:

```text
Identity sufficiently verified
+
current Judge Participation valid
+
Judge checked in
+
required current-event profile/expertise complete
+
current Panel membership resolved
+
required Access active
+
Competition lifecycle permits judging
```

Panel composition may be fully compliant or operating under an explicit Organizer exception according to Competition policy.

The Judge experience should communicate the blocking reason when readiness is not satisfied.

---

## 20. Example readiness states

### Waiting for event start

```text
You're checked in and assigned to Panel 07.
Judging opens at 9:30 AM.
```

### Waiting for Panel assignment

```text
You're checked in.
Panel assignment is still in progress.
```

### Ready

```text
Panel 07
Ready to Judge
```

### Needs Organizer help

```text
Your Panel assignment needs attention.
Please see an Organizer.
```

The experience should prefer one clear next action over exposing raw state codes.

---

## 21. Judge mode for dual-role people

A person may hold both Organizer and Judge Participations in the same or different Competition contexts.

Entering Judge onboarding must establish explicit Judge mode.

The experience should never simply hide a few Organizer buttons while leaving Organizer-sensitive data in surrounding context.

Conceptually:

```text
Organizer mode
      ↓ explicit switch
Judge mode
      ↓
Judge-safe disclosure context
```

Judge mode should remove or mask Organizer-only Team identity, scoring, Ranking, exception, and administrative information.

Switching back later requires another explicit context change.

---

## 22. Judge-facing Team names do not enter onboarding

The optional `teamName` attribute introduced by 002-A1 has no role in Judge Identity, Participation, check-in, or Panel formation by default.

It does not replace Team Alias and cannot be used as an access credential.

If a Competition later permits Judge-visible Team names during judging, that is a separate disclosure decision handled in the Judge Encounter experience and cross-cutting disclosure architecture.

---

## 23. Shared / loaner device behavior

The onboarding experience must support a shared or Organizer-provided device without carrying one Judge's private context into another Judge's session.

A clear handoff should conceptually perform:

```text
end current Judge access context
        ↓
clear locally exposed private Judge state
        ↓
return to neutral Competition entry
        ↓
next Judge establishes Identity
```

The next Judge must not see:

```text
prior Judge name
prior Scorecards
prior Notes
prior Team history
```

The precise session/local-storage mechanisms remain implementation choices.

---

## 24. Lost or changed device

A new device does not create a new Judge.

The recovery experience should be:

```text
re-establish / reverify Identity
        ↓
recover current Competition Participation
        ↓
recover Panel / check-in context
```

If a device is reported lost, compromised sessions should be revocable without revoking the Judge's underlying Participation.

This distinction should remain understandable to Organizers during live operations.

---

## 25. Event Completed boundary

Ordinary Judge onboarding is a live-event workflow.

After `Event Completed`, the normal experience should not invite a Judge to enter ordinary judging mode or browse historical private evaluation data.

If a post-event Scorecard amendment is authorized, the Judge enters through a different narrow correction path:

```text
Organizer authorization
      ↓
Judge re-verification
      ↓
temporary specific Scorecard Access
```

That is not a revival of normal event onboarding.

---

## 26. Accessibility requirements applied to onboarding

The entry/onboarding journey must not depend on:

```text
camera access
QR scanning
fine motor precision
color alone
hover
perfect vision
```

At minimum the conceptual experience requires:

- keyboard-operable entry;
- text alternatives for encoded/visual mechanisms;
- readable labels and status text;
- forgiving touch targets;
- logical focus/reading order;
- sufficient error explanation;
- ability to increase text size;
- an Organizer-assisted path when personal-device use is not workable.

Detailed cross-journey requirements remain for 003-H.

---

## 27. Degraded-network posture

003-B does not choose an offline authentication architecture.

It establishes the behavior requirement:

> The system must never claim that Identity, check-in, Panel membership, or Access has been authoritatively established when the required authoritative system state cannot actually be confirmed.

If entry services are unavailable, the operational fallback may require Organizer-assisted manual check-in and paper judging under the 002-H continuity model rather than inventing an insecure local-only Judge authority.

When digital operation returns, recovery reconciles the Judge to the existing current Participation rather than creating duplicates.

---

## 28. Error language

Onboarding errors should explain both the current known state and the next recovery action.

Prefer:

```text
We found your Judge registration, but could not confirm check-in.
Try again, or ask an Organizer to check you in.
```

rather than:

```text
Something went wrong.
```

Likewise:

```text
You're assigned to Panel 04, not Panel 07.
Please confirm with an Organizer before switching.
```

is better than a generic access-denied page.

---

## 29. Organizer visibility into onboarding state

Although the detailed Organizer live-operations experience belongs to 003-E, 003-B establishes the Judge-side states that Organizers need to observe.

Useful operational projections include:

```text
Registered / expected
Checked in
Available
Awaiting Panel
Panel assigned
Ready to judge
Needs attention
Unavailable / withdrawn
```

These are experience/derived states over Participation, Access, and Panel state, not another lifecycle concept.

---

## 30. Data minimization

The Judge onboarding experience should collect only information needed for:

- Identity continuity and recovery;
- current Competition Participation;
- Panel composition;
- conflict/operational needs;
- necessary communication where Competition policy requires it.

It should not create a broad permanent volunteer profile merely because one could be useful someday.

Any future cross-event volunteer directory or persistent profile should be designed explicitly rather than emerging accidentally from onboarding fields.

---

## 31. Primary Judge onboarding success test

A first-time volunteer should be able to arrive with a phone and, with minimal instruction:

1. identify the correct Competition;
2. establish/verify who they are;
3. establish Judge Participation;
4. provide/confirm relevant expertise;
5. check in;
6. understand whether a Panel is assigned;
7. confirm the correct Panel context;
8. know whether they are ready to judge;
9. know exactly what to do if they are not ready;
10. enter the judging experience without seeing prohibited Team identity or scoring information.

A returning Judge should accomplish the same outcome with fewer steps while still receiving a new current-event Participation.

---

## 32. Canonical Judge entry experience

```text
ENTRY
  │
  ├── QR / link / code / manual path
  │
  ▼
COMPETITION CONTEXT
  │
  ▼
IDENTITY
  │
  ├── establish first-time
  └── recognize + reverify returning
  │
  ▼
JUDGE PARTICIPATION
  │
  ▼
CURRENT-EVENT PROFILE
  │
  ├── expertise
  └── required operational information
  │
  ▼
CHECK-IN
  │
  ▼
PANEL CONTEXT
  │
  ├── assigned
  ├── awaiting assignment
  └── needs Organizer attention
  │
  ▼
READY TO JUDGE
```

The experience hides the underlying concept complexity while preserving every important authority boundary.

---

## 33. 003-B invariants

1. QR/link/code possession never establishes Judge authority by itself.
2. Returning Identity never implies returning Competition Participation.
3. Walk-in and pre-registered Judges converge on the same valid Participation semantics.
4. Judge expertise is confirmed for the current Competition.
5. Expertise and Panel composition capacity remain distinct.
6. Check-in is distinct from Identity and registration.
7. Device continuity is not Participation continuity.
8. A Judge is not ready merely because they successfully authenticated.
9. Panel membership remains Organizer-governed by default.
10. A Panel code does not silently reassign a Judge.
11. Ready-to-Judge is derived from authoritative conditions, not an arbitrary manual flag.
12. Judge mode must prevent Organizer-sensitive context leakage for dual-role people.
13. Team Name does not replace Team Alias or influence Judge onboarding.
14. Ordinary Judge onboarding closes after Event Completed.
15. Post-event correction access is a separate narrow workflow.
16. Shared devices clear prior Judge private context.
17. Degraded connectivity never causes the UI to falsely claim authoritative check-in/access state.
18. Onboarding failures expose recovery action rather than generic error only.
19. Personal-device/QR use always has an accessible alternative.
20. Judge onboarding collects only information necessary for current Competition operation and Identity continuity.

---

# 003-B Exit Position

003-B establishes a low-friction but authority-preserving path from arrival to judging:

```text
Identity
    ↓
current Judge Participation
    ↓
current-event expertise/profile
    ↓
check-in
    ↓
Organizer-governed Panel context
    ↓
derived readiness
    ↓
Judge evaluation experience
```

No new Concept is required.

The principal UX finding is that **"logged in" is not a sufficient Judge state**. The application must distinguish verification, Participation, check-in, Panel assignment, Competition lifecycle, and Access while presenting them as one understandable event-day journey.

This gives 003-C a precise starting point:

> A Judge enters the evaluation experience already established in the correct Competition, Judge mode, and Panel context, with authoritative readiness to begin or resume a specific Judging Encounter.

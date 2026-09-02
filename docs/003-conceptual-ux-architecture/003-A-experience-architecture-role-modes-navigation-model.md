# 003-A — Experience Architecture, Role Modes & Navigation Model

Status: **Complete**

## 1. Purpose

003-A defines the overall experience architecture through which MUDAC's specified Concepts will be exposed to human actors.

It does not design individual screens or components.

It establishes:

- actor-centered experience modes;
- active Competition context;
- Participation/role context;
- top-level task regions;
- lifecycle-sensitive navigation;
- current versus historical information architecture;
- privacy-safe context switching;
- cross-device/context continuity expectations;
- the boundary between Judge, Organizer, and technical Administrator experiences.

The central principle is:

> The application should be organized around what an actor is trying to accomplish in the current Competition context, not around one navigation item per database entity or Concept.

Concepts remain the behavioral foundation. The information architecture composes them into coherent work.

---

## 2. Context stack

Every authenticated/verified experience should be understandable through an explicit context stack:

```text
Identity
   ↓
Participation / role mode
   ↓
Competition
   ↓
role-specific operational context
   ↓
current task / artifact
```

Examples:

### Judge

```text
Identity: J-041
Role mode: Judge
Competition: 2026 MUDAC
Panel: Panel 07
Current Encounter: Team 014
Current task: Scorecard
```

### Organizer

```text
Identity: O-006
Role mode: Organizer
Competition: 2026 MUDAC
Operational context: Live judging
Current task: Coverage exception for Team 014
```

This context should remain recoverable and visible enough that users do not accidentally perform work in the wrong Competition or role.

---

## 3. Identity is not the navigation root

The application should not assume that one Identity corresponds to one permanent role.

A person may have:

```text
Competition A → Organizer Participation
Competition B → Judge Participation
```

or, exceptionally, separate Participations in the same Competition.

Therefore the experience root is not:

```text
User = Judge
```

It is:

```text
Identity
   ↓
select/resume valid Participation context
   ↓
enter role-specific experience
```

Authentication may establish Identity, but Participation establishes the Competition-specific experience.

---

## 4. Explicit role modes

Judge and Organizer experiences should remain explicit **modes**, not a single blended navigation tree with hidden permission differences.

Conceptually:

```text
Identity
   ├── Judge mode
   └── Organizer mode
```

If one Identity has both Participations in the same Competition, switching mode should be deliberate and visibly acknowledged.

The application should not allow subtle role leakage where an Organizer who is temporarily judging continues to see:

- institution identity;
- peer Scorecards;
- live standings;
- Organizer-only exceptions;

inside the Judge experience.

Mode establishes the disclosure posture as well as the available tasks.

---

## 5. Judge experience architecture

The Judge experience should remain deliberately narrow.

Its primary experience regions are conceptually:

### Event context

Answers:

- What event am I judging?
- What do I need to know operationally?
- Is judging currently open?

### Panel context

Answers:

- Which Panel am I on?
- Who is judging with me?
- What perspective/capacity am I filling?

### Current judging

Answers:

- Which Team are we evaluating now?
- What Rubric applies?
- What remains incomplete on my Scorecard?
- Is my work saved/finalized?

### My judging history

During ordinary event access, answers:

- Which Teams have I evaluated?
- Which Scorecards are Draft or Finalized?
- Do I need to finish or amend something?

This is an operational history, not a permanent Judge archive.

At Event Completed, ordinary access to private Scorecards/Notes/history disappears according to 002-B.

---

## 6. Judge navigation principle

Judge navigation should optimize for the next judging action, not expose the whole domain model.

A Judge should not need top-level navigation items such as:

```text
Teams
Encounters
Rubrics
Scorecards
Participations
```

because those are conceptual/domain boundaries rather than Judge tasks.

A better conceptual flow is:

```text
Event / Panel context
        ↓
Current Team / Encounter
        ↓
My Scorecard
        ↓
My completed/incomplete judging
```

The precise visual labels are deferred.

---

## 7. Organizer experience architecture

Organizer work spans a much broader lifecycle.

The top-level experience should therefore be organized around **Competition operating modes**, not a flat list of domain objects.

The canonical Organizer experience regions are:

### Competition preparation

Supports:

- Competition details;
- Divisions;
- Teams;
- Aliases;
- Rubrics;
- Evaluation Policy;
- Awards;
- Judge enrollment/readiness;
- Panel preparation;
- Export/print preparation;
- Ready-state assessment.

### Live operations

Supports:

- Judge check-in/availability;
- Panel composition;
- Encounter progress;
- outstanding Scorecards;
- Team Coverage trajectory;
- paper fallback/capture backlog;
- operational exceptions;
- participant reassignment/recusal handling.

### Reconciliation

Supports:

- unresolved Scorecards;
- paper verification;
- invalidated/replacement Encounters;
- Coverage exceptions;
- Rubric compatibility;
- Division corrections;
- scoring diagnostics;
- ties;
- ranking readiness.

### Outcomes

Supports:

- Division Rankings;
- rank-derived Award candidates;
- discretionary Awards;
- Finalization readiness;
- Official Outcome Revisions;
- post-finalization correction review.

### Materials / external representations

Supports:

- printable Rubrics;
- paper judging forms;
- event materials;
- Panel materials;
- publication/ceremony outputs;
- historical Export references.

These are experience regions, not new Concepts.

---

## 8. Lifecycle-sensitive Organizer emphasis

The Organizer information architecture should adapt emphasis according to Competition lifecycle while preserving access to legitimate historical/configuration information.

### Draft

Primary emphasis:

```text
Preparation
Readiness issues
```

### Ready

Primary emphasis:

```text
Final pre-event readiness
Judge/Panel operational preparation
Materials
Activation
```

### Active

Primary emphasis:

```text
Live Operations
Exceptions
Encounter/Scorecard progress
Coverage trajectory
```

Preparation/configuration remains available where allowed, but consequential changes receive stronger framing.

### Event Completed

Primary emphasis:

```text
Reconciliation
Coverage
Ranking readiness
Awards
Finalization readiness
```

### Finalized

Primary emphasis:

```text
Official Outcome
Exports/publication
Historical evidence/provenance
exceptional correction
```

This does not require changing the entire navigation tree at each state. It establishes which work should be foregrounded.

---

## 9. Competition context

An Organizer may eventually operate multiple Competitions over time.

Therefore the active Competition must be a first-class experience context.

The application should make it difficult to accidentally perform an action in the wrong Competition.

Consequential actions should always have an unambiguous Competition context, especially:

- Division/Team changes;
- Judge/Panel changes;
- Rubric/Policy changes;
- paper capture;
- Coverage exceptions;
- Award conferral;
- Finalization;
- publication.

Historical Competitions should remain clearly distinguishable from the current/live Competition.

---

## 10. Historical Competition experience

A Finalized past Competition should not look like an ordinary editable live Competition.

The default experience posture becomes:

```text
inspect
trace
export
review official outcome
```

rather than:

```text
edit freely
```

Legitimate post-finalization correction is entered through a clearly exceptional path.

This preserves controlled finality at the experience level.

---

## 11. Current versus historical state presentation

Phase 002 established many cases where current and historical truth differ.

The information architecture must not collapse them.

For example:

```text
Team current Division:
Graduate

Encounter E-014 presented Division:
Undergraduate
```

or:

```text
Panel current membership:
J-A, J-B, J-D

Encounter participants:
J-A, J-B, J-C
```

or:

```text
Scorecard current Version:
v2

Historical Version:
v1
```

The experience should default to the state appropriate to the user's task while making historical basis available where needed.

A user should never have to infer whether a displayed value is:

- current configuration;
- historical snapshot;
- authoritative current Version;
- superseded Version.

---

## 12. Organizer situational awareness

Organizer entry into a Competition should answer:

> What requires my attention now?

before demanding navigation through every domain object.

The experience may therefore surface derived operational summaries such as:

```text
3 Panels not composition-ready
8 outstanding Scorecards
2 Teams Coverage-incomplete
4 paper forms awaiting verification
1 unresolved Rubric compatibility issue
1 Division tie unresolved
2 required Awards pending
```

This is an experience projection over the domain model, not a `Dashboard` Concept.

The Organizer can then drill into the Concepts/evidence responsible for each condition.

---

## 13. Drill-down architecture

Operational summaries should always support movement toward source evidence.

Examples:

```text
Coverage incomplete
    ↓
Team
    ↓
Encounters
    ↓
effective obligations / Scorecards
```

```text
Rank changed
    ↓
Team Aggregate
    ↓
eligible Scorecards
    ↓
Scorecard Version
    ↓
Criterion responses
```

```text
Award candidate changed
    ↓
current Rank
    ↓
Evaluation Policy / corrected source
```

This preserves explainability in the user experience rather than only in backend data relationships.

---

## 14. Avoid entity-first navigation as the only model

Organizers may still need searchable/listable collections such as:

- Teams;
- Judges;
- Panels;
- Rubrics;
- Awards.

However, these should support tasks rather than define the entire application structure.

A flat navigation such as:

```text
Competitions
Teams
Divisions
Judges
Panels
Encounters
Rubrics
Scorecards
Awards
Exports
```

would expose the domain model but poorly represent live Competition work.

Phase 003 instead favors a hybrid:

```text
lifecycle/task-oriented experience regions
        +
contextual access to domain collections/details
```

---

## 15. Cross-context navigation safety

Changing Competition or role context while unsaved/uncommitted work exists must be safe.

Examples include:

- Judge has unsynchronized Draft changes;
- Organizer is midway through paper capture;
- Organizer is composing an exceptional correction;
- Organizer has not completed a high-consequence confirmation.

The system should never silently discard such work merely because the user changes context.

The exact autosave/navigation mechanism is deferred, but the experience contract is:

> Context switching cannot silently destroy meaningful working state.

---

## 16. Deep-link/context restoration principle

The eventual application may use links, QR codes, bookmarks, or notifications that attempt to open a specific Competition resource.

The conceptual behavior should be:

```text
requested destination
        ↓
Identity established/reverified if needed
        ↓
Participation context resolved
        ↓
Access checked
        ↓
resource opened in correct Competition/role mode
```

A URL/code itself never bypasses context or authority.

If the user's current mode is inappropriate, the application should require or offer an explicit valid context switch rather than leaking resource contents.

---

## 17. Judge mobile priority versus Organizer broader workspace

The overall experience architecture should acknowledge different device priorities.

### Judge

Primary environment:

```text
personal smartphone
portrait touch interaction
short task loops
interruptions
```

### Organizer

Primary environment may include:

```text
laptop / desktop
larger tablet
shared operational display
```

but Organizer critical live-event actions should remain usable when moving around the venue.

This does not mean building two unrelated products. It means the same conceptual information architecture can present different density and emphasis by role/device.

Detailed responsive behavior is reserved for 003-H.

---

## 18. Administrator experience boundary

Technical Administrator experience should remain separate from Competition operations where practical.

Administrator needs may include:

- system health;
- tenant/environment operation if later applicable;
- Identity/access recovery tooling;
- break-glass operation;
- technical incident handling.

Administrator should not receive a Competition Organizer experience merely because of infrastructure authority.

Break-glass access to Competition-sensitive information should require an explicit exceptional transition with reason/provenance.

The detailed technical admin console is outside the initial Competition UX scope unless implementation requirements later demand it.

---

## 19. Shared-display safety

Organizer work may occur on projected or shared screens.

The information architecture should support an operationally useful disclosure posture that does not casually expose:

- Judge Notes;
- institution/Alias mappings;
- private individual scores;
- sensitive reconciliation reasons.

A future presentation-safe operational mode may be useful, but it remains a UX projection rather than another Access role or Concept.

The important requirement is that sensitive disclosure is deliberate.

---

## 20. Role-mode privacy defaults

### Judge mode default

Least disclosure required for judging.

### Organizer mode default

Operational visibility appropriate to Competition administration, with sensitive evaluation details available through intentional drill-down rather than always occupying the primary operational view.

### Administrator mode default

Technical/system information, not Competition decision content.

This reduces accidental disclosure while preserving legitimate authority.

---

## 21. Experience architecture and Access

Navigation visibility is not itself authorization.

Even if the UI hides an action, Access remains responsible for determining whether the action is valid.

Likewise, a navigable historical link does not guarantee the current role may retrieve its contents.

The experience architecture should make permitted behavior understandable, but it does not replace Access enforcement.

---

## 22. Lifecycle-sensitive actions

Actions should be discoverable only where their meaning is valid or should be clearly framed when exceptional.

Examples:

### Active

Judge:

```text
start/resume Scorecard
finalize
amend own evaluation
```

Organizer:

```text
adjust Panel
resolve absence/recusal
capture paper
inspect progress
```

### Event Completed

Judge ordinary mode:

```text
no private Scorecard/Note history
```

Organizer:

```text
reconcile
request scoped amendment
resolve Coverage
review Rank
```

### Finalized

Organizer:

```text
review Official Outcome
publish/export
enter exceptional correction workflow
```

Ordinary live-event actions should no longer appear as routine possibilities.

---

## 23. Status architecture

003-A does not finalize all user-facing status terminology, but it establishes that status must be presented at the level where it matters.

Examples:

### Competition

```text
Draft
Ready
Active
Event Completed
Finalized
```

### Encounter

```text
Prepared
Open
Complete
Cancelled
Invalidated
```

### Scorecard

```text
Draft
Finalized
Amendment in progress
```

### Coverage

```text
Satisfied
Incomplete
Exception Accepted
```

### Result

```text
Provisional
Ranking Ready
Official
Affected / correction under review
```

The system should not use one generic `Active / Complete` vocabulary for semantically different objects.

Canonical cross-cutting labels will be refined in 003-I.

---

## 24. Search and direct retrieval

Organizers will eventually need rapid retrieval of:

- Team;
- Judge;
- Panel;
- Encounter;
- Scorecard;
- Award;
- Export.

Search is therefore an interaction capability across the information architecture, not a standalone Concept or a reason to make every object top-level navigation.

Search results must preserve Competition context and disclosure boundaries.

For example, Team search in Judge mode should not expose administrative institution identity.

---

## 25. Experience continuity across devices

A person's Competition context should be recoverable when moving between suitable devices, subject to Access/reverification requirements.

However, the system must distinguish:

```text
server-authoritative context/state
```

from:

```text
device-local unsynchronized working changes
```

The experience cannot promise that work is available on another device unless it has actually been durably synchronized.

Detailed degraded/offline behavior remains for 003-H.

---

## 26. Experience architecture invariants

003-A establishes these experience-level invariants:

1. Identity is not treated as a permanent role.
2. Judge/Organizer experiences are explicit Participation modes.
3. Role switching is deliberate where multiple Participations exist.
4. Competition context is always unambiguous for consequential work.
5. Judge navigation remains narrow and judging-task oriented.
6. Organizer architecture follows Competition operating modes rather than only entity collections.
7. Lifecycle changes shift experience emphasis without redefining domain state.
8. Historical Competitions default to inspect/trace/export rather than ordinary editing.
9. Current state and historical snapshot/version state are never silently conflated.
10. Organizer operational summaries drill down to source evidence.
11. Domain collections may be navigable but do not define the entire information architecture.
12. Context switching cannot silently discard meaningful working state.
13. Deep links/QRs never bypass Participation or Access context.
14. Judge experience is mobile-priority; Organizer experience supports broader operational density.
15. Administrator technical experience remains separate from ordinary Competition authority.
16. Shared-display disclosure of sensitive Competition information is deliberate rather than accidental.
17. Navigation visibility never substitutes for Access enforcement.
18. Lifecycle-invalid actions are not presented as ordinary actions.
19. Object-specific status semantics are preserved rather than flattened into generic labels.
20. Search/direct retrieval obeys Competition context and disclosure rules.
21. Cross-device continuity never falsely implies unsynchronized work is safely available elsewhere.

---

## 27. Explicit non-decisions

003-A does not choose:

- sidebar versus tab bar;
- top navigation versus bottom navigation;
- route paths;
- page names;
- component hierarchy;
- visual design system;
- desktop breakpoints;
- exact mobile layout;
- search technology;
- client-state management;
- front-end framework;
- authentication UI technology;
- API design;
- AWS architecture.

Those decisions should follow the experience contracts rather than define them.

---

## 28. Handoff to 003-B

003-A establishes the application's actor/context architecture.

The next group can now design the first high-risk Judge journey:

```text
arrive at event
    ↓
establish/reverify Identity
    ↓
establish Judge Participation
    ↓
confirm expertise
    ↓
check in / become eligible
    ↓
join/confirm Panel context
    ↓
reach ready-to-judge state
```

003-B should make that path fast enough for day-of-event volunteers while preserving Identity, Participation, Access, Panel, and disclosure boundaries.

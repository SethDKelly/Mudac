# 001-H — Phase 001 Consolidation & Initial Concept Catalog

Status: **Complete**

## 1. Purpose

Phase 001 established the conceptual foundation for the MUDAC competition application before screen design, component design, persistence design, or AWS service selection.

This consolidation records the first authoritative conceptual baseline. It reconciles the decisions from 001-A through 001-G, promotes the surviving candidate concepts into the initial concept catalog, identifies derived mechanisms and policy rather than concepts, records cross-cutting invariants, and defines the unresolved questions that should move into the next design phase.

The guiding discipline remains Daniel Jackson's Concept Design methodology: concepts should have singular purposes, understandable operational principles, and independent behavior; application-specific composition should be expressed through synchronizations rather than by allowing concepts to absorb one another.

---

## 2. Phase 001 product statement

MUDAC is a competition-operations and judging system for live student data challenges.

Its central purpose is:

> Enable a live academic data competition to conduct fair, traceable, efficient, multi-perspective evaluation of student Teams while minimizing administrative burden and preserving the human interaction at the center of judging.

The application is not merely an electronic score-entry form. It coordinates the surrounding judging model: Team anonymity, Judge participation, Panel composition, repeated Judging Encounters, Rubric application, Scorecard provenance, paper/electronic capture parity, evaluation coverage, aggregation, ranking, Award conferral, and event closeout.

Students are currently beneficiaries and competition participants but are not application actors. The initial application boundary therefore excludes student accounts, student submission workflows, dataset distribution, analytical execution environments, and student-facing result or feedback portals.

---

## 3. Architectural boundary condition

The intended deployment end state is:

```text
GitHub
   ↓
GitHub Actions
   ↓
AWS ecosystem
```

This is a boundary condition, not a Phase 001 architecture decision.

Phase 001 deliberately does not select specific AWS services, client frameworks, API styles, databases, identity products, local/offline persistence mechanisms, or deployment topology. Later architecture must demonstrate that its choices satisfy the conceptual, privacy, history, accessibility, and resilience requirements established here.

---

## 4. Canonical vocabulary

The following terminology is authoritative for the current design baseline.

### Team

The student group whose work is evaluated as a single competitor.

### Division

The competitive partition to which a Team belongs. A Team belongs to exactly one active Division within a Competition.

### Judge

A human actor participating in a specific Competition in the Judge role. Judge is a Participation role, not a permanent global account type or an independent concept.

### Organizer

A human actor participating in a Competition with competition-operations authority. Organizer is a Participation role, not an independent concept.

### Administrator

A system-level technical authority. Administrative technical power does not inherently confer Organizer decision authority over a Competition.

### Expertise

Judge Participation metadata representing the perspective a Judge contributes, such as Academic, Business, or Technical. Expertise is not an authorization role. A Judge may have more than one expertise classification.

### Panel

A reusable grouping of Judge Participations intended to evaluate together.

### Judging Encounter

One bounded occurrence of one Panel evaluating one Team.

### Rubric

The structured evaluation definition describing what Judges evaluate and how valid judgments are expressed.

### Scorecard

One Judge's independent evaluation of one Team within one Judging Encounter using one identifiable Rubric version.

### Award

Competition recognition conferred on a Team. Awards may be rank-derived or Organizer-conferred/discretionary.

### Alias / Competition Identity

The competition-safe Team identity presented during judging instead of administrative or institutional identity.

---

## 5. Actor and authority model

Phase 001 separates six concerns that must not collapse into one role field:

```text
WHO IS THIS?
    Identity

WHY ARE THEY HERE?
    Participation

IN WHAT CAPACITY?
    role such as Judge or Organizer

WHAT PERSPECTIVE DO THEY BRING?
    Expertise

WHAT MAY THEY DO OR SEE NOW?
    Access

WITH WHOM ARE THEY JUDGING?
    Panel
```

A person's identity may persist between annual competitions, but Competition Participation is event-scoped.

A returning Judge may be recognized and reverified more easily, but prior participation does not automatically restore current Competition authority, Panel assignment, or expertise declarations.

Authority is expected to be scoped and temporal rather than represented by a single global role. Important scopes include system, Competition, Encounter, and artifact-specific authority.

---

## 6. Competition lifecycle baseline

The provisional Competition lifecycle is:

```text
Draft
  ↓
Ready
  ↓
Active
  ↓
Event Completed
  ↓
Reconciliation
  ↓
Finalized
  ↓
Historical
```

The exact state names may be refined later, but the distinction between **Event Completed** and **Competition Finalized** is authoritative.

### Event Completed

The live judging event has ended. Ordinary Judge participation has ended. Organizer reconciliation may continue.

### Reconciliation

Organizers may resolve incomplete Scorecards, paper capture, permitted amendments, coverage exceptions, ties, rankings, and Awards.

### Competition Finalized

Scoring and Awards are settled as the official Competition outcome. Later corrections are exceptional and should require stronger authorization and provenance.

### Historical

The Competition remains retained as an authoritative historical record according to later retention policy.

---

## 7. Judge privacy and access lifecycle

Judge Scorecards, criterion Notes, overall Notes, revision history, and Judge-specific judging history are private evaluation records.

The Phase 001 baseline selects the following default:

> Judge records persist; ordinary Judge access does not.

During active participation, a Judge may need access to:

- their own current and completed Scorecards;
- their own criterion and overall Notes;
- their own judging history for the current event;
- current Panel and event information necessary to judge.

At **Event Completed**, ordinary Judge access to private judging records should expire. The underlying Scorecards, Notes, versions, provenance, and authorship remain available to authorized Organizers as part of the Competition record.

If a post-event correction requires Judge involvement, the preferred model is narrow temporary reactivation:

```text
Organizer authorizes correction
        ↓
Judge reverifies
        ↓
Temporary access to the specific evaluation
        ↓
Amendment finalized or access expires
        ↓
Temporary access removed
```

Judges do not receive competition-wide scoring, peer evaluations, Panel aggregates, Division rankings, or standings through the judging experience, either during active judging or merely because their historical identity still exists later.

---

## 8. Initial accepted concept catalog

Phase 001 accepts fifteen concepts as the initial catalog. They remain revisable if later specification exposes a failed boundary, but they are now the canonical vocabulary for Phase 002.

## 8.1 Core competition concepts

### 1. Competition

**Purpose:** Establish the lifecycle and governing context of one competition occurrence.

**Owns:** competition identity, event period, lifecycle state, completion/finalization state.

**Does not own:** Team administration, Division membership semantics, Panel composition, Rubric editing, Scorecards, Rank calculation, or Award logic.

**Operational principle:** An Organizer creates a Competition, prepares it, activates it for judging, marks the live event complete, reconciles outstanding competition state, finalizes official outcomes, and eventually retains it historically.

### 2. Division

**Purpose:** Partition competing Teams into mutually exclusive populations that should be compared against one another.

**Owns:** Division definitions and active Team-to-Division assignment.

**Key invariant:** a Team belongs to exactly one active Division in a Competition.

**Operational principle:** Organizers define Divisions and assign Teams; ranking later compares eligible Teams within the Division by default.

### 3. Team

**Purpose:** Maintain the administrative representation of a student group participating as one competing unit.

**Owns:** administrative Team identity and Team lifecycle such as active/withdrawn state.

**Does not own:** Division, Alias, Encounters, Scorecards, Aggregate, Rank, or Awards.

**Operational principle:** An Organizer establishes a Team and maintains the information needed to operate that competitor within the Competition.

### 4. Panel

**Purpose:** Maintain a reusable grouping of active Judge Participations intended to evaluate together.

**Owns:** current memberships and, where needed, the panel-composition capacity each member fulfills.

**Does not own:** historical Encounter participation.

**Operational principle:** Organizers assemble Judges into Panels, adjust Panel membership as live-event needs change, and reuse Panels across multiple Team evaluations.

### 5. Judging Encounter

**Purpose:** Represent one bounded occurrence of a Panel evaluating a Team.

**Owns:** Panel reference, Team reference, historical participant snapshot, evaluation context, lifecycle, and occurrence timing.

**Key property:** later Panel membership changes never rewrite who actually participated in an earlier Encounter.

**Operational principle:** A Panel and Team enter a judging occurrence; the participating Judges are captured; independent Scorecards are completed; the Encounter becomes complete when its evaluation obligations are satisfied.

### 6. Rubric

**Purpose:** Define a structured evaluation instrument and the semantics of valid judgment.

**Owns:** Criteria, scoring ranges, scoring guidance, weighting/point semantics, and completeness requirements.

**Operational principle:** An Organizer constructs and validates a Rubric, establishes an authoritative version, and Judges apply that version through Scorecards.

### 7. Scorecard

**Purpose:** Capture one evaluator's independent judgment within one Judging Encounter.

**Owns:** criterion responses, criterion Notes, overall Notes, draft/finalized/amendment state, Judge attribution, Encounter context, and Rubric-version basis.

**Operational principle:** A Judge independently records scores and Notes, works safely in Draft state, finalizes the completed evaluation, and may later produce a traceable amendment without erasing the prior authoritative version.

### 8. Award

**Purpose:** Define and confer recognized achievements within a Competition.

**Owns:** Award definition, scope, eligibility, selection semantics, and conferral state.

**Operational principle:** An Organizer defines an Award and later confers it on an eligible Team, either because a declared ranking rule identifies the recipient or because the Competition deliberately selects a discretionary recipient.

---

## 8.2 Supporting concepts

### 9. Identity

**Purpose:** Maintain continuity that actions or Participation episodes belong to the same human identity.

**Does not imply:** permanent Competition authority or a particular authentication mechanism.

**Operational principle:** A person establishes or reverifies identity; the same identity may later support a new, separate Competition Participation.

### 10. Participation

**Purpose:** Represent an Identity taking part in a scoped activity for a limited period and in a particular capacity.

**Owns:** Competition scope, participation role, participation status, and relevant declared attributes such as Judge expertise.

**Operational principle:** An Identity enrolls in a Competition role, becomes active as appropriate, participates, and later becomes historical without losing attribution to actions performed during the event.

### 11. Alias

**Purpose:** Give a subject a context-specific identity that can be used without exposing its underlying identity.

**Operational principle:** A Team receives a Competition-scoped Alias; Judges interact with that Alias while only appropriately authorized contexts can resolve it back to the underlying administrative Team.

### 12. Access

**Purpose:** Permit or deny actions and information disclosure according to principal, scope, resource, purpose, state, and time.

**Operational principle:** Participation and lifecycle conditions produce narrowly scoped access; when the purpose ends, access expires without deleting the underlying records.

### 13. Versioning

**Purpose:** Preserve successive authoritative states of something that may legitimately change over time.

**Primary compositions:** Rubric versions and Scorecard amendments.

**Operational principle:** A new authoritative version becomes current without erasing prior authoritative state; previous versions remain addressable for comparison and history.

### 14. Provenance

**Purpose:** Preserve the meaningful origin and transformation history needed to explain an authoritative record.

**Operational principle:** Meaningful domain actions record who acted, what changed, when, under which origin/capture path, and where necessary why.

**Important distinction:** Versioning answers what states existed; Provenance answers how and by whom those states arose.

### 15. Export

**Purpose:** Produce a stable external representation of authoritative information for distribution or printing.

**Operational principle:** An Organizer selects authoritative source information or a source version and generates a traceable representation such as a printable Rubric, event guide, Panel sheet, or join material.

**Important distinction:** PDF and QR are representations/encodings, not concepts.

---

## 9. Intentionally non-conceptual domain elements

Several important elements are intentionally subordinate state rather than independent concepts.

### Criterion

Belongs to Rubric state. It defines one evaluation dimension but currently has no independent lifecycle or operational purpose outside a Rubric.

### Note

Belongs to Scorecard state. Notes may exist at Criterion scope or Scorecard-wide scope but currently do not form an independent commenting/discussion mechanism.

### Expertise

Belongs to Judge Participation state. It affects Panel composition but not application authorization.

### Panel Membership

Belongs to Panel relational state. Historical Encounter participation is captured by Judging Encounter rather than inferred from current membership.

### Event Information

Belongs to Competition information unless later content-authoring requirements justify a separate publishing concept.

---

## 10. Derived mechanisms

The following are important domain semantics but are not currently independent concepts because they are computed from authoritative concept state and policy.

### Scorecard Total

Derived from criterion responses according to the applicable Rubric version.

### Encounter Aggregate

Derived from eligible finalized Scorecards authored by the Judges participating in the Encounter.

### Team Aggregate

By default, derived as the arithmetic mean of all eligible individual Judge Scorecards for the Team. This preserves equal Judge weighting even when Panels contain uneven Judge counts.

### Evaluation Coverage

Derived by comparing required/expected evaluation obligations with completed eligible evaluation. Coverage is intentionally independent from numeric aggregation.

### Rank

Derived from eligible Team aggregates within a Division according to declared ranking and tie policy.

### Result

Not an independent concept. A result view is a projection of Aggregate, Coverage, Rank, Awards, and official/provisional lifecycle state.

---

## 11. Policy/configuration rather than concepts

The following should remain explicit Competition policy/configuration rather than hard-coded application assumptions:

- Division definitions;
- expertise categories;
- Panel composition requirements;
- Rubric scoring model;
- Criterion ranges and weights;
- Scorecard completeness requirements;
- aggregation policy;
- evaluation coverage requirements;
- result eligibility;
- tie resolution;
- whether Panel-versus-Judge weighting differs from the default;
- Scorecard amendment rules;
- Rubric-change restrictions after judging begins;
- Award scope and selection method;
- post-finalization correction controls.

Phase 001 recommends sensible defaults but does not freeze these as MinneMUDAC-specific code constants.

---

## 12. Evaluation semantics baseline

The authoritative evaluation chain is:

```text
Rubric Criterion
      ↓
Criterion Evaluation
      ↓
Judge Scorecard
      ↓
Encounter analytical view
      ↓
Team Aggregate
      ↓
Division Rank
      ↓
Rank-derived Award where applicable
```

Discretionary Awards follow a separate path:

```text
Scores + Notes + Organizer deliberation
                ↓
             Award
                ↓
              Team
```

### Evaluation rules carried forward

- One Judge Participation has at most one logical Scorecard per Encounter.
- Scorecard revisions do not create additional evaluation weight.
- Every Scorecard is tied to one identifiable Rubric version.
- Required Criterion responses must be complete before finalization.
- Missing, zero, and N/A are distinct states.
- Missing evaluation is never silently converted to zero.
- The latest finalized Scorecard version is authoritative.
- An amendment Draft does not immediately remove the last finalized version from aggregation.
- The default Team aggregate gives equal weight to eligible Judge Scorecards.
- Outliers remain valid unless an explicit review determines that an evaluation itself is invalid.
- Judge scoring is not silently normalized.
- Ranking is Division-scoped by default.
- Exact ties require declared policy or explicit resolution rather than arbitrary hidden tie-breaking.

---

## 13. Awards baseline

Awards are a first-class concept because competition recognition is not reducible to ranking.

Awards may include examples such as:

- Division first place;
- Division second place;
- Most Innovative;
- Best Applied Analysis;
- Best Presentation;
- other Organizer-defined recognition.

An Award may be Competition-wide or Division-scoped.

A rank-derived Award may use a derived Rank to identify its candidate recipient. The recommended initial interaction is that the system derives the candidate and an Organizer confirms the conferral, preserving the distinction between mathematical ranking and official recognition.

Discretionary Awards are deliberate Organizer decisions and should not be represented as if mathematically derived unless the Award's declared selection policy actually defines such a formula.

Award conferral retains provenance and remains correctable under appropriate lifecycle controls.

---

## 14. Anonymity and disclosure baseline

The application provides controlled identity disclosure, not absolute real-world anonymity.

A Team has at least two representations:

```text
Administrative Identity
    institution
    members
    registration information

Competition Identity / Alias
    anonymous Team identifier
    Division
```

Judges see the Competition Identity and Division but not institutional identity by default.

Organizers can resolve the Competition Identity to the administrative Team when required for legitimate competition operations.

The same identity-shielding rules apply to electronic screens and generated/printed judging materials. Printing must not accidentally reintroduce institution identity that the electronic judging path intentionally hides.

---

## 15. Paper and electronic capture baseline

Paper remains a first-class supported judging channel for accessibility, preference, device limitations, and continuity during technical disruption.

Electronic and paper Scorecards use the same Rubric version and scoring semantics. Their difference is capture provenance, not evaluation meaning.

For a paper-origin evaluation:

```text
Evaluation author = Judge
Capture actor      = Organizer
Capture channel    = Paper
Rubric version     = known
```

An Organizer transcription error is a capture correction and is distinguishable from a Judge changing the underlying judgment.

Printable Rubrics and related materials must identify enough source/version context to reconnect physical records to the correct digital evaluation context.

---

## 16. Controlled finality baseline

Phase 001 identifies a recurring pattern across Rubrics, Scorecards, Awards, and Competition outcomes:

> Something may become authoritative without becoming impossible to correct.

The preferred semantics are therefore:

```text
working state
     ↓
authoritative state
     ↓
traceable amendment/correction
     ↓
new authoritative state
```

rather than either destructive mutability or absolute immutability.

For Scorecards specifically:

```text
Draft
  ↓
Finalized v1
  ↓
Amendment Draft       (v1 remains authoritative)
  ↓
Finalized v2          (v2 becomes authoritative; v1 historical)
```

This pattern is supported by Versioning and Provenance rather than duplicated independently in every concept.

---

## 17. Core synchronization families

The application emerges from coordination among independent concepts.

### Identity → Participation

A verified Identity may establish a new Competition Participation. Prior annual participation does not automatically confer current participation.

### Participation → Access

Active Participation can cause appropriate Access to be granted. Completion, withdrawal, or Competition lifecycle changes cause access to change independently from the underlying record.

### Event Completion → Judge Access Expiration

When the live event completes, ordinary Judge access to Scorecards, Notes, and current-event judging history expires while Organizer-governed records remain intact.

### Team → Alias

A Team in a blinded Competition receives a competition-safe Alias.

### Panel + Team → Judging Encounter

When a Panel begins evaluating a Team, a Judging Encounter is established and the Judges actually participating are captured as a historical snapshot.

### Encounter + Participants + Rubric Version → Scorecards

Beginning an Encounter creates or establishes one logical Scorecard obligation for each participating Judge under the applicable authoritative Rubric version.

### Scorecard Finalization → Versioning + Provenance + Derived Refresh

Finalizing an evaluation commits an authoritative version, records meaningful provenance, and updates derived Encounter completion, Coverage, Aggregate, and Rank projections.

### Scorecard Amendment → New Authoritative Version

Finalizing an amendment creates a new authoritative version and refreshes derived outcomes without treating the revision as a second independent evaluation.

### Rank → Award Candidate

For rank-derived Awards, official ranking may identify the candidate recipient; Award conferral remains an explicit recognition action.

### Authoritative source → Export

Rubric versions, Competition information, Panel/access information, and other authoritative sources may produce stable printable/distributable representations.

---

## 18. Phase 001 invariants

The following invariants are considered authoritative design constraints unless explicitly revised in a later phase.

1. A Team belongs to exactly one active Division within a Competition.
2. Division changes are corrections, not ordinary Team lifecycle behavior.
3. A Judging Encounter joins one Team and one Panel.
4. Encounter provenance preserves the Judges who actually participated.
5. Later Panel membership changes never rewrite historical Encounter participation.
6. A Judge Participation has at most one logical Scorecard per Encounter.
7. Scorecard revisions do not create additional evaluation weight.
8. Each Scorecard is attributable to one Judge Participation and one Judging Encounter.
9. Each Scorecard references an identifiable Rubric version.
10. Required Criterion responses must be complete before Scorecard finalization.
11. Missing evaluation is never interpreted as zero.
12. Finalized Scorecards participate in official aggregation.
13. The current finalized Scorecard version is authoritative.
14. An amendment Draft does not erase the last authoritative Scorecard version.
15. Paper and electronic Scorecards share evaluation semantics.
16. Manual capture does not replace the original Judge as evaluation author.
17. Evaluation Coverage is distinct from numeric Aggregation.
18. Insufficient coverage remains visible and requires declared policy or explicit Organizer resolution.
19. Outlier evaluations are not silently discarded or normalized.
20. Judges do not see peer Scorecards, peer Notes, active aggregates, or competition standings through the judging experience.
21. Judges see Team Competition Identity and Division rather than institutional identity by default.
22. Ordinary Judge access to private evaluation records expires after live event participation ends.
23. Access expiration does not delete or de-author private evaluation records.
24. A historical Judge may receive temporary narrowly scoped access if a legitimate post-event correction requires their involvement.
25. Rubric changes never silently rewrite the evaluation basis of previously completed Scorecards.
26. Rankings are Division-scoped by default.
27. Rank is derived rather than manually authored in ordinary operation.
28. Rank and Award are distinct.
29. Awards may be rank-derived or Organizer-conferred.
30. Award conferral retains provenance and may be corrected through explicit controlled workflows.
31. Official outcomes must be explainable back to authoritative Scorecards, Rubric semantics, eligibility/coverage policy, and relevant decisions.
32. Technical Administrator authority does not automatically substitute for Organizer competition authority.

---

## 19. Experience principles

The Phase 001 experience doctrine is:

### Judging focus

Technology remains secondary to observing, questioning, reasoning, and evaluating student work.

### Mobile-first Judge experience

The primary Judge interaction is designed for a smartphone in portrait orientation and should avoid desktop interaction assumptions.

### Persistent evaluation context

The current Team, Division, and judging context must remain difficult to confuse.

### Safe Drafting

Routine interruption should not destroy already-entered Scorecard work.

### Autosave semantics

The system should behave as though Draft work is continuously preserved. Saving Draft work and finalizing an evaluation remain clearly different actions.

### Explicit finalization

Finalization means the Judge asserts that the evaluation is complete and may participate in official aggregation.

### Accessible participation

Important interactions must not depend solely on color, fine motor precision, hover, or a particular personal device. Semantic accessibility and keyboard operation remain important even though Judge use is mobile-first.

### Paper legitimacy

Paper is a supported accessibility and continuity path rather than an error state.

### Degraded-operation resilience

Poor network connectivity is an expected live-event condition. The interface must communicate truthfully whether work is saved, synchronized, pending, or unavailable.

### Safe retry

Network uncertainty must not create duplicate logical Scorecards or duplicate finalization effects.

### Privacy by lifecycle

Sensitive Judge evaluation data is exposed only while there is a legitimate operational need.

### Exception-first Organizer experience

Organizers need immediate visibility into incomplete or exceptional competition state rather than manually inspecting every Team, Panel, Judge, and Encounter.

### Proportional friction

Confirmation and reason-capture should increase with the consequence of an action rather than burdening routine Draft work.

### Traceable recovery

Operational mistakes should be corrected explicitly without silently rewriting history.

### Familiar interaction

Because many Judges may use the application only once, standard understandable interaction patterns are preferred over clever or highly customized controls.

---

## 20. Operational resilience scenarios retained for later architecture

Future implementation and architecture must demonstrate credible handling of at least these scenarios:

- Judge closes or refreshes the browser during a Draft;
- temporary loss of Wi-Fi or cellular service;
- uncertain response after a Finalize request;
- repeated Finalize request caused by retry;
- Judge switches devices;
- Judge loses a device;
- shared/loaner device changes users;
- Judge cannot or does not want to use the electronic interface;
- Panel membership changes during the event;
- Judge leaves or recuses during an Encounter;
- wrong Team is selected before or during scoring;
- incomplete Scorecard remains after presentation;
- paper Rubric is captured later;
- paper transcription error is discovered;
- incorrect Division is discovered after judging begins;
- Rubric-version mismatch is discovered;
- Scorecard amendment occurs after Event Completion;
- major application/network outage requires paper-assisted continuation.

Phase 001 intentionally does not dictate the technical mechanism used to satisfy these scenarios.

---

## 21. Explicit non-concepts and deferrals

To protect conceptual clarity, the following are intentionally not concepts in the Phase 001 catalog.

### Actor/role labels

- Judge
- Organizer
- Administrator

These are roles/authority contexts composed from Identity, Participation, and Access.

### Derived or policy mechanisms

- Aggregation
- Evaluation Coverage
- Rank
- Result
- Scoring Policy
- Coverage Policy
- Tie Policy
- Panel Composition Policy

### Presentation and delivery mechanisms

- Dashboard
- Judge Portal
- Organizer Portal
- Admin Screen
- Score Form
- PDF
- QR code
- Mobile application

### Technical mechanisms

- Authentication provider
- API style
- database product
- AWS service
- GitHub Actions workflow design

### Scope deferred until evidence requires it

- student application accounts;
- student submission workflow;
- scheduling as a first-class concept;
- notifications as a first-class concept;
- student feedback publication;
- Judge-visible post-event analytics;
- generalized content publishing beyond required event/export material.

---

## 22. Open questions carried into Phase 002

The following questions remain intentionally unresolved and do not block Phase 001 exit.

### Rubric and scoring

- Which scoring models must be supported initially: point allocation, weighted common scale, or both?
- Are any Criteria permitted to be optional or N/A?
- Are Notes ever required for particular scores or Rubric Criteria?
- How are internal precision and displayed precision represented?

### Coverage and ranking

- What exact minimum Encounter/Scorecard coverage rules should the initial Competition support?
- Can coverage exceptions be approved, and what reason/provenance is required?
- What tie policies are required initially?
- Are there any legitimate cases where Panel weighting should differ from equal individual Judge weighting?

### Scorecard amendments

- May Judges independently reopen a finalized Scorecard while the Competition is Active, or must some amendments require Organizer authorization?
- At what lifecycle point do amendments require stronger reason capture or Organizer approval?
- What post-Finalization correction process is acceptable?

### Panels and Encounters

- Does a Competition preassign/schedule Panel-Team Encounters, allow ad hoc Team selection, or support both?
- What composition rules define an acceptable Panel, and what exception model is needed?
- How should recusal and early departure be represented precisely?

### Awards

- Should rank-derived Awards be automatically conferred or only proposed for Organizer confirmation?
- Are nominations useful for discretionary Awards?
- Are shared/co-recipient Awards permitted?

### Access and retention

- What exact retention period applies to Competition records?
- How much non-sensitive historical identity recognition should a returning Judge see?
- What data, if any, may remain locally on Judge devices during degraded operation and for how long?
- What exceptional Administrator access to Competition data is necessary for support?

### Export

- Which print/export artifacts are required for the initial release?
- What identifiers or machine-readable markers should paper Scorecards carry?

These questions should be resolved through explicit concept and policy specification rather than through incidental implementation choices.

---

## 23. Phase 001 exit assessment

Phase 001 meets its purpose.

The product now has:

- a stable purpose and scope boundary;
- canonical participant terminology;
- a contextual role and authority model;
- a Competition lifecycle including Event Completed and Finalized semantics;
- a precise evaluation unit centered on individual Scorecards within Judging Encounters;
- a Team anonymity/disclosure model;
- independent evaluation and privacy rules;
- paper/electronic equivalence;
- controlled-finality and revision principles;
- a distinction between judgment, coverage, aggregation, rank, and Award;
- fifteen accepted concepts with defensible singular purposes;
- identified synchronization families;
- explicit invariants;
- mobile/accessibility/resilience doctrine;
- clear architecture deferrals.

No unresolved Phase 001 question requires adding another core concept before deeper specification begins.

**Phase 001 is therefore complete.**

---

## 24. Initial concept architecture at Phase 001 exit

```text
                         COMPETITION
                              │
         ┌────────────────────┼────────────────────┐
         │                    │                    │
      DIVISION              RUBRIC               AWARD
         │                    │                    │
        TEAM                  │                    │
         │                    │                    │
       ALIAS                  │                    │
         │                    │                    │
         └────────────┐       │                    │
                      ▼       ▼                    │
                 JUDGING ENCOUNTER                 │
                      │                            │
          ┌───────────┼───────────┐                │
          │           │           │                │
      Judge Part. Judge Part. Judge Part.           │
          │           │           │                │
       SCORECARD   SCORECARD   SCORECARD            │
          │           │           │                │
          └───────────┼───────────┘                │
                      │                            │
                 authoritative                    │
                  evaluations                      │
                      │                            │
              ┌───────┴────────┐                   │
              ▼                ▼                   │
          COVERAGE         AGGREGATE               │
           derived          derived                │
              │                │                   │
              └───────┬────────┘                   │
                      ▼                            │
                     RANK ─────────────────────────┘
                    derived       rank-derived award path


IDENTITY
   │
   ▼
PARTICIPATION ────────► ACCESS
   │                     │
   └──────► PANEL         │
                          │
                    private evaluation
                        disclosure


SCORECARD / RUBRIC
       │
       ├────────► VERSIONING
       └────────► PROVENANCE


AUTHORITATIVE SOURCE / VERSION
             │
             ▼
           EXPORT
             │
       printable/distributable
       representations
```

Arrows in this diagram indicate relationships and synchronization/derivation paths, not object ownership.

---

## 25. Recommended Phase 002

The natural next phase is **Phase 002 — Concept Specification, Policy & Synchronization Refinement**.

Phase 001 discovered and bounded the concepts. Phase 002 should specify them rigorously enough to guide later UX and architecture.

Recommended groupings:

### 002-A — Competition, Division, Team & Alias Specifications

Specify lifecycle, actions, invariants, administrative identity, Division assignment correction, Team withdrawal, and Alias generation/resolution semantics.

### 002-B — Identity, Participation & Access Specifications

Specify Judge/Organizer participation lifecycle, returning identity behavior, temporal access, temporary amendment access, session-independent authority semantics, and privacy boundaries.

### 002-C — Panel & Judging Encounter Specifications

Specify Panel composition, membership changes, encounter initiation, participant snapshots, recusal/non-participation, repeat encounters, and completion semantics.

### 002-D — Rubric & Scorecard Specifications

Specify Rubric structure, scoring models, criterion semantics, Notes, draft/finalization/amendment behavior, paper-origin evaluation, and Rubric-version compatibility.

### 002-E — Versioning & Provenance Specifications

Specify generic version semantics, authoritative/current version behavior, meaningful provenance events, capture-versus-evaluation authorship, reason requirements, and historical inspection.

### 002-F — Aggregation, Coverage, Ranking & Evaluation Policy

Specify mathematical semantics, eligibility, precision, missing evaluation, coverage exceptions, outlier treatment, tie policy, and official/provisional ranking behavior.

### 002-G — Award Specification & Competition Finalization

Specify Award definition/conferral, rank-derived versus discretionary selection, Award correction, reconciliation readiness, finalization gates, and post-finalization correction.

### 002-H — Export, Print & Operational Continuity Specification

Specify printable Rubrics, event information, Panel/join materials, paper identifiers, document/version traceability, and continuity requirements.

### 002-I — Phase 002 Consolidation & Specification Exit Review

Reconcile concept specifications, synchronization contracts, policies, remaining UI questions, and readiness to proceed into conceptual UX architecture and then AWS/system architecture.

Phase 002 should remain implementation-neutral. It should produce specifications strong enough that later UI and architecture decisions can be evaluated against explicit behavioral contracts.

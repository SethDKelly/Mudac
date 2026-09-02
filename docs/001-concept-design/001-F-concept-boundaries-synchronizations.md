# 001-F — Concept Boundaries, Independence & Synchronization Candidates

**Status:** Complete  
**Phase:** 001 — Concept Design Foundation

## Purpose

Pressure-test the fifteen candidates for singularity and independence, narrow their responsibilities, and move application-specific behavior into explicit synchronizations rather than direct concept dependencies.

## Design posture

Concepts should not form a giant ownership tree. Competition should not own judging logic; Team should not own Division, Alias, Rank, or Awards; Scorecard should not calculate standings; Participation should not itself determine resource access.

Use the following distinctions consistently:

- **Concept** — owns coherent state and behavior.
- **Synchronization** — coordinates independent concepts.
- **Invariant** — identifies states that must never be allowed.
- **Derivation** — computes information from authoritative state.
- **Policy** — chooses among permitted behaviors.

## Accepted concept boundaries

### Competition
**Purpose:** establish the lifecycle and governing context of one competition occurrence.

Owns lifecycle/context only. Does not calculate scores, manage Panel composition, expose Team identities, or directly grant Judge access.

### Division
**Purpose:** partition competing Teams into mutually exclusive populations that should be compared with one another.

Division owns Team assignment/correction semantics rather than Team owning its Division behavior.

### Team
**Purpose:** maintain the administrative representation of one competing student group.

Team does not own Division, Alias, Encounters, Scorecards, Aggregate, Rank, or Awards.

### Alias
**Purpose:** provide a context-specific identity that can be used without exposing underlying identity.

Alias can assign/replace/retire/resolve an alternate identity. Whether a caller may resolve the Alias is an Access concern.

### Identity
**Purpose:** maintain continuity that actions or participation episodes belong to the same human identity.

Identity answers who the person is, not what they are doing in a Competition and not what they may access.

### Participation
**Purpose:** represent an Identity taking part in a scoped activity for a limited period and in a particular capacity.

Judge and Organizer are Participation roles. Expertise is Participation state. Participation does not itself grant resource access.

### Access
**Purpose:** permit or deny actions/information disclosure according to principal, scope, resource, purpose, and time.

Access is distinct from Participation and supports ordinary event access, expiration, revocation, and temporary post-event correction access.

### Panel
**Purpose:** maintain a reusable grouping of active Judge Participations intended to evaluate together.

Panel represents current intended grouping. Historical actual participants belong to Judging Encounter.

### Judging Encounter
**Purpose:** represent one bounded occurrence of a judging group evaluating one Team.

Encounter owns the historical participant snapshot, Team/Panel context, timing/lifecycle, and applicable evaluation context.

### Rubric
**Purpose:** define the structured evaluation instrument and semantics of valid judgment.

Criteria remain Rubric state. Rubric owns current working definition, not historical version mechanics.

### Scorecard
**Purpose:** capture one evaluator's independent judgment within one Judging Encounter.

Scorecard owns Criterion responses, Notes, Draft/finalization/amendment behavior, but not Team aggregation or ranking.

### Versioning
**Purpose:** preserve successive authoritative states of something that may legitimately change over time.

Versioning is reusable across Scorecard and Rubric. It does not decide whether a user is authorized to revise or what downstream computations should occur.

### Provenance
**Purpose:** preserve meaningful origin and transformation history needed to explain authoritative records.

Provenance is distinct from Versioning and from low-level infrastructure telemetry.

### Award
**Purpose:** define and confer recognized achievements within a Competition.

Award includes definition and conferral within one singular recognition mechanism. Rank may inform Award selection but is not part of Award's internal purpose.

### Export
**Purpose:** produce a stable external representation of authoritative information for distribution or printing.

PDF, print layout, and QR are representations, not concepts.

## Non-concepts retained as deliberate decisions

- Judge — Participation role.
- Organizer — Participation role.
- Administrator — system authority role.
- Academic/Business/Technical — Judge Participation expertise.
- Panel Membership — Panel state.
- Criterion — Rubric state.
- Note — Scorecard state.
- Event Information — Competition information.
- Finalization — lifecycle operation.
- Aggregation — derived computation.
- Evaluation Coverage — derived qualification.
- Rank — derived ordering.
- Result — projection.
- Manual Capture — Scorecard capture path + Provenance.
- QR Code — interaction/representation.
- PDF — Export representation.
- Dashboard/Portal — UI projection.
- AWS/GitHub Actions — implementation/deployment mechanisms.

## Synchronization families

### Identity, Participation, Access

```text
Identity verified + person chooses Judge role
  -> Participation.enroll(scope=Competition, role=Judge)

Judge Participation becomes active
  -> Access grants active-event Judge capabilities

Competition Event Completed
  -> Judge Participation becomes historical/completed
  -> ordinary Judge access to Scorecards/Notes/history expires
```

Post-event correction:

```text
Organizer authorizes correction
+ Judge reverifies
  -> temporary scoped Access to specific Scorecard
  -> amendment completes or grant expires
  -> temporary Access revoked
```

### Team and Alias

When a Team is established and blinded judging is required, the application associates a Competition-scoped Alias. Team itself does not know about Judge-facing anonymity.

### Division correction

Division correction should synchronize with Provenance and refresh affected derived Coverage/Aggregate/Rank projections where relevant.

### Panel and Encounter

An Organizer forms Panels from eligible Judge Participations according to composition policy.

When judging begins:

```text
Panel + Team
  -> Judging Encounter
  -> snapshot actual participating Judges
```

Later Panel membership changes never rewrite that snapshot.

### Encounter, Rubric, and Scorecard

When an Encounter begins, for each participating Judge the application starts one logical Scorecard using the applicable authoritative Rubric version.

Encounter does not directly implement Scorecard behavior; Scorecard does not decide why the Encounter exists.

### Scorecard finalization

```text
Scorecard.finalize
  -> Versioning commits authoritative Scorecard version
  -> Provenance records evaluator/context/capture channel
  -> derived Encounter completion, Coverage, Aggregation, and Rank refresh
```

### Scorecard amendment

The last finalized version remains authoritative while an amendment Draft exists. On amendment finalization, Versioning commits the new state, Provenance records the change, and derived scoring refreshes.

### Paper capture

Paper entry uses the same Scorecard concept. Provenance distinguishes:

- evaluation author = Judge;
- capture actor = Organizer;
- capture channel = Paper.

No separate PaperScorecard concept is needed.

### Rubric version establishment

When an Organizer establishes a valid Rubric for use:

```text
Rubric authoritative state
  -> Versioning commit
  -> Provenance record
```

Existing Scorecards always preserve the Rubric version under which they were created.

### Export

```text
specific authoritative source/version
  -> Export.generate
  -> PDF / printable / QR representation
```

### Derived scoring

```text
authoritative Scorecards
  -> Team Aggregate

expected evaluation obligations + completed evaluations
  -> Evaluation Coverage

Aggregate + Coverage eligibility + Division + policy
  -> Rank
```

Coverage and Aggregate remain distinct.

### Rank and Award

For rank-derived Awards, official Rank identifies the candidate recipient; Organizer confirmation is the preferred initial policy for official conferral.

Discretionary Awards can be conferred directly by authorized Organizers without Rank dependency.

### Competition finalization

Before finalization, Organizers should be able to confirm Coverage resolution, amendment settlement, current aggregation, tie resolution, official Rank, and Award conferral.

Finalization then changes authority/state rather than physically deleting history or making exceptional correction impossible.

## Event Completed versus Finalized

```text
ACTIVE
  -> Event Completed
       Judge ordinary private evaluation access ends
       Organizer reconciliation continues
       amendments/rank/Awards may remain provisional
  -> Competition Finalized
       scoring/ranking/Awards become official
       stronger controls govern further correction
```

## Provenance scope

Record meaningful domain changes such as:

- Team administrative identity change;
- Alias change;
- Division correction;
- Panel membership change;
- Encounter invalidation/replacement;
- Rubric version establishment;
- Scorecard finalization/amendment;
- paper capture/transcription correction;
- coverage exception;
- Award conferral/correction;
- Competition finalization;
- post-finalization correction.

Do not confuse provenance with telemetry such as page opens, table sorting, or transient draft keystrokes.

## Important boundaries

```text
Access      != Participation
Access      != Provenance
Versioning  != Provenance
Alias       != Access
Panel       != Encounter
Rubric      != Scorecard
Scorecard   != Aggregate
Rank        != Award
```

## Structural invariants

- Team has exactly one active Division.
- Encounter has one Team, one Panel, and a stable participant snapshot.
- Judge Participation has at most one logical Scorecard per Encounter.
- Scorecard references exact Rubric-version basis.
- Prior finalized Scorecard remains authoritative until amendment finalizes.
- Missing score is never zero.
- Judges do not receive peer evaluation data or standings.
- Judge private-data Access is event-scoped and temporary.
- Panel membership changes never rewrite Encounter history.
- Rubric changes never rewrite prior Scorecard meaning.
- Rank is Division-derived by default.
- Award is independent recognition.
- Official results are decomposable into authoritative Scorecards and declared policy.

## Provisional accepted concept catalog

### Core

1. Competition
2. Division
3. Team
4. Panel
5. Judging Encounter
6. Rubric
7. Scorecard
8. Award

### Supporting

9. Identity
10. Participation
11. Alias
12. Access
13. Versioning
14. Provenance
15. Export

These remain provisional until Phase 001 consolidation.

Next: **001-G — Experience Principles, Accessibility & Operational Resilience**.

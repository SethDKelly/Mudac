# 001-C — Competition Lifecycle & Critical Experience Scenarios

**Status:** Complete  
**Phase:** 001 — Concept Design Foundation

## Purpose

Describe how the competition concepts behave over time, from Organizer preparation through live judging, reconciliation, ranking, Awards, finalization, and historical retention.

## Refinements introduced

### Awards
Organizers can define and confer Awards. Awards are distinct from Rank and may be rank-derived or discretionary, such as Most Innovative or Best Applied Analysis.

### Notes
Scorecards support both Criterion-level Notes and overall Scorecard Notes. Notes are part of the evaluation record but do not independently alter numeric scoring.

### Historical Judges
Judge participation is event-scoped. A returning Judge may be recognized and reverified more easily, but each Competition creates a new participation context.

### Printable operational materials
Organizer-authored Competition information and authoritative Rubrics should support stable printable exports. Panel/join materials may also be exported. PDF/QR are representations, not concepts.

### Controlled Scorecard correction
Finalization makes a Scorecard authoritative for aggregation but not irrevocably immutable. Corrections produce traceable revisions.

## Competition lifecycle spine

```text
Competition creation
  -> event configuration
      -> Divisions
      -> Teams
      -> Rubrics
      -> Awards
      -> event information
  -> operational preparation
      -> printable materials
      -> Judge access setup
      -> Team competition identities
  -> Judge arrival/participation
  -> Panel formation
  -> repeated Judging Encounters
      -> individual Scorecards
      -> Notes
      -> finalization/revision
  -> aggregation and reconciliation
  -> ranking
  -> Award determination
  -> result finalization
  -> historical competition record
```

## Competition creation

Competition establishes the governing event context and lifecycle. Event information may include date, venue, schedule, Judge guidance, logistics, and instructions, but Event Information is currently treated as Competition state rather than a standalone concept.

## Division and Team establishment

Organizers define Divisions and establish Teams. Each Team receives:

- administrative identity;
- exactly one active Division;
- competition-safe identity/Alias.

Division reassignment is considered a correction, especially once judging has begun.

## Rubric definition and version identity

Rubric is the evaluation definition. Scorecard is one Judge's application of that definition.

Every Scorecard must be tied to the exact Rubric version used. Printed Rubrics likewise correspond to an identifiable version. This prevents paper/electronic scoring from silently diverging.

Scoring-semantic changes after judging begins must never mutate prior Scorecard meaning.

## Award definition

Awards may be:

- rank-derived;
- Organizer-conferred/discretionary;
- Division-scoped;
- Competition-wide.

Award provenance should identify the Award, recipient, scope, conferring authority, time, selection method, and optional rationale.

## Operational publishing/printing

Examples of stable exports include:

```text
Competition Information -> Event Guide
Rubric Version          -> Printable Rubric
Panel context           -> Panel operational sheet
Join/access mechanism   -> Printable join code/QR material
```

Printed artifacts should identify their Competition/source version sufficiently to reconnect them to the digital record.

## Judge arrival and participation

The desired day-of-event flow is lightweight:

```text
arrive
  -> establish/reverify identity
  -> join Competition as Judge
  -> confirm expertise
  -> check in
  -> become eligible for Panel assignment
```

Returning recognition should reduce friction without turning Judge into a permanent global role.

## Panel formation

Organizers form Panels from available Judge Participations using expertise/composition policy. Panel membership may change during the event, but completed Encounters preserve the participant snapshot that actually judged.

## Judging Encounter

A Judging Encounter is the anchor for one Panel evaluating one Team.

It records or references:

- Competition;
- Team;
- Panel;
- participating Judges;
- Rubric version;
- lifecycle/timing;
- Scorecards.

The system may later support preplanned Encounter assignments, ad hoc Team selection, or both.

## Scorecard authoring

Each participating Judge gets an independent Scorecard containing:

- rubric responses;
- Criterion Notes;
- overall Notes;
- author;
- Rubric version;
- draft/finalization state;
- revision history.

Draft work may be incomplete and should be preserved safely. Finalization means the evaluation is complete enough to participate in official aggregation.

## Encounter completion

A standard Encounter becomes complete when all required participating Judges have finalized their Scorecards. Incomplete Scorecards should be operationally visible without being treated as zero scores.

## Scorecard revisions

Preferred lifecycle:

```text
Draft
  -> Finalized v1
      -> Amendment Draft
          -> Finalized v2
```

Prior versions remain preserved. Revisions should be ordinary and trustworthy rather than punitive, while retaining who changed what and when.

A paper transcription correction is distinct from a Judge changing their evaluation. Provenance must preserve that difference.

## Paper judging

Paper remains a first-class capture path:

```text
Judge receives authoritative printed Rubric
  -> evaluates Team
  -> completes paper Scorecard
  -> Organizer captures evaluation
  -> capture is verified as needed
  -> same aggregation semantics apply
```

Evaluation authorship remains the Judge; capture actor remains the Organizer.

## Organizer live oversight

Organizers need views/projections across:

- Teams;
- Panels;
- Judges;
- Encounters;
- Scorecard completion;
- paper capture backlog;
- coverage;
- aggregates;
- revisions;
- exceptions.

Team, Panel, and Judge perspectives should all remain traceable to the underlying Scorecards.

## Aggregation, ranking, and Awards

Aggregation is derived from current authoritative Scorecard versions. Old revisions do not count as additional evaluations.

Ranking is distinct from aggregation and is Division-scoped by default.

Awards may follow Rank or Organizer deliberation. Discretionary Awards must not be presented as mathematically derived if they were not.

## Competition completion and finalization

Two lifecycle milestones are important:

- **Event Completed** — live judging has ended.
- **Competition Finalized** — scoring reconciliation, rank, and Awards are settled and official.

Finalization establishes authoritative competition outcome but does not make exceptional correction impossible. Post-finalization correction should require stronger provenance/authority.

## Historical record

After finalization, Organizers retain the Competition record including Scorecards, Notes, versions, Panels, Encounters, participation, Awards, and provenance according to retention/security policy.

## Critical scenarios

The design must support at least:

1. normal electronic judging;
2. returning Judge re-verification;
3. paper judging and later capture;
4. Judge Scorecard correction;
5. paper transcription correction;
6. mid-event Panel member replacement;
7. incomplete Encounter/forgotten Scorecard;
8. Team Division correction;
9. Rubric correction before judging;
10. attempted Rubric semantic change after judging begins;
11. discretionary Award conferral;
12. rank-based Award conferral;
13. printable event/rubric/join materials;
14. network disruption without loss of valid work.

## Controlled finality

A broad pattern emerges across Rubrics, Scorecards, Results, and Awards:

```text
Draft/working state
  -> authoritative state
      -> versioned or provenance-preserving correction
```

The system should prefer versioned authority over mutable current-state-only records.

## Working invariants

- Team belongs to exactly one active Division.
- Division changes are corrections, not routine movement.
- Encounter joins one Team and one Panel and preserves actual participant history.
- Each participating Judge authors an independent Scorecard.
- Each Scorecard references an identifiable Rubric version.
- Notes may exist at Criterion and Scorecard scope.
- Finalized Scorecards participate in official aggregation.
- Prior Scorecard versions remain historically available.
- Only the current authoritative Scorecard version contributes to aggregation.
- Manual capture preserves both evaluation and capture provenance.
- Judges do not receive competition-wide scoring/standings through the judging UI.
- Ranking and Award are distinct.
- Historical competitions retain provenance.

Next: **001-D — Judging Model, Anonymity & Evaluation Semantics**.

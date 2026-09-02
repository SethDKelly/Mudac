# 001-G — Experience Principles, Accessibility & Operational Resilience

**Status:** Complete  
**Phase:** 001 — Concept Design Foundation

## Purpose

Translate the conceptual architecture into non-negotiable experience constraints for a live competition environment before screen or component design begins.

The system must remain usable when Judges are first-time users, working from phones, interrupted, under time pressure, on poor connectivity, using assistive technologies, or relying on paper.

## Primary experience objectives

### Judge

> Minimize administrative friction between observing a Team presentation and recording an independent evaluation.

Judge experience should be focused, minimal, private, guided, mobile-first, and task-oriented.

### Organizer

> Provide situational awareness and recoverability across the entire live Competition without requiring constant manual reconciliation.

Organizer experience should be broad, diagnostic, exception-aware, and control-oriented.

The two experiences should not be symmetrical.

## Judging remains cognitively primary

The application must remain secondary to listening, observing, questioning, reasoning, and evaluating.

Judge UI should minimize navigation depth, administrative information, mode switching, and interaction cost during a Team presentation.

## Mobile-first judging

Primary Judge target:

- personal smartphone;
- portrait orientation;
- touch interaction;
- no dependency on hover or wide desktop tables.

Score controls should be large, clearly separated, and have an unmistakable selected state because accidental taps can change competition outcomes.

Routine scoring should be reasonably operable one-handed.

## Evaluation context must remain obvious

A Judge should never reasonably wonder which Team is being scored.

Current Team competition identity and Division should remain prominent throughout Scorecard interaction. Panel/Encounter context should be available where useful.

Moving from one Team Encounter to another must be deliberate enough to prevent accidental scoring under the wrong Team.

## Safe Drafting and autosave

Routine interruption must not destroy already-entered judging work.

Expected interruptions include:

- browser closing;
- application switching;
- phone locking;
- calls/messages;
- navigation mistakes;
- connectivity loss;
- battery/device problems.

The preferred experience behaves as if Drafts autosave. Judges should not need to understand manual save mechanics.

### Saving versus finalizing

These meanings must remain distinct:

- **Saved Draft** — work is preserved but not official.
- **Finalized** — the Judge asserts the evaluation is complete and it may participate in official aggregation.

Autosave must never silently finalize a Scorecard.

## Finalization experience

Finalization should be explicit but not frightening. The system should validate required Criteria, show omissions clearly, and allow authorized versioned amendment later.

A concise review before finalization should make missing scores or anomalies easy to detect.

## Notes

Criterion and overall Notes should remain low-friction. They are optional by default unless a Rubric explicitly requires commentary for a specific case.

Voice input may be used through platform capabilities but must never be required.

## Accessibility principles

Accessibility is a participation requirement, not later polish.

The electronic experience should not depend on:

- perfect vision;
- color perception;
- fine motor precision;
- hearing;
- one specific device;
- touch-only input.

### Color

Color must never be the sole carrier of completion, selection, error, or exception state.

### Text scaling

Increased browser/device text sizes must remain functional without clipping important controls or requiring horizontal scrolling.

### Keyboard

Important interactions, especially Organizer workflows, should remain keyboard-operable.

### Screen readers

Rubric structure, Criterion labels, score options, selected values, Notes, and completion state should expose meaningful semantic structure.

## Paper as accessibility and continuity path

Paper is a supported participation channel, not an error state. It may be preferred or necessary for Judges without suitable devices or where digital interaction is not accessible.

Paper and electronic evaluation must share the same authoritative Rubric semantics.

Digital and paper layouts may differ visually because paper requires handwriting space, print-friendly page structure, and durable identifiers.

## Printable artifact requirements

Printed Rubrics should be intentionally generated rather than relying on browser printing of an arbitrary screen.

They should contain enough context to reconnect the paper evaluation to the exact competition state it represents, potentially including:

- Competition identity;
- Rubric/version identity;
- Team competition identity when assigned;
- Division;
- Panel/Encounter information where appropriate;
- Judge/capture identifiers where appropriate.

No printed material should unnecessarily reveal institutional Team identity to Judges.

## Connectivity degradation is expected

Venue Wi-Fi/cellular service may be overloaded, intermittent, or unavailable.

The system must treat degraded connectivity as an expected operational condition rather than an impossible edge case.

The UI must communicate persistence/synchronization state truthfully. It must never claim `Saved` or `Finalized` unless that state is actually durable according to the eventual architecture.

## Retry and duplicate safety

If Finalize is retried after an ambiguous network response, the system must not create duplicate logical Scorecards.

The conceptual invariant remains:

> One logical Scorecard per Judge Participation per Judging Encounter.

Reconnection should converge safely. Concurrent edits from multiple devices are exceptional and should not silently discard one state.

## Session and device security

Judge sessions should be long enough to support the event without excessive reauthentication but must not remain indefinitely active.

Device loss should have bounded impact through session/access revocation and re-verification.

Shared or loaner devices require clear session clearing so one Judge cannot see another Judge's private evaluation data.

## Event-completion privacy

When live judging ends, ordinary Judge access to private Scorecards, Notes, and judging history should expire.

Expired access must not be bypassable by:

- old bookmarks;
- browser Back;
- stale sessions;
- prior-device state.

Underlying records remain preserved for authorized Organizer use.

Any local persistence used for offline resilience creates a security requirement around retention, encryption, cleanup, shared-device use, and event-completion invalidation. Exact technology is deferred.

## Privacy-aware presentation

Judges should understand that Scorecards and Notes are their private evaluation records. Organizers should recognize when they are viewing sensitive information.

Potential Organizer display/projector modes should avoid exposing Team identity mappings, Judge Notes, or live scoring. This is a future UI projection, not a new concept.

Incidental surfaces must also avoid leakage, including page titles, notifications, exported filenames, print previews, browser history labels, or other metadata.

## Organizer exception-first awareness

During live judging, Organizer value is driven by identifying what needs attention now.

Examples:

- Panel missing a required expertise perspective;
- Team with insufficient Encounter coverage;
- Encounter waiting on a Scorecard;
- Judge with incomplete work;
- paper Scorecard waiting for capture;
- amendment in progress;
- Division correction affecting current derived results.

Organizer views should emphasize operational state and exceptions before live ranking.

## Drillable explainability

When Organizers inspect scoring, they must be able to traverse:

```text
Team aggregate
  -> Encounter
      -> Judge Scorecard
          -> Criterion
              -> Rubric version
              -> revision/provenance
```

This is the experience manifestation of the traceability requirements from 001-D/F.

## Recoverable errors

The system should prevent common high-risk mistakes while supporting explicit traceable correction for legitimate event problems.

Examples include:

- wrong Team selected;
- wrong Division;
- wrong Panel assignment;
- missing Scorecard;
- accidental finalization;
- paper transcription error;
- incorrect Award conferral;
- post-finalization correction.

Prefer withdraw/retire/invalidate/supersede/correct over destructive deletion once meaningful competition history exists.

## Proportional confirmation

Confirmation friction should scale with consequence.

### Low consequence
No extra confirmation for ordinary Draft edits or Notes.

### Moderate consequence
Clear confirmation for Scorecard finalization, Panel replacement, or leaving an incomplete Encounter.

### High consequence
Stronger confirmation and consequence explanation for Division changes after judging, Encounter invalidation, scoring-semantic Rubric changes, Competition finalization, and official Award correction.

## Error communication

Errors should communicate:

1. what went wrong;
2. what state remains safe/preserved;
3. what the user should do next.

A generic `Unable to submit` message is insufficient when a Judge needs to know whether their work survived.

## Competition integrity over convenience

The UI must not expose behavior merely because the backend could technically support it.

Examples that remain intentionally unavailable:

- Judge access to peer Scorecards;
- Judge access to competition standings;
- silent Organizer rewriting of Judge evaluation;
- silent Rubric-semantic mutation under existing Scorecards.

## Result confidence/state

Organizers should be able to distinguish:

```text
Current Aggregate
Coverage state
Provisional Rank
Official Finalized Result
```

Live numbers must not appear more authoritative than they are.

Ranking should not dominate the active-event UI; operational completion and exception handling are more important during judging.

## Join experience

Day-of-event Judge entry should be lightweight:

```text
scan/open event access
  -> identify/reverify
  -> confirm Judge participation
  -> confirm expertise
  -> ready for Panel assignment
```

QR codes may accelerate navigation but must not themselves be treated as proof of authorization.

Panel joining should clearly confirm Judge identity and Panel context.

## Judge in-event history

During active participation, Judges should be able to answer:

- What Panel am I on?
- Which Teams have I judged?
- Did I finish the prior Scorecard?
- Which Scorecards remain incomplete?
- Do I need to amend something?

This history exists for event operation, not permanent archival access. After Event Completion, normal Judge access expires.

## Operational resilience and fallback

The event should have a documented path from electronic-first to paper-assisted operation.

```text
Digital service degraded
  -> distribute authoritative paper Rubrics
  -> judging continues
  -> paper Scorecards preserved
  -> later capture/reconciliation
  -> same Scorecard/aggregation semantics
```

A full digital outage should be operationally painful, not competition-ending.

Recovery must preserve source truth rather than reconstructing evaluation from memory.

## Accessibility and resilience reinforce each other

Examples:

- large controls improve both motor accessibility and on-the-move judging;
- clear state labels help screen readers and busy Organizers;
- paper supports accommodation and disaster recovery;
- autosave supports interruption needs and poor connectivity.

## Progressive disclosure and familiar interaction

Judges should see only the concepts necessary to judge. Organizers may see broader operational complexity.

Prefer familiar buttons, score selectors, text fields, status labels, and straightforward navigation over novel gestures or interaction patterns because many Judges may use the application once.

## Judge experience success criteria

A first-time Judge should be able to:

1. establish participation with minimal assistance;
2. understand Panel assignment;
3. identify the correct Team;
4. understand the Rubric;
5. score required Criteria;
6. add Notes where useful;
7. survive routine interruption without losing work;
8. distinguish Draft from Finalized;
9. amend an evaluation through an authorized path;
10. move to the next Team without confusion;
11. perform the core workflow comfortably on a typical smartphone.

## Organizer experience success criteria

An Organizer should be able to:

1. assess Competition readiness;
2. understand Judge presence/availability;
3. understand and correct Panel composition;
4. identify Teams with insufficient coverage;
5. identify incomplete Scorecards;
6. manage Judge substitutions;
7. enter/verify paper Scorecards;
8. investigate anomalies without corrupting source evaluation;
9. understand revisions;
10. reconcile scoring;
11. determine Rank;
12. confer Awards;
13. generate operational/printable materials;
14. finalize the Competition confidently;
15. later reconstruct the official outcome.

## Initial non-functional requirements

Future architecture must demonstrate support for:

- mobile browser compatibility;
- accessible semantic interaction;
- reliable Draft persistence;
- safe retry/idempotency;
- connectivity degradation handling;
- secure session revocation;
- time-scoped Judge Access;
- sensitive local-data management;
- Versioning and Provenance integrity;
- operational state visibility;
- print-quality Export generation;
- paper/digital provenance convergence;
- recovery without destructive rewriting.

## Technology intentionally deferred

001-G does not select service workers, PWA behavior, IndexedDB, local encryption, WebSockets, polling, Cognito, Lambda, ECS, DynamoDB, Aurora, CloudFront, or any other implementation technology.

Those choices must later answer the experience requirements established here.

## Additional candidates considered and rejected/deferred

- **Recovery** — currently an umbrella across Scorecard, Identity, Access, Versioning, Provenance, and operational fallback rather than a singular concept.
- **Notification** — potentially useful later but not yet required in the core catalog.
- **Scheduling** — potentially useful for Encounter planning but not yet required for the conceptual system to function.

Student UI remains outside current scope.

## Exit criteria

The eventual UI must preserve at least these conditions:

1. first-time Judges can judge from a phone with minimal instruction;
2. Team/Division context remains obvious;
3. peer scoring and standings remain hidden from Judges;
4. Draft work survives reasonable interruption;
5. save and finalize semantics are distinct;
6. amendments are versioned and traceable;
7. accessibility does not rely on color/touch alone;
8. paper remains first-class;
9. paper and electronic paths share Rubric semantics;
10. connectivity degradation is expected;
11. retries cannot duplicate Scorecards;
12. Judge private-data Access expires after live judging;
13. Access expiration does not delete Competition records;
14. shared devices do not leak prior Judge data;
15. Organizers can identify exceptional/incomplete states quickly;
16. correction preserves Provenance;
17. printed artifacts identify authoritative source/version;
18. identity shielding survives digital and print surfaces;
19. live results remain provisional until finalization;
20. technology failure has a defined paper continuity path.

## Exit position

Accessibility, resilience, privacy, and judging integrity reinforce one another rather than existing as separate requirements. The project now has enough behavioral and experience definition to proceed to Phase 001 consolidation before formal concept specification and architecture design.

Next: **001-H — Phase 001 Consolidation & Initial Concept Catalog**.

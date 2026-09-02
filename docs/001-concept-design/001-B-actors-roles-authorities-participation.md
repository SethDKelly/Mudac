# 001-B — Actors, Roles, Authorities & Participation

**Status:** Complete  
**Phase:** 001 — Concept Design Foundation

## Purpose

Separate human identity, event participation, authority, expertise, and grouping so they do not collapse into a single role or RBAC model.

## Actor versus participant

### Actors
Entities capable of intentionally performing actions through the application:

- Administrator
- Organizer
- Judge

### Participants
Entities that participate in competition behavior whether or not they operate the UI:

- Judge
- Team
- Panel as an evaluating grouping
- Team Division membership

A Team is a participant but not currently an application actor.

## Identity is not role

A person is not intrinsically a Judge or Organizer. Role is contextual.

```text
Identity
  -> Participation in Competition A as Organizer
  -> Participation in Competition B as Judge
```

The data model should therefore avoid a permanent global `users.role = judge` interpretation.

## Administrator

Administrator authority is system-scoped. Its purpose is to operate, secure, support, and maintain the application environment.

Technical administrative authority must not automatically confer competition authority. Platform support should not silently permit changing Judge evaluations, Competition rank, or Awards.

## Organizer

Organizer authority is primarily Competition-scoped. Organizers configure and operate the competition, including:

- Competition lifecycle and information;
- Divisions;
- Teams and their administrative/competition identities;
- Rubrics;
- Awards;
- Judge participation;
- Panels and assignments;
- Judging operations;
- manual/paper Scorecard capture;
- scoring review and reconciliation;
- aggregation/ranking visibility;
- finalization.

The initial product may bundle these capabilities into Organizer participation while preserving future ability to delegate them to more specialized roles.

## Judge

Judge is an event participation role, not a permanent account type.

A Judge participation represents a person taking part in a specific Competition for the purpose of independently evaluating student work. First-time and returning Judges use the same conceptual model.

Returning recognition may make re-verification easier, but every annual Competition establishes new participation.

## Expertise is not authority

Academic, Business, and Technical describe Judge perspective/expertise. They do not grant different application permissions.

A Judge may have more than one expertise classification. Panel composition may use a Judge in a particular capacity without assuming that a multi-disciplinary Judge fills multiple required Panel perspectives simultaneously.

## Panel

A Panel is a reusable grouping of Judges who evaluate Teams together.

```text
Panel P07
  Judge A
  Judge B
  Judge C
```

A Panel may evaluate multiple Teams. A Team may be evaluated by multiple Panels. The many-to-many relationship is realized through Judging Encounters.

## Panel membership versus encounter participation

Panel membership is mutable operational state. Historical judging must preserve who actually participated in an Encounter.

Example:

```text
09:00 Panel P07 = A, B, C
11:00 Panel P07 = A, B, D
```

Encounters completed before the replacement retain A, B, C. Later Encounters may contain A, B, D.

## Team participation

A Team participates in one Competition and belongs to exactly one active Division.

```text
Competition
  -> Division
      -> Team
```

Division changes are corrective, not routine lifecycle behavior.

A Team also participates in Judging Encounters as the object being evaluated.

```text
Panel + Team -> Judging Encounter
```

## Judge participation lifecycle

A provisional lifecycle includes:

```text
Registered
  -> Checked In
  -> Eligible for Assignment
  -> Assigned to Panel
  -> Active Judging
  -> Completed/Historical
```

Withdrawal, unavailability, reassignment, or recusal are exceptional paths.

Authentication and participation are separate. Authentication establishes identity continuity; Participation answers what that person is doing in this Competition.

## Individual evaluation authority

Each electronic Scorecard must be attributable to one Judge Participation. Shared Panel credentials are therefore insufficient for the core judging flow.

Judges should generally be able to:

- view event information needed for judging;
- view their Panel context;
- participate in eligible Encounters;
- author and save their own Scorecards;
- finalize their own Scorecards;
- view their own appropriate in-event judging history.

Judges should not generally be able to:

- view peer Scorecards before or after submission through the judging UI;
- change another Judge's evaluation;
- change Team identity or Division;
- define Rubrics;
- change Panel composition;
- alter aggregate scoring;
- view active or historical competition-wide standings through the judging experience.

## Informational independence

A Judge should not see another Judge's scores before forming and submitting their own evaluation. This protects against anchoring and preserves independent judgment.

Competition-wide scoring/standings are Organizer capabilities, not Judge capabilities.

## Organizer capture versus Judge authorship

When a Judge uses paper and an Organizer enters the evaluation electronically:

```text
Evaluation author = Judge
Capture actor      = Organizer
Capture method     = Paper
```

The Organizer does not become the author merely because they transcribed the data.

This creates an important authority distinction:

- **Evaluation authority** — the right to form the judgment.
- **Capture authority** — the right to enter a judgment formed elsewhere.

## Authority is scoped and temporal

Authorization eventually depends on more than role:

```text
Actor/Identity
+ Participation
+ Scope
+ Resource state
+ Competition state/policy
```

Examples include system scope, Competition scope, Encounter scope, and artifact scope.

A Judge's ability to edit a Scorecard depends on authorship, Encounter participation, Scorecard lifecycle state, and competition policy.

## Team identity visibility

A Team has at least two representations:

```text
Administrative Identity -> Organizer
Competition Identity    -> Judge
```

Division is intentionally visible to Judges because it is legitimate competition context. Institutional identity is shielded.

## Working invariants

1. A Team participates in a Competition through exactly one active Division.
2. A Judging Encounter joins one Team with one Panel.
3. A Team may participate in multiple Judging Encounters.
4. A Panel may participate in multiple Judging Encounters.
5. A Judge's Scorecard belongs to a particular Judging Encounter.
6. Each electronic Scorecard is attributable to one Judge Participation.
7. Expertise is distinct from application authority.
8. Panel membership is distinct from Judge identity.
9. Historical Encounter participation cannot be rewritten by later Panel membership changes.
10. Administrative Team identity is not exposed to Judges by default.
11. Judges do not see peer scores before forming/submitting their own judgment.
12. Manual capture does not change evaluation authorship.
13. Technical administrative privilege does not automatically confer competition decision authority.

## Exit position

Canonical separation:

```text
WHO YOU ARE              -> Identity
WHY YOU ARE HERE         -> Participation
WHAT YOU MAY DO          -> Authority/Access
WHAT PERSPECTIVE YOU BRING -> Expertise
WHO YOU JUDGE WITH       -> Panel
WHO YOU ARE JUDGING      -> Judging Encounter + Team
```

Next: **001-C — Competition Lifecycle & Critical Experience Scenarios**.

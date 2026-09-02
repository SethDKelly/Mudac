# 001-E — Candidate Concept Discovery

**Status:** Complete  
**Phase:** 001 — Concept Design Foundation

## Purpose

Apply Daniel Jackson's Concept Design tests to the domain candidates discovered in 001-A through 001-D and determine which ideas appear to deserve independent concept status.

Candidate tests:

- **Purpose** — does the mechanism solve a recognizable user problem?
- **Singularity** — does it have one coherent purpose?
- **Independence** — can it be understood without requiring another concept's behavior?
- **Operational principle** — can its normal use be explained simply?
- **Familiarity** — does it map to a stable mental model?

## Lifecycle privacy refinement

Two lifecycle moments are distinct:

- **Event Completed** — live judging ends.
- **Competition Finalized** — reconciliation, ranking, and Awards are settled.

Working privacy rule:

> Judge records persist; ordinary Judge access does not.

During the active event, Judges may need access to their own completed judging history, Scorecards, Notes, and event information. Once live judging ends, normal Judge access to private evaluation records should expire. Organizers retain the authoritative competition record.

If a post-event correction is needed, a Judge may be reverified and granted temporary, narrowly scoped access to the specific Scorecard being amended.

Data retention and data access are therefore separate concerns.

## Candidate categories

### Core competition candidates

- Competition
- Division
- Team
- Panel
- Judging Encounter
- Rubric
- Scorecard
- Award

### Supporting/reusable candidates

- Identity
- Participation
- Alias / Competition Identity
- Access
- Versioning / Revision
- Provenance
- Export

### Likely subordinate state

- Criterion
- Note
- Expertise
- Panel Membership
- Event Information

### Likely derived mechanisms

- Aggregation
- Evaluation Coverage
- Ranking
- Result projection

### Explicit presentation/implementation mechanisms

- QR Code
- PDF
- Dashboard
- Judge Portal
- Organizer Portal
- authentication provider
- AWS services
- GitHub Actions

## Candidate analysis

### Competition
Purpose: provide the governing lifecycle/context of one competition occurrence. Strong independent candidate.

### Division
Purpose: partition Teams into mutually exclusive populations that should be compared against one another. Strong candidate; more meaningful than a generic tag.

### Team
Purpose: represent the student group participating as one competing unit. Strong domain candidate.

### Alias / Competition Identity
Purpose: expose a context-appropriate pseudonymous identity without revealing underlying administrative identity. Strong reusable candidate.

### Identity
Purpose: establish continuity that actions/participation episodes belong to the same human identity. Strong supporting candidate; authentication technology is deferred.

### Participation
Purpose: represent a person's temporary, scoped involvement in a particular Competition and role. Very strong reusable candidate. Enables event-scoped Judge behavior and historical participation without permanent Judge authority.

### Expertise
Purpose is useful but not independent enough. Treat as Judge Participation state rather than a concept.

### Panel
Purpose: form a reusable group of Judges who collectively conduct multiple Team evaluations. Strong concept candidate.

### Panel Membership
Important relational state but not an independent user-purpose mechanism. Treat as Panel state unless later requirements demonstrate otherwise.

### Judging Encounter
Purpose: represent one occurrence of a Panel evaluating one Team. Essential domain candidate and historical anchor.

### Rubric
Purpose: define a repeatable evaluation instrument and scoring semantics. Essential concept candidate.

### Criterion
Subordinate to Rubric. It has no compelling independent lifecycle at present.

### Scorecard
Purpose: record one Judge's independent evaluation during one Encounter. Essential concept candidate.

### Note
Subordinate Scorecard state. Criterion and overall Notes do not currently justify a standalone concept.

### Finalization
Important recurring lifecycle operation but not currently a standalone concept.

### Versioning
Purpose: allow authoritative artifacts to change without erasing prior states. Strong reusable candidate applicable to Scorecards and Rubrics.

### Provenance
Purpose: explain where authoritative records came from and how they changed. Strong reusable candidate distinct from low-level audit telemetry.

### Manual Capture
Not a separate concept. It is a Scorecard capture path whose different authorship/capture semantics are preserved by Provenance.

### Access
Purpose: govern which actions and disclosures are allowed for a principal, resource/scope, state, and time. Judge access cutoff strongly validates this as an independent concept distinct from Participation.

### Export
Purpose: produce stable distributable/printable representations of authoritative information. Strong supporting candidate. PDF and QR remain representation formats.

### Event Information
Currently Competition state rather than a standalone concept.

### Aggregation
Important computation, but likely derived rather than an independent concept.

### Evaluation Coverage
Important eligibility projection/policy result, but likely derived from Encounters, participating Judges, Scorecards, and policy.

### Ranking
Important derived ordering, not necessarily an independent stateful concept.

### Result
Rejected as a catch-all concept. Results UI may project Aggregate, Coverage, Rank, and Awards without a monolithic Result concept.

### Award
Purpose: recognize a Team for an achievement defined by the Competition. Strong independent candidate because it supports both rank-derived and discretionary recognition.

### Judge / Organizer / Administrator
These are roles/authority contexts rather than necessarily independent concepts. Judge and Organizer are best expressed through Participation; Administrator is primarily system authority.

## Provisional concept catalog after pruning

### Core domain

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

## Privacy classification emerging from discovery

### Private Judge evaluation data

- Scorecards;
- Criterion Notes;
- overall Notes;
- Judge evaluation history;
- revision history.

Ordinary access:

- authoring Judge during authorized event window;
- authorized Organizers according to competition governance/retention.

### Organizer-sensitive Team data

- institution identity;
- Team registration information;
- Team-to-Alias mapping.

### Competition-operational information

- Team competition identity;
- Division;
- Panel assignment;
- event information;
- Rubric.

### Result information

- aggregates;
- coverage;
- rankings;
- Awards.

Organizer-visible by default; Judge visibility is not implied.

## Judge access lifecycle

```text
Identity
  -> Judge Participation
      -> active event Access
          own Scorecards
          own Notes
          own judging history
          event information
      -> historical Participation
          ordinary private-data Access removed
```

Temporary correction access may later be synchronized without restoring broad historical access.

## Boundary questions reserved for 001-F

- Identity versus Participation;
- Participation versus Access;
- Alias versus Team;
- Scorecard/Rubric versus generic Versioning;
- Versioning versus Provenance;
- Panel versus Panel Membership;
- Award definition versus conferral;
- Export versus source/version identity.

## Exit position

Fifteen candidates advance to strict boundary and synchronization analysis:

**Competition, Division, Team, Panel, Judging Encounter, Rubric, Scorecard, Award, Identity, Participation, Alias, Access, Versioning, Provenance, Export.**

Next: **001-F — Concept Boundaries, Independence & Synchronization Candidates**.

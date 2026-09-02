# MUDAC Design Documentation

This directory is the canonical design authority for the MUDAC competition application.

The project is being designed using Daniel Jackson's **Concept Design** methodology. Documentation should therefore preserve the distinction between:

- concepts and their purposes;
- state and actions owned by those concepts;
- synchronizations that coordinate independent concepts;
- invariants that must always hold;
- derived mechanisms such as aggregation and ranking;
- competition policy/configuration;
- UI representations and implementation mechanisms.

The documentation is intentionally written before implementation architecture. AWS hosting and GitHub Actions deployment are known boundary conditions, but specific technologies remain deferred until concept, lifecycle, evaluation, privacy, resilience, and experience requirements are stable.

## Documentation authority

When design decisions change, update the relevant phase document and this index where status or canonical terminology changes. Conversation history is useful working context, but the repository is the durable source of truth.

## Phase 001 — Concept Design Foundation

**Status: Complete**

| Group | Document | Status |
| --- | --- | --- |
| 001-A | [Competition Purpose, Product Boundary & Success](001-concept-design/001-A-purpose-boundary-success.md) | Complete |
| 001-B | [Actors, Roles, Authorities & Participation](001-concept-design/001-B-actors-roles-authorities-participation.md) | Complete |
| 001-C | [Competition Lifecycle & Critical Experience Scenarios](001-concept-design/001-C-lifecycle-critical-scenarios.md) | Complete |
| 001-D | [Judging Model, Anonymity & Evaluation Semantics](001-concept-design/001-D-judging-anonymity-evaluation-semantics.md) | Complete |
| 001-E | [Candidate Concept Discovery](001-concept-design/001-E-candidate-concept-discovery.md) | Complete |
| 001-F | [Concept Boundaries, Independence & Synchronization Candidates](001-concept-design/001-F-concept-boundaries-synchronizations.md) | Complete |
| 001-G | [Experience Principles, Accessibility & Operational Resilience](001-concept-design/001-G-experience-accessibility-resilience.md) | Complete |
| 001-H | [Phase 001 Consolidation & Initial Concept Catalog](001-concept-design/001-H-phase-consolidation-initial-concept-catalog.md) | Complete |

The canonical Phase 001 exit baseline is **001-H**. Earlier documents retain the reasoning and decisions that led to that consolidation and should be updated if a later phase intentionally revises one of their decisions.

## Accepted concept catalog

### Core competition concepts

1. Competition
2. Division
3. Team
4. Panel
5. Judging Encounter
6. Rubric
7. Scorecard
8. Award

### Supporting concepts

9. Identity
10. Participation
11. Alias
12. Access
13. Versioning
14. Provenance
15. Export

Important domain ideas intentionally outside the concept catalog include Criterion, Note, Expertise, Panel Membership, Aggregation, Evaluation Coverage, Rank, Result, PDF, QR, and UI dashboard/portal structures. See 001-H for the authoritative classification and rationale.

## Canonical terminology

- **Team** — the student group being evaluated.
- **Panel** — the group of Judges evaluating Teams together.
- **Judging Encounter** — one bounded occurrence of one Panel evaluating one Team.
- **Judge Participation** — a person's event-scoped participation as a Judge; it is not a permanent global user type.
- **Expertise** — Judge participation metadata such as Academic, Business, or Technical; it is not an access role.
- **Scorecard** — one Judge's independent evaluation during one Judging Encounter.
- **Rubric** — the structured evaluation definition used to create Scorecards.
- **Award** — competition recognition that may be rank-derived or Organizer-conferred.
- **Alias / Competition Identity** — the Team representation exposed during blinded judging instead of administrative/institutional identity.

## Important cross-phase decisions

- A Team belongs to exactly one active Division; changes are corrective rather than ordinary lifecycle behavior.
- A Judging Encounter joins one Team with one Panel and snapshots the Judges who actually participated.
- Each participating Judge authors at most one logical Scorecard per Encounter; revisions do not create additional evaluation weight.
- A finalized Scorecard is authoritative for aggregation but may be amended through a versioned, traceable workflow.
- Missing scores are never interpreted as zero.
- Evaluation Coverage is distinct from numeric Aggregation.
- Rankings are Division-scoped by default and derived from authoritative eligible evaluations.
- Awards are distinct from Rank and may be discretionary.
- Judges do not see peer evaluations or competition-wide scoring/standings through the judging experience.
- Judge Scorecards, Notes, and judging history are private evaluation data. Ordinary Judge access is event/lifecycle-scoped and expires after live judging ends; Organizer access persists according to competition governance needs.
- Event Completed and Competition Finalized are distinct lifecycle states.
- Paper and electronic judging share the same Rubric and scoring semantics.
- Printed/exported materials must be traceable to authoritative source/version information.
- The system must remain operable under mobile, accessibility, network-degradation, device-loss, and paper-fallback scenarios.
- Authoritative state should support controlled correction through Versioning and Provenance rather than silent overwrite or unnecessary absolute immutability.

## Phase 002 — Concept Specification, Policy & Synchronization Refinement

**Status: In Progress**

See the [Phase 002 index](002-concept-specification/README.md) for the specification template and phase-level rationale.

| Group | Topic | Status |
| --- | --- | --- |
| 002-A | [Competition, Division, Team & Alias Specifications](002-concept-specification/002-A-competition-division-team-alias-specifications.md) | **Complete** |
| 002-B | [Identity, Participation & Access Specifications](002-concept-specification/002-B-identity-participation-access-specifications.md) | **Complete** |
| 002-C | Panel, Membership & Judging Encounter Specifications | **Next** |
| 002-D | Rubric, Criterion, Scorecard & Notes Specifications | Planned |
| 002-E | Versioning, Provenance, Correction & Authority Preservation | Planned |
| 002-F | Aggregation, Coverage, Ranking & Evaluation Policy | Planned |
| 002-G | Awards, Reconciliation, Finalization & Official Outcomes | Planned |
| 002-H | Export, Print, Operational Continuity & External Representations | Planned |
| 002-I | Phase 002 Consolidation & Specification Exit Review | Planned |

### 002-A refinements now authoritative

- Competition lifecycle: `Draft → Ready → Active → Event Completed → Finalized`.
- `Historical` is not a separate business lifecycle state; reconciliation is activity between Event Completed and Finalized.
- Temporary incomplete Team setup is permitted only during Competition Draft.
- Before Ready, every non-withdrawn Team must have exactly one active Division and one unique active Alias.
- Division changes are explicit corrections and never rewrite completed Scorecards.
- Division is explicit state and is never inferred from Alias text.
- Alias values already used operationally are never reassigned to another Team in the same Competition.
- Historical Judging Encounters should preserve the Alias presented when judging occurred.

### 002-B refinements now authoritative

- Identity, Participation, and Access are separate concepts: continuity, event-scoped capacity, and current capability/disclosure respectively.
- Judge and Organizer are Competition-scoped Participation roles; Administrator remains primarily system-scoped authority.
- Returning Judges may reuse/reverify Identity but receive a new Participation for each Competition.
- Expertise is Judge Participation state, may be plural, and does not independently grant authority.
- Access is capability-oriented rather than a single broad role grant and may depend on Competition state, ownership, resource sensitivity, scope, purpose, and time.
- Event Completed ends ordinary Judge access to private Scorecards, Notes, and judging history while retaining the historical records.
- Post-event Judge correction uses narrow temporary Access after re-verification rather than reopening broad historical access.
- Dual-role identities remain separable by Participation/Access context.
- Shared-device and lost-device behavior must revoke/clear the prior access context without creating duplicate Identity or Participation.
- System Administrator authority does not automatically confer Competition decision authority; exceptional break-glass access must be bounded and attributable.

## Known architectural boundary

Target deployment is **GitHub Actions → AWS**. The architecture phase must later choose services and topology that satisfy the conceptual requirements rather than reshape the concepts around a preferred AWS service.

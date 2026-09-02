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

When design decisions change, update the relevant phase document and this index where status or canonical terminology changes. Conversation history is useful working context, but the repository should become the durable source of truth.

## Phase 001 — Concept Design Foundation

| Group | Document | Status |
| --- | --- | --- |
| 001-A | [Competition Purpose, Product Boundary & Success](001-concept-design/001-A-purpose-boundary-success.md) | Complete |
| 001-B | [Actors, Roles, Authorities & Participation](001-concept-design/001-B-actors-roles-authorities-participation.md) | Complete |
| 001-C | [Competition Lifecycle & Critical Experience Scenarios](001-concept-design/001-C-lifecycle-critical-scenarios.md) | Complete |
| 001-D | [Judging Model, Anonymity & Evaluation Semantics](001-concept-design/001-D-judging-anonymity-evaluation-semantics.md) | Complete |
| 001-E | [Candidate Concept Discovery](001-concept-design/001-E-candidate-concept-discovery.md) | Complete |
| 001-F | [Concept Boundaries, Independence & Synchronization Candidates](001-concept-design/001-F-concept-boundaries-synchronizations.md) | Complete |
| 001-G | [Experience Principles, Accessibility & Operational Resilience](001-concept-design/001-G-experience-accessibility-resilience.md) | Complete |
| 001-H | Phase 001 Consolidation & Initial Concept Catalog | **Next** |

## Current provisional concept catalog

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

These remain provisional until 001-H consolidates the phase.

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
- Judge Scorecards, Notes, and judging history are private evaluation data. Judge access is event/lifecycle-scoped and should expire after live judging ends; Organizer access persists according to competition governance needs.
- Paper and electronic judging share the same Rubric and scoring semantics.
- Printed/exported materials must be traceable to authoritative source/version information.
- The system must remain operable under mobile, accessibility, network-degradation, device-loss, and paper-fallback scenarios.

## Known architectural boundary

Target deployment is **GitHub Actions → AWS**. The architecture phase must later choose services and topology that satisfy the conceptual requirements rather than reshape the concepts around a preferred AWS service.

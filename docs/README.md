# MUDAC Design Documentation

This directory is the canonical design authority for the MUDAC competition application.

The project is being designed using Daniel Jackson's **Concept Design** methodology. Documentation should therefore preserve the distinction between concepts, concept-owned state/actions, synchronizations, invariants, derived mechanisms, competition policy, UI representations, and implementation mechanisms.

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

The canonical Phase 001 exit baseline is **001-H**.

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

Important domain ideas intentionally outside the concept catalog include Criterion, Note, Expertise, Panel Membership, Aggregation, Evaluation Coverage, Rank, Result, PDF, QR, and UI dashboard/portal structures.

## Canonical terminology

- **Team** — the student group being evaluated.
- **Panel** — the current group of Judge Participations intended to evaluate Teams together.
- **Judging Encounter** — one bounded occurrence of one Panel evaluating one Team, preserving actual judging context.
- **Judge Participation** — a person's Competition-scoped participation as a Judge; not a permanent global user type.
- **Expertise** — Judge Participation metadata such as Academic, Business, or Technical; not an access role.
- **Composition capacity** — the perspective a Judge membership satisfies for a specific Panel; distinct from Expertise.
- **Scorecard** — one Judge's independent evaluation during one Judging Encounter.
- **Rubric** — the structured evaluation definition used to create Scorecards.
- **Award** — competition recognition that may be rank-derived or Organizer-conferred.
- **Alias / Competition Identity** — the Team representation exposed during blinded judging instead of administrative/institutional identity.

## Important cross-phase decisions

- A Team belongs to exactly one active Division; changes are corrective rather than ordinary lifecycle behavior.
- Competition lifecycle is `Draft → Ready → Active → Event Completed → Finalized`.
- Judge and Organizer are Participation roles; Access is capability-, scope-, lifecycle-, and resource-sensitive.
- Returning Judges may reuse/reverify Identity but receive new Competition Participation.
- Ordinary Judge access to private Scorecards, Notes, and judging history expires at Event Completed without deleting records.
- Panel Membership is current/historical Panel state; it does not itself create Scorecard authority.
- Expertise and Panel composition capacity are distinct.
- A Judging Encounter joins one Team and one Panel, snapshots Team Alias/Division and starting participant context, and records later participant adjustments explicitly.
- Actual effective Encounter participants—not nominal Panel membership—determine ordinary Scorecard obligations.
- Recusal/absence are never represented as zero or unexplained missing Scorecards.
- Same Panel + same Team normally yields at most one valid Encounter per Competition; rejudging uses an explicit replacement Encounter.
- Encounter lifecycle is `Prepared → Open → Complete`, with Cancelled and Invalidated exceptional paths.
- Each participating Judge authors at most one logical Scorecard per Encounter; revisions do not create additional evaluation weight.
- Missing scores are never interpreted as zero.
- Evaluation Coverage is distinct from numeric Aggregation.
- Rankings are Division-scoped by default and derived from authoritative eligible evaluations.
- Awards are distinct from Rank and may be discretionary.
- Judges do not see peer evaluations or competition-wide scoring/standings through the judging experience.
- Paper and electronic judging share the same Rubric and scoring semantics.
- Printed/exported materials must be traceable to authoritative source/version information.
- Authoritative state supports controlled correction through Versioning and Provenance rather than silent overwrite.

## Phase 002 — Concept Specification, Policy & Synchronization Refinement

**Status: In Progress**

See the [Phase 002 index](002-concept-specification/README.md).

| Group | Topic | Status |
| --- | --- | --- |
| 002-A | [Competition, Division, Team & Alias Specifications](002-concept-specification/002-A-competition-division-team-alias-specifications.md) | **Complete** |
| 002-B | [Identity, Participation & Access Specifications](002-concept-specification/002-B-identity-participation-access-specifications.md) | **Complete** |
| 002-C | [Panel, Membership & Judging Encounter Specifications](002-concept-specification/002-C-panel-membership-judging-encounter-specifications.md) | **Complete** |
| 002-D | Rubric, Criterion, Scorecard & Notes Specifications | **Next** |
| 002-E | Versioning, Provenance, Correction & Authority Preservation | Planned |
| 002-F | Aggregation, Coverage, Ranking & Evaluation Policy | Planned |
| 002-G | Awards, Reconciliation, Finalization & Official Outcomes | Planned |
| 002-H | Export, Print, Operational Continuity & External Representations | Planned |
| 002-I | Phase 002 Consolidation & Specification Exit Review | Planned |

### Authoritative Phase 002 refinements so far

**002-A:** structural incompleteness is tolerated only during Draft; before Ready each non-withdrawn Team has exactly one active Division and unique active Alias; Division/Alias corrections preserve stable Team identity and history.

**002-B:** Identity, Participation, and Access remain independent; Access is capability-oriented; Event Completed ends ordinary Judge private-data access; post-event correction uses narrow temporary Access; Administrator system authority does not automatically confer Competition authority.

**002-C:** Panel describes intended Judge grouping while Encounter preserves actual Team evaluation occurrence. Panel membership changes do not rewrite prior Encounters. Encounter start snapshots Alias, Division, Panel context, and starting Judge participants; later recusal/absence/replacement is an explicit adjustment. Effective Encounter participants drive Scorecard obligations. Duplicate initiation must converge on one Encounter, and rejudging is explicit replacement rather than accidental double influence.

## Known architectural boundary

Target deployment is **GitHub Actions → AWS**. The architecture phase must later choose services and topology that satisfy the conceptual requirements rather than reshape the concepts around a preferred AWS service.

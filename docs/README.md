# MUDAC Design Documentation

This directory is the canonical design authority for the MUDAC competition application.

The project is being designed using Daniel Jackson's **Concept Design** methodology. Documentation preserves the distinction between concepts, concept-owned state/actions, synchronizations, invariants, derived mechanisms, competition policy, UI representations, and implementation mechanisms.

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

Aggregation, Evaluation Coverage, Rank, Criterion, Note, Expertise, Panel Membership, Result, PDF, QR, and dashboard/portal structures remain intentionally outside the standalone concept catalog.

## Canonical terminology

- **Team** — the student group being evaluated.
- **Panel** — the current group of Judge Participations intended to evaluate Teams together.
- **Judging Encounter** — one bounded occurrence of one Panel evaluating one Team, preserving actual judging context.
- **Judge Participation** — a person's Competition-scoped participation as a Judge; not a permanent global user type.
- **Expertise** — Judge Participation metadata such as Academic, Business, or Technical; not an access role.
- **Composition capacity** — the perspective a Judge membership satisfies for a specific Panel; distinct from Expertise.
- **Rubric** — the evaluation definition governing valid Criterion responses and one Judge's Scorecard calculation.
- **Criterion** — one scored dimension inside a Rubric; subordinate Rubric state.
- **Scorecard** — one logical Judge evaluation during one Judging Encounter under one exact Rubric Version.
- **Version** — one immutable authoritative snapshot within a versioned subject lineage.
- **Provenance** — meaningful origin, actor/author authority, source, reason, and transformation history of authoritative records.
- **Coverage** — derived sufficiency of qualifying evaluation; distinct from Aggregate.
- **Aggregate** — derived numerical combination of eligible authoritative Scorecards.
- **Rank** — derived Division-scoped ordering of rank-eligible Teams.
- **Award** — competition recognition with explicit scope/selection semantics; may be rank-derived or discretionary.
- **Official Outcome Revision** — authoritative reconstructible snapshot/projection of the Competition outcome established at Finalization; not a standalone Result Concept.
- **Alias / Competition Identity** — the Team representation exposed during blinded judging instead of administrative/institutional identity.

## Phase 002 — Concept Specification, Policy & Synchronization Refinement

**Status: In Progress**

See the [Phase 002 index](002-concept-specification/README.md).

| Group | Topic | Status |
| --- | --- | --- |
| 002-A | [Competition, Division, Team & Alias Specifications](002-concept-specification/002-A-competition-division-team-alias-specifications.md) | **Complete** |
| 002-B | [Identity, Participation & Access Specifications](002-concept-specification/002-B-identity-participation-access-specifications.md) | **Complete** |
| 002-C | [Panel, Membership & Judging Encounter Specifications](002-concept-specification/002-C-panel-membership-judging-encounter-specifications.md) | **Complete** |
| 002-D | [Rubric, Criterion, Scorecard & Notes Specifications](002-concept-specification/002-D-rubric-criterion-scorecard-notes-specifications.md) | **Complete** |
| 002-E | [Versioning, Provenance, Correction & Authority Preservation](002-concept-specification/002-E-versioning-provenance-correction-authority-preservation.md) | **Complete** |
| 002-F | [Aggregation, Coverage, Ranking & Evaluation Policy](002-concept-specification/002-F-aggregation-coverage-ranking-evaluation-policy.md) | **Complete** |
| 002-G | [Awards, Reconciliation, Finalization & Official Outcomes](002-concept-specification/002-G-awards-reconciliation-finalization-official-outcomes.md) | **Complete** |
| 002-H | Export, Print, Operational Continuity & External Representations | **Next** |
| 002-I | Phase 002 Consolidation & Specification Exit Review | Planned |

## Important cross-phase decisions

- Competition lifecycle is `Draft → Ready → Active → Event Completed → Finalized`.
- A Team belongs to exactly one active Division; Division/Alias correction preserves stable Team identity and historical judging context.
- Judge and Organizer are Participation roles; Access is capability-, scope-, lifecycle-, and resource-sensitive.
- Ordinary Judge private evaluation access expires at Event Completed without deleting records.
- Panel describes intended Judge grouping; Encounter preserves the actual judging occurrence and effective participants.
- Recusal/absence is never represented as zero or unexplained missing evaluation.
- Every authoritative Scorecard uses one exact Rubric Version and one Judge × Encounter logical identity.
- Scored Criteria are required in the initial model; missing, zero, and N/A remain distinct.
- Scorecard Drafts are non-authoritative; finalized Versions are authoritative; Amendment Drafts leave the prior Version authoritative until committed.
- Notes are versioned private evaluation evidence and do not secretly alter numeric scoring.
- Paper and electronic judging share evaluation semantics while Provenance preserves authorship/capture distinctions.
- Committed Versions are immutable historical snapshots; correction creates successor state or explicit invalidation/replacement rather than rewriting history.
- Correction authority follows semantic authority: Organizer/Administrator authority does not silently substitute for Judge judgment.
- Coverage and Aggregate are separate derived dimensions.
- The default Team Aggregate gives equal weight to eligible authoritative individual Judge Scorecards; Encounter means are analytical only.
- Missing evaluations are never zero; accepted Coverage exceptions never fabricate scores or hide actual shortfall.
- There is no hidden Judge normalization or automatic outlier removal in the baseline.
- Scorecards are pooled only across aggregation-compatible Rubric Versions; scoring-semantic changes are incompatible by default and are not implicitly rescaled.
- Rank is Division-scoped and derived rather than editable.
- Ranking comparison precision is explicit and distinct from display rounding.
- True ties are never broken by incidental implementation data; without a declared resolver they remain shared.
- Evaluation Policy becomes authoritative/reconstructible once judging begins because rule changes can alter outcomes without changing Judge evidence.
- Reconciliation is an Organizer closeout activity, not another Competition lifecycle state or Concept.
- A computable Ranking is not automatically ranking ready; unresolved evidence, Coverage, policy, correction, tie, or Award issues may still block closeout.
- Award remains distinct from Rank and carries explicit scope, selection method, eligibility/cardinality, and conferral history.
- Rank-derived Award candidates are derived from authoritative Ranking and Organizer-confirmed by default; confirmation cannot arbitrarily contradict the rank rule.
- Finalization is an explicit high-consequence Organizer action gated by reconciled evidence, ranking-ready Divisions, authoritative policy, resolved required Awards, and absence of unresolved outcome-affecting issues.
- Finalization creates an Official Outcome Revision that preserves the authoritative basis of the declared outcome rather than only setting a boolean flag.
- Post-finalization corrections preserve prior official outcome revisions and require explicit successor confirmation; official outcomes never silently migrate.
- Competition Finalization and public publication/disclosure are separate. Finalization does not automatically expose results or restore Judge access.

## Known architectural boundary

Target deployment is **GitHub Actions → AWS**. Architecture must later choose services and topology that satisfy these specifications rather than reshape the domain around a preferred AWS service.

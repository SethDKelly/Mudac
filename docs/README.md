# MUDAC Design Documentation

This directory is the canonical design authority for the MUDAC competition application.

The project is being designed using Daniel Jackson's **Concept Design** methodology. Conversation history is working context; the repository is the durable source of truth.

## Phase 001 — Concept Design Foundation

**Status: Complete**

Canonical exit baseline: [001-H — Phase 001 Consolidation & Initial Concept Catalog](001-concept-design/001-H-phase-consolidation-initial-concept-catalog.md).

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

Aggregation, Evaluation Coverage, Rank, Criterion, Note, Expertise, Panel Membership, Reconciliation, Evaluation Policy, Official Outcome Revision, Team Attribute Definitions, PDF, QR, and dashboard/portal structures remain subordinate, derived, policy, process, metadata, or representation mechanisms rather than standalone Concepts.

## Phase 002 — Concept Specification, Policy & Synchronization Refinement

**Status: Complete**

Canonical exit baseline: [002-I — Phase 002 Consolidation & Specification Exit Review](002-concept-specification/002-I-phase-consolidation-specification-exit-review.md).

Compatible post-exit refinement: [002-A1 — Team Extensible Attributes & Team Name](002-concept-specification/002-A1-team-extensible-attributes-team-name-refinement.md).

### Phase 002 authoritative baseline

- Competition lifecycle is `Draft → Ready → Active → Event Completed → Finalized`.
- Identity, Participation, Access, and semantic authority are distinct.
- Team supports extensible descriptive attributes; optional `teamName` remains distinct from Alias and non-competitive by default.
- Panel current membership and historical Encounter participation are distinct.
- effective Encounter participants create Scorecard obligations.
- one Judge Participation × one Encounter yields at most one logical Scorecard.
- every Scorecard uses one exact Rubric Version.
- Drafts are non-authoritative; committed Versions are immutable historical snapshots.
- Judge amendment, transcription correction, structural correction, supersession, and invalidation remain distinct.
- Coverage and Aggregate remain independent.
- default Team Aggregate equally weights eligible authoritative individual Judge Scorecards.
- Rank is Division-scoped and derived.
- Evaluation Policy is reconstructible once judging begins.
- Award remains distinct from Rank.
- Finalization creates an Official Outcome Revision and remains separate from publication.
- Export represents identified source state and does not replace source truth.
- paper and electronic judging share evaluation semantics.
- paper-origin capture is verified against its physical source before official eligibility.
- operational fallback changes capture channel, never evaluation meaning or weight.

## Phase 003 — Conceptual UX Architecture, Information Architecture & Interaction Model

**Status: In Progress**

See the [Phase 003 index](003-conceptual-ux-architecture/README.md).

| Group | Topic | Status |
| --- | --- | --- |
| 003-A | [Experience Architecture, Role Modes & Navigation Model](003-conceptual-ux-architecture/003-A-experience-architecture-role-modes-navigation-model.md) | **Complete** |
| 003-B | [Judge Entry, Identity, Participation & Panel Onboarding](003-conceptual-ux-architecture/003-B-judge-entry-identity-participation-panel-onboarding.md) | **Complete** |
| 003-C | [Judge Encounter, Rubric, Scorecard & Amendment Experience](003-conceptual-ux-architecture/003-C-judge-encounter-rubric-scorecard-amendment-experience.md) | **Complete** |
| 003-D | [Organizer Competition Setup, Configuration & Readiness Experience](003-conceptual-ux-architecture/003-D-organizer-competition-setup-configuration-readiness-experience.md) | **Complete** |
| 003-E | [Organizer Judge, Panel, Encounter & Live Operations Experience](003-conceptual-ux-architecture/003-E-organizer-judge-panel-encounter-live-operations-experience.md) | **Complete** |
| 003-F | [Reconciliation, Coverage, Ranking, Awards & Finalization Experience](003-conceptual-ux-architecture/003-F-reconciliation-coverage-ranking-awards-finalization-experience.md) | **Complete** |
| 003-G | [Paper Capture, Export, Print & Publication Experience](003-conceptual-ux-architecture/003-G-paper-capture-export-print-publication-experience.md) | **Complete** |
| 003-H | Accessibility, Mobile, Responsive & Degraded-Mode Interaction Architecture | **Next** |
| 003-I | Cross-Cutting Status, Feedback, Privacy, Disclosure & Recovery Patterns | Planned |
| 003-J | Phase 003 Consolidation & UX Architecture Exit Review | Planned |

### Phase 003 authoritative UX baseline through 003-G

The experience context stack is:

```text
Identity
   ↓
Participation / role mode
   ↓
Competition
   ↓
role-specific operational context
   ↓
current task / artifact
```

Judge onboarding establishes verified current-event Participation, check-in, Panel context, and derived readiness. Judge evaluation preserves one Draft through scoring/Notes and uses explicit Finalization plus separate amendment semantics; peer scoring and standings remain hidden.

Organizer preparation is non-linear with derived configuration readiness and separate operational warnings. Organizer live operations are exception-first rather than leaderboard-first and preserve the boundary between process authority and Judge authorship. Event completion ends ordinary live judging but carries unresolved permitted work into reconciliation.

Reconciliation begins with evidence authority, Coverage/eligibility, Rubric compatibility, corrections, and ties rather than results presentation. Coverage remains independent from Aggregate. Ranking may be calculated without being ranking-ready; Rank is never directly edited. Awards follow declared rank-derived or discretionary semantics. Finalization is explicit and creates an Official Outcome Revision without publishing it; corrected calculations do not silently replace an official revision.

Paper capture now uses the authority chain:

```text
physical source
      ↓
unique paper source reference
      ↓
capture Draft
      ↓
verification against source
      ↓
authoritative Scorecard Version
```

The Judge remains evaluation author while the Organizer remains capture actor. Ambiguous physical intent cannot be guessed. A post-verification transcription correction is distinct from a Judge amendment. Electronic and paper artifacts for the same Judge × Encounter converge on one logical Scorecard.

External representation now uses:

```text
authoritative source Version / Official Outcome Revision
      +
audience / disclosure profile
      +
purpose
      ↓
Export
      ↓
preview / validation
      ↓
print / distribute / publish
```

Artifacts can become stale or superseded without changing their historical source. Organizer visibility does not imply disclosure permission. Finalized is not published; official result publication requires an Official Outcome Revision and explicit release. Corrected outcomes mark prior publications affected and require deliberate successor publication rather than silent rewrite.

## Canonical terminology

- **Team** — student group being evaluated; supports extensible descriptive attributes including optional `teamName`.
- **Team Name** — optional descriptive Team attribute; distinct from Alias and non-competitive by default.
- **Panel** — group of Judge Participations intended to evaluate together.
- **Judging Encounter** — one bounded actual Panel–Team evaluation occurrence.
- **Judge Participation** — Competition-scoped Judge capacity.
- **Rubric** — evaluation definition.
- **Scorecard** — one logical Judge evaluation for one Encounter under one Rubric Version.
- **Version** — immutable authoritative snapshot.
- **Provenance** — meaningful origin/authority/change history.
- **Coverage** — sufficiency of qualifying evaluation.
- **Aggregate** — numerical combination of eligible authoritative Scorecards.
- **Rank** — derived Division ordering.
- **Award** — explicit Competition recognition.
- **Official Outcome Revision** — reconstructible authoritative Competition outcome snapshot.
- **Export** — audience-specific external representation tied to identified source state.
- **Alias / Competition Identity** — Judge-facing Team identity used instead of administrative/institutional identity.

## Known architectural boundary

Target deployment remains **GitHub Actions → AWS**. Front-end framework, component architecture, identity provider, API style, persistence model, offline technology, artifact infrastructure, real-time transport, OCR/scanning, publication infrastructure, and AWS services remain downstream decisions that must satisfy the Concept and UX architecture rather than redefine it.

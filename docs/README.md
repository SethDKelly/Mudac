# MUDAC Design Documentation

This directory is the canonical design authority for the MUDAC competition application.

The project is being designed using Daniel Jackson's **Concept Design** methodology. Documentation preserves the distinction between concepts, concept-owned state/actions, synchronizations, invariants, derived mechanisms, competition policy, UX representations, and implementation mechanisms.

Conversation history is working context; the repository is the durable source of truth.

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

| Group | Topic | Status |
| --- | --- | --- |
| 002-A | [Competition, Division, Team & Alias](002-concept-specification/002-A-competition-division-team-alias-specifications.md) | Complete |
| 002-A1 | [Team Extensible Attributes & Team Name Refinement](002-concept-specification/002-A1-team-extensible-attributes-team-name-refinement.md) | Complete refinement |
| 002-B | [Identity, Participation & Access](002-concept-specification/002-B-identity-participation-access-specifications.md) | Complete |
| 002-C | [Panel, Membership & Judging Encounter](002-concept-specification/002-C-panel-membership-judging-encounter-specifications.md) | Complete |
| 002-D | [Rubric, Criterion, Scorecard & Notes](002-concept-specification/002-D-rubric-criterion-scorecard-notes-specifications.md) | Complete |
| 002-E | [Versioning, Provenance, Correction & Authority Preservation](002-concept-specification/002-E-versioning-provenance-correction-authority-preservation.md) | Complete |
| 002-F | [Aggregation, Coverage, Ranking & Evaluation Policy](002-concept-specification/002-F-aggregation-coverage-ranking-evaluation-policy.md) | Complete |
| 002-G | [Awards, Reconciliation, Finalization & Official Outcomes](002-concept-specification/002-G-awards-reconciliation-finalization-official-outcomes.md) | Complete |
| 002-H | [Export, Print, Operational Continuity & External Representations](002-concept-specification/002-H-export-print-operational-continuity-external-representations.md) | Complete |
| 002-I | [Phase 002 Consolidation & Specification Exit Review](002-concept-specification/002-I-phase-consolidation-specification-exit-review.md) | Complete |

### Phase 002 authoritative baseline

- Competition lifecycle is `Draft → Ready → Active → Event Completed → Finalized`.
- Current operational state and historical observed state remain separately representable.
- Identity, Participation, Access, and semantic authority are distinct.
- Judge and Organizer are Competition-scoped Participation roles.
- ordinary Judge access to private evaluation data expires at Event Completed without deleting records.
- Team supports extensible descriptive attributes; `teamName` is a standard optional attribute distinct from Alias and carries no competitive effect by default.
- Team-attribute disclosure is explicit; student-created Team names are not Judge-visible by default during blinded judging.
- Panel current membership and historical Encounter participation are distinct.
- effective Encounter participants create Scorecard obligations.
- one Judge Participation × one Encounter yields at most one logical Scorecard.
- every Scorecard uses one exact authoritative Rubric Version.
- Drafts are non-authoritative; committed Versions are immutable historical snapshots.
- Judge amendment, transcription correction, structural correction, supersession, and invalidation remain distinct.
- Coverage and Aggregate are independent.
- the default Team Aggregate equally weights eligible authoritative individual Judge Scorecards.
- missing evaluation is never zero; Coverage exceptions never fabricate evidence.
- Judges are not silently normalized; outliers are not automatically excluded.
- incompatible Rubric Versions are not silently pooled or rescaled.
- Rank is Division-scoped and derived.
- Evaluation Policy is reconstructible once judging begins.
- Award remains distinct from Rank.
- Finalization is reconciled and creates an Official Outcome Revision.
- prior Official Outcome Revisions survive later correction.
- Finalization and public publication are separate.
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
| 003-E | Organizer Judge, Panel, Encounter & Live Operations Experience | **Next** |
| 003-F | Reconciliation, Coverage, Ranking, Awards & Finalization Experience | Planned |
| 003-G | Paper Capture, Export, Print & Publication Experience | Planned |
| 003-H | Accessibility, Mobile, Responsive & Degraded-Mode Interaction Architecture | Planned |
| 003-I | Cross-Cutting Status, Feedback, Privacy, Disclosure & Recovery Patterns | Planned |
| 003-J | Phase 003 Consolidation & UX Architecture Exit Review | Planned |

### 003-A authoritative UX baseline

The application experience context is:

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

Judge and Organizer are explicit experience modes. Judge experience remains narrow around event context, Panel context, current judging, and temporary own judging history. Organizer experience is organized around Competition operating modes—preparation, live operations, reconciliation, outcomes, and external/material workflows. Current/historical state and source authority must remain unambiguous; Organizer situational awareness is exception-first and drillable to source evidence.

### 003-B authoritative UX baseline

Judge onboarding proceeds from event entry through Identity/reverification, current Competition Participation, expertise/profile confirmation, check-in, Organizer-governed Panel context, and derived `Ready to Judge`. QR/link/code possession never grants authority, and successful login is not equivalent to readiness. Dual-role users enter explicit Judge mode, shared devices clear prior context, and ordinary Judge onboarding closes at Event Completed.

### 003-C authoritative UX baseline

The Judge evaluation experience confirms Team Alias + Division before scoring, maintains persistent context, embeds Rubric guidance/Notes into a phone-first Draft workflow, and separates presentation end from Scorecard Finalization. Draft persistence is automatic-feeling but truthful; unfinished Drafts may be retained when the event must proceed. Finalization is explicit and retry-safe, and amendment is a separate mode with prior authority preserved until successor Finalization. Peer scoring, aggregates, Coverage, Rank, and standings stay hidden.

### 003-D authoritative UX baseline

Organizer preparation is a non-linear workspace spanning Competition details, Divisions, Teams and attributes, Aliases, Rubric, Evaluation Policy, Awards, Judge/Panel preparation, and materials. One cross-workstream readiness assessment distinguishes hard domain blockers from operational warnings.

Readiness is derived from source truth rather than manual checklist completion. Active Team structural coherence, valid Aliases, a usable authoritative Rubric, valid Evaluation Policy, and configured required Award definitions can act as hard gates. Expected-Judge completeness, day-of-event Panel staffing, and material generation are operational readiness conditions unless policy explicitly promotes them into blockers.

Team setup supports bulk intake with preview/validation/exception handling. Team attributes remain typed and disclosure-controlled; Team Name is optional/non-competitive and hidden from Judges by default. Alias generation validates uniqueness and identity safety. Judge-safe preview allows disclosure review without impersonating Judge authority.

Rubric working Drafts remain distinct from the authoritative judging basis. Evaluation Policy and Coverage/tie semantics are visible, understandable configuration rather than hidden constants. Award definitions distinguish rank-derived from discretionary recognition. `Mark Ready` is an explicit Organizer lifecycle transition only after derived gates pass; warnings persist into event-day operation. Ready-state changes trigger reassessment, and readiness-invalidating changes explicitly return the Competition to Draft rather than leaving stale Ready status.

## Canonical terminology

- **Team** — student group being evaluated; supports extensible descriptive attributes including optional `teamName`.
- **Team Name** — optional descriptive/student-facing Team attribute; distinct from Alias and non-competitive by default.
- **Panel** — current group of Judge Participations intended to evaluate Teams together.
- **Judging Encounter** — one bounded actual Panel–Team evaluation occurrence.
- **Judge Participation** — Competition-scoped Judge capacity, not a permanent user type.
- **Expertise** — Judge Participation metadata, not an access role.
- **Composition capacity** — perspective a Judge satisfies on a Panel.
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

Target deployment remains **GitHub Actions → AWS**. Front-end framework, component architecture, identity provider, API style, persistence model, offline technology, artifact infrastructure, and AWS services remain downstream decisions that must satisfy the Concept and UX architecture rather than redefine it.

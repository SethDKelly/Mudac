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
| 003-E | [Organizer Judge, Panel, Encounter & Live Operations Experience](003-conceptual-ux-architecture/003-E-organizer-judge-panel-encounter-live-operations-experience.md) | **Complete** |
| 003-F | Reconciliation, Coverage, Ranking, Awards & Finalization Experience | **Next** |
| 003-G | Paper Capture, Export, Print & Publication Experience | Planned |
| 003-H | Accessibility, Mobile, Responsive & Degraded-Mode Interaction Architecture | Planned |
| 003-I | Cross-Cutting Status, Feedback, Privacy, Disclosure & Recovery Patterns | Planned |
| 003-J | Phase 003 Consolidation & UX Architecture Exit Review | Planned |

### Phase 003 authoritative UX baseline through 003-E

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

Judge onboarding establishes a trustworthy current Competition Participation, check-in, Panel context, and derived Ready-to-Judge state. The Judge's live evaluation then confirms Team Alias/Division, preserves a Draft through Rubric scoring/Notes, and uses explicit Finalization and separate amendment semantics. Peer scoring, Aggregate, Coverage, Rank, and standings remain hidden from Judges.

Organizer preparation is a non-linear workspace with derived configuration readiness and separate operational warnings. Source truth, not manual checklist completion, determines readiness. Team attributes and Team Name remain disclosure-controlled metadata, authoritative Rubric/Policy state is explicit, and Judge-safe previews support anonymity review.

Organizer live operations are exception-first rather than leaderboard-first. Activation is explicit after Ready remains valid. Judge readiness is derived; Panel composition is explainable; permanent Panel changes remain distinct from one-off Encounter substitutions; and current roster edits never rewrite historical Encounter participants. Encounter operations preserve starting participants plus adjustments, distinguish recusal/absence/substitution, prevent accidental duplicates, and preserve cancellation versus invalidation semantics.

Organizer evaluation monitoring prioritizes obligation status over Judge content. Complete Drafts are not Finalized, uncertain Finalization remains uncertain, amendment Drafts do not make prior finalized evidence missing, and structural attribution errors route to governed correction rather than casual editing. Mixed electronic/paper operation may occur by Panel or Judge, but capture-channel changes never change evaluation weight. Existing electronic Draft plus paper fallback is a duplicate-risk to reconcile, not another vote.

Organizer authority runs process integrity rather than Judge judgment. Ordinary live views avoid casual Judge Note exposure and do not center live Rank. `completeEvent` explicitly ends live judging and ordinary Judge private access while unresolved permitted evidence/capture issues remain visible for reconciliation; it does not Finalize Competition results.

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

Target deployment remains **GitHub Actions → AWS**. Front-end framework, component architecture, identity provider, API style, persistence model, offline technology, artifact infrastructure, real-time transport, and AWS services remain downstream decisions that must satisfy the Concept and UX architecture rather than redefine it.

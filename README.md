# MUDAC Competition Demo

MUDAC is a documentation-first design effort for a web application that supports live student data competitions, with MinneMUDAC as the initial reference context. The product is intended to replace or augment paper-heavy judging operations while preserving fairness, judge independence, accessibility, auditability, and operational resilience.

The design is being developed using Daniel Jackson's **Concept Design** methodology. Product purpose, Concepts, behavioral specifications, and conceptual UX architecture are stabilized. Phase 004 now establishes the repository knowledge architecture and documentation-governance layer before system/application architecture proceeds.

## Product intent

Student Teams analyze a supplied dataset and present findings and methodology to Panels of volunteer Judges. Each Judge independently completes a Rubric-based Scorecard for a Team during a Judging Encounter. Eligible authoritative Scorecards are combined under explicit Evaluation Policy to support Coverage assessment, Division-scoped ranking, Awards, and controlled official closeout.

Judge and Organizer are Competition-scoped Participation roles rather than permanent Identity types. Students are currently Competition participants and beneficiaries, not application actors.

Teams may carry extensible descriptive attributes. The initial standard optional attribute is `teamName`, allowing students to choose a memorable name without changing stable Team identity, Division, Alias, evaluation, or ranking semantics. Student-created Team names are hidden from Judges by default during blinded judging; Alias remains the Judge-facing Competition Identity.

## Core design principles

- **Independent judgment** — each Judge authors an individual Scorecard; Panel and Team results are derived.
- **Traceable aggregation** — outcomes remain decomposable to eligible Scorecards, Criteria, Rubric Versions, Provenance, and Evaluation Policy.
- **Controlled identity disclosure** — Judge-visible identity uses Alias + Division; optional Team metadata remains separately disclosure-controlled.
- **Extensible Team metadata without hidden rules** — descriptive attributes do not automatically gain scoring/ranking semantics.
- **Configurable competition policy** — Divisions, Rubrics, Awards, Panel composition, Coverage, precision, and tie behavior are configuration rather than constants.
- **Controlled finality** — authoritative state is correctable through Versioning and Provenance instead of silent overwrite.
- **Authority preservation** — Organizer/system authority does not silently substitute for Judge judgment.
- **Process integrity over Organizer score control** — live administration coordinates operations without becoming Judge authorship.
- **Capture-channel parity** — paper and electronic judging share evaluation semantics and converge on one logical Judge × Encounter evaluation.
- **Coverage before outcome confidence** — Aggregate and sufficiency of judging remain separate.
- **Explainable ranking** — Rank is derived and never directly edited.
- **Calculated is not official** — a Ranking may exist while not ranking-ready; latest corrected calculations do not silently replace an official outcome.
- **Explicit official closeout** — Finalization produces a reconstructible Official Outcome Revision.
- **Official is not automatically public** — result publication remains a separate release action.
- **Traceable external representation** — printed/downloaded/published artifacts stay tied to exact source state and audience disclosure.
- **Accessibility as semantic parity** — alternate input, assistive technology, viewport, device, or capture channel preserves Competition meaning and authority.
- **Paper continuity** — paper is a first-class accessibility/continuity path and converges on the same Scorecard model.
- **Role-aware experience** — Participation context determines Judge/Organizer mode and disclosure posture.
- **Derived readiness** — Competition, Ranking, and Finalization readiness come from source state and policy, not checkboxes.
- **Exception-first operations** — Organizer live/reconciliation views prioritize unresolved process/evidence/fairness conditions over leaderboard spectacle.
- **Draft-safe judging** — evaluation remains a non-authoritative Draft until explicit Finalization; amendment is separate afterward.
- **Mobile-first judging** — Judge workflow targets personal smartphones under live-event conditions.
- **Truthful persistence and authority** — connectivity uncertainty is never presented as confirmed Finalization, lifecycle transition, correction, or publication.
- **Multidimensional status** — workflow, authority, readiness, validity, freshness, severity, disclosure, and publication remain distinct even when visually summarized.
- **Qualified finality language** — `Ready`, `Complete`, `Finalized`, `Current`, `Official`, `Published`, and `Resolved` are qualified by subject whenever ambiguity is possible.
- **Privacy by lifecycle and representation** — ordinary Judge private-evaluation access ends with live judging, and every view/export/search result applies its target disclosure context.
- **Recovery without semantic drift** — recovery preserves work and explains known state without silently overwriting newer authority, relabeling context, or creating duplicate evaluation weight.
- **Canonical knowledge over duplicated restatement** — normative rules should have one canonical owner; dependent knowledge should cross-reference that authority unless a bounded restatement is needed for independent auditability.
- **Progressive knowledge retrieval** — humans and agents should navigate indexes to canonical knowledge and load historical phase records only when rationale/provenance is needed.
- **Technology follows semantics** — frameworks, databases, offline libraries, APIs, and AWS services must satisfy the Concept/UX/knowledge contracts rather than redefine them.

## Accepted concept catalog

### Core competition concepts

- Competition
- Division
- Team
- Panel
- Judging Encounter
- Rubric
- Scorecard
- Award

### Supporting concepts

- Identity
- Participation
- Alias
- Access
- Versioning
- Provenance
- Export

Aggregation, Coverage, Rank, Criterion, Note, Expertise, Panel Membership, Reconciliation, Evaluation Policy, Official Outcome Revision, Team Attribute Definitions, status, recovery, publication, QR/PDF, and offline mode remain subordinate/derived/policy/process/metadata/representation/implementation mechanisms rather than standalone Concepts.

## Design status

**Phase 001 — Concept Design Foundation: Complete.**

Canonical exit: [`001-H`](docs/001-concept-design/001-H-phase-consolidation-initial-concept-catalog.md).

**Phase 002 — Concept Specification, Policy & Synchronization Refinement: Complete.**

Canonical exit: [`002-I`](docs/002-concept-specification/002-I-phase-consolidation-specification-exit-review.md).

Compatible refinement: [`002-A1`](docs/002-concept-specification/002-A1-team-extensible-attributes-team-name-refinement.md).

**Phase 003 — Conceptual UX Architecture, Information Architecture & Interaction Model: Complete.**

Canonical exit: [`003-J`](docs/003-conceptual-ux-architecture/003-J-phase-consolidation-ux-architecture-exit-review.md).

**Phase 004 — Knowledge Architecture, OKF Retrofit & Documentation Governance: In Progress.**

| Group | Topic | Status |
| --- | --- | --- |
| 004-A | [OKF Adoption Authority, Methodology Compatibility & Terminology Contract](docs/004-knowledge-architecture/004-A-okf-adoption-authority-methodology-compatibility-terminology-contract.md) | **Complete** |
| 004-B | Knowledge Bundle Topology, Canonical Authority Layers & Progressive Disclosure | **Next** |
| 004-C | Canonical Concept, Policy, Invariant & Experience Knowledge Extraction | Planned |
| 004-D | Historical Phase Migration, Provenance & Source-Lineage Retrofit | Planned |
| 004-E | Cross-Reference, Stable Rule-ID & Restatement Reduction Retrofit | Planned |
| 004-F | Documentation Governance, Agent Context & Anti-Drift Rules | Planned |
| 004-G | OKF Metadata, Trust, Verification, Lifecycle & Freshness Conventions | Planned |
| 004-H | Validation Tooling, Link/Authority Checks & CI Enforcement | Planned |
| 004-I | Repository-Wide Knowledge Graph / Drift Audit & Migration Closure | Planned |
| 004-J | Phase 004 Consolidation & Knowledge-Architecture Exit Review | Planned |

See [`docs/004-knowledge-architecture/README.md`](docs/004-knowledge-architecture/README.md) for the Phase 004 plan and [`docs/README.md`](docs/README.md) for canonical documentation authority.

## Phase 004 knowledge baseline

MUDAC adopts the dedicated [GoogleCloudPlatform/open-knowledge-format](https://github.com/GoogleCloudPlatform/open-knowledge-format) repository as upstream OKF authority and initially targets [OKF v0.2](https://github.com/GoogleCloudPlatform/open-knowledge-format/blob/main/SPEC.md). The historical `knowledge-catalog/okf` copy is frozen and is not the implementation baseline.

Daniel Jackson Concept Design remains the product-design methodology authority. OKF is used to structure, type, link, attribute, and progressively expose repository knowledge; it does not redefine MUDAC Concepts, application state, or source-code architecture.

`MUDAC Concept` and OKF's generic knowledge-document `Concept` meaning are explicitly distinct. Phase 004 will establish canonical-current-knowledge versus historical-phase-provenance layers, stable cross-reference conventions, agent context rules, metadata/verification conventions, and automated drift checks.

The repository-wide documentation direction is **reference first**: one canonical owner for normative rules, cross-reference from dependent documents, and bounded restatement only where needed for comprehension or independent auditability.

## Planned next architecture layer

The previously proposed System, Application, Data & Synchronization Architecture becomes **Phase 005** after the knowledge architecture retrofit is complete.

Phase 005 may select concrete mechanisms and technologies, but lifecycle, authority, evidence, one-logical-Scorecard, Coverage/Ranking, Finalization, disclosure, accessibility, recovery, and canonical knowledge contracts remain architectural inputs rather than implementation suggestions.

## Repository documentation convention

The repository—not chat history—is the durable design baseline. Phase 004 is evolving the current phase-centric corpus into an OKF-aligned canonical knowledge graph while preserving historical design records as provenance and rationale.

## Architecture boundary condition

The intended deployment boundary remains **GitHub Actions → AWS**. Front-end framework, component/design system, identity provider, API style, database, offline persistence, synchronization/conflict strategy, artifact generation/storage, audit implementation, real-time transport, OCR/scanning, publication infrastructure, accessibility tooling, and AWS service choices follow the completed Concept/UX and knowledge-governance architecture rather than drive it.

## Status

This repository remains in **design**, not production implementation. **004-A is complete; 004-B — Knowledge Bundle Topology, Canonical Authority Layers & Progressive Disclosure is next.**

# MUDAC Competition Demo

MUDAC is a documentation-first design effort for a web application that supports live student data competitions, with MinneMUDAC as the initial reference context. The product is intended to replace or augment paper-heavy judging operations while preserving fairness, Judge independence, accessibility, auditability, and operational resilience.

The product/domain design uses Daniel Jackson's **Concept Design** methodology. Phase 004 is now introducing the **Open Knowledge Format (OKF)** as the repository knowledge-structure and navigation convention before system/application architecture begins.

## Product intent

Student Teams analyze a supplied dataset and present findings and methodology to Panels of volunteer Judges. Each Judge independently completes a Rubric-based Scorecard for a Team during a Judging Encounter. Eligible authoritative Scorecards are combined under explicit Evaluation Policy to support Coverage assessment, Division-scoped Ranking, Awards, and controlled official closeout.

Judge and Organizer are Competition-scoped Participation roles rather than permanent Identity types. Teams may carry extensible descriptive attributes such as optional `teamName`; Alias remains the blinded Judge-facing Competition identity by default.

## Core design principles

- **Independent judgment** — each Judge authors an individual Scorecard; Panel and Team results are derived.
- **Traceable aggregation** — outcomes remain decomposable to eligible Scorecards, Criteria, Rubric Versions, Provenance, and Evaluation Policy.
- **Controlled identity disclosure** — Judge-visible identity uses Alias + Division; optional Team metadata remains separately disclosure-controlled.
- **Controlled finality** — authoritative state is correctable through Versioning and Provenance rather than silent overwrite.
- **Authority preservation** — Organizer/system authority does not silently substitute for Judge judgment.
- **Capture-channel parity** — paper and electronic judging share evaluation semantics and converge on one logical Judge × Encounter evaluation.
- **Coverage before outcome confidence** — Coverage and Aggregate remain separate; missing evaluation is never zero.
- **Explainable Ranking** — Rank is derived and never directly edited.
- **Calculated is not official** — a calculated Ranking may exist without being ranking-ready or official.
- **Official is not automatically public** — Finalization creates an Official Outcome Revision; publication is a separate action.
- **Accessibility as semantic parity** — alternate input, device, assistive technology, or capture channel preserves the same Competition meaning and authority.
- **Truthful persistence and recovery** — connectivity uncertainty never becomes false authoritative success, and retries/recovery must not create duplicate evaluation weight.
- **Canonical knowledge over duplicated restatement** — normative rules should have one canonical owner; dependent knowledge should reference that authority.
- **Progressive knowledge retrieval** — humans and agents navigate indexes to relevant canonical knowledge and consult phase history only when rationale/provenance is needed.
- **Technology follows semantics** — framework, database, API, synchronization, and AWS choices must satisfy the accepted design contracts rather than redefine them.

## Accepted MUDAC Concept catalog

### Core Concepts

- Competition
- Division
- Team
- Panel
- Judging Encounter
- Rubric
- Scorecard
- Award

### Supporting Concepts

- Identity
- Participation
- Alias
- Access
- Versioning
- Provenance
- Export

Coverage, Aggregate, Rank, Criterion, Note, Expertise, Panel Membership, Reconciliation, Evaluation Policy, Official Outcome Revision, Team Attribute Definitions, status, recovery, publication, QR/PDF, and offline mode remain subordinate/derived/policy/process/metadata/representation/implementation mechanisms unless deliberately refined through Concept Design.

## Knowledge navigation

The preferred documentation entry point is [`docs/index.md`](docs/index.md), the root of the MUDAC OKF knowledge bundle.

```text
docs/index.md
      ↓
current canonical knowledge → docs/canonical/
external authorities         → docs/references/
design history/rationale     → numbered phase directories
```

During Phase 004, canonical extraction is intentionally partial. See [`docs/README.md`](docs/README.md) for the transition authority summary.

## Design status

**Phase 001 — Concept Design Foundation: Complete.**  
Exit: [`001-H`](docs/001-concept-design/001-H-phase-consolidation-initial-concept-catalog.md)

**Phase 002 — Concept Specification, Policy & Synchronization Refinement: Complete.**  
Exit: [`002-I`](docs/002-concept-specification/002-I-phase-consolidation-specification-exit-review.md)  
Compatible refinement: [`002-A1`](docs/002-concept-specification/002-A1-team-extensible-attributes-team-name-refinement.md)

**Phase 003 — Conceptual UX Architecture, Information Architecture & Interaction Model: Complete.**  
Exit: [`003-J`](docs/003-conceptual-ux-architecture/003-J-phase-consolidation-ux-architecture-exit-review.md)

**Phase 004 — Knowledge Architecture, OKF Retrofit & Documentation Governance: In Progress.**

| Group | Topic | Status |
| --- | --- | --- |
| 004-A | [OKF Adoption Authority, Methodology Compatibility & Terminology Contract](docs/004-knowledge-architecture/004-A-okf-adoption-authority-methodology-compatibility-terminology-contract.md) | **Complete** |
| 004-B | [Knowledge Bundle Topology, Canonical Authority Layers & Progressive Disclosure](docs/004-knowledge-architecture/004-B-knowledge-bundle-topology-canonical-authority-layers-progressive-disclosure.md) | **Complete** |
| 004-C | Canonical Concept, Policy, Invariant & Experience Knowledge Extraction | **Next** |
| 004-D | Historical Phase Migration, Provenance & Source-Lineage Retrofit | Planned |
| 004-E | Cross-Reference, Stable Rule-ID & Restatement Reduction Retrofit | Planned |
| 004-F | Documentation Governance, Agent Context & Anti-Drift Rules | Planned |
| 004-G | OKF Metadata, Trust, Verification, Lifecycle & Freshness Conventions | Planned |
| 004-H | Validation Tooling, Link/Authority Checks & CI Enforcement | Planned |
| 004-I | Repository-Wide Knowledge Graph / Drift Audit & Migration Closure | Planned |
| 004-J | Phase 004 Consolidation & Knowledge-Architecture Exit Review | Planned |

## Phase 004 topology decision

MUDAC uses `docs/` itself as the OKF bundle. Current meaning is extracted under `docs/canonical/`; external standards/methodologies live under `docs/references/`; existing numbered phase directories stay at their current paths as historical design records.

We intentionally do **not** move the Phase 001–004 corpus into a synthetic `/history/` tree. Preserving those paths avoids widespread link churn while still separating chronological design history from meaning-oriented canonical knowledge.

The current canonical categories are:

```text
canonical/
├── governance/
├── concepts/
├── mechanisms/
├── policies/
├── invariants/
├── experience/
└── architecture/
```

This tree is a retrieval structure, not the application ontology and not the future source-code package tree.

## Planned Phase 005

The previously proposed **System, Application, Data & Synchronization Architecture** is now Phase 005, after the knowledge/governance retrofit.

Phase 005 may choose concrete implementation mechanisms and technologies, but the lifecycle, authority, evidence, one-logical-Scorecard, Coverage/Ranking, Finalization, disclosure, accessibility, recovery, and canonical knowledge contracts remain architectural inputs rather than implementation suggestions.

## Architecture boundary

The intended deployment boundary remains **GitHub Actions → AWS**. Front-end framework, component/design system, identity provider, API style, database, offline persistence, synchronization/conflict strategy, artifact generation/storage, audit implementation, real-time transport, OCR/scanning, publication infrastructure, accessibility tooling, and AWS service choices remain downstream decisions.

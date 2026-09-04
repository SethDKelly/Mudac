# MUDAC Design Documentation

This directory is the durable design authority for the MUDAC competition application.

The project uses Daniel Jackson's **Concept Design** methodology for product/domain design and is adopting the **Open Knowledge Format (OKF)** for knowledge structure, metadata, provenance, progressive disclosure, and agent/human navigation.

## Preferred navigation

Start with [`docs/index.md`](index.md), the MUDAC OKF bundle root and preferred progressive-disclosure entry point.

Current knowledge is being extracted into [`docs/canonical/`](canonical/). External standards/methodologies are represented under [`docs/references/`](references/). Numbered phase directories remain at their existing paths as design history, rationale, and provenance.

During Phase 004 migration, canonical extraction is partial. Where a subject does not yet have an accepted canonical owner, the accepted Phase 001–003 exits and refinements remain authoritative.

## Accepted MUDAC Concept catalog

### Core Concepts

1. Competition
2. Division
3. Team
4. Panel
5. Judging Encounter
6. Rubric
7. Scorecard
8. Award

### Supporting Concepts

9. Identity
10. Participation
11. Alias
12. Access
13. Versioning
14. Provenance
15. Export

Coverage, Aggregate, Rank, Criterion, Note, Expertise, Panel Membership, Reconciliation, Evaluation Policy, Official Outcome Revision, Team Attribute Definitions, status, recovery, publication, QR/PDF, and offline mode remain subordinate, derived, policy, process, metadata, representation, UX, or implementation mechanisms rather than standalone MUDAC Concepts unless explicitly refined through Concept Design.

## Phase status

### Phase 001 — Concept Design Foundation

**Status: Complete**

Canonical exit: [001-H — Phase 001 Consolidation & Initial Concept Catalog](001-concept-design/001-H-phase-consolidation-initial-concept-catalog.md).

### Phase 002 — Concept Specification, Policy & Synchronization Refinement

**Status: Complete**

Canonical exit: [002-I — Phase 002 Consolidation & Specification Exit Review](002-concept-specification/002-I-phase-consolidation-specification-exit-review.md).

Compatible refinement: [002-A1 — Team Extensible Attributes & Team Name](002-concept-specification/002-A1-team-extensible-attributes-team-name-refinement.md).

### Phase 003 — Conceptual UX Architecture, Information Architecture & Interaction Model

**Status: Complete**

Canonical exit: [003-J — Phase 003 Consolidation & UX Architecture Exit Review](003-conceptual-ux-architecture/003-J-phase-consolidation-ux-architecture-exit-review.md).

### Phase 004 — Knowledge Architecture, OKF Retrofit & Documentation Governance

**Status: In Progress**

See the [Phase 004 index](004-knowledge-architecture/README.md).

| Group | Topic | Status |
| --- | --- | --- |
| 004-A | [OKF Adoption Authority, Methodology Compatibility & Terminology Contract](004-knowledge-architecture/004-A-okf-adoption-authority-methodology-compatibility-terminology-contract.md) | **Complete** |
| 004-B | [Knowledge Bundle Topology, Canonical Authority Layers & Progressive Disclosure](004-knowledge-architecture/004-B-knowledge-bundle-topology-canonical-authority-layers-progressive-disclosure.md) | **Complete** |
| 004-C | Canonical Concept, Policy, Invariant & Experience Knowledge Extraction | **Next** |
| 004-D | Historical Phase Migration, Provenance & Source-Lineage Retrofit | Planned |
| 004-E | Cross-Reference, Stable Rule-ID & Restatement Reduction Retrofit | Planned |
| 004-F | Documentation Governance, Agent Context & Anti-Drift Rules | Planned |
| 004-G | OKF Metadata, Trust, Verification, Lifecycle & Freshness Conventions | Planned |
| 004-H | Validation Tooling, Link/Authority Checks & CI Enforcement | Planned |
| 004-I | Repository-Wide Knowledge Graph / Drift Audit & Migration Closure | Planned |
| 004-J | Phase 004 Consolidation & Knowledge-Architecture Exit Review | Planned |

## Current stable product/UX baseline

The detailed current rules remain in the accepted Phase 001–003 exits until 004-C extracts canonical owners. Key stable distinctions include:

- Competition lifecycle: `Draft → Ready → Active → Event Completed → Finalized`.
- Identity, Participation, Access, and semantic authority are distinct.
- Team supports disclosure-controlled descriptive attributes; optional `teamName` remains distinct from Alias and non-competitive by default.
- current Panel membership and historical Encounter participation are distinct.
- one Judge Participation × one Encounter yields at most one logical Scorecard.
- every Scorecard is bound to one exact Rubric Version.
- Draft, Finalized, and Amendment Draft have distinct authority semantics.
- Organizer authority manages process integrity without becoming Judge authorship.
- Coverage remains independent from Aggregate; missing evaluation is never zero.
- Rank is derived and Division-scoped.
- calculated Ranking is not automatically ranking-ready or official.
- Finalization creates an Official Outcome Revision and remains separate from publication.
- paper and electronic traces converge onto the same logical evaluation semantics.
- accessibility is semantic parity; alternate device/input/capture paths do not change authority or evidence meaning.
- connectivity uncertainty cannot be represented as confirmed authoritative success.
- status dimensions such as lifecycle, authority, readiness, freshness, disclosure, and publication remain distinct.

## Phase 004 knowledge architecture baseline

MUDAC adopts [GoogleCloudPlatform/open-knowledge-format](https://github.com/GoogleCloudPlatform/open-knowledge-format) as upstream OKF authority and initially targets OKF v0.2. The former `knowledge-catalog/okf` copy is frozen and is not an implementation baseline.

Daniel Jackson Concept Design remains authoritative for deciding what qualifies as a MUDAC Concept and what MUDAC means. OKF governs how knowledge is represented, linked, attributed, versioned, and navigated.

The approved bundle topology is:

```text
docs/
├── index.md                 # OKF root / preferred navigation
├── README.md                # human compatibility/authority summary
├── canonical/
│   ├── governance/
│   ├── concepts/
│   ├── mechanisms/
│   ├── policies/
│   ├── invariants/
│   ├── experience/
│   └── architecture/
├── references/
├── 001-concept-design/
├── 002-concept-specification/
├── 003-conceptual-ux-architecture/
└── 004-knowledge-architecture/
```

Existing numbered phase folders are intentionally **not moved**. They remain stable design-history/provenance paths. Current meaning is extracted into `canonical/` rather than trying to make chronological phase records serve permanently as the knowledge graph.

Repository documentation follows a **reference-first** direction: normative rules should have one canonical owner; dependent documents should cross-reference that owner rather than fully restating it, except where a bounded linked restatement is necessary for comprehension or independent auditability.

## Planned Phase 005

System, Application, Data & Synchronization Architecture moves to **Phase 005** after the Phase 004 knowledge/governance retrofit.

Phase 005 may choose implementation mechanisms and technologies, but the lifecycle, authority, evidence, disclosure, accessibility, recovery, and canonical knowledge contracts remain architectural inputs rather than implementation suggestions.

## Architecture boundary

The deployment target remains **GitHub Actions → AWS**. Front-end framework, component/design system, identity provider, API style, database, offline persistence, synchronization/conflict strategy, artifact generation/storage, audit implementation, real-time transport, OCR/scanning, publication infrastructure, accessibility tooling, and AWS services remain downstream choices that must satisfy the canonical design contracts rather than redefine them.

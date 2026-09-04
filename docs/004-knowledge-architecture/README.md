# Phase 004 — Knowledge Architecture, OKF Retrofit & Documentation Governance

Status: **In Progress**

## Purpose

Phase 004 establishes the knowledge architecture governing subsequent MUDAC design and implementation documentation. Daniel Jackson Concept Design remains the product-design methodology; OKF v0.2 structures, links, attributes, and progressively exposes the resulting knowledge.

Preferred bundle entry: [docs/index.md](../index.md). Historical/phase navigation: [Phase 004 index](index.md).

## Phase plan

| Group | Topic | Status |
| --- | --- | --- |
| 004-A | [OKF Adoption Authority, Methodology Compatibility & Terminology Contract](004-A-okf-adoption-authority-methodology-compatibility-terminology-contract.md) | **Complete** |
| 004-B | [Knowledge Bundle Topology, Canonical Authority Layers & Progressive Disclosure](004-B-knowledge-bundle-topology-canonical-authority-layers-progressive-disclosure.md) | **Complete** |
| 004-C | [Canonical Concept, Policy, Invariant & Experience Knowledge Extraction](004-C-canonical-concept-policy-invariant-experience-knowledge-extraction.md) | **Complete** |
| 004-D | [Historical Phase Migration, Provenance & Source-Lineage Retrofit](004-D-historical-phase-migration-provenance-source-lineage-retrofit.md) | **Complete** |
| 004-E | Cross-Reference, Stable Rule-ID & Restatement Reduction Retrofit | **Next** |
| 004-F | Documentation Governance, Agent Context & Anti-Drift Rules | Planned |
| 004-G | OKF Metadata, Trust, Verification, Lifecycle & Freshness Conventions | Planned |
| 004-H | Validation Tooling, Link/Authority Checks & CI Enforcement | Planned |
| 004-I | Repository-Wide Knowledge Graph / Drift Audit & Migration Closure | Planned |
| 004-J | Phase 004 Consolidation & Knowledge-Architecture Exit Review | Planned |

## Authoritative baseline through 004-D

004-A establishes OKF adoption/version/terminology authority while preserving Concept Design and MUDAC semantics.

004-B establishes `docs/` as the OKF bundle root, `docs/index.md` as the progressive-disclosure root, `docs/canonical/` as meaning-oriented current knowledge, `docs/references/` for external authority context, and stable numbered phase directories as design history.

004-C establishes current canonical product/UX owners: 15 Concepts, 9 supporting mechanisms, 6 policies, 10 cross-cutting invariants, and 9 experience contracts.

004-D makes the historical/canonical relationship bidirectional without moving or rewriting the phase corpus: canonical documents point backward through material `sources`, numbered phase `index.md` files point forward to current successors, compatible post-exit refinements remain visible lineage, and historical records are treated as append-stable design evidence. Canonical governance for this relationship is [Source Lineage and Historical Design Records](../canonical/governance/source-lineage.md).

No Concept split/merge/addition or semantic correction was required through 004-D.

## Migration principle

`knowledge architecture ≠ application source-code architecture`.

Future architecture and implementation must consume canonical product/UX contracts rather than recreate them. Historical phase records remain available when rationale, chronology, or provenance is required.

## Next

004-E will assign stable normative rule identifiers where valuable, replace unnecessary duplicated restatement with direct canonical cross-references, and establish how downstream architecture/tests cite those stable contracts.
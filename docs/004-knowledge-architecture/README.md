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
| 004-E | [Cross-Reference, Stable Rule-ID & Restatement Reduction Retrofit](004-E-cross-reference-stable-rule-id-restatement-reduction-retrofit.md) | **Complete** |
| 004-F | Documentation Governance, Agent Context & Anti-Drift Rules | **Next** |
| 004-G | OKF Metadata, Trust, Verification, Lifecycle & Freshness Conventions | Planned |
| 004-H | Validation Tooling, Link/Authority Checks & CI Enforcement | Planned |
| 004-I | Repository-Wide Knowledge Graph / Drift Audit & Migration Closure | Planned |
| 004-J | Phase 004 Consolidation & Knowledge-Architecture Exit Review | Planned |

## Authoritative baseline through 004-E

004-A establishes OKF adoption/version/terminology authority while preserving Concept Design and MUDAC semantics.

004-B establishes `docs/` as the OKF bundle root, `docs/index.md` as the progressive-disclosure root, `docs/canonical/` as meaning-oriented current knowledge, `docs/references/` for external authority context, and stable numbered phase directories as design history.

004-C establishes current canonical product/UX owners: 15 Concepts, 9 supporting mechanisms, 6 policies, 10 cross-cutting invariants, and 9 experience contracts.

004-D establishes bidirectional provenance: canonical `sources` point backward to material historical records; phase `index.md` files route forward to current successors. Historical records remain append-stable design evidence.

004-E establishes [Stable Rule Identifiers & Cross-Reference Contract](../canonical/governance/rule-identifiers.md): durable owner-based IDs and explicit anchors for high-value normative rules, reference-first downstream reuse, and bounded restatement where independent auditability requires it. The ten cross-cutting invariants are now `INV-001` through `INV-010`; selected Competition, Access, Scorecard, Evaluation Policy, Rank, Official Outcome, disclosure, and Export rules also have stable IDs.

No Concept split/merge/addition or semantic correction was required through 004-E.

## Migration principle

`knowledge architecture ≠ application source-code architecture`.

Future architecture and implementation must consume canonical product/UX contracts rather than recreate them. When a stable rule ID exists, later documentation should link to it and explain only the local consequence rather than copy the full normative body.

Historical phase records remain available when rationale, chronology, or provenance is required.

## Next

004-F will convert the authority, retrieval, source-lineage, and stable-ID decisions into explicit repository/agent governance: what agents must load, what they must not restate, how canonical changes are reviewed, and how drift/conflict is handled before writes are accepted.
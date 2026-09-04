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
| 004-F | [Documentation Governance, Agent Context & Anti-Drift Rules](004-F-documentation-governance-agent-context-anti-drift-rules.md) | **Complete** |
| 004-G | [OKF Metadata, Trust, Verification, Lifecycle & Freshness Conventions](004-G-okf-metadata-trust-verification-lifecycle-freshness-conventions.md) | **Complete** |
| 004-H | [Validation Tooling, Link/Authority Checks & CI Enforcement](004-H-validation-tooling-link-authority-checks-ci-enforcement.md) | **Complete** |
| 004-I | Repository-Wide Knowledge Graph / Drift Audit & Migration Closure | **Next** |
| 004-J | Phase 004 Consolidation & Knowledge-Architecture Exit Review | Planned |

## Authoritative baseline through 004-H

004-A through 004-G establish the Concept Design/OKF boundary, bundle topology, canonical product/UX owners, historical lineage, stable rule IDs, repository/agent governance, and the `META-*` trust/lifecycle profile.

004-H establishes [Knowledge Validation & CI Enforcement](../canonical/governance/validation-enforcement.md) — `VAL-*` — plus the deterministic [`scripts/validate_knowledge.py`](../../scripts/validate_knowledge.py) validator and read-only GitHub Actions workflow.

The validator enforces machine-checkable structure such as current frontmatter shape, lifecycle/timestamp/actor syntax, stable-ID uniqueness/registry ownership, current internal links/local sources, and progressive-disclosure routing. Passing validation is structural evidence only and is never an OKF `verified` event.

No Concept split/merge/addition or product/UX semantic correction was required through 004-H.

## Governing operating principles

`knowledge architecture ≠ application source-code architecture`.

Future architecture and implementation consume canonical contracts rather than recreate or override them. Agents use minimum-sufficient progressive context. Semantic changes update canonical owners and lineage explicitly. CI validates deterministic structure without claiming semantic authority.

## Next

004-I will perform the repository-wide knowledge-graph/drift audit, exercise strict validation across the corpus, inspect remaining historical/current asymmetries and exemptions, and determine whether the OKF migration is structurally closed before the Phase 004 exit review.

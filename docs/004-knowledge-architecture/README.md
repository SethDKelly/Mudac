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
| 004-G | OKF Metadata, Trust, Verification, Lifecycle & Freshness Conventions | **Next** |
| 004-H | Validation Tooling, Link/Authority Checks & CI Enforcement | Planned |
| 004-I | Repository-Wide Knowledge Graph / Drift Audit & Migration Closure | Planned |
| 004-J | Phase 004 Consolidation & Knowledge-Architecture Exit Review | Planned |

## Authoritative baseline through 004-F

004-A establishes the Concept Design/OKF methodology and terminology boundary.

004-B establishes `docs/` as the OKF bundle root, `docs/index.md` as the progressive-disclosure root, `docs/canonical/` as meaning-oriented current knowledge, and stable numbered phase directories as design history.

004-C establishes current canonical product/UX owners: 15 Concepts, 9 supporting mechanisms, 6 policies, 10 cross-cutting invariants, and 9 experience contracts.

004-D establishes bidirectional provenance: canonical `sources` point backward to material historical records; phase `index.md` files route forward to current successors. Historical records remain append-stable evidence.

004-E establishes [Stable Rule Identifiers & Cross-Reference Contract](../canonical/governance/rule-identifiers.md): durable owner-based IDs, exact anchors, reference-first downstream reuse, and bounded restatement.

004-F establishes repository operating governance:

* [Methodology, OKF Adoption & Terminology](../canonical/governance/methodology-terminology.md);
* [Documentation Authority & Canonical Ownership](../canonical/governance/documentation-authority.md) — `DOC-*`;
* [Agent Context & Progressive Retrieval](../canonical/governance/agent-context.md) — `CTX-*`;
* [Canonical Change & Conflict Governance](../canonical/governance/change-governance.md) — `CHG-*`;
* root [`AGENTS.md`](../../AGENTS.md) as a thin agent bootstrap adapter.

No Concept split/merge/addition or product/UX semantic correction was required through 004-F.

## Governing operating principles

`knowledge architecture ≠ application source-code architecture`.

Future architecture and implementation consume canonical contracts rather than recreate or override them. Agents use minimum-sufficient progressive context instead of recursively loading the corpus. Semantic changes update canonical owners and lineage explicitly; conflicts are surfaced rather than silently normalized.

## Next

004-G will define how OKF metadata communicates generation provenance, verification/trust, knowledge lifecycle/status, deprecation/supersession, and freshness without confusing documentation metadata with MUDAC domain state.
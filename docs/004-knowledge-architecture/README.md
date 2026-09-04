# Phase 004 — Knowledge Architecture, OKF Retrofit & Documentation Governance

Status: **In Progress**

## Purpose

Phase 004 establishes the repository knowledge architecture that will govern all subsequent design and implementation documentation.

It introduces the Open Knowledge Format (OKF) as the repository's knowledge-structure and interchange convention while preserving Daniel Jackson Concept Design as the design methodology used to discover and specify MUDAC semantics.

The phase intentionally occurs before system/application architecture so that future architecture and implementation artifacts are created against a stable canonical knowledge graph rather than extending a phase-centric documentation corpus with increasingly duplicated rules.

The governing question is:

> How should MUDAC structure, identify, link, verify, evolve, and govern design knowledge so that humans and agents can retrieve authoritative context efficiently without reconstructing current truth from historical phase documents or creating documentation drift?

## External OKF authority

MUDAC adopts the dedicated [GoogleCloudPlatform/open-knowledge-format](https://github.com/GoogleCloudPlatform/open-knowledge-format) repository as the upstream OKF authority and initially targets the [OKF v0.2 specification](https://github.com/GoogleCloudPlatform/open-knowledge-format/blob/main/SPEC.md).

The former [`GoogleCloudPlatform/knowledge-catalog/okf`](https://github.com/GoogleCloudPlatform/knowledge-catalog/tree/main/okf) copy is a frozen historical snapshot and is not an implementation baseline.

## Phase plan

| Group | Topic | Status |
| --- | --- | --- |
| 004-A | [OKF Adoption Authority, Methodology Compatibility & Terminology Contract](004-A-okf-adoption-authority-methodology-compatibility-terminology-contract.md) | **Complete** |
| 004-B | Knowledge Bundle Topology, Canonical Authority Layers & Progressive Disclosure | **Next** |
| 004-C | Canonical Concept, Policy, Invariant & Experience Knowledge Extraction | Planned |
| 004-D | Historical Phase Migration, Provenance & Source-Lineage Retrofit | Planned |
| 004-E | Cross-Reference, Stable Rule-ID & Restatement Reduction Retrofit | Planned |
| 004-F | Documentation Governance, Agent Context & Anti-Drift Rules | Planned |
| 004-G | OKF Metadata, Trust, Verification, Lifecycle & Freshness Conventions | Planned |
| 004-H | Validation Tooling, Link/Authority Checks & CI Enforcement | Planned |
| 004-I | Repository-Wide Knowledge Graph / Drift Audit & Migration Closure | Planned |
| 004-J | Phase 004 Consolidation & Knowledge-Architecture Exit Review | Planned |

## Phase 003 input contract

Phase 004 treats the complete Phase 003 exit baseline as authoritative product/UX input. Knowledge restructuring may improve discoverability, provenance, cross-reference quality, and authority ownership, but it may not reinterpret Competition semantics, Judge/Organizer authority, evidence rules, disclosure boundaries, accessibility parity, recovery semantics, or official-outcome behavior.

Canonical Phase 003 exit: [003-J — Phase 003 Consolidation & UX Architecture Exit Review](../003-conceptual-ux-architecture/003-J-phase-consolidation-ux-architecture-exit-review.md).

## 004-A authoritative baseline

004-A establishes:

- Daniel Jackson Concept Design remains the product-design methodology authority;
- OKF governs knowledge representation/navigation rather than MUDAC domain semantics;
- MUDAC adopts OKF by explicit version/profile rather than silently following upstream `main`;
- `MUDAC Concept` and OKF's generic knowledge-document `Concept` meaning must be qualified and kept distinct;
- MUDAC-defined OKF `type` values classify knowledge documents but do not create domain constructs;
- canonical current knowledge and historical phase records are separate authority layers;
- historical phase records remain preserved as rationale/provenance;
- normative rules should have one canonical owner and downstream documentation should prefer references over duplicated restatement;
- necessary restatement identifies its canonical source and does not gain independent authority;
- OKF documentation provenance/verification/lifecycle metadata remains distinct from MUDAC Provenance and application lifecycle semantics;
- knowledge/documentation structure does not dictate future source-code package/module architecture;
- migration may change knowledge location/representation but may not silently change established MUDAC meaning;
- contradictions discovered during migration must be surfaced as explicit design refinements rather than hidden migration edits;
- agents should eventually navigate `index.md → canonical knowledge → linked dependencies → history only as needed`.

Canonical 004-A: [OKF Adoption Authority, Methodology Compatibility & Terminology Contract](004-A-okf-adoption-authority-methodology-compatibility-terminology-contract.md).

## Phase 004 migration principle

Phase 004 distinguishes:

```text
knowledge architecture
        ≠
application source-code architecture
```

OKF governs how repository knowledge is structured and connected. Future source code, schemas, APIs, infrastructure, and generated artifacts may be referenced as knowledge resources, but application package/module boundaries will be decided by later system architecture rather than copied from the documentation tree.

## Phase exit target

Phase 004 should end with:

- one documented OKF adoption authority and version policy;
- explicit compatibility rules between OKF terminology and Daniel Jackson Concept Design terminology;
- canonical-versus-historical documentation authority layers;
- progressive-disclosure indexes for agent/human navigation;
- extracted canonical Concept, policy, invariant, experience, and architecture knowledge;
- provenance links back to historical design records;
- stable cross-reference/rule identifiers for normative contracts;
- repository documentation and agent-context rules that prefer reference over duplicated restatement;
- OKF metadata/lifecycle/verification conventions;
- automated validation for links, metadata, authority ownership, and drift-relevant structure;
- enough knowledge stability for system/application architecture to proceed as Phase 005 without reconstructing current truth from prior phases.

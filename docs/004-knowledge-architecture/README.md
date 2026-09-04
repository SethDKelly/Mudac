# Phase 004 — Knowledge Architecture, OKF Retrofit & Documentation Governance

Status: **In Progress**

## Purpose

Phase 004 establishes the repository knowledge architecture that will govern all subsequent design and implementation documentation.

It introduces the Open Knowledge Format (OKF) as the repository's knowledge-structure and interchange convention while preserving Daniel Jackson Concept Design as the methodology used to discover and specify MUDAC semantics.

The phase intentionally occurs before system/application architecture so future architecture and implementation artifacts are created against a stable canonical knowledge graph rather than extending a phase-centric corpus with increasingly duplicated rules.

The governing question is:

> How should MUDAC structure, identify, link, verify, evolve, and govern design knowledge so that humans and agents can retrieve authoritative context efficiently without reconstructing current truth from historical phase documents or creating documentation drift?

## External OKF authority

MUDAC adopts the dedicated [GoogleCloudPlatform/open-knowledge-format](https://github.com/GoogleCloudPlatform/open-knowledge-format) repository as the upstream OKF authority and initially targets the [OKF v0.2 specification](https://github.com/GoogleCloudPlatform/open-knowledge-format/blob/main/SPEC.md).

The former [`GoogleCloudPlatform/knowledge-catalog/okf`](https://github.com/GoogleCloudPlatform/knowledge-catalog/tree/main/okf) copy is a frozen historical snapshot and is not an implementation baseline.

## Phase plan

| Group | Topic | Status |
| --- | --- | --- |
| 004-A | [OKF Adoption Authority, Methodology Compatibility & Terminology Contract](004-A-okf-adoption-authority-methodology-compatibility-terminology-contract.md) | **Complete** |
| 004-B | [Knowledge Bundle Topology, Canonical Authority Layers & Progressive Disclosure](004-B-knowledge-bundle-topology-canonical-authority-layers-progressive-disclosure.md) | **Complete** |
| 004-C | Canonical Concept, Policy, Invariant & Experience Knowledge Extraction | **Next** |
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
- `MUDAC Concept` and OKF's generic knowledge-document `Concept` meaning remain distinct;
- MUDAC-defined OKF `type` values classify knowledge documents but do not create domain constructs;
- canonical current knowledge and historical phase records are separate authority layers;
- normative rules should have one canonical owner and downstream documentation should prefer references over duplicated restatement;
- OKF documentation provenance/verification/lifecycle metadata remains distinct from MUDAC Provenance and application lifecycle semantics;
- knowledge/documentation structure does not dictate future source-code package/module architecture;
- migration may change knowledge location/representation but may not silently change established MUDAC meaning;
- contradictions discovered during migration must be surfaced as explicit design refinements rather than hidden migration edits.

Canonical 004-A: [OKF Adoption Authority, Methodology Compatibility & Terminology Contract](004-A-okf-adoption-authority-methodology-compatibility-terminology-contract.md).

## 004-B authoritative baseline

004-B establishes `docs/` as the MUDAC OKF bundle root and creates [docs/index.md](../index.md) as the preferred progressive-disclosure entry point.

The approved topology is:

```text
docs/
├── index.md
├── README.md
├── canonical/
│   ├── index.md
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

Key decisions:

- current canonical knowledge is meaning-oriented and lives under `docs/canonical/`;
- existing numbered phase directories remain at their current paths as design history/provenance;
- MUDAC will **not** physically move the historical phase corpus under a synthetic `history/` directory;
- the root index distinguishes Current Knowledge, External References, and Design History/Active Design Work;
- indexes route one semantic level at a time and must not become duplicate canonical rule stores;
- internal Markdown links should prefer relative paths where practical;
- canonical paths become stable interfaces once accepted and consumed downstream;
- `canonical/` placement alone does not grant authority—semantic extraction, sourcing, validation, indexing, and later governance/verification are also required;
- `docs/README.md` transitions toward a human compatibility/landing role while `docs/index.md` becomes the OKF navigation root;
- future phase records should consume canonical references instead of restating the full baseline;
- the knowledge tree aids retrieval but does not define the MUDAC Concept ontology or future source-code package structure.

Canonical 004-B: [Knowledge Bundle Topology, Canonical Authority Layers & Progressive Disclosure](004-B-knowledge-bundle-topology-canonical-authority-layers-progressive-disclosure.md).

## Migration principle

Phase 004 distinguishes:

```text
knowledge architecture
        ≠
application source-code architecture
```

OKF governs how repository knowledge is structured and connected. Future source code, schemas, APIs, infrastructure, and generated artifacts may be referenced as knowledge resources, but application package/module boundaries will be decided by later system architecture rather than copied from the documentation tree.

Canonical extraction is gradual. Until a subject has an accepted canonical owner, the accepted Phase 001–003 exits and refinements remain the current source of truth for that subject.

## Phase exit target

Phase 004 should end with:

- one documented OKF adoption authority and version policy;
- explicit compatibility rules between OKF terminology and Daniel Jackson Concept Design terminology;
- canonical-versus-historical documentation authority layers;
- progressive-disclosure indexes for agent/human navigation;
- extracted canonical Concept, policy, mechanism, invariant, experience, and architecture knowledge;
- provenance links back to historical design records;
- stable cross-reference/rule identifiers for normative contracts;
- repository documentation and agent-context rules that prefer reference over duplicated restatement;
- OKF metadata/lifecycle/verification conventions;
- automated validation for links, metadata, authority ownership, and drift-relevant structure;
- enough knowledge stability for system/application architecture to proceed as Phase 005 without reconstructing current truth from prior phases.

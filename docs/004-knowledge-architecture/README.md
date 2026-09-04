# Phase 004 — Knowledge Architecture, OKF Retrofit & Documentation Governance

Status: **In Progress**

## Purpose

Phase 004 establishes the repository knowledge architecture that will govern all subsequent design and implementation documentation.

It introduces the Open Knowledge Format (OKF) as the repository's knowledge-structure and interchange convention while preserving Daniel Jackson Concept Design as the design methodology used to discover and specify MUDAC semantics.

The phase intentionally occurs before system/application architecture so that future architecture and implementation artifacts are created against a stable canonical knowledge graph rather than extending a phase-centric documentation corpus with increasingly duplicated rules.

The governing question is:

> How should MUDAC structure, identify, link, verify, evolve, and govern design knowledge so that humans and agents can retrieve authoritative context efficiently without reconstructing current truth from historical phase documents or creating documentation drift?

## Phase plan

| Group | Topic | Status |
| --- | --- | --- |
| 004-A | [OKF Adoption Authority, Methodology Compatibility & Terminology Contract](004-A-okf-adoption-authority-methodology-compatibility-terminology-contract.md) | **In Progress** |
| 004-B | Knowledge Bundle Topology, Canonical Authority Layers & Progressive Disclosure | Planned |
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

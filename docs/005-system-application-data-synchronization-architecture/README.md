# Phase 005 — System, Application, Data & Synchronization Architecture

Status: **In Progress**

## Purpose

Phase 005 translates the accepted MUDAC product, UX, and knowledge-governance contracts into a coherent system/application architecture before production implementation begins.

The phase chooses architecture mechanisms only after identifying the upstream canonical contracts they must satisfy. It does not treat framework, database, authentication, offline, or AWS convenience as permission to redefine MUDAC meaning.

Preferred current authority remains [Canonical Knowledge](../canonical/). Accepted architecture decisions become current owners under [Canonical Architecture](../canonical/architecture/); this numbered phase preserves architecture reasoning, alternatives, and decision lineage.

## Phase plan

| Group | Topic | Status |
| --- | --- | --- |
| 005-A | [Architectural Drivers, Quality Attributes, Trust Boundaries & Decision Principles](005-A-architectural-drivers-quality-attributes-trust-boundaries-decision-principles.md) | **Complete** |
| 005-B | Application Boundaries, Modules, Domain Services & Dependency Architecture | **Next** |
| 005-C | Data Model, Persistence, Versioning, Provenance & Derived-Projection Architecture | Planned |
| 005-D | Identity, Authentication, Participation, Access & Session Architecture | Planned |
| 005-E | Commands, Queries, API Contracts, Transactions, Idempotency & Concurrency Architecture | Planned |
| 005-F | Draft Persistence, Synchronization, Offline/Degraded Operation & Conflict Recovery | Planned |
| 005-G | Paper Capture, Export, Artifact, Publication & External-Representation Architecture | Planned |
| 005-H | Front-End State, Navigation, Component-System & Responsive Interaction Architecture | Planned |
| 005-I | AWS Runtime, Deployment, Security, Observability, Backup & Cost Architecture | Planned |
| 005-J | Phase 005 Consolidation, Threat/Failure Review & Implementation-Readiness Exit | Planned |

## Why this decomposition

The sequence follows architectural dependency rather than UI or technology categories:

```text
architectural drivers / trust / quality attributes
        ↓
application boundaries and dependency direction
        ↓
data/persistence + identity/access
        ↓
command/query/API/transaction semantics
        ↓
synchronization and degraded recovery
        ↓
external representations + front-end state
        ↓
runtime/AWS/operations
        ↓
integrated failure/threat/readiness review
```

This ordering keeps high-consequence domain semantics upstream of technology choices while still allowing later groups to refine earlier architecture through explicit governed change when evidence requires it.

## Architecture authority rules

Phase 005 work must follow:

- [DOC-003](../canonical/governance/documentation-authority.md#doc-003) — downstream architecture cannot override upstream canonical meaning;
- [CTX-002](../canonical/governance/agent-context.md#ctx-002) and [CTX-004](../canonical/governance/agent-context.md#ctx-004) — load only relevant canonical authority and stop when sufficient;
- [CHG-005](../canonical/governance/change-governance.md#chg-005) — implementation/architecture mismatch is resolved downstream unless product design is deliberately changed;
- [META-*](../canonical/governance/metadata-trust-lifecycle.md) — accepted canonical architecture knowledge uses prospective, truthful metadata;
- [VAL-*](../canonical/governance/validation-enforcement.md) — governed documentation changes must preserve deterministic knowledge integrity.

Architecture documents should cite upstream stable rules and state local consequences rather than copy full product/UX rule bodies.

## Authoritative baseline through 005-A

005-A establishes the canonical [Architectural Foundation](../canonical/architecture/architectural-foundation.md) and `ARCH-001` through `ARCH-008`.

The architecture-wide baseline is now:

- upstream canonical product/UX/governance semantics constrain architecture;
- authoritative transitions are validated/confirmed at the authoritative boundary;
- client/device/local state is not final authority;
- derived read projections are not write authority;
- actor/author/authorizer/capture attribution survives architectural boundaries;
- retries/failures preserve logical identity and evidence;
- disclosure/security is enforced beyond presentation code;
- freshness and uncertainty remain representable;
- quality tradeoffs prioritize semantic/trust integrity before apparent availability or speculative performance;
- paper/accessibility/degraded operation are architecture concerns, not UI-only exceptions.

005-A intentionally does **not** select a framework, service topology, database, identity provider, API style, synchronization mechanism, front-end stack, or AWS service.

## Phase boundary

The intended deployment direction remains **GitHub Actions → AWS**, but Phase 005 begins without assuming a front-end framework, API style, service decomposition, database, identity provider, synchronization library/protocol, artifact stack, observability platform, or concrete AWS service set.

Those choices must emerge from the architectural drivers and later subgroup decisions.

## Next

005-B — **Application Boundaries, Modules, Domain Services & Dependency Architecture** will determine semantic responsibility boundaries and allowed dependency direction before persistence/API/runtime implementation choices are made.
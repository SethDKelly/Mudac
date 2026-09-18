# Governance

Current repository/design-governance knowledge for MUDAC.

## Methodology and authority

* [Methodology, OKF Adoption & Terminology](methodology-terminology.md)
* [Documentation Authority & Canonical Ownership](documentation-authority.md)
* [Design / Implementation Boundary](design-implementation-boundary.md)
* [Downstream Architecture & Implementation Authority Quarantine](downstream-authority-quarantine.md)

## Retrieval and change governance

* [Agent Context & Progressive Retrieval](agent-context.md)
* [Canonical Change & Conflict Governance](change-governance.md)

## Current methodology posture

```text
Jackson Concept Design: IN PROGRESS
009: COMPLETE — PASS
010: COMPLETE — PASS
011: COMPLETE — PASS
012: COMPLETE — PASS
013: COMPLETE — PASS
014: IN PROGRESS
014-A: COMPLETE — READY
014-B: COMPLETE — PASS
014-C: COMPLETE — PASS
014-D: COMPLETE — PASS
014-E: COMPLETE — PASS
014-F: COMPLETE — PASS
014-G: COMPLETE — PASS
014-H: NEXT
architecture: SUSPENDED PENDING DESIGN CLOSURE
implementation planning: SUSPENDED
new domain implementation: NOT STARTED
implementation readiness: NOT READY
implementation authorization: NOT YET
```

## Current authority

Canonical Concepts own the eighteen-Concept catalog; Synchronizations own composition/application actions; Dependence owns PF-01 inclusion/scope; completed Phase 013 owns mapping semantics.

Phase 014 owns familiarity/reuse/genericity analysis only. 014-F established product-domain vocabulary authority; 014-G completed the broader genericity/duplication-pressure audit.

## Broader genericity governance

Adopt:

```text
Generic at the boundary; specific in purpose.
shared parameter != shared purpose
shared history shape != shared lifecycle
implementation reuse != Concept identity
```

014-G adopts one narrow semantic broadening: Team intrinsically represents a competing group/unit, while PF-01 binds it to student teams.

It rejects speculative super-concepts such as generic Group, Scoped Relationship, Task, Result, Historical Record and merged representation/release ownership.

Reusable patterns identified by 014-G remain candidates for 014-H knowledge/catalog disposition and do not become canonical Concepts merely because they recur.

## Design / implementation boundary

Architecture and implementation remain quarantined through the remaining Concept Design runway. Conceptual reuse must never be inferred from shared libraries, storage models, inheritance, workflow engines, authorization frameworks, revision systems, report generators or publishing infrastructure.

## Current handoff

Proceed to **014-H — Retained Novelty, Reusable Concept-Knowledge & Catalog-Candidate Audit**.

# MUDAC Design Documentation

The repository is the durable design and implementation authority; conversation history is working context.

## Preferred navigation

Start at [index.md](index.md), the OKF v0.2 bundle root. Current product/domain, UX, governance, architecture, and retained implementation meaning lives under [Canonical Knowledge](canonical/). Root [`AGENTS.md`](../AGENTS.md) is only a bootstrap adapter into those owners.

Use numbered phase directories for rationale, design evolution, alternatives, implementation planning, and provenance.

## Status

* Phase 001 — Concept Design Foundation: **Complete**
* Phase 002 — Concept Specification, Policy & Synchronization Refinement: **Complete**
* Phase 003 — Conceptual UX Architecture: **Complete**
* Phase 004 — Knowledge Architecture, OKF Retrofit & Documentation Governance: **Complete**
* Phase 005 — System, Application, Data & Synchronization Architecture: **Complete as historical architecture exit**
* Phase 006 — Implementation Planning, Delivery Slices & Verification Strategy: **Frozen after 006-D**
  * 006-A — implementation authority/toolchain: Complete
  * 006-B — verification/evidence strategy: Complete
  * 006-C — source/package/dependency topology: Complete
  * 006-D — environment/IaC/CI/CD/local/runtime bootstrap: Complete and retained as a frozen non-domain prototype
  * 006-E through 006-M: **Deferred**
* Phase 007 — Jackson Design Refinement & Methodology Closure: **In Progress**
  * 007-A — design re-entry, implementation freeze & Jackson completion criteria: Complete
  * 007-B — Concept Completeness, Independence & Genericity Audit: **Complete**
  * **007-C — Cross-Concept Synchronization Completeness, Trigger, Preconditions/Postconditions & Authority-Seam Audit: Next**

## Current design posture

MUDAC has deliberately returned to design refinement before any domain schema, persistence, authentication, API, browser-domain, feature, or application-AWS implementation proceeds.

The current execution boundary is owned by [Design / Implementation Boundary](canonical/governance/design-implementation-boundary.md).

007-B has now re-audited the post-architecture Concept system. All fifteen prior Concepts remain accepted; current owners expose Purpose/State/Actions/Operational Principle; and [Publication](canonical/concepts/publication.md) is promoted as the sixteenth Concept because later UX/architecture proved deliberate release/distribution independent from [Export](canonical/concepts/export.md) generation.

The 006-D executable substrate remains in the repository because it is intentionally semantically thin: pinned workspace/tooling, minimal API/worker/web composition roots, package seams, local PostgreSQL service bootstrap, CI/static/dependency checks, and OpenTofu root scaffolding. It is **not** authority to continue 006-E onward.

While frozen, executable changes are limited to narrow maintenance required to keep that prototype safe/buildable and must not encode MUDAC domain semantics.

## Why Phase 005 was not erased

[005-J](005-system-application-data-synchronization-architecture/005-J-phase-005-consolidation-threat-failure-review-implementation-readiness-exit.md) remains historical provenance for the earlier conclusion that architecture was implementation-planning ready. The later human decision recorded in [007-A](007-design-refinement/007-A-design-reentry-implementation-freeze-jackson-completion-criteria.md) supersedes the assumption that implementation should continue immediately.

Historical records are preserved rather than rewritten to make earlier decisions appear never to have happened.

## Current next work

Proceed through [Phase 007](007-design-refinement/) with **007-C — Cross-Concept Synchronization Completeness, Trigger, Preconditions/Postconditions & Authority-Seam Audit**. The renewed design runway continues until a dedicated later Jackson-methodology exit explicitly authorizes implementation to resume.

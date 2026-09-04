# MUDAC Competition Demo

MUDAC is a documentation-first design effort for a web application supporting fair, traceable, resilient judging for live student data competitions.

Student Teams present analyses to Panels of volunteer Judges. Each Judge independently authors a Rubric-based Scorecard for a Team in a Judging Encounter. Authoritative Scorecards feed explicit Coverage, aggregation, ranking, Award, and controlled official-closeout semantics while preserving Judge independence, provenance, anonymity boundaries, accessibility, and paper continuity.

## Knowledge-first design

MUDAC uses Daniel Jackson's **Concept Design** methodology to determine product meaning. The repository is organized as an **Open Knowledge Format (OKF) v0.2** knowledge bundle so humans and agents can retrieve current authority without recursively loading historical design phases.

Start here:

* [`AGENTS.md`](AGENTS.md) — concise repository-agent bootstrap into canonical governance and validation expectations.
* [`docs/index.md`](docs/index.md) — preferred OKF progressive-disclosure entry point.
* [`docs/canonical/`](docs/canonical/) — current canonical product/domain, conceptual UX, governance, and accepted architecture knowledge.
* [`docs/canonical/architecture/`](docs/canonical/architecture/) — accepted current system/application architecture contracts.
* [`docs/README.md`](docs/README.md) — human-oriented documentation authority summary.

Numbered phase directories remain preserved as rationale and design provenance. Canonical documents point backward to material historical `sources`, while phase `index.md` files map forward to current canonical successors.

Knowledge structure is validated by [`scripts/validate_knowledge.py`](scripts/validate_knowledge.py) and read-only GitHub Actions CI. Passing that validator confirms deterministic repository structure only; it is not semantic verification.

## Design status

* **Phase 001 — Concept Design Foundation:** Complete
* **Phase 002 — Concept Specification, Policy & Synchronization Refinement:** Complete
* **Phase 003 — Conceptual UX Architecture:** Complete
* **Phase 004 — Knowledge Architecture, OKF Retrofit & Documentation Governance:** Complete
* **Phase 005 — System, Application, Data & Synchronization Architecture:** In Progress
  * 005-A — Architectural Drivers, Quality Attributes, Trust Boundaries & Decision Principles: Complete
  * 005-B — Application Boundaries, Modules, Domain Services & Dependency Architecture: Complete
  * **005-C — Data Model, Persistence, Versioning, Provenance & Derived-Projection Architecture: Next**

## Current architecture posture

The [Architectural Foundation](docs/canonical/architecture/architectural-foundation.md) defines architecture-wide `ARCH-*` rules. [Application Boundaries](docs/canonical/architecture/application-boundaries.md) defines `MOD-*` rules and selects a **modular-monolith-first** authoritative application with six semantic modules: Competition Governance, Identity/Participation/Access, Judging Operations, Evaluation, Outcomes/Closeout, and External Representation.

Cross-module read projections are explicitly non-authoritative; cross-module workflows coordinate above module owners; modules interact through public contracts rather than repository/table/ORM shortcuts; infrastructure depends inward through application/module ports. Independent services remain an evolutionary option only when a concrete scale, isolation, availability, ownership, or runtime driver justifies the additional distributed-system complexity.

The intended delivery boundary remains **GitHub Actions → AWS**, but database, API protocol, identity provider, offline/synchronization technology, front-end framework, artifact infrastructure, observability, and concrete AWS services remain later architecture decisions.

This repository remains in design; production implementation has not begun.

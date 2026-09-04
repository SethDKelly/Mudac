# MUDAC Competition Demo

MUDAC is a documentation-first design effort for a web application supporting fair, traceable, resilient judging for live student data competitions.

Student Teams present analyses to Panels of volunteer Judges. Each Judge independently authors a Rubric-based Scorecard for a Team in a Judging Encounter. Authoritative Scorecards feed explicit Coverage, aggregation, ranking, Award, and controlled official-closeout semantics while preserving Judge independence, provenance, anonymity boundaries, accessibility, and paper continuity.

## Knowledge-first design

MUDAC uses Daniel Jackson's **Concept Design** methodology to determine product meaning. The repository is organized as an **Open Knowledge Format (OKF) v0.2** knowledge bundle so humans and agents can retrieve current authority without recursively loading historical design phases.

Start here:

* [`AGENTS.md`](AGENTS.md) — concise repository-agent bootstrap into canonical governance and validation expectations.
* [`docs/index.md`](docs/index.md) — preferred OKF progressive-disclosure entry point.
* [`docs/canonical/`](docs/canonical/) — current canonical product/domain, conceptual UX, governance, and accepted architecture knowledge.
* [`docs/canonical/governance/`](docs/canonical/governance/) — documentation authority, agent-context, change/conflict, metadata/trust/lifecycle, validation/CI, lineage, and stable-rule governance.
* [`docs/canonical/architecture/`](docs/canonical/architecture/) — accepted current system/application architecture contracts.
* [`docs/README.md`](docs/README.md) — human-oriented documentation authority summary.

Numbered phase directories remain preserved as rationale and design provenance. Canonical documents point backward to material historical `sources`, while phase `index.md` files map forward to current canonical successors.

Knowledge structure is validated by [`scripts/validate_knowledge.py`](scripts/validate_knowledge.py) and read-only GitHub Actions CI. Passing that validator confirms deterministic repository structure only; it is not semantic verification.

Phase 004 completed the repository-wide OKF retrofit, documentation-governance model, migration audit, and knowledge-architecture exit review. The migration is structurally closed; preserved Phase 001–003 records remain historical evidence rather than unfinished metadata work.

## Design status

* **Phase 001 — Concept Design Foundation:** Complete
* **Phase 002 — Concept Specification, Policy & Synchronization Refinement:** Complete
* **Phase 003 — Conceptual UX Architecture:** Complete
* **Phase 004 — Knowledge Architecture, OKF Retrofit & Documentation Governance:** Complete
* **Phase 005 — System, Application, Data & Synchronization Architecture:** In Progress
  * 005-A — Architectural Drivers, Quality Attributes, Trust Boundaries & Decision Principles: Complete
  * **005-B — Application Boundaries, Modules, Domain Services & Dependency Architecture: Next**

## Architecture boundary

The intended delivery boundary remains **GitHub Actions → AWS**, but front-end framework, component system, identity provider, API style, persistence, offline/synchronization technology, artifact infrastructure, observability, and concrete AWS services remain architecture choices rather than assumptions inherited from the knowledge tree.

The current [Architectural Foundation](docs/canonical/architecture/architectural-foundation.md) establishes `ARCH-001` through `ARCH-008`: upstream semantic authority, authoritative transition confirmation, client/local non-authority, projection boundaries, attribution preservation, retry/failure identity, disclosure enforcement, and freshness/uncertainty representation.

Phase 005 proceeds from that foundation, evaluates architecture alternatives before locking technologies, and places accepted architecture contracts under [`docs/canonical/architecture/`](docs/canonical/architecture/) while preserving Phase 005 records as rationale and source lineage.

This repository remains in design; production implementation has not begun.

# MUDAC Competition Demo

MUDAC is a documentation-first design effort for a web application supporting fair, traceable, resilient judging for live student data competitions.

Student Teams present analyses to Panels of volunteer Judges. Each Judge independently authors a Rubric-based Scorecard for a Team in a Judging Encounter. Authoritative Scorecards feed explicit Coverage, aggregation, ranking, Award, and controlled official-closeout semantics while preserving Judge independence, provenance, anonymity boundaries, accessibility, and paper continuity.

## Knowledge-first design

MUDAC uses Daniel Jackson's **Concept Design** methodology to determine product meaning. The repository is organized as an **Open Knowledge Format (OKF) v0.2** knowledge bundle so humans and agents can retrieve current authority without recursively loading historical design phases.

Start here:

* [`AGENTS.md`](AGENTS.md) — concise repository-agent bootstrap into canonical governance.
* [`docs/index.md`](docs/index.md) — preferred OKF progressive-disclosure entry point.
* [`docs/canonical/`](docs/canonical/) — current canonical product/domain and conceptual UX knowledge.
* [`docs/canonical/governance/`](docs/canonical/governance/) — documentation authority, agent-context, change/conflict, lineage, and stable-rule governance.
* [`docs/README.md`](docs/README.md) — human-oriented documentation authority summary.

Numbered phase directories remain preserved as rationale and design provenance. Canonical documents point backward to material historical `sources`, while phase `index.md` files map forward to current canonical successors.

## Design status

* **Phase 001 — Concept Design Foundation:** Complete
* **Phase 002 — Concept Specification, Policy & Synchronization Refinement:** Complete
* **Phase 003 — Conceptual UX Architecture:** Complete
* **Phase 004 — Knowledge Architecture, OKF Retrofit & Documentation Governance:** In Progress
  * 004-A Complete
  * 004-B Complete
  * 004-C Complete
  * 004-D Complete
  * 004-E Complete
  * 004-F Complete
  * **004-G Next — OKF Metadata, Trust, Verification, Lifecycle & Freshness Conventions**

System, Application, Data & Synchronization Architecture follows as **Phase 005**.

## Architecture boundary

The intended deployment boundary remains **GitHub Actions → AWS**, but front-end framework, component system, identity provider, API style, persistence, offline/synchronization technology, artifact infrastructure, observability, and concrete AWS services remain downstream architecture choices. Those choices must satisfy canonical product/UX/governance contracts rather than redefine them.

This repository remains in design; production implementation has not begun.
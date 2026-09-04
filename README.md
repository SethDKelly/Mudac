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
* **Phase 005 — System, Application, Data & Synchronization Architecture:** Complete
  * 005-A through 005-I: Complete
  * 005-J — Consolidation, Threat/Failure Review & Implementation-Readiness Exit: Complete
* **Phase 006 — Implementation Planning, Delivery Slices & Verification Strategy:** Next

## Current architecture posture

MUDAC's current canonical architecture is a **modular-monolith-first** system with six semantic modules, a PostgreSQL authority store with append-stable Version/Provenance history, explicit command/query and idempotency/concurrency semantics, provider-adapted Identity/Participation/Access, bounded IndexedDB Draft continuity, immutable artifact/evidence storage, React + TypeScript browser architecture, and a concrete AWS runtime.

Production is single-active `us-east-2` and Multi-AZ: CloudFront fronts private origins; ECS/Fargate runs the API and bounded workers; RDS PostgreSQL Multi-AZ is authoritative persistence; Cognito User Pools authenticates while MUDAC retains application authority; SQS carries retryable async work; private evidence/Artifacts use encrypted/versioned S3; GitHub Actions deploys through OIDC-federated AWS roles; CloudWatch/ADOT/Application Signals cover infrastructure and semantic health; and whole-Region live-event failure falls back to paper until one restored digital authority is explicitly validated and promoted.

The [Phase 005 exit review](docs/005-system-application-data-synchronization-architecture/005-J-phase-005-consolidation-threat-failure-review-implementation-readiness-exit.md) found no blocking cross-layer authority contradiction. MUDAC is **implementation-planning ready, not production certified**. Remaining work is implementation selection, testing, operational evidence, and delivery governance rather than another unresolved architecture layer.

Concrete backend framework/language, ORM/migration/OpenAPI/IaC tooling, local Draft privacy/retention implementation, session/CSRF/idempotency mechanics, artifact renderer/upload validation, module dependency enforcement, measured workload/SLO/RTO/RPO targets, and production recovery/security/accessibility evidence belong to the implementation planning and verification phase.

Production implementation has not begun.
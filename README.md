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
  * 005-C — Data Model, Persistence, Versioning, Provenance & Derived-Projection Architecture: Complete
  * 005-D — Identity, Authentication, Participation, Access & Session Architecture: Complete
  * 005-E — Commands, Queries, API Contracts, Transactions, Idempotency & Concurrency Architecture: Complete
  * 005-F — Draft Persistence, Synchronization, Offline/Degraded Operation & Conflict Recovery: Complete
  * 005-G — Paper Capture, Export, Artifact, Publication & External-Representation Architecture: Complete
  * 005-H — Front-End State, Navigation, Component-System & Responsive Interaction Architecture: Complete
  * **005-I — AWS Runtime, Deployment, Security, Observability, Backup & Cost Architecture: Next**

## Current architecture posture

The [Architectural Foundation](docs/canonical/architecture/architectural-foundation.md) defines architecture-wide `ARCH-*` rules. [Application Boundaries](docs/canonical/architecture/application-boundaries.md) defines `MOD-*` rules and selects a **modular-monolith-first** authoritative application with six semantic modules: Competition Governance, Identity/Participation/Access, Judging Operations, Evaluation, Outcomes/Closeout, and External Representation.

[Data & Persistence Architecture](docs/canonical/architecture/data-persistence.md) defines `DATA-*` rules and selects one PostgreSQL-compatible relational authority database with module-owned logical namespaces. Durable resource identities are storage-independent; working/current state is distinct from immutable committed Versions; meaningful Provenance is append-stable; referenced authoritative evidence is not removed by ordinary destructive cascades; derived calculations retain a reconstructible basis; projections are rebuildable/non-authoritative; and transactional outbox/change records prevent authoritative commits from silently diverging from asynchronous projection/integration propagation.

[Identity, Authentication, Access & Session Architecture](docs/canonical/architecture/identity-access-session.md) defines `AUTH-*` rules. Authentication is provider-backed but does not grant Competition authority; external subjects map explicitly to stable MUDAC Identity; Competition Participation/context remains MUDAC-owned; Access is capability-oriented and reevaluated from current authoritative state; browsers use opaque first-party server sessions; Event Completed expires ordinary Judge private-evaluation capability even for stale sessions; dual-role capability sets remain isolated; correction grants are narrow/reverified; and routine Administrator/break-glass authority remains distinct from Competition decision authority.

[Commands, Queries, API, Transaction & Concurrency Architecture](docs/canonical/architecture/commands-api-concurrency.md) defines `API-*` rules. The primary browser boundary is versioned HTTPS/JSON; commands and queries are distinct; high-consequence transitions use explicit intent-bearing commands; confirmed success occurs only after authoritative commit; optimistic revision/precondition checks are the default concurrency mechanism with targeted locking/stronger isolation where demonstrated; durable idempotency plus logical uniqueness makes retries converge; and projection-backed reads expose freshness without becoming write authority.

[Draft Synchronization, Offline & Recovery Architecture](docs/canonical/architecture/synchronization-recovery.md) defines `SYNC-*` rules. Local persistence protects eligible non-authoritative Judge Draft work; synchronization is revision-aware against server authority; stale conflicts preserve both local and server traces; multi-device work converges on one logical Scorecard; authoritative transitions remain online/server-confirmed; reconnect re-establishes current Identity/Participation/Access before queued work is applied; uncertain command outcomes reconcile before retry; and paper remains the preferred event-continuity fallback when authoritative digital operation cannot be trusted.

[External Representation, Artifact & Publication Architecture](docs/canonical/architecture/external-representation.md) defines `REP-*` rules. Paper-origin Scorecard authority remains inside Evaluation with source/capture provenance preserved; durable Export/Artifact identity binds exact source revision, purpose, and disclosure profile; binary scans/PDFs/packages live in immutable object/blob storage behind relational authority metadata; artifact integrity is digest-addressable; generation, validation, Publication, and delivery remain distinct; source changes produce affected/successor representations rather than overwriting historical bytes; and URLs/QR/signed links/object/CDN locations remain delivery mechanisms rather than authority.

[Front-End State, Navigation & Interaction Architecture](docs/canonical/architecture/frontend-interaction.md) defines `FE-*` rules. The browser baseline is React + TypeScript with React Router Data mode for navigation/layout/error boundaries, TanStack Query for remote server/projection caching, and an IndexedDB-backed adapter for non-authoritative Draft continuity. Client state remains partitioned by ownership; high-consequence command outcomes remain explicit and non-optimistic; Judge interaction is phone-primary; Organizer interaction remains exception-first and responsively equivalent; component layering preserves semantic ownership; core workflows target WCAG 2.2 AA; and push transport is optional latency optimization rather than correctness authority.

Concrete package manager/build/CSS/component-library choices, IndexedDB wrapper/service-worker implementation, telemetry/testing stack, OpenAPI tooling, ORM/unit-of-work implementation, identity-provider vendor, exact session/idempotency stores and timings, queue/broker, push transport, object-storage/CDN product, PDF/rendering/template stack, observability, backup policy, and concrete AWS services remain later architecture decisions. The intended delivery boundary remains **GitHub Actions → AWS**.

This repository remains in design; production implementation has not begun.
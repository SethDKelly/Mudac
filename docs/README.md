# MUDAC Design Documentation

The repository is the durable design authority; conversation history is working context.

## Preferred navigation

Start at [index.md](index.md), the OKF v0.2 bundle root.

For current product/domain, conceptual UX, governance, and accepted architecture meaning, use [Canonical Knowledge](canonical/). Repository agents use root [`AGENTS.md`](../AGENTS.md) as a thin bootstrap into the same canonical governance.

Use numbered phase directories for rationale, design evolution, architecture alternatives, and source provenance. Each numbered phase has an OKF `index.md` that maps records forward to current canonical successors.

## Governance

Current governance lives under [canonical/governance/](canonical/governance/), including:

* [Documentation Authority & Canonical Ownership](canonical/governance/documentation-authority.md) — `DOC-*`;
* [Agent Context & Progressive Retrieval](canonical/governance/agent-context.md) — `CTX-*`;
* [Canonical Change & Conflict Governance](canonical/governance/change-governance.md) — `CHG-*`;
* [OKF Metadata, Trust, Verification, Lifecycle & Freshness](canonical/governance/metadata-trust-lifecycle.md) — `META-*`;
* [Knowledge Validation & CI Enforcement](canonical/governance/validation-enforcement.md) — `VAL-*`;
* [Stable Rule Identifiers](canonical/governance/rule-identifiers.md);
* [Source Lineage](canonical/governance/source-lineage.md).

These owners govern the details. This README routes to them and does not reproduce their rule bodies.

## Design status

* Phase 001 — Concept Design Foundation: **Complete**
* Phase 002 — Concept Specification, Policy & Synchronization Refinement: **Complete**
* Phase 003 — Conceptual UX Architecture: **Complete**
* Phase 004 — Knowledge Architecture, OKF Retrofit & Documentation Governance: **Complete**
* Phase 005 — System, Application, Data & Synchronization Architecture: **In Progress**
  * 005-A — Architectural Drivers, Quality Attributes, Trust Boundaries & Decision Principles: **Complete**
  * 005-B — Application Boundaries, Modules, Domain Services & Dependency Architecture: **Complete**
  * 005-C — Data Model, Persistence, Versioning, Provenance & Derived-Projection Architecture: **Complete**
  * 005-D — Identity, Authentication, Participation, Access & Session Architecture: **Complete**
  * 005-E — Commands, Queries, API Contracts, Transactions, Idempotency & Concurrency Architecture: **Complete**
  * 005-F — Draft Persistence, Synchronization, Offline/Degraded Operation & Conflict Recovery: **Complete**
  * 005-G — Paper Capture, Export, Artifact, Publication & External-Representation Architecture: **Complete**
  * 005-H — Front-End State, Navigation, Component-System & Responsive Interaction Architecture: **Complete**
  * 005-I — AWS Runtime, Deployment, Security, Observability, Backup & Cost Architecture: **Complete**
  * **005-J — Phase 005 Consolidation, Threat/Failure Review & Implementation-Readiness Exit: Next**

Current accepted architecture is routed through [canonical/architecture/](canonical/architecture/): the [Architectural Foundation](canonical/architecture/architectural-foundation.md) owns `ARCH-*`, [Application Boundaries](canonical/architecture/application-boundaries.md) owns `MOD-*`, [Data & Persistence Architecture](canonical/architecture/data-persistence.md) owns `DATA-*`, [Identity, Authentication, Access & Session Architecture](canonical/architecture/identity-access-session.md) owns `AUTH-*`, [Commands, Queries, API, Transaction & Concurrency Architecture](canonical/architecture/commands-api-concurrency.md) owns `API-*`, [Draft Synchronization, Offline & Recovery Architecture](canonical/architecture/synchronization-recovery.md) owns `SYNC-*`, [External Representation, Artifact & Publication Architecture](canonical/architecture/external-representation.md) owns `REP-*`, [Front-End State, Navigation & Interaction Architecture](canonical/architecture/frontend-interaction.md) owns `FE-*`, and [AWS Runtime, Security & Operations Architecture](canonical/architecture/aws-runtime-operations.md) owns `AWS-*`.

The current production posture is single-active `us-east-2` and Multi-AZ: CloudFront is the public application/data edge with private S3 and VPC-origin/internal-ALB origins; ECS/Fargate runs the modular-monolith API and bounded worker roles; RDS PostgreSQL Multi-AZ is authority; Cognito is the authentication provider while MUDAC retains Identity/Participation/Access and opaque sessions; private evidence/Artifacts use encrypted/versioned S3; SQS handles retryable asynchronous work; GitHub Actions deploys through OIDC-federated roles; CloudWatch/ADOT/Application Signals cover infrastructure and semantic health; backups are restored/tested and replicated outside the active Region; and whole-Region live-event loss falls back to paper until one recovered digital authority is explicitly promoted.

Knowledge CI checks deterministic structure, links, stable IDs, source edges, and routing. A green validation run is structural evidence only and never creates `verified` metadata or replaces semantic review.
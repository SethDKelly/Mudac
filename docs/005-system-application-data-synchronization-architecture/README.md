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
| 005-B | [Application Boundaries, Modules, Domain Services & Dependency Architecture](005-B-application-boundaries-modules-domain-services-dependency-architecture.md) | **Complete** |
| 005-C | [Data Model, Persistence, Versioning, Provenance & Derived-Projection Architecture](005-C-data-model-persistence-versioning-provenance-derived-projection-architecture.md) | **Complete** |
| 005-D | [Identity, Authentication, Participation, Access & Session Architecture](005-D-identity-authentication-participation-access-session-architecture.md) | **Complete** |
| 005-E | [Commands, Queries, API Contracts, Transactions, Idempotency & Concurrency Architecture](005-E-commands-queries-api-contracts-transactions-idempotency-concurrency-architecture.md) | **Complete** |
| 005-F | [Draft Persistence, Synchronization, Offline/Degraded Operation & Conflict Recovery](005-F-draft-persistence-synchronization-offline-degraded-operation-conflict-recovery.md) | **Complete** |
| 005-G | [Paper Capture, Export, Artifact, Publication & External-Representation Architecture](005-G-paper-capture-export-artifact-publication-external-representation-architecture.md) | **Complete** |
| 005-H | [Front-End State, Navigation, Component-System & Responsive Interaction Architecture](005-H-front-end-state-navigation-component-system-responsive-interaction-architecture.md) | **Complete** |
| 005-I | [AWS Runtime, Deployment, Security, Observability, Backup & Cost Architecture](005-I-aws-runtime-deployment-security-observability-backup-cost-architecture.md) | **Complete** |
| 005-J | Phase 005 Consolidation, Threat/Failure Review & Implementation-Readiness Exit | **Next** |

## Architecture sequence

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

## Authoritative baseline through 005-I

005-A establishes [Architectural Foundation](../canonical/architecture/architectural-foundation.md) and `ARCH-001` through `ARCH-008`.

005-B establishes [Application Boundaries](../canonical/architecture/application-boundaries.md) and `MOD-001` through `MOD-010`.

005-C establishes [Data & Persistence Architecture](../canonical/architecture/data-persistence.md) and `DATA-001` through `DATA-014`.

005-D establishes [Identity, Authentication, Access & Session Architecture](../canonical/architecture/identity-access-session.md) and `AUTH-001` through `AUTH-014`.

005-E establishes [Commands, Queries, API, Transaction & Concurrency Architecture](../canonical/architecture/commands-api-concurrency.md) and `API-001` through `API-015`.

005-F establishes [Draft Synchronization, Offline & Recovery Architecture](../canonical/architecture/synchronization-recovery.md) and `SYNC-001` through `SYNC-014`.

005-G establishes [External Representation, Artifact & Publication Architecture](../canonical/architecture/external-representation.md) and `REP-001` through `REP-015`.

005-H establishes [Front-End State, Navigation & Interaction Architecture](../canonical/architecture/frontend-interaction.md) and `FE-001` through `FE-018`.

005-I establishes [AWS Runtime, Security & Operations Architecture](../canonical/architecture/aws-runtime-operations.md) and `AWS-001` through `AWS-018`.

The current production/cloud baseline is:

- one active production Region, `us-east-2`, with at least two Availability Zones and explicit cold recovery to `us-east-1` rather than active-active cross-Region authority;
- CloudFront is the public MUDAC application/data edge, serving the private S3 React origin through OAC and reaching an internal ALB through CloudFront VPC origins;
- the modular monolith runs as immutable ECR releases on ECS/Fargate, with a redundant API service and bounded worker execution for retryable asynchronous work;
- RDS for PostgreSQL Multi-AZ is the production authority database; Aurora, RDS Proxy, read replicas and ElastiCache remain non-baseline until measured requirements justify them;
- Cognito User Pools is the initial authentication provider behind the MUDAC adapter, while Identity/Participation/Access and opaque sessions remain MUDAC-owned;
- SQS plus DLQs carries durable retryable asynchronous work and never replaces PostgreSQL authority or transactional-outbox semantics;
- private evidence/Artifact S3 storage uses versioning, encryption and immutable object identities behind authoritative relational metadata;
- production ALB/ECS/RDS remain private; AZ-local NAT provides required public-domain egress while a free S3 gateway endpoint removes S3 traffic from NAT;
- runtime, worker, migration, deployment and other AWS capabilities use distinct least-privilege IAM roles, Secrets Manager and KMS where appropriate;
- production/nonproduction workloads are account/environment separated and GitHub Actions deploys through OIDC-federated IAM roles rather than long-lived AWS keys;
- infrastructure is reproducible through IaC; ECS rolling deployments use immutable image releases and circuit-breaker rollback; database migrations are separately privileged and expand/contract compatible;
- production observes a live-event deployment freeze except for necessary incident response;
- frontend release assets are content-addressed and promoted only after complete upload, with backend/API compatibility maintained across rolling/cached clients;
- CloudFront/ACM/WAF/Shield/S3 OAC/CloudTrail/security groups complement but never replace MUDAC Access, CSRF, command or disclosure enforcement;
- CloudWatch structured logs/metrics/alarms plus AWS Distro for OpenTelemetry/Application Signals cover both infrastructure and MUDAC-semantic health;
- RDS keeps 35 days of PITR and cross-Region automated-backup replication; critical S3 evidence/Artifact bytes receive versioning and cross-Region recovery protection where loss would defeat reconstruction;
- backup existence is insufficient—restore exercises and application validation establish actual recovery confidence;
- a whole-Region outage during judging falls back to identified paper continuity until one restored digital authority is explicitly validated/promoted;
- cost optimization removes unjustified services and scales nonproduction down, but does not remove production Multi-AZ authority, API redundancy, required NAT availability, evidence protection, backup or security logging.

Concrete IaC tool, backend implementation language/framework, exact container/database sizes, CSS/component-primitive implementation, queue worker library, signed-delivery implementation, and numeric SLO/RTO/RPO commitments remain implementation details or measured outputs rather than unresolved architecture authority.

## Next

005-J — **Phase 005 Consolidation, Threat/Failure Review & Implementation-Readiness Exit** will exercise the complete architecture against authority, privacy, concurrency, degraded-network, database/AZ/Region failure, deployment/migration rollback, artifact/publication, identity-provider, backup/restore and cost-failure scenarios; reconcile any cross-owner contradictions; and decide whether MUDAC has enough stable system architecture to proceed into implementation design without reopening product semantics.
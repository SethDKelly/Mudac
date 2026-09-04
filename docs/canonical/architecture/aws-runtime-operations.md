---
type: Architecture Contract
title: AWS Runtime, Security & Operations Architecture
description: Defines the production AWS topology, deployment, security, observability, backup/recovery and cost contracts that realize MUDAC's accepted application architecture.
status: stable
tags: [architecture, aws, runtime, deployment, security, observability, backup, recovery, cost]
sources:
  - resource: ../../005-system-application-data-synchronization-architecture/005-I-aws-runtime-deployment-security-observability-backup-cost-architecture.md
  - resource: architectural-foundation.md
  - resource: application-boundaries.md
  - resource: data-persistence.md
  - resource: identity-access-session.md
  - resource: commands-api-concurrency.md
  - resource: synchronization-recovery.md
  - resource: external-representation.md
  - resource: frontend-interaction.md
  - resource: https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-vpc-origins.html
  - resource: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-load-balancing.html
  - resource: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZ.html
  - resource: https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools.html
  - resource: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Application-Signals-Enable-ECSMain.html
generated: { by: openai/gpt-5.6-sol, at: 2026-09-04T05:28:35Z }
---

# Purpose

Define the current AWS production topology and operational contracts for MUDAC without allowing AWS service boundaries, deployment mechanics, caches, queues, identity-provider claims, or recovery infrastructure to become new sources of MUDAC semantic authority.

<a id="aws-001"></a>
## AWS-001 — Production is single-active-Region, Multi-AZ, with explicit cold regional recovery

The active production Region is `us-east-2`. The API/application and relational authority database span at least two Availability Zones. There is no active-active or independently writable secondary MUDAC Region in the baseline.

A whole-Region outage invokes paper continuity for live judging plus explicit cold restoration/promotion from replicated backups. Cross-Region recovery never creates dual current authority.

<a id="aws-002"></a>
## AWS-002 — CloudFront is the public application/data edge; origins remain private

Normal MUDAC browser/API/data delivery enters through CloudFront. The React build is served from a private S3 origin through Origin Access Control. Dynamic application traffic reaches an internal Application Load Balancer through a CloudFront VPC origin.

Production ECS tasks, ALB origin, RDS, and private evidence/artifact buckets are not directly internet-addressable. Cognito/external identity-provider user-facing endpoints remain separate external authentication dependencies rather than MUDAC data-plane authority.

<a id="aws-003"></a>
## AWS-003 — The authoritative application runs on ECS/Fargate as API and bounded worker roles

The modular monolith is packaged as immutable ECR container releases and runs on ECS/Fargate. The initial runtime separates an API service from retryable worker execution where asynchronous work is useful, while both remain implementations of the same module/application contracts.

Worker/container separation is an operational boundary, not permission to create new semantic owners.

<a id="aws-004"></a>
## AWS-004 — Production capacity favors event continuity over reactive-only scaling

Production keeps at least two healthy API tasks across at least two AZs during normal active operation. Target-tracking autoscaling may respond to CPU, memory and/or ALB demand, but known event windows are pre-scaled and load-tested before judging begins.

Fargate Spot is not used for the authoritative API path. Capacity reduction may never intentionally remove the redundancy required for production event continuity.

<a id="aws-005"></a>
## AWS-005 — RDS for PostgreSQL Multi-AZ is the production authority database

Production authoritative relational persistence uses Amazon RDS for PostgreSQL with a Multi-AZ DB instance deployment, KMS encryption, TLS connections, automated backups/PITR, and explicit database observability.

Aurora, RDS Proxy, read replicas, and a distributed database topology are not baseline requirements. They require a demonstrated workload, availability, connection-pressure, or read-scaling driver before adoption.

<a id="aws-006"></a>
## AWS-006 — Cognito authenticates; MUDAC still owns Identity, Participation, Access and sessions

Amazon Cognito User Pools is the initial authentication provider behind the MUDAC authentication adapter. Authorization-code/OIDC authentication terminates into the first-party opaque MUDAC server-session model.

Cognito user/group/token claims cannot substitute for MUDAC Participation, contextual Access, Judge authorship, Competition authority, or historical Identity. Federation to later SAML/OIDC providers must preserve the same MUDAC Identity-link boundary.

<a id="aws-007"></a>
## AWS-007 — Private evidence and Artifact bytes use versioned, encrypted S3 behind relational authority metadata

Private paper evidence, Artifacts and print packages use private S3 storage with Block Public Access, Versioning, encryption appropriate to the data class, and unique non-overwriting object identities. Production private evidence/Artifact storage uses SSE-KMS with S3 Bucket Keys where customer-managed-key separation is material.

The PostgreSQL `REP-*` record remains semantic authority for source/disclosure/lifecycle/provenance. S3 key, version, digest, CDN path, or signed URL remains storage/delivery information.

S3 Object Lock is not baseline-mandatory until retention policy establishes a real WORM requirement compatible with its irreversible bucket implications.

<a id="aws-008"></a>
## AWS-008 — SQS carries retryable asynchronous work, not domain authority

Durable asynchronous jobs use SQS with encryption, bounded retries, idempotent consumers, and dead-letter queues. Authoritative changes reach asynchronous work through the transactional-outbox boundary where applicable.

Queue existence/delivery/order does not establish Scorecard, outcome, Publication, or other MUDAC authority, and SQS is not the primary event store.

<a id="aws-009"></a>
## AWS-009 — Application and database tiers remain private; outbound egress is explicit and availability-aware

Production ALB, ECS, and RDS resources live in private subnets and ECS tasks have no public IPs. Production uses AZ-local NAT Gateway egress because current runtime dependencies include public OAuth/domain endpoints and other explicit external services. Nonproduction may accept one NAT Gateway.

An S3 gateway endpoint is baseline because it is cost-free and keeps S3 artifact traffic off NAT. Paid interface endpoints are adopted selectively when measured traffic, cost, or security benefit justifies them rather than being provisioned decoratively.

<a id="aws-010"></a>
## AWS-010 — IAM, secrets and encryption preserve least privilege and actor separation

ECS execution, API runtime, worker runtime, migration, deployment, backup/restore, and observability capabilities use distinct least-privilege IAM roles where their permissions differ. Runtime AWS credentials come from task roles rather than static keys.

Secrets Manager owns application/database secrets that require protected storage/rotation; KMS protects production authority/private evidence stores where key-policy separation is material. The ordinary application runtime does not hold schema-migration/DDL or break-glass permissions.

<a id="aws-011"></a>
## AWS-011 — Production and nonproduction deployment authority is account/environment separated and GitHub-OIDC federated

Production and nonproduction workloads live in separate AWS accounts. GitHub Actions assumes environment-specific AWS deployment roles through OIDC with trust restricted to the intended repository and protected environment/ref.

Long-lived AWS access keys are not stored in GitHub for deployment. Production deployment uses GitHub environment protection/approval appropriate to the project.

<a id="aws-012"></a>
## AWS-012 — Infrastructure and releases are reproducible, immutable and rollback-aware

Persistent AWS infrastructure is declared through Infrastructure as Code; the specific IaC tool is replaceable implementation machinery. Manual production console changes are emergency exceptions and are reconciled back into code.

Backend releases use immutable ECR image references and ECS deployment health/circuit-breaker rollback. Schema migration runs under a dedicated migration identity and follows expand/contract compatibility so rolling old/new application tasks can coexist safely. Destructive migration is not coupled blindly to application rollout.

Known live-judging windows use a production change freeze except for necessary incident response.

<a id="aws-013"></a>
## AWS-013 — Frontend release promotion is content-addressed and API-compatible

Frontend builds publish content-hashed immutable assets before switching the release entrypoint/manifest. CloudFront invalidation targets mutable entry/manifest paths rather than invalidating content-addressed assets.

Frontend and API releases maintain a compatibility window for cached clients and rolling backend tasks. Rolling back the frontend selects a prior release entrypoint and never rewrites authoritative application data.

<a id="aws-014"></a>
## AWS-014 — Edge/infrastructure security complements but never replaces application authority

CloudFront/ACM TLS, AWS WAF managed/rate controls, Shield Standard, private origins, S3 OAC/Block Public Access, security groups, encryption, security headers/CSP, CloudTrail and related controls reduce infrastructure exposure.

None of them substitutes for server-side MUDAC Access, CSRF protection, domain validation, command preconditions, disclosure policy, or Provenance.

CloudTrail captures AWS control-plane activity; MUDAC Provenance captures domain authority/authorship. Both are retained as distinct evidence systems.

<a id="aws-015"></a>
## AWS-015 — Observability includes MUDAC semantic health, not only infrastructure utilization

Structured application logs, CloudWatch metrics/alarms, AWS Distro for OpenTelemetry and CloudWatch Application Signals are the baseline telemetry path. Operational views include infrastructure signals plus command/result classes, idempotency behavior, outbox/SQS lag, projection freshness, synchronization/recovery indicators, Artifact generation/publication failures, authentication dependency health, backup health and release identity.

Logs minimize sensitive content and exclude credentials/tokens/private Judge prose unless an explicitly governed diagnostic path requires otherwise. Retention is finite and data-class specific.

<a id="aws-016"></a>
## AWS-016 — Backups are multi-layered, cross-Region where material, and trusted only after restore testing

Production RDS retains 35 days of automated point-in-time recovery and replicates automated PostgreSQL backups to `us-east-1` with destination-region encryption. Materially risky schema/data migrations take an explicit pre-change recovery point when appropriate.

Critical S3 evidence/Artifact storage uses Versioning and cross-Region replication/copy where loss would defeat evidence or representation reconstruction. Lifecycle deletion is prohibited until product retention policy authorizes it.

Restore capability is periodically tested and application-validated; successful backup creation alone is not recovery evidence.

<a id="aws-017"></a>
## AWS-017 — Regional disaster recovery restores one authority and uses paper for live continuity

MUDAC does not fail open to an independently writable secondary Region. For complete active-Region loss, live judging uses the canonical paper fallback while operators restore database/object/runtime state into the recovery Region from replicated backups and IaC.

Recovery includes explicit validation and one-environment promotion before digital authority resumes. Paper and any local non-authoritative Draft traces are reconciled afterward through existing `SYNC-*`, `REP-*`, and correction rules.

RPO/RTO claims must come from measured restore exercises rather than untested documentation targets.

<a id="aws-018"></a>
## AWS-018 — Cost optimization removes unjustified infrastructure, not trust guarantees

The baseline deliberately avoids Aurora, RDS Proxy, read replicas, ElastiCache, EKS, service mesh, API Gateway as the primary API path, active-active multi-Region compute, and blanket paid VPC interface endpoints until concrete requirements justify them.

Nonproduction may reduce task count, availability topology and database redundancy. Production Multi-AZ authority, minimum API redundancy, required NAT availability, backups, encryption/security logging and evidence preservation are not optional cost-cutting knobs.

AWS Budgets, Cost Anomaly Detection, cost-allocation tags, finite log retention, event-aware capacity scaling, S3 lifecycle transitions allowed by retention policy, and later commitment discounts are the preferred cost controls.
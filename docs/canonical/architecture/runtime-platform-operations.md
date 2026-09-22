---
type: Architecture Contract
title: Current Runtime Platform, Security, Deployment, Availability, Observability & Disaster-Recovery Architecture
description: "Accepted ADQ-009 AWS runtime architecture: single-active-Region Multi-AZ production, CloudFront/WAF private-origin edge, ECS/Fargate application and bounded workers, RDS PostgreSQL Multi-AZ authority, Cognito authentication behind MUDAC IAM, private/versioned S3 artifacts, SQS asynchronous work, resilient private networking, OIDC-federated deployment, semantic observability, tested backups and cold regional recovery."
status: stable
tags: [architecture, current, aws, runtime, security, deployment, availability, observability, disaster-recovery, cost]
sources:
  - resource: architecture-drivers.md
  - resource: application-ownership-boundaries.md
  - resource: persistence-history-recovery.md
  - resource: identity-access-authority.md
  - resource: interface-command-concurrency.md
  - resource: offline-continuity-reconciliation.md
  - resource: artifact-export-publication-delivery.md
  - resource: browser-client-interaction.md
  - resource: aws-runtime-operations.md
  - resource: ../governance/downstream-realization-obligations.md
  - resource: https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-vpc-origins.html
  - resource: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-load-balancing.html
  - resource: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-rebalancing.html
  - resource: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZSingleStandby.html
  - resource: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReplicateBackups.html
  - resource: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithAutomatedBackups.BackupRetention.html
  - resource: https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication-requirements.html
  - resource: https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-identity-provider.html
  - resource: https://docs.github.com/en/actions/how-tos/secure-your-work/security-harden-deployments/oidc-in-aws
  - resource: https://docs.aws.amazon.com/vpc/latest/userguide/nat-gateways-regional.html
  - resource: https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-statement-type-rate-based-caveats.html
  - resource: ../../019-architecture-engineering-reentry/019-J-runtime-platform-security-deployment-availability-observability-disaster-recovery-architecture.md
generated: { by: openai/gpt-5.6-sol, at: 2026-09-22T14:35:00-05:00 }
---

# Authority

This document is **current accepted architecture authority for ADQ-009**.

It selects AWS as the initial production runtime platform and establishes the deployment, network, security, availability, asynchronous-runtime, observability, backup and disaster-recovery topology.

It does not establish production capacity numbers, contractual uptime, exact RTO/RPO, jurisdiction-specific retention/data-residency rules, final instance/task sizes, exact autoscaling thresholds or implementation package boundaries.

<a id="run-001"></a>
## RUN-001 — AWS is the selected initial production runtime platform

MUDAC uses AWS managed services for the initial production runtime.

AWS service boundaries remain implementation/runtime boundaries and never redefine MUDAC Concept ownership, application authority or product semantics.

Provider replacement remains possible behind accepted application/storage/interface contracts.

<a id="run-002"></a>
## RUN-002 — Production is single-active-Region and Multi-AZ; regional recovery is cold

The active production Region is **US East (Ohio), us-east-2**.

Production application and authoritative relational persistence span at least two Availability Zones.

**US East (N. Virginia), us-east-1** is the cold regional recovery target.

There is no active-active or independently writable secondary MUDAC Region in the baseline.

<a id="run-003"></a>
## RUN-003 — Whole-Region loss reduces digital authority rather than creating dual writers

A complete active-Region outage does not fail open to a second independently current authority.

Live competition continuity may use RCV paper/local recovery paths while operators restore one digital authority in the recovery Region.

Digital authority resumes only after recovery validation and explicit environment promotion.

<a id="run-004"></a>
## RUN-004 — CloudFront is the public application edge; application origins remain private

Normal browser application traffic enters through Amazon CloudFront.

Static client assets use a private S3 origin with origin-restricted access.

Dynamic HTTPS application/API traffic uses a CloudFront VPC origin to an internal Application Load Balancer in private subnets.

ECS application tasks, the internal ALB and RDS are not directly internet-addressable.

<a id="run-005"></a>
## RUN-005 — AWS WAF and edge controls provide infrastructure abuse reduction, not semantic authorization

Production CloudFront is protected by AWS WAF controls appropriate to measured traffic, including managed protections and rate-based controls where useful.

WAF rate limiting is approximate infrastructure protection and must not become the only enforcement for semantic limits, Access, idempotency or high-consequence command rules.

TLS, security headers/CSP and edge controls complement IAM/CMD authority rather than replace it.

<a id="run-006"></a>
## RUN-006 — The authoritative application runs as an ECS/Fargate modular-monolith service

The initial authoritative application is packaged as immutable container images and runs on Amazon ECS with AWS Fargate.

The runtime preserves the BND ownership-preserving modular monolith.

Network/deployment units do not become new semantic modules.

EKS/Kubernetes and self-managed EC2 container hosts are not baseline requirements.

<a id="run-007"></a>
## RUN-007 — Production API capacity preserves cross-AZ continuity before reactive scaling

Production runs at least two authoritative API tasks distributed across at least two Availability Zones behind the internal ALB.

Autoscaling may add capacity from measured load, but baseline event continuity does not depend on scaling from zero or on a single task.

Fargate Spot is not used for the authoritative production API baseline.

<a id="run-008"></a>
## RUN-008 — Asynchronous workers are separate runtime roles only for semantically separable work

Long-running Artifact generation, projection/integration work and similar CMD-019 tasks may run in a separate ECS/Fargate worker service.

Worker separation is operational only.

Ordinary authoritative commands remain synchronously commit-confirmed where current CMD semantics require it.

<a id="run-009"></a>
## RUN-009 — RDS for PostgreSQL Multi-AZ DB instance is the initial authority database

The PST PostgreSQL-compatible authority store is realized initially as **Amazon RDS for PostgreSQL, Multi-AZ DB instance deployment**.

The synchronous standby in another Availability Zone exists for high availability/failover and is not a read-scaling replica.

Aurora, RDS Multi-AZ DB cluster, read replicas and RDS Proxy require a demonstrated availability, connection-pressure, scaling or recovery driver before adoption.

<a id="run-010"></a>
## RUN-010 — Server-controlled application sessions initially use the relational runtime

IAM opaque first-party sessions are initially backed by the PostgreSQL-compatible runtime rather than requiring a separate Redis/session service.

Session records remain continuity/security state, not product-domain authority.

A separate session/cache service requires measured scale, availability or isolation justification.

<a id="run-011"></a>
## RUN-011 — Amazon Cognito User Pools is the initial authentication provider behind the IAM adapter

Amazon Cognito User Pools is the initial managed external authentication provider.

Cognito establishes authentication proof only.

MUDAC still owns stable Identity linkage, Competition Participation, contextual Access and opaque first-party application sessions.

Cognito federation support may later add Google, OIDC or SAML providers without making provider groups/claims MUDAC semantic roles.

<a id="run-012"></a>
## RUN-012 — Private Artifact/evidence bytes use versioned encrypted S3 behind ART authority metadata

ART large binary payloads use private Amazon S3 buckets with:

- Block Public Access;
- Versioning;
- non-overwriting object identity;
- encryption appropriate to the data class;
- integrity/digest linkage in relational ART metadata.

Sensitive production evidence/artifacts use SSE-KMS where key-policy separation is material.

S3 keys, versions and URLs remain storage/delivery locators, not semantic identity.

<a id="run-013"></a>
## RUN-013 — SQS carries bounded asynchronous technical work, never domain authority

Semantically separable asynchronous jobs use Amazon SQS where durable queueing is justified.

Queues use bounded retry, dead-letter handling and idempotent consumers.

Authoritative changes are coupled to later asynchronous work through PST/CMD durable propagation intent where required.

Queue delivery/order/existence never establishes product authority.

<a id="run-014"></a>
## RUN-014 — Application/data tiers remain private and outbound internet dependency is explicit

ECS tasks and RDS use private subnets and application tasks have no public IP addresses.

Outbound access to authentication/provider and other approved external endpoints uses resilient AWS-managed NAT.

The baseline must not couple all production egress to one zonal failure point.

Current AWS regional NAT gateway capability is preferred when environment support and cost qualification confirm fit; per-AZ zonal NAT remains an allowed equivalent resilience realization.

<a id="run-015"></a>
## RUN-015 — AWS service endpoints are adopted for concrete security/cost benefit, not decoratively

An S3 gateway VPC endpoint is baseline for private application-to-S3 traffic.

Other interface endpoints are introduced when measured traffic, security posture, egress dependency or cost demonstrates benefit.

PrivateLink endpoint count is not an architecture quality metric.

<a id="run-016"></a>
## RUN-016 — IAM roles, secrets and encryption preserve least privilege and actor separation

ECS execution, API runtime, worker runtime, migration, deployment, backup/restore and observability capabilities use distinct least-privilege IAM roles where privileges differ.

Application workloads use task roles rather than static AWS keys.

AWS Secrets Manager stores protected runtime secrets that require managed handling; AWS KMS protects production authority/private-object stores where key-policy separation is material.

Ordinary runtime credentials do not carry schema-migration or break-glass authority.

<a id="run-017"></a>
## RUN-017 — Production and nonproduction deployment authority is separated and GitHub deployment is OIDC-federated

Production and nonproduction use separate AWS account/environment authority.

GitHub Actions obtains environment-specific AWS deployment roles through OpenID Connect federation with trust restricted to the intended repository/ref/environment.

Long-lived AWS deployment access keys are not stored as GitHub secrets.

Recovery deployment authority is separately scoped from ordinary nonproduction authority.

<a id="run-018"></a>
## RUN-018 — Infrastructure and releases are reproducible, immutable and rollback-aware

Persistent infrastructure is declared through Infrastructure as Code.

OpenTofu is the current repository implementation substrate, but the semantic/runtime contract does not depend on OpenTofu-specific behavior.

Backend releases use immutable ECR image references and health-checked ECS deployment/rollback behavior.

Schema migration runs under dedicated authority and follows forward-compatible expand/contract discipline where rolling old/new runtime overlap is possible.

<a id="run-019"></a>
## RUN-019 — Frontend release promotion preserves immutable assets and API compatibility

Browser builds publish content-addressed immutable assets before switching the mutable release entrypoint/manifest.

Deployment does not overwrite historical content-addressed assets in place.

Frontend/backend rollout maintains compatible application contracts across the supported deployment overlap window.

<a id="run-020"></a>
## RUN-020 — Observability includes semantic health and release identity

The baseline telemetry path uses structured application logging, CloudWatch metrics/alarms and OpenTelemetry-compatible application instrumentation.

Operational visibility covers infrastructure plus semantic/runtime indicators such as:

- command outcome classes and unknown/reconciliation pressure;
- idempotency/retry anomalies;
- outbox/SQS lag;
- projection freshness;
- authentication/provider health;
- local-sync/recovery pressure visible to the server;
- Artifact generation/Publication failures;
- database/failover health;
- backup/replication health;
- deployment/release identity.

Infrastructure CPU alone is not application health.

<a id="run-021"></a>
## RUN-021 — Security/audit telemetry is privacy-bounded and attributable

CloudTrail and provider audit capabilities record material infrastructure/control-plane activity.

Application logs and traces minimize secrets and protected participant/evaluation content.

Correlation identifiers support incident reconstruction without turning logs into a shadow authority store.

Operational telemetry may support Provenance/investigation but never replaces semantic history.

<a id="run-022"></a>
## RUN-022 — Authoritative database recovery uses PITR plus cross-Region backup capability

RDS automated backups and point-in-time recovery are enabled for production.

Cross-Region automated backup replication targets the cold recovery Region where supported for the selected engine/topology.

The exact automated-backup retention period remains a production configuration constrained by measured recovery objectives and current retention/privacy authority; no unverified legal retention rule is invented here.

<a id="run-023"></a>
## RUN-023 — Critical object recovery uses versioning and selective cross-Region replication/copy

S3 Versioning is required for critical retained evidence/artifact buckets.

Cross-Region replication or controlled backup copy to the recovery Region is used where loss of the active-Region object set would defeat required evidence/Artifact reconstruction.

Replication is asynchronous and therefore does not justify a zero-RPO claim.

<a id="run-024"></a>
## RUN-024 — Recovery capability is trusted only after application-level restore exercises

Successful backup creation is not disaster-recovery evidence.

Restore exercises must validate:

- authoritative relational consistency;
- required history/Provenance;
- critical object availability/integrity;
- application deployment;
- identity/session recovery posture;
- reconciliation of paper/local traces where applicable;
- one-current-authority promotion.

Exact RTO/RPO claims come from measured exercises and workload evidence.

<a id="run-025"></a>
## RUN-025 — No contractual uptime, RTO or RPO is claimed without evidence

Current architecture establishes a resilient topology but does not invent numeric uptime, RTO or RPO.

Before whole-architecture sufficiency or production readiness is claimed, measurable availability/recovery objectives and evidence must be recorded at the appropriate gate.

If no business/contractual numeric target exists, the accepted validation target must still be explicit enough to test restore and event-continuity fitness.

<a id="run-026"></a>
## RUN-026 — Cost optimization removes unjustified complexity, not trust guarantees

The initial baseline intentionally avoids EKS, service mesh, active-active multi-Region compute, Aurora, read replicas, RDS Proxy, ElastiCache and blanket paid interface endpoints unless evidence justifies them.

Nonproduction may use reduced redundancy/capacity.

Production cross-AZ authority, required backups, encryption, security/audit logging and recovery evidence are not optional cost-cutting knobs.

AWS Budgets, cost-allocation tags, anomaly monitoring, bounded log retention and workload-aware scaling are expected operational controls.

# Selected topology

~~~text
Internet
  → CloudFront
      + WAF
      ├─ private S3 client assets
      └─ VPC origin
          → internal ALB
              → ECS/Fargate API tasks across >=2 AZs
                    ├─ RDS PostgreSQL Multi-AZ DB instance
                    ├─ private/versioned S3
                    ├─ SQS → ECS/Fargate worker
                    ├─ Cognito / approved external dependencies
                    └─ CloudWatch / OpenTelemetry telemetry

active Region:   us-east-2
recovery Region: us-east-1 cold restore/promotion
~~~

# Provider evidence verified for ADQ-009

Current provider documentation was rechecked on 2026-09-22.

It supports the following decision-relevant facts:

- CloudFront VPC origins can use private ALBs and are supported in us-east-2;
- ECS/Fargate supports ALB-backed services and cross-AZ service balancing/rebalancing;
- RDS PostgreSQL Multi-AZ DB instance uses a synchronous standby in another AZ;
- RDS cross-Region automated backup replication supports PostgreSQL DB instances from us-east-2 to us-east-1, while Multi-AZ DB clusters are excluded from that feature;
- S3 replication requires Versioning on source and destination;
- Cognito User Pools support local authentication plus OIDC/SAML/social federation;
- GitHub Actions OIDC can access AWS without long-lived cloud credentials;
- AWS WAF rate-based rules are approximate protection rather than exact request-limit semantics.

These are **EXTERNAL_VENDOR_FACT** evidence, not production proof.

# Existing-substrate evidence

The repository already contains:

- OpenTofu environment roots for nonproduction/us-east-2, production/us-east-2 and recovery/us-east-1;
- remote-state/bootstrap conventions;
- OpenTofu formatting/validation in CI;
- local PostgreSQL development substrate.

That evidence reduces migration cost but does not itself establish production sufficiency.

# Evidence posture

ADQ-009 uses:

- **DOCUMENTATION_REASONING** for semantic/runtime fit;
- **EXTERNAL_VENDOR_FACT** for current AWS capabilities;
- repository-static implementation evidence for existing substrate/reuse cost.

No production environment or restore exercise is claimed by this decision.

# Mandatory downstream evidence

Before production readiness, executable evidence must cover at least:

- ECS cross-AZ task behavior and deployment rollback;
- private-edge/origin reachability and direct-origin denial;
- RDS Multi-AZ failover behavior;
- application reconnect after database failover;
- Cognito-to-first-party-session flow and revocation;
- WAF/abuse handling without semantic authorization leakage;
- SQS retry/DLQ/idempotent worker behavior;
- backup/PITR restore;
- cross-Region database and critical-object recovery;
- cold recovery deployment/promotion;
- observability of semantic failure/unknown/retry states;
- secrets/role separation;
- cost baseline and anomaly controls.

# Revisit triggers

Reopen ADQ-009 when credible evidence shows:

- measured load makes ECS/Fargate or RDS Multi-AZ DB instance insufficient/disproportionate;
- recovery objectives require warmer or active regional topology;
- Cognito cannot satisfy authentication/federation requirements proportionately;
- object/recovery retention obligations require a different storage/backup design;
- runtime cost materially exceeds the accepted operating envelope;
- a service/runtime creates unacceptable lock-in or authority leakage;
- CloudFront VPC-origin restrictions conflict with required protocol/runtime behavior;
- 019-K exposes unresolved threat, failure, recovery, performance or cost contradictions.

Whole-architecture acceptance remains false until 019-L.

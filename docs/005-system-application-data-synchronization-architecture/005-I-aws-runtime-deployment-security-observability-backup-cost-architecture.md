---
type: Architecture Design Record
title: 005-I — AWS Runtime, Deployment, Security, Observability, Backup & Cost Architecture
description: Binds MUDAC's accepted application, data, identity, API, synchronization, artifact, and browser contracts to a concrete AWS production topology and operational model.
status: stable
tags: [phase-005, architecture, aws, runtime, deployment, security, observability, backup, cost]
sources:
  - resource: ../canonical/architecture/architectural-foundation.md
  - resource: ../canonical/architecture/application-boundaries.md
  - resource: ../canonical/architecture/data-persistence.md
  - resource: ../canonical/architecture/identity-access-session.md
  - resource: ../canonical/architecture/commands-api-concurrency.md
  - resource: ../canonical/architecture/synchronization-recovery.md
  - resource: ../canonical/architecture/external-representation.md
  - resource: ../canonical/architecture/frontend-interaction.md
  - resource: https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-vpc-origins.html
  - resource: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-load-balancing.html
  - resource: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZ.html
  - resource: https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools.html
  - resource: https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html
  - resource: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Application-Signals-Enable-ECSMain.html
generated: { by: openai/gpt-5.6-sol, at: 2026-09-04T05:28:35Z }
---

# Purpose

Translate the completed Phase 005 application architecture into a production AWS topology that is secure, observable, recoverable, cost-proportionate, and operationally realistic for a bounded live judging event.

005-I chooses concrete AWS service families where downstream requirements now make the choice material. It deliberately avoids adding distributed infrastructure merely because AWS offers it, and it does not allow cloud products to redefine MUDAC authority, identity, evidence, synchronization, or publication semantics.

# Decision summary

The production baseline is a **single active AWS Region (`us-east-2`) with Multi-AZ availability**, fronted by **Amazon CloudFront** as the only public application edge. CloudFront serves the React application from private S3 and reaches the application through a **CloudFront VPC origin backed by an internal Application Load Balancer**. The authoritative modular monolith runs as **Amazon ECS services on AWS Fargate**. The authority database is **Amazon RDS for PostgreSQL Multi-AZ**. Authentication uses an **Amazon Cognito User Pool** behind the MUDAC authentication adapter while MUDAC continues to own Identity/Participation/Access and opaque server sessions.

Private evidence and generated Artifacts live in **Amazon S3** behind relational metadata. Durable asynchronous jobs use **Amazon SQS** plus dead-letter queues, fed from the transactional-outbox boundary where appropriate. Application telemetry uses **CloudWatch plus AWS Distro for OpenTelemetry / CloudWatch Application Signals**. Production deployment is performed from **GitHub Actions through OIDC-federated IAM roles**, not long-lived AWS access keys.

The baseline is intentionally **not active-active multi-Region**. Regional disaster recovery uses replicated backups and cold restoration into `us-east-1`; during a whole-Region outage in live judging, MUDAC's established paper continuity contract is the authoritative event fallback.

# Production topology

```text
Internet
   |
Route 53 + ACM
   |
AWS WAF
   |
CloudFront
   |-------------------------------|
   |                               |
private S3 frontend origin         CloudFront VPC origin
(OAC, no public bucket access)          |
                                     internal ALB
                                         |
                            ECS/Fargate API service
                            across >= 2 AZs/tasks
                                  |          |
                                  |          +--> SQS async work
                                  |                  |
                                  |             ECS/Fargate worker
                                  |
                         RDS PostgreSQL Multi-AZ
                                  |
                       authoritative MUDAC state

private S3 evidence/artifact storage
   ^
   |
API / worker IAM task roles
```

CloudFront paths for dynamic API/authentication callbacks disable caching and forward only required cookies/headers. Static content-addressed frontend assets use long-lived cache policy while the application entry document/release manifest remains short-lived or explicitly invalidated during promotion.

# Region and availability posture

`us-east-2` is the active production Region. It supports the selected CloudFront VPC-origin, ECS/Fargate, RDS PostgreSQL, Cognito, S3, SQS, WAF, KMS, and CloudWatch capabilities and is a reasonable primary location for the current Midwest-centered event workload.

Production spans at least two Availability Zones:

- CloudFront VPC-origin connectivity terminates at an internal ALB;
- ECS API tasks run across at least two AZs;
- RDS uses a Multi-AZ DB instance deployment;
- private application subnets use AZ-local NAT Gateway egress;
- critical S3/RDS backups are copied/replicated outside the active Region.

An AZ loss is handled inside the active Region. A whole-Region loss is a different failure class and does not trigger automatic cross-Region writes or split authority.

# Edge, DNS, TLS and web protection

CloudFront is the only public application/data edge for normal users. The application ALB remains internal and is attached as a CloudFront VPC origin so API tasks are not internet-addressable.

The distribution uses:

- Route 53 for application DNS;
- ACM-managed TLS certificates;
- AWS WAF at CloudFront with AWS-managed baseline protections plus narrowly tuned rate-based rules;
- security response headers including HSTS, content-type protection, referrer policy, permissions policy, and a deliberately maintained Content Security Policy;
- private S3 origins through Origin Access Control (OAC), never S3 website endpoints/public-read buckets;
- caching disabled for authenticated API/auth flows and selectively enabled for immutable/static/public representation content.

WAF, CloudFront, and TLS are edge controls. They do not replace MUDAC Access checks, CSRF protection, command preconditions, disclosure logic, or server-side validation.

# ECS/Fargate runtime

The modular monolith is packaged as an immutable container image in Amazon ECR and deployed to ECS on Fargate.

The initial runtime has two process roles from the same release/image family where practical:

1. **API service** — synchronous HTTPS/JSON application, session/auth callback handling, authoritative command/query entry, and bounded in-process coordination.
2. **Worker service** — retryable asynchronous work such as Artifact generation, delivery preparation, and other explicitly queued tasks.

The authoritative domain remains one modular monolith even though API and worker processes are operationally separate. A worker invokes module/application contracts; it does not bypass repositories or become a second semantic owner.

Production API service posture:

- desired count at least two during normal production operation;
- tasks spread across at least two AZs;
- target-tracking autoscaling may use CPU, memory, and/or ALB request metrics;
- event-day pre-scaling is preferred over relying solely on reactive autoscaling;
- Fargate Spot is not used for the authoritative API path;
- Spot may later be considered for noncritical/retryable background work or nonproduction only.

The API and worker task roles are separate so background Artifact permissions do not automatically become API permissions.

# Relational authority database

Production uses **Amazon RDS for PostgreSQL, Multi-AZ DB instance deployment**.

005-I does not adopt Aurora as the baseline because MUDAC has not demonstrated a read-scale, failover, or throughput requirement that warrants a different database product and cost model. It also does not add RDS Proxy or read replicas initially because the expected Fargate task count and pooled application connections do not yet justify them.

The production database has:

- encryption at rest with KMS;
- TLS-required connections;
- automated backups and point-in-time recovery;
- storage autoscaling within explicit guardrails;
- PostgreSQL/RDS metrics and database logs exported into the operations view;
- a runtime application credential with only required DML/execute privileges;
- a distinct migration/DDL credential unavailable to normal application tasks.

Database class and storage size are deployment parameters selected by representative load tests rather than permanent architectural constants. They are sized ahead of event day rather than depending on risky mid-event resizing.

# Cognito and server-session boundary

Amazon Cognito User Pools is the initial authentication provider behind the `AUTH-014` adapter.

The browser does not treat Cognito tokens as MUDAC authorization state. Authentication follows an authorization-code/OIDC flow whose callback/token handling terminates at the MUDAC server/BFF boundary where practical. MUDAC then:

1. validates the external issuer/subject;
2. resolves the linked MUDAC Identity;
3. resolves current Participation/Access;
4. creates/updates the first-party opaque server session;
5. sends only the protected opaque session cookie to the browser.

Cognito managed login may be used initially and Cognito may later federate SAML/OIDC providers without changing MUDAC historical Identity or authorship.

Cognito's OAuth/managed-login domain endpoints remain public endpoints, so private ECS tasks require outbound internet egress for relevant server-side OAuth operations. Cognito PrivateLink is not treated as a replacement for this path because current Cognito PrivateLink support excludes user-pool domain/OAuth authorization-server workflows.

# Private networking and egress

Production VPC posture:

```text
CloudFront
   |
VPC-origin managed connection
   |
private ALB subnets
   |
private ECS application subnets
   |
private RDS subnets
```

No production ECS task receives a public IP address. RDS is not publicly accessible.

Because some runtime dependencies require public-domain egress, production uses one NAT Gateway per active AZ so loss of one AZ does not remove outbound connectivity from the surviving application tier. Nonproduction may use one NAT Gateway where reduced availability is accepted.

A free S3 gateway VPC endpoint is used so high-volume evidence/artifact S3 traffic does not consume NAT bandwidth. Paid interface VPC endpoints are added only when their security, traffic, or cost benefit is demonstrated; they are not created for every AWS service by default while NAT egress is already required.

Security groups form the primary network allow-list:

- CloudFront VPC-origin service-managed security group → internal ALB;
- ALB → ECS API tasks only;
- API/worker tasks → RDS PostgreSQL only as required;
- required egress only to AWS/external dependencies.

# S3 evidence, artifacts and frontend releases

Separate private buckets/prefix boundaries are used for materially different data classes rather than mixing deployable frontend files with private judging evidence.

Baseline storage classes:

- **frontend release bucket** — private S3 origin behind CloudFront OAC; content-addressed assets; no public-read ACL/policy;
- **private evidence/artifact bucket** — paper scans, generated Artifacts, print packages and similar retained bytes; S3 Versioning enabled; default SSE-KMS with S3 Bucket Keys for cost control; public access blocked;
- **security/audit log bucket** — CloudTrail and related durable audit records with stricter write/delete permissions.

Application-level Artifact identity remains the relational `REP-*` record. Object key/version/URL is a locator.

Artifact/evidence writes use unique immutable object keys and retain a cryptographic digest. Application runtime roles do not overwrite previously registered Artifact objects. S3 Object Lock is not mandatory yet because retention/deletion policy has not been finalized; it may be enabled for a dedicated future bucket when a concrete WORM retention requirement justifies the irreversible bucket-level commitment.

Protected downloads are authorized by MUDAC first, then receive a short-lived delivery capability such as a CloudFront signed URL/cookie. Public Publication may expose a stable application/public route that resolves an explicitly current Publication; neither route nor signed URL becomes publication authority.

# Asynchronous work and outbox delivery

SQS is the baseline durable asynchronous work queue.

The pattern is:

```text
authoritative transaction
   |
transactional outbox row
   |
outbox dispatcher
   |
SQS
   |
worker
   |
idempotent work result / Artifact / delivery record
```

Queues use server-side encryption, visibility timeout matched to work duration, bounded retries, and dead-letter queues. Queue message identity is delivery state, not domain authority. A duplicate SQS delivery must converge through the same idempotency/resource rules already established in `API-*`, `DATA-*`, and `REP-*`.

SQS is not introduced as an event-sourcing log, a replacement for PostgreSQL authority, or a general service bus between modules inside the modular monolith.

# IAM, KMS and secrets

IAM follows least privilege with distinct identities for:

- ECS task execution;
- API runtime;
- worker runtime;
- database migration task;
- deployment from GitHub Actions;
- backup/restore automation;
- observability/security services.

Runtime AWS credentials come from task roles, never application configuration files.

Secrets Manager stores database/application secrets that cannot be represented as nonsecret configuration. Database credentials support rotation; applications must tolerate connection renewal rather than pinning one credential forever. Nonsecret environment configuration may use versioned deployment configuration/Parameter Store as appropriate.

Customer-managed KMS keys are used for production authority database encryption and private evidence/artifact encryption where key policy/audit separation is material. Key deletion is strongly restricted and uses the longest practical safety window. Frontend public-release source objects do not require the same encryption classification as private evidence.

# Deployment and environment architecture

At minimum, production and nonproduction workloads live in separate AWS accounts. The AWS Organizations management account is not used as an application workload account. A dedicated security/log-archive account may be introduced as the organization matures without changing application architecture.

GitHub Actions deploys using OIDC federation to environment-specific IAM roles. No long-lived AWS access keys are stored as GitHub repository/environment secrets.

Trust is constrained to the expected repository and GitHub environment/ref. The production GitHub Environment requires protected deployment rules/manual approval appropriate to the project.

Persistent AWS infrastructure is managed as Infrastructure as Code. The specific IaC implementation (for example CDK/CloudFormation versus Terraform/OpenTofu) remains an implementation-tool decision; manual production console changes are emergency exceptions and must be reconciled back into IaC.

## Backend release

Backend deployment uses immutable ECR image references and ECS rolling deployment with the ECS deployment circuit breaker/automatic rollback enabled.

Database migration uses a dedicated one-off migration task/credential before or as an explicitly gated part of release. Schema evolution follows expand/contract compatibility because old and new application tasks can coexist during a rolling deployment. Destructive schema change is not coupled to the same instant as application rollout.

A production deployment is avoided during active judging except for a necessary incident fix. Event-day change freeze is an operational control, not merely team convention.

## Frontend release

The React build uses content-hashed assets uploaded before release activation. A release manifest/entry document is updated only after all referenced assets exist. CloudFront invalidation is limited to mutable entry/manifest paths rather than invalidating immutable hashed assets.

Frontend and API changes maintain a compatibility window sufficient for rolling backend deployment and cached browser clients. A frontend rollback restores the prior release entrypoint; it does not require rewriting authoritative application data.

# Web and infrastructure security posture

Production includes:

- CloudFront + ACM TLS;
- AWS WAF managed baseline rule groups plus rate-based protections tuned from observed traffic;
- Shield Standard protections inherent to CloudFront/Route 53;
- S3 Block Public Access and OAC;
- KMS encryption for production authority/private evidence stores;
- Secrets Manager and role-based temporary AWS credentials;
- private ALB/ECS/RDS networking;
- multi-Region CloudTrail management-event trail with log-file integrity validation;
- VPC Flow Logs retained to a cost-appropriate sink for incident analysis;
- explicit application security headers/CSP;
- dependency/container/image vulnerability scanning in CI/ECR where supported;
- routine review of IAM and externally reachable surfaces.

CloudTrail records AWS control-plane activity. MUDAC Provenance records domain authority and authorship. They are complementary and must not be substituted for one another.

# Observability architecture

The application emits structured JSON logs to CloudWatch Logs with correlation/request IDs, safe principal/Participation references where appropriate, command/result class, module, release ID, and relevant non-sensitive resource IDs. Raw Scorecard Notes, credentials, tokens, secrets, and unnecessary personal data are excluded from normal logs.

AWS Distro for OpenTelemetry and CloudWatch Application Signals are the baseline distributed telemetry path for ECS. Application telemetry must expose both infrastructure health and MUDAC-semantic health.

Minimum operational signals include:

- ALB/API request rate, latency and error classes;
- ECS task CPU/memory/restarts/deployment health;
- RDS availability, connections, storage, CPU, latency and slow/error queries;
- database pool saturation;
- session/authentication failure and Cognito dependency errors;
- authoritative command success/rejection/conflict/uncertain counts;
- idempotency replay/misuse counts;
- outbox age/backlog and dispatch failures;
- SQS queue age/depth/DLQ growth;
- projection freshness/rebuild failures;
- local-sync conflict/uncertain-result server-side indicators;
- Artifact generation/validation/publication failures;
- WAF blocks/rate-limit activity;
- backup/replication/restore-test health.

CloudWatch alarms notify operators for actionable failure conditions; dashboards support event-day operations. Alarm design avoids paging on every application-level validation rejection that is an expected user outcome.

Log retention is finite and class-specific. Operational application logs are not retained forever merely because CloudWatch can do so; security/audit logs have longer retention based on governance needs.

# Backup, restore and disaster recovery

## Database

Production RDS automated backups retain **35 days** of local point-in-time recovery history. Cross-Region automated backup replication sends PostgreSQL snapshots and transaction logs to `us-east-1` using a destination-region KMS key.

Manual/pre-change snapshots are taken before materially risky schema/data migrations where automated PITR alone would make operational rollback too uncertain.

A backup is not treated as trustworthy merely because AWS reports it exists. Restore testing is scheduled and records actual restore duration and validation results. AWS Backup restore-testing capability may be used for periodic automated exercises; application-level validation confirms that restored data is usable and internally coherent.

## S3

Critical evidence/artifact buckets use S3 Versioning. Cross-Region replication/copy is enabled for data whose loss would prevent reconstruction of retained evidence or published Artifacts. Lifecycle transitions may reduce storage cost after the active period, but deletion/expiration rules are not introduced until product retention policy explicitly permits them.

## Regional disaster

There is no automatically writable secondary MUDAC deployment.

For a whole-Region outage:

1. live event judging falls back to the canonical paper continuity process rather than creating cross-Region dual authority;
2. operators confirm the outage class and freeze conflicting recovery actions;
3. restore the authority database from replicated backup into the designated recovery Region;
4. restore/validate required configuration, secrets, buckets and runtime infrastructure from IaC/backups;
5. reconcile paper evidence and any known local/non-authoritative Draft traces under existing correction/recovery rules;
6. explicitly promote one recovered environment as current authority.

RTO/RPO are measured through restore exercises rather than invented as documentation numbers before implementation/load/recovery testing exists.

# Cost architecture

Cost optimization follows the workload rather than removing trust guarantees.

Accepted production fixed-cost items include:

- Multi-AZ RDS authority database;
- at least two API tasks during active production;
- one NAT Gateway per active AZ;
- CloudFront/WAF edge protection;
- backup replication and security logging.

Those are not removed merely to produce a lower spreadsheet estimate.

Cost is constrained elsewhere by:

- modular-monolith/Fargate rather than microservice fleets;
- RDS PostgreSQL rather than Aurora until a concrete driver exists;
- no baseline RDS Proxy/read replicas/ElastiCache/service mesh/API Gateway;
- no active-active secondary Region;
- no paid interface VPC endpoints by default while NAT remains required, except where measured security/traffic economics justify them;
- free S3 gateway endpoint for S3 traffic;
- nonproduction running fewer tasks and accepting Single-AZ database/NAT posture;
- event-aware pre-scaling followed by post-event scale-down;
- finite log retention and S3 lifecycle transitions where retention policy permits;
- Cost Allocation Tags, AWS Budgets and Cost Anomaly Detection;
- later Savings Plan/Reserved pricing only after stable utilization is demonstrated.

Production authority/fairness/recoverability controls are not optional cost knobs.

# Alternatives considered

## Lambda/API Gateway as primary API

Rejected as baseline. The modular monolith, server-managed sessions, relational transactions, predictable event-day workload, shared application runtime, and artifact/background roles fit a container service more naturally. Lambda remains available for narrow automation/validation tasks if a concrete use case warrants it.

## EKS/Kubernetes

Rejected. It introduces substantial operational control-plane and platform complexity without a workload/team requirement that justifies it.

## Aurora PostgreSQL

Deferred. RDS PostgreSQL Multi-AZ currently satisfies relational authority and availability requirements with a simpler cost/operations posture.

## Public ALB

Rejected as the normal application origin because current CloudFront VPC-origin support allows the ALB to remain in private subnets while CloudFront remains the public edge.

## Active-active multi-Region

Rejected. It would force difficult cross-Region transaction, session, synchronization, conflict, and authority questions that MUDAC does not need for its current risk profile. Paper continuity plus cold regional restore is safer and materially simpler.

## Redis/ElastiCache session store

Deferred. Server sessions can live in PostgreSQL initially at the expected scale. Add a dedicated ephemeral store only when session/cache workload demonstrates the need.

# Failure exercises required before 005-J exit

005-J should review at minimum:

1. one Fargate task dies during Scorecard Finalization;
2. one Availability Zone becomes unavailable;
3. RDS primary fails over during active judging;
4. Cognito is unavailable while existing sessions remain active;
5. NAT/egress in one AZ fails;
6. SQS delivers the same Artifact job twice;
7. an ECS deployment fails health checks and rolls back;
8. a migration completes but the new app release fails;
9. CloudFront serves an older frontend entrypoint against a newer API;
10. CloudWatch telemetry is partially unavailable while application authority remains healthy;
11. a private Artifact URL is leaked after user Access expires;
12. database data is accidentally corrupted and PITR is required;
13. the active Region is unavailable during judging;
14. backup restoration succeeds technically but application validation fails;
15. unexpected AWS cost growth occurs before or during event week.

# Closure decision

005-I establishes a concrete deployable AWS production topology without changing upstream MUDAC product semantics or introducing distributed authority. It is suitable for integrated architecture/threat/failure review in 005-J.

No new Concept, policy, invariant, or experience contract is required by this subgroup.
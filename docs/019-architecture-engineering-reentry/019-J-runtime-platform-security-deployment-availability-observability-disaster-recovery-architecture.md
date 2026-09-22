---
type: Architecture Decision
title: 019-J — Runtime Platform, Security, Deployment, Availability, Observability & Disaster-Recovery Architecture
description: "Resolves ADQ-009 by comparing unchanged historical AWS topology, a revised AWS managed-container/data-service topology, serverless-first AWS, Kubernetes/EKS, and simpler managed runtime alternatives; accepts the revised AWS topology with current provider evidence and explicit recovery/cost deferrals."
status: stable
tags: [phase-019, architecture, adq-009, aws, runtime, security, deployment, availability, observability, disaster-recovery, cost]
sources:
  - resource: ../canonical/architecture/runtime-platform-operations.md
  - resource: ../canonical/architecture/aws-runtime-operations.md
  - resource: ../canonical/architecture/architecture-drivers.md
  - resource: ../canonical/architecture/application-ownership-boundaries.md
  - resource: ../canonical/architecture/persistence-history-recovery.md
  - resource: ../canonical/architecture/identity-access-authority.md
  - resource: ../canonical/architecture/interface-command-concurrency.md
  - resource: ../canonical/architecture/offline-continuity-reconciliation.md
  - resource: ../canonical/architecture/artifact-export-publication-delivery.md
  - resource: ../canonical/architecture/browser-client-interaction.md
  - resource: ../canonical/governance/downstream-realization-obligations.md
  - resource: https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-vpc-origins.html
  - resource: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-load-balancing.html
  - resource: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZSingleStandby.html
  - resource: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReplicateBackups.html
  - resource: https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication-requirements.html
  - resource: https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-identity-provider.html
  - resource: https://docs.github.com/en/actions/how-tos/secure-your-work/security-harden-deployments/oidc-in-aws
  - resource: ../routing/phase019_architecture_decision_control.json
generated: { by: openai/gpt-5.6-sol, at: 2026-09-22T14:40:00-05:00 }
---

# Purpose

019-J resolves ADQ-009.

It decides the initial production runtime platform, compute/data realization, identity-provider realization, edge/network security, asynchronous runtime, deployment authority, observability, backup/restore, regional recovery and proportional-cost posture.

# Entry state

~~~text
Phase 019                       ACTIVE
019-A/B/C/D/E/F/G/H/I           COMPLETE
019-J                           NEXT ELIGIBLE / USER AUTHORIZED

ADQ-001..008                    ACCEPTED
ADQ-009                         PLANNED
ADQ-010                         PLANNED

Q4R-001..004                    COMPLETE
Q4 repairs complete             4 / 4
technical probes                0

accepted whole architecture     false
implementation packages         0
implementation execution        false
~~~

ADQ-009 has no blocking Q4 repair. The historical AWS candidate is qualified comparison evidence.

# Decision

**ADQ-009 — ACCEPTED.**

Selected architecture:

> **A revised AWS managed-container/data-service topology: single-active us-east-2 Multi-AZ production with cold us-east-1 recovery; CloudFront/WAF public edge and private origins; ECS/Fargate modular-monolith API plus bounded worker service; RDS PostgreSQL Multi-AZ DB instance; Cognito User Pools behind the application IAM adapter; private/versioned encrypted S3; SQS for semantically separable asynchronous work; private application/data networking with resilient managed egress; OIDC-federated deployments; CloudWatch/OpenTelemetry semantic observability; automated/PITR and cross-Region recovery evidence; and explicit avoidance of unjustified active-active/Kubernetes/cache/database complexity.**

Current owner:

> docs/canonical/architecture/runtime-platform-operations.md

Stable rules:

> RUN-001 through RUN-026

# Constraints preserved

ADQ-009 preserves ENG-011, ENG-013, ENG-015, ENG-016, ENG-017, INV-010, DRV-002/003/004/005/006/007/008/010/011/012, PST-001/011/015/016, IAM-001/006/016/017, CMD-004/011/014/019/022, RCV-009/010/017/018, ART-004/005/008/014/017/020 and CLT-001/017/018/020.

# Current provider-evidence qualification

Current AWS/GitHub documentation was checked on 2026-09-22.

Decision-relevant verified facts include:

- CloudFront VPC origins support private ALBs and are available in us-east-2;
- ECS/Fargate supports ALB-backed services and Availability-Zone balancing;
- an RDS Multi-AZ DB instance keeps a synchronous standby in another Availability Zone;
- RDS PostgreSQL cross-Region automated backup replication supports us-east-2 to us-east-1 for DB instances, while Multi-AZ DB clusters are excluded from that feature;
- S3 replication requires Versioning;
- Cognito User Pools support OIDC/SAML/social federation;
- GitHub Actions OIDC removes the need for long-lived AWS deployment credentials;
- AWS WAF rate-based rules are approximate infrastructure protection, not precise semantic request limits.

Evidence class: **EXTERNAL_VENDOR_FACT**.

These facts establish current capability fit only. They do not establish production performance, security effectiveness, recovery time or cost.

# Existing repository substrate

Repository-static evidence includes OpenTofu environment roots for nonproduction/us-east-2, production/us-east-2 and recovery/us-east-1; infrastructure-state/bootstrap conventions; OpenTofu format/validate CI; and PostgreSQL local development substrate.

This lowers adoption/migration cost. It does not prove any AWS environment is deployed or production-ready.

# Historical candidate treatment

Input:

> docs/canonical/architecture/aws-runtime-operations.md

The historical candidate remains strong evidence but is **not adopted unchanged**.

Retained hypotheses include single-active-Region Multi-AZ production, cold regional recovery, CloudFront/private-origin edge, ECS/Fargate API and bounded workers, RDS PostgreSQL Multi-AZ, Cognito behind MUDAC-owned Identity/Access/session semantics, private/versioned S3, SQS non-authoritative async work, least-privilege roles, reproducible immutable deployment, semantic observability, tested restore, and proportional cost.

Revisions:

- historical REP/SYNC/AUTH and related authority references are replaced by current ART/RCV/IAM/CMD/PST owners;
- fixed 35-day backup retention is not promoted into current architecture because exact recovery/retention objectives remain evidence-bounded;
- one-zonal-NAT-per-AZ is not frozen as the only egress topology because AWS now offers regional NAT gateways;
- CloudWatch Application Signals is not mandatory architecture; OpenTelemetry-compatible semantic instrumentation plus CloudWatch observability is the baseline;
- exact service sizes/autoscaling thresholds remain evidence-bounded.

# Alternatives

## Alternative A — Adopt the historical AWS candidate unchanged

Strong end-to-end reasoning and good scaffold fit, but it contains stale authority references, freezes provider details that now have alternatives, promotes an exact retention value without accepted recovery objectives, and over-specifies some tooling.

**Rejected as-is.**

## Alternative B — Revised AWS managed-container/data-service topology

CloudFront/WAF + private ALB, ECS/Fargate API and bounded workers, RDS PostgreSQL Multi-AZ DB instance, Cognito, S3, SQS, private networking, managed secrets/KMS, OIDC deployment and cold regional recovery.

Strengths:

- directly realizes accepted PostgreSQL/modular-monolith/request-response architecture;
- low infrastructure-host maintenance compared with EC2/EKS;
- preserves cross-AZ event continuity;
- supports bounded asynchronous work without microservice proliferation;
- reuses existing repository substrate;
- provider features support cold regional recovery;
- proportional to the current bounded live-event workload.

Weaknesses:

- material AWS lock-in;
- recurring managed-service/network cost;
- cold regional recovery cannot satisfy an aggressive RTO without later architecture change;
- provider-specific operational competence remains required.

**Selected.**

## Alternative C — AWS serverless-first API and workers

Potentially strong burst scaling and scale-down economics, but current authoritative workload already fits a long-running modular monolith. Relational sessions/transactions gain runtime/connection complexity, decomposition pressure increases, and cold/latency behavior would need proof.

**Rejected as baseline.**

Selective serverless technical functions remain possible where isolated and justified.

## Alternative D — Kubernetes/EKS platform

Flexible and portable, but cluster/platform operations are disproportionate to current workload/team evidence. No accepted scale or isolation requirement needs Kubernetes.

**Rejected.**

## Alternative E — Simpler single-instance/PaaS-style runtime

Lower operational complexity and possibly lower baseline cost, but weaker cross-AZ event continuity and less controlled private-network/recovery posture make it unsuitable for the production baseline.

**Rejected for production.**

Reduced nonproduction topology remains permitted.

# Region and availability posture

~~~text
active production       us-east-2
application runtime     >= 2 AZ
authority database      Multi-AZ
recovery Region         us-east-1
recovery mode           cold restore + explicit promotion
active-active           no
~~~

This is an availability topology, not an uptime guarantee.

# Compute posture

ECS/Fargate is selected because the accepted architecture is a modular monolith with a bounded worker need, not a service mesh.

Production API capacity remains present across zones rather than depending entirely on scale-from-zero.

# Database posture

RDS PostgreSQL Multi-AZ DB instance is selected over Single-AZ, Multi-AZ DB cluster, Aurora and self-managed PostgreSQL.

The selected topology balances cross-AZ failover, PostgreSQL compatibility, cross-Region automated-backup capability, current workload proportionality and operational simplicity.

# Identity-provider posture

Cognito User Pools is selected as the initial managed IdP because current AWS capability satisfies the IAM adapter boundary and supports later OIDC/SAML/social federation.

Cognito claims/groups never become MUDAC Competition roles or Access authority.

# Networking/security posture

~~~text
CloudFront/WAF
  → private origins
  → internal ALB
  → private ECS tasks
  → private RDS
~~~

Approved public dependencies use resilient managed egress. S3 traffic uses the gateway endpoint baseline.

WAF protects availability and reduces abuse but does not replace application Access, idempotency or semantic command validation.

# Deployment posture

Production/nonproduction authority is separated.

GitHub Actions uses OIDC-federated AWS roles rather than long-lived access keys.

Infrastructure is code-managed, container releases are immutable, and schema migration has dedicated authority plus compatibility discipline.

# Observability posture

Required operational meaning includes release identity, command outcome/unknown rates, idempotency/retry anomalies, queue/outbox/projection lag, database health/failover, authentication dependency health, Artifact/Publication failures, backup/replication health and recovery/reconciliation pressure.

Sensitive participant/evaluation content is minimized in logs and traces.

# Backup and disaster recovery

Production requires PITR-capable database backups and cross-Region recovery material.

Critical S3 evidence/artifact recovery uses Versioning plus selective cross-Region replication/copy.

Recovery remains single-authority:

~~~text
regional outage
  → digital authority unavailable
  → paper/local bounded continuity where legitimate
  → restore database + critical objects + runtime
  → validate application authority/history
  → explicitly promote one recovery environment
  → reconcile retained traces
~~~

No RTO/RPO number is claimed until measured.

# Recovery-objective qualification

Before Phase-019 whole-architecture sufficiency is accepted, the program must establish explicit measurable availability/recovery validation targets or identify the absence of a business/contractual target as a bounded residual limitation with a concrete test target.

Cold recovery is accepted as the baseline because current evidence does not justify active-active or warm-standby cost/complexity.

# Cost posture

Absent evidence, the selected baseline avoids EKS, service mesh, Aurora, RDS Proxy, read replicas, ElastiCache, active-active multi-Region compute, blanket interface endpoints and independent microservice deployment units.

Cost optimization cannot remove required production redundancy, security/audit controls, backups or recovery validation.

# Evidence classes

ADQ-009 acceptance uses:

- **DOCUMENTATION_REASONING**
- **EXTERNAL_VENDOR_FACT**
- repository-static substrate evidence

It does not claim bounded technical probe, executable AWS integration or production evidence.

# Residual uncertainty

Open questions include exact production task/CPU/memory sizes, autoscaling thresholds, NAT availability mode, RDS class/storage/IOPS, backup retention, RTO/RPO, S3 recovery scope, Cognito configuration/UX, WAF rules, secrets rotation, CloudWatch retention/alarms, alerting process, cost thresholds and whether any isolated async function should use Lambda.

# Risk disposition

**ERI-02 — controlled.** Current authority is RUN; historical AWS remains evidence.

**ERI-07 — reduced but not closed for production.** Current provider capabilities were externally revalidated; production behavior still requires executable evidence.

**ERI-08 — controlled.** Vendor/static evidence is explicitly separated from runtime/production claims.

**ERI-09 — materially reduced / carried to 019-K.** Runtime services, queues, IdP claims and delivery mechanisms remain non-authoritative.

**ERI-10 — still blocked.** ADQ-009 creates no implementation-package or execution authority.

# Implementation boundary

~~~text
accepted bounded decisions       9 / 10
Q4 repairs complete              4 / 4
technical probes                 0
accepted whole architecture      false
implementation packages          0
package derivation               false
implementation execution         false
~~~

G0 remains unsatisfied.

# Exit decision

**019-J — COMPLETE — PASS.**

**ADQ-009 — ACCEPTED.**

Next eligible:

> **019-K — Whole-Architecture Integration, Threat, Failure, Recovery, Performance, Cost & Scenario Validation**

019-K is not automatically authorized.

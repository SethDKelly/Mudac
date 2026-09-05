---
type: Implementation Contract
title: Runtime, Environment & Delivery Bootstrap
description: Defines the executable MUDAC workspace/runtime bootstrap, local/CI/nonproduction/production/recovery environment classes, implementation verification gate, OpenTofu root/state separation, supply-chain posture, and deployment-authority boundary.
status: stable
tags: [implementation, runtime, environment, local-development, ci-cd, iac, delivery]
sources:
  - resource: ../../006-implementation-planning/006-D-environment-iac-ci-cd-local-development-runtime-bootstrap.md
  - resource: implementation-foundation.md
  - resource: verification-strategy.md
  - resource: source-topology.md
  - resource: ../architecture/aws-runtime-operations.md
  - resource: ../architecture/application-boundaries.md
  - resource: ../architecture/frontend-interaction.md
generated: { by: openai/gpt-5.6-sol, at: 2026-09-05T00:09:00Z }
---

# Purpose

Define the current executable environment/runtime/delivery substrate for MUDAC. This owner realizes accepted architecture and implementation contracts; it does not create product/domain authority or claim that production infrastructure has already been provisioned.

This owner intentionally introduces no new stable-rule namespace. Runtime/bootstrap configuration should cite the upstream `AWS-*`, `IMPL-*`, `MOD-*`, `FE-*`, and other rules it implements rather than creating a parallel deployment-rule universe.

## The repository has one pinned executable workspace

The root pnpm workspace pins the accepted Node/TypeScript/tool families and commits the generated `pnpm-lock.yaml`. Frozen installs are the reproducibility baseline.

pnpm dependency build scripts remain deny-by-default under its safer-build behavior; required build packages are explicitly approved rather than globally disabling the control.

## Deployable roots remain minimal composition hosts

`apps/api`, `apps/worker`, and `apps/web` are executable composition roots under the 006-C source topology.

The API bootstrap proves Fastify process/health startup only; the worker proves lifecycle startup only; the browser proves React/Router/Query composition only. A bootstrap shell does not claim later persistence, security, API-domain, or feature behavior exists.

## Local development minimizes cloud dependency

Routine local development runs Node application processes on the host and PostgreSQL through Docker Compose.

External provider behavior such as Cognito, S3, SQS, email, scanners, and rendering is introduced behind application-owned ports. Deterministic local fakes support normal development/testing; targeted real-service smoke/integration evidence uses nonproduction when provider semantics matter.

Normal local development does not require long-lived AWS credentials.

## Environment authority remains explicit

MUDAC distinguishes:

- `local` — developer host + local PostgreSQL + deterministic provider fakes;
- `CI` — ephemeral verification runners with no ordinary production authority;
- `nonproduction` — separate AWS account in `us-east-2`, synthetic/test data and reduced redundancy where allowed;
- `production` — separate AWS account in `us-east-2`, governed by the accepted Multi-AZ `AWS-*` topology;
- `recovery` — cold-recovery root in `us-east-1`, never an independently writable active MUDAC authority.

Environment naming, config, state, and deployment roles must not collapse these classes.

## OpenTofu uses separate environment roots and separate state authority

Infrastructure roots live under:

```text
infra/environments/
  nonproduction/us-east-2/
  production/us-east-2/
  recovery/us-east-1/
```

OpenTofu workspaces are not used as a substitute for account/environment authority separation.

Each environment uses its own remote state identity. The accepted backend is encrypted/versioned private S3 with least-privilege access and S3-native locking (`use_lockfile = true`). Account-specific backend coordinates are supplied as partial configuration rather than committed credentials.

State-storage bootstrap remains administratively separate because an environment backend cannot safely create itself.

## Infrastructure modules do not mirror semantic application modules

OpenTofu modules may group concrete infrastructure capabilities such as networking, edge, compute, data, identity, messaging, storage, observability, and backup/recovery.

These groupings are implementation conveniences under `AWS-*`; they do not create or replace MUDAC semantic module ownership.

## Implementation Verification is the stable application/IaC check surface

The GitHub Actions workflow named **Implementation Verification** is the stable merge-gate identity for executable implementation checks.

Its current bootstrap checks include frozen install, formatting, TypeScript, ESLint, dependency-cruiser, Vitest, builds, Docker Compose configuration, and OpenTofu formatting/backend-disabled validation.

Later groups extend the evidence behind this stable surface where appropriate. Knowledge Validation remains separate and retains its `VAL-*` meaning.

## Supply-chain controls remain explicit and reviewable

The bootstrap uses a committed lockfile, explicit pnpm dependency-build approval, Dependabot for npm/GitHub Actions, CodeQL JavaScript/TypeScript analysis, and ignored secret/state/build-output paths.

Scanner or dependency success is evidence about the tested revision, not application authority/security certification.

## Repository checks and production deployment remain different authority boundaries

Ordinary implementation merge policy is intended to require pull requests plus current Knowledge Validation and Implementation Verification checks on `main` in accordance with `IMPL-013`.

Production deployment remains separately authorized through a protected GitHub environment and OIDC-federated AWS role under `IMPL-014`/`AWS-011`. A merge does not implicitly deploy production.

The current GitHub integration cannot administer repository rulesets/branch protection or GitHub environments. Those settings therefore remain a visible repository-admin gate until independently configured and verified; documentation must not claim enforcement merely because workflows exist.

## Runtime secrets are injected, not committed

`.env.example` documents nonsecret local configuration only. Real local secret files are ignored. AWS runtime secrets/configuration are supplied through environment/runtime mechanisms and Secrets Manager as appropriate to later feature implementation.

Long-lived AWS deployment keys do not belong in GitHub or repository configuration; deployment authority uses OIDC.

## Release identity is immutable and rollback-aware

Backend/frontend deployment workflows introduced as real AWS resources appear must bind releases to exact repository/build identity.

Backend rollout uses immutable image identity; frontend rollout uses content-addressed immutable assets plus a mutable release entrypoint/manifest. Rollback selects a prior immutable release rather than rewriting authoritative data.

Database migration is a separately privileged deployment step once 006-E supplies migrations, and application rollback must not assume destructive schema rollback.

## Infrastructure validation precedes apply but does not imply deployment

CI may format/validate OpenTofu without backend credentials. Real plan/apply occurs only under the intended environment/account deployment authority and exact reviewed revision.

A syntactically valid IaC root does not prove the AWS resources exist, are secure, can recover, or satisfy production SLOs.

# Current executable topology

```text
GitHub repository
  ├── pnpm workspace
  │    ├── apps/api        Fastify bootstrap
  │    ├── apps/worker     worker bootstrap
  │    ├── apps/web        React/Router/Query bootstrap
  │    └── packages/*      accepted module/application/projection/foundation seams
  ├── Docker Compose
  │    └── PostgreSQL local dependency
  ├── GitHub Actions
  │    ├── Knowledge Validation
  │    ├── Implementation Verification
  │    └── CodeQL
  └── infra/
       ├── bootstrap/state
       ├── modules
       └── environments
            ├── nonproduction/us-east-2
            ├── production/us-east-2
            └── recovery/us-east-1
```

# Deliberate limitations

This bootstrap does not yet implement PostgreSQL schemas/migrations, Cognito/session/Access, API command semantics, IndexedDB Drafts, domain workflows, actual AWS resources, OIDC IAM roles, production environment protection, deploy workflows, observability dashboards, load tests, or recovery exercises.

Those remain downstream work rather than hidden bootstrap behavior.

# Handoff

006-E owns the next substrate: PostgreSQL schema conventions, Kysely database typing/adapters, migrations, transaction primitives, Version/Provenance support, idempotency/outbox foundation, projections and real PostgreSQL migration/concurrency evidence.

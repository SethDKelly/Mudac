---
type: Implementation Planning Record
title: 006-D — Environment, IaC, CI/CD, Local Development & Runtime Bootstrap
description: Instantiates the Phase 006 workspace, local-development runtime, implementation CI, dependency enforcement, initial OpenTofu environment/state layout, release/deployment authority boundaries, and repository-administration residuals without implementing later domain foundations.
status: stable
tags: [phase-006, implementation, environment, iac, ci-cd, local-development, runtime, bootstrap]
sources:
  - resource: ../canonical/implementation/implementation-foundation.md
  - resource: ../canonical/implementation/verification-strategy.md
  - resource: ../canonical/implementation/source-topology.md
  - resource: ../canonical/architecture/aws-runtime-operations.md
  - resource: ../canonical/architecture/application-boundaries.md
  - resource: ../canonical/architecture/frontend-interaction.md
  - resource: https://opentofu.org/docs/language/settings/backends/s3/
  - resource: https://docs.github.com/en/actions/how-tos/secure-your-work/security-harden-deployments/oidc-in-aws
generated: { by: openai/gpt-5.6-sol, at: 2026-09-05T00:29:00Z }
---

# Purpose

Turn the accepted Phase 006 implementation/tooling/source contracts into an executable repository and environment skeleton before persistence, Identity/Access, API execution, or business-domain feature work begins.

006-D is bootstrap, not feature delivery. It may create buildable application composition roots, CI/IaC boundaries, and development/runtime infrastructure, but it must not invent Competition, Participation, Scorecard, outcome, or publication semantics that belong to later groups.

# Exit question

> Can a contributor now clone MUDAC, install one pinned workspace, start the local development dependency, build the three application composition roots, run deterministic implementation checks, preserve the 006-C dependency graph, and see a truthful path from repository revision to separate nonproduction/production/recovery infrastructure roots without pretending AWS or production readiness already exists?

**Decision: Yes, subject to one external repository-administration residual described below.**

# Executable workspace bootstrap

006-D creates the pnpm monorepo defined by 006-C:

```text
apps/
  api/
  worker/
  web/
packages/
  modules/
    competition/
    identity-access/
    judging-operations/
    evaluation/
    outcomes/
    external-representation/
  application/
  projections/
  foundation/
  test-support/
infra/
tests/
```

`@mudac/api-client` remains absent until 006-G establishes the generated transport/client boundary.

All current application packages remain private workspace packages. The six authoritative module packages contain only public boundary placeholders at this stage; creating a workspace package does not claim that its later domain implementation already exists.

# Pinned implementation toolchain

The executable manifests pin the current accepted families rather than using floating `latest` ranges:

- Node.js 24 runtime family through `.node-version` and package engines;
- pnpm 11.25.0 and a committed generated lockfile;
- TypeScript 6.0.3;
- Fastify 5.12.1;
- React/React DOM 19.2.8;
- React Router 8.3.1;
- TanStack Query 5.102.8;
- Vite 8.2.2;
- Vitest 4.1.11;
- Playwright 1.62.1;
- ESLint 10.8.1 plus TypeScript-aware rules;
- Prettier 3.9.6;
- dependency-cruiser 18.2.0;
- OpenTofu 1.12.0 in CI.

The pins are reproducibility inputs, not permanent product semantics. Future upgrades remain governed by `IMPL-010`.

pnpm 11's safer-build behavior is kept enabled. The workspace explicitly allows the required `esbuild` install script instead of disabling the supply-chain check globally.

# Minimal composition roots

## API

`apps/api` boots Fastify and exposes only `/healthz`.

This route demonstrates transport/runtime startup. It does not imply that later API, authentication, persistence, readiness, or domain endpoints exist.

## Worker

`apps/worker` establishes process lifecycle/signal handling only. It consumes no authoritative queue or domain work yet.

## Browser

`apps/web` establishes the React, React Router Data-capable, and TanStack Query composition shell with a deliberately content-light bootstrap page.

No protected route, session, local Draft, Scorecard, or Organizer/Judge feature behavior is claimed before 006-F through 006-J.

# Local development topology

The default local topology is deliberately simple:

```text
host machine
  ├── pnpm / Node
  ├── apps/api
  ├── apps/worker
  └── apps/web
       │
       └── Docker Compose PostgreSQL
```

Routine local development does not require long-lived AWS credentials.

Cognito, S3, SQS, email/invitation delivery, artifact rendering, and similar external dependencies use deterministic application-owned fakes/adapters as their later feature groups introduce them. Vendor semantics that matter are verified through targeted nonproduction integration rather than making a broad local cloud emulator a correctness dependency.

`.env.example` contains development-only examples; actual `.env*` secret files are ignored.

The local PostgreSQL Compose service is a bootstrap development dependency, not the final 006-E schema or production database-version contract.

# Implementation verification

006-D creates the stable GitHub Actions workflow named **Implementation Verification**.

The current aggregate executes:

```text
frozen pnpm install
      ↓
format check
      ↓
TypeScript strict type check
      ↓
ESLint
      ↓
dependency-cruiser source-graph check
      ↓
Vitest
      ↓
API / worker / web builds
      ↓
Docker Compose configuration check
      ↓
OpenTofu format + backend-disabled root validation
```

Deeper database, browser E2E, accessibility, security, concurrency, migration and operational evidence is added by later groups to the verification strategy rather than pretending empty suites prove those behaviors today.

Knowledge Validation remains separate under `VAL-*`.

## Bootstrap gate exercise

The new executable gate was run repeatedly while 006-D was being built rather than treated as decorative configuration. It exposed and forced correction of bootstrap incompatibilities including:

- pnpm 11 rejecting an unapproved `esbuild` install script until the required build was explicitly allowlisted;
- an early Node 24 type-definition pin that conflicted with the TypeScript 6 configuration;
- use of a removed Vitest workspace helper instead of the current root-project configuration;
- formatter scope that initially reached non-implementation files with different ownership/parser assumptions;
- ESLint invocation/configuration issues around empty test paths and type-aware project discovery.

The corrections preserve the intended controls: frozen installation, safer dependency builds, strict TypeScript, typed ESLint rules, package-boundary checks, and current Vitest behavior remain enabled rather than being suppressed to obtain a green build.

The final exact revision still must pass both Knowledge Validation and Implementation Verification before promotion; this record does not treat a successful earlier/intermediate revision as evidence for a later commit.

# Source dependency enforcement

The executable dependency-cruiser configuration blocks at least:

- production circular dependencies;
- packages depending on deployable apps;
- authoritative modules depending on coordination/projections;
- module dependency reversal across the accepted authority ordering;
- `foundation` acquiring business/server ownership;
- browser imports of server-only implementation;
- production imports of `test-support`.

Restrictive package exports and ESLint import restrictions reinforce the same boundary. Later code must extend the configuration when new package surfaces appear rather than bypassing it through path aliases or deep imports.

# Security and supply-chain bootstrap

006-D adds:

- frozen lockfile installation;
- pnpm explicit build-script approval;
- weekly Dependabot checks for npm and GitHub Actions;
- CodeQL JavaScript/TypeScript analysis on pull requests/main plus schedule;
- ignored local secrets/state/output files;
- read-only permission for ordinary implementation verification.

This is baseline supply-chain/static evidence. It does not substitute for behavioral Access/session/disclosure/security verification in later groups.

# Environment classes

## Local

Host-run Node applications plus Docker PostgreSQL and deterministic provider fakes. No normal AWS deployment authority.

## CI

GitHub-hosted runners use pinned manifests/lockfile and deterministic checks. Real PostgreSQL/Testcontainers is introduced when 006-E tests require PostgreSQL semantics. Ordinary implementation verification receives no production AWS credentials.

## Nonproduction

A separate AWS account, active in `us-east-2`, may use reduced redundancy while exercising real Cognito/S3/SQS/AWS-provider semantics with synthetic data.

## Production

A separate production AWS account in `us-east-2` implements the Multi-AZ `AWS-*` topology. Merge to `main` is not production-deployment authority.

## Recovery

A separate OpenTofu root targets `us-east-1` as the cold-recovery Region. It never represents an independently writable active production authority.

# OpenTofu topology

006-D establishes separate root/state identities:

```text
infra/
  bootstrap/state/
  modules/
  environments/
    nonproduction/us-east-2/
    production/us-east-2/
    recovery/us-east-1/
```

MUDAC does not use OpenTofu workspaces to blur these authority boundaries.

Each environment root declares an S3 backend and ships only an example partial backend configuration. Account-specific bucket names and credentials are not committed.

The intended state backend uses:

- private S3;
- Versioning;
- encryption/KMS appropriate to administrative state;
- least-privilege access;
- S3-native state locking with `use_lockfile = true`.

The state-storage bootstrap remains outside the environment roots because a backend cannot safely create itself. Concrete account IDs/bucket names are not fabricated before account bootstrap exists.

# AWS infrastructure sequencing

The accepted implementation order for real resources is:

1. state/administrative bootstrap;
2. GitHub OIDC and environment-specific deployment authority;
3. networking/private subnet/NAT/S3 gateway endpoint;
4. KMS/private buckets/ECR/logging foundations;
5. Cognito and SQS/DLQ boundaries;
6. RDS authority substrate;
7. ECS/Fargate and internal ALB;
8. CloudFront/OAC/VPC origin/WAF/ACM/DNS;
9. observability and backup/recovery controls;
10. deployment smoke/rollback evidence.

This sequencing is infrastructure dependency order only. It does not change the semantic module graph.

# Deployment authority and release posture

The intended delivery chain remains:

```text
pull request
  ├── Knowledge Validation
  └── Implementation Verification
          ↓
        main
          ↓
nonproduction deployment authority
          ↓
production protected environment + approval
          ↓
OIDC-federated production role
```

No long-lived AWS deploy key belongs in GitHub.

Later executable deployment workflows must bind each release to the exact Git commit/build identity and use immutable ECR image references plus content-addressed frontend assets. Database migration runs as a separately privileged step before compatible application rollout once 006-E supplies migrations.

Application rollback selects a prior immutable build; it does not assume database migrations can be blindly reversed. Expand/contract compatibility remains mandatory.

# Repository-administration residual

The intended `main` policy from `IMPL-013` requires pull requests and current Knowledge Validation + Implementation Verification checks before ordinary implementation merges, with force-push/deletion protection. Production additionally requires a protected GitHub environment.

The current connected GitHub capability can read repository rulesets but cannot create/update rulesets, branch protection, or environments. The repository currently exposes no repository rulesets through the available ruleset read. The branch-protection read itself is not accessible to this integration, so 006-D does not overclaim the exact effective protection state.

Therefore:

- workflow checks are now executable;
- intended protection settings are documented;
- actual GitHub repository/environment administration remains an **external repository-admin action required before CI is relied upon as an enforced merge/deploy control**.

This residual does not change system architecture, but it remains a delivery-governance gate and must stay visible until independently configured and verified.

# Production-readiness boundary

006-D does **not** claim:

- AWS accounts/resources are provisioned;
- Cognito/RDS/SQS/S3 application integration exists;
- production branch/environment controls are active;
- production load/SLO/security/accessibility evidence exists;
- restore/DR or paper-fallback exercises have passed;
- later domain foundations are implemented.

Those claims remain owned by later 006 groups and the integrated 006-M exit.

# Exit decision

006-D passes when the final branch has both Knowledge Validation and Implementation Verification green, current implementation routing identifies this bootstrap as accepted, the temporary lockfile-generation mechanism is absent, and the external repository-admin residual is explicitly retained rather than misrepresented as complete.

# Handoff

Proceed to **006-E — Persistence, Schema, Migration, Provenance, Outbox & Projection Foundation**.

006-E may now assume an executable pnpm/TypeScript workspace, real local PostgreSQL entry point, module package boundaries, deterministic verification gate, and separate infrastructure environment roots. It should add PostgreSQL/Kysely/migration behavior inside those boundaries without reopening repository topology or deployment authority.

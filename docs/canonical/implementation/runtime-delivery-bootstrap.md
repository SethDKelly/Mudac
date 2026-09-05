---
type: Implementation Contract
title: Runtime, Environment & Delivery Bootstrap
description: Defines the retained executable MUDAC workspace/runtime bootstrap, environment classes, verification gate, OpenTofu root/state separation, supply-chain posture, deployment-authority boundary, and current frozen-prototype status.
status: stable
tags: [implementation, runtime, environment, local-development, ci-cd, iac, delivery, frozen]
sources:
  - resource: ../../006-implementation-planning/006-D-environment-iac-ci-cd-local-development-runtime-bootstrap.md
  - resource: ../governance/design-implementation-boundary.md
  - resource: implementation-foundation.md
  - resource: verification-strategy.md
  - resource: source-topology.md
  - resource: ../architecture/aws-runtime-operations.md
  - resource: ../architecture/application-boundaries.md
  - resource: ../architecture/frontend-interaction.md
generated: { by: openai/gpt-5.6-sol, at: 2026-09-05T01:23:00Z }
---

# Purpose

Define the retained executable environment/runtime/delivery substrate established by 006-D. This owner realizes accepted architecture and implementation contracts; it does not create product/domain authority or claim that production infrastructure has been provisioned.

The current [Design / Implementation Boundary](../governance/design-implementation-boundary.md) freezes advancement beyond this bootstrap while MUDAC returns to deliberate design refinement.

This owner intentionally introduces no new stable-rule namespace. Runtime/bootstrap configuration cites the upstream `AWS-*`, `IMPL-*`, `MOD-*`, `FE-*`, and other rules it implements rather than creating a parallel deployment-rule universe.

# Current status — frozen non-domain prototype

The repository may retain and narrowly maintain the 006-D substrate, but must not use it to advance deferred domain implementation until an explicit later design-methodology exit authorizes resume.

Permitted retained substrate includes:

- pinned pnpm/Node/TypeScript manifests and lockfile;
- minimal `apps/api`, `apps/worker`, and `apps/web` composition roots;
- package/module seams without MUDAC domain behavior;
- Docker Compose PostgreSQL as a local service without authoritative MUDAC schema;
- Implementation Verification, CodeQL, Dependabot and dependency-boundary checks;
- OpenTofu environment/state-root scaffolding without application production provisioning.

Narrow security/compatibility maintenance is allowed when needed to keep this prototype safe/buildable and when it does not encode deferred domain semantics.

# Executable workspace

The root pnpm workspace pins the accepted Node/TypeScript/tool families and commits the generated `pnpm-lock.yaml`. Frozen installs are the reproducibility baseline.

pnpm dependency build scripts remain deny-by-default under its safer-build behavior; required build packages are explicitly approved rather than globally disabling the control.

`apps/api`, `apps/worker`, and `apps/web` are executable composition roots under the accepted source topology. The API proves Fastify process/health startup only; the worker proves lifecycle startup only; the browser proves React/Router/Query composition only.

A bootstrap shell does not claim persistence, security, API-domain, local-Draft, or feature behavior exists.

# Local development

Routine local development runs Node application processes on the host and PostgreSQL through Docker Compose.

External provider behavior such as Cognito, S3, SQS, email, scanners, and rendering remains behind application-owned ports when later authorized. Deterministic local fakes support normal development/testing; targeted real-service smoke/integration evidence uses nonproduction when provider semantics matter.

Normal local development does not require long-lived AWS credentials.

# Environment authority

MUDAC distinguishes:

- `local` — developer host + local PostgreSQL + deterministic provider fakes;
- `CI` — ephemeral verification runners with no ordinary production authority;
- `nonproduction` — separate AWS account in `us-east-2`, synthetic/test data and reduced redundancy where allowed;
- `production` — separate AWS account in `us-east-2`, governed by the accepted Multi-AZ `AWS-*` topology;
- `recovery` — cold-recovery root in `us-east-1`, never an independently writable active MUDAC authority.

Environment naming, config, state, and deployment roles must not collapse these classes.

# OpenTofu topology

Infrastructure roots remain:

```text
infra/environments/
  nonproduction/us-east-2/
  production/us-east-2/
  recovery/us-east-1/
```

OpenTofu workspaces are not used as a substitute for account/environment authority separation.

Each environment uses its own remote state identity. The accepted backend is encrypted/versioned private S3 with least-privilege access and S3-native locking (`use_lockfile = true`). Account-specific backend coordinates are supplied as partial configuration rather than committed credentials.

State-storage bootstrap remains administratively separate because an environment backend cannot safely create itself.

OpenTofu modules may group concrete infrastructure capabilities such as networking, edge, compute, data, identity, messaging, storage, observability, and backup/recovery. Those groupings are implementation conveniences under `AWS-*`; they do not create or replace MUDAC semantic module ownership.

# Verification and supply-chain posture

The GitHub Actions workflow named **Implementation Verification** remains the stable executable check surface for the retained bootstrap.

Its current checks include frozen install, formatting, TypeScript, ESLint, dependency-cruiser, Vitest, builds, Docker Compose configuration, and OpenTofu formatting/backend-disabled validation.

Knowledge Validation remains separate and retains its `VAL-*` meaning.

The bootstrap also retains a committed lockfile, explicit pnpm dependency-build approval, Dependabot for npm/GitHub Actions, CodeQL JavaScript/TypeScript analysis, and ignored secret/state/build-output paths.

Scanner or CI success is evidence about the tested revision, not application authority, design-methodology closure, implementation-resume authority, or production certification.

# Repository and deployment authority

Ordinary implementation merge policy is intended to require pull requests plus current Knowledge Validation and Implementation Verification checks on `main` in accordance with `IMPL-013`.

Production deployment remains separately authorized through a protected GitHub environment and OIDC-federated AWS role under `IMPL-014`/`AWS-011`. A merge does not implicitly deploy production.

The current GitHub integration cannot administer repository rulesets/branch protection or GitHub environments. Those settings remain a visible repository-admin gate until independently configured and verified; documentation must not claim enforcement merely because workflows exist.

Real local secret files are ignored. AWS runtime secrets/configuration use environment/runtime mechanisms and Secrets Manager when future implementation is authorized. Long-lived AWS deployment keys do not belong in GitHub or repository configuration.

# Release posture retained for future implementation

When implementation eventually resumes, backend/frontend deployment workflows must bind releases to exact repository/build identity. Backend rollout uses immutable image identity; frontend rollout uses content-addressed immutable assets plus a mutable release entrypoint/manifest.

Database migration remains a separately privileged deployment step once schema work is re-authorized, and application rollback must not assume destructive schema rollback.

CI may format/validate OpenTofu without backend credentials. Real plan/apply occurs only under intended environment/account deployment authority and an exact reviewed revision.

A syntactically valid IaC root does not prove AWS resources exist, are secure, can recover, or satisfy production SLOs.

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

This frozen bootstrap does not implement PostgreSQL domain schemas/migrations, Cognito/session/Access, API command semantics, IndexedDB Drafts, domain workflows, actual AWS application resources, OIDC IAM roles, production environment protection, deploy workflows, observability dashboards, load tests, or recovery exercises.

Those items are deferred by the current design re-entry decision rather than merely waiting in the immediate implementation queue.

# Handoff

Current work proceeds to [Phase 007 — Jackson Design Refinement & Methodology Closure](../../007-design-refinement/), beginning with **007-B — Concept Completeness, Independence & Genericity Audit**.

006-E persistence work remains deferred until a later explicit design exit authorizes implementation to resume.

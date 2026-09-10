---
type: Implementation Contract
title: Runtime, Environment & Delivery Bootstrap
description: Defines the qualified retained MUDAC workspace/runtime bootstrap, environment classes, verification gate, OpenTofu root/state separation, supply-chain posture, deployment-authority boundary, and protected-baseline status.
status: stable
tags: [implementation, runtime, environment, local-development, ci-cd, iac, delivery, protected-baseline, qualified]
sources:
  - resource: ../../006-implementation-planning/006-D-environment-iac-ci-cd-local-development-runtime-bootstrap.md
  - resource: ../../007-design-refinement/007-I-formal-jackson-concept-design-methodology-exit-accepted-residual-uncertainty-implementation-resume-boundary-decision.md
  - resource: ../../008-implementation-reentry/008-A-implementation-reentry-authority-canonical-baseline-change-control-planning-guardrails.md
  - resource: ../../008-implementation-reentry/008-B-protected-006-D-baseline-qualification-drift-audit-toolchain-environment-reconciliation.md
  - resource: ../../008-implementation-reentry/008-C-residual-risk-ingestion-historical-006-mapping-decision-register-supersession-matrix.md
  - resource: ../../008-implementation-reentry/008-D-persistence-temporal-truth-versioning-provenance-governed-exceptions-outbox-projection-migration-implementation-plan.md
  - resource: ../governance/design-implementation-boundary.md
  - resource: implementation-foundation.md
  - resource: verification-strategy.md
  - resource: source-topology.md
  - resource: persistence-history-projection.md
  - resource: ../architecture/aws-runtime-operations.md
  - resource: ../architecture/application-boundaries.md
  - resource: ../architecture/frontend-interaction.md
generated: { by: openai/gpt-5.6-sol, at: 2026-09-10T19:13:00Z }
---

# Purpose

Define the retained executable environment/runtime/delivery substrate established by 006-D and re-qualified by 008-B. This owner realizes accepted architecture and implementation contracts; it does not create product/domain authority or claim production infrastructure has been provisioned.

The current [Design / Implementation Boundary](../governance/design-implementation-boundary.md) treats this substrate as a **qualified protected non-domain implementation baseline** while Phase 008 refreshes the implementation plan.

This owner introduces no new stable-rule namespace. Runtime/bootstrap configuration cites upstream `AWS-*`, `IMPL-*`, `MOD-*`, `FE-*`, and related rules rather than creating a parallel deployment-rule universe.

# Current status — qualified protected baseline

008-B audited the retained workspace, package topology, toolchain pins, lockfile, application roots, local PostgreSQL, dependency enforcement, CI, supply-chain configuration, and OpenTofu roots against current authority.

**Result: qualified for Phase 008 planning after narrow non-domain remediation.**

008-C assigned the remaining repository-administration/dependency-evidence limits to later Phase 008 owners and fully superseded the historical 006-E through 006-M execution queue. 008-D has since accepted the downstream persistence/history/migration plan while keeping the executable baseline itself schema-free.

Until 008-L explicitly authorizes the first executable domain slice, this substrate may be retained and narrowly maintained but not extended into new MUDAC domain behavior.

# Qualified executable workspace

The root pnpm workspace retains:

- Node.js 24 runtime family;
- pnpm 11.25.0;
- TypeScript 6.0.3;
- Fastify 5.12.1;
- React/React DOM 19.2.8;
- React Router 8.3.1;
- TanStack Query 5.102.8;
- Vite 8.2.2;
- Vitest 4.1.11;
- Playwright 1.62.1;
- ESLint 10.8.1;
- Prettier 3.9.6;
- dependency-cruiser 18.2.0;
- OpenTofu 1.12.0 in CI with roots constrained to the 1.12 family.

The committed lockfile agrees with the inspected manifest pins. Frozen installs remain the reproducibility baseline.

pnpm dependency build scripts remain deny-by-default under safer-build behavior; required `esbuild` execution is explicitly allowlisted instead of globally disabling the control.

No upgrade is required merely because a newer release exists. Material upgrades remain deliberate under `IMPL-010` and require compatibility evidence when consequential.

# Composition roots and domain boundary

`apps/api`, `apps/worker`, and `apps/web` remain executable composition roots under the accepted source topology.

- API: Fastify startup plus `/healthz` only.
- Worker: process lifecycle/signal handling only.
- Browser: React/Router/Query bootstrap only.

The six authoritative module packages remain minimal public seams. `@mudac/application` and `@mudac/projections` remain non-domain placeholders, and `@mudac/foundation` remains business-neutral.

008-B found no authoritative domain schema, migration, repository, authentication/session behavior, domain API, IndexedDB Draft behavior, Competition/Judging/Evaluation/Outcome/Export/Publication implementation, or domain-purpose AWS resource.

008-D is a planning artifact only and did not alter that executable fact. Therefore new domain implementation after 006-D remains **NOT STARTED**.

# Local development

Routine local development runs Node application processes on the host and PostgreSQL through Docker Compose.

The current local service uses `postgres:17-alpine` with development-only default credentials and a named local volume. This is a qualified local bootstrap dependency, not a production PostgreSQL-version contract and not an authoritative MUDAC schema.

008-D defines the future PostgreSQL schema/migration conventions but does not instantiate them in this bootstrap.

External provider behavior such as Cognito, S3, SQS, email, scanners, and rendering remains behind application-owned ports. Deterministic local fakes support normal development/testing; targeted real-service evidence belongs to later authorized work when provider semantics matter.

Normal local development does not require long-lived AWS credentials.

# Environment authority

MUDAC distinguishes:

- `local` — developer host + local PostgreSQL + deterministic provider fakes;
- `CI` — ephemeral verification runners with no ordinary production authority;
- `nonproduction` — separate AWS account in `us-east-2`, synthetic/test data and reduced redundancy where allowed;
- `production` — separate AWS account in `us-east-2`, governed by accepted Multi-AZ `AWS-*` topology;
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

Each environment uses its own S3 remote-state identity. Example partial backend configuration retains encryption and S3-native locking (`use_lockfile = true`). Account-specific backend coordinates and credentials are not committed.

State-storage bootstrap remains administratively separate because an environment backend cannot safely create itself.

008-B confirmed the environment roots remain scaffolding-only: their current `main.tf` files identify environment/Region and do not provision AWS application resources. Reusable infrastructure modules also remain placeholders.

# Verification and supply-chain posture

The GitHub Actions workflow named **Implementation Verification** remains the stable executable check surface for the retained bootstrap.

It covers frozen install, formatting, TypeScript, ESLint, dependency-cruiser, Vitest, application builds, Docker Compose configuration, OpenTofu formatting, and backend-disabled root validation.

The workflow covers all pull requests and pushes to `main`. 008-B removed the obsolete historical `phase-006-*` direct-push special case.

Knowledge Validation remains separate under `VAL-*`. CodeQL remains configured for JavaScript/TypeScript analysis. Dependabot remains configured weekly for npm and GitHub Actions.

The final 008-B bootstrap head passed Implementation Verification and CodeQL. That is evidence for the tested revision, not implementation or production authority.

The baseline also retains ignored local secrets/state/output, restrictive package exports, and source dependency enforcement.

The current connector does not expose the Dependabot alert inventory used for a complete vulnerability-state assertion. 008-C assigns that evidence limitation to 008-K. Therefore configured controls and successful CI may be claimed; zero open dependency vulnerabilities may not be inferred.

Scanner or CI success is evidence about a tested revision, not application authority, implementation correctness, first-slice authorization, deployment authority, or production certification.

# Repository and deployment authority

Ordinary implementation merge policy is intended to require pull requests plus current Knowledge Validation and applicable Implementation Verification checks on `main` under `IMPL-013`.

008-B revalidated that the repository rulesets endpoint currently returns no rulesets. Branch-protection state cannot be read by the connected integration. 008-C assigns this administration/evidence residual to 008-K with 008-L authorization-gate responsibility. Documentation therefore must not claim the intended merge controls are enforced.

Production deployment remains separately authorized through a protected GitHub environment and OIDC-federated AWS role under `IMPL-014`/`AWS-011`. Those controls and actual production resources are not established by this baseline.

Real local secret files are ignored. Long-lived AWS deployment keys do not belong in GitHub or repository configuration.

# Release posture retained for future implementation

When later implementation is authorized, backend/frontend deployment workflows must bind releases to exact repository/build identity. Backend rollout uses immutable image identity; frontend rollout uses content-addressed immutable assets plus a mutable release entrypoint/manifest.

008-D now requires SQL-first forward migrations, checksum verification, an advisory migration lock, separate migrator authority, no application-startup auto-migration, and expand/migrate/contract compatibility. Database migration remains a separately privileged deployment step once schema work is authorized, and application rollback must not assume destructive schema rollback.

CI may validate OpenTofu without backend credentials. Real plan/apply occurs only under intended environment/account deployment authority and an exact reviewed revision.

A syntactically valid IaC root does not prove AWS resources exist, are secure, can recover, or satisfy production SLOs.

# Current executable topology

```text
GitHub repository
  ├── pnpm workspace
  │    ├── apps/api        Fastify health bootstrap
  │    ├── apps/worker     lifecycle bootstrap
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

This qualified bootstrap still does not implement the PostgreSQL schemas/migrations/outbox/projections planned by 008-D, Cognito/session/Access, API command semantics, IndexedDB Drafts, domain workflows, actual AWS application resources, OIDC IAM roles, production environment protection, deploy workflows, observability dashboards, load tests, or recovery exercises.

These are later implementation-planning/evidence concerns, not defects in the 006-D bootstrap.

# Handoff

The protected baseline remains qualified as current planning input. 008-D has fixed the persistence/history/migration contract that future authorized work will add to it.

Proceed to **008-E — Identity, Authentication, Participation, Access, Session, Invitation, Secrets & Technical-Authority Implementation Plan**.

No first executable domain slice is authorized before 008-L; new domain implementation remains not started.

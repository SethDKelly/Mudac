---
type: Implementation Contract
title: Implementation Authority, Toolchain & Delivery Governance
description: Defines MUDAC's current implementation authority, common runtime/toolchain, repository delivery controls, dependency/version policy, security-scanning posture, and Phase 006 completion contract.
status: stable
tags: [implementation, authority, toolchain, delivery, repository, security]
sources:
  - resource: ../../006-implementation-planning/006-A-implementation-authority-delivery-governance-toolchain-repository-enforcement.md
  - resource: runtime-delivery-bootstrap.md
  - resource: ../governance/documentation-authority.md
  - resource: ../governance/change-governance.md
  - resource: ../governance/validation-enforcement.md
  - resource: ../architecture/application-boundaries.md
  - resource: ../architecture/data-persistence.md
  - resource: ../architecture/commands-api-concurrency.md
  - resource: ../architecture/frontend-interaction.md
  - resource: ../architecture/aws-runtime-operations.md
generated: { by: openai/gpt-5.6-sol, at: 2026-09-05T00:20:00Z }
---

# Purpose

Define the durable implementation-level rules established at Phase 006 entry. These rules constrain source code, build/test tooling, migrations, generated contracts, CI/CD, and IaC while remaining subordinate to canonical product/UX/governance and architecture meaning.

<a id="impl-001"></a>
## IMPL-001 — Upstream canonical meaning outranks implementation convenience

Source code, tests, framework conventions, migrations, generated code, and infrastructure must satisfy current canonical product/UX/governance and architecture contracts. If an implementation choice conflicts with upstream meaning and redesign was not explicitly requested, the implementation changes.

A semantic redesign uses `CHG-*`; it is never hidden in code, tests, schema defaults, framework behavior, or an implementation ADR.

<a id="impl-002"></a>
## IMPL-002 — Application implementation uses one primary TypeScript/Node toolchain

The initial server and browser implementation use TypeScript on the Node.js 24 LTS toolchain. The repository does not introduce another primary application language/runtime without a demonstrated capability, workload, security, or maintenance driver.

Exact patch/minor versions are pinned in implementation manifests/lockfiles and upgraded deliberately; this rule owns the runtime family, not an eternal patch number.

<a id="impl-003"></a>
## IMPL-003 — Fastify is the server transport host, not the domain architecture

Fastify 5.x is the initial HTTP/application-host framework. Routes, hooks, plugins, validation/serialization integration, and server lifecycle remain transport/runtime concerns.

MUDAC modules, commands, domain rules, Access, transactions, and persistence ownership stay behind application/module contracts and do not depend on Fastify as their semantic model.

<a id="impl-004"></a>
## IMPL-004 — pnpm workspaces are the initial repository package/workspace mechanism

The TypeScript implementation uses pnpm workspaces and a committed lockfile. Repository orchestration begins with pnpm workspace/recursive scripts and ordinary CI composition.

Nx, Turborepo, Bazel, or another task-graph/cache platform requires measured build/test/repository pressure before adoption.

<a id="impl-005"></a>
## IMPL-005 — PostgreSQL access uses Kysely over node-postgres with explicit migrations

Application persistence adapters use Kysely with `pg`/node-postgres for typed, inspectable SQL access. Production schema evolution uses version-controlled explicit migrations; automatic schema push/synchronization is not a production migration mechanism.

Persistence rows/query models remain adapter concerns and cannot become shared cross-module domain entities. 006-E owns detailed schema, migration, generated-type, transaction, and projection conventions.

<a id="impl-006"></a>
## IMPL-006 — API schemas are explicit transport contracts and generate OpenAPI outward

Fastify transport adapters register explicit JSON-schema-compatible request/response contracts. The published OpenAPI representation is generated from the accepted transport boundary and may feed generated clients.

Domain or persistence objects are not serialized as the public contract merely to reduce mapping code. Exact type-provider/client-generator packages remain 006-G implementation details.

<a id="impl-007"></a>
## IMPL-007 — Verification uses Vitest and Playwright families with evidence defined before feature scale

Vitest is the baseline TypeScript test-runner family; Playwright is the browser end-to-end family. 006-B defines the complete test/evidence matrix, fixtures, database integration strategy, accessibility/security layers, and blocking CI gates before broad feature implementation.

A newly released major is adopted only after compatibility evidence rather than because it is latest.

<a id="impl-008"></a>
## IMPL-008 — Type, lint and formatting checks are mandatory implementation gates

TypeScript strict type checking, ESLint flat configuration with TypeScript-aware rules, and Prettier deterministic formatting form the baseline static-quality gate.

Suppressions are narrow and explained. Repository/module dependency enforcement is added explicitly in 006-C rather than assumed from directory naming.

<a id="impl-009"></a>
## IMPL-009 — Persistent AWS infrastructure is implemented with OpenTofu

OpenTofu is the baseline IaC tool for the accepted AWS topology. Infrastructure plans/state/modules remain separate from application semantic modules and are reviewed as infrastructure changes.

The runtime/delivery bootstrap owns environment/state/backend/module layout and deployment sequencing. Application code does not create unmanaged long-lived production infrastructure as an ordinary runtime side effect.

<a id="impl-010"></a>
## IMPL-010 — Dependency versions and lockfiles are deliberate, reproducible inputs

The committed pnpm lockfile is part of the reviewed build input. Direct dependency ranges are intentionally bounded, CI/container builds use the lockfile, and dependency updates are reviewed as code.

Automated update PRs may be used but do not auto-merge solely because a version exists. Material major/toolchain upgrades require compatibility evidence and an implementation decision record when they affect cross-cutting behavior.

<a id="impl-011"></a>
## IMPL-011 — Generated code is identifiable, reproducible, and not hand-owned

Generated clients/types/assets used by the implementation have a known source contract and deterministic generation command where practical. Generated outputs are identifiable by path/header/convention and are not manually edited as an alternate source of truth.

CI may regenerate/diff-check material generated outputs so source contracts and checked-in artifacts cannot drift silently.

<a id="impl-012"></a>
## IMPL-012 — Security and supply-chain scanning is layered and dispositioned

The implementation baseline uses layered dependency, static-code, container and IaC scanning appropriate to introduced artifacts, including GitHub dependency/CodeQL capabilities, package audit signals, Trivy, and OpenTofu/TFLint checks when applicable.

Findings are fixed, shown to be inapplicable, or explicitly accepted with reason/owner/expiry-equivalent handling. Broad permanent suppression is not the default resolution.

<a id="impl-013"></a>
## IMPL-013 — `main` is intended to be PR-gated by required current checks before implementation merges

Once implementation work begins, ordinary changes reach `main` through pull requests with required current Knowledge Validation and applicable implementation-CI checks. Force pushes and branch deletion are prohibited.

A mandatory reviewer count is not required while the repository is effectively single-maintainer; review requirements should strengthen when independent maintainers exist rather than create ceremonial self-approval.

The required workflow checks now exist, but repository ruleset/branch-protection administration remains an external repository-admin gate because the current connected GitHub capability cannot configure or verify all protection settings. Workflow existence must not be represented as enforced merge policy until those controls are independently configured and confirmed.

<a id="impl-014"></a>
## IMPL-014 — Merge does not imply production deployment authority

Production deployment is independently gated through the protected GitHub environment and OIDC-federated AWS deployment role required by `AWS-011`. Merge success does not itself authorize or prove a production release.

Production workflow execution uses immutable release identity and does not rely on long-lived AWS keys. The protected environment and AWS role must be actually provisioned/configured before production deployment authority is claimed.

<a id="impl-015"></a>
## IMPL-015 — Material implementation decisions are recorded without becoming upstream redesign

Cross-cutting/reversible implementation choices that affect multiple delivery groups use implementation decision records with upstream-rule links, alternatives, consequences, reversibility, and supersession history.

An implementation decision record cannot override canonical architecture. A choice that would change product/architecture semantics escalates through `CHG-*` first.

<a id="impl-016"></a>
## IMPL-016 — Phase 006 subgroup completion requires implementation and evidence closure

A Phase 006 subgroup is complete only when its material decisions are explicit, current implementation routing is updated, applicable quality/security/tests pass, relevant stable-rule traceability exists, compatibility/migration implications are addressed, unresolved risks are assigned to named later gates, documentation validation remains green, and the next dependency-safe handoff is identified.

Passing CI is evidence for the tested revision, not semantic verification metadata or production certification.

# Selected toolchain summary

```text
runtime/language     Node.js 24 LTS + TypeScript 6.x
workspace/package    pnpm workspaces
server transport     Fastify 5.x
PostgreSQL access    Kysely + node-postgres
schema evolution     explicit version-controlled migrations
API description      explicit transport schemas → OpenAPI
unit/integration     Vitest family
browser E2E          Playwright family
static quality       tsc strict + ESLint + Prettier
AWS IaC              OpenTofu
security baseline    GitHub dependency/CodeQL + package audit + Trivy + IaC checks
```

Exact implementation versions are pinned in manifests/lockfiles and are not permanent canonical semantics.

# Delivery posture

006-A established the common toolchain/governance, 006-B the verification/evidence model, 006-C the source/package boundaries, and 006-D the executable workspace/local/CI/IaC bootstrap. The next implementation substrate is 006-E persistence.

The stable Knowledge Validation and Implementation Verification workflows are executable. Actual repository protection and protected production-environment administration remains explicitly external until independently configured and verified; this owner does not conflate workflow availability with enforced GitHub policy.

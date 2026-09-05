---
type: Implementation Contract
title: Verification Strategy, Evidence & Quality Gates
description: Defines MUDAC's current verification layers, deterministic evidence/fixture rules, stable-rule traceability, external-adapter testing, accessibility/security/concurrency/recovery evidence, and CI quality-gate semantics.
status: stable
tags: [implementation, verification, testing, evidence, fixtures, quality-gates]
sources:
  - resource: ../../006-implementation-planning/006-B-verification-strategy-test-harness-evidence-fixtures-quality-gates.md
  - resource: implementation-foundation.md
  - resource: runtime-delivery-bootstrap.md
  - resource: ../governance/validation-enforcement.md
  - resource: ../architecture/architectural-foundation.md
  - resource: ../architecture/application-boundaries.md
  - resource: ../architecture/data-persistence.md
  - resource: ../architecture/identity-access-session.md
  - resource: ../architecture/commands-api-concurrency.md
  - resource: ../architecture/synchronization-recovery.md
  - resource: ../architecture/external-representation.md
  - resource: ../architecture/frontend-interaction.md
  - resource: ../architecture/aws-runtime-operations.md
generated: { by: openai/gpt-5.6-sol, at: 2026-09-05T00:20:00Z }
---

# Purpose

Define durable implementation-level verification rules for MUDAC. Verification demonstrates that implementation behavior satisfies current canonical contracts; it does not create product meaning, replace semantic review, or certify production readiness by itself.

This owner intentionally does not introduce a second stable-rule namespace. Verification evidence should trace the existing canonical product/architecture/implementation rule IDs it proves rather than creating a parallel rule universe for tests.

## Verification evidence is subordinate to canonical meaning

Tests, fixtures, snapshots, scanners, CI results, and operational exercises prove selected behavior for a tested revision. They do not override canonical product/UX/governance/architecture/implementation rules.

When a test and canonical meaning conflict, determine whether the test encodes an implementation mistake or whether a deliberate `CHG-*` semantic change is required. Do not weaken canonical meaning by merely changing the test.

## Use the smallest trustworthy evidence layer that crosses the material boundary

Verification is selected by the failure/authority boundary being protected rather than by a universal test pyramid.

Pure logic uses unit/module evidence; PostgreSQL semantics use real PostgreSQL; transport contracts use the HTTP/application boundary; browser interaction/accessibility uses rendered DOM/real-browser evidence; disaster recovery and event-day readiness require operational exercises.

## Stable-rule traceability references identifiers, not copied rule text

Executable/manual/operational evidence may map to canonical stable rule IDs through a machine-readable traceability index once relevant source/evidence locations exist.

Traceability records rule IDs, evidence identifiers/types/locations, and cadence/gate information without becoming a duplicate normative rule store.

## Tests control nondeterminism through explicit ports and deterministic fixtures

Time, IDs, external delivery/providers, and other nondeterministic boundaries use explicit test seams where needed. Fixtures use synthetic data and identify consequential lifecycle/authority/version/disclosure state rather than hiding it behind magical defaults.

Sleep timing, test-order dependence, uncontrolled network calls, and shared mutable global state are not accepted foundations for authoritative behavior tests.

## PostgreSQL-dependent behavior is verified against real PostgreSQL

When correctness depends on SQL constraints, transactions, isolation/locking, migrations, concurrency, PostgreSQL types, or other production database semantics, tests use disposable real PostgreSQL environments such as Testcontainers rather than SQLite, in-memory maps, or query-layer mocks.

Database integration starts from explicit migrations except when intentionally testing migration from a prior release state.

## External adapters have deterministic contract fakes plus real-service evidence where vendor semantics matter

Cognito, S3, SQS, email/invitation delivery, artifact rendering, scanners, and similar external boundaries are represented behind application-owned ports with deterministic fakes for routine tests.

Where correctness depends materially on vendor behavior, targeted nonproduction integration/smoke evidence against the real service is also required. A broad cloud emulator is not sufficient proof of production provider semantics.

## Consequential commands require success, denial, conflict, retry, and uncertainty evidence as applicable

High-consequence transitions must be verified across the material result classes defined by `API-*`, including confirmed commit, validation/precondition failure, authorization denial, stale revision conflict, idempotent replay/misuse, temporary failure, and uncertain/lost-response reconciliation where relevant.

Logical uniqueness/domain constraints are tested independently from API idempotency so retry protection cannot hide duplicate semantic creation defects.

## Security verification tests application authority and disclosure, not only scanners

Security evidence includes contextual Access/resource authorization, dual-role isolation, session/CSRF/revocation/shared-device behavior, invitation/token scope/expiry/replay, break-glass separation, private Artifact delivery, disclosure surfaces, idempotency abuse, and upload validation as those features exist.

Static/dependency/container/IaC scanners complement rather than replace these behavioral tests.

## Accessibility evidence combines semantic tests, automated scanning, and manual assessment

Component/browser tests prefer semantic roles/names/labels and include automated axe-compatible scanning of critical workflow states.

Automated accessibility scanning is not production certification. Critical Judge/Organizer flows also require manual keyboard, assistive-technology, zoom/reflow, and other relevant evidence before release readiness under `FE-013`/`INV-009`.

## Browser end-to-end tests protect critical user journeys, not every internal branch

Playwright end-to-end tests cover integration seams that cheaper layers cannot reliably prove: authentication/context entry, Judge/Organizer isolation, authoritative Finalization, conflict/recovery, paper capture, closeout, and external representation as implemented.

Pure calculations and local module behavior remain tested at lower layers rather than duplicated broadly through the browser.

## Fixture and scenario ownership follows semantic module ownership

Module test builders own their module's resources and public setup contracts. Cross-module scenarios compose those public builders/contracts instead of mutating another module's tables or importing private persistence models.

Test code cannot become a permanent bypass around `MOD-*`/`DATA-*` ownership simply because it runs outside production.

## Golden/snapshot evidence is reserved for intentional external or historical fidelity

Golden fixtures are appropriate for stable outward contracts/representations such as OpenAPI, serialized disclosure profiles, migration compatibility samples, Artifact metadata/manifests, and later reviewed print/PDF outputs.

Large opaque object snapshots or broad React DOM snapshots are not the default. Golden changes require intentional review of the contract/output change.

## Code coverage is diagnostic evidence, not a correctness oracle

Vitest coverage is collected for visibility/regression analysis, but no single repository-wide line/branch percentage proves MUDAC correctness or substitutes for rule/behavior evidence.

Package-specific floors may be introduced once implementation exists and they detect meaningful regression. Consequential paths require explicit behavioral evidence regardless of percentage.

## CI uses stable blocking gates plus deeper scheduled/release evidence

The executable **Implementation Verification** workflow now provides the stable application/IaC check identity established by 006-D, while Knowledge Validation remains separate. Internal checks may evolve without forcing a new semantic meaning for the gate.

The current bootstrap gate covers reproducible installation, formatting, type checking, lint, source dependency rules, current unit tests/builds, local Compose configuration, and OpenTofu formatting/root validation. Later groups add applicable database/API/component/generated/security evidence behind the same verification posture. Deeper browser/concurrency/recovery/scanner suites may run on main/schedule; migration/load/restore/DR/manual-accessibility/event-day evidence belongs to release/operational readiness as appropriate.

Workflow existence does not prove GitHub branch protection currently requires the check; repository-admin enforcement remains explicitly tracked by the runtime/delivery owner.

## Flaky evidence is a defect and retries cannot silently convert failure into trust

Retries may collect diagnostics, but an initial blocking-test failure remains visible and a later retry pass does not by itself establish trusted evidence.

Quarantine requires an explicit owner/reason and cannot indefinitely remove verification from consequential authority/security behavior.

## Verification artifacts are useful, synthetic, and privacy-minimized

CI may retain structured results, coverage, traces/screenshots/videos on failure, scanner reports, migration logs, and later operational evidence for diagnosis.

Fixtures/artifacts use synthetic data by default; secrets, production tokens, private Judge prose, hidden Team identity, and unnecessary personal data are not captured merely for test convenience. Evidence retention is bounded by operational need.

# Verification layer summary

```text
pure/unit               Vitest
module contract         Vitest + real owned collaborators
PostgreSQL integration  disposable real PostgreSQL/Testcontainers
API/transport           Fastify application boundary + real DB when material
React interaction       Testing Library-style semantic queries
browser E2E             Playwright
accessibility           semantic queries + axe automation + manual evidence
security                behavioral authority/disclosure tests + scanners
concurrency/recovery    deterministic barriers + real transactions/adapters
migration/deployment    prior/current schema compatibility + rollout evidence
operational readiness   load/restore/DR/paper/runbook exercises
```

# Current CI posture

006-D has instantiated the pinned workspace and the stable **Implementation Verification** workflow. 006-E onward add real persistence/domain/browser evidence as their behavior appears; empty test categories are not treated as proof before the corresponding implementation exists.

Knowledge Validation remains its own `VAL-*`-governed read-only structural check and is not absorbed into the application test runner. Repository ruleset/environment administration remains an external GitHub administration gate until independently configured and verified.

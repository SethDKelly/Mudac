---
type: Implementation Planning Record
title: 006-B — Verification Strategy, Test Harness, Evidence Fixtures & Quality Gates
description: Defines MUDAC's implementation verification model, test layers, deterministic fixture strategy, stable-rule traceability, external-adapter verification, accessibility/security/concurrency/recovery evidence, and CI quality gates.
status: stable
tags: [phase-006, implementation, verification, testing, evidence, fixtures, quality-gates]
sources:
  - resource: ../005-system-application-data-synchronization-architecture/005-J-phase-005-consolidation-threat-failure-review-implementation-readiness-exit.md
  - resource: ../canonical/implementation/implementation-foundation.md
  - resource: ../canonical/governance/validation-enforcement.md
  - resource: ../canonical/architecture/architectural-foundation.md
  - resource: ../canonical/architecture/application-boundaries.md
  - resource: ../canonical/architecture/data-persistence.md
  - resource: ../canonical/architecture/identity-access-session.md
  - resource: ../canonical/architecture/commands-api-concurrency.md
  - resource: ../canonical/architecture/synchronization-recovery.md
  - resource: ../canonical/architecture/external-representation.md
  - resource: ../canonical/architecture/frontend-interaction.md
  - resource: ../canonical/architecture/aws-runtime-operations.md
  - resource: https://vitest.dev/config/coverage
  - resource: https://playwright.dev/docs/accessibility-testing
  - resource: https://node.testcontainers.org/modules/postgresql/
  - resource: https://testing-library.com/docs/react-testing-library/intro/
generated: { by: openai/gpt-5.6-sol, at: 2026-09-04T15:23:00Z }
---

# Purpose

Define the verification system that Phase 006 implementation work must use before feature volume makes ad hoc testing conventions expensive or misleading.

006-B does not create product semantics. It defines how implementation demonstrates conformance to existing canonical product, UX, architecture, and implementation contracts while preserving the distinction between executable evidence, structural CI, semantic review, and production-readiness proof.

# Governing verification model

MUDAC does not use one test pyramid or one coverage percentage as the definition of correctness. Evidence is selected according to the authority/failure boundary being protected.

```text
canonical rule / behavior
        ↓
smallest trustworthy evidence layer
        ↓
real boundary where semantics matter
        ↓
recorded result / diagnostic evidence
```

A pure calculation should usually be proven without a browser. A PostgreSQL concurrency invariant should be exercised against real PostgreSQL. A browser disclosure/accessibility workflow should be exercised through the rendered DOM or real browser. A regional restore claim cannot be established by a unit test.

# Accepted verification layers

## 1. Pure/unit verification

Use Vitest for deterministic business-neutral utilities, value objects, pure domain policies/calculations, state-transition helpers, serialization helpers, and small application functions that do not require a real external boundary.

Unit tests should prefer explicit inputs/outputs over framework internals and should not mock private functions merely to force implementation shape.

## 2. Module-contract verification

Each authoritative module is tested through its public application/domain contract with internal collaborators real whenever practical. Module tests prove invariants, lifecycle transitions, authority checks delegated to the module, Version/Provenance consequences, and error semantics without routing through HTTP unless transport behavior is the subject.

Cross-module tests compose public contracts rather than importing another module's repository or mutating its storage directly.

## 3. PostgreSQL integration verification

Database-dependent behavior uses disposable **real PostgreSQL** instances through Testcontainers for Node.js or an equivalent container boundary selected consistently by the harness.

SQLite, an in-memory map, or ORM/query-builder mocks are not substitutes for PostgreSQL evidence when the behavior depends on:

- SQL constraints;
- transaction visibility/isolation;
- row locking;
- unique/foreign/check constraints;
- migration behavior;
- concurrent writes;
- JSON/array/database-specific types;
- advisory/database semantics actually used by production.

Every database integration environment starts from explicit migrations rather than a hidden schema snapshot unless the test is intentionally a migration-from-prior-version case.

## 4. API/transport contract verification

Fastify routes are tested at the application transport boundary using Fastify's in-process request injection where appropriate. Tests exercise the real transport schemas, session/CSRF hooks, DTO mapping, application command/query invocation, semantic error mapping, and response contracts.

Authoritative API paths use the real application/module transaction and PostgreSQL integration boundary when the behavior under test depends on persistence or concurrency.

Generated OpenAPI is contract-diffed against its accepted source schemas; a generated client is tested against representative contract fixtures once introduced in 006-G.

## 5. Browser component/interaction verification

React component and semantic-pattern tests use Testing Library-style user-visible queries and interactions rather than asserting component internals. Accessible names/roles/labels are preferred over implementation selectors.

Component tests prove local rendering, interaction, validation assistance, status/recovery presentation, and context-state behavior that does not require a complete deployed system.

## 6. Browser end-to-end verification

Playwright covers critical role/workflow journeys through the assembled browser + API + database system. E2E tests prove integration seams that smaller tests cannot, including authenticated navigation, Judge/Organizer mode separation, explicit Finalization, conflict/recovery surfaces, paper capture, reconciliation/finalization, and external-representation workflows as those slices are delivered.

E2E is not used to re-test every pure calculation already covered more cheaply below the browser boundary.

## 7. Security verification

Security evidence includes deterministic application tests plus appropriate scanning and later operational review.

The application test catalog must cover, as features appear:

- current contextual Access rather than stale role/session claims;
- horizontal/vertical resource authorization and concealment behavior;
- Judge/Organizer dual-role isolation;
- session fixation/revocation/logout/shared-device behavior;
- CSRF enforcement for cookie-authenticated mutation;
- invitation/token replay/expiry/scope;
- idempotency-key abuse and replay;
- private Artifact delivery and signed-delivery boundaries;
- disclosure leakage through body/metadata/filename/QR/accessibility layers;
- break-glass/operator separation;
- upload type/size/integrity/content-scanning behavior when uploads exist.

CodeQL, dependency review, package audit, Trivy and IaC/container scanning complement these tests but do not replace authorization/domain verification.

## 8. Accessibility verification

Automated accessibility checks use Playwright with `@axe-core/playwright` (or an equivalent axe integration) on critical workflow states, plus Testing Library semantic queries during component tests.

Automated scanning is necessary but insufficient. Critical Judge and Organizer workflows also require manual assistive-technology/keyboard/reflow evidence before production readiness. Automated checks cannot certify WCAG semantic parity by themselves.

## 9. Concurrency/idempotency/recovery verification

The harness must make race and retry behavior reproducible rather than relying on chance timing.

Required evidence patterns include, when the associated implementation exists:

- two writers from the same expected revision;
- same idempotency key + same intent;
- same idempotency key + materially different intent;
- different idempotency keys attempting duplicate semantic creation;
- commit succeeds but response is lost;
- lock/isolation retry paths;
- outbox record committed with source transaction;
- duplicate/out-of-order asynchronous delivery;
- projection lag/rebuild;
- local Draft conflict preserving both traces;
- Access expiry before queued Draft synchronization;
- worker crash/retry/DLQ handling;
- Artifact upload without authoritative registration and vice versa.

Tests synchronize on explicit barriers/hooks/test seams rather than sleep-based race timing where possible.

## 10. Migration/deployment compatibility verification

Migration evidence must prove more than "migration applies to an empty database."

The strategy includes:

- migrate empty database to current;
- migrate representative prior-release schema/data to current;
- run old/new application compatibility checks during expand/contract windows where applicable;
- verify destructive/contract migration preconditions;
- exercise rollback/recovery procedure where schema rollback is claimed;
- ensure retained Version/Provenance/evidence cannot be destroyed by ordinary cascade or migration accident.

006-E/006-D define the exact migration harness and deployment sequencing.

## 11. Infrastructure/operational verification

OpenTofu format/validate, TFLint, Trivy/IaC scanning, plan review, immutable release/smoke tests, observability checks, backup restore exercises, regional cold recovery, event-day load tests, and paper fallback drills are verification layers rather than substitutes for application tests.

The expensive/destructive operational layers run on an appropriate scheduled/manual/release cadence rather than every pull request.

# Test-double policy

Use test doubles at **external or nondeterministic boundaries**, not as a default replacement for owned application behavior.

Good fake/adapter seams include:

- clock/time;
- ID generation;
- Cognito authentication exchange;
- email/invitation delivery;
- S3 object operations;
- SQS dispatch/receive;
- artifact renderer;
- external malware/content scanner;
- deployment/cloud APIs.

A deterministic fake must implement the same application-owned port contract as the real adapter. Where vendor semantics materially affect correctness, targeted integration/smoke tests against the real nonproduction service are additionally required.

MUDAC does not treat a broad AWS emulator as proof that Cognito/S3/SQS production semantics are correct. Emulation may accelerate local tests, but real-service evidence is used where the vendor boundary itself matters.

# Fixture and scenario strategy

## Deterministic factories

Factories build the smallest valid resource state with explicit overrides. Tests control time and stable IDs where reproducibility matters.

Factories must not hide consequential defaults such as lifecycle state, author/actor identity, Rubric Version, Participation, disclosure context, or authority basis.

## Module-owned fixture builders

Fixture ownership follows semantic module ownership. A module may expose test builders for its public resources; another module's test must compose those builders/public contracts rather than reaching into private persistence rows.

This keeps test code from becoming an accepted backdoor around `MOD-*`.

## Scenario builders

Cross-module scenarios compose explicit resources into reusable named situations such as:

- active Competition with one Panel/Encounter;
- Judge with one valid Participation;
- dual-role Judge/Organizer Identity;
- Scorecard Draft at known revision;
- Finalized Scorecard Version with correction successor;
- incomplete Coverage/reconciliation exception;
- Official Outcome Revision with successor;
- paper-origin Scorecard capture;
- private/published Artifact states.

Scenario builders identify material state; they do not create a second narrative specification of product rules.

## Golden/contract fixtures

Golden fixtures are reserved for outputs where exact external or historical fidelity matters, such as:

- OpenAPI contracts;
- disclosure profiles/serialized public DTOs;
- migration compatibility samples;
- Artifact metadata/manifests;
- later PDF/print external representations where exact rendering/content is intentionally reviewed.

Broad React DOM snapshots and large opaque object snapshots are not the default testing style. Golden changes require intentional review of why the external contract/output changed.

## Synthetic-only test data

Committed fixtures, screenshots, traces, database dumps, and test artifacts use synthetic data. Real Judge/Team/private-note content, real credentials, production tokens, or unnecessary personal information are never copied into repository fixtures.

# Stable-rule traceability

Verification traceability references **stable rule IDs only**; it does not duplicate the rule text.

Phase 006 will maintain a machine-readable evidence index once source topology is established. An evidence entry conceptually records:

```text
evidence identifier
stable rule ID(s)
evidence kind
implementation/test location
execution cadence/gate
```

One test may support several rules and one rule may require several evidence types. Not every documentation/governance rule is executable as a software test; such rules may instead map to structural validator, review, operational, or manual evidence.

The evidence index is routing/traceability, not a new normative rule store.

# Coverage posture

Vitest V8 coverage is collected for implementation visibility and regression analysis.

MUDAC does **not** use a single repository-wide line/branch percentage as proof of correctness or as the sole merge gate. A high percentage can still miss authority, race, failure, and disclosure behavior.

Later package-specific floors may be introduced when code exists and the threshold detects real regression rather than rewarding trivial test execution. Consequential paths remain required to have explicit behavioral evidence regardless of percentage.

# Accessibility/browser evidence posture

Testing Library semantic queries are preferred in component tests because they exercise the rendered interface through user-visible/accessibility-facing structure rather than React internals.

Playwright + axe is used for automated checks across important states, but manual keyboard/screen-reader/zoom/reflow testing remains a production-readiness requirement. Automated accessibility tooling catches only mechanically detectable classes of defect.

# CI quality-gate model

## Pull-request blocking gate

When implementation bootstrap exists, ordinary PRs must pass a stable aggregate **Implementation Verification** gate composed from applicable jobs such as:

- lockfile/install reproducibility;
- formatting;
- TypeScript strict type check;
- ESLint;
- Vitest unit/module tests;
- affected PostgreSQL/API integration tests;
- component tests;
- generated-contract drift checks;
- applicable dependency/static/IaC scans;
- Knowledge Validation remains a separate required check.

The exact workflow/job names are implemented in 006-D, but the aggregate check should remain stable so branch-protection policy does not churn as internal jobs evolve.

## Main/nightly/deep verification

Full integration and expensive suites may run after merge and/or on schedule, including:

- complete PostgreSQL integration suite;
- full Playwright browser suite/matrix;
- automated accessibility scans;
- concurrency/recovery stress cases;
- full CodeQL/dependency/container/IaC scans;
- generated contract/golden drift;
- broader compatibility tests.

A failure in a deep suite creates a visible implementation defect and blocks production promotion until resolved/dispositioned; it is not ignored because the PR fast gate was green.

## Release/operational evidence

Production promotion additionally depends on the evidence appropriate to the release, eventually including:

- migration compatibility/rollback evidence;
- security review/scanning disposition;
- manual accessibility evidence for affected critical flows;
- event-shaped load/concurrency tests;
- restore/RPO/RTO evidence;
- paper fallback/reconciliation exercise;
- observability/runbook/event-day readiness.

006-M owns the integrated production-readiness exit.

# Flaky-test policy

A flaky blocking test is a defect in the verification system or the implementation.

Retries may be used to collect diagnostics, but a retry pass does not erase the original failure or silently turn an unstable assertion into trusted evidence. Quarantine requires an explicit issue/owner/reason and cannot indefinitely remove coverage from a consequential authority/security path.

Sleep-based timing, shared mutable global fixtures, test-order dependence, and uncontrolled external network dependencies are treated as common flake sources to remove.

# Evidence retention and privacy

CI may retain JUnit-style results, coverage reports, Playwright traces/screenshots/videos on failure, scanner reports, migration logs, and later operational evidence as useful diagnostics.

Evidence collection follows data minimization:

- synthetic test data by default;
- secrets/tokens never emitted;
- private Judge prose and hidden Team identity not captured merely for debugging;
- browser/network traces scrub or avoid sensitive payloads;
- retention duration follows operational need rather than indefinite accumulation.

# Verification ownership and change rules

A test that fails because implementation diverges from canonical meaning is not "fixed" by weakening the test unless canonical meaning is deliberately changed through `CHG-*`.

A test that encodes accidental implementation detail should be changed when the implementation is legitimately refactored without semantic change.

Verification code therefore answers:

> What externally or semantically observable behavior must remain true at this boundary?

not:

> How did today's implementation happen to achieve it internally?

# Exit result

006-B establishes a verification/evidence architecture sufficient for source/package topology and implementation bootstrap to proceed without every package inventing its own testing model.

No product or Phase 005 architecture rule changes.

The next dependency-safe subgroup is **006-C — Source Topology, Module/Package Boundaries, Shared Foundation & Dependency Enforcement**.

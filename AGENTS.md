# MUDAC Repository Agent Rules

This file is a **bootstrap adapter**, not the canonical source of MUDAC product, synchronization, architecture, implementation, verification, source-topology, runtime, or documentation rules.

Canonical governance lives under [`docs/canonical/governance/`](docs/canonical/governance/).

## Required start

1. Start at [`docs/index.md`](docs/index.md).
2. For current meaning, use [`docs/canonical/`](docs/canonical/).
3. For behavior spanning more than one Concept, load the relevant owner under [`docs/canonical/synchronizations/`](docs/canonical/synchronizations/) rather than reconstructing coordination from old phase history.
4. For correction, invalidation, supersession, replacement, current-vs-historical truth, affected/stale state, official-outcome succession, or Publication timeline work, additionally load [`Temporal Truth, Correction & Historical Authority`](docs/canonical/synchronizations/temporal-truth-correction.md).
5. For Judge/Organizer interaction, route, status, exception, confirmation, recovery, or UI-authority design, additionally load [`Experience Action, State & Authority Traceability`](docs/canonical/experience/action-authority-traceability.md) plus only the task-relevant experience owner(s).
6. For exception, waiver, override, acknowledgement/suppression, policy-bypass, or technical-emergency-versus-semantic-authority work, additionally load [`Operational Exception & Override Governance`](docs/canonical/policies/operational-exception-governance.md) plus the specific governing policy/Concept owner.
7. For Export/Publication or external representation work, preserve exact source authority and load the relevant [`Export`](docs/canonical/concepts/export.md), [`Publication`](docs/canonical/concepts/publication.md), disclosure, official-outcome, and temporal owners as needed. A representation cannot promote its source authority.
8. **Before any implementation/code/IaC task, read [`Design / Implementation Boundary`](docs/canonical/governance/design-implementation-boundary.md). The Jackson Concept Design methodology is complete for the current baseline, implementation planning is active, the 006-D non-domain substrate is qualified, but no executable domain slice is authorized.**
9. For architecture work, load only the relevant owner(s) under [`docs/canonical/architecture/`](docs/canonical/architecture/) plus materially relevant upstream constraints.
10. For implementation-planning work, also load the active [`Phase 008`](docs/008-implementation-reentry/) routing, the relevant owner(s) under [`docs/canonical/implementation/`](docs/canonical/implementation/), task-relevant architecture, and materially relevant product/UX/governance/synchronization constraints. [008-A](docs/008-implementation-reentry/008-A-implementation-reentry-authority-canonical-baseline-change-control-planning-guardrails.md) defines planning authority; [008-B](docs/008-implementation-reentry/008-B-protected-006-D-baseline-qualification-drift-audit-toolchain-environment-reconciliation.md) defines the qualified bootstrap baseline and its open evidence limits.
11. Verification/test work additionally loads [`Verification Strategy, Evidence & Quality Gates`](docs/canonical/implementation/verification-strategy.md).
12. Source/package/import work additionally loads [`Source Topology, Package Boundaries & Dependency Enforcement`](docs/canonical/implementation/source-topology.md).
13. Runtime/environment/CI/IaC work additionally loads [`Runtime, Environment & Delivery Bootstrap`](docs/canonical/implementation/runtime-delivery-bootstrap.md).
14. Use numbered phase history only for rationale, chronology, rejected alternatives, implementation lineage, or source audit.

Governed by `DOC-*`, `CTX-*`, `CHG-*`, `META-*`, `VAL-*`, task-relevant canonical synchronization/architecture rules, [`IMPL-*`](docs/canonical/implementation/implementation-foundation.md), the task-relevant canonical implementation owners, the active Phase 008 plan, and the current [Design / Implementation Boundary](docs/canonical/governance/design-implementation-boundary.md).

## Current post-methodology implementation boundary

The renewed Jackson Concept Design methodology formally exited through Phase 007-I for the current MUDAC baseline.

Phase 008 is active. 008-A established implementation-planning authority; 008-B qualified the retained 006-D substrate after narrow non-domain remediation.

Current status:

```text
Jackson Concept Design methodology: COMPLETE / EXITED
Phase 008 subdivision: COMPLETE
implementation planning authority: ESTABLISHED
008-A: COMPLETE
008-B: COMPLETE — PASS AFTER NARROW REMEDIATION
protected 006-D baseline: QUALIFIED FOR PHASE 008 PLANNING
008-C: NEXT / NOT STARTED
first executable domain slice: NOT YET AUTHORIZED
new domain implementation after 006-D: NOT STARTED
```

The executable work created through 006-D is retained as a **qualified protected non-domain implementation baseline**. Qualification permits later Phase 008 planning to rely on that substrate; it does not authorize domain extension.

Until **008-L — Consolidated Dependency Graph, Implementation Roadmap, First-Slice Authorization & Phase Exit Review** explicitly authorizes the first domain implementation slice, agents must not advance into new:

- domain PostgreSQL schema/migrations/repositories/outbox/projections;
- Cognito/session/Participation/Access/invitation implementation;
- production command/query API or idempotency/transaction implementation;
- IndexedDB Draft semantics;
- Competition, Judging, Evaluation, Outcome, Award, Export, Artifact or Publication feature implementation;
- real AWS application provisioning/deployment intended to support those domain paths.

Permitted executable changes before first-slice authorization remain narrow dependency/security/compatibility maintenance, non-domain verification/tooling repair, documentation/routing changes, and removal of accidental behavior that conflicts with current authority.

Current work should proceed to **008-C — Residual-Risk Ingestion, Historical 006 Mapping, Decision Register & Supersession Matrix**, not immediate domain coding.

## Qualified bootstrap evidence and limits

008-B confirmed the retained exact toolchain/lockfile, three composition roots, six authoritative module seams, schema-free local PostgreSQL bootstrap, dependency enforcement, CI configuration, and resource-free separated OpenTofu roots.

Two narrow drift items were repaired: stale browser copy pointing to later Phase 006 slices and an obsolete `phase-006-*` special push trigger in Implementation Verification.

Two limits remain visible:

- no repository rulesets are currently visible and branch-protection state cannot be read by the connected integration, so intended merge controls must not be claimed as enforced;
- Dependabot is configured, but the alert inventory is unavailable through the current connector, so zero open dependency findings must not be inferred.

## Do not

- recursively preload all of `docs/` for ordinary work;
- reconstruct current rules from old phase history when a canonical owner exists;
- duplicate synchronization or temporal semantics independently inside multiple Concept/architecture/implementation documents when the canonical synchronization owner can be referenced;
- collapse lifecycle, currentness, validity, affected/stale currency, replacement, distribution state, and historical observation into one convenience status merely for implementation ease;
- let a screen, route, work mode, status badge, exception row, confirmation dialog, recovery affordance, or enabled control become an alternate domain-action or authority owner;
- create a generic `override`/`force` path that can bypass policy-specific preconditions, source truth, authorship, official-outcome, disclosure, uncertainty, or historical-retention semantics;
- treat acknowledgement, dismissal, suppression, or closing of an exception presentation as repair of its authoritative source condition;
- let Export/Publication labeling or formatting promote provisional/calculated/Affected state into stronger authority than its identified source basis;
- copy complete canonical rules into downstream docs/tests/configuration when a rule ID/link plus local consequence is sufficient;
- let README/index/traceability/agent/test-fixture files become competing rule stores;
- silently resolve canonical contradictions by choosing convenient implementation wording;
- change product semantics only in code, tests, migrations, IaC, generated schemas, or comments;
- infer package/service/database structure from the knowledge-directory layout;
- create a package per Concept/table/command/screen/document merely because the subject is named;
- create `common`, `shared-domain`, generic `services`/`models`, or central infrastructure packages to bypass ownership;
- deep-import another workspace's private source or bypass package `exports` through cross-root relative paths/path aliases;
- let browser code import authoritative server modules, persistence implementations, or server-only test helpers;
- let Fastify routes, Kysely rows, OpenAPI DTOs, React components, OpenTofu modules, mocks, fixtures, or snapshots become alternate domain owners;
- substitute SQLite/in-memory evidence for real PostgreSQL when PostgreSQL semantics matter;
- hide flaky consequential tests behind retries or indefinite quarantine;
- treat CI, coverage, scanners, workflow existence, IaC validation, or deployment configuration as semantic verification or production certification;
- infer that completion of Concept Design, Phase 008 subdivision, 008-A/008-B completion, a qualified bootstrap, green checks, historical 005-J readiness, or old 006-E–M plans authorize skipping the 008-L first-slice boundary;
- begin Phase 009 or any new domain implementation before 008-L explicitly authorizes the first slice.

## Protected executable baseline

The selected implementation family remains Node.js 24 LTS + TypeScript, pnpm workspaces, Fastify, Kysely + node-postgres, explicit migrations, outward-generated OpenAPI, Vitest/Playwright, strict TypeScript + ESLint + Prettier, and OpenTofu.

Current source/runtime consequences retained and qualified from 006-D:

- `apps/api`, `apps/worker`, and `apps/web` are composition roots;
- six authoritative module packages remain empty/minimal semantic seams within the modular monolith;
- `@mudac/application` coordinates above owners and `@mudac/projections` is non-authoritative;
- `@mudac/foundation` remains business-neutral;
- package exports, dependency-cruiser, and ESLint enforce the dependency graph;
- local development uses host Node processes plus Docker Compose PostgreSQL without domain schema;
- external AWS/provider behavior uses deterministic fakes locally and targeted real-service evidence in nonproduction when later authorized;
- `Implementation Verification` is the stable executable CI check surface;
- OpenTofu has separate nonproduction `us-east-2`, production `us-east-2`, and cold-recovery `us-east-1` roots/state identities without application resources;
- actual GitHub branch/ruleset and protected production-environment administration remains an external repository-admin gate until independently configured.

These are preserved substrate choices, not first-slice implementation authority.

## Validation

Knowledge changes:

```text
python -m pip install -r requirements-docs.txt
python scripts/validate_knowledge.py
```

Permitted executable-maintenance changes before first-slice authorization:

```text
pnpm install --frozen-lockfile
pnpm verify
```

CI additionally validates current OpenTofu roots. Passing checks are evidence for the tested revision, not OKF verification, implementation correctness, authority to skip the Phase 008 boundary, or production certification.

## Canonical changes

If implementation planning discovers a genuine semantic contradiction, missing semantic owner, or the human requests a semantic change, use [`CHG-*`](docs/canonical/governance/change-governance.md). If an implementation/test/architecture mechanism conflicts with canonical meaning and redesign was not requested, the downstream mechanism adapts.

## Context stopping rule

Once sufficient authoritative context is loaded to perform the task safely, stop expanding context unless a concrete unresolved dependency remains.

# MUDAC Repository Agent Rules

This file is a **bootstrap adapter**, not the canonical source of MUDAC product, architecture, implementation, verification, source-topology, or documentation rules.

Canonical governance lives under [`docs/canonical/governance/`](docs/canonical/governance/).

## Required start

1. Start at [`docs/index.md`](docs/index.md).
2. For current product/UX/governance/accepted architecture/accepted implementation meaning, use [`docs/canonical/`](docs/canonical/).
3. For architecture work, load the relevant owner(s) under [`docs/canonical/architecture/`](docs/canonical/architecture/) plus only the upstream canonical constraints materially relevant to the decision.
4. For implementation work, load the relevant owner(s) under [`docs/canonical/implementation/`](docs/canonical/implementation/), the architecture owner(s) they realize, and only the upstream product/UX/governance constraints materially relevant to the task.
5. For verification/test work, additionally load [`Verification Strategy, Evidence & Quality Gates`](docs/canonical/implementation/verification-strategy.md) and trace evidence to the existing canonical stable rule IDs being proven rather than copying their rule bodies into tests or fixtures.
6. For source/package/import/dependency work, additionally load [`Source Topology, Package Boundaries & Dependency Enforcement`](docs/canonical/implementation/source-topology.md). Do not infer package layout from `docs/` or create new shared packages to escape an ownership conflict.
7. Read only the category/owner documents materially relevant to the task.
8. Follow stable rule IDs and linked dependencies as needed.
9. Use numbered phase history only for rationale, chronology, rejected alternatives, implementation planning lineage, or source audit.

Governed by:

- [`DOC-*` — Documentation Authority](docs/canonical/governance/documentation-authority.md)
- [`CTX-*` — Agent Context](docs/canonical/governance/agent-context.md)
- [`CHG-*` — Canonical Change & Conflict Governance](docs/canonical/governance/change-governance.md)
- [`META-*` — OKF Metadata, Trust, Lifecycle & Freshness](docs/canonical/governance/metadata-trust-lifecycle.md)
- [`VAL-*` — Knowledge Validation & CI Enforcement](docs/canonical/governance/validation-enforcement.md)
- [`ARCH-*` — Architectural Foundation](docs/canonical/architecture/architectural-foundation.md)
- [`IMPL-*` — Implementation Authority, Toolchain & Delivery Governance](docs/canonical/implementation/implementation-foundation.md)
- [Verification Strategy, Evidence & Quality Gates](docs/canonical/implementation/verification-strategy.md)
- [Source Topology, Package Boundaries & Dependency Enforcement](docs/canonical/implementation/source-topology.md)
- [Stable Rule Identifiers](docs/canonical/governance/rule-identifiers.md)
- [Source Lineage](docs/canonical/governance/source-lineage.md)

## Do not

- recursively preload all of `docs/` for ordinary work;
- reconstruct current rules from Phase 001–005 when a canonical owner exists;
- copy complete canonical rules into architecture/implementation/test documents when a link/stable ID plus local consequence is sufficient;
- let README/index/traceability/agent/test-fixture files become competing rule stores;
- silently resolve canonical contradictions by choosing convenient wording;
- rewrite historical phase decisions to match later truth;
- change product semantics only in code, architecture, tests, migrations, IaC, generated schemas, or comments;
- infer source-code package/service/database structure from the knowledge-directory layout;
- create new MUDAC Concepts merely because a subject has its own OKF document;
- create a package per Concept/table/command/screen/document merely because the subject is independently named;
- create `common`, `shared-domain`, `services`, `models`, or central infrastructure packages to bypass an ownership/dependency problem;
- deep-import another workspace package's private source, repository, table/query model, adapter, test helper, or internal service;
- let browser code import server module/application/persistence implementation merely for type reuse;
- fabricate `generated`, `verified`, source credibility, or `stale_after` metadata for cosmetic completeness;
- treat CI, coverage percentage, snapshots, scanners, or validator conformance as semantic verification or production certification;
- select or replace implementation technology without identifying the upstream architecture constraint and implementation need that justify it;
- let Fastify routes/plugins, Kysely query models, OpenAPI DTOs, React components, OpenTofu modules, mocks, fixtures, or golden snapshots become alternate owners of domain semantics;
- substitute SQLite/in-memory persistence evidence for real PostgreSQL when behavior depends on PostgreSQL constraints, transactions, locking, migrations, or concurrency;
- hide flaky consequential tests behind automatic retries or indefinite quarantine.

## Canonical changes

If the human explicitly asks to change MUDAC design meaning, follow [`Canonical Change & Conflict Governance`](docs/canonical/governance/change-governance.md): update the canonical owner, preserve rationale/source lineage, review stable-rule compatibility/dependents, and keep history reconstructible.

If implementation, test behavior, source layout, or architecture conflicts with canonical meaning and no redesign was requested, the downstream mechanism must adapt.

Meaningful edits to OKF concept/architecture/implementation documents follow the [`META-*` profile](docs/canonical/governance/metadata-trust-lifecycle.md): record real generation provenance prospectively, preserve only verification that actually covers current content, and keep lifecycle/freshness metadata semantically accurate.

## Implementation baseline

Current implementation family is governed by [`IMPL-*`](docs/canonical/implementation/implementation-foundation.md): Node.js 24 LTS + TypeScript, pnpm workspaces, Fastify as the server transport host, Kysely + node-postgres for PostgreSQL adapters, explicit migrations, transport schemas that generate OpenAPI outward, Vitest/Playwright verification families, strict TypeScript + ESLint + Prettier, and OpenTofu for persistent AWS IaC.

Verification is governed by [`Verification Strategy, Evidence & Quality Gates`](docs/canonical/implementation/verification-strategy.md): use the smallest trustworthy evidence layer, real PostgreSQL where its semantics matter, deterministic synthetic fixtures/fakes, Testing Library/Playwright/axe/manual accessibility evidence as appropriate, explicit security/concurrency/recovery evidence, diagnostic rather than oracle-style coverage, and privacy-minimized artifacts. Verification traces existing canonical stable rule IDs; it intentionally does not create a parallel normative rule namespace.

Source/package boundaries are governed by [`Source Topology, Package Boundaries & Dependency Enforcement`](docs/canonical/implementation/source-topology.md): `apps/api`, `apps/worker`, and `apps/web` are composition roots; six authoritative server modules are separate workspace packages; cross-module coordination/projections/shared foundation have bounded roles; package-root exports are explicit; internal workspace dependencies use pnpm `workspace:` declarations; browser/server and test/production boundaries remain isolated; and dependency-cruiser is the graph-level enforcement mechanism once 006-D instantiates executable tooling.

Exact package versions are pinned in implementation manifests/lockfiles when introduced and are not permanent canonical semantics. Exact database/API/browser implementation details remain owned by their later Phase 006 groups.

## Validation

After changes to governed knowledge, routing, rule IDs, validation tooling, or related documentation, run:

```text
python -m pip install -r requirements-docs.txt
python scripts/validate_knowledge.py
```

As implementation tooling is introduced, run the applicable type/lint/test/security/generated-code/dependency checks defined by `IMPL-*`, the current verification owner, and the source-topology owner.

The validator checks deterministic knowledge structure only. A passing result is **not** an OKF `verified` event and does not replace semantic/design review.

## Context stopping rule

Once sufficient authoritative context has been loaded to perform the scoped task safely, stop expanding documentation context unless a concrete unresolved dependency remains.

Future Cursor/IDE/tool-specific agent rules may point to this file and canonical governance, but they must not fork or override it.

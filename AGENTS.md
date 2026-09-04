# MUDAC Repository Agent Rules

This file is a **bootstrap adapter**, not the canonical source of MUDAC product, architecture, implementation, or documentation rules.

Canonical governance lives under [`docs/canonical/governance/`](docs/canonical/governance/).

## Required start

1. Start at [`docs/index.md`](docs/index.md).
2. For current product/UX/governance/accepted architecture/accepted implementation meaning, use [`docs/canonical/`](docs/canonical/).
3. For architecture work, load the relevant owner(s) under [`docs/canonical/architecture/`](docs/canonical/architecture/) plus only the upstream canonical constraints materially relevant to the decision.
4. For implementation work, load the relevant owner(s) under [`docs/canonical/implementation/`](docs/canonical/implementation/), the architecture owner(s) they realize, and only the upstream product/UX/governance constraints materially relevant to the task.
5. Read only the category/owner documents materially relevant to the task.
6. Follow stable rule IDs and linked dependencies as needed.
7. Use numbered phase history only for rationale, chronology, rejected alternatives, implementation planning lineage, or source audit.

Governed by:

- [`DOC-*` — Documentation Authority](docs/canonical/governance/documentation-authority.md)
- [`CTX-*` — Agent Context](docs/canonical/governance/agent-context.md)
- [`CHG-*` — Canonical Change & Conflict Governance](docs/canonical/governance/change-governance.md)
- [`META-*` — OKF Metadata, Trust, Lifecycle & Freshness](docs/canonical/governance/metadata-trust-lifecycle.md)
- [`VAL-*` — Knowledge Validation & CI Enforcement](docs/canonical/governance/validation-enforcement.md)
- [`ARCH-*` — Architectural Foundation](docs/canonical/architecture/architectural-foundation.md)
- [`IMPL-*` — Implementation Authority, Toolchain & Delivery Governance](docs/canonical/implementation/implementation-foundation.md)
- [Stable Rule Identifiers](docs/canonical/governance/rule-identifiers.md)
- [Source Lineage](docs/canonical/governance/source-lineage.md)

## Do not

- recursively preload all of `docs/` for ordinary work;
- reconstruct current rules from Phase 001–005 when a canonical owner exists;
- copy complete canonical rules into architecture/implementation documents when a link/stable ID plus local consequence is sufficient;
- let README/index/traceability/agent files become competing rule stores;
- silently resolve canonical contradictions by choosing convenient wording;
- rewrite historical phase decisions to match later truth;
- change product semantics only in code, architecture, tests, migrations, IaC, generated schemas, or comments;
- infer source-code package/service/database structure from the knowledge-directory layout;
- create new MUDAC Concepts merely because a subject has its own OKF document;
- fabricate `generated`, `verified`, source credibility, or `stale_after` metadata for cosmetic completeness;
- treat CI or validator conformance as semantic verification;
- select or replace implementation technology without identifying the upstream architecture constraint and implementation need that justify it;
- let Fastify routes/plugins, Kysely query models, OpenAPI DTOs, React components, or OpenTofu modules become alternate owners of domain semantics.

## Canonical changes

If the human explicitly asks to change MUDAC design meaning, follow [`Canonical Change & Conflict Governance`](docs/canonical/governance/change-governance.md): update the canonical owner, preserve rationale/source lineage, review stable-rule compatibility/dependents, and keep history reconstructible.

If implementation or architecture conflicts with canonical meaning and no redesign was requested, the downstream mechanism must adapt.

Meaningful edits to OKF concept/architecture/implementation documents follow the [`META-*` profile](docs/canonical/governance/metadata-trust-lifecycle.md): record real generation provenance prospectively, preserve only verification that actually covers current content, and keep lifecycle/freshness metadata semantically accurate.

## Implementation baseline

Current implementation family is governed by [`IMPL-*`](docs/canonical/implementation/implementation-foundation.md): Node.js 24 LTS + TypeScript, pnpm workspaces, Fastify as the server transport host, Kysely + node-postgres for PostgreSQL adapters, explicit migrations, transport schemas that generate OpenAPI outward, Vitest/Playwright verification families, strict TypeScript + ESLint + Prettier, and OpenTofu for persistent AWS IaC.

Exact package/source topology is not implied by this bootstrap or the knowledge tree; Phase 006-C owns that boundary. Exact package versions are pinned in implementation manifests/lockfiles when introduced and are not permanent canonical semantics.

## Validation

After changes to governed knowledge, routing, rule IDs, validation tooling, or related documentation, run:

```text
python -m pip install -r requirements-docs.txt
python scripts/validate_knowledge.py
```

As implementation tooling is introduced, run the applicable type/lint/test/security/generated-code checks defined by `IMPL-*` and the current Phase 006 verification owner.

The validator checks deterministic knowledge structure only. A passing result is **not** an OKF `verified` event and does not replace semantic/design review.

## Context stopping rule

Once sufficient authoritative context has been loaded to perform the scoped task safely, stop expanding documentation context unless a concrete unresolved dependency remains.

Future Cursor/IDE/tool-specific agent rules may point to this file and canonical governance, but they must not fork or override it.

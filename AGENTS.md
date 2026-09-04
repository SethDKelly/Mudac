# MUDAC Repository Agent Rules

This file is a **bootstrap adapter**, not the canonical source of MUDAC product or documentation rules.

Canonical governance lives under [`docs/canonical/governance/`](docs/canonical/governance/).

## Required start

1. Start at [`docs/index.md`](docs/index.md).
2. For current product/UX meaning, use [`docs/canonical/`](docs/canonical/).
3. Read only the category/owner documents materially relevant to the task.
4. Follow stable rule IDs and linked dependencies as needed.
5. Use numbered phase history only for rationale, chronology, rejected alternatives, or source audit.

Governed by:

- [`DOC-*` — Documentation Authority](docs/canonical/governance/documentation-authority.md)
- [`CTX-*` — Agent Context](docs/canonical/governance/agent-context.md)
- [`CHG-*` — Canonical Change & Conflict Governance](docs/canonical/governance/change-governance.md)
- [Stable Rule Identifiers](docs/canonical/governance/rule-identifiers.md)
- [Source Lineage](docs/canonical/governance/source-lineage.md)

## Do not

- recursively preload all of `docs/` for ordinary work;
- reconstruct current rules from Phase 001–003 when a canonical owner exists;
- copy complete canonical rules into architecture/implementation documents when a link/stable ID plus local consequence is sufficient;
- let README/index/traceability/agent files become competing rule stores;
- silently resolve canonical contradictions by choosing convenient wording;
- rewrite historical phase decisions to match later truth;
- change product semantics only in code, architecture, tests, or comments;
- infer source-code package/service/database structure from the knowledge-directory layout;
- create new MUDAC Concepts merely because a subject has its own OKF document.

## Canonical changes

If the human explicitly asks to change MUDAC design meaning, follow [`Canonical Change & Conflict Governance`](docs/canonical/governance/change-governance.md): update the canonical owner, preserve rationale/source lineage, review stable-rule compatibility/dependents, and keep history reconstructible.

If implementation conflicts with canonical meaning and no redesign was requested, the implementation must adapt.

## Context stopping rule

Once sufficient authoritative context has been loaded to perform the scoped task safely, stop expanding documentation context unless a concrete unresolved dependency remains.

Future Cursor/IDE/tool-specific agent rules may point to this file and canonical governance, but they must not fork or override it.
---
name: resolve-context
description: Resolve the minimum authoritative MUDAC repository context for a human-selected task. Use when current status, scope, owner, stable rule, or governing contract is unclear. Read-only.
---
# Resolve context

## Human-directed boundary

This workflow is **A1**. Retrieval does not authorize edits or follow-on work.

## Workflow

1. Identify the human-selected objective, requested action and explicit exclusions.
2. Read root `AGENTS.md` and current lifecycle status only as needed.
3. If an exact stable ID is known, run `python scripts/resolve_stable_id.py <ID>`.
4. Otherwise route through `docs/index.md` to the smallest relevant current family and owner.
5. Apply the T0–T5 retrieval tiers in `docs/canonical/governance/agent-context.md`.
6. Load another current owner only for a concrete unresolved dependency.
7. Load history, deprecated adapters, candidates or external evidence only when the task explicitly needs that tier.
8. Return the minimum context set, unresolved assumptions and any A3/A4 escalation.

## Stop conditions

Stop rather than guess when current authority cannot be resolved, required routing is broken, owners materially conflict, or the task requires ungranted A3/A4 authority. Do not edit repository files.

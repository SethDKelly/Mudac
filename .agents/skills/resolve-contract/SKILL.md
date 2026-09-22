---
name: resolve-contract
description: Resolve an exact MUDAC stable rule ID or tightly bounded semantic question to its current authored owner and minimum surrounding context. Read-only.
---
# Resolve contract

## Human-directed boundary

This workflow is **A1**. It locates authority; it does not create or modify authority.

## Workflow

1. Preserve the exact ID/question without broadening it.
2. For a stable ID, run `python scripts/resolve_stable_id.py <ID>`.
3. Use `--include-candidates` or `--include-deprecated` only when the human-selected task explicitly requires non-current material.
4. Use `--history` only for provenance/rationale work.
5. Read the smallest surrounding current owner section needed to understand the rule and material relationships.
6. If no ID is known, route through `docs/index.md`, identify the relevant owner/rule, then resolve exactly.
7. Distinguish current authority from generated routing, candidate material, historical text, examples and model memory.

## Stop conditions

Do not invent IDs, use first search match as authority, or treat candidate/history as current. Do not edit repository files.

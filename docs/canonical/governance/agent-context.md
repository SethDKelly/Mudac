---
type: Documentation Authority
title: Agent Context & Progressive Retrieval
description: Defines the minimum-sufficient context loading, progressive disclosure, historical retrieval, and anti-bloat behavior required of repository agents.
status: stable
tags: [governance, agents, context, retrieval, anti-bloat]
sources:
  - resource: ../../004-knowledge-architecture/004-B-knowledge-bundle-topology-canonical-authority-layers-progressive-disclosure.md
  - resource: ../../004-knowledge-architecture/004-D-historical-phase-migration-provenance-source-lineage-retrofit.md
  - resource: ../../004-knowledge-architecture/004-E-cross-reference-stable-rule-id-restatement-reduction-retrofit.md
  - resource: ../../004-knowledge-architecture/004-F-documentation-governance-agent-context-anti-drift-rules.md
---

# Purpose

Give agents enough authoritative context to act correctly while preventing recursive corpus loading, historical reconstruction of already-canonical meaning, and context growth that increases cost or contradiction risk without improving the task.

<a id="ctx-001"></a>
## CTX-001 — Start with progressive disclosure

For repository work, begin with the smallest routing path that can identify current authority:

```text
AGENTS.md
    ↓
docs/index.md
    ↓
relevant canonical category/index
    ↓
target owner(s)
```

Do not begin ordinary work by recursively scanning the numbered phase corpus.

<a id="ctx-002"></a>
## CTX-002 — Load only task-relevant owners and dependencies

After identifying the target owner, load only the linked Concepts, mechanisms, policies, invariants, experience contracts, governance rules, or architecture contracts whose meaning materially affects the task.

Shared phase origin or vocabulary mention is not sufficient reason to load another document.

<a id="ctx-003"></a>
## CTX-003 — Historical context is on-demand through lineage

Use history when the task requires rationale, chronology, rejected alternatives, comparison with prior design, or audit of the canonical extraction.

Prefer a canonical owner's material `sources` links. If starting from history, enter through the phase `index.md` and follow the relevant record/current-successor mapping.

Do not follow every source edge merely because it exists.

<a id="ctx-004"></a>
## CTX-004 — Stop context expansion when authority is sufficient

Once the agent has enough authoritative current knowledge to answer or perform the scoped task safely, it should stop loading additional documentation unless a concrete unresolved dependency remains.

More context is not automatically better context.

<a id="ctx-005"></a>
## CTX-005 — Recursive corpus loading is not the default

Agents must not routinely load:

- all of `docs/`;
- all canonical categories;
- all of Phase 001–003;
- every historical source of every canonical dependency;
- all documents containing the same noun.

Broad corpus review is appropriate only when the task itself is broad—for example repository-wide drift audit, phase consolidation, or authority migration.

# Task profiles

## Current product/design question

Use the specific canonical owner(s). Load history only if rationale is requested or a contradiction is suspected.

## Architecture/implementation work

Load the relevant canonical owners and exact stable rules the design must satisfy. Add historical context only when the architecture decision depends on original rationale/tradeoffs.

## Canonical change

Load [Documentation Authority](documentation-authority.md), [Canonical Change & Conflict Governance](change-governance.md), the target owner, applicable stable rules, material sources when semantics may change, and known dependents.

## Historical analysis

Start from the current owner where possible, then follow only the material lineage needed to answer the historical question.

# Summarization discipline

An agent may internally summarize loaded authority for working context, but a new repository artifact should not be created merely to persist that summary unless it has a genuine independent ownership purpose.

When writing downstream documentation, use links/stable IDs plus local consequences instead of embedding a context pack.

# Tool-specific adapters

`AGENTS.md` and future IDE-specific rules are bootstrap adapters. They should remain small enough to read on every task and point to this canonical contract rather than copying it.
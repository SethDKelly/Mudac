---
type: Design Phase Record
title: 004-F — Documentation Governance, Agent Context & Anti-Drift Rules
description: Establish repository operating rules for documentation authority, agent context loading, canonical change governance, and anti-drift behavior.
status: stable
tags: [phase-004, governance, agents, anti-drift, context]
sources:
  - resource: 004-A-okf-adoption-authority-methodology-compatibility-terminology-contract.md
  - resource: 004-B-knowledge-bundle-topology-canonical-authority-layers-progressive-disclosure.md
  - resource: 004-C-canonical-concept-policy-invariant-experience-knowledge-extraction.md
  - resource: 004-D-historical-phase-migration-provenance-source-lineage-retrofit.md
  - resource: 004-E-cross-reference-stable-rule-id-restatement-reduction-retrofit.md
---

# Purpose

004-F turns the knowledge architecture established in 004-A through 004-E into repository operating law for humans and software agents.

The governing objective is:

> Give future design, architecture, implementation, and agent work enough authoritative context to act correctly without recursively loading the repository, duplicating canonical rules, silently rewriting design history, or allowing downstream artifacts to drift into competing sources of truth.

004-F creates canonical governance owners for methodology/terminology, documentation authority, agent context loading, and canonical change governance. It also adds a root `AGENTS.md` as a thin repository adapter that routes agents into those canonical owners rather than duplicating them.

# 1. Governance layers

MUDAC now distinguishes:

```text
methodology / terminology governance
        ↓
documentation authority
        ↓
canonical current knowledge
        ↓
architecture / implementation / tests
```

Historical phase records remain a provenance/rationale layer and do not compete with canonical current owners.

Repository landing pages, indexes, traceability tables, `AGENTS.md`, future tool-specific agent rules, code comments, and tests may reference canonical authority. They do not acquire authority merely by repeating it.

# 2. Explicit human instruction and repository authority

A human request determines the task to perform. It does not silently change existing MUDAC semantics merely because the requested implementation would be easier under a different rule.

If a human explicitly asks to change product/design meaning, the change is performed through the canonical-change workflow defined by 004-F: identify the canonical owner, preserve rationale/source lineage, review stable-rule compatibility and dependents, update current authority, and keep history reconstructible.

If the task is ordinary architecture or implementation work, canonical product/UX rules remain constraints.

# 3. Authority precedence

For current MUDAC meaning, the preferred authority order is:

```text
canonical governance
        ↓
canonical Concepts / mechanisms / policies / invariants / experience
        ↓
accepted architecture contracts
        ↓
implementation / tests / operational docs
```

Historical phase records explain how current meaning was reached. They are consulted for rationale, chronology, rejected alternatives, or audit rather than used as a convenient competing current-rule source.

When a canonical owner exists, a README, phase summary, generated artifact, implementation document, source-code comment, or test cannot override that owner by restating the rule differently.

# 4. One-owner anti-drift rule

Normative meaning should have one canonical owner.

Dependent knowledge:

1. links to the owner or stable rule ID;
2. states only the local consequence required by its purpose;
3. avoids copying the full normative body;
4. uses bounded restatement only where independent auditability or necessary comprehension requires it.

Indexes summarize/rout; they do not become additional rule stores.

# 5. Agent bootstrap contract

Repository agents begin with the smallest sufficient authority path:

```text
AGENTS.md
    ↓
docs/index.md
    ↓
relevant canonical category index
    ↓
target canonical owner(s)
    ↓
linked rule/dependency only as needed
```

Agents do not recursively preload `docs/`, Phase 001–003, or the entire canonical tree.

The normal context-expansion rule is demand-driven: load another document only when the current task depends on meaning owned there.

# 6. Task-specific retrieval

## Current meaning or product question

Use the relevant canonical owner(s). Historical sources are unnecessary unless rationale is requested or the canonical extraction is being audited.

## Architecture or implementation design

Load the relevant canonical owner(s), stable rule IDs, and applicable experience/policy/invariant dependencies. Do not load unrelated Concepts merely because they share the same phase history.

## Historical rationale

Begin from the current canonical owner and follow its material `sources`, or enter a historical phase through that phase's `index.md`. Do not recursively load the whole chronology.

## Canonical edit

Load the target owner, relevant governance, its material sources when semantics may change, and known dependents/stable-rule references.

## Historical record edit

Treat the record as append-stable evidence. Narrow typo/link corrections are allowed; later truth is not back-written over an earlier decision.

# 7. Context-budget discipline

Agents must stop expanding context when they have sufficient authoritative material to complete the task safely.

More context is not automatically better context.

Prohibited default behaviors include:

- recursively reading every phase before ordinary work;
- loading all canonical categories for a narrow task;
- following every `sources` edge when rationale is not needed;
- treating all documents that mention a noun as equally authoritative;
- copying large upstream rule blocks into downstream artifacts “for context.”

A downstream document should be independently understandable through concise local consequence plus links—not through corpus duplication.

# 8. Agentic bloat controls

Agents must not create new documentation solely because a concept/rule is mentioned frequently.

A new canonical document requires a genuine independently retrievable owner boundary. A new phase record requires actual design/decision work, not a prose mirror of already canonical rules.

Agents must not create:

- umbrella summaries that restate the canonical corpus and then become de facto authority;
- parallel “current rules” under phase directories;
- technology-specific copies of product rules;
- separate agent rule sets that redefine canonical governance;
- exhaustive context packs when progressive disclosure is sufficient;
- new MUDAC Concepts merely because OKF has a knowledge document for a subject.

# 9. Architecture-option auditability

Reference-first documentation does not forbid local explanation.

An architecture option may briefly restate a canonical rule when the option must be independently auditable, but it must link the owner/stable ID and make clear that the local prose is a consequence/restatement rather than a new authority.

Preferred pattern:

```text
Constraint: INV-010 — Truthful Authority Under Uncertainty.
Local consequence: this protocol cannot acknowledge Finalization until authoritative persistence is confirmed.
```

The architecture document should not copy the entire invariant and Scorecard lifecycle.

# 10. Canonical change classification

Before editing canonical meaning, classify the proposed change as:

### Editorial

Wording, organization, typo, link, or explanatory clarification that preserves semantics.

### Compatible semantic refinement

Adds precision without invalidating the existing contract. Stable rule IDs may remain when their meaning stays compatible.

### Material semantic change

Changes an accepted behavior, boundary, authority, lifecycle, policy, invariant, or experience contract. This requires explicit design/refinement rationale and dependent impact review; incompatible stable rules receive new IDs rather than silently changing old meanings.

# 11. Canonical change workflow

A semantic canonical change requires:

1. identify the canonical owner;
2. identify the human/design intent authorizing the change;
3. inspect material historical sources when needed to understand the existing rationale;
4. classify stable-rule compatibility;
5. update the canonical owner rather than a downstream copy;
6. update/add material `sources` lineage for the new rationale/refinement;
7. review known canonical dependents and later architecture/tests citing affected stable IDs;
8. update routing/indexes when ownership or discoverability changes;
9. preserve historical decisions rather than rewriting them to match the new result.

Future automated checks support this workflow but do not replace semantic review.

# 12. Conflict handling

## Canonical versus historical

Canonical current meaning normally governs. If the historical source suggests the canonical extraction is wrong or incomplete, treat that as a documentation defect to investigate—not permission to choose whichever wording is convenient.

## Canonical versus canonical

Do not silently pick one or merge them by intuition. Surface the contradiction, identify the intended owner, and resolve it through explicit design/refinement before downstream work relies on the disputed rule.

## Canonical versus implementation

Canonical meaning governs unless a human explicitly chooses to redesign the product. Implementation must adapt, or the design must be deliberately changed through the canonical-change workflow.

## Human requested design change versus current canonical

The human request authorizes the design change, but the agent must update current authority and lineage rather than leaving the repository internally contradictory.

# 13. Stable-rule impact review

A semantic change to an identified rule triggers review of known dependents.

At minimum ask:

- Is the existing ID still semantically compatible?
- Which canonical documents link this ID?
- Which architecture documents or tests cite it?
- Does the change alter source lineage?
- Is a successor/new rule ID required?
- Does any bounded restatement now need revision?

IDs are never reused for incompatible meaning.

# 14. Write-scope discipline

Agents should make the smallest set of repository changes that leaves authority coherent.

A canonical semantic change may require owner, lineage, registry, dependent, index, and phase-record updates. An unrelated README rewrite is not automatically justified.

Conversely, “small diff” is not a reason to leave a known authority mismatch unresolved.

# 15. History preservation

Historical Phase 001–004 records remain append-stable design evidence.

Later work may add lineage/index links or narrow corrections, but semantic evolution is recorded through later refinement/current canonical knowledge instead of rewriting the original record as though earlier reasoning never existed.

# 16. Tool-specific agent adapters

`AGENTS.md` is a repository adapter, not canonical authority.

Future Cursor rules, IDE instructions, CI hints, or other agent-tool adapters may be added when useful, but they must:

- route to the same canonical governance;
- remain concise;
- not fork the rule set;
- not copy the full product corpus;
- not claim higher authority than canonical MUDAC knowledge.

This prevents tool configuration from becoming another drifting documentation layer.

# 17. New governance namespaces

004-F introduces stable governance rules:

```text
DOC-*  documentation authority / ownership
CTX-*  agent retrieval and context-budget discipline
CHG-*  canonical change and conflict governance
```

The identifiers are registered in the canonical rule-ID registry and owned by their respective governance documents.

# 18. Findings

004-F found no need to change the 15-Concept catalog or any product/UX rule.

The largest drift risks were structural rather than semantic:

- treating README/index summaries as interchangeable with canonical owners;
- recursive agent loading of historical phases;
- duplicating product rules into architecture documents;
- allowing implementation mismatch to redefine design implicitly;
- changing a stable rule without reviewing dependents;
- tool-specific agent instructions becoming a parallel authority layer.

The governance contracts directly address those risks.

# Deliberate deferrals

004-F does not finalize:

- OKF `generated`, `verified`, status/lifecycle, and freshness conventions — 004-G;
- automated metadata/link/rule-ID/dependency validation — 004-H;
- repository-wide final drift audit and migration closure — 004-I.

# Exit position

MUDAC now has explicit rules for what current authority is, how agents retrieve only the context they need, how canonical knowledge changes, how conflicts are handled, and how future architecture/implementation avoids recreating the documentation-drift problem Phase 004 was introduced to solve.

004-F passes governance/agent-context review and hands off to **004-G — OKF Metadata, Trust, Verification, Lifecycle & Freshness Conventions**.
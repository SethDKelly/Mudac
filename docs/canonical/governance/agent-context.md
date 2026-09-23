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
  - resource: ../../020-autonomous-implementation-program-design-verification-v1-delivery/020-C-cursor-codex-roles-work-isolation-context-provenance-autonomy-circuit-breakers.md
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

<a id="ctx-006"></a>
## CTX-006 — Resolve a known stable ID directly before broad discovery

When a task already supplies an exact stable rule ID, use the deterministic stable-ID resolver rather than loading the full rule registry, scanning all canonical files, or ranking search results.

Default resolution is current-authority only. Candidate, deprecated-adapter and numbered-phase evidence require explicit non-current/provenance modes under [Deterministic Ownership, Stable Reference Resolution & Drift Control](deterministic-ownership-resolution.md).

The resolver returns a locator; load only the smallest surrounding owner context needed to apply the rule.

<a id="ctx-007"></a>
## CTX-007 — Minimum sufficient authoritative context is the retrieval objective

Context quality is measured by whether the agent has the smallest authoritative set needed to complete the selected task safely—not by how much repository material it can fit into a model window.

Additional context requires a concrete unresolved dependency, provenance need, candidate-comparison need, or external-evidence need.

<a id="ctx-008"></a>
## CTX-008 — Retrieval expands through explicit tiers

Use the following tier order:

~~~text
T0  bootstrap adapter
    AGENTS.md

T1  deterministic routing
    known ID → resolver
    unknown subject → docs/index.md → smallest family index

T2  current owner
    smallest current canonical owner that controls the task

T3  linked current dependency
    only when an unresolved dependency materially affects the task

T4  provenance / deprecated adapter / downstream candidate
    only when the task explicitly needs rationale, comparison, audit or re-entry evidence

T5  external/provider evidence
    only when the task depends on current external mechanics or factual compatibility
~~~

Ordinary current-semantic work should normally stop at T2 or T3.

<a id="ctx-009"></a>
## CTX-009 — Hard byte budgets govern routinely loaded routing surfaces, not canonical truth

Persistent/bootstrap and routing surfaces have deterministic UTF-8 byte envelopes defined by `docs/routing/context_budget.json`.

Substantive canonical owners are not truncated merely to fit those envelopes. If a canonical owner is large, improve routing, use exact stable-ID lookup, or decompose the task rather than duplicating or weakening the owner.

<a id="ctx-010"></a>
## CTX-010 — Representative current-task packs are measured as regression evidence

The context-budget validator measures representative current-rule, single-family, cross-owner and governance task packs.

These packs are regression tests for retrieval architecture, not claims that every future task must contain exactly those files.

Provider tokenization is intentionally not used for blocking CI because UTF-8 bytes are deterministic across repository tooling.

<a id="ctx-011"></a>
## CTX-011 — Cross-owner expansion requires an unresolved semantic dependency

Do not add another current owner because it shares vocabulary, phase ancestry, tags, or search proximity.

Expand from T2 to T3 only when the current owner links or the task itself exposes a material dependency that cannot be safely resolved locally.

<a id="ctx-012"></a>
## CTX-012 — History, quarantined candidates and external evidence are explicit extended-context tiers

Numbered-phase history, deprecated adapters, suspended Architecture/Implementation candidates and external/vendor material are excluded from ordinary startup/current-task context.

Load them only when the selected task requires provenance, historical comparison, post-closure candidate qualification, external compatibility, or other explicit evidence.

<a id="ctx-013"></a>
## CTX-013 — Assembled context packs are ephemeral unless they have independent ownership purpose

An agent may assemble a temporary working set of routes, owners, stable IDs and evidence.

Do not persist that working set as another repository summary merely to make a future agent preload it. Persist durable rules in their natural owner and persist reusable procedures only when they have a real independent workflow purpose.

A future implementation **work-unit context manifest** is an allowed operational artifact because it records the authorized task envelope, exact base revision, authority references, owned surfaces, evidence obligations, external-action permissions and circuit breakers. It must reference current owners/rules rather than copying their normative prose and becoming a shadow authority store.

<a id="ctx-014"></a>
## CTX-014 — Budget pressure is resolved by routing or task decomposition, never semantic truncation

When a hard routing/task-pack budget is exceeded:

1. remove duplicated bootstrap/restatement material;
2. replace broad loading with stable-ID or family routing;
3. split a genuinely broad task into dependency-safe parts when appropriate;
4. keep required canonical meaning intact.

A context limit is never permission to omit a material rule from the work that depends on it.

<a id="ctx-015"></a>
## CTX-015 — Larger model context windows do not justify routine context growth

A provider supporting a larger context window may improve exceptional-task capacity, but it does not change MUDAC retrieval discipline.

Routine context remains minimum-sufficient because unnecessary context increases retrieval cost, contradiction exposure and authority confusion even when it technically fits.

<a id="ctx-016"></a>
## CTX-016 — Broad-audit context is task-scoped and temporary

Repository-wide audits, topology migrations and methodology reconciliations may legitimately exceed ordinary current-task packs.

The broad scope must come from the selected task itself. Once that task ends, the expanded corpus is not converted into a new always-loaded context baseline.

# Context budget measurement

Deterministic measurement is performed with:

~~~bash
python scripts/measure_context_budget.py
~~~

Hard limits cover startup/routing/procedure surfaces and representative task packs. Canonical-owner size above the informational review threshold is not itself a failure.

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

# Autonomous implementation context discipline

A Coordinator hands an Implementer a compact work-unit context manifest, not a dump of repository history.

The Implementer still resolves current authority through the normal CTX tiers and loads only material dependencies.

Independent Reviewers begin from the phase/package/work-unit contract, exact base/head diff, relevant current owners and evidence outputs. They must not rely solely on the Implementer's summary or provider conversation memory.

Technical run/session history may support diagnosis, but it is not canonical meaning and private model reasoning is never required as repository evidence.

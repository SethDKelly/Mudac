---
type: Phase Qualification
title: 018-F — Agent Context, Progressive Retrieval, Context-Budget & Anti-Bloat Architecture
description: "Defines tiered progressive retrieval, minimum-sufficient authoritative context, deterministic UTF-8 byte budgets for startup/routing surfaces, representative current-task context packs, explicit extended-context tiers for history/candidates/external evidence, ephemeral context-pack rules, and CI measurement that prevents agentic context bloat without truncating canonical semantics."
status: stable
tags: [phase-018, agents, context, progressive-retrieval, context-budget, anti-bloat, measurement]
sources:
  - resource: 018-E-agentic-development-authority-human-directed-scope-change-classes-safety-boundaries.md
  - resource: ../canonical/governance/agent-context.md
  - resource: ../canonical/governance/deterministic-ownership-resolution.md
  - resource: ../routing/context_budget.json
  - resource: ../../scripts/measure_context_budget.py
  - resource: ../../AGENTS.md
generated: { by: openai/gpt-5.6-sol, at: 2026-09-22T03:21:00Z }
---

# Purpose

018-F makes MUDAC's progressive-retrieval policy measurable.

The objective is not to minimize documentation volume. The objective is:

> **minimum sufficient authoritative context for the selected task.**

Historical evidence may remain large. Canonical owners may remain detailed. Agent startup and routing surfaces should remain small, deterministic and composable.

# 1. Retrieval tiers

018-F formalizes the following tier model:

~~~text
T0  bootstrap
    AGENTS.md

T1  deterministic routing
    known ID → stable-ID resolver
    unknown subject → docs/index.md → smallest family index

T2  current owner
    smallest current canonical owner controlling the task

T3  linked current dependency
    only for a concrete unresolved dependency

T4  provenance / deprecated adapter / downstream candidate
    explicit rationale, audit, comparison or re-entry need only

T5  external/provider evidence
    explicit current compatibility/mechanics need only
~~~

Ordinary current-semantic work should normally stop at T2 or T3.

# 2. New canonical context rules

018-F adds CTX-007 through CTX-016 to Agent Context & Progressive Retrieval.

They establish:

- minimum-sufficient authoritative context as the goal;
- explicit retrieval tiers;
- byte budgets for routine routing surfaces rather than semantic owners;
- representative task-pack measurement;
- dependency-based cross-owner expansion;
- explicit extended-context tiers;
- ephemeral rather than persisted ad hoc context packs;
- routing/decomposition rather than semantic truncation under budget pressure;
- no routine context expansion merely because a provider supports a larger window;
- broad audit context as temporary and task-scoped.

# 3. Deterministic byte unit

Blocking context budgets use:

> **UTF-8 bytes**

rather than provider-specific tokens.

Reason:

- bytes are deterministic in repository CI;
- tokenization varies by provider/model/version;
- MUDAC is measuring repository-surface bloat, not claiming exact runtime prompt construction.

Provider-specific token/runtime observations may be added later as compatibility evidence without replacing byte-based repository limits.

# 4. Hard routing/startup budgets

018-F adds:

> docs/routing/context_budget.json

Current hard limits:

| Surface | Limit |
| --- | ---: |
| AGENTS.md | 8 KiB |
| docs/index.md | 8 KiB |
| docs/canonical/index.md | 5 KiB |
| one canonical family index | 6 KiB |
| knowledge/index.md | 4 KiB |
| one nested knowledge index | 6 KiB |
| one generated OKF routing concept | 4 KiB |
| one future canonical agent skill | 8 KiB |

These are intentionally conservative routing/procedure envelopes.

They are not size limits on substantive current semantic owners.

# 5. Representative task-pack budgets

018-F introduces deterministic regression packs rather than trying to model every future agent task.

| Profile | Measured | Limit |
| --- | ---: | ---: |
| known current small rule | 6,178 B | 16 KiB |
| known current governance rule | 17,544 B | 24 KiB |
| single-family current task | 20,863 B | 32 KiB |
| cross-owner current task | 38,547 B | 48 KiB |
| governance current task | 37,617 B | 48 KiB |

The packs demonstrate that common retrieval paths remain comfortably below their envelopes.

They are not instructions to load every listed file for every task.

# 6. Startup/routing measurements

At 018-F validation:

~~~text
AGENTS.md                  5,183 / 8,192 bytes
docs/index.md              5,320 / 8,192 bytes
docs/canonical/index.md    2,573 / 5,120 bytes
~~~

Canonical family indexes remain below the 6 KiB per-index envelope.

Generated OKF routing surfaces remain far below their corresponding limits.

# 7. Canonical owner size is not a hard budget

018-F intentionally does not fail CI merely because a substantive current owner exceeds a byte threshold.

The informational review threshold is:

> 32 KiB

At validation, one current owner exceeds it:

~~~text
docs/canonical/governance/rule-identifiers.md
37,713 bytes
~~~

That is not a failure because the registry is structured reference data and 018-D already provides direct stable-ID resolution so normal tasks do not need to preload it.

The correct response to a large owner is one of:

- deterministic lookup;
- better routing;
- natural semantic decomposition when justified;
- task decomposition.

The incorrect response is truncating canonical meaning.

# 8. Cross-owner expansion

A shared noun, tag, phase origin or search hit is not enough to load another owner.

T2 expands to T3 only when:

- the current owner contains a material dependency;
- the task explicitly spans the second owner;
- unresolved semantics cannot be safely handled from the current owner alone.

This prevents cross-category snowballing.

# 9. Extended-context tiers

The following remain excluded from normal startup/current-task context:

- numbered phase history;
- deprecated adapters;
- quarantined Architecture candidates;
- quarantined Implementation candidates;
- vendor/external documentation.

They are loaded only for explicit provenance, comparison, re-entry, compatibility or evidence needs.

018-F provides soft guidance of approximately 96 KiB for intentionally assembled history/candidate packs, but this is not a semantic truncation limit. Broad tasks may exceed it when the task itself genuinely requires broader evidence.

# 10. Context-pack anti-bloat rule

Temporary working context may be assembled during a task.

It should not automatically become a new checked-in "summary for future agents."

A persisted summary must have a real independent ownership/workflow purpose.

Otherwise durable knowledge remains in:

- natural canonical owners;
- stable IDs;
- indexes/routes;
- accepted procedure/skill artifacts.

This prevents every agent run from adding another layer of restated repository meaning.

# 11. Budget-failure behavior

When a hard budget fails:

1. remove duplicated routing/bootstrap prose;
2. replace broad loading with stable-ID/family routing;
3. decompose an overly broad task when appropriate;
4. preserve canonical meaning intact.

A context budget never authorizes omission of a material rule that the selected work depends on.

# 12. Machine measurement

018-F adds:

> scripts/measure_context_budget.py

It measures:

- persistent/bootstrap surfaces;
- canonical family indexes;
- generated OKF routing surfaces;
- future .agents/skills SKILL.md surfaces if present;
- representative current-task packs;
- informational large-current-owner observations.

It exits nonzero only for hard budget or required-surface failures.

# 13. CI integration

Knowledge Validation now runs:

~~~bash
python scripts/measure_context_budget.py
~~~

This turns context-bloat control into repository evidence rather than a style aspiration.

# 14. Validation evidence

Mechanics commit:

> 4ded3fe79be13c3219ff61071b6e5a8065e2e354

Knowledge Validation run:

> 35682811969 — **SUCCESS**

Results:

~~~text
authored knowledge validation     PASS
Markdown files                    337
frontmatter blocks                245
stable rule anchors               252
errors                            0
warnings                          0

generated OKF projection          PASS
owner inventory                   PASS
stable-reference index            PASS — 252 IDs
agentic authority policy          PASS
context budget measurement        PASS — 0 hard errors
stable-ID role smoke tests        PASS
~~~

# 15. Stable-reference impact

CTX-007 through CTX-016 add ten current governance rules.

Exit counts:

~~~text
stable IDs total                 252
current-authority IDs            110
downstream-candidate IDs         142
CTX IDs                           16
~~~

No candidate Architecture/Implementation rule changed authority.

# 16. Relationship to 018-G/H

018-F establishes the context economics that future tooling must obey.

018-G should create canonical skills and thin tool adapters within these envelopes.

018-H should then test the actual adapters, skills, status mirrors and conformance behavior.

018-F deliberately does not invent tool-specific prompt behavior before those adapters exist.

# 17. Gate evaluation

| Phase-018 gate | 018-F result |
| --- | --- |
| P18-G1 semantic preservation | PASS |
| P18-G2 current/history integrity | PASS |
| P18-G3 documentation economy | PASS |
| P18-G4 OKF qualification | PRESERVED |
| P18-G5 deterministic routing | PRESERVED |
| P18-G6 human-directed agent authority | PRESERVED |
| P18-G7 context proportionality | **PASS** |
| P18-G8 conformance proportionality | PARTIAL PASS — context measurement active; broader adapter/scenario conformance remains 018-H |
| P18-G10 architecture re-entry integrity | PASS |
| P18-G12 execution boundary | PASS |

# 18. Exit decision

**018-F — COMPLETE — PASS.**

At exit:

~~~text
retrieval tiers                   DEFINED
minimum-sufficient context        CANONICAL RULE
startup/routing byte budgets      ACTIVE
representative task budgets       ACTIVE
history/candidate loading         EXPLICIT ON-DEMAND
context-pack persistence          RESTRICTED
semantic truncation for budget    PROHIBITED
provider window as bloat excuse   PROHIBITED
context budget CI                 PASSING
feature implementation            NOT AUTHORIZED
~~~

The next authorized work is:

> **018-G — Agent Skills, Tool Adapters, Workflow Contracts & Cross-Agent Portability**

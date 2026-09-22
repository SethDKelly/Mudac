---
type: Phase Qualification
title: 018-G — Agent Skills, Tool Adapters, Workflow Contracts & Cross-Agent Portability
description: "Establishes one canonical portable workflow layer under .agents/skills, thin provider adapters for Codex/Cursor/Claude Code, workflow action-class boundaries, evidence-calibrated tool compatibility, adapter/context budgets, deterministic structural validation, and an explicit distinction between repository configuration support and provider runtime verification."
status: stable
tags: [phase-018, agents, skills, workflows, adapters, portability, codex, cursor, claude]
sources:
  - resource: 018-F-agent-context-progressive-retrieval-context-budget-anti-bloat-architecture.md
  - resource: ../canonical/governance/agent-workflow-portability.md
  - resource: ../canonical/governance/agentic-authority-scope.md
  - resource: ../canonical/governance/agent-context.md
  - resource: ../routing/agent_tool_compatibility.json
  - resource: ../../AGENTS.md
  - resource: ../../CLAUDE.md
  - resource: ../../scripts/validate_agent_workflows.py
  - resource: https://developers.openai.com/docs/agent-configuration/agents-md
  - resource: https://developers.openai.com/docs/build-skills
  - resource: https://cursor.com/docs/rules
  - resource: https://cursor.com/docs/skills
  - resource: https://docs.anthropic.com/en/docs/claude-code/memory
generated: { by: openai/gpt-5.6-sol, at: 2026-09-22T03:30:00Z }
---

# Purpose

018-G makes repeatable MUDAC agent workflows portable across coding-agent environments without letting each provider become a separate source of workflow or semantic authority.

018-E established what agents may do.

018-F established how little context they should need.

018-G establishes:

> **one workflow source, thin provider bridges, evidence-calibrated compatibility.**

# 1. Canonical workflow source

Reusable MUDAC workflows now live only at:

~~~text
.agents/skills/<workflow>/SKILL.md
~~~

Seven workflows are registered:

| Workflow | Normal action class | Purpose |
| --- | --- | --- |
| resolve-context | A1 | find minimum sufficient current context |
| resolve-contract | A1 | resolve one exact current stable rule/owner |
| execute-selected-task | A2 | execute one explicitly selected bounded repository task |
| review-change | A1 | review an actual change against current authority |
| run-conformance | A1 | run/report safe deterministic checks |
| update-traceability | A2 | repair directly affected routing/reference/status/traceability |
| exit-review | A1; A2 only for explicitly requested recording | evaluate one selected exit boundary |

These skills own procedure only.

They do not duplicate product/design/architecture semantics.

# 2. Canonical workflow governance

018-G adds:

> docs/canonical/governance/agent-workflow-portability.md

with WFL-001 through WFL-012.

The rules establish:

- one canonical workflow source;
- skills as procedure rather than semantic authority;
- required human-directed and stop-condition sections;
- thin provider adapters;
- provider discovery differences not changing MUDAC authority;
- fixed workflow action classes;
- execute-selected-task not manufacturing implementation authority;
- conformance not self-fixing by default;
- review staying A1 unless fixes are requested;
- exit review not auto-starting next work;
- evidence-calibrated tool compatibility claims;
- adapter failure degrading convenience rather than moving semantic authority.

# 3. Codex adapter

Current provider documentation establishes repository AGENTS.md loading and project .agents/skills discovery.

MUDAC therefore uses:

~~~text
AGENTS.md
.agents/skills/
~~~

directly for Codex.

No CODEX.md or .codex/AGENTS.md semantic duplicate is created.

Repository validation explicitly rejects those duplicate adapter surfaces.

Runtime status remains:

> not-smoke-verified-by-repository

because provider documentation plus repository structure is not proof of a particular local Codex runtime/session.

# 4. Cursor adapter

Current Cursor documentation supports root AGENTS.md, project .cursor/rules, and project .agents/skills.

MUDAC uses:

~~~text
AGENTS.md
.agents/skills/
.cursor/rules/00-mudac-routing.mdc
~~~

The Cursor rule is:

- relevance-selected;
- not alwaysApply;
- routing-only;
- subordinate to AGENTS.md, canonical governance and canonical skills.

The rule is not a second workflow source.

# 5. Claude Code adapter

Current Claude Code documentation identifies root CLAUDE.md as project memory and supports @-path imports.

MUDAC therefore uses a tiny root:

> CLAUDE.md

that imports AGENTS.md and points to canonical .agents/skills.

The initial DMTZ-inspired .claude/CLAUDE.md location was rejected during 018-G after checking current provider documentation and was replaced before phase exit.

Thin files under:

> .claude/commands/

point to the canonical skill source.

Those command bridges add no MUDAC semantics.

Their actual runtime discovery/behavior remains explicitly unverified by repository CI.

# 6. Provider compatibility manifest

018-G adds:

> docs/routing/agent_tool_compatibility.json

The manifest records:

- shared instruction source;
- canonical agentic authority;
- context policy;
- workflow contract/root;
- skill action classes;
- provider instruction/workflow mechanisms;
- repository configuration status;
- runtime verification status;
- external evidence URLs;
- duplicate-semantic-adapter prohibition.

The manifest is compatibility/routing data only.

# 7. Why MUDAC does not generate a second OKF workflow catalog

018-G deliberately does not add generated workflow copies under knowledge/.

Reason:

- project .agents/skills is already a portable procedure surface for supported agents;
- provider bridges can point directly to it;
- adding generated workflow concepts would create another discovery layer without current evidence that generic OKF consumers need procedure discovery;
- 018-F requires minimum-sufficient context and discourages duplicate routing without a concrete consumer.

If a future generic OKF consumer requires workflow routing, a generated routing-only projection may be added without changing workflow authority.

# 8. Tool-specific semantics are prohibited

Provider adapters may specialize:

- discovery;
- invocation syntax;
- commands;
- lightweight routing hints.

They may not specialize:

- product meaning;
- stable-rule ownership;
- A1–A4 boundaries;
- architecture authority;
- implementation authorization;
- evidence standards.

No coding agent is semantically privileged.

# 9. Context-budget impact

All new workflow/provider surfaces are measured.

Validated measurements include:

~~~text
CLAUDE.md                        257 / 2,048 bytes
Cursor rules aggregate          744 / 8,192 bytes

Cursor persistent baseline    5,638 / 12,288 bytes
Claude persistent baseline    5,895 / 12,288 bytes
Codex persistent baseline     5,638 /  8,192 bytes
~~~

Canonical skill sizes:

~~~text
execute-selected-task    1,407 / 8,192 bytes
exit-review              1,351 / 8,192 bytes
resolve-context          1,278 / 8,192 bytes
resolve-contract         1,143 / 8,192 bytes
review-change            1,225 / 8,192 bytes
run-conformance          1,211 / 8,192 bytes
update-traceability      1,215 / 8,192 bytes
~~~

No workflow comes close to its hard context envelope.

# 10. Deterministic adapter validation

018-G adds:

> scripts/validate_agent_workflows.py

It checks:

- exactly seven registered canonical skills;
- canonical skill path/name/frontmatter;
- required Human-directed boundary / Workflow / Stop conditions;
- skill budget;
- manifest action-class registration;
- thin Claude command bridges;
- no duplicate provider skill copies;
- root Claude import/routing bridge;
- thin Cursor routing rule and non-alwaysApply behavior;
- no duplicate Codex semantic adapter;
- three tool profiles;
- runtime status remaining unverified until actual smoke evidence exists;
- WFL-001 through WFL-012 presence.

# 11. Validation-trigger coverage

Knowledge Validation now triggers on changes to:

- AGENTS.md;
- CLAUDE.md;
- .agents/**;
- .cursor/**;
- .claude/**;
- scripts/**;
- docs/**;
- knowledge/**.

Provider-adapter changes therefore cannot bypass the repository conformance suite merely because product documentation is unchanged.

# 12. Stable-reference and owner impact

018-G adds one current Governance owner and twelve current WFL rules.

Exit counts:

~~~text
governed documentation paths       107
current-authority paths             84
downstream-candidate paths          15
historical adapters                  6
external references                  2

stable IDs                         264
current-authority IDs              122
downstream-candidate IDs           142
WFL IDs                             12
~~~

No downstream candidate became current.

# 13. Validation evidence

Initial portable-workflow mechanics:

> ba48bf8ce266642fb0f04a519d84babb3ba071a4

Provider-path correction:

> e97e56adce63bb51d7bb7db2d51639c4f8a6cd48

CI-trigger correction:

> 66c4ee1ad54d1444631e98b335be8d79afbc42a3

Final pre-consolidation Knowledge Validation:

> run 35683368316 — **SUCCESS**

Results:

~~~text
Markdown files                         354
frontmatter blocks                     254
stable rule anchors                    264
errors                                   0
warnings                                 0

OKF projection                         PASS
owner inventory                        PASS
stable-reference index                 PASS — 264 IDs
agentic authority policy               PASS
context budget measurement             PASS — 0 hard errors
portable skills/tool adapters          PASS — 7 skills / 3 tools
stable-ID role smoke tests             PASS
~~~

# 14. Runtime-compatibility carry-forward

018-G proves:

- repository structure;
- adapter subordination;
- skill portability format;
- provider-documented instruction/discovery mechanisms where cited;
- context budgets;
- deterministic references.

It does **not** prove that a particular installed Codex, Cursor or Claude Code version has loaded and obeyed each adapter in a live runtime.

Therefore runtime compatibility remains explicit carry-forward to 018-H where conformance evidence can be broadened without overstating the current result.

# 15. Relationship to 018-H

018-H should now treat the agent foundation as an integrated system and qualify:

- adapter/skill negative controls;
- status-mirror drift;
- reference integrity;
- generated artifact drift;
- conformance orchestration;
- tool-runtime smoke evidence when available and proportionate;
- secret/sensitive-data agentic checks;
- CI coverage and false-positive/false-authority risks.

It should not duplicate the workflow source created here.

# 16. Gate evaluation

| Phase-018 gate | 018-G result |
| --- | --- |
| P18-G1 semantic preservation | PASS |
| P18-G2 current/history integrity | PASS |
| P18-G3 documentation economy | PASS — one workflow source / thin bridges |
| P18-G4 OKF qualification | PRESERVED |
| P18-G5 deterministic routing | PRESERVED |
| P18-G6 human-directed agent authority | PRESERVED |
| P18-G7 context proportionality | PASS |
| P18-G8 conformance proportionality | PARTIAL PASS — static adapter/skill validation active; integrated/runtime conformance remains 018-H |
| P18-G10 architecture re-entry integrity | PASS |
| P18-G12 execution boundary | PASS |

# 17. Exit decision

**018-G — COMPLETE — PASS WITH RUNTIME COMPATIBILITY CARRY-FORWARD.**

At exit:

~~~text
canonical reusable workflow source     .agents/skills/
registered portable workflows          7
tool profiles                           3
provider-specific semantic copies       0
Cursor always-loaded custom rules       0
Codex duplicate instruction file        0
Claude root bridge                    THIN
skill/adapter context budgets          PASS
structural cross-tool conformance      PASS
provider runtime smoke verification    CARRY-FORWARD
domain implementation                  NOT AUTHORIZED
~~~

The next authorized work is:

> **018-H — Agentic Conformance, Knowledge Validation, Status Drift, Reference Integrity & CI Enforcement**

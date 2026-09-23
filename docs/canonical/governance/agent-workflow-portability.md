---
type: Documentation Authority
title: Portable Agent Workflows & Tool Adapter Contract
description: Defines the single-source portable skill model, tool-adapter subordination, workflow action-class boundaries, provider capability evidence, bridge constraints, and cross-agent portability rules for MUDAC repository agents.
status: stable
tags: [governance, agents, skills, workflows, adapters, portability, cursor, codex, claude]
sources:
  - resource: agentic-authority-scope.md
  - resource: agent-context.md
  - resource: deterministic-ownership-resolution.md
  - resource: validation-enforcement.md
  - resource: ../../018-pre-implementation-repository-qualification-agentic-development-architecture-reentry/018-F-agent-context-progressive-retrieval-context-budget-anti-bloat-architecture.md
  - resource: ../../020-autonomous-implementation-program-design-verification-v1-delivery/020-C-cursor-codex-roles-work-isolation-context-provenance-autonomy-circuit-breakers.md
generated: { by: openai/gpt-5.6-sol, at: 2026-09-22T03:45:00Z }
---

# Purpose

Define one reusable MUDAC workflow source that multiple coding-agent tools may consume without copying semantic authority or creating provider-specific workflow forks.

<a id="wfl-001"></a>
## WFL-001 — Canonical reusable workflows live once under .agents/skills

The repository workflow source is:

~~~text
.agents/skills/<workflow>/SKILL.md
~~~

A provider may discover that location natively or use a thin adapter. Duplicate provider-owned copies of the same MUDAC workflow are prohibited.

<a id="wfl-002"></a>
## WFL-002 — Skills own procedure, not product semantics

A skill describes how to perform a repeatable repository task.

It must route to canonical MUDAC owners and stable rules rather than restating product, design, architecture or implementation contracts as independent authority.

When skill text conflicts with canonical authority, canonical authority wins and the skill must be repaired.

<a id="wfl-003"></a>
## WFL-003 — Every canonical skill declares its human-directed boundary and stop conditions

Each MUDAC skill must include:

- Human-directed boundary;
- Workflow;
- Stop conditions.

The boundary identifies the normal A1/A2 role and any A3/A4 escalation.

The skill may not convert a human-selected task into autonomous next-work selection.

<a id="wfl-004"></a>
## WFL-004 — Provider adapters are thin routing bridges

Cursor rules, the root Claude import bridge, Claude command bridges and any future provider-specific files may point to:

- AGENTS.md;
- the canonical workflow skill;
- canonical governance;
- repository-native commands.

They may not contain a second copy of the workflow or provider-specific semantic rules.

<a id="wfl-005"></a>
## WFL-005 — Provider-native discovery and orchestration differences do not change MUDAC authority

Tools may discover AGENTS.md, skills, commands, rules, worktrees, cloud agents or subagents differently.

Those mechanics affect ergonomics and execution topology only.

The shared authority order, A1–A4 model, current-owner resolution, context discipline, G2 envelope, work-unit scope, review independence and execution boundaries remain identical across tools.

Cursor/Codex provider features may implement the Coordinator/Implementer/Reviewer mechanics, but provider orchestration never creates scope or lifecycle authority.

<a id="wfl-006"></a>
## WFL-006 — Workflow action class is fixed by the canonical workflow contract

Registered reusable workflows have a declared normal action class.

A1 workflows remain read-only unless the human separately requests an A2 recording/fix action.

The A2 execute-selected-task workflow remains bounded by the selected task and cannot perform A3/A4 actions merely because the skill was invoked.

<a id="wfl-007"></a>
## WFL-007 — Execute-selected-task cannot manufacture implementation authority

The generic A2 execution workflow may execute currently authorized repository work.

Before domain implementation, it must confirm implementation execution is actually authorized by the active repository state/package.

For a delegated implementation work unit, the workflow must also confirm that:

- the parent phase/package has G2;
- the work unit is declared in the active execution graph;
- the current agent role is permitted;
- the exact base/context manifest is present;
- no circuit breaker has fired.

A delegated work unit inherits its parent task envelope; it is not a new autonomous task-selection event.

Phase-020 design work does not become domain implementation merely because an A2 skill or provider subagent exists.

<a id="wfl-008"></a>
## WFL-008 — Run-conformance reports failures faithfully and does not self-fix by default

The conformance workflow is normally A1 and may run safe non-destructive checks.

A failed check does not authorize edits, requirement weakening, external mutation or semantic change.

Fixes require an enclosing human-selected A2 task.

<a id="wfl-009"></a>
## WFL-009 — Review-change remains A1 unless the human explicitly requests fixes

Review must inspect actual changed artifacts, resolve governing owners/contracts and distinguish defects from questions or unavailable evidence.

Finding a defect does not silently change the task from review to repair.

<a id="wfl-010"></a>
## WFL-010 — Exit review stops after the selected boundary

An exit-review workflow may evaluate or, when explicitly requested, record the selected exit decision.

It may report next eligible work.

It may not begin that next work.

<a id="wfl-011"></a>
## WFL-011 — Tool compatibility claims are evidence-calibrated

The tool compatibility manifest distinguishes:

- repository/static configuration support;
- documented provider mechanism;
- runtime smoke verification.

Static repository validation cannot be represented as proof that a specific installed provider version loaded or obeyed the adapter at runtime.

<a id="wfl-012"></a>
## WFL-012 — Adapter failure degrades provider convenience, not semantic authority

If a provider stops discovering a bridge, rule or skill location, MUDAC semantics do not move into that provider's workaround file.

Repair or replace the adapter while preserving:

~~~text
AGENTS.md bootstrap
→ canonical governance
→ .agents/skills procedure
→ canonical semantic owners
~~~

# Registered portable workflows

| Workflow | Normal class | Purpose |
| --- | --- | --- |
| resolve-context | A1 | find minimum sufficient current context |
| resolve-contract | A1 | resolve exact stable rule/owner |
| execute-selected-task | A2 | perform one explicitly selected bounded repository task |
| review-change | A1 | review actual change against current authority |
| run-conformance | A1 | run/report safe deterministic evidence |
| update-traceability | A2 | update directly affected routing/reference/status/traceability surfaces |
| exit-review | A1; A2 only when recording was explicitly requested | evaluate one selected exit boundary |

# Tool adapters

The machine-readable compatibility manifest is:

> docs/routing/agent_tool_compatibility.json

Current repository targets are:

- **Codex:** root AGENTS.md plus project .agents/skills; no CODEX.md duplicate;
- **Cursor:** root AGENTS.md plus project .agents/skills, with one optional relevance-selected routing rule;
- **Claude Code:** tiny root CLAUDE.md import bridge to AGENTS.md plus .claude/commands references to canonical .agents/skills.

Provider mechanics may evolve. WFL-011 requires support claims to track actual evidence rather than assumption.


# Autonomous implementation role portability

The Phase-020 operating model defines logical roles:

- Human Authorizer;
- Coordinator;
- Implementer;
- Reviewer;
- Verifier;
- Gatekeeper.

Cursor, Codex or another compatible agent may fill Coordinator, Implementer or Reviewer roles.

The role—not the provider—controls what the run may do.

Provider-specific worktree/cloud/subagent features remain adapters for the same contract. The repository must not create separate semantic instructions for a Cursor implementer and a Codex implementer.

A Coordinator may delegate only within the current G2-authorized execution graph. Implementers cannot recursively delegate implementation. Reviewers use a fresh independent run/context and are read-only unless repair work is separately assigned.

The machine projection is:

> docs/routing/autonomous_implementation_operating_model.json

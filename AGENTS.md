# MUDAC Repository Agent Rules

This file is a **bootstrap adapter**, not product/design authority.

## Required start

1. Start at [docs/index.md](docs/index.md). The generated [knowledge/](knowledge/) tree is generic OKF compatibility routing only and is never a substitute for authored authority.
2. Use [Canonical Knowledge](docs/canonical/) to find the smallest task-relevant current owner.
3. For Concept Design closure evidence, read [Phase 017](docs/017-methodology-closure-canonical-consolidation-completion-decision/). For the completed repository-qualification baseline, use [Phase 018](docs/018-pre-implementation-repository-qualification-agentic-development-architecture-reentry/). For accepted architecture, use [Accepted MUDAC Architecture](docs/canonical/architecture/accepted-architecture.md) plus the Phase-019 closure record. Phase 020 is active; use its [phase definition](docs/020-autonomous-implementation-program-design-verification-v1-delivery/README.md), machine control, implementation-program contract and accepted architecture.
4. Read [Design / Implementation Boundary](docs/canonical/governance/design-implementation-boundary.md) before architecture, implementation, tooling, runtime, persistence, security, or delivery work.
5. Load historical phase records only when rationale, chronology, rejected alternatives, repair propagation, or audit evidence is actually needed.

Do **not** recursively preload all canonical categories or numbered phases. Follow [Agent Context & Progressive Retrieval](docs/canonical/governance/agent-context.md).

## Current authority model

```text
current product meaning
  → canonical Project / Concepts / Synchronizations / Dependence /
    Experience / Mechanisms / Policies / Invariants

documentation / change / retrieval authority
  → canonical Governance

historical numbered phases
  → evidence / provenance

architecture + implementation corpus
  → suspended downstream candidates until explicit post-closure re-entry
```

The current product family remains:

> **PF-01 — MUDAC Live Competition Judging & Official Outcome**

## Current lifecycle posture

```text
Phase 016  COMPLETE — PASS WITH CLOSURE HANDOFF
Phase 017  COMPLETE — PASS WITH BOUNDED CARRY-FORWARD
Concept Design CLOSED

PHASE 018 COMPLETE — PASS
018-A/B/C/D/E/F/G/H/I/J/K/L/M COMPLETE
PHASE 019 COMPLETE — PASS — 019-A/B/C/D/E/F/G/H/I/J/K/L COMPLETE — WHOLE ARCHITECTURE ACCEPTED / G0 SATISFIED

historical architecture       SUSPENDED / QUARANTINED
accepted new architecture      NOT ESTABLISHED
implementation readiness      READY
implementation execution      NOT STARTED
execution authorization       NOT GRANTED
```

The active work is:

> **PHASE 019 COMPLETE — Architecture & Engineering Re-entry — 019-A/B/C/D/E/F/G/H/I/J/K/L COMPLETE**

## Human-directed action boundary

Follow [Agentic Development Authority, Human-Directed Scope & Action Boundaries](docs/canonical/governance/agentic-authority-scope.md).

- **A1 — review / inspect / plan:** read and validate safely; do not edit unless the human also requested change.
- **A2 — bounded change / build / fix:** make directly necessary repository edits and safe validation inside the selected task; do not start adjacent work automatically.
- **A3 — external / destructive / scope-expanding:** requires explicit human authorization for the specific consequential action.
- **A4 — semantic / accepted-architecture change:** requires explicit human change intent plus canonical change/re-entry governance; implementation difficulty is not permission to weaken accepted meaning.

A passing check does not authorize merge, deploy, the next phase/subphase, or a new implementation package.

## Portable workflows

Canonical reusable procedures live in `.agents/skills/<name>/SKILL.md` under [Portable Agent Workflows & Tool Adapter Contract](docs/canonical/governance/agent-workflow-portability.md).

Use the matching workflow when helpful, but the skill never increases the action authority granted by the human-selected task. Provider adapters are thin bridges only; do not copy MUDAC semantic rules into Cursor/Claude/Codex-specific files.

## Context budget discipline

Use minimum-sufficient context under [Agent Context & Progressive Retrieval](docs/canonical/governance/agent-context.md).

- Known ID: resolve directly; do not preload the rule registry.
- Unknown subject: route through the smallest family/owner.
- Expand to another current owner only for a concrete unresolved dependency.
- History, quarantined candidates and external/vendor material are on-demand extended tiers, not startup context.
- Do not persist ad hoc context packs as new summary authority.

Hard repository byte budgets apply to routing/bootstrap surfaces, not to canonical semantic truth.

For full repository agentic/documentation checks, run `python scripts/run_agentic_conformance.py`; a PASS is static repository evidence only.

## Retrieval discipline

- Known stable rule ID → run `python scripts/resolve_stable_id.py <ID>` and load the returned current owner; do not scan the full registry first.
- Current semantic question without a known ID → open the natural canonical owner.
- Cross-owner terminology question → use [Domain Vocabulary & Expectation-Transfer Rules](docs/canonical/project/domain-vocabulary-expectation-transfer.md).
- Product-family question → use [Product-Family Scope](docs/canonical/dependence/product-family-scope.md).
- User-visible meaning → use [Experience](docs/canonical/experience/).
- Historical rationale → follow the current owner's `sources` or the relevant numbered-phase index.
- Architecture/implementation comparison → consult the quarantine and re-entry governance first.

Do not treat an index, README, generated `knowledge/` projection, agent rule, phase record, architecture candidate, implementation candidate, code artifact, or test as permission to override a current canonical owner.

Phase 018 and Phase 019 are complete. Phase 020 is ACTIVE with 020-A/B complete and 020-C next eligible. Phase 020 may design/derive the implementation program but active implementation packages remain zero and domain implementation execution is unauthorized until explicit G2.


Current Phase-019 progression:

~~~text
PHASE 019 COMPLETE
019-A/B/C/D/E/F/G/H/I/J/K/L COMPLETE
ADQ-001 / ADQ-002 / ADQ-003 / ADQ-004 / ADQ-005 / ADQ-006 / ADQ-007 / ADQ-008 / ADQ-009 / ADQ-010 ACCEPTED
Q4R-001 / Q4R-002 / Q4R-003 / Q4R-004 COMPLETE
accepted whole architecture true
G0 package derivation ALLOWED
PHASE 020 ACTIVE
020-A/B COMPLETE
020-C NEXT ELIGIBLE
active implementation packages 0
implementation execution NOT AUTHORIZED
~~~

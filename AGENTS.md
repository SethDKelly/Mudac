# MUDAC Repository Agent Rules

This file is a **bootstrap adapter**, not product/design authority.

## Required start

1. Start at [docs/index.md](docs/index.md).
2. Use [Canonical Knowledge](docs/canonical/) to find the smallest task-relevant current owner.
3. For Concept Design closure evidence, read [Phase 017](docs/017-methodology-closure-canonical-consolidation-completion-decision/). For post-closure work, begin from the Phase 017 handoff and the post-Concept-Design re-entry contract.
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

## Current methodology posture

```text
Phase 016  COMPLETE — PASS WITH CLOSURE HANDOFF
Phase 017  COMPLETE — PASS WITH BOUNDED CARRY-FORWARD
Concept Design CLOSED

historical architecture       SUSPENDED / QUARANTINED
accepted new architecture      NOT ESTABLISHED
implementation readiness      READY
implementation execution      NOT STARTED
execution authorization       NOT GRANTED
```

The active work is:

> **Phase 018 Start Gate — Pre-Implementation Audit, OKF/Repository Hardening, Agentic Development Preparation & Architecture/Engineering Re-entry Planning**

## Retrieval discipline

- Current semantic question → open the natural canonical owner.
- Cross-owner terminology question → use [Domain Vocabulary & Expectation-Transfer Rules](docs/canonical/project/domain-vocabulary-expectation-transfer.md).
- Product-family question → use [Product-Family Scope](docs/canonical/dependence/product-family-scope.md).
- User-visible meaning → use [Experience](docs/canonical/experience/).
- Historical rationale → follow the current owner's `sources` or the relevant numbered-phase index.
- Architecture/implementation comparison → consult the quarantine and re-entry governance first.

Do not treat an index, README, agent rule, phase record, architecture candidate, implementation candidate, code artifact, or test as permission to override a current canonical owner.

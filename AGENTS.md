# MUDAC Repository Agent Rules

This file is a **bootstrap adapter**, not product/design authority.

## Required start

1. Start at [docs/index.md](docs/index.md).
2. Use [Canonical Knowledge](docs/canonical/) to find the smallest task-relevant current owner.
3. For active methodology work, read [Phase 017](docs/017-methodology-closure-canonical-consolidation-completion-decision/).
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
Phase 017  IN PROGRESS
017-A..F   COMPLETE — PASS/READY as recorded by Phase 017
017-G      IN PROGRESS

architecture authority        SUSPENDED
implementation readiness      NOT READY
implementation execution      NOT STARTED
implementation authorization  NOT YET
```

The active work is:

> **017-G — Documentation Authority, OKF Progressive Disclosure & Closure-Evidence Integrity Reconciliation**

## Retrieval discipline

- Current semantic question → open the natural canonical owner.
- Cross-owner terminology question → use [Domain Vocabulary & Expectation-Transfer Rules](docs/canonical/project/domain-vocabulary-expectation-transfer.md).
- Product-family question → use [Product-Family Scope](docs/canonical/dependence/product-family-scope.md).
- User-visible meaning → use [Experience](docs/canonical/experience/).
- Historical rationale → follow the current owner's `sources` or the relevant numbered-phase index.
- Architecture/implementation comparison → consult the quarantine and re-entry governance first.

Do not treat an index, README, agent rule, phase record, architecture candidate, implementation candidate, code artifact, or test as permission to override a current canonical owner.

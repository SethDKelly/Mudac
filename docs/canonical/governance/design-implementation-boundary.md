---
type: Documentation Authority
title: Design / Implementation Boundary
description: "Defines the durable boundary among MUDAC Concept Design, quarantined historical downstream work, post-closure architecture/engineering re-entry, implementation readiness, implementation execution authority, and production readiness."
status: stable
tags: [governance, methodology, design, architecture, implementation, boundary, reentry]
sources:
  - resource: ../../009-jackson-methodology-realignment/009-A-methodology-authority-reset-prior-exit-reopen-design-only-guardrails.md
  - resource: ../../016-scenario-misfit-exception-failure-adversarial-design-validation/016-K-phase-016-consolidation-validation-completeness-exit-review-phase-017-handoff.md
  - resource: ../../017-methodology-closure-canonical-consolidation-completion-decision/017-F-implementation-contamination-downstream-realization-obligations-architecture-neutral-handoff-audit.md
  - resource: downstream-authority-quarantine.md
  - resource: post-concept-design-reentry.md
---

# Purpose

Keep the authority boundary among Concept Design, historical downstream work, future architecture/engineering re-entry, implementation execution, and production readiness explicit.

# Current state

Phase 017 successfully closed Jackson-aligned Concept Design. Phase 018 subsequently qualified the repository and is now complete; Phase 019 architecture/engineering re-entry is authorized to begin at 019-A.

~~~text
Jackson Concept Design              CLOSED
implementation readiness            READY
implementation execution            NOT STARTED
implementation execution auth       NOT GRANTED
production readiness                NOT ESTABLISHED

historical architecture candidates  SUSPENDED / QUARANTINED
accepted new architecture           NOT ESTABLISHED
Phase 018                          COMPLETE — PASS
Phase 019                          AUTHORIZED — 019-A NEXT ELIGIBLE
architecture evaluation framework   DEFINED / PRE-SELECTION
accepted architecture               NOT ESTABLISHED
implementation-program framework    DEFINED / PRE-ARCHITECTURE
active implementation packages      0
package derivation                   NOT ALLOWED
006-D executable substrate          FROZEN HISTORICAL NON-DOMAIN FACT
008 implementation queue            HALTED / NOT ACTIVE
~~~

Current closure evidence is routed through [docs/index.md](../../index.md) and [Phase 017](../../017-methodology-closure-canonical-consolidation-completion-decision/).

# Authority direction

~~~text
human product intent / evidence
        ↓
canonical Project / Purpose
        ↓
current Concepts / Policies / Mechanisms / Invariants
        ↓
Synchronizations / application-action semantics
        ↓
Dependence / PF-01 scope
        ↓
Experience mapping
        ↓
successfully closed Concept Design

then, only after explicit re-entry:

architecture / engineering
        ↓
implementation planning
        ↓
separate execution authorization
~~~

Historical architecture, implementation, UI, code, tests, and tooling are never upstream Concept Design authority.

# Concept Design boundary

Concept Design owns representation-independent product meaning, including:

- purpose and affected-party needs;
- Concept purpose/state/actions/operational principles;
- composition/application actions;
- dependence/PF-01 scope;
- user-visible semantic obligations;
- familiarity/reuse/genericity decisions;
- cross-Concept integrity;
- scenario/misfit validation;
- accepted limitations and bounded uncertainty.

It does **not** select source/package topology, database technology, APIs, runtime services, cloud vendors, frameworks, authentication providers, synchronization protocols, transaction mechanisms, or delivery sequence.

# Quarantined downstream material

Pre-Phase-009 architecture/implementation material is preserved under the [Downstream Architecture & Implementation Authority Quarantine](downstream-authority-quarantine.md).

It may be used to:

- understand historical rationale;
- detect contamination;
- expose engineering assumptions;
- preserve potentially useful candidate knowledge for later revalidation.

It may not be used to prove that current product semantics are correct because old architecture or code already expects them.

# Frozen executable substrate

The retained 006-D workspace/runtime/bootstrap is a **historical non-domain executable fact**.

Narrow maintenance is permitted only when needed for repository safety/buildability, such as:

- critical dependency/security remediation;
- broken non-domain CI/tooling repair;
- compatibility maintenance that adds no MUDAC domain semantics;
- removal of accidental behavior contradicting current authority.

Maintenance must not become a path to resume domain implementation.

# No automatic reactivation

A successful Concept Design closure does **not** automatically:

- reactivate canonical architecture candidates;
- reactivate implementation candidates;
- resume 006-E–M;
- resume 008-F–L;
- accept PostgreSQL/AWS/Cognito/React/Fastify/TypeScript/OpenTofu or any other prior physical choice;
- authorize a first domain slice;
- authorize implementation execution.

All downstream candidates must pass the separate [Post-Concept-Design Architecture & Engineering Re-entry](post-concept-design-reentry.md) process. Architecture evaluation is governed by [Architecture Re-entry Evaluation & Decision Contract](architecture-reentry-evaluation.md), and future implementation planning/delivery by [Implementation Program, Verification & Delivery-Gate Contract](implementation-program-delivery.md).

# Readiness versus execution

The successful Phase-017 decision establishes:

~~~text
Concept Design           CLOSED
implementation readiness READY
~~~

but:

~~~text
readiness
  != accepted architecture
  != accepted implementation plan
  != implementation execution authorization
  != production readiness
~~~

Implementation execution requires a later explicit downstream authorization. Phase 019 may evaluate and accept architecture through the ARE contract, but active implementation packages remain zero and package derivation remains blocked until accepted architecture exists and the later implementation start gate is explicitly invoked.

# Downstream realization obligations

Future architecture/engineering must preserve current conceptual properties, including:

- Identity != Participation != Access;
- technical privilege != semantic authority;
- one logical evaluation / Scorecard weight;
- Draft != authoritative state;
- current != historical truth;
- missing != zero;
- Coverage != Aggregate != Rank;
- Rank != Award;
- Finalization != Outcome Declaration;
- ordinary result != exceptional no-result != unknown;
- source != Export != Publication != possession;
- truthful uncertainty and current-state preconditions;
- accessibility/degraded semantic parity.

These constraints do not prescribe the implementation mechanism.

# Reopen and change routing

If downstream engineering reveals a real product-semantic contradiction:

1. stop treating it as an engineering-only problem;
2. route the evidence to the natural canonical owner under [Canonical Change & Conflict Governance](change-governance.md);
3. change product semantics only through explicit design authority;
4. propagate/revalidate affected downstream work.

Engineering difficulty alone is not evidence that Concept Design is wrong.

# Retrieval rule

For current methodology status and closure evidence, use [docs/index.md](../../index.md) and [Phase 017](../../017-methodology-closure-canonical-consolidation-completion-decision/).

For historical details about how this boundary evolved, follow this document's sources and the numbered phase records rather than expanding this current owner into a phase-history log.

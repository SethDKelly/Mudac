---
type: Documentation Authority
title: Documentation Authority & Canonical Ownership
description: Defines current-knowledge precedence, one-owner discipline, downstream constraints, historical preservation, and the non-authoritative role of routing/summary artifacts.
status: stable
tags: [governance, authority, canonical, anti-drift]
sources:
  - resource: ../../004-knowledge-architecture/004-A-okf-adoption-authority-methodology-compatibility-terminology-contract.md
  - resource: ../../004-knowledge-architecture/004-B-knowledge-bundle-topology-canonical-authority-layers-progressive-disclosure.md
  - resource: ../../004-knowledge-architecture/004-C-canonical-concept-policy-invariant-experience-knowledge-extraction.md
  - resource: ../../004-knowledge-architecture/004-F-documentation-governance-agent-context-anti-drift-rules.md
---

# Purpose

Define where current MUDAC rules live and prevent summaries, implementation artifacts, agent instructions, or historical records from becoming accidental competing authorities.

<a id="doc-001"></a>
## DOC-001 — Canonical owner controls current meaning

When a subject has an accepted document under `docs/canonical/`, that document is the preferred current owner of its meaning.

Historical phase records remain material evidence and rationale but are not the ordinary current-rule surface once a canonical owner exists.

<a id="doc-002"></a>
## DOC-002 — One normative rule has one canonical owner

A normative rule should be owned in one canonical document/anchor. Dependents reference that owner—preferably through a stable rule ID—rather than creating independent normative copies.

Bounded restatement is permitted for independent auditability or necessary comprehension, but the linked canonical owner remains authoritative.

<a id="doc-003"></a>
## DOC-003 — Downstream artifacts cannot override upstream canonical meaning

Architecture, implementation, tests, runbooks, code comments, generated artifacts, and operational documentation must satisfy canonical product/UX/governance contracts. They cannot redefine those contracts merely by documenting or implementing different behavior.

If product meaning is intentionally changed, update canonical authority through [Canonical Change & Conflict Governance](change-governance.md) rather than allowing the downstream artifact to become the change mechanism.

<a id="doc-004"></a>
## DOC-004 — Historical phase records are append-stable provenance

Numbered design-phase records preserve the reasoning and decisions accepted at that point in time. Later semantic evolution is recorded through later refinement/current canonical knowledge rather than rewriting an earlier record to pretend the later answer was always present.

Narrow typo/link corrections remain permissible. See [Source Lineage](source-lineage.md).

<a id="doc-005"></a>
## DOC-005 — Indexes, READMEs, registries, and agent adapters route; they do not become rule owners

`index.md`, `README.md`, stable-ID registries, traceability tables, `AGENTS.md`, and future IDE/agent adapters may summarize and link authority. Their summaries remain subordinate to the canonical owners they reference.

A routing artifact must not accumulate full rule bodies merely because it is frequently read.

<a id="doc-006"></a>
## DOC-006 — Knowledge topology does not dictate source-code topology

The canonical knowledge tree organizes retrieval and authority. It does not require future packages, services, APIs, schemas, databases, or AWS resources to mirror the documentation hierarchy.

Implementation structure is a downstream architecture decision constrained by canonical meaning, not derived mechanically from folder layout.

# Human instruction

An explicit human request may intentionally change MUDAC design. That request authorizes the change workflow; it does not make a downstream file authoritative without updating the canonical owner and lineage.

# Cross-reference rule

When an identified rule exists, downstream documentation should link the exact owner/anchor and explain the local consequence. See [Stable Rule Identifiers & Cross-Reference Contract](rule-identifiers.md).
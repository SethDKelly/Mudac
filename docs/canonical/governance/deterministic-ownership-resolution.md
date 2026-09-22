---
type: Documentation Authority
title: Deterministic Ownership, Stable Reference Resolution & Drift Control
description: Defines machine-readable owner-role classification, exact stable-ID resolution, non-current candidate/history handling, relocation safety, and fail-closed drift behavior without making routing artifacts semantic authority.
status: stable
tags: [governance, ownership, stable-id, routing, resolution, drift, agents]
sources:
  - resource: documentation-authority.md
  - resource: rule-identifiers.md
  - resource: agent-context.md
  - resource: validation-enforcement.md
  - resource: ../../018-pre-implementation-repository-qualification-agentic-development-architecture-reentry/018-B-whole-corpus-documentation-inventory-duplication-concision-current-history-topology-audit.md
  - resource: ../../018-pre-implementation-repository-qualification-agentic-development-architecture-reentry/018-C-okf-v0.2-conformance-progressive-disclosure-metadata-knowledge-bundle-qualification.md
generated: { by: openai/gpt-5.6-sol, at: 2026-09-22T03:08:00Z }
---

# Purpose

Make MUDAC current authority deterministically resolvable by tools while preserving the distinction between semantic ownership, routing metadata, suspended downstream candidates, deprecated adapters and numbered-phase provenance.

The machine-readable policy is [canonical_ownership.json](../../routing/canonical_ownership.json). Its generated path-role inventory is [canonical_owner_inventory.json](../../routing/canonical_owner_inventory.json). The generated exact-ID routing index is [stable_reference_index.json](../../routing/stable_reference_index.json).

<a id="own-001"></a>
## OWN-001 — Semantic authority remains in authored owner documents

Machine-readable ownership policy, generated indexes, resolvers, search results and OKF projection files are routing aids only.

They may identify an authored owner. They do not own or reinterpret the rule being routed.

<a id="own-002"></a>
## OWN-002 — Ownership role is classified before path content is trusted

A path is classified through the ownership policy before a tool treats it as current authority.

The role precedence is:

~~~text
explicit historical-adapter path
        ↓
downstream-candidate root
        ↓
current canonical owner root
        ↓
external-reference root
        ↓
numbered-phase evidence
        ↓
other / unresolved
~~~

Within a current canonical root, a deprecated artifact is non-current even though its path remains under canonical.

Path location by itself is therefore insufficient evidence of authority.

<a id="own-003"></a>
## OWN-003 — Exact stable-ID resolution defaults to current authority only

A known stable ID resolves through the generated stable-reference index.

Default resolution succeeds only when the indexed owner role is:

> current-authority

The resolver returns the authored owner path plus exact stable fragment. It does not return a copied rule body as a new source of truth.

<a id="own-004"></a>
## OWN-004 — Suspended downstream IDs require explicit candidate resolution

Stable IDs owned by quarantined Architecture or Implementation documents remain addressable for referential integrity, but they are not current accepted authority.

A tool must request candidate inclusion explicitly before such an ID is returned as a candidate locator.

Candidate resolution must label the result as downstream-candidate and must not silently satisfy a request for current authority.

<a id="own-005"></a>
## OWN-005 — Deprecated and historical adapters never satisfy current resolution

Deprecated or explicitly historical adapters remain addressable for link and provenance continuity.

They cannot satisfy current-owner resolution. If a tool exposes one, the result must be explicitly requested as non-current and must retain that role label.

<a id="own-006"></a>
## OWN-006 — Numbered-phase occurrences are provenance only and opt-in

Historical or active numbered-phase occurrences of a stable ID do not participate in owner selection.

They may be returned only through explicit history/provenance lookup after the current or explicitly requested non-current owner has been identified.

Search frequency, phase recency and first textual occurrence cannot override the resolved owner.

<a id="own-007"></a>
## OWN-007 — Generated ownership indexes are deterministic and rebuildable

The owner inventory is derived from the repository paths plus the authored classification policy. The stable-reference index is derived from:

1. the authored ownership classification policy;
2. the authored stable-rule registry;
3. the actual target owner/anchor structure checked by repository validation.

Both generated artifacts may be deleted and regenerated without changing MUDAC semantics.

Hand-editing the generated index is prohibited.

<a id="own-008"></a>
## OWN-008 — Resolution fails closed on drift

Resolution must fail/report rather than guess when:

- a stable ID is absent from the generated index;
- multiple owners claim the same stable ID;
- the registry target is missing;
- the target fragment is missing;
- the generated index does not match its source registry/policy;
- the owner role is non-current but the caller requested ordinary current resolution.

A resolver must never choose the first search result as a fallback.

<a id="own-009"></a>
## OWN-009 — Stable identity is the rule ID, not its current file path

A path is a current locator, not the permanent identity of a stable rule.

A safe owner relocation must update the authored owner, registry target, generated index and affected current links together while preserving the stable ID when semantics remain compatible.

If semantics change incompatibly, the replacement receives a new ID under the Stable Rule Identifiers contract.

<a id="own-010"></a>
## OWN-010 — Unknown-subject discovery and known-ID resolution are different operations

When the exact ID is known, resolve it directly instead of traversing broad discovery or search.

When no exact stable ID or owner path is known, start from docs/index.md and the smallest relevant canonical family. Identify the governing owner/rule there, then use exact resolution if needed.

This keeps search and discovery from becoming implicit authority algorithms.

<a id="own-011"></a>
## OWN-011 — Artifact lifecycle status and semantic owner role remain distinct

OKF status describes the knowledge artifact lifecycle. Ownership role describes how the repository may use the artifact for semantic resolution.

Examples:

~~~text
status: stable + role: current-authority
  → ordinary current owner

status: stable + role: downstream-candidate
  → current routing artifact/candidate record, not accepted architecture

status: deprecated + canonical path
  → non-current adapter, not current authority
~~~

Neither field alone substitutes for the full classification rule.

<a id="own-012"></a>
## OWN-012 — Routing/status mirrors cannot become independent authority

Root READMEs, AGENTS.md, generated OKF routes, phase indexes and other compact mirrors remain routing conveniences.

Where they repeat owner or lifecycle information, drift is a validation concern rather than permission to choose whichever copy is newest. The natural authored owner and active phase record remain controlling.

Broader automated mirror enforcement is completed in the Phase-018 conformance work rather than by turning a status manifest into a new semantic plane.

# Resolution interfaces

Current exact stable-ID lookup:

~~~bash
python scripts/resolve_stable_id.py <ID>
~~~

Explicit suspended candidate lookup:

~~~bash
python scripts/resolve_stable_id.py <ID> --include-candidates
~~~

Explicit deprecated/historical-adapter lookup:

~~~bash
python scripts/resolve_stable_id.py <ID> --include-deprecated
~~~

Separate numbered-phase provenance lookup:

~~~bash
python scripts/resolve_stable_id.py <ID> --history
~~~

For structured consumers, add --json.

# Relocation decision for 018-B historical adapters

018-D finds no reason to physically relocate the six historical adapters merely to improve deterministic resolution.

Their role is now explicit in the ownership policy, so a path under canonical no longer causes current-resolution ambiguity.

Physical relocation remains optional and should occur only when it improves human topology enough to justify link churn.

# Downstream candidate topology decision

018-D likewise does not move Architecture or Implementation candidate trees.

The policy classifies their complete roots as downstream-candidate before any exact ID is resolved.

Their semantic disposition remains a Phase-018-J architecture/implementation qualification concern.

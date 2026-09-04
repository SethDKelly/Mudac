---
type: Documentation Authority
title: Canonical Change & Conflict Governance
description: Defines how canonical MUDAC meaning may change, how stable-rule impacts are reviewed, and how contradictions are resolved without silent drift.
status: stable
tags: [governance, change, conflict, impact, anti-drift]
sources:
  - resource: ../../004-knowledge-architecture/004-D-historical-phase-migration-provenance-source-lineage-retrofit.md
  - resource: ../../004-knowledge-architecture/004-E-cross-reference-stable-rule-id-restatement-reduction-retrofit.md
  - resource: ../../004-knowledge-architecture/004-F-documentation-governance-agent-context-anti-drift-rules.md
---

# Purpose

Make product/design evolution explicit and traceable so implementation convenience, editorial cleanup, or agent conflict resolution cannot silently change MUDAC semantics.

# Change classification

Before changing canonical knowledge, classify the change:

- **Editorial** — wording, layout, link, typo, or explanation changes with no semantic effect.
- **Compatible refinement** — adds precision while preserving the accepted contract.
- **Material semantic change** — changes behavior, boundary, authority, lifecycle, policy, invariant, or experience meaning.

Material semantic changes require explicit design/refinement rationale and impact review.

<a id="chg-001"></a>
## CHG-001 — Semantic change updates the canonical owner explicitly

When product/design meaning changes, update the canonical owner rather than relying on a downstream architecture, implementation, test, README, or agent instruction to carry the new meaning.

A material change should be attributable to an explicit human/design decision or accepted refinement record so future readers can reconstruct why the current contract changed.

<a id="chg-002"></a>
## CHG-002 — Stable-rule semantic change requires dependent impact review

If a changed contract has a stable rule ID, determine whether the existing ID remains semantically compatible and identify known dependents.

Review canonical references and, once present, architecture/tests that cite the affected ID. A materially incompatible replacement receives a new ID; retired IDs are not reassigned.

<a id="chg-003"></a>
## CHG-003 — Contradictions are surfaced, not silently normalized

When two authoritative-looking sources conflict, do not merge them by intuition or select the more convenient interpretation.

- canonical versus historical: current canonical normally governs, but evidence of a faulty extraction is treated as a documentation defect to resolve;
- canonical versus canonical: identify intended ownership and explicitly resolve the conflict before downstream work relies on it;
- canonical versus implementation: implementation adapts unless the human intentionally changes the product design.

<a id="chg-004"></a>
## CHG-004 — Canonical semantic changes preserve lineage and navigation coherence

A semantic change must review the owner's material `sources`, affected cross-links/stable IDs, known dependents, and routing/index entries where ownership/discoverability changes.

The objective is not to touch every README; it is to leave no known authority mismatch behind.

<a id="chg-005"></a>
## CHG-005 — Implementation mismatch is resolved downstream unless design is deliberately changed

If an implementation approach cannot satisfy a canonical rule, that is an architecture/implementation problem by default—not implicit permission to weaken the rule.

The options are:

1. choose a different implementation mechanism; or
2. explicitly redesign the product through this canonical-change workflow.

# Human-requested design changes

A direct human request to alter product/design meaning is sufficient intent to begin the change workflow. The agent should not resist the requested redesign merely because it differs from current canonical state; it should update canonical authority, lineage, stable-rule compatibility, and dependents so the repository ends coherent.

# Historical preservation

Do not rewrite old phase records to make them agree retroactively with a new decision. Preserve the earlier record and add the later refinement/current canonical result, consistent with [Source Lineage](source-lineage.md) and [DOC-004](documentation-authority.md#doc-004).

# Editorial changes

Editorial changes do not require a design phase or new rule ID when semantics are preserved. They still must not accidentally broaden/narrow a stable rule while retaining its ID.

# Review depth

Impact review is proportional to consequence. A typo does not require a repository-wide audit. A change to `INV-*`, Scorecard authority, Competition lifecycle, Evaluation Policy, disclosure, or official-outcome semantics may affect many later contracts and warrants broader review.

004-H will automate structural checks such as duplicate IDs and broken links; semantic compatibility remains a design-review responsibility.
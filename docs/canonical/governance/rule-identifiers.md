---
type: Documentation Authority
title: Stable Rule Identifiers & Cross-Reference Contract
description: Governs durable normative rule IDs and how dependent MUDAC knowledge references canonical owners without creating duplicate authority.
status: stable
tags: [governance, rule-id, cross-reference, anti-drift]
sources:
  - resource: ../../004-knowledge-architecture/004-A-okf-adoption-authority-methodology-compatibility-terminology-contract.md
  - resource: ../../004-knowledge-architecture/004-C-canonical-concept-policy-invariant-experience-knowledge-extraction.md
  - resource: ../../004-knowledge-architecture/004-E-cross-reference-stable-rule-id-restatement-reduction-retrofit.md
---

# Canonical contract

Stable rule IDs identify durable normative contracts owned by canonical knowledge documents. The ID is a reference interface; the linked owner remains the source of rule meaning.

Rule IDs are owner-based rather than phase-based. They must not be reused for a different meaning.

# Reference syntax

Rule owners use explicit anchors:

```markdown
<a id="sc-001"></a>
## SC-001 — Draft is non-authoritative
```

Dependents use ordinary Markdown links:

```markdown
[SC-001](../concepts/scorecard.md#sc-001)
```

A naked ID may be used in nearby prose only when the linked form has already established the referent and ambiguity is impossible.

# Restatement rule

A dependent document should cite the canonical ID and explain only its local consequence. Full restatement is reserved for cases where independent auditability or necessary comprehension justifies it, and the restatement remains subordinate to the linked owner.

# Stability rule

Editorial clarification may retain an ID when semantics remain compatible. A materially incompatible replacement receives a new ID. Retired IDs are never reassigned.

# Cross-cutting invariants

* [INV-001 — Judge Independence](../invariants/judge-independence.md#inv-001)
* [INV-002 — One Logical Scorecard per Judge × Encounter](../invariants/one-logical-scorecard.md#inv-002)
* [INV-003 — Missing Is Never Zero](../invariants/missing-never-zero.md#inv-003)
* [INV-004 — Organizer Authority Does Not Become Judge Authorship](../invariants/organizer-not-judge-author.md#inv-004)
* [INV-005 — Current and Historical Truth Remain Distinct](../invariants/current-vs-historical-truth.md#inv-005)
* [INV-006 — Calculated Is Not Official](../invariants/calculated-not-official.md#inv-006)
* [INV-007 — Official Is Not Automatically Public](../invariants/official-not-automatically-public.md#inv-007)
* [INV-008 — Capture-Channel Parity](../invariants/capture-channel-parity.md#inv-008)
* [INV-009 — Accessibility Is Semantic Parity](../invariants/accessibility-semantic-parity.md#inv-009)
* [INV-010 — Truthful Authority Under Uncertainty](../invariants/truthful-authority-under-uncertainty.md#inv-010)

# Competition

* [COMP-001 — Competition Lifecycle](../concepts/competition.md#comp-001)
* [COMP-002 — Post-Finalization Correction Preserves Finalized Lifecycle](../concepts/competition.md#comp-002)

# Access

* [ACC-001 — Access Is Contextual](../concepts/access.md#acc-001)
* [ACC-002 — Access Does Not Transfer Semantic Authority](../concepts/access.md#acc-002)

# Scorecard

* [SC-001 — Draft Is Non-Authoritative](../concepts/scorecard.md#sc-001)
* [SC-002 — Amendment Preserves Prior Authority Until Successor Finalization](../concepts/scorecard.md#sc-002)
* [SC-003 — Structural Scorecard Identity Is Not Amended](../concepts/scorecard.md#sc-003)

Logical uniqueness/evaluation weight is separately owned by [INV-002](../invariants/one-logical-scorecard.md#inv-002), and Judge authorship by [INV-004](../invariants/organizer-not-judge-author.md#inv-004).

# Evaluation Policy

* [EVAL-001 — Equal Eligible Individual Judge Weighting](../policies/evaluation-policy.md#eval-001)
* [EVAL-002 — No Silent Rubric Pooling or Rescaling](../policies/evaluation-policy.md#eval-002)
* [EVAL-003 — Outcome-Affecting Policy Is Reconstructible](../policies/evaluation-policy.md#eval-003)

# Ranking

* [RANK-001 — Rank Is Derived and Non-Editable](../mechanisms/rank.md#rank-001)
* [RANK-002 — Precision and Ties Follow Declared Policy](../mechanisms/rank.md#rank-002)

# Official Outcomes

* [OUT-001 — Finalization Establishes an Official Outcome Revision](../mechanisms/official-outcome-revision.md#out-001)
* [OUT-002 — Official Correction Requires Explicit Successor Confirmation](../mechanisms/official-outcome-revision.md#out-002)

# Disclosure

* [DISC-001 — Blinded Judge Team Identity](../policies/anonymity-disclosure.md#disc-001)
* [DISC-002 — Disclosure Is Audience/Purpose Specific](../policies/anonymity-disclosure.md#disc-002)

# Export

* [EXPORT-001 — Export Represents Source Truth; It Does Not Replace It](../concepts/export.md#export-001)
* [EXPORT-002 — Generation and Publication Are Distinct](../concepts/export.md#export-002)

# Change impact

A proposed semantic change to an identified rule must trigger review of known canonical dependents and, once present, architecture/tests that cite the ID. 004-F defines the governance workflow; 004-H will validate uniqueness and link resolution mechanically.

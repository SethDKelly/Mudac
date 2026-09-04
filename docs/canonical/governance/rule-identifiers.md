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
  - resource: ../../004-knowledge-architecture/004-F-documentation-governance-agent-context-anti-drift-rules.md
  - resource: ../../004-knowledge-architecture/004-G-okf-metadata-trust-verification-lifecycle-freshness-conventions.md
  - resource: ../../004-knowledge-architecture/004-H-validation-tooling-link-authority-checks-ci-enforcement.md
generated: { by: openai/gpt-5.6-sol, at: 2026-09-04T04:09:23Z }
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

# Architecture foundation

* [ARCH-001 — Upstream Canonical Semantics Constrain Architecture](../architecture/architectural-foundation.md#arch-001)
* [ARCH-002 — Authoritative Transitions Are Validated and Confirmed at the Authoritative Boundary](../architecture/architectural-foundation.md#arch-002)
* [ARCH-003 — Client, Device, and Local State Are Not Final Authority](../architecture/architectural-foundation.md#arch-003)
* [ARCH-004 — Derived Projections Are Not Write Authority](../architecture/architectural-foundation.md#arch-004)
* [ARCH-005 — Actor, Author, Authorizer, and Capture Attribution Survive Boundaries](../architecture/architectural-foundation.md#arch-005)
* [ARCH-006 — Failure and Retry Preserve Logical Identity and Evidence](../architecture/architectural-foundation.md#arch-006)
* [ARCH-007 — Security and Disclosure Are Enforced Beyond Presentation Code](../architecture/architectural-foundation.md#arch-007)
* [ARCH-008 — Freshness and Uncertainty Remain Representable](../architecture/architectural-foundation.md#arch-008)

# Documentation authority

* [DOC-001 — Canonical Owner Controls Current Meaning](documentation-authority.md#doc-001)
* [DOC-002 — One Normative Rule Has One Canonical Owner](documentation-authority.md#doc-002)
* [DOC-003 — Downstream Artifacts Cannot Override Upstream Canonical Meaning](documentation-authority.md#doc-003)
* [DOC-004 — Historical Phase Records Are Append-Stable Provenance](documentation-authority.md#doc-004)
* [DOC-005 — Routing/Summary/Agent Artifacts Do Not Become Rule Owners](documentation-authority.md#doc-005)
* [DOC-006 — Knowledge Topology Does Not Dictate Source-Code Topology](documentation-authority.md#doc-006)

# Agent context

* [CTX-001 — Start With Progressive Disclosure](agent-context.md#ctx-001)
* [CTX-002 — Load Only Task-Relevant Owners and Dependencies](agent-context.md#ctx-002)
* [CTX-003 — Historical Context Is On-Demand Through Lineage](agent-context.md#ctx-003)
* [CTX-004 — Stop Context Expansion When Authority Is Sufficient](agent-context.md#ctx-004)
* [CTX-005 — Recursive Corpus Loading Is Not the Default](agent-context.md#ctx-005)

# Canonical change governance

* [CHG-001 — Semantic Change Updates the Canonical Owner Explicitly](change-governance.md#chg-001)
* [CHG-002 — Stable-Rule Semantic Change Requires Dependent Impact Review](change-governance.md#chg-002)
* [CHG-003 — Contradictions Are Surfaced, Not Silently Normalized](change-governance.md#chg-003)
* [CHG-004 — Canonical Semantic Changes Preserve Lineage and Navigation Coherence](change-governance.md#chg-004)
* [CHG-005 — Implementation Mismatch Is Resolved Downstream Unless Design Is Deliberately Changed](change-governance.md#chg-005)

# OKF metadata, trust, lifecycle and freshness

* [META-001 — Canonical Knowledge Uses a Deliberate MUDAC Frontmatter Profile](metadata-trust-lifecycle.md#meta-001)
* [META-002 — `generated` Records the Actual Producer of Current Meaningful Content](metadata-trust-lifecycle.md#meta-002)
* [META-003 — `verified` Records an Actual Content/Source Confirmation Event](metadata-trust-lifecycle.md#meta-003)
* [META-004 — OKF `status` Describes Knowledge-Artifact Lifecycle, Not MUDAC Domain State](metadata-trust-lifecycle.md#meta-004)
* [META-005 — `stale_after` Is Used Only for a Real Absolute Freshness Boundary](metadata-trust-lifecycle.md#meta-005)
* [META-006 — Source Credibility Metadata Must Remain Factual and Material](metadata-trust-lifecycle.md#meta-006)
* [META-007 — OKF Trust Signals Do Not Replace MUDAC Authority or Access](metadata-trust-lifecycle.md#meta-007)
* [META-008 — Legacy Records Are Not Speculatively Backfilled](metadata-trust-lifecycle.md#meta-008)
* [META-009 — Metadata Updates Preserve Semantic and Historical Distinctions](metadata-trust-lifecycle.md#meta-009)

# Validation and CI enforcement

* [VAL-001 — Validation Proves Structural Conformance, Not Semantic Verification](validation-enforcement.md#val-001)
* [VAL-002 — Current Canonical/Reference Knowledge Receives Deterministic Metadata-Shape Checks](validation-enforcement.md#val-002)
* [VAL-003 — Stable Rule IDs Are Globally Unique, Explicitly Anchored, and Registry-Resolvable](validation-enforcement.md#val-003)
* [VAL-004 — Current Authority Links and Local Source Edges Must Resolve](validation-enforcement.md#val-004)
* [VAL-005 — Progressive-Disclosure Routing Surfaces Are Structural Requirements](validation-enforcement.md#val-005)
* [VAL-006 — Legacy Exemptions Are Explicit and Must Not Become Blanket Validation Bypasses](validation-enforcement.md#val-006)
* [VAL-007 — Knowledge Validation Is a Blocking, Read-Only CI Check](validation-enforcement.md#val-007)
* [VAL-008 — Validator Evolution Is Governed Because It Encodes Repository Policy](validation-enforcement.md#val-008)

# Change impact

A proposed semantic change to an identified rule must trigger review of known canonical dependents and, once present, architecture/tests that cite the ID. [Canonical Change & Conflict Governance](change-governance.md) defines the workflow; [OKF Metadata, Trust, Verification, Lifecycle & Freshness](metadata-trust-lifecycle.md) governs knowledge-artifact metadata; [Knowledge Validation & CI Enforcement](validation-enforcement.md) governs deterministic CI enforcement.

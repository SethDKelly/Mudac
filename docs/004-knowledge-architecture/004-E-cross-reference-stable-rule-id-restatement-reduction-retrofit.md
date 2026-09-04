---
type: Design Phase Record
title: 004-E — Cross-Reference, Stable Rule-ID & Restatement Reduction Retrofit
description: Establish stable normative rule identifiers and reduce duplicated canonical restatement by linking dependent knowledge to one authoritative owner.
status: stable
tags: [phase-004, cross-reference, rule-id, anti-drift]
sources:
  - resource: 004-A-okf-adoption-authority-methodology-compatibility-terminology-contract.md
  - resource: 004-B-knowledge-bundle-topology-canonical-authority-layers-progressive-disclosure.md
  - resource: 004-C-canonical-concept-policy-invariant-experience-knowledge-extraction.md
  - resource: 004-D-historical-phase-migration-provenance-source-lineage-retrofit.md
---

# Purpose

004-E makes canonical MUDAC rules addressable at a stable granularity suitable for architecture, implementation, tests, review, and agent reasoning.

The objective is not to assign a number to every sentence. It is to give durable identifiers to rules whose meaning is repeatedly depended upon, then make dependent documents link to those owners rather than becoming parallel normative copies.

The governing objective is:

> A downstream artifact should be able to say exactly which canonical contract it satisfies without copying that contract into a new place where it can drift.

# 1. Stable rule-ID model

MUDAC uses owner-based rule IDs rather than phase-based IDs.

Examples:

```text
SC-001       Scorecard-owned rule
COMP-001     Competition-owned rule
ACC-001      Access-owned rule
EVAL-001     Evaluation Policy rule
RANK-001     Rank mechanism rule
OUT-001      Official Outcome Revision rule
DISC-001     Disclosure policy rule
EXPORT-001   Export-owned rule
INV-001      cross-cutting invariant
```

Phase numbers are intentionally absent because rule identity must survive later design phases, document movement, prose cleanup, and architecture evolution.

# 2. What receives an ID

A rule receives a stable ID when it is materially useful as a dependency for later architecture, implementation, tests, governance, or audit.

Good candidates are rules that are:

- normative rather than merely explanatory;
- stable enough to act as a contract;
- repeatedly depended upon;
- likely to appear in acceptance criteria or architecture reviews;
- consequential if silently changed;
- narrow enough to cite independently.

A whole document does not automatically require IDs for every paragraph.

# 3. What does not receive an ID

MUDAC does not assign stable IDs merely to:

- headings used only for prose organization;
- examples;
- explanatory diagrams;
- historical observations;
- temporary migration instructions;
- every Concept field or UX detail;
- text whose stable owner is already a linked invariant/rule elsewhere.

Excessive IDs create false precision and make maintenance harder.

# 4. Identifier stability

Once a rule ID is accepted and referenced downstream:

1. the ID is never reused for another meaning;
2. editorial clarification may retain the ID if semantic meaning remains compatible;
3. a materially incompatible semantic replacement receives a new ID;
4. the old ID remains discoverable as superseded/deprecated history rather than being silently reassigned;
5. moving or renaming the owner document requires preserving or repairing links to the ID.

Detailed lifecycle metadata is finalized in 004-G.

# 5. Stable anchor convention

Rule owners use an explicit lowercase HTML anchor immediately before the rule heading:

```markdown
<a id="sc-001"></a>
## SC-001 — Draft is non-authoritative
```

Dependent documents link to that explicit anchor:

```markdown
[SC-001](../concepts/scorecard.md#sc-001)
```

The explicit anchor is the stable interface. Heading wording may improve without changing the link target.

# 6. Cross-reference-first contract

When a rule already has a canonical owner, a dependent document should normally:

1. link to the stable rule ID;
2. state only the local consequence needed for its own purpose;
3. avoid reproducing the complete normative rule body.

Preferred pattern:

```text
This synchronization must satisfy SC-001.
Therefore local Draft state cannot be counted as authoritative evidence.
```

Avoid:

```text
full Scorecard lifecycle copied into API document
full Scorecard lifecycle copied into persistence document
full Scorecard lifecycle copied into UI document
```

# 7. Bounded restatement

Restatement is allowed when a document must be independently auditable or when the consequence cannot be understood without a concise statement of the upstream rule.

Such restatement:

- links to the stable canonical rule;
- is clearly subordinate to that owner;
- does not introduce broader or narrower semantics;
- should normally be shorter than the canonical rule body;
- must be reviewed if the canonical rule changes.

# 8. Rule registry

The canonical registry is [Stable Rule Identifiers & Cross-Reference Contract](../canonical/governance/rule-identifiers.md).

The registry is an index of identifiers and owners, not another copy of the rule bodies.

Canonical rule meaning lives at the linked owner/anchor.

# 9. Initial invariant namespace

004-E assigns stable IDs to all ten cross-cutting invariants because they are intentionally designed as repeated architecture/test dependencies:

```text
INV-001  Judge Independence
INV-002  One Logical Scorecard per Judge × Encounter
INV-003  Missing Is Never Zero
INV-004  Organizer Authority Does Not Become Judge Authorship
INV-005  Current and Historical Truth Remain Distinct
INV-006  Calculated Is Not Official
INV-007  Official Is Not Automatically Public
INV-008  Capture-Channel Parity
INV-009  Accessibility Is Semantic Parity
INV-010  Truthful Authority Under Uncertainty
```

# 10. Initial owner-local namespaces

004-E also assigns IDs to a deliberately small set of owner-local rules:

```text
COMP-001  Competition lifecycle
COMP-002  Post-finalization correction does not roll lifecycle backward

ACC-001   Access is contextual; Identity/role alone is insufficient
ACC-002   Access capability does not transfer semantic authority

SC-001    A complete Draft remains non-authoritative
SC-002    Amendment Draft preserves prior Finalized authority until successor Finalization
SC-003    Structural Scorecard identity is not changed by ordinary amendment

EVAL-001  Baseline equal weighting of eligible authoritative individual Judge Scorecards
EVAL-002  Incompatible Rubric semantics are not silently pooled or rescaled
EVAL-003  Outcome-affecting Evaluation Policy is reconstructible once judging begins

RANK-001  Rank is derived and never directly edited
RANK-002  Precision and tie resolution follow declared policy, never hidden implementation order

OUT-001   Competition Finalization establishes an Official Outcome Revision
OUT-002   Corrected calculations require explicit successor-revision confirmation to change official outcome

DISC-001  Blinded Judge Team identity is Alias + Division; administrative identity/Team Name are hidden by default
DISC-002  Disclosure is audience/purpose-specific; Organizer visibility does not imply Export/public visibility

EXPORT-001 Export represents identified source state and never becomes source truth
EXPORT-002 Export generation and publication are distinct operations
```

# 11. Restatement-reduction retrofit

The canonical owners above are rewritten so repeated cross-cutting rules point to the appropriate `INV-*` owner rather than restating complete bodies.

Examples:

- Scorecard links to `INV-002` for logical uniqueness/evaluation weight and `INV-004` for Judge authorship;
- Evaluation Policy links to `INV-003` instead of independently owning “missing is never zero”;
- Rank links to `INV-006` for calculated-versus-official semantics;
- Official Outcome Revision links to `INV-006` and `INV-007` rather than copying those complete rules;
- Anonymity & Disclosure links to `INV-001` for peer-result non-disclosure;
- Export links to `INV-007` for Finalization/publication separation.

This preserves local comprehension while removing competing normative ownership.

# 12. Historical phase records are not rewritten for deduplication

Phase 001–003 records intentionally contain historical restatement because they document how understanding evolved and because many were designed to be independently auditable phase artifacts.

004-E does not rewrite those bodies simply to make them shorter.

Reference-first reduction applies primarily to current canonical knowledge and all future downstream architecture/implementation documentation.

# 13. Future architecture citation contract

Phase 005 architecture should cite stable rules directly.

Example:

```text
Persistence design must satisfy:
- SC-001
- SC-002
- INV-002
- INV-010
```

The architecture document then explains how its mechanism satisfies those constraints rather than reproducing their definitions.

Tests may use the same IDs in names, metadata, traceability matrices, or acceptance criteria where useful.

# 14. Change-impact contract

Changing an identified rule requires more discipline than editing ordinary explanatory prose.

A change must consider:

- whether the semantic meaning is still compatible with the existing ID;
- which canonical documents reference the rule;
- which architecture/contracts/tests cite the ID;
- whether historical source lineage changes;
- whether dependent documentation needs review even when no wording copy exists.

004-F defines the governance process and 004-H adds automated structural checks.

# 15. Migration findings

The ID/restatement retrofit exposed no contradictory canonical ownership.

The main duplicated rules found were already concentrated around the intended invariants: Judge independence, one logical Scorecard, missing/zero distinction, Judge authorship, calculated/official separation, publication separation, capture parity, accessibility parity, and uncertainty semantics.

Those now have explicit stable owners rather than relying on repeated prose equivalence.

# Deliberate deferrals

004-E does not finalize:

- agent/repository governance and change-review procedure — 004-F;
- full OKF metadata/trust/verification/lifecycle profile — 004-G;
- automated duplicate-ID/link/backlink validation — 004-H;
- repository-wide final drift closure — 004-I.

# Exit position

Canonical MUDAC knowledge now supports precise, stable cross-reference from future architecture, implementation, tests, and agents without requiring downstream documents to duplicate upstream rules.

004-E passes cross-reference/restatement review and hands off to **004-F — Documentation Governance, Agent Context & Anti-Drift Rules**.

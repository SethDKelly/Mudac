---
type: Design Phase Record
title: 004-D — Historical Phase Migration, Provenance & Source-Lineage Retrofit
description: Preserve numbered design history while making backward and forward knowledge lineage explicit between historical phase records and current canonical owners.
status: stable
tags: [phase-004, okf, provenance, lineage, history]
sources:
  - resource: 004-A-okf-adoption-authority-methodology-compatibility-terminology-contract.md
  - resource: 004-B-knowledge-bundle-topology-canonical-authority-layers-progressive-disclosure.md
  - resource: 004-C-canonical-concept-policy-invariant-experience-knowledge-extraction.md
  - resource: ../001-concept-design/001-H-phase-consolidation-initial-concept-catalog.md
  - resource: ../002-concept-specification/002-I-phase-consolidation-specification-exit-review.md
  - resource: ../003-conceptual-ux-architecture/003-J-phase-consolidation-ux-architecture-exit-review.md
---

# Purpose

004-D makes the relationship between MUDAC's design history and its new canonical knowledge layer explicit without rewriting or relocating the historical phase corpus.

The problem is not that the Phase 001–003 records lack value. They contain the rationale, tradeoffs, rejected alternatives, pressure tests, and chronology that explain why the current design exists. The problem is that, after 004-C, those records should no longer compete with concise canonical owners as the ordinary retrieval surface for current truth.

The governing objective is:

> Preserve historical design evidence as durable provenance while making it easy to move in both directions: from current canonical knowledge back to the records that produced it, and from a historical phase record forward to the current knowledge that succeeded it.

# 1. Historical records remain evidence, not obsolete clutter

Numbered phase records continue to serve as authoritative evidence of design evolution.

They are retained for:

- rationale and tradeoff reconstruction;
- discovery chronology;
- rejected alternatives;
- pressure tests and exit reviews;
- reconstructing when a rule entered or changed the design;
- reviewing whether a later canonical extraction preserved meaning;
- audit of later architecture decisions against original product intent.

A historical record does not become incorrect merely because a canonical successor now exists.

The authority distinction is temporal and functional:

```text
historical phase record
    explains how / why / when

canonical knowledge document
    states current accepted meaning
```

# 2. No physical history migration

004-D reaffirms the 004-B decision that historical records remain at their established paths:

```text
docs/001-concept-design/
docs/002-concept-specification/
docs/003-conceptual-ux-architecture/
docs/004-knowledge-architecture/
```

There is no synthetic `docs/history/` relocation.

Path preservation protects existing Markdown links, commit history, citations, external references, and human bookmarks. The historical role is expressed by the knowledge graph and phase indexes, not by moving files into a different directory.

# 3. Bidirectional lineage model

MUDAC now represents lineage in two complementary directions.

## Canonical → historical

Canonical OKF knowledge documents use `sources[].resource` to identify material phase records from which the current knowledge was derived.

Conceptually:

```text
canonical/concepts/scorecard.md
        ↓ sources
002-D
002-E
002-I
```

This is the preferred path when a consumer starts from current truth and needs rationale or provenance.

## Historical → canonical

Each numbered phase directory now receives an OKF `index.md` that identifies the phase records and the canonical subjects they materially produced, refined, or validated.

Conceptually:

```text
002-F
  Aggregation, Coverage, Ranking & Evaluation Policy
        ↓ current successors
canonical/mechanisms/aggregate.md
canonical/mechanisms/coverage.md
canonical/mechanisms/rank.md
canonical/policies/evaluation-policy.md
```

This is the preferred path when a consumer starts from history and asks, “Where does this rule live now?”

# 4. Lineage is not duplication

Lineage maps identify relationships; they do not restate the complete rule bodies.

A phase index may say that 002-D materially feeds `Scorecard`, `Rubric`, `Criterion & Notes`, and the one-logical-Scorecard invariant. It should not copy those current contracts into the index.

Likewise, a canonical document should name the historical sources that materially support it rather than reproducing the entire phase rationale.

The model is:

```text
phase record
   ↘
    lineage edge ──→ canonical owner
   ↗
canonical source metadata
```

not:

```text
historical prose copied into canonical prose
```

# 5. Material-source rule

A canonical document's `sources` list is not intended to contain every phase file that ever mentioned the subject.

A historical source should be included when it materially:

- introduced the subject;
- established or changed its boundary;
- specified authoritative behavior;
- established a governing policy or invariant;
- pressure-tested/refined the current contract;
- served as the accepted phase exit that confirmed the result.

Incidental repetition is not source lineage.

This keeps provenance useful rather than turning `sources` into a full-text occurrence index.

# 6. Primary versus consolidating historical sources

Historical lineage commonly contains both detailed and consolidating sources.

Example:

```text
002-D
    primary behavioral specification for Scorecard

002-I
    phase-level confirmation that Scorecard composes coherently
```

Both may be valid sources, but they serve different purposes.

MUDAC does not invent a credibility score or rank them numerically. Consumers can infer their role from title, phase position, and the linked content.

A future metadata profile may add MUDAC-specific source-role metadata if it proves useful, but 004-D does not create an unnecessary custom schema before 004-G.

# 7. Exit reviews remain especially important provenance

Phase exit documents such as 001-H, 002-I, and 003-J remain high-value historical sources because they record whether the phase passed, what seams were tested, what remained deferred, and whether any Concept changes were required.

They are not substitutes for the more specific source records when detailed rationale matters.

The normal pattern is therefore:

```text
specific phase record
        +
phase exit record
        ↓
canonical current owner
```

where both materially contribute.

# 8. Compatible post-exit refinements remain visible

A compatible refinement such as `002-A1 — Team Extensible Attributes & Team Name` remains explicit lineage rather than being hidden beneath the older phase exit.

For Team and Team Attributes, 002-A1 is a material source even though it occurred after 002-I.

This establishes a general rule:

> Phase exits are consolidation checkpoints, not a mechanism for erasing compatible later refinements.

A canonical owner must point to the material refinement when the refinement contributes current truth.

# 9. Historical files are preserved before metadata normalization

004-D deliberately does **not** bulk-rewrite the bodies of Phase 001–003 records merely to add modern metadata.

Those files are evidence artifacts, and large mechanical rewrites would create noisy diffs that reduce the usefulness of Git history.

Instead, this group adds phase-level `index.md` lineage maps and preserves existing record paths/content.

The later 004-G metadata profile will decide how much frontmatter normalization should be applied to legacy phase records, including `generated`, `verified`, lifecycle/freshness fields, and whether some legacy records should be treated as source resources rather than fully normalized concept documents.

Until then, the absence of OKF metadata on a historical record must not be interpreted as loss of historical authority.

# 10. Canonical provenance remains OKF knowledge provenance

The `sources` relationships introduced by 004-C and governed here describe **documentation lineage**.

They do not replace the MUDAC Provenance Concept.

```text
OKF/source lineage
    Why does this knowledge document say this?

MUDAC Provenance Concept
    How and through whose authority did Competition-domain state arise or change?
```

The canonical [Provenance Concept](../canonical/concepts/provenance.md) is itself sourced from historical design records using OKF provenance.

# 11. Forward-lineage phase indexes

004-D adds `index.md` files to the numbered phase directories.

These indexes serve four purposes:

1. progressive disclosure within design history;
2. concise description of each historical record;
3. explicit identification of current canonical successors;
4. a warning that historical records are rationale/provenance rather than the default current-rule owners after 004-C.

Existing `README.md` files remain as compatibility/human phase summaries where already present. `index.md` becomes the OKF navigation surface.

# 12. Phase lineage granularity

Forward lineage is recorded at the level needed to answer a practical retrieval question.

A phase record may point to:

- one canonical Concept;
- several related canonical owners;
- a category index when the record was broad discovery/consolidation work;
- no current canonical successor when the record is primarily methodology/history rather than a product rule.

The absence of a successor does not mean the historical record is unimportant.

# 13. Canonical-source completeness expectation

After 004-D, every baseline canonical product/UX knowledge document should have at least one material historical `sources` relationship, and phase indexes should make the major forward lineage discoverable.

004-D does not claim that the source graph is permanently exhaustive. Later design phases will add new sources when they deliberately refine canonical knowledge.

The maintenance rule is:

```text
canonical meaning changes
        ↓
update canonical body
        +
update material sources
        +
review dependents
```

The dependent-review mechanism is developed further in 004-E/004-F/004-H.

# 14. Historical-path stability

Because canonical documents may cite historical records directly, historical paths are now part of the knowledge-lineage interface.

Moving or renaming a historical phase record requires:

- updating canonical `sources` references;
- updating phase indexes and internal links;
- validating downstream links;
- preserving enough Git history to reconstruct the change.

Ordinary cleanup is therefore not sufficient reason to rename historical artifacts.

# 15. Corrections to history

Historical phase records should generally be treated as append-stable evidence.

If a historical document contains a typo or broken link, a narrow correction may be appropriate.

If later work discovers that the historical **decision itself** was wrong, the preferred pattern is not to rewrite the record as though the earlier decision never happened. Instead:

```text
historical decision
        ↓
explicit later refinement / superseding phase record
        ↓
canonical owner updated
```

This preserves design provenance.

# 16. Supersession is semantic, not destructive

A canonical owner may supersede a historical rule for current interpretation while the historical record remains valid evidence of what was once accepted.

Likewise, a later canonical refinement may supersede an earlier canonical statement without requiring deletion of the historical phase source.

The words `superseded` and `deprecated` should apply to the relevant knowledge artifact/meaning, not erase history.

Detailed OKF lifecycle conventions are deferred to 004-G.

# 17. Agent retrieval contract for history

When current meaning is required, agents should continue to follow:

```text
docs/index.md
      ↓
canonical category
      ↓
canonical owner
```

History is loaded when the task requires:

- rationale;
- rejected alternatives;
- decision chronology;
- audit of a canonical extraction;
- understanding why a boundary exists;
- comparison of old and current design.

When entering history, agents should start with that phase's `index.md` and open only the relevant record(s).

# 18. Source-lineage graph after 004-D

The intended knowledge graph is now:

```text
external authority / methodology
            ↓
      Phase design work
            ↓
 historical phase records
       ↘         ↙
        sources / successors
            ↓
   canonical current knowledge
            ↓
 future architecture contracts
            ↓
 implementation / tests / ops
```

The arrows do not imply that later layers can rewrite upstream meaning. They show derivation and constraint.

# 19. Migration findings

The lineage retrofit exposed no contradiction requiring product redesign.

The following remained coherent:

- the 15-Concept catalog;
- Team Name as a compatible Team-attribute refinement;
- Phase 002 behavioral seams;
- Phase 003 UX contracts;
- canonical-versus-historical authority;
- the distinction between OKF provenance and MUDAC Provenance.

No historical path needed relocation.

# 20. Deliberate deferrals

004-D does not finalize:

- stable normative rule IDs — 004-E;
- broad replacement of duplicated restatement with links — 004-E;
- agent/repository governance rules — 004-F;
- complete OKF trust/generation/verification/lifecycle/freshness profile — 004-G;
- automated backlink/source/link validation — 004-H;
- final repository-wide drift audit — 004-I.

# Exit position

Historical design is now a navigable provenance layer rather than a competing current-knowledge layer.

Consumers can move backward from canonical knowledge through `sources`, forward from historical phase indexes to current canonical successors, and retain the original phase chronology without path churn or destructive rewriting.

004-D therefore passes lineage retrofit review and hands off to **004-E — Cross-Reference, Stable Rule-ID & Restatement Reduction Retrofit**.
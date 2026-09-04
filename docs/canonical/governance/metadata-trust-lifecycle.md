---
type: Documentation Authority
title: OKF Metadata, Trust, Verification, Lifecycle & Freshness
description: Defines the MUDAC profile for OKF provenance, generation, verification, lifecycle, freshness, actor identity, and legacy-metadata handling.
status: stable
tags: [governance, okf, metadata, trust, verification, lifecycle, freshness]
sources:
  - resource: ../../004-knowledge-architecture/004-A-okf-adoption-authority-methodology-compatibility-terminology-contract.md
  - resource: ../../004-knowledge-architecture/004-D-historical-phase-migration-provenance-source-lineage-retrofit.md
  - resource: ../../004-knowledge-architecture/004-F-documentation-governance-agent-context-anti-drift-rules.md
  - resource: ../../references/open-knowledge-format.md
generated: { by: openai/gpt-5.6-sol, at: 2026-09-04T03:30:09Z }
---

# Purpose

Define how MUDAC uses OKF v0.2 metadata to communicate where knowledge came from, who produced it, whether it has actually been verified, whether the artifact is current in its knowledge lifecycle, and whether a time-sensitive assertion should be treated as stale.

This metadata describes the **knowledge artifact**. It does not replace MUDAC domain state, authorization, semantic authority, or design-governance precedence.

<a id="meta-001"></a>
## META-001 — Canonical knowledge uses a deliberate MUDAC frontmatter profile

Substantive current knowledge under `docs/canonical/` should use:

- `type` — required by OKF and descriptive of the MUDAC knowledge role;
- `title` — human-readable owner name;
- `description` — concise retrieval summary;
- `status` — explicit knowledge-artifact lifecycle;
- `tags` — useful cross-cutting retrieval labels;
- `sources` — material provenance for how the current knowledge was derived.

`resource`, `generated`, `verified`, and `stale_after` are used according to the rules below. `index.md` remains a reserved routing document rather than a concept document and does not receive ordinary concept frontmatter; the bundle-root `docs/index.md` may carry `okf_version`.

MUDAC does not add custom metadata fields merely because OKF allows extensions. New producer-defined keys require a concrete machine-readable governance need that links/prose cannot satisfy.

<a id="meta-002"></a>
## META-002 — `generated` records the actual producer of the current meaningful content

`generated.by` identifies who or what produced the current meaningful content, and `generated.at` records its last meaningful change.

MUDAC uses the OKF actor convention:

- `<producer>/<version>` for an agent/tool, for example `openai/gpt-5.6-sol`;
- `human:<id>` for a person;
- `process:<id>` for an automated process.

Generation identity is distinct from Git author/committer identity. An agent-generated document committed through a human Git identity remains agent-generated unless the human materially rewrites the content.

New canonical documents and new phase records should record `generated` when the producer/time are known. Once present, a meaningful content change updates `generated` to the producer/time responsible for that new content.

Purely mechanical formatting, typo, or link repair that does not meaningfully change content need not advance `generated.at`.

Do not guess or retroactively manufacture a producer/timestamp merely to fill metadata.

<a id="meta-003"></a>
## META-003 — `verified` records an actual content/source confirmation event

`verified` is optional and must correspond to a real verification event in which the verifier checked the current content against its declared source(s), resource, or accepted authoritative basis.

The following do **not** by themselves constitute OKF verification:

- committing or merging a file;
- a phase being marked Complete;
- a user saying to proceed to the next subgroup;
- CI syntax/link/frontmatter validation;
- successful generation by an agent;
- a test suite passing against implementation behavior.

A human review is recorded only when a human actually performs/declares that review. A machine verification is recorded only when an agent/process actually checks the content against its basis.

If meaningful content changes after an existing verification, verification entries that are not known to cover the changed content must not be silently carried forward. Git history preserves the old verification event; current frontmatter should represent verification of the **current** content. A verifier may then re-check the changed content and record a new event.

Independent verification is preferred for high-consequence semantic changes, but OKF trust tier and MUDAC authority remain separate concerns.

<a id="meta-004"></a>
## META-004 — OKF `status` describes knowledge-artifact lifecycle, not MUDAC domain state

MUDAC uses the OKF v0.2 lifecycle values exactly:

- `draft` — not yet ready for ordinary consumption; potentially incomplete;
- `stable` — ready for consumption/current in its knowledge role;
- `deprecated` — retained for links/history but no longer current in that role.

`stable` does **not** mean human-reviewed. Trust is expressed separately through `verified`.

`status` must never be used for Competition lifecycle values such as Ready, Active, Event Completed, or Finalized.

Completed historical phase records are not deprecated merely because canonical current knowledge now exists. They remain stable **historical evidence** in their provenance role. Conversely, a canonical owner that has been replaced may be `deprecated` while remaining addressable for historical links.

When a canonical document is deprecated, its body/index should point to the current successor. MUDAC does not introduce a custom supersession frontmatter schema in the baseline profile; ordinary links plus `status: deprecated` are sufficient unless a later automation requirement proves otherwise.

<a id="meta-005"></a>
## META-005 — `stale_after` is used only for a real absolute freshness boundary

`stale_after` is an optional absolute ISO 8601 instant. Use it only when the knowledge genuinely becomes stale on/after a known time.

Do not assign arbitrary TTLs such as “review every six months” to durable Concepts, invariants, or design policies merely to create activity.

A document becoming stale does not automatically make it deprecated, invalid, inaccessible, or non-authoritative. Staleness is a review/freshness signal. Consumers must surface it and determine consequence from the subject's governance.

A new upstream standard/version does not automatically make a pinned MUDAC adoption profile stale: MUDAC adoption changes through explicit review. Where upstream recency matters, prefer a pinned source resource plus factual source `last_modified` when known.

<a id="meta-006"></a>
## META-006 — Source credibility metadata must remain factual and material

`sources` follows the material-source rule in [Source Lineage](source-lineage.md): inclusion means the source materially introduced, specified, refined, pressure-tested, or confirmed the current knowledge—not merely that it mentions the same noun.

Optional source credibility signals such as `author`, `usage_count`, `usage_window`, and `last_modified` are recorded only when objectively known. MUDAC does not invent usage counts, freshness dates, credibility scores, or source authors to make metadata look complete.

Use `sources[].id` when claim-level attribution is materially useful. Do not assign source IDs solely for decorative uniformity.

<a id="meta-007"></a>
## META-007 — OKF trust signals are advisory and do not replace MUDAC authority or Access

OKF derives trust tier from `verified`:

- no `verified` → unverified;
- non-human verification only → machine-confirmed;
- any `human:<id>` verification → human-reviewed.

MUDAC does not reinterpret those tiers.

A canonical owner may be `status: stable` and unverified in OKF trust terms while still being the current MUDAC authority under [DOC-001](documentation-authority.md#doc-001). Conversely, a human-reviewed document does not gain Access privileges or authority to override another canonical owner.

Trust tier is not authentication, authorization, policy approval, Competition Finalization, or domain Provenance.

<a id="meta-008"></a>
## META-008 — Legacy records are not bulk-rewritten or speculatively backfilled for metadata completeness

Phase 001–003 historical records predate the OKF retrofit and often have no frontmatter. Their historical authority is established by preserved paths, Git history, phase indexes, and source lineage; missing OKF metadata does not make them less valid as evidence.

MUDAC will not bulk-rewrite those bodies merely to add `type`, `generated`, `verified`, or `status` where doing so creates noisy history or requires guessing.

Likewise, pre-004-G canonical/Phase 004 documents are not retroactively assigned `generated` or `verified` unless the producer/verification event can be established confidently and the metadata update has real value.

New documents and future meaningful edits follow the profile prospectively.

<a id="meta-009"></a>
## META-009 — Metadata updates must preserve semantic and historical distinctions

A metadata edit must not silently change product meaning or design authority.

Examples:

- changing `status: stable` to `deprecated` is a knowledge-lifecycle decision and requires a current-successor path;
- adding `verified` requires an actual verification event;
- advancing `generated.at` without meaningful content change is unnecessary churn;
- setting `stale_after` must reflect a real absolute freshness boundary;
- removing or changing material `sources` may alter knowledge provenance and therefore requires appropriate review.

Metadata is part of the knowledge contract and is subject to [Canonical Change & Conflict Governance](change-governance.md) where the change affects authority, provenance, or interpretation.

# `log.md` convention

OKF reserves optional `log.md` files for chronological update history. MUDAC does **not** create a bundle-level `docs/log.md` merely for formal completeness.

Git history plus numbered phase records already provide detailed chronology and attribution. A manually duplicated bundle changelog would create another maintenance surface and drift risk.

A future `log.md` may be added if a concrete consumer needs a curated knowledge-update feed that Git/phase history cannot provide. If introduced, it should summarize and link changes rather than become another semantic authority layer.

# Prospective canonical example

```yaml
---
type: Design Policy
title: Example Policy
description: Example current MUDAC policy owner.
status: stable
tags: [policy]
sources:
  - resource: ../../005-system-architecture/example-source.md
generated: { by: openai/gpt-5.6-sol, at: 2026-09-04T03:30:09Z }
---
```

No `verified` key means the current content is unverified in OKF trust-tier terms. That is explicit rather than an error.

# Verification after a meaningful change

If the document had previously contained:

```yaml
verified: { by: human:reviewer, at: 2026-09-05T15:00:00Z }
```

and later receives a meaningful semantic change, the old verification is not automatically copied into the new current frontmatter. After the reviewer checks the changed content, the new verification event may be recorded.

# Legacy profile

For preserved historical records without OKF frontmatter:

```text
legacy phase body + Git history + phase index + canonical source lineage
        = valid historical evidence
```

The retrofit does not require rewriting that body to manufacture modern metadata.

# Relationship to validation tooling

004-H will validate structural properties such as:

- allowed/required frontmatter fields for applicable MUDAC document classes;
- timestamp syntax;
- actor-shape syntax where present;
- lifecycle values;
- source/link resolution where appropriate;
- stable-ID uniqueness.

Those checks must not add `verified` merely because the file is structurally valid.

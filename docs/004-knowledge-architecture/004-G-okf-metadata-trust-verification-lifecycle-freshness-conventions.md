---
type: Design Phase Record
title: 004-G — OKF Metadata, Trust, Verification, Lifecycle & Freshness Conventions
description: Establish the MUDAC profile for OKF provenance, generation, verification, trust tiers, lifecycle status, freshness, actor identity, and legacy metadata handling.
status: stable
tags: [phase-004, okf, metadata, trust, verification, lifecycle, freshness]
sources:
  - resource: 004-A-okf-adoption-authority-methodology-compatibility-terminology-contract.md
  - resource: 004-D-historical-phase-migration-provenance-source-lineage-retrofit.md
  - resource: 004-F-documentation-governance-agent-context-anti-drift-rules.md
  - resource: ../references/open-knowledge-format.md
generated: { by: openai/gpt-5.6-sol, at: 2026-09-04T03:26:36Z }
---

# Purpose

004-G defines how MUDAC uses the OKF v0.2 metadata families that answer four different questions:

```text
sources
    where did this knowledge come from?

generated
    who/what produced the current meaningful content, and when?

verified
    who/what actually confirmed the current content against its basis?

status / stale_after
    is this knowledge artifact current in its lifecycle, and is it still fresh?
```

The governing objective is:

> Metadata must increase trust and maintainability by describing real knowledge events; it must never manufacture confidence, conflate documentation state with Competition state, or rewrite historical evidence merely to make the corpus look uniformly modern.

# 1. Upstream OKF authority verified

004-G rechecked the dedicated `GoogleCloudPlatform/open-knowledge-format` repository rather than the frozen legacy `knowledge-catalog/okf` copy.

The upstream specification identifies itself as **OKF Version 0.2** and defines:

- `sources` as provenance;
- `generated` as current-content production attribution;
- `verified` as confirmation events;
- derived trust tiers: unverified, machine-confirmed, human-reviewed;
- `status: draft | stable | deprecated`;
- `stale_after` as an absolute timestamp after which content is stale;
- the actor convention for agents/tools, humans, and automated processes.

The MUDAC reference is pinned at [Open Knowledge Format v0.2](../references/open-knowledge-format.md) rather than allowing future upstream changes to silently alter the adopted contract.

# 2. Metadata is artifact metadata, not application-domain state

The most important semantic boundary is:

```text
OKF status / trust / freshness
        ≠
MUDAC Competition state / Access / authority / Provenance
```

Examples:

- `status: stable` does not mean Competition Ready or Finalized;
- `verified: human:*` does not grant Organizer/Judge Access;
- `generated.by` does not establish Judge authorship;
- OKF `sources` does not replace the MUDAC Provenance Concept;
- `stale_after` does not invalidate a Scorecard or Official Outcome Revision.

# 3. MUDAC canonical frontmatter profile

For substantive current documents under `docs/canonical/`, MUDAC expects:

```yaml
type: ...
title: ...
description: ...
status: ...
tags: [...]
sources:
  - resource: ...
```

`resource`, `generated`, `verified`, and `stale_after` are conditional rather than decorative requirements.

`index.md` remains routing/progressive-disclosure content and is not converted into a concept document. The bundle-root `docs/index.md` may carry `okf_version` as defined by OKF.

# 4. Generation provenance

`generated` records the producer responsible for the current meaningful content.

The current MUDAC actor convention follows OKF:

```text
agent/tool       <producer>/<version>
human            human:<id>
automation       process:<id>
```

For example:

```yaml
generated: { by: openai/gpt-5.6-sol, at: 2026-09-04T03:26:36Z }
```

Generation identity is not inferred from the Git committer. If an agent writes a document and a human's Git identity commits it, the content remains agent-generated unless the human materially rewrites it.

From 004-G forward, new canonical documents and phase records should capture generation metadata when producer/time are known. Meaningful edits update it. Mechanical typo/link/format repair need not create meaningless timestamp churn.

# 5. No speculative generation backfill

The pre-004-G corpus does not receive fabricated `generated` metadata.

Although Git may reveal commit author/time, that does not prove who actually generated the prose. Earlier canonical extraction was performed through agent-assisted work but the repository did not yet have an adopted actor-attribution convention.

Therefore:

> Unknown historical generation metadata remains unknown.

This is preferable to false precision.

# 6. Verification means actual verification

`verified` is stronger than acceptance, publication, or structural validation.

A verification event means the current content was actually checked against its declared sources/resource/accepted basis by the named verifier.

It is **not** automatically created by:

- a Git commit or merge;
- a passing CI workflow;
- completing a phase;
- advancing to the next phase;
- an agent generating the document;
- a human saying “proceed” without performing a content verification;
- implementation tests passing.

This preserves the credibility of the OKF trust-tier signal.

# 7. Verification after content change

A meaningful content change must not inherit old verification blindly.

Preferred current-state behavior:

```text
content v1
verified by human A
        ↓
meaningful content change
        ↓
content v2 generated
verification no longer asserted
        ↓
actual re-check
        ↓
new verification event
```

Git history already preserves that v1 had been verified. Current frontmatter should describe trust in v2, not keep a human-reviewed badge merely because an older version was reviewed.

Independent verification is preferred where consequences are high, but 004-G does not require a second actor for every documentation change.

# 8. Trust tier remains advisory

OKF derives trust tier from `verified`:

```text
no verified                  unverified
non-human verifier(s)        machine-confirmed
human:<id> verifier present  human-reviewed
```

MUDAC uses this definition without inventing another score.

Critically:

```text
current canonical authority
        ≠
OKF trust tier
```

A `status: stable` canonical document with no `verified` key remains the current MUDAC owner under documentation governance; it simply carries an explicit unverified trust signal.

Likewise, a human-reviewed historical or downstream document cannot override a different canonical owner merely because it has a higher trust tier.

# 9. Structural validation is not semantic verification

004-H will add deterministic checks for frontmatter, timestamps, links, IDs, and related structure.

Those processes may prove that:

```text
metadata parses
links resolve
rule IDs are unique
required fields exist
```

They do **not** prove that the product/design statements are correct relative to their sources.

Therefore CI must not append `verified` merely because conformance checks pass.

# 10. Lifecycle status profile

MUDAC uses OKF's lifecycle values without extensions:

```text
draft
stable
deprecated
```

Their meanings are knowledge-artifact meanings:

- **draft** — unfinished/not ready for ordinary consumption;
- **stable** — ready/current in the document's role;
- **deprecated** — no longer current in that role, retained for history/links.

MUDAC does not add `complete`, `active`, `finalized`, `historical`, or other application/phase vocabulary as OKF status values.

# 11. Stable does not mean verified

OKF deliberately separates lifecycle from trust.

Therefore:

```text
status: stable
verified: absent
```

is valid and means:

```text
ready/current for consumption
+
unverified trust tier
```

This is the correct interpretation of much of the canonical MUDAC corpus today.

# 12. Historical does not mean deprecated

Phase 001–003 documents remain current **as historical evidence**.

They no longer own current product meaning where a canonical successor exists, but they still correctly represent what the accepted design record said at that point.

So the model is:

```text
canonical Scorecard
    current semantic owner

002-D
    stable historical specification evidence
```

not:

```text
002-D = deprecated because old
```

If legacy phase files are ever normalized individually, their knowledge role should be preserved rather than mislabeled merely because newer phases exist.

# 13. Canonical deprecation and supersession

A canonical document becomes `deprecated` when it no longer owns current knowledge but must remain addressable for links/history.

Baseline behavior:

1. retain the document/path when historical links matter;
2. set `status: deprecated`;
3. state the replacement/successor prominently in the body/index;
4. preserve retired stable-rule IDs and never reuse them;
5. update current routing so consumers reach the successor.

004-G deliberately does not create custom `superseded_by`/`supersedes` YAML fields yet. Ordinary Markdown links plus lifecycle status are sufficient and remain consistent with OKF minimalism. A custom machine-readable field can be introduced later if a real automation requirement justifies it.

# 14. Freshness through `stale_after`

`stale_after` is an absolute instant, not a relative TTL.

MUDAC uses it only where there is a defensible statement:

> On or after this specific instant, the content should be treated as stale until reviewed/regenerated.

It should not be scattered across durable Concepts or invariants simply to force periodic maintenance.

Good future candidates may include time-bounded external operational references or environment-specific assumptions with a known end/review date.

# 15. Stale is distinct from deprecated

A stale document may still be the current owner pending review.

```text
status: stable
stale_after: passed
```

means the consumer must surface a freshness concern. It does not silently change lifecycle to deprecated.

Whether stale knowledge may still be used is subject-specific; the metadata itself does not invent a new authority transition.

# 16. Upstream evolution does not silently stale a pinned adoption

MUDAC adopts OKF **v0.2** deliberately.

A later OKF release does not by itself make the v0.2 MUDAC profile incorrect. Instead:

```text
upstream release/change
        ↓
compatibility/adoption review
        ↓
explicit MUDAC adoption decision
```

The external OKF reference is therefore pinned to a source revision. We do not assign an arbitrary `stale_after` to it merely because upstream may change someday.

# 17. Source credibility signals

OKF permits optional per-source facts such as:

```text
author
usage_count
usage_window
last_modified
```

MUDAC records them only when objectively known and useful.

The repository will not manufacture:

- source authors;
- artificial usage counts;
- guessed modification timestamps;
- subjective credibility scores.

Source inclusion continues to follow the material-source rule established in 004-D.

# 18. Source IDs and per-claim attribution

`sources[].id` is useful when a body claim needs explicit source attribution.

MUDAC does not force IDs on every source merely for uniformity. They are used when claim-level attribution or stable source-keying materially improves traceability.

The new [Open Knowledge Format reference](../references/open-knowledge-format.md), for example, uses a stable source ID because the document directly describes a specific pinned external specification.

# 19. Legacy historical record strategy

004-D deferred whether to bulk-normalize Phase 001–003 files. 004-G resolves that question conservatively:

> Do not bulk-rewrite preserved historical bodies solely for metadata conformity.

Reasons:

- it creates large noisy diffs against evidence artifacts;
- generation actors cannot always be reconstructed accurately;
- human verification cannot be inferred retrospectively;
- phase index + Git history + canonical `sources` already establish their historical role.

Legacy absence of OKF frontmatter is therefore explicitly supported by the MUDAC migration profile.

# 20. Pre-004-G canonical metadata strategy

Existing canonical documents already use `type`, `title`, `description`, `status`, `tags`, and `sources` but usually lack `generated`/`verified`.

004-G does not mass-backfill those fields.

Future meaningful changes to those documents should adopt the prospective metadata profile at the time of change, using the actual producer and any real verification events.

This yields gradual trustworthy convergence rather than synthetic uniformity.

# 21. Metadata-change governance

Metadata edits can themselves be consequential.

Examples requiring semantic/governance awareness include:

- `stable → deprecated`;
- changing/removing material sources;
- adding a verification claim;
- adding `stale_after`;
- changing a source resource to a different authority/version.

Those changes follow the same canonical-change and impact-review discipline where authority/interpretation is affected.

# 22. New stable metadata rules

004-G introduces the `META-*` governance namespace:

```text
META-001  Canonical knowledge uses the MUDAC frontmatter profile
META-002  generated records actual current-content production
META-003  verified records actual current-content/source confirmation
META-004  status describes knowledge lifecycle, not domain state
META-005  stale_after requires a real absolute freshness boundary
META-006  source credibility metadata is factual/material only
META-007  OKF trust tier does not replace MUDAC authority or Access
META-008  legacy records are not speculatively backfilled
META-009  metadata changes preserve semantic/historical distinctions
```

The identifiers are owned by [OKF Metadata, Trust, Verification, Lifecycle & Freshness](../canonical/governance/metadata-trust-lifecycle.md) and registered in the stable-rule registry.

# 23. Migration findings

004-G found no product/UX contradiction and required no Concept change.

The principal risks were metadata-specific:

- treating `stable` as equivalent to human-reviewed;
- claiming verification from ordinary phase acceptance or CI;
- carrying old verification through meaningful content changes;
- marking old phase records deprecated simply because they are historical;
- assigning arbitrary freshness TTLs to durable design knowledge;
- guessing generation actors for pre-retrofit content;
- letting trust tier override repository authority.

The adopted profile resolves those risks explicitly.

# Deliberate deferrals

004-G does not implement:

- automated frontmatter/rule/link validation — 004-H;
- repository-wide final drift and metadata conformance audit — 004-I;
- Phase 004 overall exit review — 004-J.

# Exit position

MUDAC now has an explicit OKF v0.2 metadata profile that distinguishes provenance, production, verification, lifecycle, freshness, and authority without manufacturing trust or rewriting design history.

New knowledge can become progressively more trustable because the metadata records real events rather than decorative completeness.

004-G passes metadata/trust/lifecycle review and hands off to **004-H — Validation Tooling, Link/Authority Checks & CI Enforcement**.

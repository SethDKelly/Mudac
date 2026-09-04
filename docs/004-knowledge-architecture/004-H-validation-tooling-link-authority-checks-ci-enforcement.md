---
type: Design Phase Record
title: 004-H — Validation Tooling, Link/Authority Checks & CI Enforcement
description: Implement deterministic validation and CI enforcement for MUDAC knowledge structure, metadata, stable rule IDs, links, source edges, and progressive-disclosure routing.
status: stable
tags: [phase-004, validation, ci, links, anti-drift]
sources:
  - resource: 004-E-cross-reference-stable-rule-id-restatement-reduction-retrofit.md
  - resource: 004-F-documentation-governance-agent-context-anti-drift-rules.md
  - resource: 004-G-okf-metadata-trust-verification-lifecycle-freshness-conventions.md
generated: { by: openai/gpt-5.6-sol, at: 2026-09-04T03:35:40Z }
---

# Purpose

004-H converts the deterministic portions of Phase 004 knowledge governance into executable repository guardrails.

The governing objective is:

> Fail repository changes that structurally break the canonical knowledge graph, stable references, OKF metadata profile, or progressive-disclosure routing while preserving the distinction between machine-checkable conformance and semantic design verification.

# 1. Enforcement boundary

The validator enforces only facts that can be determined locally and reproducibly from repository content.

It checks:

- current OKF/frontmatter shape;
- lifecycle values;
- timestamp and actor syntax;
- material local source-path resolution;
- stable rule-ID uniqueness and owner/registry agreement;
- current authority/routing Markdown links;
- required progressive-disclosure surfaces;
- workflow read-only/enforcement wiring.

It does not decide whether a design rule is good, whether prose faithfully captures human intent, or whether an implementation satisfies a Concept in the semantic sense.

# 2. Canonical validation governance

Current enforcement semantics live in [Knowledge Validation & CI Enforcement](../canonical/governance/validation-enforcement.md), which introduces `VAL-001` through `VAL-008`.

The validator implementation and workflow are downstream mechanisms constrained by those rules.

# 3. Validator implementation

The repository now includes:

```text
scripts/validate_knowledge.py
requirements-docs.txt
```

The validator is Python-based and uses PyYAML only for safe YAML/frontmatter parsing. All graph/path/rule checks use the Python standard library and operate against the checked-out repository.

Normal validation performs no network calls.

External URLs are not fetched or scored; CI therefore cannot fail merely because a third-party website is temporarily unavailable.

# 4. Frontmatter enforcement

Substantive documents under:

```text
docs/canonical/
docs/references/
```

must carry the current MUDAC OKF profile established by `META-001`:

```text
type
title
description
status
tags
sources
```

When optional metadata exists, the validator checks its deterministic shape:

```text
generated
verified
stale_after
source credibility fields
usage_window
```

The validator does not require `verified` and never creates it.

# 5. Lifecycle and time checks

`status` is restricted to the adopted OKF values:

```text
draft
stable
deprecated
```

Timestamp-valued metadata must be a valid ISO 8601 datetime with an explicit UTC offset.

That applies to fields such as:

```text
generated.at
verified[].at
stale_after
sources[].last_modified
usage_window.from / to
```

This is syntax validation only. It does not establish that the timestamp corresponds to a truthful real-world event; truthful attribution remains governed by `META-*`.

# 6. Stable rule-ID checks

The validator scans canonical explicit anchors matching the stable rule-ID shape.

It requires that each stable ID:

1. occurs at one canonical owner only;
2. is immediately followed by a heading naming the same ID;
3. appears once in `rule-identifiers.md`;
4. resolves from the registry to the exact owner path and explicit anchor.

This makes duplicate IDs, unregistered rules, dead registry entries, and registry/owner disagreement blocking failures.

# 7. Link and source-edge checks

Hard link validation applies to current authority/routing surfaces:

- root `README.md` and `AGENTS.md`;
- `docs/index.md` and `docs/README.md`;
- all current canonical documents;
- external-reference documents;
- phase `index.md` / `README.md` routing surfaces;
- Phase 004 records.

Internal file/directory links must resolve.

Stable rule fragments must resolve to explicit stable anchors.

Local path-like `sources[].resource` values must resolve relative to their knowledge document or the OKF bundle root as appropriate.

HTTP/HTTPS references are not fetched in routine CI.

# 8. Historical exemptions

004-H does not make Phase 001–003 bodies retroactively conform to the current frontmatter profile.

Likewise, routine CI does not fail because a preserved historical narrative contains an old link style that has not been included in the current-authority enforcement surface.

Their phase indexes remain validated as the supported navigation layer into those records.

This follows `META-008` and preserves the append-stable history contract from 004-D/004-F.

# 9. Progressive-disclosure checks

The validator requires the routing files needed by the agent retrieval model:

```text
AGENTS.md
README.md
docs/index.md
docs/README.md
docs/canonical/index.md
docs/canonical/<category>/index.md
docs/references/index.md
docs/<numbered-phase>/index.md
```

The bundle root must explicitly declare:

```yaml
okf_version: "0.2"
```

A missing phase/category index is therefore a structural regression.

# 10. CI workflow

`.github/workflows/knowledge-validation.yml` runs validation for relevant pull requests and pushes to `main`, with manual invocation available.

The workflow uses:

```text
contents: read
```

and does not mutate repository content.

Its only job is to install the documented validator dependency and run:

```text
python scripts/validate_knowledge.py
```

A non-zero validator exit code fails the check.

# 11. Pass/fail semantics

The validator always emits an explicit reminder:

> Passing this validator is structural evidence only; it is never an OKF verified event.

This is deliberate defense against CI status being mistaken for the `verified` trust field introduced by OKF v0.2.

# 12. Warning mode and 004-I handoff

The validator has a warning channel and supports:

```text
--strict-warnings
```

Routine CI currently blocks deterministic current-authority errors.

004-I can use stricter audit behavior while examining the full repository knowledge graph. That audit may promote well-understood warning classes into routine CI errors once the existing corpus is proven compatible.

# 13. Validator governance

Because validator behavior determines what repository states CI accepts, the validator is itself governed knowledge infrastructure.

Changes to validation behavior must follow `VAL-008` and should not introduce semantic heuristics disguised as deterministic validation.

Examples of inappropriate checks include:

- deciding whether a Concept's operational principle is conceptually sound;
- inferring that a human reviewed content because a PR was merged;
- assigning credibility based on the reputation of a source URL;
- automatically changing a rule ID because wording changed;
- rewriting historical records to satisfy modern style.

Those require design/review governance, not syntax automation.

# 14. Findings

004-H did not expose a need to change MUDAC product/UX semantics or the 15-Concept catalog.

The main enforcement risks were knowledge-governance risks:

- future broken cross-references;
- duplicate or orphaned stable rule IDs;
- malformed trust/lifecycle metadata;
- missing phase/category routing;
- CI workflows acquiring write authority;
- accidental treatment of structural success as semantic verification.

The new validator and `VAL-*` governance address those risks deterministically.

# Deliberate deferrals

004-H does not perform the final repository-wide drift/conformance review. That belongs to **004-I — Repository-Wide Knowledge Graph / Drift Audit & Migration Closure**.

004-I should exercise the validator across the complete corpus, inspect remaining historical/current cross-reference asymmetries, evaluate warnings/exemptions, and decide whether the migration can be considered structurally closed before the Phase 004 exit review.

# Exit position

MUDAC now has executable, read-only CI guardrails for the machine-checkable portions of its knowledge architecture without conflating validation with trust or semantic authority.

004-H passes validation-tooling design and hands off to **004-I — Repository-Wide Knowledge Graph / Drift Audit & Migration Closure**.

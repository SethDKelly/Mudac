---
type: Documentation Authority
title: Knowledge Validation & CI Enforcement
description: Defines deterministic validation boundaries, blocking structural checks, legacy exemptions, CI behavior, and the distinction between conformance evidence and semantic verification.
status: stable
tags: [governance, validation, ci, links, anti-drift]
sources:
  - resource: ../../004-knowledge-architecture/004-E-cross-reference-stable-rule-id-restatement-reduction-retrofit.md
  - resource: ../../004-knowledge-architecture/004-F-documentation-governance-agent-context-anti-drift-rules.md
  - resource: ../../004-knowledge-architecture/004-G-okf-metadata-trust-verification-lifecycle-freshness-conventions.md
  - resource: ../../004-knowledge-architecture/004-H-validation-tooling-link-authority-checks-ci-enforcement.md
generated: { by: openai/gpt-5.6-sol, at: 2026-09-04T03:35:40Z }
---

# Purpose

Turn the structural portions of MUDAC knowledge governance into deterministic repository checks without pretending software can mechanically prove that the design is semantically correct.

The canonical validator is [`scripts/validate_knowledge.py`](../../../scripts/validate_knowledge.py). GitHub Actions runs it through [`.github/workflows/knowledge-validation.yml`](../../../.github/workflows/knowledge-validation.yml).

<a id="val-001"></a>
## VAL-001 — Validation proves structural conformance, not semantic verification

A passing validation run means only that the checked repository structures satisfy deterministic rules encoded by the validator.

It does **not** mean:

- the prose is semantically correct;
- a Concept or policy was human-reviewed;
- an architectural choice satisfies every product requirement;
- an OKF `verified` event occurred;
- a MUDAC domain state or authority decision was confirmed.

CI must never add or imply `verified` metadata merely because validation passed. This rule operationalizes [META-003](metadata-trust-lifecycle.md#meta-003).

<a id="val-002"></a>
## VAL-002 — Current canonical/reference knowledge receives deterministic metadata-shape checks

Substantive current documents under `docs/canonical/` and `docs/references/` must have parseable OKF frontmatter consistent with the MUDAC profile.

The validator checks deterministic properties such as:

- required current-knowledge keys (`type`, `title`, `description`, `status`, `tags`, `sources`);
- allowed `status` values;
- list/mapping shapes;
- ISO 8601 timestamps with explicit UTC offsets;
- actor syntax for `generated`/`verified` where present;
- source entry shape and local source-target existence where applicable.

The validator does not invent missing metadata. Legacy exemptions remain governed by [META-008](metadata-trust-lifecycle.md#meta-008).

<a id="val-003"></a>
## VAL-003 — Stable rule IDs are globally unique, explicitly anchored, and registry-resolvable

Every stable rule anchor under `docs/canonical/` must:

1. use the accepted `<namespace>-NNN` form;
2. be globally unique;
3. be followed by a heading naming the same rule ID;
4. appear exactly once in the stable rule registry;
5. resolve from the registry back to the actual owner/anchor.

The registry remains an index rather than a rule store under [DOC-005](documentation-authority.md#doc-005).

<a id="val-004"></a>
## VAL-004 — Current authority links and local source edges must resolve

Internal Markdown links on current authority/routing surfaces must resolve to an existing file or directory. Links to stable rule fragments must resolve to explicit stable anchors.

Local `sources[].resource` paths in frontmatter must resolve when they are path-like. External URLs are treated as external references and are not fetched during deterministic validation.

Phase 001–003 historical bodies are not globally rewritten merely to satisfy modern link style. Their phase indexes and current-successor routing surfaces are validated; repository-wide historical drift review belongs to 004-I.

<a id="val-005"></a>
## VAL-005 — Progressive-disclosure routing surfaces are structural requirements

The validator requires the repository entrypoints and category/phase indexes that make [CTX-001](agent-context.md#ctx-001) executable, including:

- root `AGENTS.md` and `README.md`;
- `docs/index.md` with `okf_version: "0.2"`;
- `docs/README.md`;
- canonical category indexes;
- `docs/references/index.md`;
- an `index.md` for every numbered phase directory.

Missing routing is therefore treated as a CI error rather than an optional documentation nicety.

<a id="val-006"></a>
## VAL-006 — Legacy exemptions are explicit and must not become blanket validation bypasses

Phase 001–003 records may lack OKF frontmatter because [META-008](metadata-trust-lifecycle.md#meta-008) deliberately preserves them without speculative bulk rewrite.

That exemption does not permit current canonical knowledge, current routing surfaces, or newly introduced governed artifacts to omit required structure.

When the validator must add another exemption, the exemption should be narrow, documented, and justified by canonical governance rather than encoded as an unexplained path skip.

<a id="val-007"></a>
## VAL-007 — Knowledge validation is a blocking, read-only CI check

The GitHub Actions knowledge-validation workflow runs on relevant pull requests and pushes to `main` and may be invoked manually.

The workflow:

- checks out the repository;
- installs only the validator's documented dependency set;
- executes `python scripts/validate_knowledge.py`;
- uses repository `contents: read` permission;
- fails the workflow when validator errors exist;
- never edits knowledge, creates verification metadata, or repairs files automatically.

Automatic repair would blur review/authority boundaries and is intentionally outside the CI validator.

<a id="val-008"></a>
## VAL-008 — Validator evolution is governed because the validator encodes repository policy

Changing validator behavior can change what repository states are accepted or rejected. Therefore validator/workflow changes are governance-sensitive.

A validator change should:

1. identify the canonical rule it is enforcing or the new structural risk it addresses;
2. avoid converting semantic judgment into brittle heuristics;
3. remain deterministic and network-independent for normal validation;
4. preserve legacy exemptions unless governance explicitly changes them;
5. update this contract when enforcement semantics materially change.

The validator is implementation of governance, not a higher authority than the governance documents it enforces.

# Error and warning model

Routine CI fails on **errors**. The validator also supports warnings and a `--strict-warnings` mode for broader audits.

The default distinction is:

```text
error
    deterministic violation of a current enforced contract

warning
    structurally detectable concern not yet appropriate as a routine CI blocker
```

004-I may run stricter drift analysis and decide whether additional warning classes should become errors after the existing corpus is reviewed.

# Network boundary

Normal validation performs no network calls. External URLs are syntax/reference edges only; their current availability or semantic content is not inferred from a CI run.

This keeps validation deterministic and prevents transient external failures from being confused with internal knowledge corruption.

# Relationship to future implementation CI

Phase 005 and later may add code, schema, security, accessibility, or architecture conformance checks. Those may cite stable MUDAC rules and coexist with knowledge validation, but they should not overload this validator into a universal application test runner.

The knowledge validator remains responsible for the integrity of the knowledge/governance graph itself.

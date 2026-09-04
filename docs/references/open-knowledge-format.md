---
type: External Reference
title: Open Knowledge Format v0.2
description: Pinned external reference and MUDAC adoption context for the Open Knowledge Format specification used by this repository.
resource: https://github.com/GoogleCloudPlatform/open-knowledge-format/blob/ad30107c31c06aec8a7d5636e0d1058118604e6f/SPEC.md
status: stable
tags: [reference, okf, metadata, provenance]
sources:
  - id: okf-spec-v0.2
    resource: https://github.com/GoogleCloudPlatform/open-knowledge-format/blob/ad30107c31c06aec8a7d5636e0d1058118604e6f/SPEC.md
    title: Open Knowledge Format Specification v0.2
generated: { by: openai/gpt-5.6-sol, at: 2026-09-04T03:26:36Z }
---

# Authority

MUDAC adopts **Open Knowledge Format v0.2** as its knowledge representation/navigation convention.

The pinned source above reflects upstream `GoogleCloudPlatform/open-knowledge-format` `main` at commit `ad30107c31c06aec8a7d5636e0d1058118604e6f` when 004-G was performed. MUDAC's adopted version does not float automatically with future upstream changes; a later OKF release or materially changed v0.2 interpretation requires explicit compatibility review under the Phase 004 governance model.

# Adopted semantics

MUDAC uses the v0.2 conventions for:

- Markdown concept documents with YAML frontmatter;
- `index.md` progressive disclosure and `log.md` reserved history convention;
- producer-defined `type` values;
- `sources` provenance and optional source credibility signals;
- `generated` production attribution;
- `verified` verification events and derived trust tiers;
- `status: draft | stable | deprecated`;
- absolute `stale_after` freshness boundaries;
- ordinary Markdown cross-links and bundle-relative/relative resources;
- OKF actor conventions for generation/verification metadata.

The exact MUDAC profile is governed by [OKF Metadata, Trust, Verification, Lifecycle & Freshness](../canonical/governance/metadata-trust-lifecycle.md).

# MUDAC-specific boundaries

OKF does not determine MUDAC's application Concepts, domain lifecycle, source-code architecture, Access model, or domain Provenance semantics.

MUDAC does not currently require OKF Attested Computation metadata merely because v0.2 supports it. If later architecture introduces knowledge that materially benefits from attested computation, that adoption should be designed explicitly rather than inferred from the format.

# Trust boundary

OKF trust tier is advisory metadata about a knowledge document. It is distinct from MUDAC documentation authority and from application Access/authorization.

A canonical MUDAC document may therefore be current and `status: stable` while remaining unverified in OKF trust terms. Human-reviewed metadata is only added after an actual human verification event.

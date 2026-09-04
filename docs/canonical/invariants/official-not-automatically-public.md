---
type: Design Invariant
title: Official Is Not Automatically Public
description: Internal Competition Finalization and external result publication are separate authority/disclosure operations.
status: stable
tags: [invariant, finalization, publication]
sources:
  - resource: ../../002-concept-specification/002-H-export-print-operational-continuity-external-representations.md
  - resource: ../../003-conceptual-ux-architecture/003-G-paper-capture-export-print-publication-experience.md
---

<a id="inv-007"></a>
# INV-007 — Official Is Not Automatically Public

`Competition Finalized ≠ Results Published`.

Finalization establishes an [Official Outcome Revision](../mechanisms/official-outcome-revision.md). Publication requires a separate audience/disclosure-aware [Export](../concepts/export.md) and deliberate release action.

A publication failure does not weaken official internal state. A corrected official revision does not silently rewrite already distributed prior artifacts.
---
type: Architecture Decision
title: 019-H — Artifact, Export, Publication, External Representation & Delivery Architecture
description: "Resolves ADQ-007 by comparing unchanged historical REP architecture, transient generation, mutable latest-file publication, database-contained binary storage, and immutable durable artifacts behind authoritative relational metadata with explicit Publication and delivery separation."
status: stable
tags: [phase-019, architecture, adq-007, artifact, export, publication, representation, delivery]
sources:
  - resource: ../canonical/architecture/artifact-export-publication-delivery.md
  - resource: ../canonical/architecture/external-representation.md
  - resource: ../canonical/architecture/persistence-history-recovery.md
  - resource: ../canonical/architecture/identity-access-authority.md
  - resource: ../canonical/architecture/interface-command-concurrency.md
  - resource: ../canonical/architecture/offline-continuity-reconciliation.md
  - resource: ../canonical/concepts/export.md
  - resource: ../canonical/concepts/publication.md
  - resource: ../canonical/synchronizations/external-representation-publication-release.md
  - resource: ../canonical/experience/external-representation-release.md
  - resource: ../canonical/invariants/current-vs-historical-truth.md
  - resource: ../canonical/invariants/official-not-automatically-public.md
  - resource: ../canonical/governance/downstream-realization-obligations.md
  - resource: ../routing/phase019_architecture_decision_control.json
generated: { by: openai/gpt-5.6-sol, at: 2026-09-22T12:45:00-05:00 }
---

# Purpose

019-H resolves ADQ-007: how exact source authority becomes stable Export representations, durable Artifact bytes, explicit Publication releases and downstream delivery without allowing files, URLs, caches, print jobs or possession to replace semantic authority.

# Entry state

~~~text
Phase 019                       ACTIVE
019-A/B/C/D/E/F/G               COMPLETE
019-H                           NEXT ELIGIBLE / USER AUTHORIZED
ADQ-001..006                    ACCEPTED
ADQ-007                         PLANNED
ADQ-008..010                    PLANNED
Q4R-001 / Q4R-002 / Q4R-003    COMPLETE
Q4R-004                         REQUIRED FOR 019-I
Q4 repairs complete             3 / 4
technical probes                0
accepted whole architecture     false
implementation packages         0
implementation execution        false
~~~

ADQ-007 has no blocking Q4 repair. The historical external-representation candidate is qualified comparison input only.

# Decision

**ADQ-007 — ACCEPTED.**

Selected architecture:

> **Exact-source Export records in relational authority; immutable integrity-addressed Artifact bytes in provider-neutral object/blob storage behind authoritative metadata; complete-surface disclosure validation; idempotent/retryable generation with asynchronous completion where justified; explicit Publication bound to exact representations; source-change affectedness without historical rewrite; successor-based replacement; withdrawal without external-recall fiction; and non-authoritative delivery.**

Current owner:

> docs/canonical/architecture/artifact-export-publication-delivery.md

Stable rules:

> ART-001 through ART-020

# Constraints preserved

ADQ-007 preserves ENG-006/010/011/014/015/017, EXPORT-001/002/003, PUB-001, INV-005/007, accepted PST history/provenance rules, CMD transaction/idempotency/reconciliation rules, current IAM authority and RCV degraded-continuity boundaries.

# Historical candidate treatment

Input:

> docs/canonical/architecture/external-representation.md

Useful retained hypotheses include exact source/disclosure binding, semantic metadata separate from large binary bytes, immutable Artifact bytes and digest identity, generation/validation/Publication/delivery separation, explicit Publication, source correction through affected/stale/successor state, non-authoritative delivery locators and end-to-end Provenance.

The candidate is not adopted unchanged because it contains stale Encounter-era wording, historical module references and AWS/S3/CloudFront/SQS selections that belong to current/later authority. Current RCV/Concept owners govern paper lineage.

# Alternatives

## A — Historical REP architecture unchanged

Strong semantics, but stale bindings and inherited runtime/provider choices make unchanged adoption invalid.

**Rejected as-is.**

## B — Transient on-demand generation only

Render from source, stream bytes and discard durable representation state.

This minimizes storage but cannot reliably reconstruct exactly what was previously printed/released after source, renderer or template changes.

**Rejected as baseline.**

## C — Mutable latest artifact with stable URL

Overwrite one file/key when source changes.

This simplifies links but destroys historical byte identity and silently retargets prior release, conflicting with EXPORT-003 and INV-005.

**Rejected.**

## D — Store large durable binary bytes directly in the relational authority database

This gives one storage family but burdens transactional authority storage, backup and recovery with large immutable payloads without semantic benefit.

**Rejected as baseline.**

## E — Immutable artifacts behind authoritative metadata + explicit Publication

Characteristics:

- exact Export SourceBasis/purpose/AudienceProfile;
- relational Export/Artifact/Publication metadata;
- immutable object/blob bytes with digest;
- complete-surface disclosure validation;
- idempotent generation;
- explicit Publication;
- source-change affectedness without history rewrite;
- explicit successor release;
- withdrawal without false external recall;
- provider-neutral delivery.

**Selected.**

# Architectural consequences

Export, Artifact and Publication remain distinct identities.

Authoritative metadata stays in the accepted PostgreSQL-compatible authority store. Large retained bytes use an object/blob port. No cloud provider is selected.

Generation can be synchronous or asynchronous based on workload. Orphan uploaded bytes never become Artifact authority. Validation is distinct and may reject generation results.

Publication is a high-consequence command and re-evaluates current release prerequisites.

Source correction can mark Export Affected/Stale or lead to successor Export. It never overwrites retained bytes or retargets historical Publication.

Withdrawal stops current MUDAC distribution authority but cannot guarantee deletion of copies already outside MUDAC control.

Delivery receipts/logs are transport evidence, not domain authority.

# Evidence

Acceptance evidence class: **DOCUMENTATION_REASONING**.

No technical probe is required to choose this semantic/storage topology.

Later executable evidence must cover exact SourceBasis immutability, byte digest/integrity, no retained-byte overwrite, generator retry convergence, disclosure enforcement, Publication precondition revalidation, source correction without historical rewrite, successor preservation, withdrawal stopping controlled ordinary delivery, external-copy persistence and delivery-failure separation.

Provider performance, cache invalidation, object-store durability and cost remain ADQ-009 evidence concerns.

# Reversibility / lock-in

Intentional commitments are durable Export identity, immutable retained Artifact bytes, digest identity, relational semantic metadata, object/blob boundary for large bytes, explicit Publication, successor correction and delivery non-authority.

Not selected: S3, CDN, queue, renderer, PDF library, email provider, print vendor, signed URL mechanism, scanner or exact retention period.

# Residual uncertainty

Open questions include exact object/blob service, encryption/provider controls, renderer stack, supported formats, print requirements, accessibility tooling, binary scanning, signed-link lifetime/revocation, CDN invalidation, restricted/public delivery topology, async worker mechanism, size/throughput limits, lifecycle/archive policy, legal retention and delivery-provider retry/observability.

# Scenario impact

ADQ-007 closes architecture posture for stale Export after source correction, withdrawn Publication while external copies remain, corrected successor representation, Publication with downstream delivery failure and disclosure-safe externalization.

# Risk disposition

**ERI-02 — controlled.** Current authority is ART-*; historical REP-* remains evidence.

**ERI-04 — controlled for ADQ-007.** Encounter-era wording is not adopted; current RCV and Concept owners govern paper lineage.

**ERI-09 — materially reduced / carried to 019-K.** Externalization consumes source authority and cannot promote or mutate source owners.

External-copy persistence after withdrawal is an explicit product/architecture limitation, not hidden failure.

# Implementation boundary

~~~text
accepted bounded decisions       7 / 10
Q4 repairs complete              3 / 4
technical probes                 0
accepted whole architecture      false
implementation packages          0
package derivation               false
implementation execution         false
~~~

G0 remains unsatisfied.

# Exit decision

**019-H — COMPLETE — PASS.**

**ADQ-007 — ACCEPTED.**

Next eligible:

> **019-I — Browser/Client State, Navigation, Accessibility & Degraded Interaction Architecture**

019-I is not automatically authorized. Q4R-004 must complete before the historical front-end candidate participates in ADQ-008 comparison.

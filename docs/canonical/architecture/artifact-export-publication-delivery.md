---
type: Architecture Contract
title: Current Artifact, Export, Publication & External Delivery Architecture
description: "Accepted ADQ-007 architecture for exact-source Exports, immutable artifact bytes, explicit Publication, successor replacement, withdrawal, and non-authoritative delivery."
status: stable
tags: [architecture, current, artifact, export, publication, delivery]
sources:
  - resource: persistence-history-recovery.md
  - resource: identity-access-authority.md
  - resource: interface-command-concurrency.md
  - resource: offline-continuity-reconciliation.md
  - resource: external-representation.md
  - resource: ../concepts/export.md
  - resource: ../concepts/publication.md
  - resource: ../synchronizations/external-representation-publication-release.md
  - resource: ../experience/external-representation-release.md
  - resource: ../invariants/current-vs-historical-truth.md
  - resource: ../invariants/official-not-automatically-public.md
  - resource: ../governance/downstream-realization-obligations.md
  - resource: ../../019-architecture-engineering-reentry/019-H-artifact-export-publication-external-representation-delivery-architecture.md
generated: { by: openai/gpt-5.6-sol, at: 2026-09-22T12:45:00-05:00 }
---

# Authority

This document is **current accepted architecture authority for ADQ-007**.

It establishes how MUDAC realizes Export, durable artifacts, Publication release, withdrawal/succession, controlled retrieval and external delivery. It does not select an object-store vendor, CDN, renderer, print vendor, queue, signed-link implementation, delivery provider, exact media formats or retention periods.

<a id="art-001"></a>
## ART-001 — Externalization is downstream of source authority

Artifact generation, rendering, Publication, transport and recipient possession never create or strengthen source semantic authority.

~~~text
source authority
  != Export
  != Artifact bytes
  != Publication
  != delivery success
  != recipient possession
~~~

<a id="art-002"></a>
## ART-002 — Every durable Export binds an exact SourceBasis, purpose and AudienceProfile

A meaningful Export records the exact source Version/revision/basis plus representation purpose/profile and AudienceProfile/disclosure class. Later source change never rewrites that historical SourceBasis.

<a id="art-003"></a>
## ART-003 — Export identity, Artifact identity and storage/delivery locators are distinct

Bucket keys, filenames, URLs, QR targets and print-job identifiers are locators, not semantic identity.

<a id="art-004"></a>
## ART-004 — Durable Artifact bytes are immutable and integrity-addressable

Once registered as complete, retained bytes are not overwritten in place. Artifact metadata records stable identity, cryptographic digest, format/media, size, generation basis and storage locator as applicable. Regeneration creates a new Artifact.

<a id="art-005"></a>
## ART-005 — Relational authority owns semantic metadata; large binary payloads use an object/blob-storage port

The accepted PST store owns Export, Artifact, Publication, source/disclosure basis, lifecycle and Provenance metadata. Large generated files and retained binary evidence use provider-neutral object/blob storage. Object existence alone establishes no semantic authority.

<a id="art-006"></a>
## ART-006 — Disclosure validation covers the complete externally observable artifact surface

Audience/disclosure enforcement covers visible content and, where applicable, filenames, document metadata, accessibility text, embedded layers, QR/barcode payloads, manifests, previews and machine-readable structures. UI hiding is not an artifact disclosure boundary.

<a id="art-007"></a>
## ART-007 — Generation, validation, Publication and delivery are distinct states

Generation requested/running/completed, Artifact registration, validation, Publication and downstream delivery remain distinct. Generator success does not imply Publication; Publication does not prove transport completion; delivery failure does not erase committed Publication.

<a id="art-008"></a>
## ART-008 — Artifact generation is idempotent/retryable and may complete asynchronously

Generation binds stable logical operation identity to the exact Export/source/disclosure/format/generator basis. Retry converges on a known result or explicit failure/unknown state. Long-running generation may use CMD-019 asynchronous execution without creating a new domain Concept.

<a id="art-009"></a>
## ART-009 — Artifact validation is purpose-specific and never promotes source authority

Validation may check semantic fidelity, rendering, required content, disclosure leakage, accessibility, print constraints, link/QR usability, integrity and appropriate binary-safety properties. It can reject bytes but cannot change SourceBasis, make a source official or publish a representation.

<a id="art-010"></a>
## ART-010 — Publication is an explicit authoritative release record bound to one exact representation

A Publication records stable identity, exact Export/Artifact representation, Audience, Channel, PublishingAuthority, publication time, distribution state and predecessor/successor relation as applicable. A generated file or public-looking URL is not Publication by itself.

<a id="art-011"></a>
## ART-011 — Publication eligibility is evaluated against current release prerequisites

Before ordinary release the application revalidates material prerequisites: selected representation, Export suitability/currentness, sufficient source authority, compatible Audience/Channel, current disclosure constraints and current PublishingAuthority.

<a id="art-012"></a>
## ART-012 — Source changes affect representation currentness without rewriting historical bytes or release records

Source changes may make Export Affected, Stale, Superseded or require revalidation. Retained Artifact bytes and historical Publication remain bound to what existed or was released. No correction silently overwrites bytes or retargets Publication.

<a id="art-013"></a>
## ART-013 — Corrected or replacement release uses explicit successor identities

~~~text
new SourceBasis
  → new Export
  → new Artifact when needed
  → explicit successor Publication
~~~

Predecessor Export, Artifact and Publication remain reconstructible.

<a id="art-014"></a>
## ART-014 — Withdrawal ends current MUDAC distribution authority; it does not claim external recall

Withdrawal preserves what was released, to whom/where, under whose authority and when. MUDAC-controlled surfaces stop ordinary new delivery where withdrawal requires it. Printed, downloaded, cached, screenshotted or emailed copies may remain outside MUDAC control.

<a id="art-015"></a>
## ART-015 — Delivery mechanisms are transport capabilities, not semantic authority

URLs, object keys, CDN paths, signed links, QR codes, email sends and print jobs may locate or transport a representation. They do not establish source authority, Access, Export currentness, Publication authority or recipient compliance.

<a id="art-016"></a>
## ART-016 — Private and public retrieval preserve the selected disclosure/release boundary

Restricted retrieval requires current authorization appropriate to the representation and context. Public representation requires Publication whose Audience/Channel permits public distribution. A signed URL or hard-to-guess path is not itself disclosure policy.

<a id="art-017"></a>
## ART-017 — MUDAC-controlled delivery reflects current Publication state without rewriting possession history

Controlled delivery surfaces honor current Publication/distribution state where practical and material. Withdrawn or superseded release may stop new controlled downloads while historical release records and external copies remain. Cache/provider mechanics remain ADQ-009 work.

<a id="art-018"></a>
## ART-018 — External-representation Provenance is reconstructible end-to-end

MUDAC can reconstruct exact SourceBasis, purpose/AudienceProfile, currency history, generator basis, Artifact identity/digest/locator, validation basis, Publication actor/authority/time/Audience/Channel, retained delivery evidence, affected/withdrawn/superseded state and successor relation as applicable.

<a id="art-019"></a>
## ART-019 — Retention and deletion preserve referenced historical meaning and remain evidence-bounded

Cleanup may remove disposable transient generation or transport material where policy permits, but must not silently destroy bytes/metadata required to explain retained Export/Publication history. Exact legal retention and erasure remain ENG-002 external-evidence work.

<a id="art-020"></a>
## ART-020 — Externalization mechanisms remain replaceable behind application contracts

Object storage, CDN, renderer, print integration, asynchronous worker/queue, email/delivery provider, signed-link mechanism and scanning tools remain replaceable. They must preserve ART-001..019 and cannot become semantic authority.

# Selected architecture

~~~text
authoritative source
  → exact Export record
      + SourceBasis
      + purpose
      + AudienceProfile
      + currency
  → generation
  → immutable Artifact bytes
      + relational metadata
      + digest
      + object/blob locator
  → validation
  → explicit Publication
      + Audience
      + Channel
      + PublishingAuthority
      + distribution state
  → delivery
      + transport evidence only
~~~

# Evidence posture

ADQ-007 acceptance uses **DOCUMENTATION_REASONING**.

Later executable evidence must cover source-basis stability, byte immutability/integrity, generator idempotency, disclosure checks, Publication preconditions, affected/stale propagation, successor preservation, withdrawal behavior, controlled-delivery currentness and delivery-failure separation.

# Revisit triggers

Reopen ADQ-007 if representation formats cannot preserve source/disclosure fidelity, provider constraints make immutable identity or controlled withdrawal infeasible, retained-artifact cost becomes disproportionate, binding retention/erasure law conflicts with history semantics, delivery requires independent authoritative workflow semantics, or 019-K finds unresolved disclosure/stale-copy/release-history risk.

Whole-architecture acceptance remains false until 019-L.

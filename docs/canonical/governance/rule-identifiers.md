---
type: Documentation Authority
title: Stable Rule Identifiers & Cross-Reference Contract
description: Governs durable normative rule IDs and how dependent MUDAC knowledge references canonical owners without creating duplicate authority.
status: stable
tags: [governance, rule-id, cross-reference, anti-drift]
sources:
  - resource: ../../004-knowledge-architecture/004-A-okf-adoption-authority-methodology-compatibility-terminology-contract.md
  - resource: ../../004-knowledge-architecture/004-C-canonical-concept-policy-invariant-experience-knowledge-extraction.md
  - resource: ../../004-knowledge-architecture/004-E-cross-reference-stable-rule-id-restatement-reduction-retrofit.md
  - resource: ../../004-knowledge-architecture/004-F-documentation-governance-agent-context-anti-drift-rules.md
  - resource: ../../004-knowledge-architecture/004-G-okf-metadata-trust-verification-lifecycle-freshness-conventions.md
  - resource: ../../004-knowledge-architecture/004-H-validation-tooling-link-authority-checks-ci-enforcement.md
  - resource: ../../010-project-purpose-candidate-specification-modularity/010-H-concept-boundary-convergence-respecification-canonical-reconciliation.md
generated: { by: openai/gpt-5.6-sol, at: 2026-09-22T09:30:00-05:00 }
---

# Canonical contract

Stable rule IDs identify durable normative contracts owned by canonical knowledge documents. The ID is a reference interface; the linked owner remains the source of rule meaning.

Rule IDs are owner-based rather than phase-based. They must not be reused for a different meaning.

# Reference syntax

Rule owners use explicit anchors:

```markdown
<a id="sc-001"></a>
## SC-001 — Draft is non-authoritative
```

Dependents use ordinary Markdown links:

```markdown
[SC-001](../concepts/scorecard.md#sc-001)
```

A naked ID may be used in nearby prose only when the linked form has already established the referent and ambiguity is impossible.

# Restatement rule

A dependent document should cite the canonical ID and explain only its local consequence. Full restatement is reserved for cases where independent auditability or necessary comprehension justifies it, and the restatement remains subordinate to the linked owner.

# Stability rule

Editorial clarification may retain an ID when semantics remain compatible. A materially incompatible replacement receives a new ID. Retired IDs are never reassigned.

# Cross-cutting invariants

* [INV-001 — Judge Independence](../invariants/judge-independence.md#inv-001)
* [INV-002 — One Logical Evaluation per Evaluation Obligation](../invariants/one-logical-scorecard.md#inv-002)
* [INV-003 — Missing Is Never Zero](../invariants/missing-never-zero.md#inv-003)
* [INV-004 — Organizer Authority Does Not Become Judge Authorship](../invariants/organizer-not-judge-author.md#inv-004)
* [INV-005 — Current and Historical Truth Remain Distinct](../invariants/current-vs-historical-truth.md#inv-005)
* [INV-006 — Calculated Is Not Declared Official](../invariants/calculated-not-official.md#inv-006)
* [INV-007 — Official Is Not Automatically Public](../invariants/official-not-automatically-public.md#inv-007)
* [INV-008 — Capture-Channel Parity](../invariants/capture-channel-parity.md#inv-008)
* [INV-009 — Accessibility Is Semantic Parity](../invariants/accessibility-semantic-parity.md#inv-009)
* [INV-010 — Truthful Authority Under Uncertainty](../invariants/truthful-authority-under-uncertainty.md#inv-010)

# Competition

* [COMP-001 — Competition Lifecycle](../concepts/competition.md#comp-001)
* [COMP-002 — Post-Finalization Correction Preserves Finalized Lifecycle](../concepts/competition.md#comp-002)

# Access

* [ACC-001 — Access Is Contextual](../concepts/access.md#acc-001)
* [ACC-002 — Access Does Not Transfer Semantic Authority](../concepts/access.md#acc-002)

# Scorecard

* [SC-001 — Draft Is Non-Authoritative](../concepts/scorecard.md#sc-001)
* [SC-002 — Amendment Preserves Prior Authority Until Successor Finalization](../concepts/scorecard.md#sc-002)
* [SC-003 — Structural Scorecard Identity Is Not Amended](../concepts/scorecard.md#sc-003)

Logical uniqueness/evaluation weight is separately owned by [INV-002](../invariants/one-logical-scorecard.md#inv-002), and Judge authorship by [INV-004](../invariants/organizer-not-judge-author.md#inv-004).

# Evaluation Policy

* [EVAL-001 — Equal Eligible Individual Judge Weighting](../policies/evaluation-policy.md#eval-001)
* [EVAL-002 — No Silent Rubric Pooling or Rescaling](../policies/evaluation-policy.md#eval-002)
* [EVAL-003 — Outcome-Affecting Policy Is Reconstructible](../policies/evaluation-policy.md#eval-003)

# Ranking

* [RANK-001 — Rank Is Derived and Non-Editable](../mechanisms/rank.md#rank-001)
* [RANK-002 — Precision and Ties Follow Declared Policy](../mechanisms/rank.md#rank-002)

# Outcome Declaration

* [OUT-001 — Explicit Declaration Establishes Official Outcome Authority](../concepts/outcome-declaration.md#out-001)
* [OUT-002 — Affected Declaration Requires Explicit Successor Confirmation](../concepts/outcome-declaration.md#out-002)

# Disclosure

* [DISC-001 — Blinded Judge Team Identity](../policies/anonymity-disclosure.md#disc-001)
* [DISC-002 — Disclosure Is Audience and Purpose Specific](../policies/anonymity-disclosure.md#disc-002)

# Export

* [EXPORT-001 — Export Represents Source Authority; It Never Promotes It](../concepts/export.md#export-001)
* [EXPORT-002 — Currency and Distribution Are Separate](../concepts/export.md#export-002)
* [EXPORT-003 — Historical Basis Is Stable](../concepts/export.md#export-003)

# Publication

* [PUB-001 — Publication Prerequisites Follow Representation Purpose and Source Authority](../concepts/publication.md#pub-001)

# Operational exception and override governance

* [OPG-001 — Governed Exceptions Preserve Source Truth](../policies/operational-exception-governance.md#opg-001)
* [OPG-002 — Exception Authority Is Explicit, Scoped, Attributable, and Reasoned](../policies/operational-exception-governance.md#opg-002)
* [OPG-003 — Generic Override Cannot Bypass Semantic Invariants](../policies/operational-exception-governance.md#opg-003)
* [OPG-004 — Acknowledgement, Suppression, and Presentation State Are Not Resolution](../policies/operational-exception-governance.md#opg-004)
* [OPG-005 — Technical Emergency Capability Does Not Create Policy Authority](../policies/operational-exception-governance.md#opg-005)
* [OPG-006 — Exceptional Closeout May Declare Absence of an Ordinary Result, Never Fabricate One](../policies/operational-exception-governance.md#opg-006)

# Accepted architecture drivers

* [DRV-001 — Current Semantic Authority Is the First Architecture Constraint](../architecture/architecture-drivers.md#drv-001)
* [DRV-002 — Quality Priority Is Semantic/Trust Integrity, Then Event Continuity, Then Sustaining Quality](../architecture/architecture-drivers.md#drv-002)
* [DRV-003 — Safe Unavailability or Uncertainty Is Preferred to Fabricated Authority](../architecture/architecture-drivers.md#drv-003)
* [DRV-004 — Paper Continuity Is a Valid Resilience Path, Not a Second Authority Model](../architecture/architecture-drivers.md#drv-004)
* [DRV-005 — The Baseline Workload Is Bounded, Bursty and Live-Event Shaped](../architecture/architecture-drivers.md#drv-005)
* [DRV-006 — Exact Capacity, Latency and Recovery Targets Remain Evidence-Bounded Until Quantified](../architecture/architecture-drivers.md#drv-006)
* [DRV-007 — Trust Boundaries Require Explicit Re-establishment of Relevant Authority](../architecture/architecture-drivers.md#drv-007)
* [DRV-008 — Security and Disclosure Are Semantic-Boundary Obligations](../architecture/architecture-drivers.md#drv-008)
* [DRV-009 — Accessibility, Device Continuity and Degraded Operation Preserve Semantic Parity](../architecture/architecture-drivers.md#drv-009)
* [DRV-010 — Operability and Cost Must Be Proportional to Demonstrated Event Needs](../architecture/architecture-drivers.md#drv-010)
* [DRV-011 — Reversibility and Provider/Service Lock-in Are Explicit Decision Dimensions](../architecture/architecture-drivers.md#drv-011)
* [DRV-012 — The Current Delivery Environment Constrains Context, Not Service Topology](../architecture/architecture-drivers.md#drv-012)
# Accepted application boundary architecture

* [BND-001 — The Initial Authoritative Application Topology Is an Ownership-Preserving Modular Monolith](../architecture/application-ownership-boundaries.md#bnd-001)
* [BND-002 — Current Authoritative Ownership Is Grouped Into Five Cohesive Modules](../architecture/application-ownership-boundaries.md#bnd-002)
* [BND-003 — Versioning and Provenance Are Cross-Cutting Concepts, Not Central God-Modules](../architecture/application-ownership-boundaries.md#bnd-003)
* [BND-004 — Every Authoritative Fact and State-Changing Command Has One Primary Module Owner](../architecture/application-ownership-boundaries.md#bnd-004)
* [BND-005 — Cross-Owner Workflows Coordinate Above Owners Without Becoming a New Semantic Owner](../architecture/application-ownership-boundaries.md#bnd-005)
* [BND-006 — Cross-Module State Access Uses Public Contracts and Stable Identities, Never Another Module's Storage](../architecture/application-ownership-boundaries.md#bnd-006)
* [BND-007 — Dependency Direction Is Acyclic and Follows Authority Flow](../architecture/application-ownership-boundaries.md#bnd-007)
* [BND-008 — Read Projections May Compose Across Modules but Never Become Write Authority](../architecture/application-ownership-boundaries.md#bnd-008)
* [BND-009 — Identity/Access Enforcement Remains Explicit at Protected Owner Boundaries](../architecture/application-ownership-boundaries.md#bnd-009)
* [BND-010 — External Representation Is Strictly Downstream of Source Authority](../architecture/application-ownership-boundaries.md#bnd-010)
* [BND-011 — Module Extraction Is Allowed Only Through Preserved Contracts and Demonstrated Drivers](../architecture/application-ownership-boundaries.md#bnd-011)
* [BND-012 — Source/Package Layout and Provider/Runtime Deployment Remain Later Decisions](../architecture/application-ownership-boundaries.md#bnd-012)
# Accepted persistence, history and recovery architecture

* [PST-001 — The Authoritative Persistence Family Is PostgreSQL-Compatible Relational Storage](../architecture/persistence-history-recovery.md#pst-001)
* [PST-002 — One Logical Authority Database Is the Initial Storage Topology](../architecture/persistence-history-recovery.md#pst-002)
* [PST-003 — Storage Ownership Follows BND Application Ownership](../architecture/persistence-history-recovery.md#pst-003)
* [PST-004 — Durable Resource Identity Is Independent of Mutable Business Labels and Physical Storage](../architecture/persistence-history-recovery.md#pst-004)
* [PST-005 — Working/Current State and Committed Authoritative History Are Structurally Distinct](../architecture/persistence-history-recovery.md#pst-005)
* [PST-006 — Committed Versions Are Immutable and May Legitimately Have No Current Eligible Successor](../architecture/persistence-history-recovery.md#pst-006)
* [PST-007 — Meaningful Provenance Is Append-Stable and Distinct From Technical Telemetry](../architecture/persistence-history-recovery.md#pst-007)
* [PST-008 — Ordinary Destructive Operations Cannot Erase Referenced Authoritative History](../architecture/persistence-history-recovery.md#pst-008)
* [PST-009 — Derived Calculations and Read Projections Are Non-Authoritative and Reconstructible](../architecture/persistence-history-recovery.md#pst-009)
* [PST-010 — Projection Loss Is Recovered by Rebuild, Not by Promoting Projection Backups to Authority](../architecture/persistence-history-recovery.md#pst-010)
* [PST-011 — Asynchronous Propagation, When Used, Is Durably Coupled to the Authoritative Commit](../architecture/persistence-history-recovery.md#pst-011)
* [PST-012 — System-Wide Event Sourcing Is Not the Baseline Persistence Architecture](../architecture/persistence-history-recovery.md#pst-012)
* [PST-013 — Core Semantic Fields Remain Explicit; Semi-Structured Storage Is Bounded](../architecture/persistence-history-recovery.md#pst-013)
* [PST-014 — Schema Migration Is Owner-Scoped, Forward-Compatible and History-Preserving](../architecture/persistence-history-recovery.md#pst-014)
* [PST-015 — Data Recovery Restores Authoritative Consistency Before Service Availability Is Claimed](../architecture/persistence-history-recovery.md#pst-015)
* [PST-016 — Recovery Never Fabricates Authority After Uncertain or Partial Failure](../architecture/persistence-history-recovery.md#pst-016)
# Accepted identity, authentication, access and session architecture

* [IAM-001 — Authentication Proves Principal Control; MUDAC Owns Application Identity and Authority](../architecture/identity-access-authority.md#iam-001)
* [IAM-002 — External Authentication Subjects Link Explicitly to Durable MUDAC Identity](../architecture/identity-access-authority.md#iam-002)
* [IAM-003 — Participation Is Competition-Scoped and Never Becomes a Permanent Account Role](../architecture/identity-access-authority.md#iam-003)
* [IAM-004 — Capabilities Never Union Across Participation Contexts](../architecture/identity-access-authority.md#iam-004)
* [IAM-005 — Access Is Evaluated From Current Application Authority at Protected Boundaries](../architecture/identity-access-authority.md#iam-005)
* [IAM-006 — Browser Continuity Uses an Opaque First-Party Server-Controlled Session](../architecture/identity-access-authority.md#iam-006)
* [IAM-007 — Session State Is Continuity and Assurance Evidence, Not Capability Authority](../architecture/identity-access-authority.md#iam-007)
* [IAM-008 — Sessions Are Bounded, Revocable and Replaceable Without Changing Semantic Identity](../architecture/identity-access-authority.md#iam-008)
* [IAM-009 — Shared-Device and Context Handoff Terminates Prior Private Context Before Reuse](../architecture/identity-access-authority.md#iam-009)
* [IAM-010 — Invitation, QR, Event and Deep-Link Credentials Route or Claim Bounded Context; They Do Not Authenticate Authority](../architecture/identity-access-authority.md#iam-010)
* [IAM-011 — Reverification and Step-Up Strengthen Principal Assurance but Never Create Application Capability](../architecture/identity-access-authority.md#iam-011)
* [IAM-012 — Exceptional Application Access Is Narrow, Attributable, Expiring and Revocable](../architecture/identity-access-authority.md#iam-012)
* [IAM-013 — Identity Recovery/Linking Cannot Silently Rewrite Historical Attribution](../architecture/identity-access-authority.md#iam-013)
* [IAM-014 — Technical/Operator Authority Is a Separate Principal/Context From Competition Participation](../architecture/identity-access-authority.md#iam-014)
* [IAM-015 — Break-Glass Access Is Exceptional Technical Authority, Not Semantic Impersonation](../architecture/identity-access-authority.md#iam-015)
* [IAM-016 — Authentication-Provider Integration Remains Replaceable Behind an Application Adapter](../architecture/identity-access-authority.md#iam-016)
* [IAM-017 — Authentication/Provider Unavailability Reduces Capability Safely; It Does Not Broaden Authority](../architecture/identity-access-authority.md#iam-017)
* [IAM-018 — Access Denial and Security Response Preserve Truthful, Non-Leaking Explanation](../architecture/identity-access-authority.md#iam-018)
# Suspended downstream rule-ID partition

The following architecture/implementation rule IDs are preserved for **historical/candidate downstream referential integrity** while their owner documents remain suspended under the [Downstream Architecture & Implementation Authority Quarantine](downstream-authority-quarantine.md).

Registry presence means only that an ID remains stable and resolvable. It does **not** mean:

- the architecture/implementation rule is current accepted authority;
- the referenced technology/topology has been adopted after Concept Design closure;
- a successful Phase-017 closure automatically reactivates the rule;
- downstream rules may constrain current Concept Design.

Any later architecture/engineering re-entry must explicitly adopt, revise, replace, or retire these candidates under [Post-Concept-Design Architecture & Engineering Re-entry](post-concept-design-reentry.md).

# Architecture foundation

* [ARCH-001 — Upstream Canonical Semantics Constrain Architecture](../architecture/architectural-foundation.md#arch-001)
* [ARCH-002 — Authoritative Transitions Are Validated and Confirmed at the Authoritative Boundary](../architecture/architectural-foundation.md#arch-002)
* [ARCH-003 — Client, Device, and Local State Are Not Final Authority](../architecture/architectural-foundation.md#arch-003)
* [ARCH-004 — Derived Projections Are Not Write Authority](../architecture/architectural-foundation.md#arch-004)
* [ARCH-005 — Actor, Author, Authorizer, and Capture Attribution Survive Boundaries](../architecture/architectural-foundation.md#arch-005)
* [ARCH-006 — Failure and Retry Preserve Logical Identity and Evidence](../architecture/architectural-foundation.md#arch-006)
* [ARCH-007 — Security and Disclosure Are Enforced Beyond Presentation Code](../architecture/architectural-foundation.md#arch-007)
* [ARCH-008 — Freshness and Uncertainty Remain Representable](../architecture/architectural-foundation.md#arch-008)

# Application modules and dependencies

* [MOD-001 — The Initial Authoritative Application Is a Modular Monolith](../architecture/application-boundaries.md#mod-001)
* [MOD-002 — Each Authoritative Fact and Command Has One Module Owner](../architecture/application-boundaries.md#mod-002)
* [MOD-003 — Cross-Module Interaction Cannot Bypass Public Ownership Boundaries](../architecture/application-boundaries.md#mod-003)
* [MOD-004 — Cross-Module Workflows Coordinate Above Module Owners](../architecture/application-boundaries.md#mod-004)
* [MOD-005 — Dependency Direction Remains Acyclic and Downstream-Oriented](../architecture/application-boundaries.md#mod-005)
* [MOD-006 — Projection/Query Composition Is Non-Authoritative](../architecture/application-boundaries.md#mod-006)
* [MOD-007 — Cross-Cutting Technical Reuse Does Not Centralize Semantic Ownership](../architecture/application-boundaries.md#mod-007)
* [MOD-008 — Shared Foundation Remains Small and Business-Neutral](../architecture/application-boundaries.md#mod-008)
* [MOD-009 — Infrastructure Depends Inward Through Application/Module Ports](../architecture/application-boundaries.md#mod-009)
* [MOD-010 — Deployment Boundaries May Evolve Without Changing Semantic Boundaries](../architecture/application-boundaries.md#mod-010)

# Data, persistence, versioning, provenance and projections

* [DATA-001 — Authoritative Persistence Is Relational and PostgreSQL-Compatible](../architecture/data-persistence.md#data-001)
* [DATA-002 — One Logical Authority Database Initially; Storage Ownership Remains Module-Scoped](../architecture/data-persistence.md#data-002)
* [DATA-003 — Durable Identities Are Stable and Independent of Storage/Business Labels](../architecture/data-persistence.md#data-003)
* [DATA-004 — Physical Co-Location Does Not Permit Cross-Module Storage Bypass](../architecture/data-persistence.md#data-004)
* [DATA-005 — Working/Current State and Committed Versions Remain Structurally Distinct](../architecture/data-persistence.md#data-005)
* [DATA-006 — Committed Versions and Meaningful Provenance Are Append-Stable](../architecture/data-persistence.md#data-006)
* [DATA-007 — Referenced Authoritative Evidence Is Not Erased Through Ordinary Destructive Cascade](../architecture/data-persistence.md#data-007)
* [DATA-008 — Persisted Derived Calculations Remain Reconstructible From an Identified Basis](../architecture/data-persistence.md#data-008)
* [DATA-009 — Read Projections Are Disposable, Rebuildable, and Non-Authoritative](../architecture/data-persistence.md#data-009)
* [DATA-010 — Projection Freshness and Authority Basis Remain Observable](../architecture/data-persistence.md#data-010)
* [DATA-011 — Asynchronous Change Propagation Is Transactionally Coupled to the Source Change](../architecture/data-persistence.md#data-011)
* [DATA-012 — Outbox/Events Do Not Replace Authoritative State or Require Primary Event Sourcing](../architecture/data-persistence.md#data-012)
* [DATA-013 — Database Constraints Reinforce Owner Invariants but Do Not Replace Domain Authority Checks](../architecture/data-persistence.md#data-013)
* [DATA-014 — Core Semantic Fields Remain Explicit; Semi-Structured Storage Is Reserved for Genuinely Extensible Data](../architecture/data-persistence.md#data-014)

# Identity, authentication, access and sessions

* [AUTH-001 — Authentication Establishes Principal Continuity, Not Competition Authority](../architecture/identity-access-session.md#auth-001)
* [AUTH-002 — External Subjects Link Explicitly to Stable MUDAC Identity](../architecture/identity-access-session.md#auth-002)
* [AUTH-003 — Participation Context Is Explicit and Never Inferred as a Permanent Identity Role](../architecture/identity-access-session.md#auth-003)
* [AUTH-004 — Access Is Evaluated From Current Authoritative Context at Protected Boundaries](../architecture/identity-access-session.md#auth-004)
* [AUTH-005 — Browser Authentication Terminates in a First-Party Opaque Server Session](../architecture/identity-access-session.md#auth-005)
* [AUTH-006 — Session Context Is Convenience State, Not Authorization Authority](../architecture/identity-access-session.md#auth-006)
* [AUTH-007 — Event Completion Expires Judge Capability Through Source-State Authorization](../architecture/identity-access-session.md#auth-007)
* [AUTH-008 — Event Invitations and QR/Codes Accelerate Entry but Do Not Confer Identity or Access](../architecture/identity-access-session.md#auth-008)
* [AUTH-009 — Dual-Role Capability Sets Remain Isolated by Explicit Participation Context](../architecture/identity-access-session.md#auth-009)
* [AUTH-010 — Post-Event Judge Correction Uses Narrow Temporary Access Plus Reverification](../architecture/identity-access-session.md#auth-010)
* [AUTH-011 — Device Loss or Handoff Revokes Session State Without Changing Semantic Identity](../architecture/identity-access-session.md#auth-011)
* [AUTH-012 — System Administration and Break-Glass Authority Remain Separate From Competition Authority](../architecture/identity-access-session.md#auth-012)
* [AUTH-013 — Step-Up Authentication Strengthens Proof but Never Creates Capability](../architecture/identity-access-session.md#auth-013)
* [AUTH-014 — Authentication-Provider Implementation Remains Replaceable Behind an Adapter](../architecture/identity-access-session.md#auth-014)

# Commands, queries, API, transactions and concurrency

* [API-001 — Commands and Queries Are Distinct Application Contracts](../architecture/commands-api-concurrency.md#api-001)
* [API-002 — The Primary Browser Application Contract Is Versioned HTTPS/JSON](../architecture/commands-api-concurrency.md#api-002)
* [API-003 — Transport Adapters Do Not Own Domain Authority](../architecture/commands-api-concurrency.md#api-003)
* [API-004 — A Successful Authoritative Command Is Confirmed Only After Transaction Commit](../architecture/commands-api-concurrency.md#api-004)
* [API-005 — Single-Module Commands Use One Owning Transaction Boundary](../architecture/commands-api-concurrency.md#api-005)
* [API-006 — Cross-Module Atomic Transactions Are Narrow and Coordinator-Owned](../architecture/commands-api-concurrency.md#api-006)
* [API-007 — Optimistic Concurrency Is the Default Mutable-State Strategy](../architecture/commands-api-concurrency.md#api-007)
* [API-008 — Pessimistic Locking and Stronger Isolation Are Targeted Tools, Not Global Defaults](../architecture/commands-api-concurrency.md#api-008)
* [API-009 — Externally Retryable Commands Have Durable Idempotency Semantics](../architecture/commands-api-concurrency.md#api-009)
* [API-010 — Lost Responses Reconcile to Committed Authority Instead of Inviting Blind Repetition](../architecture/commands-api-concurrency.md#api-010)
* [API-011 — Query Freshness Is Explicit and Never Becomes Command Authority](../architecture/commands-api-concurrency.md#api-011)
* [API-012 — Application Results Distinguish Semantic Failure Classes](../architecture/commands-api-concurrency.md#api-012)
* [API-013 — Command Responses Return Authoritative Identity/Revision, Not Assumed Projection Freshness](../architecture/commands-api-concurrency.md#api-013)
* [API-014 — Public API DTOs Remain Separate From Internal Module/Domain Models](../architecture/commands-api-concurrency.md#api-014)
* [API-015 — Cookie-Authenticated Mutations Require Deliberate Request-Forgery Protection](../architecture/commands-api-concurrency.md#api-015)

# Draft synchronization, offline and recovery

* [SYNC-001 — Local Persistence Is Bounded to Non-Authoritative Continuity State](../architecture/synchronization-recovery.md#sync-001)
* [SYNC-002 — Local Draft State Is Bound to Stable Semantic Identity and a Confirmed Server Base](../architecture/synchronization-recovery.md#sync-002)
* [SYNC-003 — Server Draft Revision Remains Authoritative and Synchronization Is Revision-Aware](../architecture/synchronization-recovery.md#sync-003)
* [SYNC-004 — Stale Draft Conflicts Preserve Both Server and Local Judge Work](../architecture/synchronization-recovery.md#sync-004)
* [SYNC-005 — Automatic Merge Is Permitted Only When Semantic Safety Is Demonstrable](../architecture/synchronization-recovery.md#sync-005)
* [SYNC-006 — Multiple Devices Converge on One Logical Scorecard](../architecture/synchronization-recovery.md#sync-006)
* [SYNC-007 — Finalization and Other Authoritative Transitions Require Reachable Server Authority](../architecture/synchronization-recovery.md#sync-007)
* [SYNC-008 — Uncertain Consequential Outcomes Are Reconciled Before Another Transition Is Attempted](../architecture/synchronization-recovery.md#sync-008)
* [SYNC-009 — Reconnect Re-Establishes Authentication, Access, Identity, and Current Server State Before Applying Queued Work](../architecture/synchronization-recovery.md#sync-009)
* [SYNC-010 — Cached Reads Remain Explicitly Stale-Capable and Disclosure-Bounded](../architecture/synchronization-recovery.md#sync-010)
* [SYNC-011 — Access Expiry or Revocation Blocks Automatic Synchronization of Private Pending Work](../architecture/synchronization-recovery.md#sync-011)
* [SYNC-012 — Paper and Electronic Traces Converge on One Logical Evaluation With Preserved Provenance](../architecture/synchronization-recovery.md#sync-012)
* [SYNC-013 — Synchronization Status Preserves Authority, Freshness, Conflict, and Uncertainty as Distinct Dimensions](../architecture/synchronization-recovery.md#sync-013)
* [SYNC-014 — Degraded Digital Operation Yields to Paper When Authoritative Continuity Cannot Be Trusted](../architecture/synchronization-recovery.md#sync-014)

# Paper capture, external representation, artifacts and publication

* [REP-001 — Paper-Origin Scorecard Authority Remains Owned by Evaluation](../architecture/external-representation.md#rep-001)
* [REP-002 — Physical Evidence Has a Stable Source Reference and Preserved Capture Provenance](../architecture/external-representation.md#rep-002)
* [REP-003 — Paper Verification Establishes Transcription Fidelity, Not Invented Judge Intent](../architecture/external-representation.md#rep-003)
* [REP-004 — Binary Evidence and Generated Artifacts Use Immutable Object/Blob Storage Behind Authoritative Metadata](../architecture/external-representation.md#rep-004)
* [REP-005 — Every Durable Export/Artifact Binds an Exact Source Basis, Purpose, and Disclosure Profile](../architecture/external-representation.md#rep-005)
* [REP-006 — Disclosure Applies to the Complete Artifact Surface](../architecture/external-representation.md#rep-006)
* [REP-007 — Durable Artifact Bytes Are Immutable and Integrity-Addressable](../architecture/external-representation.md#rep-007)
* [REP-008 — Generation, Validation, Publication, and Delivery Are Distinct States](../architecture/external-representation.md#rep-008)
* [REP-009 — Artifact Generation Is Idempotent/Retryable and May Be Asynchronous](../architecture/external-representation.md#rep-009)
* [REP-010 — Artifact Validation Is Purpose-Specific and Does Not Create Source Authority](../architecture/external-representation.md#rep-010)
* [REP-011 — Publication Is an Explicit Authoritative Distribution Record Bound to One Artifact](../architecture/external-representation.md#rep-011)
* [REP-012 — Source Changes Affect Dependent Representations Without Rewriting Historical Artifacts](../architecture/external-representation.md#rep-012)
* [REP-013 — Replacement Publication Is Explicit and Successor-Based](../architecture/external-representation.md#rep-013)
* [REP-014 — URLs, QR Codes, Signed Links, Print Jobs, and Delivery Channels Do Not Confer Authority](../architecture/external-representation.md#rep-014)
* [REP-015 — External-Representation Provenance Remains Reconstructible End-to-End](../architecture/external-representation.md#rep-015)

# Front-end state, navigation and interaction

* [FE-001 — The Browser Baseline Is React + TypeScript With Explicit Architectural Adapters](../architecture/frontend-interaction.md#fe-001)
* [FE-002 — React Router Owns Route/Navigation Boundaries, Not Domain Authority](../architecture/frontend-interaction.md#fe-002)
* [FE-003 — Client State Is Partitioned by Semantic Ownership](../architecture/frontend-interaction.md#fe-003)
* [FE-004 — TanStack Query Owns Remote Client Cache and Never Becomes Authoritative State](../architecture/frontend-interaction.md#fe-004)
* [FE-005 — Durable Local Draft Continuity Uses an IndexedDB-Backed Adapter and Remains Non-Authoritative](../architecture/frontend-interaction.md#fe-005)
* [FE-006 — High-Consequence Command State Is Explicit and Never Optimistically Final](../architecture/frontend-interaction.md#fe-006)
* [FE-007 — Role/Participation Mode Is Explicit and Changes Disclosure as Well as Navigation](../architecture/frontend-interaction.md#fe-007)
* [FE-008 — Context Transitions Partition or Clear Private Client State](../architecture/frontend-interaction.md#fe-008)
* [FE-009 — Judge Interaction Is Phone-Primary and Task-Centered](../architecture/frontend-interaction.md#fe-009)
* [FE-010 — Organizer Interaction Is Exception-First and Responsively Composable](../architecture/frontend-interaction.md#fe-010)
* [FE-011 — Component Architecture Separates Primitives, Semantic Patterns, Domain Features, and Route Compositions](../architecture/frontend-interaction.md#fe-011)
* [FE-012 — Semantic Status Presentation Preserves Independent State Dimensions](../architecture/frontend-interaction.md#fe-012)
* [FE-013 — Core Browser Workflows Target WCAG 2.2 AA Semantic Parity](../architecture/frontend-interaction.md#fe-013)
* [FE-014 — Client Validation Assists; Server Validation Remains Authoritative](../architecture/frontend-interaction.md#fe-014)
* [FE-015 — Conflict/Recovery UI Preserves Evidence Instead of Reducing Failure to a Toast](../architecture/frontend-interaction.md#fe-015)
* [FE-016 — Real-Time Push Is an Accelerator, Not a Correctness Dependency](../architecture/frontend-interaction.md#fe-016)
* [FE-017 — Dense/Tabular Information May Transform Responsively Without Semantic Loss](../architecture/frontend-interaction.md#fe-017)
* [FE-018 — Client Error Boundaries Contain Failure Without Inventing Source-State Loss](../architecture/frontend-interaction.md#fe-018)

# AWS runtime, deployment, security and operations

* [AWS-001 — Production Is Single-Active-Region, Multi-AZ, With Explicit Cold Regional Recovery](../architecture/aws-runtime-operations.md#aws-001)
* [AWS-002 — CloudFront Is the Public Application/Data Edge; Origins Remain Private](../architecture/aws-runtime-operations.md#aws-002)
* [AWS-003 — The Authoritative Application Runs on ECS/Fargate as API and Bounded Worker Roles](../architecture/aws-runtime-operations.md#aws-003)
* [AWS-004 — Production Capacity Favors Event Continuity Over Reactive-Only Scaling](../architecture/aws-runtime-operations.md#aws-004)
* [AWS-005 — RDS for PostgreSQL Multi-AZ Is the Production Authority Database](../architecture/aws-runtime-operations.md#aws-005)
* [AWS-006 — Cognito Authenticates; MUDAC Still Owns Identity, Participation, Access and Sessions](../architecture/aws-runtime-operations.md#aws-006)
* [AWS-007 — Private Evidence and Artifact Bytes Use Versioned, Encrypted S3 Behind Relational Authority Metadata](../architecture/aws-runtime-operations.md#aws-007)
* [AWS-008 — SQS Carries Retryable Asynchronous Work, Not Domain Authority](../architecture/aws-runtime-operations.md#aws-008)
* [AWS-009 — Application and Database Tiers Remain Private; Outbound Egress Is Explicit and Availability-Aware](../architecture/aws-runtime-operations.md#aws-009)
* [AWS-010 — IAM, Secrets and Encryption Preserve Least Privilege and Actor Separation](../architecture/aws-runtime-operations.md#aws-010)
* [AWS-011 — Production and Nonproduction Deployment Authority Is Account/Environment Separated and GitHub-OIDC Federated](../architecture/aws-runtime-operations.md#aws-011)
* [AWS-012 — Infrastructure and Releases Are Reproducible, Immutable and Rollback-Aware](../architecture/aws-runtime-operations.md#aws-012)
* [AWS-013 — Frontend Release Promotion Is Content-Addressed and API-Compatible](../architecture/aws-runtime-operations.md#aws-013)
* [AWS-014 — Edge/Infrastructure Security Complements but Never Replaces Application Authority](../architecture/aws-runtime-operations.md#aws-014)
* [AWS-015 — Observability Includes MUDAC Semantic Health, Not Only Infrastructure Utilization](../architecture/aws-runtime-operations.md#aws-015)
* [AWS-016 — Backups Are Multi-Layered, Cross-Region Where Material, and Trusted Only After Restore Testing](../architecture/aws-runtime-operations.md#aws-016)
* [AWS-017 — Regional Disaster Recovery Restores One Authority and Uses Paper for Live Continuity](../architecture/aws-runtime-operations.md#aws-017)
* [AWS-018 — Cost Optimization Removes Unjustified Infrastructure, Not Trust Guarantees](../architecture/aws-runtime-operations.md#aws-018)

# Implementation authority, toolchain and delivery

* [IMPL-001 — Upstream Canonical Meaning Outranks Implementation Convenience](../implementation/implementation-foundation.md#impl-001)
* [IMPL-002 — Application Implementation Uses One Primary TypeScript/Node Toolchain](../implementation/implementation-foundation.md#impl-002)
* [IMPL-003 — Fastify Is the Server Transport Host, Not the Domain Architecture](../implementation/implementation-foundation.md#impl-003)
* [IMPL-004 — pnpm Workspaces Are the Initial Repository Package/Workspace Mechanism](../implementation/implementation-foundation.md#impl-004)
* [IMPL-005 — PostgreSQL Access Uses Kysely Over node-postgres With Explicit Migrations](../implementation/implementation-foundation.md#impl-005)
* [IMPL-006 — API Schemas Are Explicit Transport Contracts and Generate OpenAPI Outward](../implementation/implementation-foundation.md#impl-006)
* [IMPL-007 — Verification Uses Vitest and Playwright Families With Evidence Defined Before Feature Scale](../implementation/implementation-foundation.md#impl-007)
* [IMPL-008 — Type, Lint and Formatting Checks Are Mandatory Implementation Gates](../implementation/implementation-foundation.md#impl-008)
* [IMPL-009 — Persistent AWS Infrastructure Is Implemented With OpenTofu](../implementation/implementation-foundation.md#impl-009)
* [IMPL-010 — Dependency Versions and Lockfiles Are Deliberate, Reproducible Inputs](../implementation/implementation-foundation.md#impl-010)
* [IMPL-011 — Generated Code Is Identifiable, Reproducible, and Not Hand-Owned](../implementation/implementation-foundation.md#impl-011)
* [IMPL-012 — Security and Supply-Chain Scanning Is Layered and Dispositioned](../implementation/implementation-foundation.md#impl-012)
* [IMPL-013 — `main` Is Intended to Be PR-Gated by Required Current Checks Before Implementation Merges](../implementation/implementation-foundation.md#impl-013)
* [IMPL-014 — Merge Does Not Imply Production Deployment Authority](../implementation/implementation-foundation.md#impl-014)
* [IMPL-015 — Material Implementation Decisions Are Recorded Without Becoming Upstream Redesign](../implementation/implementation-foundation.md#impl-015)
* [IMPL-016 — Phase 006 Subgroup Completion Requires Implementation and Evidence Closure](../implementation/implementation-foundation.md#impl-016)

# Active governance rule IDs resume here

The downstream candidate partition ends above. The governance IDs below remain current repository/documentation authority.

# Documentation authority

* [DOC-001 — Canonical Owner Controls Current Meaning](documentation-authority.md#doc-001)
* [DOC-002 — One Normative Rule Has One Canonical Owner](documentation-authority.md#doc-002)
* [DOC-003 — Downstream Artifacts Cannot Override Upstream Canonical Meaning](documentation-authority.md#doc-003)
* [DOC-004 — Historical Phase Records Are Append-Stable Provenance](documentation-authority.md#doc-004)
* [DOC-005 — Routing/Summary/Agent Artifacts Do Not Become Rule Owners](documentation-authority.md#doc-005)
* [DOC-006 — Knowledge Topology Does Not Dictate Source-Code Topology](documentation-authority.md#doc-006)
* [DOC-007 — Methodology Status Is Routed, Not Replicated Through Category Indexes](documentation-authority.md#doc-007)

# Agent context

* [CTX-001 — Start With Progressive Disclosure](agent-context.md#ctx-001)
* [CTX-002 — Load Only Task-Relevant Owners and Dependencies](agent-context.md#ctx-002)
* [CTX-003 — Historical Context Is On-Demand Through Lineage](agent-context.md#ctx-003)
* [CTX-004 — Stop Context Expansion When Authority Is Sufficient](agent-context.md#ctx-004)
* [CTX-005 — Recursive Corpus Loading Is Not the Default](agent-context.md#ctx-005)
* [CTX-006 — Resolve a Known Stable ID Directly Before Broad Discovery](agent-context.md#ctx-006)
* [CTX-007 — Minimum Sufficient Authoritative Context Is the Retrieval Objective](agent-context.md#ctx-007)
* [CTX-008 — Retrieval Expands Through Explicit Tiers](agent-context.md#ctx-008)
* [CTX-009 — Hard Byte Budgets Govern Routinely Loaded Routing Surfaces, Not Canonical Truth](agent-context.md#ctx-009)
* [CTX-010 — Representative Current-Task Packs Are Measured as Regression Evidence](agent-context.md#ctx-010)
* [CTX-011 — Cross-Owner Expansion Requires an Unresolved Semantic Dependency](agent-context.md#ctx-011)
* [CTX-012 — History, Quarantined Candidates and External Evidence Are Explicit Extended-Context Tiers](agent-context.md#ctx-012)
* [CTX-013 — Assembled Context Packs Are Ephemeral Unless They Have Independent Ownership Purpose](agent-context.md#ctx-013)
* [CTX-014 — Budget Pressure Is Resolved by Routing or Task Decomposition, Never Semantic Truncation](agent-context.md#ctx-014)
* [CTX-015 — Larger Model Context Windows Do Not Justify Routine Context Growth](agent-context.md#ctx-015)
* [CTX-016 — Broad-Audit Context Is Task-Scoped and Temporary](agent-context.md#ctx-016)

# Canonical change governance

* [CHG-001 — Semantic Change Updates the Canonical Owner Explicitly](change-governance.md#chg-001)
* [CHG-002 — Stable-Rule Semantic Change Requires Dependent Impact Review](change-governance.md#chg-002)
* [CHG-003 — Contradictions Are Surfaced, Not Silently Normalized](change-governance.md#chg-003)
* [CHG-004 — Canonical Semantic Changes Preserve Lineage and Navigation Coherence](change-governance.md#chg-004)
* [CHG-005 — Implementation Mismatch Is Resolved Downstream Unless Design Is Deliberately Changed](change-governance.md#chg-005)

# Phase-019 architecture decision authority and evidence

* [ADA-001 — Phase-019 Authority Derives Only From the 018-M Exit Decision](architecture-decision-authority.md#ada-001)
* [ADA-002 — The Exact Phase-018 Closure Baseline Is the Phase-019 Entry Snapshot](architecture-decision-authority.md#ada-002)
* [ADA-003 — ADQ-001 Through ADQ-010 Are the Governed Decision Graph](architecture-decision-authority.md#ada-003)
* [ADA-004 — Each Architecture Question Has a Durable Decision Record](architecture-decision-authority.md#ada-004)
* [ADA-005 — Decision State Is Explicit and Cannot Skip Acceptance Preconditions](architecture-decision-authority.md#ada-005)
* [ADA-006 — Individual Accepted Decisions Do Not Establish Accepted Whole Architecture](architecture-decision-authority.md#ada-006)
* [ADA-007 — Decision Evidence Must Distinguish Facts, Analysis, Probes and Runtime Proof](architecture-decision-authority.md#ada-007)
* [ADA-008 — Q4 Repair Produces a Current Comparison Translation, Not a Rewrite of History](architecture-decision-authority.md#ada-008)
* [ADA-009 — Credible Alternatives Are Recorded Before Selection](architecture-decision-authority.md#ada-009)
* [ADA-010 — Technical Probes Require Explicit Bounded Authorization](architecture-decision-authority.md#ada-010)
* [ADA-011 — Residual Uncertainty Is Recorded With a Revisit Trigger](architecture-decision-authority.md#ada-011)
* [ADA-012 — Whole-Architecture Acceptance Requires Complete Decision and Validation Closure](architecture-decision-authority.md#ada-012)
* [ADA-013 — Accepted Decisions Are Superseded Explicitly, Never Silently Rewritten](architecture-decision-authority.md#ada-013)
* [ADA-014 — Phase Progression Is Human-Directed and Dependency-Safe](architecture-decision-authority.md#ada-014)
* [ADA-015 — Implementation Remains Frozen Until Whole Architecture Acceptance](architecture-decision-authority.md#ada-015)
* [ADA-016 — Machine Decision Control Is Routing and Evidence State, Not Independent Semantic Authority](architecture-decision-authority.md#ada-016)
# Implementation program, verification and delivery gates

* [IPG-001 — Phase-018 Implementation Framework Does Not Create Active Packages or Execution Authority](implementation-program-delivery.md#ipg-001)
* [IPG-002 — Implementation Packages Derive From Accepted Architecture and Current Semantic Authority](implementation-program-delivery.md#ipg-002)
* [IPG-003 — Package Identity Is Durable and Independent of Source Layout](implementation-program-delivery.md#ipg-003)
* [IPG-004 — Every Package Has an Explicit Scope and Evidence Contract](implementation-program-delivery.md#ipg-004)
* [IPG-005 — Package Lifecycle Separates Planning, Authorization, Execution and Completion](implementation-program-delivery.md#ipg-005)
* [IPG-006 — Package Execution Is Human-Directed and Cannot Auto-Advance](implementation-program-delivery.md#ipg-006)
* [IPG-007 — Package Dependencies Must Be Explicit and Acyclic](implementation-program-delivery.md#ipg-007)
* [IPG-008 — Verification Evidence Uses Explicit Evidence Classes](implementation-program-delivery.md#ipg-008)
* [IPG-009 — Use the Smallest Trustworthy Evidence Layer That Crosses the Material Boundary](implementation-program-delivery.md#ipg-009)
* [IPG-010 — Phase-016 Scenario Seeds Must Survive Into Package and Program Verification](implementation-program-delivery.md#ipg-010)
* [IPG-011 — Data, Schema and Migration Changes Require Compatibility and Recovery Evidence](implementation-program-delivery.md#ipg-011)
* [IPG-012 — Supply Chain, Secrets, Fixtures and Sensitive Data Are Package Gates](implementation-program-delivery.md#ipg-012)
* [IPG-013 — Review, Merge, Release and Deployment Are Distinct Authorities](implementation-program-delivery.md#ipg-013)
* [IPG-014 — Package Completion Requires Evidence Closure, Not Merely Code Completion](implementation-program-delivery.md#ipg-014)
* [IPG-015 — Semantic and Architecture Mismatches Escalate Instead of Being Hidden in Implementation](implementation-program-delivery.md#ipg-015)
* [IPG-016 — Implementation Program Exit Requires Whole-System Evidence and Explicit Next Authority](implementation-program-delivery.md#ipg-016)
# Architecture re-entry evaluation and decision governance

* [ARE-001 — Phase-018 Architecture Re-entry Planning Does Not Select Architecture](architecture-reentry-evaluation.md#are-001)
* [ARE-002 — Current Semantic Authority and ENG Obligations Are Hard Decision Constraints](architecture-reentry-evaluation.md#are-002)
* [ARE-003 — Architecture Questions Have Explicit Scope, Dependencies and Deferrals](architecture-reentry-evaluation.md#are-003)
* [ARE-004 — Material Architecture Choices Require Credible Alternatives](architecture-reentry-evaluation.md#are-004)
* [ARE-005 — Q4 Candidate Material Is Inadmissible Unchanged](architecture-reentry-evaluation.md#are-005)
* [ARE-006 — Architecture Evaluation Uses a Common Evidence Envelope](architecture-reentry-evaluation.md#are-006)
* [ARE-007 — Evidence Strength and Uncertainty Stay Calibrated](architecture-reentry-evaluation.md#are-007)
* [ARE-008 — The Architecture Decision Graph Is Dependency-Safe](architecture-reentry-evaluation.md#are-008)
* [ARE-009 — Accepted Architecture Decisions Require Explicit Decision Evidence](architecture-reentry-evaluation.md#are-009)
* [ARE-010 — Architecture Authority Is Created Only by Explicit Acceptance](architecture-reentry-evaluation.md#are-010)
* [ARE-011 — Architecture Probes Are Separate, Bounded Evidence Activities](architecture-reentry-evaluation.md#are-011)
* [ARE-012 — Architecture Re-entry Ends Before Implementation Execution Begins](architecture-reentry-evaluation.md#are-012)
# Downstream realization and engineering handoff

* [ENG-001 — Conceptual Obligation Precedes Mechanism Selection](downstream-realization-obligations.md#eng-001)
* [ENG-002 — Retention and Jurisdiction-Specific Compliance Remain Evidence-Bounded Until Externally Established](downstream-realization-obligations.md#eng-002)
* [ENG-003 — Competition-Specific Policy Values Remain Explicit Configuration](downstream-realization-obligations.md#eng-003)
* [ENG-004 — Identity, Participation, Access, Authorship and Technical Privilege Remain Distinct](downstream-realization-obligations.md#eng-004)
* [ENG-005 — One Logical Evaluation and Evidence/Authorship Integrity Survive Retries, Capture Paths and Correction](downstream-realization-obligations.md#eng-005)
* [ENG-006 — Currentness, History, Provenance and Correction Remain Simultaneously Reconstructible](downstream-realization-obligations.md#eng-006)
* [ENG-007 — Current-State, Concurrency, Retry and Uncertainty Preserve Owner Truth](downstream-realization-obligations.md#eng-007)
* [ENG-008 — Offline, Multi-Device, Degraded and Paper Recovery Converge Without Multiplying Domain Subjects](downstream-realization-obligations.md#eng-008)
* [ENG-009 — Outcome and Officiality Distinctions Remain Explicit](downstream-realization-obligations.md#eng-009)
* [ENG-010 — Source, Export, Publication and Possession Remain Separate](downstream-realization-obligations.md#eng-010)
* [ENG-011 — Security, Disclosure and Abuse Controls Protect Semantic Authority Rather Than Replacing It](downstream-realization-obligations.md#eng-011)
* [ENG-012 — Accessibility and Device Continuity Preserve Consequential Semantic Parity](downstream-realization-obligations.md#eng-012)
* [ENG-013 — Availability, Deployment and Recovery Mechanisms Preserve Truthful Authority Under Failure](downstream-realization-obligations.md#eng-013)
* [ENG-014 — Phase-016 Semantic Scenarios Are Mandatory Downstream Verification Seeds](downstream-realization-obligations.md#eng-014)
* [ENG-015 — Evidence Strength Must Match the Downstream Claim](downstream-realization-obligations.md#eng-015)
* [ENG-016 — Supply-Chain, Secrets, Fixture/Privacy and Migration Controls Must Exist Before Implementation Sprawl](downstream-realization-obligations.md#eng-016)
* [ENG-017 — Historical Architecture, Implementation and Executable Substrate Remain Evidence Until Explicitly Qualified](downstream-realization-obligations.md#eng-017)
* [ENG-018 — Provider/Tool Runtime Compatibility Is Required Only When Relied Upon and Is Evidence-Calibrated](downstream-realization-obligations.md#eng-018)
# Agentic conformance, drift detection and CI evidence

* [CNF-001 — Integrated Conformance Proves Repository Configuration Health, Not Domain/Runtime Health](agentic-conformance.md#cnf-001)
* [CNF-002 — Phase Program Indexes Own Phase Progression; Status Mirrors Are Derived](agentic-conformance.md#cnf-002)
* [CNF-003 — Generated Artifacts Must Be Exactly Reproducible From Authored Sources](agentic-conformance.md#cnf-003)
* [CNF-004 — Stable-Reference Integrity Is Fail-Closed and Role-Aware](agentic-conformance.md#cnf-004)
* [CNF-005 — Critical Guards Require Executable Negative Controls](agentic-conformance.md#cnf-005)
* [CNF-006 — Agent Workflow/Adapters Remain Subordinate Under Conformance](agentic-conformance.md#cnf-006)
* [CNF-007 — Secret Scanning Is Narrow, High-Confidence and Not a Substitute for Enterprise Scanning](agentic-conformance.md#cnf-007)
* [CNF-008 — Knowledge CI Remains Read-Only Against Repository Authority](agentic-conformance.md#cnf-008)
* [CNF-009 — Blocking Checks Cannot Be Silently Downgraded by Orchestration](agentic-conformance.md#cnf-009)
* [CNF-010 — Evidence Classes Remain Explicit](agentic-conformance.md#cnf-010)
* [CNF-011 — Provider Runtime Compatibility Remains Separate From Static Adapter Conformance](agentic-conformance.md#cnf-011)
* [CNF-012 — Conformance Must Remain Proportional and Architecture-Neutral Before Re-entry](agentic-conformance.md#cnf-012)

# Portable agent workflows and tool adapters

* [WFL-001 — Canonical Reusable Workflows Live Once Under .agents/skills](agent-workflow-portability.md#wfl-001)
* [WFL-002 — Skills Own Procedure, Not Product Semantics](agent-workflow-portability.md#wfl-002)
* [WFL-003 — Every Canonical Skill Declares Its Human-Directed Boundary and Stop Conditions](agent-workflow-portability.md#wfl-003)
* [WFL-004 — Provider Adapters Are Thin Routing Bridges](agent-workflow-portability.md#wfl-004)
* [WFL-005 — Provider-Native Discovery Differences Do Not Change MUDAC Authority](agent-workflow-portability.md#wfl-005)
* [WFL-006 — Workflow Action Class Is Fixed by the Canonical Workflow Contract](agent-workflow-portability.md#wfl-006)
* [WFL-007 — Execute-Selected-Task Cannot Manufacture Implementation Authority](agent-workflow-portability.md#wfl-007)
* [WFL-008 — Run-Conformance Reports Failures Faithfully and Does Not Self-Fix by Default](agent-workflow-portability.md#wfl-008)
* [WFL-009 — Review-Change Remains A1 Unless the Human Explicitly Requests Fixes](agent-workflow-portability.md#wfl-009)
* [WFL-010 — Exit Review Stops After the Selected Boundary](agent-workflow-portability.md#wfl-010)
* [WFL-011 — Tool Compatibility Claims Are Evidence-Calibrated](agent-workflow-portability.md#wfl-011)
* [WFL-012 — Adapter Failure Degrades Provider Convenience, Not Semantic Authority](agent-workflow-portability.md#wfl-012)

# Agentic development authority and scope

* [AGT-001 — Human-Selected Work Establishes the Task Envelope, Not Product Authority](agentic-authority-scope.md#agt-001)
* [AGT-002 — Repository Authority Outranks Tools, Prompts, Memory and Convenience](agentic-authority-scope.md#agt-002)
* [AGT-003 — A1 Review, Inspection, Assessment and Planning Do Not Authorize Repository Edits](agentic-authority-scope.md#agt-003)
* [AGT-004 — A2 Authorizes Bounded Repository Changes Necessary to Complete the Selected Task](agentic-authority-scope.md#agt-004)
* [AGT-005 — Supporting Changes Must Be Necessary, Proportional and Causally Tied to the Task](agentic-authority-scope.md#agt-005)
* [AGT-006 — A3 External, Destructive or Scope-Expanding Actions Require Explicit Human Authorization](agentic-authority-scope.md#agt-006)
* [AGT-007 — A4 Semantic or Accepted-Architecture Change Requires Explicit Human Change Intent and Governed Propagation](agentic-authority-scope.md#agt-007)
* [AGT-008 — Implementation Difficulty Never Authorizes Weakening Semantic Authority](agentic-authority-scope.md#agt-008)
* [AGT-009 — Task Completion Stops at the Selected Boundary](agentic-authority-scope.md#agt-009)
* [AGT-010 — MUDAC Agentic Development Is Human-Directed, Not Autonomously Work-Selecting](agentic-authority-scope.md#agt-010)
* [AGT-011 — Tool Adapters Are Subordinate and No Coding Agent Is Semantically Privileged](agentic-authority-scope.md#agt-011)
* [AGT-012 — Memory, Chat History and Generated Summaries Are Advisory Only](agentic-authority-scope.md#agt-012)
* [AGT-013 — Retrieved External Content Is Evidence or Guidance, Not Repository Authority by Default](agentic-authority-scope.md#agt-013)
* [AGT-014 — Safe Validation Is Part of Bounded Work; Consequential Execution Is Not](agentic-authority-scope.md#agt-014)
* [AGT-015 — Secrets, Real Sensitive Data and Privilege Expansion Remain Outside Ordinary Agent Scope](agentic-authority-scope.md#agt-015)
* [AGT-016 — Conflict Behavior Is Fail-Closed and Surfaced When It Affects Scope or Authority](agentic-authority-scope.md#agt-016)

# Deterministic ownership and stable resolution

* [OWN-001 — Semantic Authority Remains in Authored Owner Documents](deterministic-ownership-resolution.md#own-001)
* [OWN-002 — Ownership Role Is Classified Before Path Content Is Trusted](deterministic-ownership-resolution.md#own-002)
* [OWN-003 — Exact Stable-ID Resolution Defaults to Current Authority Only](deterministic-ownership-resolution.md#own-003)
* [OWN-004 — Suspended Downstream IDs Require Explicit Candidate Resolution](deterministic-ownership-resolution.md#own-004)
* [OWN-005 — Deprecated and Historical Adapters Never Satisfy Current Resolution](deterministic-ownership-resolution.md#own-005)
* [OWN-006 — Numbered-Phase Occurrences Are Provenance Only and Opt-In](deterministic-ownership-resolution.md#own-006)
* [OWN-007 — Generated Ownership Indexes Are Deterministic and Rebuildable](deterministic-ownership-resolution.md#own-007)
* [OWN-008 — Resolution Fails Closed on Drift](deterministic-ownership-resolution.md#own-008)
* [OWN-009 — Stable Identity Is the Rule ID, Not Its Current File Path](deterministic-ownership-resolution.md#own-009)
* [OWN-010 — Unknown-Subject Discovery and Known-ID Resolution Are Different Operations](deterministic-ownership-resolution.md#own-010)
* [OWN-011 — Artifact Lifecycle Status and Semantic Owner Role Remain Distinct](deterministic-ownership-resolution.md#own-011)
* [OWN-012 — Routing/Status Mirrors Cannot Become Independent Authority](deterministic-ownership-resolution.md#own-012)

# OKF metadata, trust, lifecycle and freshness

* [META-001 — Canonical Knowledge Uses a Deliberate MUDAC Frontmatter Profile](metadata-trust-lifecycle.md#meta-001)
* [META-002 — `generated` Records the Actual Producer of Current Meaningful Content](metadata-trust-lifecycle.md#meta-002)
* [META-003 — `verified` Records an Actual Content/Source Confirmation Event](metadata-trust-lifecycle.md#meta-003)
* [META-004 — OKF `status` Describes Knowledge-Artifact Lifecycle, Not MUDAC Domain State](metadata-trust-lifecycle.md#meta-004)
* [META-005 — `stale_after` Is Used Only for a Real Absolute Freshness Boundary](metadata-trust-lifecycle.md#meta-005)
* [META-006 — Source Credibility Metadata Must Remain Factual and Material](metadata-trust-lifecycle.md#meta-006)
* [META-007 — OKF Trust Signals Do Not Replace MUDAC Authority or Access](metadata-trust-lifecycle.md#meta-007)
* [META-008 — Legacy Records Are Not Speculatively Backfilled](metadata-trust-lifecycle.md#meta-008)
* [META-009 — Metadata Updates Preserve Semantic and Historical Distinctions](metadata-trust-lifecycle.md#meta-009)
* [META-010 — Authored Documentation and Strict OKF Compatibility Are Separate Layers](metadata-trust-lifecycle.md#meta-010)

# Validation and CI enforcement

* [VAL-001 — Validation Proves Structural Conformance, Not Semantic Verification](validation-enforcement.md#val-001)
* [VAL-002 — Current Canonical/Reference Knowledge Receives Deterministic Metadata-Shape Checks](validation-enforcement.md#val-002)
* [VAL-003 — Stable Rule IDs Are Globally Unique, Explicitly Anchored, and Registry-Resolvable](validation-enforcement.md#val-003)
* [VAL-004 — Current Authority Links and Local Source Edges Must Resolve](validation-enforcement.md#val-004)
* [VAL-005 — Progressive-Disclosure Routing Surfaces Are Structural Requirements](validation-enforcement.md#val-005)
* [VAL-006 — Legacy Exemptions Are Explicit and Must Not Become Blanket Validation Bypasses](validation-enforcement.md#val-006)
* [VAL-007 — Knowledge Validation Is a Blocking, Read-Only CI Check](validation-enforcement.md#val-007)
* [VAL-008 — Validator Evolution Is Governed Because It Encodes Repository Policy](validation-enforcement.md#val-008)

# Change impact

A proposed semantic change to an identified rule must trigger review of known canonical dependents and, once present, architecture/tests that cite the ID. [Canonical Change & Conflict Governance](change-governance.md) defines the workflow; [OKF Metadata, Trust, Verification, Lifecycle & Freshness](metadata-trust-lifecycle.md) governs knowledge-artifact metadata; [Knowledge Validation & CI Enforcement](validation-enforcement.md) governs deterministic CI enforcement.
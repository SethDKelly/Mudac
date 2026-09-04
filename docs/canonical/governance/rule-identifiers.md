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
generated: { by: openai/gpt-5.6-sol, at: 2026-09-04T05:28:35Z }
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
* [INV-002 — One Logical Scorecard per Judge × Encounter](../invariants/one-logical-scorecard.md#inv-002)
* [INV-003 — Missing Is Never Zero](../invariants/missing-never-zero.md#inv-003)
* [INV-004 — Organizer Authority Does Not Become Judge Authorship](../invariants/organizer-not-judge-author.md#inv-004)
* [INV-005 — Current and Historical Truth Remain Distinct](../invariants/current-vs-historical-truth.md#inv-005)
* [INV-006 — Calculated Is Not Official](../invariants/calculated-not-official.md#inv-006)
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

# Official Outcomes

* [OUT-001 — Finalization Establishes an Official Outcome Revision](../mechanisms/official-outcome-revision.md#out-001)
* [OUT-002 — Official Correction Requires Explicit Successor Confirmation](../mechanisms/official-outcome-revision.md#out-002)

# Disclosure

* [DISC-001 — Blinded Judge Team Identity](../policies/anonymity-disclosure.md#disc-001)
* [DISC-002 — Disclosure Is Audience and Purpose Specific](../policies/anonymity-disclosure.md#disc-002)

# Export

* [EXPORT-001 — Export Represents Source Truth; It Does Not Replace It](../concepts/export.md#export-001)
* [EXPORT-002 — Generation and Publication Are Distinct](../concepts/export.md#export-002)

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

# Documentation authority

* [DOC-001 — Canonical Owner Controls Current Meaning](documentation-authority.md#doc-001)
* [DOC-002 — One Normative Rule Has One Canonical Owner](documentation-authority.md#doc-002)
* [DOC-003 — Downstream Artifacts Cannot Override Upstream Canonical Meaning](documentation-authority.md#doc-003)
* [DOC-004 — Historical Phase Records Are Append-Stable Provenance](documentation-authority.md#doc-004)
* [DOC-005 — Routing/Summary/Agent Artifacts Do Not Become Rule Owners](documentation-authority.md#doc-005)
* [DOC-006 — Knowledge Topology Does Not Dictate Source-Code Topology](documentation-authority.md#doc-006)

# Agent context

* [CTX-001 — Start With Progressive Disclosure](agent-context.md#ctx-001)
* [CTX-002 — Load Only Task-Relevant Owners and Dependencies](agent-context.md#ctx-002)
* [CTX-003 — Historical Context Is On-Demand Through Lineage](agent-context.md#ctx-003)
* [CTX-004 — Stop Context Expansion When Authority Is Sufficient](agent-context.md#ctx-004)
* [CTX-005 — Recursive Corpus Loading Is Not the Default](agent-context.md#ctx-005)

# Canonical change governance

* [CHG-001 — Semantic Change Updates the Canonical Owner Explicitly](change-governance.md#chg-001)
* [CHG-002 — Stable-Rule Semantic Change Requires Dependent Impact Review](change-governance.md#chg-002)
* [CHG-003 — Contradictions Are Surfaced, Not Silently Normalized](change-governance.md#chg-003)
* [CHG-004 — Canonical Semantic Changes Preserve Lineage and Navigation Coherence](change-governance.md#chg-004)
* [CHG-005 — Implementation Mismatch Is Resolved Downstream Unless Design Is Deliberately Changed](change-governance.md#chg-005)

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
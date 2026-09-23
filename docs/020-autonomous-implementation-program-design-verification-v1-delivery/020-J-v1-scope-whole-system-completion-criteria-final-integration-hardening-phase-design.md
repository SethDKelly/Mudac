---
type: Phase Record
title: 020-J — v1 Scope, Whole-System Completion Criteria & Final Integration/Hardening Phase Design
description: "Defines the PF-01 v1 implementation boundary, whole-system completion predicates, integrated critical journeys, terminal integration/hardening phase, immutable v1 completion evidence and the explicit separation between implementation completion, G6 release-candidate authority and G7 production readiness."
status: stable
tags: [phase-020, v1, whole-system, integration, hardening, completion, release-boundary]
sources:
  - resource: README.md
  - resource: 020-F-implementation-phase-contract-visible-criteria-evidence-classes-hidden-evaluation-architecture.md
  - resource: 020-G-ci-cd-security-supply-chain-exact-sha-verification-evidence-bundle-architecture.md
  - resource: 020-H-independent-code-review-adversarial-review-repair-reopen-exit-gate-governance.md
  - resource: 020-I-migration-recovery-accessibility-performance-cost-scenario-verification-design.md
  - resource: ../canonical/project/mandate-context.md
  - resource: ../canonical/project/purpose-needs-success-tensions.md
  - resource: ../canonical/dependence/product-family-scope.md
  - resource: ../canonical/architecture/accepted-architecture.md
  - resource: ../canonical/governance/implementation-program-delivery.md
  - resource: ../routing/phase020_v1_completion_integration_design.json
generated: { by: openai/gpt-5.6-sol, at: 2026-09-23T13:56:00-05:00 }
---

# Purpose

Define exactly what the first implemented MUDAC v1 means at the **implementation-program boundary**.

020-J answers:

1. which product scope v1 must realize;
2. what package completion is insufficient to prove;
3. which composed user/system journeys must work end to end;
4. what whole-system evidence is required after package-local completion;
5. what the final integration/hardening phase may and may not do; and
6. where implementation completion stops before release-candidate and production authority.

020-J is still **pre-implementation design**.

It grants no G1, G2, G6 or G7 authority.

# Entry state

~~~text
PHASE 020 ACTIVE
020-A/B/C/D/E/F/G/H/I COMPLETE
020-J NEXT ELIGIBLE / USER AUTHORIZED

proposed packages                 15
G1-ready packages                 0
G2-authorized packages            0
active implementation packages    0
implementation execution          NOT AUTHORIZED
release authority                 NOT GRANTED
production authority              NOT GRANTED
~~~

Exact planning baseline:

> 73c56b965060321e1f742df5026ec75465b0fbd6

# Decision

**020-J — ACCEPT PF-01 AS THE V1 PRODUCT BOUNDARY AND REQUIRE A TERMINAL WHOLE-SYSTEM INTEGRATION/HARDENING PHASE BEFORE V1 IMPLEMENTATION COMPLETION.**

The governing distinction is:

> **All packages complete does not by itself mean v1 complete.**

And:

> **v1 implementation complete does not mean release candidate authorized, deployed, or production ready.**

# v1 product scope

The initial v1 realizes the sole adopted current product variant:

> **PF-01 — MUDAC Live Competition Judging & Official Outcome**

v1 is the initial implemented baseline of PF-01, not a new product-family definition.

All eighteen current Concepts remain in product scope:

~~~text
Competition
Division
Team
Panel
Evaluation Occurrence
Evaluation Obligation
Rubric
Scorecard
Award
Identity
Participation
Alias
Access
Versioning
Provenance
Outcome Declaration
Export
Publication
~~~

Not every Competition must instantiate every optional capability.

For example, a Competition may have no Award, an Outcome Declaration may remain non-public, and an Export may exist without Publication. Those are PF-01 profiles rather than reduced product variants.

# v1 capability envelope

v1 must support the current judged/outcome lifecycle as one coherent application:

- competition judging-context and policy setup;
- competitor establishment and bias-aware Team identity/Alias handling;
- Judge/Organizer Identity, Participation, Access and session realization;
- Panel and Evaluation Occurrence preparation/operation;
- Evaluation Obligation and remaining-work realization;
- exact Rubric/evaluation basis;
- independent Scorecard Draft and authoritative Finalization;
- offline/shared-device/paper/electronic continuity and reconciliation;
- live Organizer visibility into readiness, gaps and exceptions;
- history/Provenance-preserving amendment/correction;
- Coverage/Aggregate/Rank derivation with missingness preserved;
- Award support as event-optional recognition;
- ordinary and exceptional/no-result Outcome Declaration;
- source-bound Export generation/currentness;
- controlled Publication/release/withdrawal/successor behavior;
- accessible/responsive/degraded semantic parity;
- enough operational deployment, backup/recovery and evidence infrastructure to support later release evaluation.

This is a capability boundary, not permission to introduce additional product semantics.

# Explicit v1 non-goals

The current project boundary already excludes, and v1 continues to exclude:

- student accounts/dashboard;
- student submission management;
- dataset hosting/distribution;
- notebook, analytics or ML execution infrastructure;
- faculty-advisor management;
- general ticketing/marketing;
- prize payment/disbursement;
- general-purpose competition management outside judging/outcomes;
- advanced Judge normalization/calibration as mandatory core behavior;
- formal room/time-slot scheduling optimization;
- notification systems as required core functionality;
- rich public-results portal beyond controlled representation/release;
- unadopted product-family contractions;
- intentionally non-blinded judging;
- new semantic owners introduced merely for workflow convenience.

Activating one of these requires explicit scope/change authority.

The final integration phase cannot smuggle future-scope work into v1 under the label "hardening."

# Package relation to v1

The current implementation candidate set remains:

> **IMP-001 through IMP-015**

020-J treats all fifteen as expected v1 work **if retained by 020-K**.

020-K retains authority to split, merge or supersede a candidate while creating final implementation-phase/package definitions, but it may not lose a current v1 obligation while doing so.

Therefore:

~~~text
15 current package candidates
    != 15 immutable future package shapes

but

all current v1 obligations
    == must survive final 020-K decomposition
~~~

No package becomes G1-ready in 020-J.

# Package completion versus system completion

A package G5 record proves that package against its package contract.

It does not prove:

- cross-package journeys;
- all fifteen scenario compositions;
- final integrated configuration;
- whole-system Access/privacy behavior;
- final migration/restore behavior;
- end-to-end accessibility;
- event-load behavior;
- final artifact/evidence composition;
- absence of integration-created architecture drift.

Thus:

> **package G5 closure is necessary but not sufficient for v1 implementation completion.**

# Integrated critical journeys

020-J defines nine mandatory whole-system journey families.

## JNY-01 — Competition preparation and blinded judging context

An Organizer can establish:

- Competition/Division/Team/Alias;
- Judge Identity/Participation/Access;
- Panel;
- Evaluation Occurrence;
- Evaluation Obligation;
- exact Rubric/evaluation basis.

Bias-sensitive disclosure remains correct throughout preparation.

## JNY-02 — Judge entry, Draft, independent evaluation and Finalization

A Judge can:

- enter the correct current context;
- perform accessible independent judging;
- preserve Draft semantics;
- Finalize through the authoritative command path;
- receive truthful confirmation;
- see correct remaining responsibility.

Peer information or protected identity cannot leak merely because the integrated UI/runtime is functioning.

## JNY-03 — Interruption, device, offline and paper continuity

The integrated system demonstrates:

- local Draft preservation;
- shared-device privacy/context reset;
- offline/degraded continuity;
- paper fallback;
- one logical evaluation;
- reconnect and current Access reevaluation;
- conflict/uncertain-result recovery.

## JNY-04 — Organizer live operations, incompletion and exceptions

The Organizer can identify and act on:

- readiness;
- remaining obligations;
- missing evidence;
- substitution/reassignment;
- exceptions;
- partial/unknown outcomes;

without inventing judgment or transferring authorship.

## JNY-05 — Correction, Versioning, Provenance and affectedness

Legitimate corrections preserve:

- prior historical authority;
- current successor authority;
- actor/authorship distinction;
- correction lineage;
- affected/stale downstream state.

## JNY-06 — Outcome formation, recognition and official declaration

The system demonstrates:

- Coverage/Aggregate/Rank distinction;
- Award optionality;
- ordinary outcome closeout;
- exceptional/no-result closeout;
- explicit Outcome Declaration;
- affected/successor declaration behavior.

## JNY-07 — Export, Publication and external possession

The system preserves:

~~~text
source authority
!= Export
!= Publication
!= recipient possession
~~~

including currentness, disclosure, release, withdrawal and successor behavior.

## JNY-08 — Access revocation, privacy and technical-support separation

The integrated system proves:

- stale/revoked Access is denied;
- private browser/local state is not leaked across context;
- technical privilege does not become competition authority;
- support/recovery does not transfer authorship.

## JNY-09 — Deployment failure, restore and resumed digital authority

Operational evidence demonstrates:

- immutable release identity;
- backup/restore;
- application consistency validation;
- derived-state restoration/currentness;
- one-authority regional recovery;
- paper/local trace reconciliation before digital authority resumes.

# Whole-system completion criteria

020-J establishes twelve stable program-level criteria.

## V1-WS-01 — PF-01 scope fidelity

The integrated system realizes PF-01 and does not add an unapproved non-goal or alternate product variant.

## V1-WS-02 — Package/dependency closure

Every final retained v1 package has a qualifying G5 completion record and all hard, integration and evidence dependencies are closed or explicitly non-applicable.

## V1-WS-03 — Purpose and semantic traceability

P-01 through P-09, all eighteen Concepts, current policies/invariants and accepted architecture trace to implemented ownership with no unexplained semantic gap.

## V1-WS-04 — Integrated critical journeys

JNY-01 through JNY-09 pass across their actual material browser/API/persistence/provider boundaries.

## V1-WS-05 — Fifteen-scenario composed replay

SCN-01 through SCN-15 all PASS on the final qualifying integrated candidate at the composed boundaries defined in 020-I.

## V1-WS-06 — Architecture and ownership conformance

All nine accepted architecture families remain satisfied with:

- no reverse-authority path;
- no owner-boundary contradiction;
- no unapproved architecture change.

## V1-WS-07 — Security, privacy and authority hardening

Integrated Access/disclosure, abuse protection, secrets, technical privilege and test-control boundaries pass their required behavioral and supply-chain evidence.

## V1-WS-08 — Migration, recovery and degraded continuity

Supported migration, uncertain-command recovery, projection rebuild, backup restore and applicable DR/degraded paths preserve authority/history at the required evidence floors.

## V1-WS-09 — Accessibility and responsive semantic parity

Critical Judge and Organizer flows meet the visible WCAG 2.2 AA-oriented semantic-parity contract with both automated and required manual evidence.

## V1-WS-10 — Performance, event-load and cost

Visible performance/workload requirements pass in the declared environment; event pressure does not weaken semantic truth; material runtime cost/control evidence exists.

## V1-WS-11 — Build, supply-chain and evidence integrity

The final candidate has:

- reproducible exact-revision verification;
- required security/supply-chain evidence;
- SBOM/provenance/attestation where applicable;
- immutable whole-system evidence.

## V1-WS-12 — Knowledge, operations and residual-risk closure

Canonical/routing/operational knowledge matches the final candidate, no known blocker is hidden, and every accepted non-blocking residual risk has an owner and revisit gate.

All twelve criteria are blocking for v1 implementation completion.

# Terminal final integration/hardening phase

020-J creates the **logical** terminal implementation phase:

> **V1-FINAL**

020-K owns its final phase number and title.

V1-FINAL is not a new semantic package or product owner.

Its purpose is to qualify **one composed revision** rather than fifteen individually green package histories.

# V1-FINAL entry gate

The final phase requires:

- explicit G2 for the final phase;
- all final retained v1 packages G1-complete;
- all predecessor implementation phases complete;
- all retained v1 packages G5 before final evidence freeze;
- exact integrated baseline SHA/tree;
- healthy integration/nonproduction environment;
- working test-control and evidence infrastructure;
- no unresolved semantic or accepted-architecture blocker;
- repository-enforcement evidence before main protection is trusted as a control.

No part of Phase 020 grants this future G2.

# Important G5/hardening interaction

020-H established that a package's prior G2 closes when that package reaches G5.

V1-FINAL therefore **does not gain blanket authority to edit completed packages**.

020-K must explicitly identify integration-owned surfaces.

If V1-FINAL reveals a defect:

- integration-only defect inside a declared V1-FINAL surface → repair inside V1-FINAL G2;
- defect in source owned by a completed package → **020-H REOPEN_REQUIRED + explicit re-authorization**;
- missing package scope → program/package replan;
- semantic contradiction → Concept/change governance;
- accepted-architecture contradiction → architecture re-entry;
- external/provider/legal blocker → evidence-bounded BLOCKED/escalation.

This is intentionally stricter than letting a final phase become an uncontrolled "fix anything" phase.

# Permitted final-phase work

Within its declared surfaces, V1-FINAL may perform:

- whole-system test/evidence orchestration;
- final integration-only configuration;
- scenario/journey harness composition;
- release-candidate evidence assembly without granting release authority;
- documentation/traceability reconciliation;
- non-semantic operational hardening.

# Prohibited final-phase work

V1-FINAL may not:

- add a new product feature/Concept;
- activate a v1 non-goal;
- silently change accepted architecture;
- edit completed package-owned source without reopen/re-authorization;
- lower criteria or evidence floors;
- use production merely to fill missing preproduction evidence;
- grant release or production authority.

# Final candidate identity

The qualifying v1 candidate records:

- exact commit SHA;
- exact tree SHA;
- immutable artifact digest set;
- integration environment identity;
- criteria-contract version;
- scenario-matrix version.

All whole-system evidence and reviews bind to that candidate.

# Whole-system evidence bundle

v1 closure produces one immutable, content-addressed whole-system bundle containing at least:

- final candidate SHA/tree;
- retained package G5 records;
- V1-WS-01..12;
- JNY-01..09;
- SCN-01..15;
- architecture conformance;
- security/privacy/access review;
- migration/recovery evidence;
- manual + automated accessibility evidence;
- performance/event-load evidence;
- cost evidence/guards;
- SBOM/provenance/attestation;
- independent code review;
- adversarial conformance review;
- repository-enforcement evidence;
- failure/retry history;
- exceptions/residual risks;
- Gatekeeper decision.

Missing mandatory evidence yields BLOCKED/INCONCLUSIVE rather than assumed success.

# V1 completion state

The successful terminal state is:

> **V1_IMPLEMENTATION_COMPLETE**

Meaning:

> the PF-01 v1 implementation-program obligations are complete on one qualifying integrated revision.

It does **not** mean:

- G6 granted;
- deployment authorized;
- G7 granted;
- production ready.

The successor lifecycle state is:

> **RELEASE_CANDIDATE_ELIGIBLE_NOT_AUTHORIZED**

# G6 handoff

G6 remains separate and requires explicit release authority.

Valid E6 evidence from V1-FINAL may be reused where:

- it still applies;
- release source/artifact identity matches;
- configuration has not materially changed.

If release packaging/configuration creates a different material tree or artifact, affected evidence reruns.

At minimum, G6 reconciles:

- release artifact/provenance;
- deployment/migration/rollback;
- restore/recovery;
- event-load evidence;
- critical-flow accessibility;
- runtime cost/security/observability controls.

G6 remains distinct from G7.

# Residual risk

v1 completion requires **zero known blocking findings**.

Non-blocking residual risk may remain only with:

- owner;
- rationale;
- impact;
- revisit gate/trigger.

Residual risk cannot hide:

- an unsatisfied visible criterion;
- architecture contradiction;
- semantic contradiction;
- failed mandatory scenario.

A future improvement outside the v1 requirement does not block v1 merely because it would be useful.

# Anti-bloat rules

The final hardening phase is particularly vulnerable to agentic scope expansion.

Therefore:

- final hardening is not a feature catch-all;
- explicit non-goals remain out;
- generic infrastructure needs a current v1 obligation;
- semantic rules are not duplicated into integration orchestration;
- accepted architecture is not redesigned for aesthetic uniformity;
- non-required improvements route to backlog/residual risk unless separately authorized.

# Relationship to 020-K

020-J closes the **program-level target**.

020-K now has enough authority to define:

- final implementation phase sequence;
- final package plans;
- package-specific visible criteria/evidence;
- package G1 readiness;
- Coordinator/Implementer/Reviewer assignment strategy;
- V1-FINAL's final phase number/name and integration-owned surfaces.

020-K may refine decomposition but cannot weaken the v1 boundary defined here.

# Machine contract

Current projection:

> docs/routing/phase020_v1_completion_integration_design.json

Phase-020 validation must fail if:

- PF-01 stops being the v1 target without scope change;
- any of the eighteen Concepts disappears from v1 product scope;
- P-01..P-09 stop being whole-system obligations;
- any JNY-01..09 or V1-WS-01..12 disappears;
- SCN-01..15 are no longer required for final composed replay;
- final hardening gains blanket write authority over completed packages;
- final hardening may add features/non-goals;
- v1 completion grants G6/G7/deployment authority;
- package completion is treated as sufficient for v1 completion;
- blocking residual risk is allowed;
- 020-J promotes packages to G1/G2.

# Phase-020 boundary after 020-J

~~~text
PHASE 020 ACTIVE
020-A/B/C/D/E/F/G/H/I/J COMPLETE
020-K NEXT ELIGIBLE

proposed packages                 15
G1-ready packages                 0
G2-authorized packages            0
active implementation packages    0
implementation execution          NOT AUTHORIZED
release authority                 NOT GRANTED
production authority              NOT GRANTED
~~~

# Exit decision

**020-J — COMPLETE — PASS.**

MUDAC now has a bounded v1 product definition, program-level completion contract and terminal integration/hardening design that proves a composed PF-01 implementation without letting final hardening become a new product-design phase or letting implementation completion masquerade as release/production authority.

Next eligible:

> **020-K — Full Autonomous Implementation Roadmap, Agent Assignment Strategy, Phase/Package Definitions & Entry Readiness**

020-K is **NEXT ELIGIBLE / NOT AUTOMATICALLY AUTHORIZED**.

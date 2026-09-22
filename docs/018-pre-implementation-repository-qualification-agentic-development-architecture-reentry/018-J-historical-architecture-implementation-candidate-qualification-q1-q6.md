---
type: Phase Qualification
title: 018-J — Historical Architecture & Implementation Candidate Qualification Under Q1–Q6
description: Qualifies all preserved downstream architecture and implementation candidates against the current Q1–Q6 re-entry model, ENG realization obligations, Phase-016 validation seeds and ERI risks; records comparison eligibility, stale semantic bindings, technology revalidation needs and frozen executable facts without selecting or activating architecture.
status: stable
tags: [phase-018, architecture, implementation, candidates, q1-q6, qualification, reentry, quarantine]
sources:
  - resource: 018-I-downstream-realization-obligation-carry-forward-engineering-risk-reconciliation.md
  - resource: ../canonical/governance/post-concept-design-reentry.md
  - resource: ../canonical/governance/downstream-realization-obligations.md
  - resource: ../canonical/governance/downstream-authority-quarantine.md
  - resource: ../routing/downstream_candidate_qualification.json
  - resource: ../../scripts/validate_candidate_qualification.py
  - resource: ../017-methodology-closure-canonical-consolidation-completion-decision/017-F-implementation-contamination-downstream-realization-obligations-architecture-neutral-handoff-audit.md
generated: { by: openai/gpt-5.6-sol, at: 2026-09-22T04:46:00Z }
---

# Purpose

018-J determines what the preserved pre-Phase-009 downstream corpus is allowed to contribute to the fresh architecture/engineering process.

It does not decide that the historical architecture was right or wrong as a whole.

Every retained architecture/implementation candidate is qualified against:

- the closed current Concept Design;
- Q1 through Q6 from the Post-Concept-Design Re-entry contract;
- ENG-001 through ENG-018;
- ERI-01 through ERI-10;
- the Phase-016 scenario handoff;
- current authority/history/downstream separation.

The governing question is:

> What may legitimately be reused as requirement evidence, comparison input, executable fact or later implementation hypothesis, and what must first be revised, revalidated or kept inactive?

# 1. Entry baseline

018-J enters with:

~~~text
Concept Design                     CLOSED
018-I obligations                  ENG-001..018
018-I engineering risks            ERI-01..10
historical architecture owners     9
historical implementation owners   6
downstream candidate owners        15
candidate stable IDs               142
accepted architecture              NOT ESTABLISHED
implementation execution           NOT AUTHORIZED
~~~

The 15 candidate documents already carry suspension notices from 017-F.

018-J therefore qualifies rather than rewrites their historical bodies.

# 2. Qualification model

| Class | Meaning | 018-J treatment |
| --- | --- | --- |
| Q1 | conceptual/quality force worth preserving | reuse as requirement evidence, traced back to current semantic authority |
| Q2 | plausible architecture hypothesis | eligible for comparison after current-obligation revalidation |
| Q3 | concrete technology/vendor/physical hypothesis | no current authority; compare/reselect only with fresh evidence |
| Q4 | stale semantic binding | mandatory revision/removal before candidate may be adopted |
| Q5 | frozen executable non-domain substrate | preserve as fact; reuse or replace without architecture privilege |
| Q6 | obsolete/cancelled roadmap | not an active queue; do not resume |

One document may contain more than one class.

# 3. Machine-readable qualification evidence

018-J adds:

docs/routing/downstream_candidate_qualification.json

The register is explicitly:

> QUALIFICATION EVIDENCE ONLY — DOES NOT ACCEPT OR ACTIVATE ARCHITECTURE/IMPLEMENTATION

It records for all 15 candidates:

- layer;
- Q classes;
- disposition;
- continued suspended-candidate authority state;
- 018-K comparison eligibility;
- semantic-revision requirement;
- technology-revalidation requirement;
- Q5 executable-fact status;
- known stale bindings;
- relevant ENG obligations;
- relevant ERI risks;
- qualification rationale.

The register is not a semantic owner and does not replace the candidate documents.

# 4. Qualification totals

~~~text
candidate documents                 15
architecture candidates              9
implementation candidates            6

documents containing Q1              6
documents containing Q2              8
documents containing Q3             12
documents containing Q4              6
documents containing Q5              1
candidate documents containing Q6    0

historical Q6 roadmap families       2
  006-E–M
  008-F–L

adopted candidates                    0
activated candidate stable IDs        0
~~~

Q6 is represented by historical delivery queues rather than by the fifteen retained canonical candidate owners.

# 5. Architecture candidate qualification

## 5.1 Architectural Foundation

Classification:

**Q1 + Q2 — QUALIFIED COMPARISON INPUT**

Reusable forces include canonical semantics constraining architecture, authoritative confirmation at authoritative boundaries, local/projection state remaining non-authoritative, retry preserving logical identity, disclosure/security crossing presentation boundaries, and freshness/uncertainty remaining representable.

Disposition:

- retain for 018-K comparison;
- trace reusable forces to current semantic/ENG owners;
- revalidate topology/vendor examples;
- do not reactivate ARCH-* IDs as current architecture.

## 5.2 Application Boundaries

Classification:

**Q2 + Q4 — QUALIFIED AFTER REVISION**

Potentially useful ideas include bounded ownership, public owner interfaces, coordination above owners, projection separation and acyclic dependency intent.

Material stale bindings include Judging Encounter, Official Outcome Revision and module boundaries derived from older semantic ownership.

Disposition:

- eligible for 018-K only after the stale semantic map is replaced with current Concept/owner structure;
- modular-monolith and module topology remain hypotheses.

## 5.3 Data / Persistence

Classification:

**Q2 + Q3 — QUALIFIED COMPARISON INPUT**

Potentially useful ideas include current/history structural distinction, retained versions/Provenance, non-authoritative projections, reconstructible derived state and owner-bound persistence concepts.

Unaccepted choices include PostgreSQL compatibility, RDS, one logical authority database, outbox specifics and physical schema ownership.

Disposition:

- retain for comparison;
- all storage/technology choices require fresh evidence.

## 5.4 Identity / Access / Session

Classification:

**Q1 + Q2 + Q3 — QUALIFIED COMPARISON INPUT**

Strong alignment remains with ENG-004:

~~~text
authentication != Identity
Identity != Participation
Participation != Access
session != authority
technical administration != Competition authority
~~~

Unaccepted choices include provider/session topology and Cognito/AWS bindings.

Disposition:

- retain semantic/quality reasoning;
- compare provider/session alternatives in 018-K;
- no provider is preselected.

## 5.5 Commands / API / Concurrency

Classification:

**Q1 + Q2 + Q4 — QUALIFIED AFTER REVISION**

Useful forces include command/query authority separation, current-state validation, retry/idempotency, unknown-result handling and projection-freshness distinction.

Stale binding:

- Official Outcome Revision.

Unaccepted physical defaults include fixed HTTPS/JSON style, transaction defaults and concurrency strategy.

Disposition:

- revise stale semantic binding before architecture adoption;
- compare transaction/API/concurrency mechanisms afresh.

## 5.6 Synchronization / Recovery

Classification:

**Q1 + Q2 + Q3 + Q4 — QUALIFIED AFTER REVISION**

Useful forces include non-authoritative local Drafts, current-state-aware reconciliation, preserved uncertainty, multi-device convergence on one logical Scorecard, and paper/electronic convergence on one logical evaluation.

Revalidation is required for IndexedDB, local synchronization topology, older Encounter-era grouping assumptions and exact online-authority requirements.

Disposition:

- high-value candidate after semantic reconciliation;
- preserve ENG-005/007/008/012/014 pressure.

## 5.7 External Representation

Classification:

**Q1 + Q2 + Q3 — QUALIFIED COMPARISON INPUT**

Useful forces include artifact source basis, source/Export/Publication separation, complete-surface disclosure, immutable historical artifacts, successor/withdrawal semantics and end-to-end provenance.

Physical object/blob storage and delivery mechanisms remain open.

Disposition:

- retain for 018-K comparison;
- choose artifact/storage/transport topology later.

## 5.8 Front-End Interaction

Classification:

**Q2 + Q3 + Q4 — QUALIFIED AFTER REVISION**

Useful principles include client cache/local state not becoming authority, high-consequence actions not being optimistically final, disclosure/context changes partitioning client state, accessible semantic parity and recovery/conflict UI preserving evidence.

However:

- Phase-013 Experience is current interaction authority;
- React, Router, Query and IndexedDB choices are Q3 hypotheses;
- older mapping assumptions cannot override current Experience owners.

Disposition:

- revise against current Experience before architecture adoption;
- frontend framework remains open.

## 5.9 AWS Runtime / Operations

Classification:

**Q3 — QUALIFIED VENDOR HYPOTHESIS**

The document represents a coherent AWS-specific realization including ECS/Fargate, RDS, Cognito, S3, SQS, IAM, CloudFront and regional recovery.

Current Concept Design requires none of those vendors.

Disposition:

- preserve as one concrete provider/runtime option for comparison;
- do not treat prior internal coherence or historical acceptance as current selection evidence;
- 018-K must evaluate quality, security, operations, cost and reversibility against viable alternatives or explicitly justify a constrained alternative set.

# 6. Implementation candidate qualification

Implementation candidates are not architecture-selection authority.

Their primary use begins after architecture alignment.

## 6.1 Implementation Foundation

Classification:

**Q3 + Q4 — QUALIFIED IMPLEMENTATION HYPOTHESIS**

Reusable ideas include reproducible dependencies, explicit schemas, layered scanning, PR quality gates, merge/deploy separation and evidence closure.

Concrete selections include TypeScript/Node, Fastify, Kysely, PostgreSQL, pnpm and OpenTofu.

Stale execution/semantic references include Official Outcome Revision and historical 008-L / Phase-009 gates.

Disposition:

- preserve as later implementation-planning evidence;
- do not use as 018-K architecture selection authority;
- stale bindings/gates must be removed before any current implementation contract derives from it.

## 6.2 Verification Strategy

Classification:

**Q1 + Q3 — QUALIFIED VERIFICATION INPUT**

High-value reusable material includes evidence subordinate to product meaning, smallest sufficient evidence layer, deterministic fixtures, consequence-specific retry/conflict/uncertainty cases, security/accessibility behavior evidence, flaky-test discipline and synthetic/privacy-minimized fixtures.

Framework/service bindings remain hypotheses.

Disposition:

- carry principles forward into 018-L;
- derive actual framework/test topology after architecture selection;
- preserve ENG-014/015/016.

## 6.3 Source Topology

Classification:

**Q3 — QUALIFIED IMPLEMENTATION HYPOTHESIS**

Package/workspace boundaries are physical choices.

Disposition:

- do not infer source packages from Concept families;
- use only after 018-K architecture has established actual ownership/dependency decisions;
- prior package layout has no current privilege.

## 6.4 Runtime / Delivery Bootstrap

Classification:

**Q3 + Q5 — FACT ONLY**

The retained Node/pnpm/TypeScript/API/worker/web/PostgreSQL/OpenTofu scaffold is a real executable repository fact.

Disposition:

~~~text
may retain
may partially reuse
may replace
must not constrain architecture
must not become domain implementation by inertia
~~~

It is excluded from 018-K architecture comparison as an adopted candidate.

Its practical reuse can be considered after architecture decisions.

## 6.5 Persistence / History / Projection Implementation Plan

Classification:

**Q3 + Q4 — QUALIFIED AFTER REVISION**

Potentially reusable physical patterns include version/history/provenance/outbox/projection/migration techniques.

Blocking issues include PostgreSQL-specific assumptions, Official Outcome Revision, obsolete 008-L execution references and physical ownership choices made before current Concept completion.

Disposition:

- not activatable unchanged;
- later implementation planning may reuse selected patterns only after architecture alignment and semantic revision.

## 6.6 Identity / Authentication / Access / Session Implementation Plan

Classification:

**Q3 — QUALIFIED IMPLEMENTATION HYPOTHESIS**

It contains detailed Cognito/OIDC/session/PostgreSQL realization ideas.

Disposition:

- preserve for later implementation comparison;
- current Identity/Participation/Access semantics constrain it;
- Cognito, database model and session mechanics are not currently selected.

# 7. Q6 roadmap qualification

Q6 applies to the historical queues:

~~~text
006-E through 006-M
008-F through 008-L
~~~

Decision:

**OBSOLETE/CANCELLED AS ACTIVE ROADMAPS.**

They remain historical evidence only.

018-K and 018-L must not resume them or use their sequence as the default new delivery plan.

A fresh delivery decomposition will be derived from the newly selected architecture.

# 8. Stale-semantic binding register

Six candidate documents require explicit semantic revision before adoption or current downstream reuse:

| Candidate | Material stale binding |
| --- | --- |
| application-boundaries | Judging Encounter / Official Outcome Revision-era module mapping |
| commands-api-concurrency | Official Outcome Revision |
| synchronization-recovery | Encounter-era grouping assumptions |
| frontend-interaction | pre-Phase-013 interaction/mapping assumptions |
| implementation-foundation | Official Outcome Revision + old execution gates |
| persistence-history-projection | Official Outcome Revision + old execution gate |

Other implementation documents may contain historical gate prose, but their qualified use is already implementation-hypothesis/fact/verification-only and does not make those gates current.

# 9. Technology-hypothesis register

The preserved corpus contains concrete choices including PostgreSQL/RDS, AWS, Cognito, React, Fastify, TypeScript, pnpm, OpenTofu, IndexedDB, transactional outbox, fixed package topology and fixed browser/API transport patterns.

018-J decision:

> All remain hypotheses or frozen executable facts. None is adopted by Phase 018-J.

Existing code is evidence of reuse cost/compatibility, not justification by itself.

# 10. Candidate-to-risk reconciliation

## ERI-02 — historical candidate mistaken for accepted architecture

Status after 018-J:

**CONTROLLED BY MACHINE-READABLE QUALIFICATION.**

Every one of the 15 candidate documents is registered as suspended-candidate, and adopted count must remain zero.

## ERI-04 — stale semantic bindings survive reuse

Status:

**EXPLICITLY IDENTIFIED — NOT YET REPAIRED INTO NEW ARCHITECTURE.**

Q4 candidates are barred from unchanged adoption.

Actual candidate revision belongs to 018-K or the accepted architecture work that follows.

## ERI-09 — cross-owner coupling / derived authority leakage

Status:

**ACTIVE ARCHITECTURE EVALUATION RISK.**

Candidate boundary/data/API/sync/frontend patterns may help or worsen it.

018-K must evaluate this explicitly.

# 11. Conformance protection

018-J adds:

scripts/validate_candidate_qualification.py

It verifies:

- the register covers exactly the 15 architecture/implementation candidate owners;
- each owner remains downstream-candidate;
- only Q1–Q6 classifications are used;
- every record has a valid disposition;
- Q4 requires explicit semantic revision;
- Q5 requires executable-fact treatment;
- ENG references resolve as current authority;
- ERI references are well-formed;
- register summary counts match the records;
- adopted count remains zero.

The integrated conformance runner includes this validator.

# 12. Negative control

The Phase-018 conformance suite now includes a seventh mutation guard.

It deliberately changes the downstream candidate qualification adopted count from 0 to 1 and requires candidate qualification validation to fail.

This protects against a future routing/editing error silently converting historical qualification into architecture activation.

# 13. Initial qualification validation issue

The first integrated run after adding the register failed:

> Knowledge Validation run 35688060293 — FAIL

The substantive records were valid, but the summary header incorrectly stated:

~~~text
Q2 documents   7
Q3 documents  10
~~~

while deterministic counting of the records produced:

~~~text
Q2 documents   8
Q3 documents  12
~~~

The summary was corrected; no candidate classification or disposition changed.

# 14. Passing validation evidence

Corrected mechanics head:

> a6939176438a680b82557aced677c64d98b83d99

Knowledge Validation run:

> 35688092905 — SUCCESS

Evidence:

~~~text
Markdown files                         359
frontmatter blocks                     259
stable rule anchors                    294
knowledge errors                         0
knowledge warnings                       0

owner inventory                        PASS — 109 paths
stable-reference index                 PASS — 294 IDs
context budgets                        PASS — 0 hard errors
portable workflows/adapters            PASS
status mirrors                         PASS — 018-A..I COMPLETE / 018-J NEXT
candidate qualification                PASS — 15 candidates
negative controls                      PASS — 7 mutations
repository configuration conformance   PASS
~~~

# 15. 018-K input set

018-K may now consume the architecture-candidate portion of the register without opening all historical implementation material by default.

Architecture comparison set:

~~~text
Architectural Foundation            QUALIFIED COMPARISON INPUT
Application Boundaries              QUALIFIED AFTER REVISION
Data / Persistence                  QUALIFIED COMPARISON INPUT
Identity / Access / Session         QUALIFIED COMPARISON INPUT
Commands / API / Concurrency        QUALIFIED AFTER REVISION
Synchronization / Recovery          QUALIFIED AFTER REVISION
External Representation             QUALIFIED COMPARISON INPUT
Front-End Interaction               QUALIFIED AFTER REVISION
AWS Runtime / Operations            QUALIFIED VENDOR HYPOTHESIS
~~~

Implementation candidates remain downstream planning evidence, not architecture authority.

# 16. What 018-J did not decide

018-J did not decide:

- modular monolith versus alternative topology;
- PostgreSQL versus another persistence technology;
- AWS versus another provider/runtime;
- Cognito versus another identity provider;
- React versus another frontend architecture;
- REST/JSON versus another application interface;
- outbox versus another propagation mechanism;
- IndexedDB versus another offline continuity mechanism;
- whether the 006-D scaffold should be retained;
- implementation package order;
- implementation execution authorization.

Those decisions belong downstream.

# 17. Gate evaluation

| Phase-018 gate | 018-J result |
| --- | --- |
| P18-G1 semantic preservation | PASS |
| P18-G2 current/history integrity | PASS |
| P18-G3 documentation economy | PASS — one qualification register, historical bodies preserved |
| P18-G5 deterministic routing | PASS |
| P18-G6 human-directed authority | PASS |
| P18-G7 context proportionality | PASS — 018-K can load qualified architecture candidates selectively |
| P18-G8 conformance proportionality | PASS |
| P18-G9 status/reference integrity | PASS |
| P18-G10 architecture re-entry integrity | PASS |
| P18-G11 downstream obligation/risk sufficiency | PASS |
| P18-G12 execution boundary | PASS |

# 18. Exit decision

**018-J — COMPLETE — PASS.**

At exit:

~~~text
historical candidate owners            15 / 15 QUALIFIED
architecture candidates                 9 / 9 QUALIFIED
implementation candidates               6 / 6 QUALIFIED
Q4 stale candidates                     6 IDENTIFIED
Q5 frozen executable candidate          1
Q6 active historical roadmaps           0
adopted candidates                      0
accepted architecture                   NOT ESTABLISHED
implementation program                  NOT ACCEPTED
domain implementation                   NOT STARTED
execution authorization                 NOT GRANTED
~~~

The next authorized work is:

> **018-K — Architecture Decision Questions, Constraints, Evaluation Evidence & Re-entry Decomposition**

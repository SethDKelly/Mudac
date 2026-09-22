---
type: Phase Qualification
title: 018-K — Architecture Decision Questions, Constraints, Evaluation Evidence & Re-entry Decomposition
description: Defines the fresh pre-selection architecture decision framework, ten architecture question families, current semantic and ENG constraints, evidence dimensions, dependency graph, historical-candidate handling rules, architecture-probe boundary, explicit acceptance mechanics, and a proposed 019-A through 019-L re-entry program without selecting architecture or authorizing implementation.
status: stable
tags: [phase-018, architecture, reentry, decisions, constraints, evidence, alternatives, decomposition]
sources:
  - resource: 018-I-downstream-realization-obligation-carry-forward-engineering-risk-reconciliation.md
  - resource: 018-J-historical-architecture-implementation-candidate-qualification-q1-q6.md
  - resource: ../canonical/governance/architecture-reentry-evaluation.md
  - resource: ../canonical/governance/downstream-realization-obligations.md
  - resource: ../canonical/governance/post-concept-design-reentry.md
  - resource: ../routing/architecture_reentry_plan.json
  - resource: ../routing/downstream_candidate_qualification.json
  - resource: ../../scripts/validate_architecture_reentry_plan.py
generated: { by: openai/gpt-5.6-sol, at: 2026-09-22T05:07:00Z }
---

# Purpose

018-K defines the architecture work that must occur after Phase 018 without performing that architecture work prematurely.

The phase converts the qualified candidate corpus and ENG obligations into a decision program:

~~~text
closed Concept Design
        ↓
current ENG obligations
        ↓
qualified candidate evidence
        ↓
explicit architecture questions
        ↓
evidence and alternatives
        ↓
dependency-safe architecture re-entry
        ↓
accepted architecture
        ↓
implementation planning
~~~

018-K owns the question/evidence framework.

It does not own the eventual answers.

# 1. Entry state

~~~text
Concept Design                       CLOSED
durable realization obligations      ENG-001..018
historical candidates                15 / 15 QUALIFIED
architecture candidates               9 / 9 QUALIFIED
implementation candidates             6 / 6 QUALIFIED
adopted candidates                     0
accepted architecture                 NOT ESTABLISHED
implementation execution              NOT AUTHORIZED
~~~

The Q1–Q6 register from 018-J is the only historical-candidate input used by default.

# 2. Exit decision

**018-K — COMPLETE — PASS — PRE-SELECTION ARCHITECTURE RE-ENTRY PROGRAM DEFINED.**

At exit:

~~~text
architecture evaluation contract      ACTIVE — ARE-001..012
architecture question families        10
selected architecture questions        0
accepted architecture                 NOT ESTABLISHED
historical candidates                 STILL SUSPENDED
proposed re-entry phase               019-A..019-L
019 authorization                     NOT GRANTED BY 018-K ALONE
implementation execution              NOT AUTHORIZED
~~~

# 3. Current architecture-evaluation owner

018-K adds:

> docs/canonical/governance/architecture-reentry-evaluation.md

The owner defines ARE-001 through ARE-012.

Those rules establish that:

- Phase-018 planning cannot select architecture;
- current semantic authority and ENG obligations are hard constraints;
- each architecture question has scope, dependencies and deferrals;
- material decisions require credible alternatives;
- Q4 candidate material cannot be adopted unchanged;
- all decisions use a common evidence envelope;
- evidence strength and uncertainty remain calibrated;
- the decision graph is dependency-safe;
- accepted decisions require explicit rationale and evidence;
- architecture authority is created only through explicit acceptance;
- technical probes are separately bounded evidence activities;
- architecture re-entry ends before implementation execution begins.

# 4. Machine-readable pre-selection plan

018-K adds:

> docs/routing/architecture_reentry_plan.json

The plan is explicitly marked:

> PRE-SELECTION ARCHITECTURE PLANNING EVIDENCE ONLY — DOES NOT SELECT OR ACCEPT ARCHITECTURE

Current state:

~~~text
framework_state                    PRE_SELECTION
question_count                     10
selected_question_count             0
accepted_architecture_established   false
implementation_execution_authorized false
~~~

# 5. Architecture question set

## ADQ-001 — Drivers, quality attributes, workload assumptions and trust boundaries

Purpose:

Establish the decision basis used by all later architecture choices.

This includes:

- live-event workload and failure shape;
- authority and disclosure boundaries;
- availability and recovery expectations;
- accessibility and degraded-operation obligations;
- operational and cost constraints;
- reversibility expectations;
- evidence thresholds.

This is a foundation question, not a technology decision.

Historical input:

- Architectural Foundation — qualified comparison input.

## ADQ-002 — Application ownership, decomposition and dependency topology

Question:

How should current semantic ownership map into application boundaries, coordination boundaries and evolution/deployment seams?

Historical input:

- Application Boundaries — revision required before comparison.

Credible alternative classes include:

- ownership-preserving modular monolith;
- simpler ownership-preserving monolith/package topology;
- selectively distributed services where evidence justifies operational cost.

The historical module map is not reused unchanged.

## ADQ-003 — Authoritative persistence, history, Provenance and projections

Question:

What durable architecture best preserves current/history separation, correction lineage, Provenance, reconstructible derived state, migration and recovery?

Historical input:

- Data/Persistence architecture — comparison input.

Alternative classes include relational authority-store approaches and other hybrid/log-oriented approaches only where the current history/query obligations justify them.

PostgreSQL and RDS remain candidates, not decisions.

## ADQ-004 — Identity, authentication, Participation, Access and sessions

Question:

How should authentication, provider linkage, first-party/session continuity, reverification, compromised-device response and current Access enforcement be realized while MUDAC retains semantic authority?

Historical input:

- Identity/Access/Session architecture — comparison input.

No identity provider is selected by 018-K.

## ADQ-005 — Interface, command/query, transaction, concurrency, retry and idempotency

Question:

How should application interfaces and transaction/concurrency behavior preserve logical action identity, current-state preconditions, stale-intent rejection, retries, partial results and unknown outcomes?

Historical input:

- Commands/API/Concurrency — revision required before comparison.

The old Official Outcome Revision binding must not survive into a new decision.

## ADQ-006 — Offline Draft, multi-device, degraded and paper recovery

Question:

How much digital offline capability is justified, and how does non-authoritative local work reconcile safely to current authority?

Historical input:

- Synchronization/Recovery — revision required before comparison.

Alternative classes deliberately include:

- bounded revision-aware local Draft persistence;
- minimal digital offline continuity plus paper fallback;
- richer local-first Draft synchronization only where conflict semantics remain safely bounded.

This avoids assuming IndexedDB or rich offline sync is required merely because it was previously designed.

## ADQ-007 — Artifact, Export, Publication and external delivery

Question:

How should representation generation, retained artifacts, Publication and external delivery preserve exact source basis, currentness, disclosure and historical fidelity?

Historical input:

- External Representation architecture — comparison input.

The object-storage provider remains open.

## ADQ-008 — Browser/client state, navigation, accessibility and degraded interaction

Question:

What browser architecture best satisfies current Phase-013 Experience authority, phone-primary judging, organizer workflows, contextual disclosure, accessibility, recovery and bounded client state?

Historical input:

- Front-End Interaction — revision required before comparison.

React and its historical supporting libraries remain hypotheses.

## ADQ-009 — Runtime platform, deployment, availability, observability and disaster recovery

Question:

What runtime/platform architecture meets the actual event continuity, security, restore/recovery, staffing, cost and scaling needs?

Historical input:

- AWS Runtime/Operations — comparison input as a vendor hypothesis.

At minimum the later decision must compare the historical AWS realization against credible alternative runtime classes or explicitly justify why the feasible set is constrained.

AWS is not selected by 018-K.

## ADQ-010 — Whole-architecture reconciliation

Purpose:

Reconcile the individually selected architecture decisions as one system.

Required replay includes:

- all Phase-016 downstream scenario seeds;
- cross-owner coupling;
- derived-authority leakage;
- security/disclosure;
- failure propagation;
- recovery composition;
- accessibility/degraded parity;
- performance and workload fit;
- cost/operability;
- reversibility and migration;
- residual risk.

Architecture acceptance occurs only after this reconciliation succeeds.

# 6. Decision dependency graph

The pre-selection graph is:

~~~text
ADQ-001 drivers
   ↓
ADQ-002 application boundaries
   ├───────────────┐
   ↓               ↓
ADQ-003 data       ADQ-004 identity
   └──────┬────────┘
          ↓
ADQ-005 interfaces / transactions / concurrency
        ↙   ↓   ↘
ADQ-006   ADQ-007
offline   representation
    ↘       ↙
      ADQ-008 browser/client
            ↓
      ADQ-009 runtime/platform
            ↓
      ADQ-010 whole-system reconciliation
~~~

The machine validator checks that the actual dependency graph is acyclic.

The diagram is explanatory; the JSON plan is the exact dependency source.

# 7. Common evidence envelope

Every material architecture choice is evaluated proportionately across:

1. semantic and authority fit;
2. cross-owner coupling and derived-authority risk;
3. failure, retry, uncertainty and recovery;
4. security, privacy and disclosure;
5. accessibility and degraded semantic parity;
6. operational complexity, availability and observability;
7. workload, performance and scaling fit;
8. cost and organizational operability;
9. reversibility, migration and lock-in;
10. Phase-016 scenario impact;
11. compatibility/reuse cost of existing substrate as a secondary concern.

No single dimension automatically determines the answer.

Existing code therefore appears only as cost/compatibility evidence, never as architecture authority.

# 8. Alternative-comparison rule

Material decisions require at least two credible alternative classes unless current constraints genuinely eliminate all but one feasible class.

A later decision may narrow the feasible set, but it must record the reason.

The historical candidate is permitted to compete.

It receives no chronology bonus.

# 9. Q4 repair boundary

The following architecture candidates enter later comparison only after stale semantics are removed or translated to current authority:

- Application Boundaries;
- Commands/API/Concurrency;
- Synchronization/Recovery;
- Front-End Interaction.

Historical implementation Q4 material remains implementation-level evidence and is not part of the architecture comparison set.

Repairing a Q4 candidate makes it admissible.

It does not make it preferred.

# 10. Architecture probe boundary

018-K does not authorize executable architecture probes.

The future architecture phase may explicitly authorize a disposable probe where documentation or vendor evidence cannot answer a material question.

A probe must state:

- the question;
- scope;
- evidence target;
- what conclusion the probe can and cannot support;
- retention/disposal behavior.

A successful probe cannot silently become production domain implementation.

# 11. Acceptance mechanics

A later accepted architecture decision must record:

- question and scope;
- current owner/ENG constraints;
- considered alternatives;
- evidence and tradeoffs;
- affected scenarios and ERI risks;
- selected option;
- rejected alternatives and rationale;
- migration/reversibility effects;
- residual uncertainty;
- revisit triggers;
- historical candidate supersession/retention outcome.

The architecture qualification register, the pre-selection plan and existing code cannot themselves establish acceptance.

# 12. Proposed Phase 019 decomposition

018-K defines the following future program:

> **Phase 019 — Architecture & Engineering Re-entry**

Proposed dependency-safe subphases:

| Subphase | Purpose |
| --- | --- |
| 019-A | Architecture Re-entry Start Gate, Authority, Current Baseline & Decision-Evidence Model |
| 019-B | Architecture Drivers, Quality Attributes, Workload, Trust Boundary & Constraint Qualification |
| 019-C | Application Ownership, Boundary, Coordination & Dependency Architecture |
| 019-D | Persistence, History, Provenance, Projection, Migration & Recovery Architecture |
| 019-E | Identity, Authentication, Participation, Access, Session & Technical-Authority Architecture |
| 019-F | Interface, Command/Query, Transaction, Concurrency, Retry & Idempotency Architecture |
| 019-G | Offline Draft, Multi-device, Degraded, Paper & Reconciliation Architecture |
| 019-H | Artifact, Export, Publication, External Representation & Delivery Architecture |
| 019-I | Browser/Client State, Navigation, Accessibility & Degraded Interaction Architecture |
| 019-J | Runtime Platform, Security, Deployment, Availability, Observability & Disaster Recovery Architecture |
| 019-K | Whole-Architecture Integration, Threat, Failure, Recovery, Performance, Cost & Scenario Validation |
| 019-L | Architecture Consolidation, Acceptance, Candidate Supersession & Implementation Handoff |

018-K defines this program.

It does not authorize Phase 019 by itself.

Phase-018 exit authority remains with 018-M.

# 13. Implementation-level deferral

018-K explicitly defers the following unless an architecture choice materially constrains them:

- package/workspace topology;
- test framework;
- formatting/lint stack;
- ORM/query builder;
- migration tooling;
- exact CI composition;
- implementation package sequence.

This keeps Phase 019 architecture work from becoming implementation-plan selection by another name.

018-L may define the implementation-program framework before architecture selection, but the actual implementation packages will still be populated from accepted architecture later.

# 14. Conformance protection

018-K adds:

> scripts/validate_architecture_reentry_plan.py

The validator checks:

- exactly ADQ-001 through ADQ-010 exist;
- all questions remain PLANNED in the Phase-018 pre-selection plan;
- selected options remain null;
- accepted architecture remains false;
- implementation execution authorization remains false;
- material decisions have at least two alternative classes;
- current stable constraints resolve as current authority;
- candidate inputs are qualified architecture candidates;
- Q4 candidates are explicitly marked revision-required;
- no implementation candidate enters the architecture comparison set;
- the decision graph is acyclic;
- the proposed 019-A through 019-L decomposition is complete;
- the plan explicitly denies selection/acceptance authority.

# 15. Negative control

The conformance suite now contains eight mutations.

The new 018-K mutation deliberately:

- selects an ADQ-002 alternative;
- changes its status to DECIDED;
- increments selected-question count;
- changes accepted architecture to true.

The architecture-plan validator must reject the mutated repository.

This makes accidental pre-selection mechanically visible.

# 16. Deterministic authority impact

018-K adds one current Governance owner and twelve ARE stable rules.

Current mechanics baseline:

~~~text
governed documentation paths       110
current-authority paths             87
downstream-candidate paths          15
historical adapters                  6
external references                  2

stable IDs                         306
current-authority IDs              164
downstream-candidate IDs           142
ARE IDs                             12
~~~

The candidate count and candidate-ID role are unchanged.

# 17. Validation evidence

Mechanics head before phase recording:

> 6309ceabaa44cb2c3076b107946f2f35685ba7ff

Knowledge Validation run:

> 35689372078 — **SUCCESS**

Evidence:

~~~text
Markdown files                         361
frontmatter blocks                     261
stable rule anchors                    306
knowledge errors                         0
knowledge warnings                       0

owner inventory                        PASS — 110 paths
stable-reference index                 PASS — 306 IDs
context budgets                        PASS
portable workflows/adapters            PASS
status mirrors                         PASS — 018-A..J COMPLETE / 018-K NEXT
candidate qualification                PASS — 15 candidates
architecture re-entry plan             PASS — 10 questions / 0 selected
accepted architecture                  false
negative controls                      PASS — 8 mutations
repository configuration conformance   PASS
~~~

# 18. Risk reconciliation

## ERI-02 — historical scaffold/candidate mistaken for architecture

Disposition:

**FURTHER CONTROLLED.**

Candidate qualification is now downstream input only, and architecture acceptance has a separate explicit mechanism.

## ERI-03 — architecture emerges during coding

Disposition:

**CONTROLLED BY RE-ENTRY PROGRAM DESIGN.**

The ten architecture questions and proposed Phase 019 program are now explicit before implementation.

## ERI-04 — stale semantic bindings survive reuse

Disposition:

**CONTROLLED OPEN.**

Q4 comparison requires semantic repair before adoption.

The actual repairs/decisions belong to Phase 019.

## ERI-09 — cross-owner coupling / derived authority leakage

Disposition:

**EXPLICIT ARCHITECTURE EVALUATION OBLIGATION.**

ADQ-002 and ADQ-010 require coupling and authority-leakage analysis.

## ERI-10 — implementation begins before architecture/program gates

Disposition:

**CONTROLLED.**

018-K grants neither Phase-019 authority nor implementation execution authority.

# 19. Phase-018 gate evaluation

| Gate | 018-K result |
| --- | --- |
| P18-G1 semantic preservation | PASS |
| P18-G2 current/history integrity | PASS |
| P18-G3 documentation economy | PASS — one current evaluation owner plus one machine plan |
| P18-G5 deterministic routing | PASS |
| P18-G6 human-directed authority | PASS |
| P18-G7 context proportionality | PASS |
| P18-G8 conformance proportionality | PASS |
| P18-G9 status/reference integrity | PASS |
| P18-G10 architecture re-entry integrity | **PASS** |
| P18-G11 downstream obligation/risk sufficiency | PASS |
| P18-G12 execution boundary | PASS |

# 20. Handoff to 018-L

018-L should now design the **implementation-program framework**, not implementation packages themselves.

It should define:

- implementation package/slice identity and authority;
- traceability from accepted architecture and current semantics;
- verification/evidence classes and scenario carry-forward;
- dependency-safe package sequencing rules;
- migration/rollback expectations;
- security/supply-chain/secrets/fixture/privacy gates;
- code review/merge/release evidence boundaries;
- package completion and program exit criteria;
- execution authorization boundary.

It must assume:

~~~text
architecture evaluation framework    READY
accepted architecture                NOT ESTABLISHED
actual implementation packages       NOT YET DERIVED
implementation execution             NOT AUTHORIZED
~~~

The next authorized work is:

> **018-L — Implementation Program Structure, Verification Strategy & Delivery-Gate Design**

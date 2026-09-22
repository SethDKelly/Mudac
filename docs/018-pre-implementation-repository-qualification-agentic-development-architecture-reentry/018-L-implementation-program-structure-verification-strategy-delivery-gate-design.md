---
type: Phase Qualification
title: 018-L — Implementation Program Structure, Verification Strategy & Delivery-Gate Design
description: Defines the technology-neutral implementation-program contract, package lifecycle and schema, evidence classes, Phase-016 scenario carry-forward, dependency and migration rules, supply-chain/secrets/privacy gates, review/merge/release separation, completion criteria, execution-authorization boundary and deferred post-architecture implementation start gate without creating active packages or authorizing domain implementation.
status: stable
tags: [phase-018, implementation, program, packages, verification, evidence, delivery, gates, migration, security]
sources:
  - resource: 018-K-architecture-decision-questions-constraints-evaluation-evidence-reentry-decomposition.md
  - resource: ../canonical/governance/implementation-program-delivery.md
  - resource: ../canonical/governance/architecture-reentry-evaluation.md
  - resource: ../canonical/governance/downstream-realization-obligations.md
  - resource: ../routing/implementation_program_framework.json
  - resource: ../routing/architecture_reentry_plan.json
  - resource: ../canonical/implementation/verification-strategy.md
  - resource: ../../scripts/validate_implementation_program_framework.py
generated: { by: openai/gpt-5.6-sol, at: 2026-09-22T05:20:00Z }
---

# Purpose

018-L defines how implementation will later be planned, authorized, verified and closed without deriving actual implementation packages before architecture exists.

The phase preserves the ordering:

~~~text
accepted product semantics
        ↓
accepted architecture
        ↓
implementation package derivation
        ↓
package planning
        ↓
explicit package execution authorization
        ↓
implementation + evidence
        ↓
package completion
        ↓
whole-program evidence closure
        ↓
separate release / production authority
~~~

018-L defines the program grammar and gates.

It does not instantiate the program.

# 1. Entry state

018-L enters with:

~~~text
Concept Design                       CLOSED
architecture evaluation framework    READY
architecture questions               10 PLANNED
architecture selections              0
accepted architecture                NOT ESTABLISHED
historical implementation candidates 6 QUALIFIED / SUSPENDED
active implementation packages       0
domain implementation                NOT STARTED
execution authorization              NOT GRANTED
~~~

The historical verification strategy is available only as qualified Q1/Q3 input.

# 2. Exit decision

**018-L — COMPLETE — PASS — IMPLEMENTATION PROGRAM FRAMEWORK DEFINED; PACKAGE DERIVATION DEFERRED UNTIL ACCEPTED ARCHITECTURE.**

At exit:

~~~text
implementation program contract       ACTIVE — IPG-001..016
implementation package schema         DEFINED
package lifecycle                     DEFINED
evidence classes                      E1..E7 DEFINED
delivery gates                        G0..G7 DEFINED
Phase-016 scenario seeds              15 PRESERVED
active implementation packages        0
package derivation allowed             false
implementation execution authorized   false
accepted architecture                  false
future implementation lifecycle       PHASE 020 NAMED / DECOMPOSITION DEFERRED
~~~

# 3. Current implementation-program owner

018-L adds:

> docs/canonical/governance/implementation-program-delivery.md

It defines IPG-001 through IPG-016.

The rules establish that:

- Phase 018 creates no active packages;
- packages derive only from accepted architecture and current semantics;
- package identity is durable and source-layout independent;
- every package has explicit scope and evidence obligations;
- planning, authorization, execution and completion are distinct states;
- package execution remains human-directed;
- dependencies are explicit and acyclic;
- evidence classes are calibrated;
- the smallest trustworthy evidence layer is used;
- Phase-016 scenario seeds survive into implementation evidence;
- state/migration changes require compatibility and recovery evidence;
- supply-chain/secrets/fixture/privacy controls are gates;
- review, merge, release and deployment are distinct authorities;
- completion requires evidence closure, not merely code completion;
- semantic or architecture mismatches escalate rather than being hidden;
- whole-program completion still does not imply production authority.

# 4. Machine-readable program framework

018-L adds:

> docs/routing/implementation_program_framework.json

Its authority banner is:

> PRE-ARCHITECTURE IMPLEMENTATION PROGRAM FRAMEWORK ONLY — DOES NOT CREATE PACKAGES OR AUTHORIZE EXECUTION

Current state:

~~~text
framework_state                      PRE_ARCHITECTURE
accepted_architecture_required        true
accepted_architecture_established     false
package_derivation_allowed            false
implementation_execution_authorized   false
active_package_count                  0
active_packages                       []
~~~

The implementation framework is cross-checked against the architecture re-entry plan.

# 5. Package lifecycle

The generic package lifecycle is:

~~~text
PROPOSED
  ↓
PLANNED
  ↓
READY_FOR_AUTHORIZATION
  ↓
AUTHORIZED
  ↓
IN_PROGRESS
  ↓
EVIDENCE_REVIEW
  ↓
COMPLETE
~~~

Additional states:

~~~text
BLOCKED
SUPERSEDED
CANCELLED
~~~

Only an explicit transition into AUTHORIZED permits domain implementation execution.

A package becoming COMPLETE may make another package eligible.

It does not authorize the next package.

# 6. Package schema

Every future implementation package must define:

- durable package ID;
- title and purpose;
- in-scope behavior;
- explicit exclusions;
- semantic references;
- accepted architecture references;
- ENG obligations;
- predecessor/dependency packages;
- owned implementation surfaces;
- data/schema/migration impact;
- security/privacy/disclosure impact;
- accessibility/degraded-operation impact;
- failure/recovery impact;
- required evidence classes;
- affected Phase-016 scenario seeds;
- compatibility/rollback expectations;
- residual risks.

This schema deliberately avoids assuming source folders or historical package topology.

Package identity is independent of a source path.

# 7. Package-boundary rule

Implementation packages must be derived from:

~~~text
current semantic authority
+ accepted architecture
+ engineering obligations
+ dependency/evidence structure
~~~

They are not derived mechanically from:

- one Concept = one package;
- one architecture document = one package;
- one source folder = one package;
- historical 006/008 groupings;
- the existing pnpm workspace;
- an agent-preferred coding order.

This prevents old physical structure from becoming the new delivery plan by inertia.

# 8. Evidence classes

018-L defines seven evidence classes.

| Class | Meaning | Representative evidence |
| --- | --- | --- |
| E1 | documentation/static | docs, types, lint, static analysis, generated-contract checks |
| E2 | unit/component | isolated deterministic behavior |
| E3 | integration/runtime | selected real database/provider/process boundary |
| E4 | scenario/end-to-end | consequential cross-boundary workflow |
| E5 | security/accessibility/recovery | specialized authority/disclosure/accessibility/concurrency/recovery evidence |
| E6 | operational/deployment | migrations, rollout, restore, load, observability, DR |
| E7 | production | evidence from an authorized production context |

The evidence ladder is not a universal requirement that every package use every class.

Each package selects the smallest trustworthy classes that cross its material boundaries.

A weaker class cannot be reported as a stronger one.

# 9. Historical verification strategy reconciliation

The suspended historical Verification Strategy contains useful Q1 principles that remain compatible with ENG-014/015/016, including:

- evidence subordinate to current product meaning;
- smallest sufficient evidence layer;
- deterministic fixtures;
- explicit nondeterminism seams;
- behavioral security evidence;
- accessibility evidence beyond automated scanners;
- consequential retry/conflict/uncertainty scenarios;
- synthetic/privacy-minimized test data;
- CI as revision evidence rather than production certification.

018-L promotes those principles into technology-neutral IPG rules.

It does **not** promote its concrete Q3 choices.

Therefore the following remain hypotheses until accepted architecture and package planning make them applicable:

- Vitest;
- Playwright;
- Testcontainers;
- PostgreSQL-specific integration;
- Fastify application testing;
- React testing libraries;
- AWS-specific scanners/services.

# 10. Phase-016 scenario preservation

All fifteen downstream scenarios remain in the implementation framework:

1. lost-response retry after consequential authoritative action;
2. duplicate/offline Draft convergence;
3. shared-device context handoff;
4. stale Participation/Access/session state;
5. paper/electronic capture disagreement;
6. post-finalization correction;
7. affected Outcome Declaration with the same visible winner;
8. exceptional no-result closeout;
9. stale Export after source correction;
10. withdrawn Publication while external copies remain;
11. concurrent/repeated legitimate intent;
12. partial bulk result;
13. unknown/degraded result;
14. adversarial request volume;
15. conflicting legitimate authority resolved at the natural owner.

Future package planning must map affected scenarios.

Whole-program verification must reconcile the entire applicable scenario set.

# 11. Delivery-gate model

018-L defines eight gates.

## G0 — Architecture Accepted

Purpose:

Allow implementation package derivation only when accepted current architecture exists.

Current state:

**NOT SATISFIED.**

Therefore package derivation remains blocked.

## G1 — Package Planned

Requires:

- complete package scope;
- dependencies;
- traceability;
- risks;
- evidence contract;
- migration/security impacts.

It does not authorize implementation.

## G2 — Package Authorized

This is the only implementation-program gate that grants package execution authority.

Requires:

- G1 completion;
- predecessor closure or demonstrated independence;
- explicit human/program authorization;
- no unresolved semantic or architecture blocker.

## G3 — Implementation Evidence

Requires applicable E1 through E5 package evidence.

Retries or reruns cannot erase visible initial failures.

## G4 — Compatibility / Integration

Requires relevant:

- shared-state compatibility;
- migration evidence;
- integration evidence;
- recovery evidence;
- scenario reconciliation.

## G5 — Package Complete

Requires evidence closure, current traceability/docs, residual-risk assignment and no hidden blocker.

G5 does not imply release authority.

## G6 — Release Candidate

Requires separate release authority and applicable E6 evidence.

## G7 — Production Readiness

Requires applicable E6/E7 evidence plus operational/security/accessibility/recovery and external requirements.

G7 still precedes any separately governed production action where one is required.

# 12. Data / migration discipline

Any future package changing durable state must address:

- forward migration;
- transition compatibility;
- backfill/transformation semantics;
- rollback or roll-forward-only rationale;
- recovery from partial migration;
- historical/Provenance preservation;
- destructive-data boundaries;
- migration execution authority.

Application rollback cannot assume destructive schema rollback.

018-L intentionally does not select a migration tool.

# 13. Supply-chain, secret, fixture and privacy discipline

Future package completion must use proportionate controls for:

- reproducible dependencies and generated artifacts;
- secret exclusion from source/fixtures/logs;
- synthetic fixtures by default;
- sensitive Judge/Team/Competition data minimization;
- least-authority provider credentials;
- applicable dependency/static/IaC/container/artifact scanning.

Scanner success is E1/E5 evidence only as applicable.

It does not replace behavioral security evidence.

# 14. Review / merge / release / deployment separation

018-L defines:

~~~text
package COMPLETE
  != merged
  != release candidate
  != deployed
  != production ready
~~~

The current GitHub Implementation Verification workflow remains a Q5/bootstrap fact.

Its successful operation does not mean the historical toolchain or architecture has been selected.

Actual branch/ruleset/environment enforcement must be evidenced separately before it is claimed as active policy.

# 15. Human-directed package execution

Future implementation inherits AGT governance.

Therefore:

- a human selects an authorized package;
- an agent may perform bounded A2 work inside that package after G2;
- an agent may complete supporting tests/docs/routing that are causally necessary;
- completion may name the next eligible package;
- the agent cannot autonomously start it;
- deploy/release/destructive/external actions remain A3;
- semantic or accepted-architecture changes remain A4.

This avoids turning the implementation program into an unattended agent queue.

# 16. Future implementation lifecycle

018-L reserves the name:

> **Phase 020 — Implementation Planning & Controlled Delivery**

But:

> **Phase-020 package decomposition is intentionally DEFERRED UNTIL ACCEPTED ARCHITECTURE.**

This is a deliberate result, not missing work.

A future Phase-020 start gate must first consume the exact accepted Phase-019 architecture and then:

1. confirm that architecture baseline;
2. derive implementation packages;
3. construct the package dependency graph;
4. map semantic/ENG/IPG/scenario/evidence obligations;
5. qualify useful historical Q3/Q5 implementation substrate;
6. establish supply-chain/secrets/fixture/privacy/migration baselines;
7. identify planning-ready packages;
8. explicitly decide whether any package receives G2 authorization.

A fixed 020-A through 020-N feature sequence before architecture selection would recreate the architecture-by-inertia problem Phase 018 exists to prevent.

# 17. Conformance protection

018-L adds:

> scripts/validate_implementation_program_framework.py

It checks:

- framework state remains PRE_ARCHITECTURE;
- accepted architecture remains false;
- architecture and implementation framework state agree;
- package derivation remains false;
- execution authorization remains false;
- active package count remains zero;
- active package list remains empty;
- package lifecycle is intact;
- required package schema fields remain complete;
- E1 through E7 remain defined;
- all 15 scenario seeds remain present;
- G0 through G7 remain defined;
- only G2 can grant package execution authority;
- package auto-advance remains disabled;
- migration/supply-chain/privacy boundary rules remain active;
- Phase-020 decomposition remains deferred until architecture acceptance.

# 18. Negative control

The conformance suite now contains nine mutations.

The new 018-L mutation deliberately changes the framework to:

~~~text
package_derivation_allowed            true
implementation_execution_authorized   true
active_package_count                  1
active_packages                       [IMP-001]
~~~

The implementation-program validator must reject the mutated repository.

This gives the no-implementation-before-architecture boundary executable protection.

# 19. Deterministic authority impact

018-L adds one current Governance owner and sixteen IPG stable rules.

Mechanics state:

~~~text
governed documentation paths       111
current-authority paths             88
downstream-candidate paths          15
historical adapters                  6
external references                  2

stable IDs                         322
current-authority IDs              180
downstream-candidate IDs           142
IPG IDs                             16
~~~

No historical implementation candidate became current authority.

# 20. Validation evidence

Mechanics head before phase recording:

> c14d8b2ccb4aecfe44edd01fc27743a5b8c615f2

Knowledge Validation:

> run 35690148466 — **SUCCESS**

Evidence:

~~~text
Markdown files                         363
frontmatter blocks                     263
stable rule anchors                    322
knowledge errors                         0
knowledge warnings                       0

owner inventory                        PASS — 111 paths
stable-reference index                 PASS — 322 IDs
context budgets                        PASS
portable workflows/adapters            PASS
status mirrors                         PASS — 018-A..K COMPLETE / 018-L NEXT
candidate qualification                PASS — 15 candidates
architecture re-entry plan             PASS — 10 questions / 0 selected
accepted architecture                  false
implementation program framework       PASS — 0 active packages
package derivation                     false
implementation execution               false
negative controls                      PASS — 9 mutations
repository configuration conformance   PASS
~~~

# 21. Risk reconciliation

## ERI-03 — architecture emerges opportunistically during feature coding

Disposition:

**CONTROLLED.**

No package may even be derived until accepted architecture exists.

## ERI-05 — Phase-016 scenarios lost during implementation planning

Disposition:

**CONTROLLED BY IPG-010 AND FRAMEWORK SCENARIO REGISTER.**

All fifteen scenarios are explicit package/program evidence inputs.

## ERI-06 — supply-chain/secrets/privacy-fixture/migration controls arrive late

Disposition:

**CONTROLLED BY IPG-011/012 AND G1–G5.**

The controls are package-plan and completion concerns rather than post-hoc release cleanup.

## ERI-07 — provider-agent runtime assumptions

Disposition:

**BOUNDED.**

Provider runtime evidence remains required only when materially relied upon.

## ERI-08 — static proof promoted into runtime/production proof

Disposition:

**CONTROLLED BY E1–E7 CLASSIFICATION AND IPG-008/009/013.**

## ERI-10 — implementation begins before gates are accepted

Disposition:

**MECHANICALLY CONTROLLED.**

G2 is the only package execution gate, and the current framework has no packages and no execution authority.

# 22. Phase-018 gate evaluation

| Gate | 018-L result |
| --- | --- |
| P18-G1 semantic preservation | PASS |
| P18-G2 current/history integrity | PASS |
| P18-G3 documentation economy | PASS — one current program owner plus one machine framework |
| P18-G5 deterministic routing | PASS |
| P18-G6 human-directed authority | PASS |
| P18-G7 context proportionality | PASS |
| P18-G8 conformance proportionality | PASS |
| P18-G9 status/reference integrity | PASS |
| P18-G10 architecture re-entry integrity | PASS |
| P18-G11 downstream obligation/risk sufficiency | PASS |
| P18-G12 execution boundary | **PASS** |

# 23. Handoff to 018-M

018-M should now evaluate the whole Phase-018 program rather than adding more preparation machinery.

It should:

1. re-run the repository readiness scorecard from the 018-A baseline;
2. compare original R18 risks against current controls/residuals;
3. confirm Concept Design remained closed and uncontaminated;
4. confirm historical architecture/implementation remained non-authoritative;
5. confirm the architecture plan still has zero selections;
6. confirm the implementation framework still has zero packages and no execution authority;
7. identify any residual blocker to fresh architecture re-entry;
8. decide whether Phase 019 may be authorized;
9. explicitly state what remains unauthorized after Phase-018 exit;
10. record the Phase-018 closure posture and next lifecycle authority.

The next authorized work is:

> **018-M — Pre-Implementation Residual Risk Register, Repository Scorecard Regrade & Implementation Entry Decision**

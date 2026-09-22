---
type: Governance Contract
title: Phase-019 Architecture Decision Authority & Evidence Contract
description: Governs the authorized Phase-019 architecture decision process, exact entry baseline, per-question decision authority, Q4 semantic repair, evidence and alternative requirements, bounded technical probes, individual-decision acceptance, whole-architecture acceptance, supersession, and the continuing implementation-execution boundary.
status: stable
tags: [governance, architecture, phase-019, decisions, evidence, q4, probes, acceptance, supersession]
sources:
  - resource: architecture-reentry-evaluation.md
  - resource: downstream-realization-obligations.md
  - resource: implementation-program-delivery.md
  - resource: post-concept-design-reentry.md
  - resource: ../../018-pre-implementation-repository-qualification-agentic-development-architecture-reentry/018-M-pre-implementation-residual-risk-register-repository-scorecard-regrade-implementation-entry-decision.md
  - resource: ../../routing/architecture_reentry_plan.json
  - resource: ../../routing/downstream_candidate_qualification.json
generated: { by: openai/gpt-5.6-sol, at: 2026-09-22T05:52:00Z }
---

# Purpose

Phase 019 is the first lifecycle permitted to make fresh architecture decisions after Concept Design closure.

This contract defines how those decisions become legitimate.

It supplements ARE governance with Phase-019 execution authority and evidence mechanics. It does not itself choose any architecture option.

<a id="ada-001"></a>
## ADA-001 — Phase-019 Authority Derives Only From the 018-M Exit Decision

Phase 019 exists because 018-M explicitly authorized Architecture & Engineering Re-entry.

That authority permits the selected Phase-019 subphase to perform architecture evaluation, bounded repair, evidence gathering and decision work within its declared scope.

It does not grant domain implementation execution, deployment, release or production authority.

<a id="ada-002"></a>
## ADA-002 — The Exact Phase-018 Closure Baseline Is the Phase-019 Entry Snapshot

Phase 019 begins from commit:

~~~text
526b8533395e7cbdabf567c56115f024b78a10f5
~~~

The machine decision-control record preserves the blob identities of the qualified candidate register, ENG obligations, ARE contract, IPG contract, architecture plan, implementation framework and 018-M decision at entry.

Later legitimate evolution does not rewrite the entry snapshot.

<a id="ada-003"></a>
## ADA-003 — ADQ-001 Through ADQ-010 Are the Governed Decision Graph

The ten questions defined by the Phase-018 architecture re-entry plan are the initial Phase-019 architecture decision set.

A Phase-019 subphase may refine a question's evidence or alternative set but may not silently add, remove, merge or bypass a material architecture question.

Material graph change requires explicit Phase-019 governance evidence and must preserve upstream semantic authority.

<a id="ada-004"></a>
## ADA-004 — Each Architecture Question Has a Durable Decision Record

Each ADQ maintains a record independent of a particular prose document or tool.

The record includes at least:

- question ID and title;
- owning decision subphase;
- current decision state;
- current semantic and ENG constraints;
- credible alternatives considered;
- historical candidate inputs and their qualification/repair state;
- evidence references and evidence classes;
- Phase-016 scenarios and ERI risks affected;
- selected option when one exists;
- rationale and rejected alternatives;
- reversibility and migration consequences;
- residual uncertainty and revisit triggers;
- acceptance evidence and accepting subphase.

The record is routing/evidence state, not a replacement for the canonical architecture owner created after acceptance.

<a id="ada-005"></a>
## ADA-005 — Decision State Is Explicit and Cannot Skip Acceptance Preconditions

Allowed decision progression is:

~~~text
PLANNED
  ↓
EVALUATING
  ↓
PROPOSED
  ↓
ACCEPTED
~~~

A decision may also become:

~~~text
BLOCKED
REOPENED
SUPERSEDED
~~~

A decision cannot become ACCEPTED before its owning subphase has completed the required comparison/evidence work.

No transition may be inferred from code existence or historical candidate completeness.

<a id="ada-006"></a>
## ADA-006 — Individual Accepted Decisions Do Not Establish Accepted Whole Architecture

ADQ-level acceptance means a bounded architecture decision has current downstream decision authority.

It does not set whole-architecture acceptance to true.

Whole-architecture acceptance remains reserved for 019-L after ADQ-001 through ADQ-010 are resolved and 019-K whole-system reconciliation has passed.

<a id="ada-007"></a>
## ADA-007 — Decision Evidence Must Distinguish Facts, Analysis, Probes and Runtime Proof

Evidence references are classified using the ARE evidence classes:

- DOCUMENTATION_REASONING;
- EXTERNAL_VENDOR_FACT;
- BOUNDED_TECHNICAL_PROBE;
- EXECUTABLE_INTEGRATION_EVIDENCE;
- PRODUCTION_EVIDENCE.

The decision record states what each item can support.

Reasoning cannot masquerade as runtime proof, and a probe cannot establish production readiness.

<a id="ada-008"></a>
## ADA-008 — Q4 Repair Produces a Current Comparison Translation, Not a Rewrite of History

Historical candidate documents classified Q4 remain preserved evidence.

Before such a candidate may be compared, Phase 019 creates a repair record that identifies:

- the candidate;
- stale binding(s);
- current semantic owner(s) replacing those bindings;
- portions retained as architecture hypothesis;
- portions excluded as obsolete;
- resulting revised comparison statement;
- evidence that the repair preserves current meaning.

The historical candidate is not edited to pretend it was always current.

Completion of repair makes the revised hypothesis comparison-eligible; it does not adopt it.

<a id="ada-009"></a>
## ADA-009 — Credible Alternatives Are Recorded Before Selection

For each material decision, the evaluated alternative set is explicit before acceptance.

A historical candidate may participate only according to its Q1–Q6 qualification and Q4 repair state.

Existing implementation cost, developer familiarity or scaffold compatibility may be considered only as secondary evidence and cannot substitute for semantic/quality fit.

<a id="ada-010"></a>
## ADA-010 — Technical Probes Require Explicit Bounded Authorization

A Phase-019 subphase may authorize a technical probe only when existing documentation, external/vendor facts and analysis cannot resolve a material architecture uncertainty.

Every probe authorization states:

- related ADQ;
- question being tested;
- scope and time/boundary;
- permitted repository/runtime surfaces;
- evidence target;
- prohibited domain/production use;
- retention/disposal decision.

A probe does not become accepted architecture or implementation because it succeeds.

019-A authorizes no technical probe.

<a id="ada-011"></a>
## ADA-011 — Residual Uncertainty Is Recorded With a Revisit Trigger

Architecture decisions need not fabricate evidence that cannot exist yet.

An accepted decision may carry bounded uncertainty only when the record identifies:

- what remains unknown;
- why acceptance is still justified;
- the risk owner;
- the evidence class expected later;
- the exact revisit trigger or lifecycle gate.

Unbounded ambiguity blocks acceptance.

<a id="ada-012"></a>
## ADA-012 — Whole-Architecture Acceptance Requires Complete Decision and Validation Closure

019-L may establish accepted architecture only when:

1. ADQ-001 through ADQ-009 have accepted decisions;
2. ADQ-010 whole-architecture validation has passed;
3. all blocking Q4 repairs are complete;
4. cross-decision contradictions are resolved;
5. Phase-016 scenario coverage is reconciled;
6. residual architecture risks are explicitly dispositioned;
7. historical candidate supersession/retention is explicit;
8. current architecture owner documents are created and routed.

Until those conditions hold, accepted architecture remains false.

<a id="ada-013"></a>
## ADA-013 — Accepted Decisions Are Superseded Explicitly, Never Silently Rewritten

If later Phase-019 evidence invalidates an accepted bounded decision, its record moves through REOPENED or SUPERSEDED with explicit evidence and successor linkage.

Editing the rationale or selected option in place without preserving the prior decision is prohibited.

This applies within Phase 019 and to later architecture change governance.

<a id="ada-014"></a>
## ADA-014 — Phase Progression Is Human-Directed and Dependency-Safe

Completing a Phase-019 subphase may make the next subphase eligible.

It does not authorize an agent to begin that next subphase automatically.

A downstream subphase may not finalize a decision while unresolved predecessor decisions can materially change its assumptions.

<a id="ada-015"></a>
## ADA-015 — Implementation Remains Frozen Until Whole Architecture Acceptance

Throughout Phase 019 prior to successful 019-L acceptance:

~~~text
active implementation packages      = 0
package derivation allowed          = false
implementation execution authorized = false
~~~

Architecture decision documents, Q4 repairs, evaluation matrices and authorized probes are architecture evidence, not implementation packages.

<a id="ada-016"></a>
## ADA-016 — Machine Decision Control Is Routing and Evidence State, Not Independent Semantic Authority

The Phase-019 machine control record is:

docs/routing/phase019_architecture_decision_control.json

It mirrors:

- the Phase-018 entry snapshot;
- Phase-019 subphase progression;
- ADQ decision state;
- Q4 repair state;
- bounded probe authorizations;
- whole-architecture acceptance state.

The semantic and architecture meaning remains owned by current canonical documents and accepted architecture decision records.

Generated or machine-readable state cannot create authority that the corresponding governed acceptance event did not create.

# Current Phase-019 posture

After 019-C:

~~~text
Phase 019                         ACTIVE
019-A / 019-B / 019-C             COMPLETE
019-D                             NEXT ELIGIBLE
ADQ-001 / ADQ-002                 ACCEPTED
ADQ decisions accepted            2 / 10
Q4 architecture repairs complete  1 / 4
technical probes authorized       0
accepted whole architecture       false
active implementation packages    0
implementation execution          NOT AUTHORIZED
~~~

Current accepted architecture owners are:

- docs/canonical/architecture/architecture-drivers.md (DRV-001..012);
- docs/canonical/architecture/application-ownership-boundaries.md (BND-001..012).

Q4R-001 is complete. 019-D may now evaluate ADQ-003 against the accepted driver and application-boundary baselines.

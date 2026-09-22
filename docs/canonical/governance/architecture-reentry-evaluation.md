---
type: Governance Contract
title: Architecture Re-entry Evaluation & Decision Contract
description: Defines the pre-selection architecture decision framework, hard semantic constraints, alternative-comparison rules, evidence requirements, decision dependencies, probe boundaries, acceptance mechanics, and downstream re-entry sequence used after Phase-018 qualification.
status: stable
tags: [governance, architecture, reentry, decisions, alternatives, evidence, constraints, risk, verification]
sources:
  - resource: post-concept-design-reentry.md
  - resource: downstream-realization-obligations.md
  - resource: downstream-authority-quarantine.md
  - resource: ../../routing/downstream_candidate_qualification.json
  - resource: ../../018-pre-implementation-repository-qualification-agentic-development-architecture-reentry/018-J-historical-architecture-implementation-candidate-qualification-q1-q6.md
generated: { by: openai/gpt-5.6-sol, at: 2026-09-22T04:55:00Z }
---

# Purpose

Define how MUDAC moves from qualified historical architecture evidence to a fresh accepted architecture without allowing chronology, existing code, vendor familiarity or implementation convenience to substitute for a decision.

This contract governs architecture evaluation.

It does not itself select an architecture.

<a id="are-001"></a>
## ARE-001 — Phase-018 Architecture Re-entry Planning Does Not Select Architecture

The Phase-018 architecture re-entry plan defines questions, constraints, evidence, dependencies and decision gates only.

While the plan is in pre-selection state:

- selected options remain null;
- all historical architecture owners remain downstream candidates;
- accepted architecture remains not established;
- implementation execution remains unauthorized.

<a id="are-002"></a>
## ARE-002 — Current Semantic Authority and ENG Obligations Are Hard Decision Constraints

Every architecture decision begins from current Project, Concept, Synchronization, Dependence, Experience, Invariant, Policy and Mechanism authority plus the applicable ENG obligations.

Historical architecture can provide evidence or hypotheses but cannot weaken those constraints.

If no plausible realization can satisfy the current constraints, route the contradiction through change governance rather than silently relaxing product meaning.

<a id="are-003"></a>
## ARE-003 — Architecture Questions Have Explicit Scope, Dependencies and Deferrals

Each architecture question must state:

- the decision boundary;
- the current constraints it must preserve;
- predecessor decisions whose results it depends upon;
- affected validation scenarios;
- qualified historical candidate inputs, if any;
- concerns deliberately deferred to implementation or production evidence.

This prevents architecture decisions from being hidden inside later coding choices.

<a id="are-004"></a>
## ARE-004 — Material Architecture Choices Require Credible Alternatives

A material architecture decision evaluates at least two credible alternatives unless current constraints genuinely eliminate all but one feasible class.

The historical MUDAC candidate may be one alternative.

Its prior existence, completeness or executable scaffold is not a comparative advantage by itself.

A constrained single-option evaluation must document why other classes are infeasible.

<a id="are-005"></a>
## ARE-005 — Q4 Candidate Material Is Inadmissible Unchanged

A candidate classified Q4 may inform an architecture decision only after its stale semantic binding is removed or translated to current semantic owners.

The architecture decision must evaluate the revised hypothesis, not the superseded name or ownership model.

Q4 repair is a prerequisite to adoption, not evidence for adoption.

<a id="are-006"></a>
## ARE-006 — Architecture Evaluation Uses a Common Evidence Envelope

Material decisions evaluate evidence proportionate to their scope across:

- semantic and authority fit;
- cross-owner coupling and derived-authority risk;
- failure, retry, uncertainty and recovery behavior;
- security, privacy and disclosure;
- accessibility and degraded semantic parity;
- operational complexity, availability and observability;
- workload, performance and scaling fit where material;
- cost and organizational operability where material;
- reversibility, migration and lock-in;
- impact on Phase-016 validation scenarios;
- compatibility and reuse cost of existing substrate as a secondary consideration.

No single dimension automatically wins.

<a id="are-007"></a>
## ARE-007 — Evidence Strength and Uncertainty Stay Calibrated

Architecture decisions distinguish documented reasoning, external or vendor facts, bounded technical probes, executable integration evidence and production evidence.

A decision may be accepted with explicitly bounded later evidence when the unresolved evidence cannot reasonably be obtained before implementation, provided the residual risk and revisit trigger are recorded.

Static documentation cannot be promoted into runtime proof.

<a id="are-008"></a>
## ARE-008 — The Architecture Decision Graph Is Dependency-Safe

A downstream architecture decision may not be finalized while a predecessor decision capable of materially changing its assumptions remains unresolved.

Parallel decisions are allowed when their boundaries are independent and their shared constraints are explicit.

The architecture program must end with whole-system reconciliation rather than assuming individually reasonable choices compose safely.

<a id="are-009"></a>
## ARE-009 — Accepted Architecture Decisions Require Explicit Decision Evidence

An accepted architecture decision records at minimum:

- question and scope;
- current semantic and ENG constraints;
- considered alternatives;
- evidence and tradeoffs;
- affected scenarios and risks;
- chosen option;
- rejected alternatives and why;
- reversibility and migration consequences;
- residual uncertainty and revisit triggers;
- superseded historical candidate material where applicable.

A decision is not accepted merely because a document was edited or code already exists.

<a id="are-010"></a>
## ARE-010 — Architecture Authority Is Created Only by Explicit Acceptance

The qualification register, evaluation plan, historical architecture subtree, executable scaffold and technical probes are not accepted architecture authority.

Accepted downstream architecture becomes current only through an explicit architecture-acceptance event and current architecture owner or owners that clearly supersede or disposition historical candidates.

Until then, candidate stable IDs retain downstream-candidate role.

<a id="are-011"></a>
## ARE-011 — Architecture Probes Are Separate, Bounded Evidence Activities

A later architecture phase may authorize a disposable technical probe when documentation or vendor evidence is insufficient.

A probe must have a stated question, scope, evidence target and disposal or retention rule.

A probe may not silently become production domain implementation, expand product scope, or acquire semantic authority because it works.

Phase 018 does not itself authorize such probes.

<a id="are-012"></a>
## ARE-012 — Architecture Re-entry Ends Before Implementation Execution Begins

The fresh architecture program must:

1. establish decision authority and drivers;
2. decide the material architecture questions in dependency-safe order;
3. reconcile cross-cutting security, failure, operational and scenario obligations;
4. create accepted current architecture authority;
5. explicitly supersede, retain or retire historical candidate material;
6. hand accepted architecture to implementation planning.

Implementation package execution requires a later explicit authorization.

# Decision-question register

The machine-readable pre-selection question and dependency plan is:

docs/routing/architecture_reentry_plan.json

It is planning evidence, not architecture authority.

# Required architecture decision dimensions

The architecture re-entry program must address at least:

1. drivers, quality attributes, workload assumptions and trust boundaries;
2. application ownership and decomposition and dependency topology;
3. authoritative persistence, history, Provenance and projections;
4. Identity, authentication, Participation, Access and session realization;
5. command and query interfaces, transaction, concurrency, retry and idempotency;
6. offline and local Draft, multi-device, degraded and paper recovery;
7. external representation, Artifact, Export and Publication realization;
8. browser and client state, navigation, accessibility and degraded interaction;
9. runtime and platform, deployment, availability, observability and disaster recovery;
10. whole-architecture integration, security, failure, performance, cost and reversibility reconciliation.

The exact technology selected for any dimension remains open until the downstream architecture phase records an accepted decision.

# Implementation-level deferrals

The following are not architecture selections merely because historical implementation material exists:

- exact package or workspace topology;
- exact test framework;
- code formatting or lint tooling;
- concrete ORM or query builder;
- exact migration tool;
- final CI job composition;
- implementation package sequence.

Architecture may constrain these later choices, but implementation planning derives them after architecture acceptance.

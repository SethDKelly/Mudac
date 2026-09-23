---
type: Phase Record
title: 020-H — Independent Code Review, Adversarial Review, Repair/Reopen & Exit-Gate Governance
description: "Defines independent code review, adversarial conformance review, finding/fix verification, bounded repair, completion Gatekeeper authority, immutable exit records, post-completion invalidation and explicit reopen/re-authorization semantics for autonomous implementation without granting Phase-020 execution authority."
status: stable
tags: [phase-020, review, adversarial-review, repair, reopen, gatekeeper, exit-gate, autonomous-development]
sources:
  - resource: README.md
  - resource: 020-C-cursor-codex-roles-work-isolation-context-provenance-autonomy-circuit-breakers.md
  - resource: 020-F-implementation-phase-contract-visible-criteria-evidence-classes-hidden-evaluation-architecture.md
  - resource: 020-G-ci-cd-security-supply-chain-exact-sha-verification-evidence-bundle-architecture.md
  - resource: ../canonical/governance/implementation-program-delivery.md
  - resource: ../canonical/governance/agentic-conformance.md
  - resource: ../routing/autonomous_implementation_operating_model.json
  - resource: ../routing/phase020_implementation_phase_contract.json
  - resource: ../routing/phase020_ci_supplychain_evidence_architecture.json
  - resource: ../routing/phase020_review_repair_exit_gate_governance.json
generated: { by: openai/gpt-5.6-sol, at: 2026-09-23T13:35:00-05:00 }
---

# Purpose

Define how a future Phase-021+ implementation candidate is independently reviewed, challenged, repaired, accepted, invalidated and—when necessary—reopened without allowing autonomous agents to self-certify completion or silently expand authority.

020-H closes the governance gap between 020-C role/isolation controls, 020-F visible criteria/protected verification, 020-G exact-revision evidence bundles, and future G5 package/phase completion.

The phase establishes two distinct review functions:

1. **independent code review** — does the implementation correctly and maintainably realize its declared obligations?; and
2. **adversarial conformance review** — could the candidate appear green while evading, weakening, bypassing or overfitting the actual contract?

# Entry state

~~~text
PHASE 020 ACTIVE
020-A/B/C/D/E/F/G COMPLETE
020-H NEXT ELIGIBLE / USER AUTHORIZED

proposed packages                 15
G1-ready packages                 0
G2-authorized packages            0
active implementation packages    0
implementation execution          NOT AUTHORIZED
release authority                 NOT GRANTED
production authority              NOT GRANTED
~~~

Exact 020-H planning baseline:

> ca89fbd80867c4dc4909eabdf9bd23f13613937a

# Decision

**020-H — ACCEPT INDEPENDENT DUAL-PASS REVIEW, BOUNDED REPAIR AND IMMUTABLE EXIT/REOPEN GOVERNANCE.**

The governing rules are:

> **The author does not certify the author's own implementation.**

> **Repair may correct an authorized implementation; repair may not enlarge the authorization.**

> **Completion is an immutable evidence decision. Later invalidation creates a reopen obligation, not retroactive permission to resume coding.**

# Review pipeline

~~~text
IMPLEMENTATION COMPLETE / REVIEW REQUESTED
                  |
                  v
        PUBLIC / PROTECTED EVIDENCE
                  |
          +-------+-------+
          |               |
          v               v
 INDEPENDENT CODE     ADVERSARIAL
      REVIEW           CONFORMANCE
          |               |
          +-------+-------+
                  |
                  v
             GATEKEEPER
          /       |       \
       PASS    REPAIR    BLOCK
        |         |        |
        v         v        v
     COMPLETE   new SHA   escalation
                  |
                  +----> evidence/review rerun
~~~

The Gatekeeper receives evidence. It does not replace the Reviewer or Verifier.

# Candidate freeze and review record

Review begins only against an exact frozen candidate SHA/tree.

The review record includes phase/package ID, candidate SHA/tree, base/integration SHA where applicable, diff identity, criteria/evidence-contract versions, evidence-bundle reference, reviewer identity/run, independently resolved authority references, findings and final review outcome.

Any source/configuration change that changes the candidate tree invalidates prior review approval for affected surfaces. Mechanical metadata changes may reuse evidence only under the 020-G content-equivalence rule.

# Independent code review

The code review examines at least:

- semantic and architecture fidelity;
- state-transition and authority correctness;
- data/history/Provenance behavior;
- transaction, concurrency, idempotency and uncertainty handling;
- security/privacy/disclosure boundaries;
- accessibility/degraded behavior where applicable;
- migration/compatibility/recovery;
- failure behavior and observability;
- dependency/provider boundaries;
- unnecessary coupling or duplicate authority;
- maintainability and comprehensibility;
- test/evidence quality and material-boundary fit;
- scope discipline and absence of unrelated work.

Review is not a style contest. Cosmetic preferences are not blockers unless a visible project standard makes them required.

# Reviewer independence

A qualifying Reviewer is an independent review run/context and cannot be the same authoring run that produced the candidate.

Reviewer context begins from:

1. phase/package contract;
2. exact base/head diff;
3. current authority resolved independently;
4. evidence bundle/raw evidence.

The implementer summary may be consulted only as supplemental rationale.

Provider diversity remains preferred, not mandatory.

Reviewer default authority is read-only. If a Reviewer edits the candidate, that Reviewer becomes an **Implementer for the affected revision**; the new candidate must receive another independent review.

# Adversarial conformance review

Adversarial review assumes the candidate may have optimized for obvious tests instead of the actual contract.

It challenges at least:

## Contract evasion

- fixture/example overfitting;
- evaluator/test identity hard-coding;
- test-only domain semantics;
- semantic bypass configuration;
- authority-redefining hidden defaults;
- missing negative-space behavior.

## Authority erosion

- technical privilege treated as MUDAC authority;
- cross-owner writes or leaked natural-owner responsibility;
- test-control/admin paths acquiring product authority;
- provider behavior treated as semantic truth;
- client/projection behavior becoming authoritative.

## Evidence gaming

- weakened/disabled tests or scanners;
- retry-until-green;
- stale evidence from another SHA;
- evidence-class overclaim;
- fixture seeding counted as command behavior;
- hidden failures or indefinite quarantine.

## Security/privacy escape

- credential exposure;
- untrusted code receiving privileged tokens;
- sensitive data in logs/evidence;
- synthetic actors receiving semantic bypass;
- unsafe shell/cloud/database/navigation escape hatches.

## Complexity/scope gaming

- unnecessary abstraction that evades ownership boundaries;
- duplicated semantic rules;
- speculative out-of-scope framework work;
- "generic" infrastructure that expands future authority;
- dead compatibility paths preserving superseded architecture.

Adversarial review derives challenges only from visible authority and accepted architecture. It may not invent hidden product requirements.

# Adversarial execution boundary

Adversarial review may inspect source/configuration, create bounded local/non-production tests, use approved test-control/protected-evaluator interfaces, and exercise malformed/stale/concurrent/repeated/partial/denied cases within the visible contract.

It may not target production, exfiltrate hidden probes, use unauthorized secrets, perform destructive external actions, modify candidate source while retaining reviewer status, or convert a preference into a mandatory acceptance rule.

# Finding model

Every finding has a stable ID and records:

~~~text
finding_id
review_type
candidate_sha
category
severity
blocking
statement
authority_refs
affected_criteria
evidence_refs
recommended_repair_direction
status
disposition_rationale
~~~

Severities are **CRITICAL**, **MAJOR**, **MINOR**, and **NOTE**.

Blocking status is explicit and must be justified against visible authority. A required-criterion defect cannot be made non-blocking merely by lowering severity.

A review with any open blocking finding cannot report PASS.

Finding dispositions are:

- RESOLVED;
- ACCEPTED_RISK_WITH_AUTHORITY;
- NOT_APPLICABLE_WITH_APPROVED_RATIONALE;
- SUPERSEDED_BY_NEW_FINDING.

Comment-resolution UI, elapsed time, or implementer assertion alone cannot close a blocking finding. Risk acceptance requires an actor with actual risk-acceptance authority.

# Review outcomes

Each review pass resolves to exactly one of:

~~~text
PASS
CHANGES_REQUIRED
BLOCKED
INCONCLUSIVE
~~~

Only PASS is successful for exit.

CHANGES_REQUIRED routes to repair. BLOCKED routes to escalation/re-entry. INCONCLUSIVE fails closed until trustworthy review exists.

# Repair loop

Before G5, a failed review/evidence result may return to implementation under the **existing G2 envelope** only when repair:

- remains inside original authorized scope;
- adds no undeclared package/work unit;
- needs no semantic/architecture change;
- needs no unplanned privilege;
- respects serialized surfaces;
- preserves success criteria;
- preserves failure/retry history.

Repair creates a new candidate SHA. Affected verification and review rerun against that SHA.

Review diagnostics identify the violated obligation and repair boundary without unnecessarily prescribing a secret answer.

# Repair budget

Every implementation phase/package defines a bounded repair budget before G2.

The budget may use repair-cycle count, elapsed review window, compute/cost envelope, repeated-identical-failure threshold, or a declared combination.

020-H does not choose universal numeric values.

Budget exhaustion yields BLOCKED or explicit human/program extension; it never lowers acceptance criteria.

# Repair escalation

Ordinary repair stops and escalates when:

- scope expansion is required;
- a new package/dependency is required;
- semantics/architecture appear contradictory;
- the same mandatory failure repeats beyond the declared threshold;
- evidence remains nondeterministic;
- migration/recovery safety cannot be established;
- security repair changes trust/authority architecture;
- production/unplanned destructive access is required;
- serialized-surface collision cannot be resolved.

The existing G2 envelope remains unchanged during escalation.

# Gatekeeper

The Gatekeeper is an **exit decision integrator**, not a super-reviewer.

It verifies:

- exact candidate SHA/tree matches mandatory evidence;
- visible criteria and evidence obligations are satisfied;
- public CI is clean;
- protected evaluation is clean where declared;
- independent code review is PASS;
- adversarial conformance review is PASS;
- no blocking finding remains open;
- exception/risk acceptance has valid authority;
- traceability/docs are current;
- failure/retry history remains visible;
- residual risks have owners/revisit gates;
- no circuit breaker remains unresolved.

The Gatekeeper cannot edit source, waive mandatory criteria, convert FAIL to PASS, fabricate evidence, grant next-phase G2, merge, or deploy.

The Gatekeeper may be a pre-authorized agent or deterministic automation, but for a candidate it cannot be the same authoring run as an Implementer.

# Exit decisions

The Gatekeeper emits exactly one:

- **COMPLETE**;
- **REPAIR_REQUIRED**;
- **BLOCKED**;
- **INCONCLUSIVE**.

Only COMPLETE creates G5.

The other outcomes never authorize the next package.

# Immutable G5 completion record

A G5 completion record is immutable and content-addressed.

It records package/phase ID, exact candidate SHA/tree, evidence-bundle digest, code/adversarial review references, Gatekeeper identity/run, completion timestamp, residual-risk references and:

> **NEXT_ELIGIBLE_NOT_AUTHORIZED**

Corrections never rewrite historical completion evidence.

# Integration after review

When a reviewed candidate is integrated into another branch/main, the integration SHA is recorded and material tree/config/dependency differences are classified.

Affected evidence is rerun. Pre-integration approval cannot be represented as approval of materially different integrated code.

# Post-completion invalidation

A completed package/phase may later be challenged by newly discovered security/authority defects, integration regression, corrupt evidence/provenance, invalidated provider assumptions, migration/recovery failure, semantic/architecture mismatch, or proof that a mandatory criterion never actually passed.

The prior G5 record remains historical fact.

A linked invalidation/reopen record is created.

# Reopen states

A post-completion assessment resolves to:

- COMPLETION_REMAINS_VALID;
- REOPEN_REQUIRED;
- UPSTREAM_CHANGE_OR_ARCHITECTURE_REENTRY_REQUIRED;
- INCONCLUSIVE.

REOPEN_REQUIRED means the completed implementation is no longer sufficient for current progression. It does **not** grant implementation authority.

# Reopen authorization

Once G5 closed the package/phase, its former G2 execution envelope is closed.

Post-G5 implementation repair requires:

1. invalidation/reopen record;
2. updated scope/criteria/evidence obligations if needed;
3. dependency/impact review;
4. explicit human/program re-authorization;
5. a new candidate/evidence/review/exit cycle.

If semantic or accepted-architecture contradiction exists, CHG/architecture re-entry occurs before ordinary implementation reopen.

# Downstream invalidation propagation

An upstream reopen does not automatically reopen every downstream package.

Impact is classified using hard/integration/evidence dependencies, shared durable state/schema, shared public contracts, affected scenarios and reused artifact/evidence identity.

Each downstream package receives one of:

- NO_IMPACT;
- EVIDENCE_REFRESH_REQUIRED;
- REVIEW_REFRESH_REQUIRED;
- REOPEN_REQUIRED;
- UPSTREAM_REENTRY_BLOCKER.

That classification is retained as evidence.

# Non-blocking improvements and anti-bloat

Review findings outside the current acceptance boundary become residual risks, backlog/future-package items, later hardening work or documentation cleanup.

They may not be smuggled into the current G2 envelope simply because a reviewer prefers them.

# Machine-checkable control

Current projection:

> docs/routing/phase020_review_repair_exit_gate_governance.json

Phase-020 validation must fail if the contract drifts so that:

- implementers can self-review/self-close;
- reviewer edits remain independently approved without rereview;
- adversarial review can invent hidden requirements;
- PASS can coexist with open blocking findings;
- repair can expand G2;
- source-changing repair reuses stale approval;
- Gatekeeper can override mandatory failure;
- G5 auto-authorizes next execution;
- post-G5 reopen automatically restores old G2;
- completion records can be rewritten;
- Phase 020 gains implementation/release/production authority.

# Phase-020 boundary after 020-H

~~~text
PHASE 020 ACTIVE
020-A/B/C/D/E/F/G/H COMPLETE
020-I NEXT ELIGIBLE

proposed packages                 15
G1-ready packages                 0
G2-authorized packages            0
active implementation packages    0
implementation execution          NOT AUTHORIZED
release authority                 NOT GRANTED
production authority              NOT GRANTED
~~~

# Carry-forward

- **020-I** instantiates migration, recovery, accessibility, performance, cost and scenario verification obligations that review must inspect.
- **020-J** defines whole-system v1 completion and final integration/hardening exit criteria.
- **020-K** instantiates package-specific review/evidence/repair contracts and Gatekeeper ownership.
- **020-L** audits review, repair, reopen and implementation-entry controls before Phase 021.

# Exit decision

**020-H — COMPLETE — PASS.**

MUDAC now has review/exit governance that allows efficient autonomous repair of ordinary defects without allowing implementers, reviewers, green tests or later reopen events to manufacture lifecycle authority.

Next eligible:

> **020-I — Migration, Recovery, Accessibility, Performance, Cost & Scenario Verification Design**

020-I is **NEXT ELIGIBLE / NOT AUTOMATICALLY AUTHORIZED**.

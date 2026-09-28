# 021-R-B — Orchestrator State Machine, Transition Guards & Human Authority Stops

## Status

**STARTED — design contract drafted; exit review not yet performed.**

021-R-B turns the successful Phase-021 operating sequence into an explicit state machine. It defines coordination eligibility, not new implementation authority.

## State-machine purpose

The orchestrator answers four questions deterministically:

1. **What is the current lifecycle state?**
2. **What event has occurred?**
3. **What evidence/guard conditions are required before transition?**
4. **Which actor, if any, is eligible to act next?**

The orchestrator must never answer a fifth question by itself:

> “Should human/program authority grant a consequential action?”

That remains external human authority.

## Core states

The initial state vocabulary is:

```text
IDLE
PLANNING_READY
START_GATE_READY
AWAITING_G2
G2_AUTHORIZED
WORKSPACE_PROVISIONING
IMPLEMENTING
CANDIDATE_REGISTERED
VERIFYING
AWAITING_INDEPENDENT_REVIEW
REPAIR_REQUIRED
AWAITING_ADVERSARIAL_REVIEW
AWAITING_PR_CI
AWAITING_G5
AWAITING_HUMAN_MERGE
INTEGRATION_VERIFYING
AWAITING_CLOSURE_MERGE
COMPLETE
BLOCKED
INCONCLUSIVE
REOPEN_REQUIRED
```

These names describe orchestration states. They do not replace phase/package semantic states maintained by phase authority.

## Principal transition path

```text
PLANNING_READY
  → START_GATE_READY
  → AWAITING_G2
  → G2_AUTHORIZED                       [HUMAN AUTHORITY]
  → WORKSPACE_PROVISIONING
  → IMPLEMENTING
  → CANDIDATE_REGISTERED
  → VERIFYING
  → AWAITING_INDEPENDENT_REVIEW
  → AWAITING_ADVERSARIAL_REVIEW
  → AWAITING_PR_CI
  → AWAITING_G5
  → AWAITING_HUMAN_MERGE                [HUMAN AUTHORITY]
  → INTEGRATION_VERIFYING
  → AWAITING_CLOSURE_MERGE              [HUMAN AUTHORITY]
  → COMPLETE
```

A package may omit a separate closure PR only when its future package contract explicitly authorizes a different evidence integration pattern. The orchestrator may not infer that exception.

## Repair path

```text
review/verification BLOCKED
  → REPAIR_REQUIRED
  → repair-budget / scope guards
  → IMPLEMENTING
  → new candidate SHA/tree
  → VERIFYING
  → fresh independent review
  → fresh adversarial review
```

The orchestrator must record candidate generation. Evidence from generation N cannot be relabeled as evidence for generation N+1.

## Head-drift path

After any review, CI or G5 evidence binds a candidate:

```text
PR_HEAD_CHANGED
  → classify SHA/tree/material-surface delta

same SHA
  → no transition

new SHA + same tree
  → provenance-only binding refresh

new tree + protected material surfaces equivalent
  → integration/delta review route

material protected surface changed
  → invalidate affected evidence
  → return to VERIFYING / independent-review chain

unknown / ambiguous classification
  → INCONCLUSIVE
```

The exact evidence-invalidation calculation belongs to 021-R-C; R-B only requires the transition categories.

## Human authority stops

The state machine must never auto-cross these guards:

| Boundary | Required external authority |
|---|---|
| `AWAITING_G2 → G2_AUTHORIZED` | explicit human/program G2 |
| scope expansion during repair | explicit human/Gatekeeper disposition, and re-authorization where required |
| accepted-architecture contradiction | explicit re-entry/change authority |
| repair-budget override | explicit human/Gatekeeper authority |
| `AWAITING_HUMAN_MERGE → INTEGRATION_VERIFYING` | human protected-merge decision plus observed merge event |
| release eligibility → release | explicit human release authority |
| production eligibility → production | explicit human production authority |
| phase complete → next phase | explicit next-phase start/G2 authority |
| `AWAITING_CLOSURE_MERGE → COMPLETE` | human closure merge when closure PR is part of the package pattern |

An MCP tool, GitHub event, agent message or passing check cannot synthesize these approvals.

## Fail-closed transitions

The orchestrator must enter `BLOCKED`, `INCONCLUSIVE` or `REOPEN_REQUIRED` instead of improvising when:

- current authority cannot be resolved uniquely;
- a required evidence dependency is missing;
- a serialized resource has conflicting writers;
- candidate SHA/tree cannot be established;
- a reviewer is not independent;
- adversarial-session freshness cannot be established;
- verification is nondeterministic;
- event ordering cannot be reconciled;
- repair budget is exhausted;
- repeated-identical-failure threshold is reached;
- scope expansion is needed;
- accepted architecture appears contradictory;
- a production target/secret/data boundary is encountered;
- post-G5 material source change occurs without reopen authority; or
- a requested transition has no declared rule.

Unknown event types may be logged, but may not advance state.

## Event classes

Initial event families:

- `authority.*`
- `workspace.*`
- `candidate.*`
- `verification.*`
- `review.independent.*`
- `review.adversarial.*`
- `repair.*`
- `github.pull_request.*`
- `github.check.*`
- `github.workflow.*`
- `gate.g5.*`
- `human.merge.*`
- `integration.*`
- `closure.*`
- `circuit_breaker.*`
- `reopen.*`

Each accepted event requires an idempotency identity and source provenance. 021-R-E will define the GitHub-specific mapping.

## Actor eligibility

The state machine may emit a `next_action`, but only from a declared role:

- `HUMAN_PROGRAM_AUTHORITY`
- `COORDINATOR_ORCHESTRATOR`
- `CODEX_IMPLEMENTER`
- `CURSOR_IMPLEMENTER`
- `CURSOR_INDEPENDENT_REVIEWER`
- `CODEX_INDEPENDENT_REVIEWER`
- `CURSOR_ADVERSARIAL_REVIEWER`
- `CODEX_ADVERSARIAL_REVIEWER`
- `GATEKEEPER`
- `CI_VERIFIER`

Provider identity and role identity are separate. A provider may fill a different role only in a new independent run that satisfies the role contract.

## No self-certification

The state machine must reject transition evidence when the same run/session/revision acts in incompatible roles, including:

- implementer → independent reviewer;
- implementer → adversarial reviewer;
- reviewer that edits source → reviewer PASS for the changed source;
- Gatekeeper that repairs missing implementation → G5 approval of that repair without new independent evidence.

## State projection rule

The orchestrator state is a **projection**, not semantic authority.

Immutable records remain authoritative for their facts:

- human G2 record;
- candidate SHA/tree;
- verification result;
- review result;
- CI run/check identity;
- G5 decision;
- merge event/integration SHA; and
- reopen/closure records.

The current-state projection may be rebuilt from those records. If projection and immutable facts disagree, reconciliation fails closed and immutable facts win.

## Initial acceptance tests for later implementation

The future autonomy implementation should be able to replay at least the actual Phase-021 sequence and produce the same stops/decisions:

1. register initial candidate;
2. independent review PASS;
3. adversarial review BLOCKED;
4. bounded Repair Cycle 1;
5. new candidate registration;
6. independent PASS;
7. adversarial PASS;
8. PR CI PASS;
9. G5 COMPLETE;
10. PR head drift after `main` merge;
11. governance-only/material-equivalent delta classification;
12. independent delta PASS;
13. adversarial delta PASS;
14. G5 integration rebinding;
15. human implementation merge;
16. post-merge verification;
17. closure PR synchronization;
18. closure CI PASS;
19. human closure merge; and
20. final state COMPLETE with Phase 022 still unauthorized.

That historical replay becomes the first high-value shadow test before the autonomy layer is trusted to route Phase 022.

## Open items for R-B exit

- reconcile this vocabulary against all existing 020-C/H/G machine contracts;
- prove every state transition has one unambiguous guard set;
- specify terminal/reopen semantics precisely;
- define how package-specific optional stages are declared without ad-hoc branching; and
- validate that no state transition itself grants authority reserved to humans.

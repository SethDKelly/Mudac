# 021-R-B — Orchestrator State Machine, Transition Guards, Human Authority Stops & Fail-Closed Semantics

## Status

**COMPLETE — PASS.**

021-R-B converts the proven Phase-021 operating sequence into an explicit lifecycle state machine. It defines deterministic routing eligibility and fail-closed behavior. It does **not** create implementation, merge, release, production, architecture-change, or next-phase authority.

## Exit result

R-B closes with five design questions resolved:

1. the state vocabulary is reconciled against the accepted 020-C operating model, 020-G exact-revision/evidence architecture, and 020-H review/repair/reopen governance;
2. every declared transition has an explicit guard set;
3. `COMPLETE`, `BLOCKED`, `INCONCLUSIVE`, `REPAIR_REQUIRED`, and `REOPEN_REQUIRED` have precise semantics;
4. package-specific stage variation is declared through a lifecycle profile rather than inferred ad hoc; and
5. no transition, GitHub event, MCP call, review PASS, CI PASS, G5 record, or merge event can synthesize authority reserved to a human/program authority.

Machine projection: `docs/routing/autonomy_orchestrator_contract.json`.

## Reconciliation with existing authority

R-B does not replace the Phase-020 contracts. It specializes them into an orchestration projection.

| Existing contract | R-B obligation retained |
|---|---|
| **020-C — autonomous implementation operating model** | human selects the phase/package; G2 is required; Coordinator cannot expand scope or grant G2; worktrees use exact bases; serialized surfaces fail closed; implementer/reviewer/gatekeeper roles remain distinct; hard/engineering circuit breakers remain effective; next phase is never auto-authorized |
| **020-G — CI / exact-revision evidence architecture** | evidence names exact revisions; unexpected HEAD is rejected; PR merge refs are not silently treated as exact candidates; changed trees invalidate affected evidence; content-equivalence reuse requires proof; failed attempts remain retained; CI PASS does not grant merge/release/production authority |
| **020-H — review / repair / exit governance** | author does not certify own implementation; independent and adversarial reviews bind exact candidates; bounded pre-G5 repair may remain inside the original G2; source repair creates a new candidate; G5 is immutable; post-G5 invalidation creates reopen obligations and never restores old G2 automatically |

Where R-B and a normative Phase-020/current canonical contract appear to disagree, reconciliation fails closed and the normative contract wins until the conflict is explicitly resolved.

## Orchestrator responsibility

The orchestrator answers only:

1. what lifecycle state is supported by immutable facts;
2. what event was observed;
3. which declared transition, if any, matches;
4. whether every transition guard is satisfied; and
5. which role is eligible to perform the next bounded action.

The orchestrator does **not** decide whether a human should grant consequential authority.

## State model

```text
inactive
  IDLE

pre-authorization
  PLANNING_READY
  START_GATE_READY
  AWAITING_G2

authorized execution
  G2_AUTHORIZED
  WORKSPACE_PROVISIONING
  IMPLEMENTING
  CANDIDATE_REGISTERED
  VERIFYING

independent evaluation
  AWAITING_INDEPENDENT_REVIEW
  AWAITING_ADVERSARIAL_REVIEW
  AWAITING_PR_CI
  AWAITING_G5

human/integration boundary
  AWAITING_HUMAN_MERGE
  INTEGRATION_VERIFYING
  AWAITING_CLOSURE_MERGE

successful terminal
  COMPLETE

exception states
  REPAIR_REQUIRED
  BLOCKED
  INCONCLUSIVE
  REOPEN_REQUIRED
```

These are orchestration states, not replacements for semantic phase/package authority records.

## Event envelope

Every event eligible to affect state must be immutable or reconstructable and contain, where applicable:

- `event_id`;
- `event_type`;
- source system;
- observed timestamp;
- phase/package/work-unit subject;
- actor role or system identity;
- run/session identity when applicable;
- authority references;
- candidate/base/integration revision identity when applicable; and
- payload/content digest.

Duplicate delivery is expected. The same event identity with the same payload is idempotent. The same identity with a conflicting payload is a reconciliation failure and cannot advance state.

## Named guard set

R-B establishes named guards so transitions are data-driven rather than conversational.

| Guard | Requirement |
|---|---|
| `G_STATE_MATCH` | projected current state matches the transition source and immutable facts do not contradict it |
| `G_AUTHORITY_RESOLVED` | current authority resolves uniquely and the action stays inside its declared envelope |
| `G_G2_EXPLICIT` | explicit human/program G2 names the executable phase/package/work unit |
| `G_REVISION_EXACT` | required SHA/tree identities are known and match the evidence subject |
| `G_EVIDENCE_COMPLETE` | all prerequisite evidence is present, current, non-invalidated, and correctly classified |
| `G_ROLE_ELIGIBLE` | actor role is declared for the action and incompatible role history is absent |
| `G_REVIEW_INDEPENDENT` | reviewer is independent of candidate authoring and has not edited the reviewed revision |
| `G_ADVERSARIAL_FRESH` | adversarial review is a fresh independent run/session against the exact candidate |
| `G_REPAIR_WITHIN_SCOPE` | repair remains within the original G2, work unit, criteria, and declared dependencies |
| `G_REPAIR_BUDGET` | repair budget and repeated-identical-failure thresholds remain available |
| `G_SERIALIZED_SURFACES_CLEAR` | no conflicting writer controls a required serialized surface |
| `G_REQUIRED_CI_PASS` | declared required checks pass for the relevant exact revision; failed history remains retained |
| `G_G5_COMPLETE` | exact-candidate Gatekeeper `COMPLETE` record exists and mandatory predicates remain satisfied |
| `G_HUMAN_MERGE_DECISION` | human protected-merge action/approval is observed; automation did not synthesize it |
| `G_INTEGRATION_CLASSIFIED` | integration SHA is recorded and material delta/evidence impact is classified |
| `G_CLOSURE_SATISFIED` | declared closure mode and required closure evidence are satisfied |
| `G_NO_CIRCUIT_BREAKER` | no unresolved hard or engineering-integrity circuit breaker applies |
| `G_EVENT_IDEMPOTENT` | event was not previously applied with conflicting content |
| `G_EVENT_ORDER_RECONCILED` | late/out-of-order delivery reconciles against repository and immutable evidence truth |
| `G_REOPEN_RECORD` | post-completion invalidation record exists without rewriting historical completion |
| `G_REOPEN_REAUTHORIZED` | explicit human/program reauthorization exists before reopened execution |
| `G_STAGE_PROFILE_DECLARED` | lifecycle variation was declared before execution and is not inferred ad hoc |

A missing guard is not treated as `true`. It produces no transition and routes to `BLOCKED` or `INCONCLUSIVE` according to whether the missing fact is a prohibition or an unresolved fact.

## Principal transition path

The default profile is:

```text
PLANNING_READY
  → START_GATE_READY
  → AWAITING_G2
  → G2_AUTHORIZED                       [HUMAN G2]
  → WORKSPACE_PROVISIONING
  → IMPLEMENTING
  → CANDIDATE_REGISTERED
  → VERIFYING
  → AWAITING_INDEPENDENT_REVIEW
  → AWAITING_ADVERSARIAL_REVIEW
  → AWAITING_PR_CI
  → AWAITING_G5
  → AWAITING_HUMAN_MERGE                [HUMAN MERGE]
  → INTEGRATION_VERIFYING
  → AWAITING_CLOSURE_MERGE              [default closure profile]
  → COMPLETE                            [HUMAN CLOSURE MERGE]
```

The machine contract assigns a guard set to every arrow.

## Lifecycle profiles and optional stages

Optional stages are never discovered by improvisation. Before G2, each package/phase must declare a lifecycle profile.

Default requirements are:

- protected PR integration — required;
- exact candidate verification — required;
- independent code review — required;
- adversarial conformance review — required;
- G5 exit gate — required;
- integration verification — required; and
- closure mode — `SEPARATE_CLOSURE_PR` unless the package contract explicitly selects another allowed mode.

Allowed closure modes are:

1. `SEPARATE_CLOSURE_PR`;
2. `CLOSURE_EVIDENCE_IN_EXISTING_INTEGRATION_FLOW`; or
3. `NOT_APPLICABLE_WITH_EXPLICIT_AUTHORITY`.

Changing the lifecycle profile after G2 is an authority delta requiring review; the orchestrator cannot silently skip a stage because it appears unnecessary.

## Repair semantics

A blocking defect before G5 may enter `REPAIR_REQUIRED` only if the defect is repairable inside the still-open G2 scope and budget.

```text
required verification/review/CI/G5 defect
  → REPAIR_REQUIRED
  → G_REPAIR_WITHIN_SCOPE
  → G_REPAIR_BUDGET
  → IMPLEMENTING
  → new candidate SHA/tree
  → affected verification
  → fresh affected review chain
```

A source change creates a new candidate generation. Evidence for generation N cannot be relabeled as evidence for generation N+1.

Scope expansion, new undeclared package/dependency, architecture/semantic contradiction, exhausted budget, repeated-identical failure threshold, unresolved serialized-surface collision, production boundary, or nondeterministic mandatory evidence routes to `BLOCKED`/`INCONCLUSIVE` rather than repair-by-improvisation.

## Head-drift semantics

After candidate-bound evidence exists, a head change is classified before any further state advance:

| Delta | Result |
|---|---|
| same SHA | no action |
| new SHA, same tree | provenance/binding refresh only |
| new tree, protected material proven equivalent | delta-review route; R-C determines evidence reuse |
| protected material changed | affected evidence invalidated; return to the earliest required verification/review state |
| classification not provable | `INCONCLUSIVE` |

R-B defines the state consequences; 021-R-C owns the evidence dependency/invalidation calculation.

## Exception-state semantics

### `REPAIR_REQUIRED`

A known defect exists and may be repairable under the current pre-G5 G2. No scope increase is implied. Source repair creates a new candidate and reruns affected evidence/reviews.

### `BLOCKED`

The current envelope cannot legally or safely advance. `BLOCKED` does not itself grant scope expansion, budget extension, new G2, merge, release, production, or architecture-change authority.

A blocked flow may resume only when a new immutable disposition/authority resolves the blocker. Resume occurs at the **earliest state whose guards are now satisfied**; mandatory states cannot be skipped.

### `INCONCLUSIVE`

The orchestrator cannot deterministically establish a required fact. Automatic retry-until-green is forbidden. New evidence or successful reconciliation must establish the missing fact, after which state is recomputed from immutable records rather than optimistically advanced.

### `COMPLETE`

`COMPLETE` means the declared lifecycle profile is satisfied for the recorded revision and closure mode. The completion/G5 history remains immutable. `COMPLETE` does not grant the next phase, release, or production authority.

### `REOPEN_REQUIRED`

A post-completion invalidation has been established. Historical completion is retained, but current confidence is invalidated.

Old G2 is **not** restored. Reopened implementation requires:

1. an invalidation/reopen record;
2. dependency-impact review;
3. updated scope/criteria/evidence where needed; and
4. explicit human/program reauthorization.

Only after reauthorization may the projected state enter `G2_AUTHORIZED` for a new candidate/evidence/review cycle. Architecture contradiction instead blocks on upstream re-entry.

## Human authority stops

The state machine cannot auto-cross:

| Boundary | Required external authority |
|---|---|
| `AWAITING_G2 → G2_AUTHORIZED` | explicit human/program G2 |
| material scope expansion | explicit human/program disposition and reauthorization when execution changes |
| accepted architecture contradiction | explicit change/re-entry authority |
| repair-budget override | explicit human/program extension |
| protected implementation merge | human merge decision plus observed merge event |
| closure merge when required | human closure merge decision |
| reopened implementation | explicit human/program reauthorization |
| release | explicit release authority |
| production | explicit production authority |
| phase/package completion → next phase | explicit next-phase start/G2 authority |

The following implications are explicitly false:

```text
review PASS  != merge authority
CI PASS      != merge authority
G5 COMPLETE  != merge authority
G5 COMPLETE  != next G2
merge        != release authority
merge        != production authority
COMPLETE     != next-phase authority
GitHub event != human approval
MCP call     != human approval
```

## Role independence

R-B preserves the 020-C/H role model:

- implementer cannot independently certify the same candidate;
- independent review cannot reuse the authoring run/session;
- adversarial review must be a fresh independent run/session;
- a reviewer that edits source becomes an implementer for the changed revision;
- Gatekeeper cannot repair candidate source and then certify the repair without new independent evidence;
- provider diversity is preferred, but role/run independence is mandatory.

## Projection and reconciliation

Current orchestrator state is a projection over immutable facts, including:

- G2/reopen authority records;
- candidate SHA/tree;
- verification records;
- independent/adversarial review records;
- CI/check/run identities;
- G5/completion record;
- merge/integration identity;
- closure records; and
- invalidation/reopen records.

The projection is rebuildable. Bootstrap prose is not execution authority. If projection and immutable facts conflict, the projection does not win: reconciliation fails closed.

Out-of-order GitHub/event delivery is expected and never trusted as chronology by itself. 021-R-E will define concrete GitHub event mapping and reconciliation mechanics.

## Undeclared transitions

No dynamic transition synthesis is allowed.

If an event does not match a declared transition for the supported current state, the event may be recorded for audit but cannot advance state. Material unknown cases route to `INCONCLUSIVE` or `BLOCKED`.

## R-B shadow acceptance obligations

Later implementation must replay at least the actual Phase-021 sequence and demonstrate the same decisions/stops:

1. initial candidate registration;
2. independent PASS;
3. adversarial BLOCKED;
4. bounded Repair Cycle 1;
5. new candidate registration;
6. fresh independent PASS;
7. fresh adversarial PASS;
8. required PR CI PASS;
9. G5 COMPLETE;
10. candidate/head drift after integration;
11. governance-only/material-equivalent delta classification;
12. delta review/evidence refresh;
13. G5/integration rebinding;
14. human implementation merge;
15. post-merge verification;
16. closure synchronization;
17. closure CI PASS;
18. human closure merge; and
19. final `COMPLETE` while Phase 022 remains unauthorized.

R-G owns the executable shadow-replay plan; R-B fixes the expected state semantics.

## Exit decision

**021-R-B COMPLETE — PASS.**

Exit criteria:

- 020-C/G/H semantics reconciled — **PASS**;
- every declared transition has an explicit guard set — **PASS**;
- terminal/exception/reopen semantics are explicit — **PASS**;
- package-specific variation has a predeclared lifecycle-profile mechanism — **PASS**;
- human authority cannot be inferred from machine events — **PASS**;
- application/runtime autonomy remains unimplemented and unauthorized — **PASS**;
- Phase 022 remains `NEXT ELIGIBLE / NOT AUTHORIZED` — **PASS**.

**Next eligible retrospective work: 021-R-C — Evidence Dependency Graph, Invalidation, Content Equivalence & Evidence Reuse.**

# AUT-001-B — Stage Transition / Start Gate

**Decision:** PASS — READY FOR IMPLEMENTATION / NOT STARTED

## 1. Authority and transition

AUT-001-B is already included in the human-authorized AUT-001 core G2 envelope. This start gate does not create a new G2 and does not expand the authorized package.

The prior current-stage projection named AUT-001-A. AUT-001-A has now passed G5, merged through explicit human authority, and integrated on `aut-001/start-gate` as:

- reviewed candidate: `9133eabeb18dfd10d533ab399dc1c3b3c0ae4c1a`
- integration: `e69e76398aedfe17bc8a800c235d16548ff42d44`
- integration tree: `dff68862e95c2be6a05bc8385b6f4d6df3fe9790`
- candidate→integration classification: `PROVENANCE_ONLY_CHANGE / CONTENT_EQUIVALENT`
- post-merge Knowledge Validation: run `36458789685` — SUCCESS

`docs/routing/aut001_b_stage_transition_start_gate.json` therefore becomes the current-stage projection for B only. The original G2 scope, exclusions, criteria, repair rules, human authority stops, production denial, Phase-022 denial, and predecessor gating remain binding.

## 2. Purpose

AUT-001-B implements the first live external-observation stage of the control plane: a **read-only GitHub shadow and reconciliation layer**.

Its responsibility is to observe GitHub notifications and current repository truth, normalize immutable delivery/fact records, reconcile PR/ref/check/workflow state, feed trustworthy facts into the deterministic AUT-001-A projection core, and record every disagreement between projected state and authoritative repository/human coordination state.

B does not perform coordination writes. It observes, reconciles, projects, records, and fails closed.

## 3. Governing principles

The following are non-negotiable:

1. **GitHub events are notifications, not lifecycle truth.**
2. **Arrival order is not lifecycle order.**
3. **Consequential projected state must be reconciled against current authoritative repository truth.**
4. **Stale/superseded facts remain historical and cannot satisfy current evidence.**
5. **PR number identity never substitutes for exact SHA/tree identity.**
6. **Missed events must be recoverable by startup/periodic reconciliation.**
7. **Every shadow divergence must be recorded, explained, and dispositioned.**
8. **Any unsafe advancement prediction is a blocking defect.**
9. **AUT-001-B performs no GitHub mutation and no agent dispatch.**

## 4. Exact entry baseline

Implementation must branch from the B start-gate line descended from:

`e69e76398aedfe17bc8a800c235d16548ff42d44`

with tree:

`dff68862e95c2be6a05bc8385b6f4d6df3fe9790`

Planning branch:

`aut-001/b-start-gate`

A future B implementation branch must be created from the final exact start-gate head and record that base explicitly.

## 5. In scope

- read-only GitHub API/repository truth acquisition;
- normalized immutable delivery envelopes;
- delivery idempotency and conflicting-delivery detection;
- semantic PR/ref/check/workflow fact extraction;
- exact-head and base-drift reconciliation;
- stale, duplicate, conflicting, out-of-order and missed-event handling;
- startup and/or periodic authoritative reconciliation;
- append-only shadow observation and processing-attempt records;
- reuse of AUT-001-A lifecycle/evidence logic rather than duplicate logic;
- deterministic projected state / eligible-next-action computation;
- shadow divergence recording, explanation and disposition;
- restart reconstruction from local append-only records plus current authoritative truth;
- bounded live shadow evidence in `AUT-S`;
- read-only observability/health needed to prove the above.

## 6. Out of scope

AUT-001-B may not implement or exercise:

- GitHub writes of any kind;
- PR creation/update/comment/review mutations;
- ready/draft transitions;
- dependency-branch synchronization;
- provider/Cursor/Codex dispatch;
- development-control MCP runtime;
- bounded non-human side effects;
- generic shell, Git, GitHub API, HTTP, SQL, cloud, or browser-eval capability surfaces;
- secret retrieval or publication of secret/signature values;
- production application/database/cloud/browser access;
- protected or closure merge;
- G2 creation, scope expansion, architecture acceptance, or repair-budget override;
- release or production;
- Phase 022 execution/authority;
- AUT-001-F / 020-D bridge behavior.

## 7. Material surfaces

Prefer the canonical pre-G2 selectors rather than adding new path qualifications:

- `tools/autonomy-control/src/github/` — `AUT-MS-GITHUB`
- `tools/autonomy-control/src/storage/` — `AUT-MS-STORAGE-OPS`
- `tools/autonomy-control/src/observability/` — `AUT-MS-STORAGE-OPS`
- `tools/autonomy-control/src/health/` — `AUT-MS-STORAGE-OPS`
- `tools/autonomy-control/test/` — `AUT-MS-HARNESS`
- `tools/autonomy-control/fixtures/` — `AUT-MS-HARNESS`

The optional shared evaluator surface:

`.github/workflows/autonomy-control-shadow.yml`

is **not automatically reserved or required**. If implementation proves it necessary, it must be separately reserved/classified and its evaluator impact reviewed before use.

Any unmatched changed path is `INCONCLUSIVE_UNTIL_CLASSIFIED`.

## 8. Required visible criteria

### AUT-C02 — fail-closed incomplete/contradictory truth

Unknown, contradictory, stale, out-of-order or incomplete live truth must never produce optimistic lifecycle advancement.

### AUT-C05 — GitHub truth/idempotency/reconciliation

Delivery idempotency, semantic fact idempotency, exact-head check evaluation, head/base drift, missed-event reconciliation and GitHub truth must conform to R-E without treating notification order as authority.

### AUT-C11 — restart/missed-delivery recovery

A restart, missed delivery or transient read failure must reconstruct safe current shadow state from append-only local records plus authoritative external truth without erasing failed/stale history or using retry-until-green acceptance.

### AUT-C15 — shadow divergence

Every disagreement between projected state/next action and authoritative human/repository truth must be recorded, explainable and dispositioned. Any unsafe advancement prediction blocks B acceptance.

## 9. Evidence obligations

### AUT-E03 — mandatory B evidence

Run a bounded live read-only GitHub shadow window that:

- reconciles PR/ref/check/workflow truth;
- binds evidence to an exact candidate revision;
- records divergence;
- demonstrates zero GitHub mutation.

### AUT-E08 — B recovery slice

Demonstrate restart/replay and missed-delivery reconstruction with append-only historical preservation and no retry-until-green behavior.

### AUT-E09 — B stage review slice

Before B G5, obtain:

- exact-head repository verification;
- fresh independent review in a separate context/worktree;
- fresh adversarial review in another separate context/worktree;
- no unresolved blocking findings.

## 10. Mandatory scenario matrix

At minimum B must execute and retain evidence for:

1. duplicate identical delivery → idempotent no-op;
2. duplicate key with conflicting payload → fail closed/security reconciliation;
3. unknown event/action → record without lifecycle advance;
4. stale event for superseded head → historical only;
5. late check for superseded candidate → does not satisfy current CI;
6. PR head movement → freeze optimistic advancement + classify delta;
7. base drift → observe/reconcile only, no synchronization write;
8. required check missing/running/failed/cancelled → no CI-pass transition;
9. merge notification alone → insufficient until PR/ref/integration truth reconciles;
10. missed delivery → authoritative reconciliation reconstructs truth;
11. restart → deterministic reconstruction without history erasure;
12. projected-state disagreement → divergence record with explanation/disposition;
13. unsafe advancement prediction → blocking defect;
14. complete live shadow window → zero GitHub mutations.

## 11. Implementation constraints

Preferred role assignment from the package contract:

- implementer: **Cursor**
- independent reviewer: **Codex**
- adversarial reviewer: **fresh separate session**

Provider choice is not authority-bearing.

B must reuse the AUT-001-A deterministic projection/evidence primitives. Reimplementing a competing lifecycle or materiality engine is not permitted.

Storage technology is intentionally not prescribed. Prefer the smallest tool-local mechanism that can prove append-only history, deterministic replay and restart reconstruction. New infrastructure requires justification and material classification.

## 12. Circuit breakers

Immediately block/fail closed on:

- any GitHub write attempt;
- any agent-dispatch attempt;
- generic external capability request;
- production target or credential use;
- event treated as truth without reconciliation;
- notification arrival order used as lifecycle order;
- unexplained shadow divergence;
- unsafe optimistic advancement prediction;
- conflicting delivery identity;
- unavailable mandatory truth followed by optimistic fallback;
- unmapped material change;
- scope/authority expansion requirement.

## 13. Repair policy

B receives the package-default bounded repair policy:

- 2 ordinary repair cycles;
- repeated identical mandatory failure threshold: 2;
- scope expansion is not repair;
- budget exhaustion requires explicit human/program extension;
- source repair creates a new candidate generation;
- affected evidence and reviews must refresh.

## 14. Exit boundary

AUT-001-B may reach G5 only when all of the following are true:

- exact candidate SHA/tree recorded;
- repository verification clean;
- AUT-C02/C05/C11/C15 satisfied;
- AUT-E03 satisfied through a bounded live read-only shadow window;
- B slice of AUT-E08 satisfied;
- zero GitHub mutation demonstrated;
- all observed divergence dispositioned;
- fresh independent review PASS;
- fresh adversarial review PASS;
- no open blocking findings;
- B Gatekeeper returns COMPLETE;
- merge/integration remains a separate human-authority step.

## 15. Start-gate decision

All predecessor and authority conditions required to begin B are satisfied.

**AUT-001-B START GATE: PASS / READY FOR IMPLEMENTATION / NOT STARTED.**

This decision makes B the current stage projection inside the already-authorized core G2 envelope. It does not start implementation automatically and grants no authority for AUT-001-C, AUT-001-F, Phase 022, merge, release, or production beyond what is already explicitly present in the package authority.

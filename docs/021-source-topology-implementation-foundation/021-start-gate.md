# Phase 021 Start Gate — Source Topology & Implementation Foundation

**Package:** IMP-001  
**Decision:** PASS — READY FOR G2 DECISION  
**G2:** NOT AUTHORIZED  
**Implementation execution:** NOT AUTHORIZED

## Entry baseline

Phase 020 is complete on protected `main`. The Phase-021 start baseline is:

- commit: `37d7f30713424c89408573cf62269a388d9a0c4c`
- tree: `5bd544961bc94eed27aae9955e3cd3cacb4d4dc8`
- ruleset: `main — protected` / active
- required checks: Knowledge Validation, Implementation Verification, CodeQL

## Substrate qualification

Accepted architecture has five semantic owners:

1. Competition Context
2. Identity & Access
3. Evaluation
4. Outcomes & Officiality
5. External Representation

The executable workspace still contains a sixth shell: `packages/modules/judging-operations`.

That shell contains only `export {};` and no domain behavior. The current dependency-cruiser rules also encode the obsolete six-owner chain.

Therefore IMP-001 can be implemented as a bounded mechanical topology repair. No semantic code migration is required.

## Authorized implementation shape if G2 is later granted

One writable implementation work unit only:

> **021-I01 — Codex Implementer**

It owns the complete bounded IMP-001 repair because the relevant surfaces are serialized root/workspace/dependency surfaces. Parallel implementation would increase collision risk without useful concurrency.

Implementation sequence:

1. retire the empty `judging-operations` package and executable references;
2. update workspace/lock metadata only as required by that removal;
3. rewrite dependency-cruiser rules for the accepted five-owner topology;
4. preserve application/foundation/projection/test-support boundaries;
5. run full verification and prove there is no active six-owner executable path.

Scope explicitly excludes domain behavior, database schema, provider deployment, feature UI, semantic redesign and architecture changes.

## Review shape

After Codex freezes and pushes a candidate commit:

- **021-R01 — Cursor independent code review** runs against the exact candidate SHA in a separate worktree and must not edit it.
- **021-R02 — Cursor adversarial conformance review** runs in a fresh Cursor session against the same SHA and specifically challenges stale six-owner assumptions, scope expansion and hidden semantic movement.
- Findings go back to Codex. Cursor does not fix findings while acting as Reviewer.
- Any Codex repair creates a new candidate SHA and invalidates affected approvals/evidence.
- Public CI and repository verification run against the new candidate.
- A separate Gatekeeper integrates the evidence and may decide COMPLETE, REPAIR_REQUIRED, BLOCKED or INCONCLUSIVE. It cannot grant the next G2.

## Start-gate decision

All Phase-021 prerequisites are satisfied for a human G2 decision:

- Phase 020 complete;
- protected main verified;
- IMP-001 G1 READY_FOR_AUTHORIZATION;
- no hard predecessors;
- scope and exclusions explicit;
- work-unit graph explicit;
- implementer/reviewer roles explicit;
- serialized surfaces explicit;
- visible criteria/evidence already defined by 020-K;
- repair budget explicit;
- no current semantic/architecture blocker.

**This start gate does not grant G2.**

The next decision is whether to explicitly authorize **IMP-001 / Phase 021** for implementation under the exact scope above.

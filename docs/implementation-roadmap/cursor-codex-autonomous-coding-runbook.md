# Cursor + Codex Autonomous Implementation Runbook

This runbook is the default human operating procedure for MUDAC autonomous implementation.

It does **not** grant G2 or any other execution authority.

## Principle

Use Git revisions as the handoff boundary between agents.

Do not make Cursor and Codex collaborate through one writable checkout or one long shared conversation.

The default cycle is:

~~~text
Human / Coordinator
        |
        | explicit G2
        v
Codex IMPLEMENTER
writable worktree
        |
        | freeze candidate SHA
        v
Cursor REVIEWER
separate detached worktree
        |
        | PASS or findings
        v
Codex IMPLEMENTER
repair same authorized scope
        |
        | new candidate SHA
        v
Cursor fresh review
        |
        v
CI / verifier
        |
        v
Gatekeeper
        |
        v
Human merge decision
~~~

For packages whose roadmap assignment prefers Cursor implementation, reverse Codex and Cursor.

## Recommended local layout

Keep one control checkout that tracks protected main and is not used for implementation edits.

Example on Windows PowerShell/Git Bash terminology:

~~~text
Mudac/                         control checkout on main
../mudac-wt-021-codex/        writable implementation worktree
../mudac-wt-021-cursor-review/ detached review worktree
~~~

The control checkout is where you inspect lifecycle state, fetch branches, create worktrees and verify merges.

## Before an implementation run

From the control checkout:

~~~bash
git fetch origin
git switch main
git pull --ff-only
git status
git rev-parse HEAD
git rev-parse HEAD^{tree}
~~~

Compare the SHA/tree against the authorized start-gate/G2 record. If they differ materially, stop and re-run the start-gate baseline check.

Install/use the repository-declared toolchain:

- Node 24
- pnpm 11.25.x
- Git
- Codex CLI or Codex IDE integration
- Cursor

Do not place production credentials or production data in either agent worktree.

## Create the Codex implementation worktree

Only after explicit G2:

~~~bash
git fetch origin
git worktree add ../mudac-wt-021-codex -b work/021/imp-001-topology <AUTHORIZED_BASE_SHA>
cd ../mudac-wt-021-codex
pnpm install --frozen-lockfile
~~~

Launch Codex **from this worktree**.

For Phase 021, give Codex the Phase-021 start-gate record plus the IMP-001 contract and tell it:

> Implement only work unit 021-I01 under the granted G2 scope. Read AGENTS.md first. Do not broaden scope, alter product semantics, modify database/provider/UI behavior, merge, deploy, or touch production. Stop on any circuit breaker. Run the required verification, commit the candidate, and report the exact commit SHA/tree, changed files, commands run, evidence, and residual concerns.

Do not ask Codex to review/approve its own candidate.

## Freeze the candidate

When Codex reports completion:

~~~bash
git status
git log -1 --oneline
git rev-parse HEAD
git rev-parse HEAD^{tree}
pnpm verify
python scripts/run_agentic_conformance.py
git push -u origin work/021/imp-001-topology
~~~

Open a draft PR to protected `main`.

The PR becomes the shared coordination surface. Record the candidate SHA/tree and verification results there.

Do not continue editing while Cursor reviews that SHA.

## Create the Cursor review worktree

From the control checkout:

~~~bash
git fetch origin
git worktree add --detach ../mudac-wt-021-cursor-review <CANDIDATE_SHA>
~~~

Open **that detached worktree** in Cursor.

Do not open the Codex writable worktree as the Cursor review workspace.

For the independent code-review session, tell Cursor:

> Review this exact candidate SHA for IMP-001. Do not edit files. Resolve current authority independently from repository docs before considering implementer rationale. Review architecture fidelity, correctness, dependency direction, stale six-owner assumptions, scope discipline, maintainability and evidence quality. Return PASS or structured findings with file/line evidence, authority references, affected criteria, severity/blocking status, and recommended repair direction.

For adversarial review, start a **fresh Cursor session** against the same detached worktree:

> Perform adversarial conformance review of this exact IMP-001 candidate. Do not edit files. Try to falsify the claim that the workspace now represents the accepted five-owner topology without semantic/domain movement. Look for hidden six-owner references, dependency-rule gaps, test/evidence gaming, speculative abstractions, scope expansion, weakened checks, or authority leakage. Return PASS or structured findings.

## Repair loop

If Cursor finds a blocking defect:

1. Record the finding against the reviewed candidate SHA.
2. Return to the Codex implementation worktree.
3. Give Codex only the structured findings and relevant public authority.
4. Codex repairs within the original G2 scope.
5. Run verification.
6. Commit/push a **new** candidate SHA.
7. Recreate or retarget the Cursor review worktree to that new SHA.
8. Start fresh review sessions again.

Default repair budget is three cycles. Two repeated materially identical failures are an escalation signal.

Cursor must not fix code while acting as Reviewer. If Cursor edits the candidate, Cursor becomes an Implementer for that revision and a new independent review is required.

## PR and merge policy

The protected PR is the integration boundary.

A candidate is not ready to merge merely because an agent says it is done.

Before merge, require:

- exact candidate identity known;
- visible criteria satisfied;
- independent code review PASS;
- adversarial conformance PASS;
- required CI PASS;
- no unresolved circuit breaker;
- Gatekeeper COMPLETE/G5 decision;
- human merge decision.

The Gatekeeper does not grant the next phase's G2.

## Role rotation across the roadmap

Use the 020-K preferred assignments as the default rotation:

| Package | Implementer | Independent reviewer |
|---|---|---|
| IMP-001 | Codex | Cursor |
| IMP-002 | Codex | Cursor |
| IMP-003 | Cursor | Codex |
| IMP-004 | Cursor | Codex |
| IMP-005 | Codex | Cursor |
| IMP-006 | Codex | Cursor |
| IMP-007 | Cursor | Codex |
| IMP-008 | Cursor | Codex |
| IMP-009 | Cursor | Codex |
| IMP-010 | Cursor | Codex |
| IMP-011 | Codex | Cursor |
| IMP-012 | Cursor | Codex |
| IMP-013 | Codex | Cursor |
| IMP-014 | Codex | Cursor |
| IMP-015 | Codex | Cursor |

Provider assignment is a default operating profile, not semantic authority. If one provider is unavailable, a fresh independent run may substitute, but author/reviewer independence remains mandatory.

## Cursor-native worktrees

Cursor supports isolated worktrees natively. They are useful, but for MUDAC the recommended first implementation phases use **explicit Git worktrees created by the Coordinator** because the branch name, base SHA and path remain obvious to both Cursor and Codex.

After the process is stable, Cursor-native `/worktree` or CLI `--worktree` may be used where it preserves the same exact-base and isolated-write rules.

## Codex environment

Codex should start inside the authorized implementation worktree and read repository `AGENTS.md` before changing files.

Keep the environment reproducible and let repository commands provide the feedback loop. Do not compensate for a failing repository setup with ad-hoc global dependencies or hidden local state.

## Information passed between agents

Pass:

- phase/package/work-unit IDs;
- exact base/candidate SHA and tree;
- public authority references;
- in-scope/excluded surfaces;
- changed-file list;
- commands/results;
- structured review findings;
- CI links/run IDs;
- residual risks.

Do not pass private chain-of-thought, hidden evaluator probes, secrets, or a giant transcript of the other agent's conversation.

The repository plus exact Git identity is the source of shared truth.

## Phase 021 concrete setup

When G2 is granted for IMP-001:

~~~bash
# control checkout
git fetch origin
git switch main
git pull --ff-only

# implementation
git worktree add ../mudac-wt-021-codex   -b work/021/imp-001-topology   <AUTHORIZED_BASE_SHA>

# later, after Codex freezes candidate
git worktree add --detach ../mudac-wt-021-cursor-review   <CANDIDATE_SHA>
~~~

Phase 021 deliberately uses one implementation worktree at a time because root manifests, lockfile and dependency rules are serialized surfaces.

## Stop conditions

Stop instead of improvising when:

- implementation requires domain behavior;
- an accepted architecture rule appears contradictory;
- the change needs a new package outside IMP-001;
- a serialized surface is being modified by another active agent;
- production access/data/secrets appear;
- verification is nondeterministic;
- repair requires weakening tests or criteria;
- the repair budget is exhausted.

Escalate through the human/program authority rather than silently expanding the task.

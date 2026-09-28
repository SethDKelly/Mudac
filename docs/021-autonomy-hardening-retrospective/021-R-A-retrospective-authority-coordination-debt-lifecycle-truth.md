# 021-R-A — Retrospective Authority, Coordination Debt & Lifecycle-Truth Boundary

## Decision

**021-R-A COMPLETE — PASS.**

This record opens a post-completion retrospective/design boundary only. Phase 021 remains COMPLETE and its G5/integration evidence remains historical fact. Phase 022 remains NEXT ELIGIBLE / NOT AUTHORIZED.

## Exact retrospective baseline

The retrospective begins from protected `main`:

- commit: `29637b92047047f7c1e3a08ff377f4ca68a2997a`
- tree: `4878dcfa09540033d2f51d88ef93b1d460a2fe29`
- preceding Phase-021 implementation integration: `a38d9cb3da9dcad70467fef15ebd91743a80bbb3`
- Phase-021 completion/G5 closure PR: #20

The retrospective may describe lessons from earlier exact revisions but may not rewrite those revisions' evidence.

## Why this boundary exists

Phase 021 demonstrated that the designed safety model works. In particular it successfully exercised:

- exact-SHA candidate freezing;
- isolated implementer/reviewer work;
- independent review followed by a fresh adversarial review;
- bounded repair after adversarial falsification;
- re-verification on a new candidate;
- protected PR checks;
- G5 before human merge;
- detection of candidate-head drift after `main` entered the implementation branch;
- content-equivalence reasoning instead of either silent evidence reuse or wasteful full restart;
- independent and adversarial integration-delta review;
- append-only rebinding rather than historical evidence mutation;
- implementation PR followed by governance/closure PR; and
- post-merge exact-revision verification.

The process succeeded, but a human/coordinator still performed most orchestration transitions manually.

## Observed coordination debt

### CD-001 — Manual next-action routing

The runbook defines the correct sequence, but a coordinator must still decide and initiate almost every transition: worktree setup, candidate freeze, reviewer dispatch, repair return, CI observation, G5 preparation, merge pause and post-merge closure.

**Design response:** encode eligible transitions and next actors in a machine-readable state machine.

### CD-002 — Exact-revision drift requires human detection

PR #19 changed from the reviewed G5 candidate to a different head after `main` was merged. The process caught this correctly, but only after manual inspection.

**Design response:** any head/tree change after evidence binding becomes an event that automatically triggers delta classification and evidence invalidation/reuse calculation.

### CD-003 — Evidence dependencies are implicit

Humans reasoned that executable IMP-001 surfaces were unchanged while authority/governance surfaces changed, so full implementation evidence could be reused but exact-head/G5 binding required refresh.

**Design response:** represent evidence dependencies, material-surface classes and invalidation rules explicitly.

### CD-004 — Review dispatch is conversational

Independent and adversarial Cursor sessions were correctly separated, but prompts/context were manually assembled and freshness was operational convention.

**Design response:** dispatcher-issued immutable context manifests and run identities, with role/session freshness encoded as evidence.

### CD-005 — GitHub choreography is manual

Draft/open/ready transitions, base synchronization, CI observation and post-merge identity capture required human coordination.

**Design response:** event-driven GitHub adapter with idempotent event handling and reconciliation against repository truth.

### CD-006 — Current lifecycle posture can drift across routing surfaces

At this retrospective baseline, the Phase-021 index correctly reports Phase 021 COMPLETE/INTEGRATED and Phase 022 NOT AUTHORIZED, while root `AGENTS.md`, `docs/index.md`, and some older operating-model current-position text still narrate a pre-Phase-021 posture.

This does not invalidate the completed Phase-021 implementation, but it is an autonomy risk: agents should not infer current execution authority from several independently maintained prose snapshots.

**Design response:** establish one machine-readable current lifecycle projection derived from immutable phase/gate records; bootstrap prose must route to it rather than independently narrate mutable current state.

### CD-007 — Closure evidence required a second PR but dependency was not machine-managed

The implementation/closure split worked well, but the closure PR became out-of-date when its dependency merged.

**Design response:** encode PR dependency/order and automatic base synchronization/reverification rules.

## Authority boundary

The retrospective is permitted as repository governance/design work under the user's explicit instruction. Its allowed actions are limited to:

- planning and design documents;
- machine-readable draft control contracts;
- validation of those contracts where non-executing;
- lifecycle-routing normalization that does not rewrite historical gate evidence; and
- a later recommendation for a separately authorized autonomy implementation work unit.

The retrospective does not grant source/runtime implementation authority.

## Non-negotiable inherited constraints

The autonomy layer must preserve:

1. explicit G2 before implementation execution;
2. isolated writable worktrees;
3. implementer/reviewer independence;
4. a fresh adversarial review after independent PASS;
5. exact-SHA/tree evidence binding;
6. bounded repair and circuit breakers;
7. protected CI;
8. Gatekeeper G5 without self-repair or self-review;
9. human protected-merge authority;
10. no automatic release/production;
11. no automatic next-phase authority;
12. hidden probes may not create hidden requirements; and
13. source/tree changes invalidate affected evidence rather than being silently accepted.

## Lifecycle-truth rule accepted for subsequent design

021-R adopts this rule for R-B..G:

> **Mutable current lifecycle state must have one machine-readable projection whose facts are derived from immutable authority/evidence records. Human-facing bootstrap prose may summarize or link to that projection but must not become a competing execution-authority ledger.**

The future projection must distinguish at least:

- historical gate facts;
- current phase/package eligibility;
- current G2 authorization;
- active candidate identity;
- evidence/review state;
- merge/release/production authority; and
- next-phase authority.

## Exit assessment

021-R-A passes because:

- Phase-021 history was reviewed without reopening it;
- the autonomy opportunity is expressed as coordination automation rather than broader agent discretion;
- lifecycle-truth drift is explicitly recognized;
- inherited safety/authority gates remain intact; and
- the next design unit can define the orchestrator state machine without authorizing implementation.

**Next:** 021-R-B — Orchestrator State Machine, Transition Guards, Human Authority Stops & Fail-Closed Semantics.

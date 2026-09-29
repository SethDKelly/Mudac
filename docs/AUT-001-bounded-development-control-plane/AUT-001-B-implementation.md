# AUT-001-B — Live Read-Only Shadow & GitHub Reconciliation

**State:** REPAIR CYCLE 1 IMPLEMENTED / NEW CANDIDATE AWAITING EXACT-HEAD CI + RETAINED LIVE SHADOW

## Repair Cycle 1 candidate

- start-gate base: `f87f57fa42edd1ec81fc79626f6c93091793d71f`
- implementation branch: `aut-001/b-read-only-shadow`
- historical independently reviewed candidate: `a000d58bb310f797e92d8f9c2bcc0f9afa147b5f` (immutable; `CHANGES_REQUIRED`)
- repair cycle: `1 / 2`
- exact verification/review candidate: the branch head after Repair Cycle 1 commits; bind CI/reviews to that exact SHA/tree.

Finding closure requires refreshed independent review. Code edits alone do not close `AUT-B-IR-01` through `AUT-B-IR-06`.

## Repair Cycle 1 scope

Repairs accepted independent-review findings inside the existing AUT-001-B G2 envelope:

- `AUT-B-IR-01` — bind required-check truth to package contract + live repository ruleset enforcement
- `AUT-B-IR-02` — execute Stage-B harness under canonical `pnpm test` / `pnpm verify`
- `AUT-B-IR-03` — separate semantic-fact identity from observation timestamps
- `AUT-B-IR-04` — unknown action under known event family → `RECORD_NO_ADVANCE`
- `AUT-B-IR-05` — bounded observation window with retained AUT-E03 artifact evidence
- `AUT-B-IR-06` — separate check-run context satisfaction from workflow provenance; no check-run ID attempt ordinal

Shared evaluator surface reservation for Vitest inclusion:

- `docs/routing/aut001_b_vitest_evaluator_reservation.json`

## Implemented boundary

AUT-001-B implements the read-only reconciliation substrate only. It introduces no GitHub write capability, no agent dispatch, no MCP action surface, no branch synchronization, no merge authority, and no production or Phase-022 authority.

## Verification boundary

Repository CI and retained live-shadow artifact evidence must qualify the exact Repair Cycle 1 candidate before independent/adversarial review and B G5.

Any further source repair creates a new candidate generation and consumes remaining repair budget.

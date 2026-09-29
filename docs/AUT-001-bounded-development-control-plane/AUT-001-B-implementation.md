# AUT-001-B — Live Read-Only Shadow & GitHub Reconciliation

**State:** REPAIR CYCLE 2 IMPLEMENTED / NEW CANDIDATE AWAITING EXACT-HEAD CI + RETAINED LIVE SHADOW + INDEPENDENT REVIEW

## Repair Cycle 2 candidate

- start-gate base: `f87f57fa42edd1ec81fc79626f6c93091793d71f`
- implementation branch: `aut-001/b-read-only-shadow`
- immutable Repair Cycle 1 reviewed candidate: `3ee685c78d530c428d6b5656a3bf03ec18812371` (`CHANGES_REQUIRED`)
- Repair Cycle 1 reviewed tree: `bff9f5fd5381a13300f21777b115d9a211c7c1ab`
- repair cycle consumption after this source candidate: `2 / 2`
- exact verification/review candidate: bind CI/reviews only to the final Repair Cycle 2 branch head SHA/tree after freeze; earlier green runs are historical only.

Finding closure requires refreshed independent review in a fresh Codex session/worktree. Code edits alone do not close `AUT-B-R1-IR-*` findings.

## Repair Cycle 2 finding → repair mapping

| Finding | Severity | Repair |
| --- | --- | --- |
| `AUT-B-R1-IR-01` | BLOCKING | Required-check currentness parses validated timestamps to numeric instants; malformed/contradictory/tied currentness → `INCONCLUSIVE` |
| `AUT-B-R1-IR-02` | MAJOR | Additive Stage-B delta `AUT-MS-ROOT-WORKSPACE-B-EXT` classifies `vitest.config.ts`; SR-002 references the delta, not the immutable G1 selector set |
| `AUT-B-R1-IR-03` | MAJOR | Live ruleset `conditions.ref_name` validated against Stage-B authority expectation (`~DEFAULT_BRANCH`, empty exclude) |
| `AUT-B-R1-IR-04` | OBSERVATION | Green shadow workflow means terminal `PASS` only; `FAILED` / `INCONCLUSIVE` / structural failure exit nonzero |
| `AUT-B-R1-IR-05` | MAJOR | Durable AUT-E03 reference/retention contract under `docs/evidence/aut001/`; artifact retains `evidence.json` + digest manifest for 90 days |

## Additive authority / material-surface delta

- `docs/routing/aut001_b_stage_authority_material_delta.json`
- binds immutable G2 + G1 package contract + G1 material-surface manifest
- classifies `vitest.config.ts` as shared/serialized `CI_EVALUATOR_MATERIAL`
- strengthens protected default-branch ruleset ref-condition expectation
- no G1 rewrite, no criteria weakening, no production/Phase-022 authority

## Preserved closed findings

- `AUT-B-IR-03` — semantic identity vs `observedAt`-only metadata
- `AUT-B-IR-04` — unknown/empty/null/case-variant action remains non-advancing

## AUT-C15 remain fail-closed

Head drift, base drift, required-set disagreement, malformed currentness ambiguity, unavailable mandatory truth, restart reconstruction conflict, unsafe lifecycle advancement, and wrong enforcement-scope ruleset remain blocking.

## Implemented boundary

AUT-001-B implements the read-only reconciliation substrate only. It introduces no GitHub write capability, no agent dispatch, no MCP action surface, no branch synchronization, no merge authority, and no production or Phase-022 authority.

## Verification / review boundary

Repository CI and retained live-shadow artifact evidence must qualify the exact Repair Cycle 2 candidate before independent review. Only a fresh independent `PASS` permits a separate fresh adversarial review.

Repair Cycle 2 completion does **not** complete AUT-001-B, grant B G5, mark PR #23 ready, merge, authorize AUT-001-C/F, Phase 022, release, or production.

Any further ordinary source repair requires explicit `HUMAN_PROGRAM_AUTHORITY` repair-budget extension.

# AUT-001-B — Live Read-Only Shadow & GitHub Reconciliation

**State:** IMPLEMENTATION CANDIDATE CREATED / VERIFICATION PENDING

## Candidate generation 1

- start-gate base: `f87f57fa42edd1ec81fc79626f6c93091793d71f`
- implementation branch: `aut-001/b-read-only-shadow`
- implementation commit: `4ed158a21d1584e604202a18eb83b8be5dbccb44`
- implementation tree: `a54fa669c29c48bf2eef4d7c6db2980ada4da40e`

## Implemented boundary

AUT-001-B implements the read-only reconciliation substrate only. It introduces no GitHub write capability, no agent dispatch, no MCP action surface, no branch synchronization, no merge authority, and no production or Phase-022 authority.

Implemented mechanics:

- immutable verified webhook-delivery journal with delivery-idempotency and conflicting-digest detection;
- append-only normalized GitHub semantic facts for PR head/state/merge, refs, checks and workflow runs;
- exact-head required-check evaluation with late/superseded evidence rejection and ambiguous-attempt fail-closed behavior;
- bounded read-only GitHub truth client interface exposing only PR/ref/check/workflow/ancestry reads;
- authoritative truth collection and identity reconciliation;
- head/base drift detection;
- deterministic reuse of AUT-001-A lifecycle projection;
- reconciled `github.check.required_set_pass` derivation only when exact candidate/base/current required-check truth permits it;
- no synthesis of human merge or other human-authority transitions;
- divergence recording with blocking unsafe-advancement treatment;
- merge-truth ancestry/identity reconciliation;
- restart reconstruction from append-only journal snapshots plus fresh authoritative reads;
- fail-closed handling when mandatory GitHub truth is unavailable;
- mandatory Stage-B scenario harness under canonical `tools/autonomy-control/test/` evaluator surface.

## Verification boundary

This record does not claim AUT-E03 live-shadow completion yet. Repository CI must first qualify this exact source candidate. A bounded live read-only shadow evidence window must then be recorded against an exact candidate generation before independent/adversarial review and B G5.

Any source repair creates a new candidate generation and invalidates affected exact-revision evidence.

# AUT-001-A — Control-Plane Substrate & Deterministic Replay Core

**State:** AUTHORIZED / REPAIR CYCLE 1 IN PROGRESS

## Purpose

Implement the non-side-effecting foundation of AUT-001: an isolated development-control tooling substrate, append-only fact model, deterministic lifecycle projection, revision/evidence classification, and an executable replay/failure harness grounded in the Phase-021 oracle.

## Scope

Writable implementation scope is `tools/autonomy-control/` plus test/evidence surfaces and only the minimum shared root configuration needed to include the new tooling in typecheck, lint, format, and test verification.

No GitHub mutation adapter, provider dispatch, MCP server, application behavior, production capability, Phase-022 execution, or 020-D bridge is included.

## Required evidence

- deterministic replay produces the same state and authority-stop result from the same immutable facts;
- executable-material, governance-material, evaluator-material, provenance-only, evidence-only, mixed and inconclusive revision cases classify conservatively;
- unknown, contradictory, stale, malformed or incomplete facts cannot optimistically advance lifecycle state;
- historical Phase-021 candidate generations remain distinct and are never silently relabeled;
- human authority stops require both an authority reference and the matching authority kind;
- duplicate fact identity is idempotent only for identical immutable contents; digest-label reuse cannot conceal conflicting payloads;
- Stage-A-owned failure cases execute through the actual fact store, lifecycle projection and/or revision classifier rather than an expected-value lookup.

## Failure-injection evidence boundary

Independent review of the first candidate identified an invalid evidence claim: AUT-001-A cannot honestly claim runtime execution of failure cases whose owning mechanisms do not exist until AUT-001-B through AUT-001-F.

The repaired Stage-A harness therefore partitions the canonical 28 R-G cases into:

1. `EXECUTABLE_IN_A` — the case can be exercised through Stage-A fact, lifecycle, evidence/materiality, or human-stop behavior and must produce an independently asserted disposition; and
2. `DEFERRED` — the case remains a mandatory downstream obligation with an explicit owning AUT stage, but AUT-001-A must not report it as an executable PASS.

This does **not** weaken AUT-001-G. Full operational qualification still requires executable coverage of the complete applicable failure matrix after the owning runtimes exist. The repair removes premature green evidence rather than removing a program obligation.

## Material-surface qualification

The G1 material-surface manifest remains the canonical package-level surface taxonomy. The first implementation candidate placed Stage-A core files directly under `tools/autonomy-control/src/` and tests under `tests/autonomy-control/`, while the pre-G2 selectors anticipated more granular future subdirectories. Until a reviewed selector/path qualification is recorded, those concrete Stage-A paths must be treated conservatively as executable/evaluator material; they may not be considered non-material merely because a selector does not match.

A path-to-surface qualification record for the Stage-A implementation is therefore part of repair cycle 1 and must itself receive authority-delta review because it concerns post-G2 material classification. It does not expand writable scope.

## Authority-reference limitation and repair

The first candidate only checked for a non-empty human authority reference. Repair cycle 1 additionally requires the event's authority kind to match the human-stop transition (`G2`, protected implementation merge, closure merge, reopen G2, or completion-validity disposition). Runtime validation against a repository-backed authority catalog remains a later ingest/integration responsibility; Stage A must still fail closed when the authority kind is absent or mismatched.

## Review boundary

The candidate must be frozen at an exact SHA, verified, independently reviewed in a read-only session, then adversarially challenged in a fresh session. Repairs create a new candidate generation.

The first independent review of `e30fcf8070f607c56fe14a4e3107e43f202d3b65` returned `CHANGES_REQUIRED`. Its evidence remains historical and must not be reused as a PASS for the repaired candidate.

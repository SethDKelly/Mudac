# AUT-001-A — Control-Plane Substrate & Deterministic Replay Core

**State:** AUTHORIZED / IN PROGRESS

## Purpose

Implement the non-side-effecting foundation of AUT-001: an isolated development-control tooling substrate, append-only fact model, deterministic lifecycle projection, revision/evidence classification, and an executable replay/failure harness grounded in the Phase-021 oracle.

## Scope

Writable implementation scope is `tools/autonomy-control/` plus test/evidence surfaces and only the minimum shared root configuration needed to include the new tooling in typecheck, lint, format, and test verification.

No GitHub mutation adapter, provider dispatch, MCP server, application behavior, production capability, Phase-022 execution, or 020-D bridge is included.

## Required evidence

- deterministic replay produces the same state and authority-stop result from the same immutable facts;
- executable-material, governance-material, provenance-only, evidence-only and inconclusive revision cases classify conservatively;
- unknown/contradictory/stale facts cannot optimistically advance lifecycle state;
- historical Phase-021 candidate generations remain distinct and are never silently relabeled;
- human authority stops remain represented in projected eligibility.

## Review boundary

The candidate must be frozen at an exact SHA, verified, independently reviewed in a read-only session, then adversarially challenged in a fresh session. Repairs create a new candidate generation.

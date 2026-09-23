---
type: Documentation Authority
title: Agentic Conformance, Drift Detection & CI Evidence Contract
description: Defines integrated repository-agent conformance, status-mirror derivation, generated/reference integrity, negative controls, narrow secret scanning, CI read-only behavior, evidence-class separation, provider-runtime limitations, and proportional enforcement before implementation.
status: stable
tags: [governance, conformance, ci, drift, status, references, negative-controls, secrets, agents]
sources:
  - resource: validation-enforcement.md
  - resource: agentic-authority-scope.md
  - resource: agent-workflow-portability.md
  - resource: deterministic-ownership-resolution.md
  - resource: ../../018-pre-implementation-repository-qualification-agentic-development-architecture-reentry/018-G-agent-skills-tool-adapters-workflow-contracts-cross-agent-portability.md
  - resource: ../../020-autonomous-implementation-program-design-verification-v1-delivery/020-C-cursor-codex-roles-work-isolation-context-provenance-autonomy-circuit-breakers.md
  - resource: ../../020-autonomous-implementation-program-design-verification-v1-delivery/020-D-nonproduction-environment-synthetic-data-observability-mcp-agent-test-control-plane-architecture.md
  - resource: ../../020-autonomous-implementation-program-design-verification-v1-delivery/020-F-implementation-phase-contract-visible-criteria-evidence-classes-hidden-evaluation-architecture.md
  - resource: ../../020-autonomous-implementation-program-design-verification-v1-delivery/020-G-ci-cd-security-supply-chain-exact-sha-verification-evidence-bundle-architecture.md
  - resource: ../../020-autonomous-implementation-program-design-verification-v1-delivery/020-H-independent-code-review-adversarial-review-repair-reopen-exit-gate-governance.md
  - resource: ../../020-autonomous-implementation-program-design-verification-v1-delivery/020-I-migration-recovery-accessibility-performance-cost-scenario-verification-design.md
  - resource: ../../020-autonomous-implementation-program-design-verification-v1-delivery/020-J-v1-scope-whole-system-completion-criteria-final-integration-hardening-phase-design.md
generated: { by: openai/gpt-5.6-sol, at: 2026-09-22T03:53:00Z }
---

# Purpose

Define how MUDAC proves that the repository knowledge, routing and agentic controls remain internally coherent before architecture selection or domain implementation.

<a id="cnf-001"></a>
## CNF-001 — Integrated Conformance Proves Repository Configuration Health, Not Domain/Runtime Health

The integrated conformance runner may prove documentation structure, routing, generated-artifact reproducibility, stable-reference integrity, agent-policy structure, workflow/adapters, context budgets, status mirrors, narrow credential guards and negative controls.

A PASS does not establish product runtime behavior, provider-agent obedience, deployment readiness, production readiness or domain implementation correctness.

<a id="cnf-002"></a>
## CNF-002 — Phase Program Indexes Own Phase Progression; Status Mirrors Are Derived

The Phase-018 index owns the Phase-018 progression and closure handoff.

Root README, docs README/index, AGENTS.md, canonical index, Phase-017 handoff and suspended Implementation index are mirrors.

While Phase 018 is active, the status validator derives its contiguous completed prefix and one NEXT subphase. After closure, it requires A–M COMPLETE plus the Phase-019 authorization handoff. No separate machine status file becomes lifecycle authority.

<a id="cnf-003"></a>
## CNF-003 — Generated Artifacts Must Be Exactly Reproducible From Authored Sources

Generated OKF projection, canonical owner inventory and stable-reference index must pass byte-for-byte regeneration checks.

Hand-edited generated output is a blocking drift defect.

<a id="cnf-004"></a>
## CNF-004 — Stable-Reference Integrity Is Fail-Closed and Role-Aware

Every registered stable ID must retain one valid authored owner/anchor and an explicit ownership role.

Current resolution must reject quarantined candidates unless candidate inclusion is explicit. Historical/provenance occurrences never compete with the owner.

<a id="cnf-005"></a>
## CNF-005 — Critical Guards Require Executable Negative Controls

For controls where a false-positive PASS would materially weaken authority or security boundaries, CI must include mutation-based negative tests showing the relevant validator fails when the protected contract is deliberately broken.

Current negative controls cover status-mirror drift, A1 edit-authority corruption, duplicate provider workflow source, generated OKF drift, stable-reference index drift, downstream-candidate adoption leakage, architecture pre-selection leakage, implementation-execution leakage, Phase-019 premature decision acceptance, Phase-020 implementation-authority leakage, recursive autonomous-delegation leakage, non-production MCP production-target leakage, implementation-package dependency-cycle leakage, protected-evaluator hidden-requirement leakage, exact-revision/evidence-contract weakening, review/reopen authority collapse, cross-cutting scenario/evidence erosion, v1 scope/final-integration authority expansion and high-confidence secret insertion.

<a id="cnf-006"></a>
## CNF-006 — Agent Workflow/Adapters Remain Subordinate Under Conformance

Conformance must verify that canonical workflows remain single-source, provider bridges remain thin, tool-runtime claims remain evidence-calibrated and no provider adapter creates independent semantic authority.

<a id="cnf-007"></a>
## CNF-007 — Secret Scanning Is Narrow, High-Confidence and Not a Substitute for Enterprise Scanning

Repository agentic/authority surfaces receive a deterministic high-confidence credential and forbidden-sensitive-filename scan.

The guard intentionally avoids broad PII heuristics and low-confidence entropy guessing that would turn documentation prose into unreliable failures.

Organization/provider secret scanning remains a separate operational control.

<a id="cnf-008"></a>
## CNF-008 — Knowledge CI Remains Read-Only Against Repository Authority

The knowledge/conformance workflow uses repository contents read permission and may mutate only ephemeral runner workspace for negative controls or reports.

CI does not commit fixes, regenerate-and-push artifacts, update status, merge or deploy.

<a id="cnf-009"></a>
## CNF-009 — Blocking Checks Cannot Be Silently Downgraded by Orchestration

The integrated runner reports each check independently and returns failure when any blocking check fails.

A runner/report formatting layer may not convert a validator failure into success.

<a id="cnf-010"></a>
## CNF-010 — Evidence Classes Remain Explicit

Repository/static conformance, executable unit/integration behavior, provider runtime verification, external/manual evidence and production evidence are distinct.

A stronger-sounding conclusion cannot be inferred from a weaker evidence class.

<a id="cnf-011"></a>
## CNF-011 — Provider Runtime Compatibility Remains Separate From Static Adapter Conformance

Static provider documentation plus adapter validation establishes repository configuration support only.

Codex, Cursor or Claude Code runtime discovery/obedience may be marked verified only after an actual runtime smoke event with recorded evidence.

Absence of that smoke evidence does not block repository agentic conformance when runtime verification is not required for the current phase.

<a id="cnf-012"></a>
## CNF-012 — Conformance Must Remain Proportional and Architecture-Neutral Before Re-entry

Phase-018 conformance may protect documentation/agentic authority, routing, references, secret hygiene and CI boundaries.

It must not prematurely enforce quarantined framework/database/cloud/source-topology decisions merely because historical implementation candidates exist.

Architecture-specific executable guards are introduced only after architecture decisions are accepted through downstream re-entry.

# Integrated command

Run the repository agentic/documentation suite with:

~~~bash
python scripts/run_agentic_conformance.py
~~~

Optional human-readable report:

~~~bash
python scripts/run_agentic_conformance.py --report agentic-conformance-report.md
~~~

The report is generated evidence and should not be committed by default unless a selected phase/package explicitly requires durable evidence.

---
type: Phase Qualification
title: 018-E — Agentic Development Authority, Human-Directed Scope, Change Classes & Safety Boundaries
description: "Establishes MUDAC's tool-neutral human-directed agentic development authority model, task-envelope rules, A1–A4 action classes, necessary-supporting-change limits, external/destructive action boundaries, semantic/architecture change routing, memory/tool subordination, completion rules, sensitive-data safeguards, and deterministic policy checks."
status: stable
tags: [phase-018, agentic-development, human-directed, authority, scope, action-class, safety, change-control]
sources:
  - resource: 018-D-canonical-ownership-stable-references-deterministic-resolution-drift-control-design.md
  - resource: ../canonical/governance/agentic-authority-scope.md
  - resource: ../canonical/governance/change-governance.md
  - resource: ../canonical/governance/design-implementation-boundary.md
  - resource: ../canonical/governance/post-concept-design-reentry.md
  - resource: ../routing/agentic_action_policy.json
  - resource: ../../AGENTS.md
  - resource: ../../scripts/validate_agentic_authority_policy.py
generated: { by: openai/gpt-5.6-sol, at: 2026-09-22T03:12:00Z }
---

# Purpose

018-E defines the authority and scope model for coding-agent work before MUDAC introduces tool-specific skills/adapters or begins domain implementation.

018-D answered: **Which authored authority applies?**

018-E answers: **Once that authority is known, what may an agent do, what requires explicit additional human authorization, and where must the agent stop?**

The result is deliberately tool-neutral and smaller than a complete agentic framework.

# 1. Governing model

MUDAC agentic development is now explicitly **human-directed**.

A human selects the task. Repository authority governs current meaning. The agent may execute bounded work inside the selected task, but does not become an autonomous work selector.

~~~text
human-selected task
  ↓
current canonical semantic/governance authority
  ↓
repository agent/change-control governance
  ↓
active accepted architecture/implementation package
  ↓
executable evidence
  ↓
reviewed external tool/vendor guidance
  ↓
agent memory / conversational assumptions
~~~

The human-selected task determines what work is being requested. It does not by itself silently change current MUDAC semantics.

# 2. Canonical authority contract

018-E adds docs/canonical/governance/agentic-authority-scope.md, owning AGT-001 through AGT-016.

The machine-readable projection is docs/routing/agentic_action_policy.json. The JSON policy is for conformance and adapter consumption; it is not semantic authority.

# 3. Task envelope

Every agent task is bounded by the requested objective, active Phase/subphase or selected package, directly owned artifacts, necessary supporting changes, required validation/evidence, directly impacted routing/status/reference/traceability surfaces, and explicit exclusions.

This gives agents enough discretion to finish real work without turning every supporting edit into another permission round-trip, while preventing that discretion from becoming open-ended backlog authority.

# 4. A1 — read / review / plan

A1 permits repository reading/search, stable-ID/current-owner resolution, safe read-only validation, and reporting findings. It does **not** authorize repository edits, external/destructive actions, or semantic/architecture adoption.

Finding a defect during review does not itself authorize changing it.

# 5. A2 — bounded change / build / fix

A2 authorizes directly necessary repository changes inside the selected task, including tests/fixtures, generated-routing refreshes, status/index/reference/traceability updates, accurate documentation, and safe non-destructive validation.

A2 excludes unrelated cleanup, speculative features, adjacent backlog work, automatic continuation into the next subphase/package, external/destructive actions, and silent semantic or architecture adoption.

# 6. Necessary supporting change test

A supporting change is in scope when omitting it would leave the selected task incomplete, inconsistent, unvalidated or misleading.

If a supporting change materially broadens authority, risk or review burden, it becomes scope expansion and therefore A3 rather than ordinary A2.

# 7. A3 — external / destructive / scope-expanding

A3 includes deployment/release/promotion, cloud or external resource mutation, destructive migrations/data/history operations, force-push/shared-history rewrite, unattended merge when not explicitly selected, secrets/sensitive-data privilege expansion, unrelated phase/package/feature selection, and recursive implementation delegation.

A3 requires explicit human authorization for the specific consequential action.

# 8. A4 — semantic / accepted-architecture change

A4 covers changes to accepted product/design meaning or, once present, accepted architecture.

An agent may identify conflicts, analyze alternatives and draft a change proposal, but may not silently adopt the change.

A4 requires explicit human change intent, canonical change/re-entry governance, stable-rule compatibility/dependent-impact review, lineage preservation, and downstream propagation/revalidation where affected.

# 9. Implementation difficulty rule

Implementation difficulty is evidence to investigate, not permission to weaken accepted semantics. The sequence is compliant realization → downstream architecture reassessment → better evidence/instrumentation when proof is the issue → governed architecture/change request if necessary.

# 10. Completion boundary

Completing the selected task authorizes reporting results, evidence, residual risk and the next eligible work. It does not authorize starting that next work automatically.

A successful CI run likewise does not authorize merge, deploy, the next Phase/subphase, or a new implementation package.

# 11. Tool neutrality

No coding agent is semantically privileged. Future Cursor, Codex, Claude Code or other adapters may specialize mechanics and ergonomics, but not semantic ownership, A1–A4 scope, architecture authority or evidence requirements.

# 12. Memory and external content

Agent memory, chat history, scratchpads, generated summaries, vendor documentation, retrieved external files/messages and tool output remain advisory context/evidence according to role, not repository authority by default.

# 13. Sensitive-data boundary

Agents must not commit credentials, production secrets/tokens or real sensitive personal/event data. Synthetic fixtures remain the default. Privilege expansion, real production-data access and secret exposure are A3 actions.

# 14. Deterministic conformance added

018-E adds scripts/validate_agentic_authority_policy.py.

The validator checks canonical contract linkage, authority precedence, exactly A1–A4, A1 no-edit behavior, A2 bounded-edit/non-external/non-semantic limits, A3 explicit authorization, A4 explicit human intent/change control, human-directed/no-autonomous-next-work rules, completion-stop rules, AGT-001 through AGT-016 presence, and AGENTS.md bootstrap exposure.

It intentionally does not attempt to infer from arbitrary future natural-language requests which class applies; that remains a reasoning responsibility.

# 15. Stable-reference and owner impact

018-E adds sixteen current stable governance IDs: AGT-001 through AGT-016.

~~~text
governed paths total             106
current-authority paths           83
downstream-candidate paths        15
historical adapters                6
external references                2

stable IDs total                 242
current-authority IDs            100
downstream-candidate IDs         142
AGT IDs                           16
~~~

# 16. Bootstrap adaptation

AGENTS.md now exposes a compact A1–A4 summary and routes to the canonical agentic authority owner. The summary remains subordinate.

# 17. Workflow drift repaired

018-E discovered a small workflow-trigger defect: push paths contained a duplicate knowledge/** entry, while pull-request paths omitted knowledge/**.

The trigger was normalized so generated OKF changes invoke knowledge validation on both pushes and pull requests without duplication.

# 18. Validation evidence

Initial 018-E mechanics commit: f7bd510e695cdf41aa94fad0ffddc6ca2c7cbfaa

Knowledge Validation run: 35682129123 — **SUCCESS**

~~~text
authored knowledge structure       PASS
generated OKF projection           PASS
generated owner inventory          PASS
generated stable-reference index   PASS
agentic authority policy           PASS
stable-ID role smoke tests         PASS
~~~

The policy validator proves machine-readable A1–A4 safety invariants. It does not prove every future agent invocation will reason correctly.

# 19. Relationship to later agentic phases

018-E intentionally does not create tool-specific skills/adapters, context-budget measurement, agent-conformance scenario suites, unattended orchestration or autonomous backlog processing.

~~~text
018-F  context / anti-bloat architecture
018-G  skills / adapters / workflow contracts
018-H  conformance / drift / CI enforcement
~~~

# 20. Gate evaluation

| Phase-018 gate | 018-E result |
| --- | --- |
| P18-G1 semantic preservation | PASS |
| P18-G2 current/history integrity | PASS |
| P18-G3 documentation economy | PASS |
| P18-G4 OKF qualification | PRESERVED |
| P18-G5 deterministic routing | PRESERVED |
| P18-G6 human-directed agent authority | **PASS** |
| P18-G7 context proportionality | PARTIAL — 018-F |
| P18-G8 conformance proportionality | PARTIAL PASS — broader scenario/tool conformance remains 018-H |
| P18-G10 architecture re-entry integrity | PASS |
| P18-G12 execution boundary | PASS |

# 21. Exit decision

**018-E — COMPLETE — PASS.**

~~~text
agentic development mode          HUMAN-DIRECTED
authority precedence              DEFINED
task envelope                     DEFINED
A1 review                         READ-ONLY BY DEFAULT
A2 bounded repository change      AUTHORIZED WITHIN SELECTED TASK
A3 consequential action           EXPLICIT HUMAN AUTHORIZATION REQUIRED
A4 semantic/architecture change   EXPLICIT HUMAN INTENT + CHANGE GOVERNANCE
autonomous next-work selection    NOT AUTHORIZED
unattended task queue             NOT AUTHORIZED
tool-specific semantic authority  NONE
feature implementation            NOT AUTHORIZED
~~~

The next authorized work is:

> **018-F — Agent Context, Progressive Retrieval, Context-Budget & Anti-Bloat Architecture**

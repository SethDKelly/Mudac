---
type: Phase Qualification
title: 018-H — Agentic Conformance, Knowledge Validation, Status Drift, Reference Integrity & CI Enforcement
description: "Integrates MUDAC's documentation and agentic validators into one read-only conformance runner; derives lifecycle mirror status from the Phase-018 authority; proves generated/reference integrity, role-aware stable resolution, portable workflow/adapters, bounded context, narrow credential hygiene and six mutation-based negative controls; and preserves provider-runtime verification as a bounded explicit carry-forward."
status: stable
tags: [phase-018, agentic-conformance, ci, status-drift, reference-integrity, negative-controls, secrets, validation]
sources:
  - resource: 018-G-agent-skills-tool-adapters-workflow-contracts-cross-agent-portability.md
  - resource: ../canonical/governance/agentic-conformance.md
  - resource: ../canonical/governance/validation-enforcement.md
  - resource: ../../scripts/run_agentic_conformance.py
  - resource: ../../scripts/validate_status_mirrors.py
  - resource: ../../scripts/validate_resolution_smoke.py
  - resource: ../../scripts/scan_agentic_secrets.py
  - resource: ../../scripts/test_agentic_conformance_guards.py
generated: { by: openai/gpt-5.6-sol, at: 2026-09-22T03:49:00Z }
---

# Purpose

018-H qualifies the Phase-018 documentation/agentic control plane as an integrated system.

Earlier subphases established individual mechanisms. This subphase asks whether those mechanisms remain coherent together, whether critical checks actually fail when violated, and whether CI can enforce them without acquiring semantic or repository-write authority.

# 1. Integrated conformance command

The repository now has one local/CI entry point:

~~~bash
python scripts/run_agentic_conformance.py
~~~

The runner executes the blocking repository/static checks and returns failure if any check fails.

An optional report may be created with:

~~~bash
python scripts/run_agentic_conformance.py --report agentic-conformance-report.md
~~~

The report is generated evidence and is not committed by default.

# 2. Integrated check set

At exit the runner covers:

1. authored knowledge structure and links;
2. generated OKF projection reproducibility;
3. generated owner inventory reproducibility;
4. generated stable-reference index reproducibility;
5. A1–A4 agentic authority policy;
6. context budgets;
7. portable skills/tool adapters;
8. Phase-018 status-mirror drift;
9. current versus downstream-candidate stable-resolution behavior;
10. narrow agentic/authority secret scan;
11. cross-cutting mutation-based negative controls.

The pre-existing stable-anchor, frontmatter, source-resource and workflow contracts remain part of the authored knowledge validator.

# 3. Status authority and drift

018-H does not introduce a machine-owned lifecycle status manifest.

Instead:

~~~text
Phase-018 index
  = subphase progression authority

README / docs index / AGENTS / canonical index /
Phase-017 handoff / suspended Implementation index
  = derived live mirrors
~~~

scripts/validate_status_mirrors.py derives the completed sequence and one NEXT subphase from the Phase-018 index, then requires every live mirror to contain the same compact state.

This satisfies OWN-012 without creating another authority plane.

# 4. Generated and reference integrity

Conformance requires byte-exact reproducibility for:

- knowledge/ OKF routing projection;
- docs/routing/canonical_owner_inventory.json;
- docs/routing/stable_reference_index.json.

Stable-reference behavior is additionally smoke-tested:

~~~text
INV-001
  → ordinary resolution succeeds as current-authority

ARCH-001
  → ordinary current resolution fails

ARCH-001 --include-candidates
  → succeeds explicitly as downstream-candidate
~~~

This proves role behavior rather than only JSON shape.

# 5. Negative controls

018-H adds six mutation-based guard tests.

Each creates an isolated temporary repository copy, deliberately violates one contract, and requires the real validator to return nonzero.

Current guards:

| Mutation | Expected detector |
| --- | --- |
| stale Phase-018 mirror | status mirror validator |
| A1 repository_edits changed to true | agentic authority validator |
| duplicate Claude workflow source | portable workflow validator |
| hand-edited knowledge/index.md | OKF projection generator/checker |
| altered stable-reference index | stable-index generator/checker |
| injected high-confidence GitHub-style token | agentic secret scanner |

A negative control passing unexpectedly fails the conformance suite.

# 6. Negative-control repair evidence

The first integrated 018-H run correctly failed one negative control.

Run:

> 35684494292 — FAIL

All positive repository checks passed, but the status-drift mutation changed only one of multiple identical next-state occurrences in AGENTS.md. Another correct occurrence remained, so the status validator still found valid current status.

That was a weakness in the **test mutation**, not in the repository status.

The mutation was strengthened to replace all matching current-next occurrences.

The subsequent integrated run passed all six mutations.

This repair is useful evidence that 018-H is testing guard effectiveness rather than merely checking that guard scripts execute.

# 7. Secret and sensitive-data boundary

018-H adds a narrow checked-in agentic/authority scanner.

It checks selected governance, routing, agent, generated-knowledge and Phase-018 surfaces for:

- private-key headers;
- high-confidence AWS/GitHub/OpenAI/Anthropic/Slack/Google credential patterns;
- non-placeholder structured secret fields in structured data;
- sensitive credential-file names such as private keys and secrets files.

It intentionally does not use broad PII inference or entropy heuristics.

Therefore:

> secret scan PASS is useful repository hygiene evidence, not a claim of complete enterprise DLP or secret management.

# 8. CI enforcement

Knowledge Validation now runs the same integrated command used locally.

The workflow remains:

~~~text
permissions:
  contents: read
~~~

It may mutate ephemeral temporary copies during negative tests but cannot commit repairs, advance status, merge or deploy.

This eliminates duplicated CI orchestration between individual checks and the local conformance workflow.

# 9. CI trigger coverage

The workflow triggers for changes to:

- AGENTS.md;
- CLAUDE.md;
- README.md;
- requirements-docs.txt;
- scripts/**;
- docs/**;
- knowledge/**;
- .agents/**;
- .cursor/**;
- .claude/**;
- the Knowledge Validation workflow itself.

Agentic/knowledge control-plane changes therefore receive the same integrated checks.

# 10. Canonical conformance rules

018-H adds:

> docs/canonical/governance/agentic-conformance.md

with CNF-001 through CNF-012.

The rules distinguish repository configuration health from runtime health, derive status mirrors, require generated reproducibility and role-aware references, require negative controls, preserve adapter subordination, bound secret scanning, keep CI read-only, prohibit orchestration downgrades, distinguish evidence classes, separate provider runtime verification and keep pre-reentry conformance architecture-neutral.

# 11. Stable-reference and owner impact

018-H adds one current Governance owner and twelve current CNF rules.

Current counts:

~~~text
governed documentation paths       108
current-authority paths             85
downstream-candidate paths          15
historical adapters                  6
external references                  2

stable IDs                         276
current-authority IDs              134
downstream-candidate IDs           142
CNF IDs                             12
~~~

No historical Architecture or Implementation candidate was activated.

# 12. Context effect

Despite the added conformance routing, all hard context budgets remain passing.

The bootstrap remains well within its envelope and the canonical run-conformance skill remains far below the skill limit.

The large stable-rule registry remains informationally above the owner review threshold but is still bypassed for known-ID lookup through the 018-D resolver.

# 13. Final validation evidence

Final mechanics commit before phase recording:

> 8cb037622fc3fc5cb87d91c146a44c2b15eeeb61

Knowledge Validation:

> run 35684525787 — **SUCCESS**

Evidence:

~~~text
Markdown files                         356
frontmatter blocks                     256
stable rule anchors                    276
knowledge errors                         0
knowledge warnings                       0

owner inventory                        PASS — 108 paths
stable-reference index                 PASS — 276 IDs
agentic authority policy               PASS
context budget                         PASS — 0 hard errors
portable skills/tool adapters          PASS — 7 skills / 3 tools
status mirror drift                    PASS
stable-resolution behavior             PASS
agentic/authority secret scan          PASS — 69 text files / 0 findings
negative controls                      PASS — 6 mutations
repository configuration conformance   PASS
~~~

# 14. Provider runtime carry-forward

The tool compatibility manifest still reports:

~~~text
Codex runtime       not-smoke-verified-by-repository
Cursor runtime      not-smoke-verified-by-repository
Claude Code runtime not-smoke-verified-by-repository
~~~

018-H does not manufacture runtime evidence.

This is a bounded compatibility evidence gap, not a semantic or repository-conformance blocker.

A later environment where the actual provider runtimes are available may record smoke evidence and update the manifest through the same evidence-calibrated governance.

# 15. Architecture-neutrality check

No Phase-018-H guard enforces historical:

- Fastify;
- PostgreSQL;
- Kysely;
- Cognito;
- AWS topology;
- modular-monolith choice;
- historical source-package structure;
- historical Phase-008 implementation sequence.

Those remain quarantined candidates for 018-J.

Conformance currently protects only the repository/documentation/agentic control plane that must exist before candidate evaluation.

# 16. 018-I handoff

The repository control plane is now sufficiently deterministic to move from **repository preparation risk** to **downstream engineering obligation/risk reconciliation**.

018-I should:

1. consume CF-01 through CF-04 from Phase 017;
2. inventory all remaining downstream realization obligations;
3. distinguish product-semantic obligation from engineering uncertainty;
4. identify evidence expected before architecture selection or implementation;
5. define revisit triggers and owners;
6. include bounded tooling/runtime compatibility concerns where they affect engineering workflow;
7. avoid prematurely selecting solutions that belong in 018-J/K.

# 17. Gate evaluation

| Phase-018 gate | 018-H result |
| --- | --- |
| P18-G1 semantic preservation | PASS |
| P18-G2 current/history integrity | PASS |
| P18-G3 documentation economy | PASS |
| P18-G4 OKF qualification | PRESERVED |
| P18-G5 deterministic routing | PASS |
| P18-G6 human-directed agent authority | PASS |
| P18-G7 context proportionality | PASS |
| P18-G8 conformance proportionality | **PASS** |
| P18-G9 status/reference integrity | **PASS** |
| P18-G10 architecture re-entry integrity | PASS |
| P18-G12 execution boundary | PASS |

# 18. Exit decision

**018-H — COMPLETE — PASS WITH BOUNDED PROVIDER-RUNTIME VERIFICATION CARRY-FORWARD.**

At exit:

~~~text
integrated conformance runner        ACTIVE
status-mirror derivation             ACTIVE
generated artifact drift checks      ACTIVE
stable-reference role checks         ACTIVE
agent authority checks               ACTIVE
portable workflow/adapter checks     ACTIVE
context budgets                      ACTIVE
narrow secret scan                   ACTIVE
mutation negative controls           ACTIVE — 6
CI repository permissions            READ-ONLY
provider runtime smoke evidence      BOUNDED CARRY-FORWARD
architecture-specific enforcement    NOT INTRODUCED
domain implementation                NOT AUTHORIZED
~~~

The next authorized work is:

> **018-I — Downstream Realization Obligation, Carry-Forward & Engineering-Risk Reconciliation**

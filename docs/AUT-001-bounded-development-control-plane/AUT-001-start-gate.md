# AUT-001 Start Gate — Bounded Development-Control Plane Implementation

**Package:** AUT-001  
**Decision:** PASS — READY FOR G2 DECISION  
**G1:** READY_FOR_AUTHORIZATION  
**G2:** NOT AUTHORIZED  
**Implementation execution:** NOT AUTHORIZED  
**Phase 022:** NEXT ELIGIBLE / NOT AUTHORIZED  
**Release / production:** NOT AUTHORIZED

## 1. Entry authority and baseline

AUT-001 is the implementation boundary recommended by the completed Phase-021-R autonomy-hardening retrospective. R-G validated the R-B through R-F control-plane design against the real Phase-021 history and adversarial contract cases, but explicitly did **not** implement the runtime or create execution authority.

The exact start-gate baseline is:

- protected `main`: `29637b92047047f7c1e3a08ff377f4ca68a2997a`
- protected `main` tree: `4878dcfa09540033d2f51d88ef93b1d460a2fe29`
- R-G authority/handoff: `1dd32506baf692549ffb435b1893e7fc76feaff3`
- R-G tree: `badbb48be7df2dfbe2c0513a5bb4a2495aab7d0a`
- planning branch: `aut-001/start-gate`
- active ruleset: `main — protected`
- required checks:
  - Validate agentic/documentation conformance
  - Implementation Verification
  - CodeQL JavaScript/TypeScript
- bypass actors: none

Authoritative machine package contract:

- `docs/routing/aut001_implementation_package_contract.json`
- `docs/routing/aut001_material_surface_manifest.json`
- `docs/routing/aut001_start_gate.json`

## 2. Package purpose

AUT-001 implements the coordination machinery designed in R-B through R-F so that future implementation work can be mechanically routed, replayed, reconciled and audited without giving automation additional semantic or program authority.

AUT-001 is infrastructure for the development process. It is **not** a sixth MUDAC semantic owner and must not be placed inside the application/domain ownership model.

The preferred isolated source boundary is:

`tools/autonomy-control/`

Application/domain packages are read-only by default and are outside AUT-001 implementation scope.

## 3. Non-negotiable authority boundary

AUT-001 may implement mechanics for:

- lifecycle projection;
- evidence dependency/invalidation;
- agent dispatch;
- GitHub reconciliation;
- development-control MCP query/record operations;
- carefully bounded non-human coordination actions;
- nonproduction test-control evidence composition.

AUT-001 may **not** create or exercise authority for:

- G2;
- material scope expansion;
- architecture or semantic acceptance;
- repair-budget override;
- protected implementation merge;
- closure merge where required;
- reopen execution;
- release;
- production;
- Phase-022 or any next-phase authorization.

Those remain human/program authority stops.

## 4. Logical implementation sequence

### AUT-001-A — Control-Plane Substrate & Deterministic Replay Core

Create the isolated tool substrate, append-only facts/operations, deterministic R-B state projection, R-C revision/evidence engine, and executable Phase-021 historical replay/failure harness.

External side effects are forbidden.

### AUT-001-B — Live Read-Only Shadow & GitHub Reconciliation

Consume real GitHub repository truth and webhook/check/workflow notifications in a read-only shadow. Compare projected state/next action against authoritative human/repository truth and record every divergence.

No GitHub writes and no agent dispatch.

### AUT-001-C — Dispatcher, Provider Adapters, Isolation & Provenance

Implement R-D dispatch, immutable context/provenance manifests, serialized-surface reservations and provider adapters for Cursor and Codex.

Provider mechanics must be qualified before use. Missing provider functionality may block the stage; it may not be replaced by an authority-expanding generic shell escape.

### AUT-001-D — Development-Control MCP Query/Record & Authorization Boundary

Implement MCP QUERY and RECORD_COMPUTE capabilities, resource-bound authentication/authorization, schema validation and audit envelopes.

No bounded side-effecting MCP actions are enabled yet.

### AUT-001-E — Bounded Non-Human Side Effects

Progressively enable only declared bounded actions such as isolated worktree creation, authorized agent dispatch, draft-PR coordination, declared ready/draft transitions, dependency branch synchronization and serialized-surface reservations.

Every consequential action requires operation identity, optimistic expected-state preconditions, reconciliation and circuit-breaker enforcement.

Protected merge, release, production, G2, scope expansion and next-phase authority remain structurally absent.

### AUT-001-F — 020-D Test-Control Evidence Bridge

Compose development control with the independently authorized 020-D nonproduction test-control runtime through declared evidence requests and evidence references.

This stage is currently **dependency blocked** because the 020-D runtime is designed but not yet independently implemented and accepted. That dependency may not be bypassed.

### AUT-001-G — Independent Exit, Shadow Qualification & Enablement Recommendation

Run exact-candidate verification, executable historical replay, runtime failure injection, independent security review, fresh code review, fresh adversarial review, shadow-divergence review and G5.

G5 may recommend operational enablement. It may not enable itself or authorize Phase 022.

## 5. Acceptance profiles

AUT-001 deliberately separates core coordination from the future test-control composition dependency.

### CORE_COORDINATION

Requires A through E plus the core portion of G.

It can become eligible for a **separate human operational-enablement decision**. Even after such acceptance, using it to coordinate Phase 022 still requires a separate Phase-022 G2.

### FULL_COMPOSED

Adds F plus full-composed G evidence after the 020-D runtime is independently operational and authorized.

This profile enables only the nonproduction evidence bridge. It does not create production test-control capability.

## 6. Visible acceptance model

Fifteen visible success criteria are frozen in the package contract. They cover:

1. deterministic lifecycle replay;
2. fail-closed ambiguity/stale-event handling;
3. exact-revision evidence dependency and invalidation;
4. dispatch role/session isolation and provenance;
5. GitHub reconciliation/idempotency/exact-head CI;
6. absence of generic capability escape;
7. structural production denial;
8. resource-bound remote authentication/authorization;
9. staged bounded side effects and optimistic preconditions;
10. 020-D bridge nonproduction/independent-authorization semantics;
11. restart, missed-event and recovery behavior;
12. preservation of human authority stops;
13. Cursor/Codex adapter equivalence under the R-D contract;
14. safe disablement and human-coordinated fallback;
15. shadow divergence visibility, with any unsafe optimistic advancement treated as blocking.

The material-surface manifest maps these criteria and evidence obligations to concrete new control-plane source/evaluator/governance boundaries before G2. Unmapped or ambiguous changes fail inconclusive rather than inheriting acceptance.

## 7. Evidence floor

Required evidence includes:

- deterministic executable replay of the historical Phase-021 oracle and R-G failure cases;
- adversarial fail-closed/invalidation/reopen scenarios;
- live read-only GitHub shadow evidence;
- Cursor and Codex adapter conformance evidence;
- MCP authorization, generic-escape and production-denial abuse testing;
- bounded-action idempotency/precondition/security evidence;
- 020-D bridge evidence once its external dependency exists;
- restart/recovery/disablement evidence;
- fresh independent and adversarial exact-candidate review.

No E7 production evidence is required or permitted for AUT-001 acceptance.

## 8. Provider/role operating model

The preferred execution pattern alternates Cursor and Codex between implementation and independent review across subphases. This improves review diversity without making provider identity an authority primitive.

Typical pairing:

- A — Codex implement / Cursor independent review;
- B — Cursor implement / Codex independent review;
- C — Codex implement / Cursor independent review;
- D — Cursor implement / Codex independent review;
- E — Codex implement / Cursor independent review;
- F — Cursor implement / Codex independent review.

Every adversarial review still requires a fresh, isolated session. A reviewer cannot repair the candidate while remaining Reviewer. A repair produces a new candidate generation and refreshes affected evidence/reviews.

## 9. Repair and escalation

Default package repair budget:

- maximum ordinary repair cycles per subphase before explicit human/program disposition: 2;
- repeated identical mandatory-failure threshold: 2;
- source-changing repair creates a new candidate generation;
- affected evidence and reviews must refresh;
- scope expansion is never an ordinary repair;
- production access, authority-boundary expansion, or semantic/architecture contradiction is an immediate blocker/re-entry condition.

## 10. Rollback and human fallback

AUT-001 must always be safely disableable.

The rollback path is:

1. disable side-effecting adapters/MCP bounded actions;
2. drain/reconcile any in-flight operation and serialized-surface reservation;
3. retain append-only facts, failures, evidence and provenance;
4. reconcile repository/external truth;
5. return coordination to the existing human-driven process.

No application/domain rollback is required merely because the control plane is disabled.

## 11. Start-gate findings

Three implementation risks remain visible but do not block G1:

1. **020-D runtime dependency.** This blocks AUT-001-F and FULL_COMPOSED acceptance, not A-E/Core qualification.
2. **Provider mechanics qualification.** Cursor/Codex runtime invocation and session identity must be proven during C; generic fallback is forbidden.
3. **Remote security realization.** The identity-provider choice and exact GitHub App permission matrix remain implementation decisions, but least privilege/resource binding and production denial are acceptance requirements rather than optional design preferences.

## 12. Start-gate decision

AUT-001 satisfies the package G1 contract:

- exact baseline known;
- R-G handoff valid;
- scope and exclusions explicit;
- control-plane/domain boundary explicit;
- seven-subphase dependency graph explicit;
- material surfaces defined before G2;
- provider and review roles explicit;
- visible criteria instantiated;
- evidence obligations instantiated;
- nonproduction environments and external actions bounded;
- circuit breakers explicit;
- repair budget explicit;
- rollback/human fallback explicit;
- residual implementation risks explicit;
- exit/G5 predicates explicit.

Therefore:

> **AUT-001 START GATE — PASS / READY FOR G2 DECISION**

**This record does not grant G2 or authorize implementation.**

The recommended initial G2 envelope, if explicitly approved by human/program authority, is **AUT-001-A through AUT-001-E plus AUT-001-G CORE qualification**. AUT-001-F / FULL_COMPOSED remains deferred until the independent 020-D runtime dependency is satisfied.

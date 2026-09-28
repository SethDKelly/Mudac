# 021-R-F — Development-Control MCP Interfaces, Authorization, Production Denial & Test-Control Composition

## Status

**COMPLETE — PASS.**

021-R-F defines the capability/API boundary through which an autonomy implementation may expose the R-B orchestrator, R-C evidence graph, R-D dispatcher, and R-E GitHub reconciler to agents and deterministic tooling without converting tool possession into semantic authority.

It is a design/governance contract only. No MCP server is implemented or deployed by this subphase. Phase 022, runtime autonomy implementation, release, production, and provider deployment remain unauthorized.

Machine projection: `docs/routing/autonomy_development_control_mcp_contract.json`.

## Governing distinction

MUDAC now has two intentionally separate control-plane concepts:

1. **Development-control MCP** — coordinates implementation lifecycle, dispatch, evidence, GitHub reconciliation and bounded development actions.
2. **020-D application test-control MCP** — exercises real non-production MUDAC behavior through environment, fixture, action, browser, observation and fault capabilities.

They may compose, but they are not one authority plane.

```text
implementation lifecycle                         application behavior
------------------------                         --------------------
R-B state / R-C evidence                         020-D environment registry
R-D dispatch / provenance         compose         fixture / action / browser
R-E GitHub reconciliation       <-------->        observe / fault
        |                                             |
        v                                             v
Development-Control MCP                         Test-Control MCP
        |                                             |
        +------------------ evidence refs ------------+
```

The development-control plane may request or correlate a declared test-control run only when an authorized evidence obligation requires it. It may not bypass the 020-D environment, capability, actor, or production-denial rules.

## Core rule

> **MCP capability is an interface to already-resolved authority; it never creates authority.**

A caller may possess a tool and still be forbidden to invoke it for the current phase/package/revision/state.

Authorization is evaluated from:

- authenticated technical principal;
- requested MCP capability;
- current R-B lifecycle state;
- active authority/G2 record where applicable;
- exact revision identity;
- R-D role/dispatch identity;
- R-E operation preconditions for GitHub writes;
- environment/evidence envelope for test-control composition.

No tool call may infer or synthesize missing G2, merge, release, production, reopen or next-phase authority.

## API design principles

1. **Capability-based, not shell-based.** Tools represent narrow lifecycle operations and queries.
2. **Read/compute/action are distinct privilege classes.** A caller that can inspect state does not thereby gain mutation authority.
3. **Every consequential write is preconditioned and idempotent.**
4. **Exact revision and authority bindings travel with consequential requests.**
5. **Production is denied structurally, not by naming convention.**
6. **Secrets are referenced through separately authorized principals/resources, never returned as tool results.**
7. **Application semantic actions stay in the 020-D test-control plane.**
8. **Development-control tools do not become an alternate Git, GitHub, shell, SQL, cloud or browser interface.**
9. **Human-only transitions remain human-only even if a technically callable endpoint could be imagined.**
10. **All consequential requests/results are provenance/evidence-graph ingestible.**

## Capability classes

### Query capabilities

Read-only capabilities project existing facts. Representative tools:

- `implementation.get_state`
- `implementation.get_authority`
- `implementation.get_candidate`
- `implementation.get_evidence_status`
- `implementation.get_invalidated_evidence`
- `implementation.get_merge_eligibility`
- `implementation.get_next_action`
- `implementation.get_pr_reconciliation`
- `implementation.get_dispatch_status`
- `implementation.get_serialized_surface_reservations`

Query tools:

- never mutate repository/GitHub/environment state;
- return explicit exact revision/currentness metadata;
- distinguish unknown/inconclusive from false;
- do not expose hidden evaluator material, credentials, tokens or private model reasoning.

### Record/compute capabilities

These add immutable technical facts or deterministic projections but do not themselves perform external development mutations.

Representative tools:

- `implementation.register_candidate`
- `implementation.record_verification`
- `implementation.record_review`
- `implementation.record_dispatch_provenance`
- `implementation.classify_delta`
- `implementation.compute_reverification_plan`
- `implementation.prepare_g5`
- `implementation.record_integration`
- `implementation.record_closure`
- `implementation.reconcile_github`

The important boundary is that a `record_*` call cannot fabricate the underlying event/evidence. The request must reference verifiable source identities such as candidate SHA/tree, provider run, review record, workflow/check run, GitHub fact or content-addressed manifest.

`prepare_g5` may assemble and validate the gate input set; it may not turn missing mandatory evidence into PASS or grant merge/next-phase authority.

### Bounded action capabilities

These are potentially mutating development operations and require the strongest preconditions.

Representative tools:

- `implementation.create_worktree`
- `implementation.dispatch_agent`
- `implementation.open_or_update_draft_pr`
- `implementation.mark_pr_ready_or_draft`
- `implementation.synchronize_dependency_branch`
- `implementation.reserve_serialized_surface`
- `implementation.release_serialized_surface`
- `implementation.request_test_control_run`

Every bounded action requires:

- explicit capability grant for the technical principal;
- current authority/role eligibility;
- exact expected lifecycle state;
- exact expected subject revision where applicable;
- idempotent operation ID;
- optimistic preconditions for external writes;
- circuit-breaker evaluation;
- provenance result.

No generic `run_command`, `git`, `github_api`, `http`, `sql`, `aws`, `browser_eval`, `read_secret`, `merge`, `deploy` or equivalent catch-all capability is allowed.

## Human-authority capabilities are forbidden

The following tool classes are intentionally absent, not merely disabled by default:

- `implementation.grant_g2`
- `implementation.expand_scope`
- `implementation.accept_architecture_change`
- `implementation.override_repair_budget`
- `implementation.approve_merge`
- `implementation.merge_protected_implementation`
- `implementation.authorize_reopen_execution`
- `implementation.authorize_release`
- `implementation.authorize_production`
- `implementation.authorize_next_phase`

Human/program authority may create immutable authority records through the repository/program process, and the control plane may observe those records. It cannot manufacture them through an agent-callable MCP tool.

## Principal and role model

R-F distinguishes:

- **human/program authority principal** — outside agent role, source of consequential authorization records;
- **orchestrator service principal** — computes state/eligibility and routes bounded operations;
- **dispatcher principal** — starts agent runs only from eligible R-B actions;
- **agent/provider principal** — executes one R-D role-bound dispatch;
- **verifier/evaluator principal** — produces evidence for exact revisions;
- **GitHub adapter principal** — narrow repository/PR/check reconciliation and explicitly authorized coordination writes;
- **test-control principal** — 020-D non-production application testing only.

A single deployed service may technically host more than one adapter later, but authority scopes remain logically and audibly distinct.

## Authorization decision

Every consequential request evaluates a machine-readable authorization tuple:

```text
principal
+ capability
+ role / dispatch identity
+ phase/package/work-unit
+ exact subject SHA/tree
+ expected R-B state
+ authority digest
+ material/evidence scope
+ external-action envelope
+ environment class when applicable
= ALLOW | DENY | BLOCKED | INCONCLUSIVE
```

`ALLOW` means the already-existing authority permits this bounded operation. It is not a new authority record.

Known prohibition yields `DENY` or `BLOCKED` depending on whether the request violates authority or an active circuit breaker. Missing/ambiguous required truth yields `INCONCLUSIVE`.

## Token/resource boundary

If the future MCP server is remote, every consequential capability requires authenticated resource-bound authorization.

Minimum validation:

- issuer;
- signature/key validity;
- expiration;
- audience/resource bound specifically to the development-control plane;
- principal identity;
- capability/scope;
- optional dispatch/run binding for agent-scoped credentials.

Credential passthrough is forbidden.

A GitHub token, test-control token, cloud token, or user identity intended for another resource cannot be accepted merely because the same actor ultimately controls it.

Short-lived, task/resource-bound credentials are preferred. Exact identity-provider realization is deferred to implementation design.

## Proposed logical scopes

A future implementation may map capabilities to scopes such as:

```text
impl.read
impl.record
impl.dispatch
impl.workspace
impl.github.read
impl.github.coordinate
impl.evidence
impl.test.request
```

No `impl.authority`, `impl.merge`, `impl.release`, `impl.production` or similarly broad human-authority scope is defined.

Scopes alone are insufficient; state/authority/revision guards still apply server-side.

## Production denial

The development-control plane is not a production-control plane.

It must not expose:

- production application actions;
- production database access;
- production browser/session control;
- production cloud mutation;
- production deployment/release action;
- production secrets;
- production test-control composition;
- production fault injection.

Production denial is enforced through capability absence plus environment/resource checks.

If a future deployment needs to observe a production-derived public release identity or GitHub release metadata, that is a separately governed read boundary and cannot become a production mutation path.

Completion of R-F does not authorize such deployment.

## Relationship to GitHub

Development-control MCP consumes the R-E adapter rather than exposing raw GitHub API access.

Examples:

```text
implementation.get_pr_reconciliation
        -> R-E reconciler read

implementation.open_or_update_draft_pr
        -> R-E idempotent operation with expected-head precondition

implementation.synchronize_dependency_branch
        -> R-E authorized coordination operation
        -> new head registered
        -> R-C classification required
```

The MCP layer cannot bypass R-E optimistic concurrency or idempotency by issuing raw GitHub writes.

`implementation.get_merge_eligibility` reports whether machine guards are satisfied; it does not perform or approve a merge.

## Relationship to agent dispatch

`implementation.dispatch_agent` is a façade over R-D.

It requires an already-computed eligible next action and creates exactly one immutable dispatch packet.

The request cannot:

- choose a broader role;
- widen writable surfaces;
- add undeclared external actions;
- reuse a stale authority digest;
- convert review to repair;
- skip required reviewer freshness;
- silently take a serialized surface reservation.

Provider/session/run output returns through R-D provenance and becomes R-C evidence/facts only after validation.

## Relationship to evidence and G5

The MCP surface may help query and assemble evidence, but R-C/020-H remain authoritative for validity and exit decisions.

`implementation.prepare_g5` returns a structured gate-preparation object containing:

- candidate SHA/tree;
- criteria/evidence mapping;
- current verification nodes;
- independent/adversarial review status;
- required CI status;
- invalidated/stale evidence;
- residual risks/findings;
- unresolved circuit breakers;
- exact authority references.

It may return `READY_FOR_GATEKEEPER_EVALUATION`, `NOT_READY`, `BLOCKED` or `INCONCLUSIVE`.

It cannot return a fabricated G5 PASS or create human merge authority.

## Composition with 020-D test-control MCP

The development-control plane does not reproduce application test tools.

`implementation.request_test_control_run` accepts only a **declared evidence request**, for example:

- environment tier (`NPT-L`, `NPT-P`, `NPT-S`);
- registered test/evidence profile;
- exact application release/candidate identity;
- fixture blueprint references;
- synthetic actor references;
- named action/browser/observe/fault capabilities required;
- evidence obligation refs;
- allowed duration/resource envelope.

It then requests execution through the 020-D test-control plane.

The development-control caller may not supply:

- arbitrary target URL;
- arbitrary SQL;
- arbitrary HTTP;
- arbitrary shell;
- arbitrary AWS/cloud command;
- arbitrary browser JavaScript;
- production environment selector;
- secret value.

020-D independently rechecks its own technical-principal, environment registry, capability and production-denial rules. Development-control authorization cannot override them.

Likewise, successful 020-D application behavior evidence cannot grant implementation lifecycle authority.

## Evidence result bridge

A composed test-control result must return a bounded evidence reference containing at least:

- development `operation_id`;
- evidence request/profile ID;
- test-control `test_run_id`;
- environment ID/class;
- exact release/build SHA;
- capability/profile versions;
- result class;
- trace/correlation handles;
- cleanup/fault status when relevant;
- artifact/evidence digests;
- evidence-class claim supported;
- provenance identity.

The development-control plane records a reference/digest into R-C; it does not rewrite application telemetry as implementation authority.

## Evidence-class discipline

Composition preserves 020-D’s evidence boundary:

- non-production test control may support E2–E5 and selected E6 when the material boundary is actually exercised;
- fixture seeding proves setup, not the user/application command that would normally create that state;
- test-control output cannot create E7 production evidence;
- hidden evaluator inputs may stay hidden, but requirements/evidence obligations remain visible.

## Environment and fault safety

For NPT-P/NPT-S operations, the development-control request may identify the evidence need but may not bypass environment leasing/serialization.

Privileged fault profiles retain their separate environment/A3-style authority needs from 020-D. Ordinary implementer dispatch cannot escalate to privileged infrastructure faulting because an MCP method exists.

Unresolved fault/cleanup state produces `BLOCKED` or `INCONCLUSIVE` rather than returning a shared environment to service automatically.

## Tool request envelope

Every consequential tool request includes or resolves:

- request/operation ID;
- caller principal;
- capability;
- phase/package/work unit;
- role/dispatch/run identity where applicable;
- expected R-B state;
- exact SHA/tree subject;
- authority refs/digest;
- evidence/material-surface refs;
- expected external subject state for mutating operations;
- idempotency key;
- requested result/evidence class;
- request digest.

## Tool result envelope

Every result contains:

- operation ID;
- server/control-plane revision;
- decision (`ALLOW`/`DENY`/`BLOCKED`/`INCONCLUSIVE` as applicable);
- result/disposition;
- exact subject SHA/tree/currentness;
- authority digest observed;
- immutable fact/evidence/provenance refs created;
- external result identity where applicable;
- side-effect status;
- retryability classification;
- bounded diagnostics;
- result digest.

A bare `ok` is insufficient for consequential operations.

## Idempotency and concurrency

MCP does not introduce a second retry model.

It reuses R-D/R-E semantics:

- same operation ID + same request digest after success -> idempotent result/retrieval;
- same operation ID + conflicting digest -> `INCONCLUSIVE`;
- expected-head/state mismatch -> reconciliation, no force overwrite;
- transport retry does not erase failed attempt history;
- mandatory evidence retry-until-green remains forbidden.

Serialized surface reservations are explicit resources, not implicit locks hidden inside an agent session.

## Error model

R-F defines stable classes suitable for agents and deterministic clients:

- `AUTHORITY_DENIED`
- `ROLE_NOT_ELIGIBLE`
- `STATE_MISMATCH`
- `REVISION_MISMATCH`
- `AUTHORITY_DIGEST_STALE`
- `CAPABILITY_NOT_GRANTED`
- `HUMAN_AUTHORITY_REQUIRED`
- `PRODUCTION_TARGET_FORBIDDEN`
- `SECRET_OR_PROTECTED_DATA_FORBIDDEN`
- `SERIALIZED_SURFACE_CONFLICT`
- `SIDE_EFFECT_PRECONDITION_FAILED`
- `EVIDENCE_MISSING_OR_INVALIDATED`
- `TEST_CONTROL_ENVIRONMENT_INELIGIBLE`
- `TEST_CONTROL_CAPABILITY_DENIED`
- `TEST_CONTROL_CLEANUP_UNRESOLVED`
- `EXTERNAL_SYSTEM_UNAVAILABLE`
- `INCONCLUSIVE_RECONCILIATION_REQUIRED`
- `UNSUPPORTED_CAPABILITY`

Errors distinguish retryable transport/infrastructure failures from non-retryable authority/scope violations.

## Security boundary

The future server must provide:

- least-privilege resource scopes;
- task/dispatch-bound authorization where useful;
- auditable principal/action/result identity;
- explicit allowlist tool registration;
- server-side schema validation;
- request/result size limits;
- time/resource bounds for expensive actions;
- redaction of credentials/tokens/session cookies;
- protected-evaluator output separation;
- no arbitrary filesystem, process, network or cloud escape;
- no tool-generated authority records.

Tool descriptions and model instructions are not security boundaries.

## Audit/provenance

Every consequential tool request/result becomes append-only technical provenance linked to:

- principal;
- dispatch/run when applicable;
- exact revision;
- authority digest;
- lifecycle state;
- operation ID;
- external GitHub/test-control identity;
- generated evidence/fact IDs.

Private chain-of-thought and full provider conversation transcripts remain excluded.

## Deployment topology remains deferred

R-F defines interfaces, not runtime placement.

Later implementation may choose a local process, repository service, CI-hosted component or bounded remote service, provided the same authorization and production-denial contract holds.

A single server process may host multiple capability adapters, but logical principal/scope and control-plane separation must remain auditable.

## Shadow-mode requirement

Before any development-control MCP may route live implementation actions, R-G must replay Phase 021 and failure-injection cases in shadow mode.

At minimum R-G must prove:

1. query tools never mutate state;
2. human-authority tool attempts are absent/rejected;
3. stale SHA/authority requests fail closed;
4. duplicate operations are idempotent;
5. conflicting operation reuse becomes inconclusive;
6. GitHub precondition drift prevents overwrite;
7. production target requests are denied structurally;
8. raw shell/SQL/cloud/HTTP/browser-eval/secret capabilities do not exist;
9. a composed NPT-L test request produces a bounded evidence reference without bypassing 020-D;
10. a production or ineligible test-control target is rejected by both planes;
11. test-control PASS does not advance lifecycle without R-B/R-C guards;
12. no MCP result authorizes Phase 022.

## Exit review

R-F closes PASS because:

1. development-control and application test-control responsibilities are separate;
2. a capability taxonomy exists for query, record/compute and bounded action tools;
3. human-authority operations are intentionally absent from the agent-callable tool surface;
4. principal/resource/capability/state/revision authorization is explicit;
5. production denial is structural and composes with 020-D production denial;
6. GitHub actions route through R-E rather than raw API access;
7. agent dispatch routes through R-D rather than provider-specific authority;
8. evidence/G5 handling preserves R-C/020-H validity rules;
9. test-control composition preserves environment, actor, capability and evidence-class boundaries;
10. idempotency, optimistic concurrency, error classes and provenance are defined; and
11. R-G has a concrete shadow/failure-injection oracle before any live runtime recommendation.

## Handoff

**021-R-G — Shadow Replay, Failure Injection, Exit Review & Autonomy Implementation Recommendation** is next eligible.

R-G should validate R-B through R-F against the actual Phase-021 sequence, adversarial failure cases and authority-denial cases, then decide what bounded autonomy implementation package—if any—should be recommended before Phase 022. R-F completion does not itself authorize that implementation or Phase 022.
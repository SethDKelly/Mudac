# 021-R-D — Agent Dispatcher, Role Identity, Session Isolation, Context Generation & Provenance Manifests

## Status

**COMPLETE — PASS.**

021-R-D defines how the R-B orchestrator and R-C evidence graph may dispatch bounded work to Cursor, Codex, or a future provider without granting that provider independent scope or semantic authority.

It is a design/governance contract only. Runtime autonomy implementation, Phase 022 execution, merge, release, production, and provider deployment remain unauthorized.

Machine projection: `docs/routing/autonomy_agent_dispatch_contract.json`.

## Governing rules retained

R-D specializes existing governance rather than replacing it:

- human-selected/G2-authorized scope bounds agent execution;
- Coordinator delegation is limited to declared work units and one level of delegation;
- provider identity does not create semantic privilege;
- implementation uses isolated writable worktrees from exact bases;
- reviewers are independent runs and read-only by default;
- context retrieval follows minimum-sufficient progressive disclosure;
- provenance records technical facts, not private model reasoning;
- secrets, protected probes, production targets, and undeclared external actions remain outside ordinary dispatch.

## Design objective

A dispatcher must deterministically answer:

1. which role is eligible for the next R-B action;
2. which exact revision and authority envelope apply;
3. which repository surfaces may be read or written;
4. what minimum context must be resolved;
5. what session/worktree isolation is required;
6. which evidence/provenance must be returned; and
7. which events require fail-closed escalation instead of further delegation.

The dispatcher never decides whether new human authority should be granted.

## Role identity is separate from provider identity

R-D defines role identity independently from tool/provider identity.

Supported role classes are:

- `COORDINATOR_ORCHESTRATOR`
- `IMPLEMENTER`
- `INDEPENDENT_REVIEWER`
- `ADVERSARIAL_REVIEWER`
- `VERIFIER`
- `GATEKEEPER`
- `HUMAN_PROGRAM_AUTHORITY`

Provider adapters may include Cursor, Codex, CI automation, deterministic scripts, or future compatible systems.

A provider may fill more than one role across the lifecycle only through distinct dispatches that independently satisfy the role contract. Provider sameness does not defeat independence by itself; run/session/worktree/authority separation does.

## Role capabilities

### Coordinator / Orchestrator

May:

- resolve the current machine-projected state;
- construct dispatch packets;
- assign declared work units within active G2;
- reserve/release serialized surfaces;
- collect run manifests and evidence references;
- route repair/review/verification according to R-B/R-C.

May not:

- write candidate implementation source;
- expand G2 scope;
- create undeclared work units;
- synthesize reviewer PASS;
- merge/deploy;
- grant release, production, or next-phase authority.

### Implementer

May:

- write only the authorized worktree and owned surfaces;
- make necessary bounded supporting changes explicitly permitted by the work-unit context manifest;
- run allowed non-destructive verification;
- push/update the specifically authorized branch/PR only when the G2 external-action envelope permits it;
- emit candidate and provenance records.

May not:

- self-certify independent or adversarial review;
- write ordinary `main`;
- cross serialized-surface ownership;
- expand scope, architecture, privileges, or environment;
- merge/deploy or continue to another work unit merely because the current unit completes.

### Independent Reviewer

Must:

- use a distinct run/session from candidate authoring;
- start from the phase/package/work-unit contract, exact base/head diff, current authority, and evidence rather than implementer conversation memory;
- be read-only against candidate source;
- record exact SHA/tree and review inputs;
- fail closed if independence or exact revision cannot be proven.

If the reviewer edits candidate source, that run becomes an implementer run for the changed revision and cannot certify it.

### Adversarial Reviewer

Has all independent-review requirements plus:

- a fresh run/session for the adversarial task;
- no reuse of prior reviewer scratchpad/session state as authoritative input;
- only visible requirements/authority as semantic basis;
- protected probe details withheld from implementers;
- no candidate mutation.

### Verifier

May run declared deterministic/protected verification against an exact revision. It may record evidence but may not redefine requirements, grant authority, or repair source within the same evidence identity.

### Gatekeeper

May integrate already-produced evidence into a G5 decision only under the 020-H/R-B gate contract. It cannot repair candidate source, fabricate missing evidence, merge, deploy, or grant next G2.

## Dispatch packet

Every agent dispatch is immutable/content-addressed and requires:

- `dispatch_id`;
- `phase_or_package_id`;
- `work_unit_id` when applicable;
- requested `role`;
- selected provider/adapter;
- exact base/candidate SHA and tree as applicable;
- candidate generation;
- authority references and authority digest;
- lifecycle-state expectation;
- task purpose;
- in-scope and out-of-scope statements;
- owned/writable surfaces;
- read-only/reference surfaces;
- serialized-surface reservations;
- dependency work units;
- visible criteria and evidence obligations;
- material-surface IDs from R-C;
- required verification/review output;
- allowed external actions;
- circuit breakers;
- context retrieval seed;
- session-freshness requirement;
- timeout/resource envelope when declared;
- expected output artifact types.

The dispatcher must reject a packet if current R-B state, current authority, exact revision identity, serialized-surface ownership, or role eligibility no longer matches when execution begins.

## Dispatch identity and idempotency

A dispatch is keyed by immutable `dispatch_id` plus packet digest.

- same `dispatch_id` + same digest: idempotent replay/recovery;
- same `dispatch_id` + different digest: `INCONCLUSIVE` / reconciliation required;
- retries create distinct run IDs even when the dispatch packet is unchanged;
- a new candidate generation requires a new dispatch for revision-bound review/evidence;
- prior outputs remain historical and are never overwritten.

## Worktree and filesystem isolation

### Implementer isolation

Default:

```text
control checkout / protected main       read-only coordination
           |
           +-- isolated writable worktree for declared work unit
```

Requirements:

- worktree created from exact authorized base/checkout SHA;
- dedicated branch using the declared branch naming pattern;
- only one writer for serialized surfaces unless an explicit coordination contract says otherwise;
- no writable shared implementation worktree between agents;
- clean worktree identity captured at run start and end;
- unexpected baseline drift triggers a circuit breaker.

### Reviewer isolation

Reviewers use:

- detached exact candidate checkout/worktree;
- read-only source posture;
- no implementer writable worktree reuse;
- no uncommitted candidate mutations;
- independent provider session/run identity.

Temporary probe fixtures must be outside candidate source or demonstrably discarded without changing reviewed tree identity.

## Session freshness and independence

R-D distinguishes:

- provider account identity;
- provider/tool identity;
- dispatcher run identity;
- provider session/conversation identity;
- worktree identity;
- candidate generation;
- role identity.

Independent review requires a run/session distinct from implementation. Adversarial review requires a fresh review run/session distinct from both implementation and the preceding independent review.

Freshness cannot be proven solely by a natural-language statement such as “new session.” The eventual adapter should record whatever stable session/run identifier is available and a dispatcher-generated nonce. If provider session identity is unavailable, the result must use a declared compensating isolation mechanism or fail `INCONCLUSIVE` when freshness is mandatory.

## Context generation

R-D applies CTX-001–CTX-016.

The dispatcher produces a **context manifest**, not a corpus dump.

The manifest references:

- exact task/authority records;
- relevant canonical owners and stable IDs;
- exact base/candidate revisions;
- material-surface and evidence obligations;
- dependencies that remain unresolved;
- allowed historical/external evidence tiers;
- circuit breakers and exclusions.

It does not copy entire canonical rule text into a shadow authority store.

### Context tiers by role

Implementer default:

```text
T0/T1 bootstrap and routing
T2 current owner(s)
T3 only material linked dependencies
T4/T5 only when the work unit explicitly needs provenance/external evidence
```

Independent reviewer default:

1. phase/package/work-unit contract;
2. exact base/candidate diff;
3. current authority independently resolved;
4. relevant current owners/stable IDs;
5. raw evidence/evidence graph nodes;
6. implementer rationale only after independent authority resolution when useful.

Adversarial reviewer default:

- same authority basis as independent review;
- fresh context assembly;
- visible requirements and material boundaries;
- protected evaluator/probe implementation details only when the adversarial role itself is authorized to inspect them;
- no implementer conversational scratchpad as authority.

## Context manifest fields

The machine context manifest requires:

- `manifest_id` and digest;
- dispatch/work-unit/role identity;
- authority refs;
- exact revision refs;
- canonical owner/stable-ID refs;
- material-surface refs;
- visible criterion/evidence obligation refs;
- owned/writable/read-only surfaces;
- dependency work units;
- allowed retrieval tiers;
- allowed external sources/actions;
- exclusions;
- circuit breakers;
- protected-information classes permitted/forbidden;
- budget/profile identifier.

A manifest is operational routing metadata; canonical owners retain normative meaning.

## Anti-bloat and anti-shadow-authority rules

The dispatcher must not:

- recursively preload all numbered phases;
- copy canonical owners wholesale into every prompt;
- persist model-generated summaries as replacement authority;
- reuse historical context merely because it was loaded in a previous session;
- infer authority from chat memory;
- widen context because a provider supports a larger window.

Context expansion requires an unresolved dependency or explicit provenance/external-evidence need.

## Protected information classes

Dispatch distinguishes:

- `PUBLIC_AUTHORITY` — visible requirements/contracts;
- `REVIEW_EVIDENCE` — findings/results appropriate to reviewer role;
- `PROTECTED_EVALUATOR_DETAIL` — hidden probe implementation data;
- `SECRET_OR_SENSITIVE` — credentials, production secrets, real sensitive data.

Rules:

- implementers receive `PUBLIC_AUTHORITY` and permitted repair diagnostics, not protected probe internals;
- reviewers receive only the protected detail required by their declared role;
- ordinary dispatch never transfers `SECRET_OR_SENSITIVE` data;
- secrets are referenced through separately authorized environment/principal mechanisms, never embedded in manifests/prompts/provenance.

## Provenance manifest

Every run emits an immutable technical provenance manifest suitable for R-C evidence-graph ingestion.

Required fields:

- schema/version;
- `dispatch_id`;
- `run_id`;
- phase/package/work-unit;
- role;
- provider/adapter and adapter version;
- dispatcher version/revision;
- provider session identity or declared freshness substitute;
- start/end timestamps;
- base/candidate input SHA/tree;
- candidate generation;
- branch/worktree identity and cleanliness state;
- authority refs + digest;
- context manifest ID/digest;
- serialized-surface reservations;
- external actions actually performed;
- verification/evidence references;
- changed-file/material-surface summary for implementers;
- finding IDs for reviewers;
- output candidate SHA/tree when applicable;
- final disposition;
- circuit breakers encountered;
- manifest digest.

Optional non-sensitive diagnostics may include command names, tool versions, resource usage, and failure classifications.

## Provenance exclusions

The provenance manifest must never require or store:

- private chain-of-thought;
- hidden model reasoning;
- full provider prompt/conversation transcript;
- secret values or credentials;
- protected probe source/fixture values in implementer-visible evidence;
- unrelated user/account data.

A concise task/dispatch digest is sufficient to identify what the model was asked to do.

## Run dispositions

Every run terminates with one of:

- `COMPLETED_WITH_OUTPUT`
- `PASS`
- `CHANGES_REQUIRED`
- `BLOCKED`
- `INCONCLUSIVE`
- `CANCELLED`
- `SUPERSEDED`
- `FAILED_INFRASTRUCTURE`

A run disposition does not itself advance lifecycle state; R-B evaluates the corresponding immutable event and guards.

## Repair dispatch

A repair dispatch must include:

- triggering finding IDs;
- candidate generation being superseded;
- unchanged original G2 scope/criteria;
- remaining repair budget;
- explicit bounded repair direction;
- evidence/reviews invalidated by R-C;
- expected new candidate generation.

It must not include hidden probe answers or silently enlarge scope.

## Reviewer prompt generation

Reviewer instructions should be generated from contracts, not manually improvised each time.

Independent-review generation requires:

- exact candidate identity;
- authority resolution instructions;
- review dimensions;
- evidence inputs;
- required structured output schema;
- read-only/no-repair boundary.

Adversarial-review generation additionally requires:

- explicit falsification objective;
- fresh-session requirement;
- visible criteria/material boundaries;
- challenge categories from 020-H;
- prohibition on hidden requirements;
- no candidate edits.

Delta reviews additionally consume the R-C changed-surface/equivalence/invalidation plan.

## Concurrency and serialized surfaces

The dispatcher may parallelize only work units proven dependency-safe.

Before dispatch it must acquire logical reservations for declared serialized surfaces. Conflicting reservations fail closed rather than relying on agents to coordinate socially.

Reservation release is an immutable event. Abandoned/stale reservations require reconciliation; they cannot be silently stolen.

R-E will define eventing/reconciliation mechanics for these reservations.

## Provider adapters

A provider adapter owns mechanics such as:

- starting a Cursor/Codex run/session;
- materializing the allowed workspace/context;
- passing structured task instructions;
- collecting structured outputs;
- reporting provider/session identity and tool capabilities.

Adapters may not:

- reinterpret semantic authority;
- expand the dispatch packet;
- add undeclared write/external capabilities;
- suppress failure/circuit-breaker outcomes;
- self-convert reviewer runs into repair runs.

Provider-specific ergonomics are subordinate to the common contract.

## Failure and fail-closed conditions

Dispatch fails closed when:

- role is not eligible for current R-B state;
- current authority differs from packet authority digest;
- exact revision no longer matches;
- worktree cannot be isolated;
- serialized surface is already reserved incompatibly;
- required reviewer/adversarial freshness cannot be proven;
- context requires authority outside allowed tiers/envelope;
- provider requires secret/production access outside authorization;
- provider cannot satisfy read-only/write capability boundary;
- provenance fields required for the role cannot be produced;
- packet/session identity conflicts with a previous immutable record.

## Phase-021 replay expectations

R-G shadow replay should prove at least:

1. Codex implementer dispatch receives only 021-I01 scope and writable worktree;
2. independent Cursor review cannot reuse implementer session/worktree;
3. fresh adversarial Cursor review has distinct session identity;
4. adversarial BLOCKED routes a bounded repair dispatch with findings but not hidden answers;
5. Repair Cycle 1 creates a new candidate generation and fresh review dispatches;
6. PR-head governance delta generates independent/adversarial delta-review packets using R-C classification;
7. no PASS, CI, G5, or merge event generates Phase-022 dispatch authority.

## Exit review

R-D closes PASS because:

1. role and provider identity are separated;
2. capabilities are role-bounded;
3. dispatch packets are immutable, exact-revision and authority-bound;
4. implementer/reviewer worktree and session isolation are explicit;
5. reviewer/adversarial freshness is mechanically evidentiary rather than conversational;
6. context generation follows minimum-sufficient canonical routing without shadow authority;
7. protected probes/secrets/chain-of-thought are excluded appropriately;
8. every run produces an R-C-ingestible provenance manifest;
9. repair/reviewer prompts can be generated deterministically from contracts; and
10. concurrency requires serialized-surface reservations rather than social coordination.

## Handoff

**021-R-E — GitHub Event Integration, Deduplication/Idempotency, PR/CI Choreography & Reconciliation** is next eligible.

R-E should consume dispatch/run identities from this contract and define how GitHub/webhook/check events become trustworthy immutable lifecycle facts despite duplicate, late, and out-of-order delivery.
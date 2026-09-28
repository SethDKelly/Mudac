# 021-R-E — GitHub Event Integration, Deduplication/Idempotency, PR/CI Choreography & Reconciliation

## Status

**COMPLETE — PASS.**

021-R-E defines how GitHub activity becomes trustworthy lifecycle evidence for the R-B orchestrator without allowing webhook delivery order, duplicate events, stale PR state, or CI presentation differences to create false lifecycle transitions.

It remains a design/governance contract only. Runtime autonomy implementation, Phase 022 execution, merge, release, production, and provider deployment remain unauthorized.

Machine projection: `docs/routing/autonomy_github_event_contract.json`.

## Governing rule

> **A GitHub event is a notification, not lifecycle truth.**

Webhook/check/workflow events are append-only observations. Lifecycle state may advance only after the event is reconciled against current GitHub/repository truth and the applicable R-B/R-C/R-D contracts.

This preserves:

- R-B guarded transition semantics;
- R-C exact-revision evidence and invalidation rules;
- R-D dispatch/run/provenance identities;
- 020-G exact-SHA CI evidence; and
- 020-H immutable review/G5 history.

## External GitHub mechanics considered

Current GitHub webhook guidance establishes useful transport facts that R-E treats as mechanics rather than MUDAC authority:

- webhook handlers should inspect event type and action explicitly;
- `X-GitHub-Delivery` identifies a delivery and is retained for redelivery;
- webhook handlers should acknowledge receipt quickly and process asynchronously;
- GitHub can redeliver missed deliveries;
- event families such as `pull_request`, `check_run`, `check_suite`, `workflow_run`, and `push` have distinct payload/trigger semantics.

These mechanics are external dependencies. MUDAC still reconciles all consequential state against repository truth instead of trusting delivery arrival alone.

## Event pipeline

R-E defines the logical pipeline:

```text
GitHub delivery / poll / reconciliation trigger
        ↓
verify source + normalize envelope
        ↓
append immutable delivery record
        ↓
deduplicate delivery identity
        ↓
correlate subject identities
        ↓
query/reconcile current GitHub + repository truth
        ↓
produce immutable reconciled fact(s)
        ↓
R-C evidence/update calculation if revision/evaluator changed
        ↓
R-B guard evaluation
        ↓
next action eligibility only
```

No raw webhook bypasses the reconciliation stage for a consequential lifecycle transition.

## GitHub event envelope

Normalized ingress requires:

- `delivery_id`;
- webhook/hook or app installation identity when available;
- repository stable identity;
- event family;
- action;
- received timestamp;
- signature-verification result;
- payload digest;
- sender/system identity where available;
- PR number or ref when applicable;
- payload head/base SHA where supplied;
- check/workflow run identity when applicable;
- installation identity when applicable;
- redelivery indicator when available.

Raw secret-bearing headers or credentials are not retained in ordinary evidence.

## Delivery idempotency

Primary delivery idempotency key:

```text
source installation / hook identity
+ repository identity
+ X-GitHub-Delivery
```

Rules:

- same delivery identity + same payload digest → `IDEMPOTENT_NOOP` after the first accepted record;
- same delivery identity + conflicting payload digest → `INCONCLUSIVE_SECURITY_RECONCILIATION`;
- a GitHub redelivery remains historical evidence of another delivery attempt but does not create another semantic lifecycle fact;
- processing retries never overwrite the original delivery record;
- processing attempt IDs are distinct from delivery IDs.

## Semantic fact idempotency

Different deliveries can report the same GitHub fact. R-E therefore defines a second identity layer for normalized facts.

Examples:

- PR head fact: repository + PR number + head SHA;
- PR merge fact: repository + PR number + merge commit SHA;
- check fact: repository + check-run ID + attempt/run identity + head SHA + conclusion;
- workflow fact: repository + workflow/run/attempt + head SHA + conclusion;
- ref fact: repository + ref + observed SHA;
- review/thread fact: repository + PR + review/thread stable identity + state.

A duplicate normalized fact is a no-op. A later fact that supersedes an earlier one appends a new fact and leaves prior history intact.

## Event order is never trusted

Events may be duplicated, delayed, retried, or observed after a newer repository fact.

Therefore:

- `observed_at` does not establish lifecycle order by itself;
- webhook arrival time does not outrank exact repository/PR/run identity;
- a late event for an old PR head remains historical and cannot regress current state;
- a check completion for a superseded candidate cannot satisfy current exact-head CI;
- an out-of-order merge event must be reconciled with PR state and the base ref before integration is registered.

## Reconciliation model

Every consequential event routes through a reconciler.

### PR reconciler

Fetch/establish:

- PR number;
- open/closed/merged/draft state;
- current head SHA;
- base ref and current base SHA;
- merge commit SHA when merged;
- mergeability/freshness signal where available;
- unresolved required review threads where applicable.

### Ref reconciler

Establish exact current SHA/tree for:

- implementation branch;
- closure branch when used;
- protected `main`;
- any exact integration revision required by evidence.

### Check/CI reconciler

Establish:

- exact subject SHA;
- required-check set from current repository enforcement/phase contract;
- check-run/workflow-run identities and attempts;
- workflow definition/evaluator identity where required by 020-G;
- conclusion;
- whether the check applies to the current candidate rather than a superseded head.

### Evidence reconciler

Correlate GitHub facts to:

- R-D dispatch/run IDs;
- candidate generation;
- R-C evidence nodes/bindings;
- G5 exact candidate;
- integration/closure identity.

## CI truth hierarchy

R-E does not assume that every GitHub status surface reports the same thing.

For current MUDAC required PR evidence:

1. required check-runs/workflow runs tied to the exact candidate are the primary execution evidence;
2. workflow metadata supplies provenance/run-attempt identity;
3. branch/ruleset required-check configuration supplies the required set;
4. legacy combined commit status may be observed but cannot override exact check-run evidence when it is empty, lagging, or semantically different;
5. contradictory signals trigger reconciliation rather than optimistic PASS.

This directly addresses the Phase-021 observation where current check-runs were successful while a legacy combined-status surface did not represent those checks usefully.

## Required-check set evaluation

`github.check.required_set_pass` may be emitted only when:

- current candidate SHA/tree is known;
- the required check set is known for the current protected integration path;
- every required check result is tied to the relevant exact head;
- every required check is terminal and successful;
- no required check is missing, cancelled, skipped incompatibly, stale, or still running;
- evaluator/workflow material has not changed in a way R-C says invalidates prior evidence;
- no later head update supersedes the evaluated revision.

Green checks never create merge authority.

## PR choreography

### Draft implementation PR

When the lifecycle profile permits PR creation and the dispatch/G2 external-action envelope authorizes it, the control plane may prepare/open/update a **draft** PR for the authorized branch.

Automation may:

- create/update title/body/status evidence;
- associate exact candidate identity;
- observe checks;
- mark synchronization need.

Automation may not merge.

### Ready-for-review

A PR becomes eligible to move out of draft only after the declared review/CI/G5 choreography permits it. The exact human/automation responsibility may be package-profile-specific, but moving to ready state never grants merge authority.

### PR synchronize/head change

Any change to a PR head after revision-bound evidence exists triggers:

```text
new head observed
→ freeze merge eligibility
→ establish old/new SHA + tree
→ R-C classify delta
→ invalidate/rebind evidence
→ route required delta/full review
→ rerun exact-head CI as required
```

The control plane may not continue using stale G5/review evidence solely because the PR number is unchanged.

### Base branch drift

If strict branch freshness requires the implementation/closure branch to include current `main`, R-E may classify a synchronization action as eligible only if the current lifecycle profile and allowed external actions permit branch synchronization.

Synchronization:

- is an implementation/governance branch mutation;
- creates a new head identity;
- triggers R-C material-difference classification;
- cannot silently reuse stale exact-head approval;
- cannot itself authorize merge.

### Merge

A merge event is sufficient only after reconciliation proves:

- the PR is actually merged;
- the expected PR/head relationship is known;
- the merge commit/integration SHA exists;
- protected human merge authority was the governing transition where required;
- current `main` reflects the expected integration;
- integration SHA/tree are registered as a distinct R-C identity.

## Closure-PR dependency choreography

The default R-B lifecycle uses a separate closure PR unless another profile was declared before G2.

R-E encodes the dependency:

```text
implementation PR merged
       ↓
register integration SHA/tree
       ↓
update closure evidence
       ↓
closure branch may become behind main
       ↓
synchronization eligible if authorized
       ↓
new closure head + fresh required checks
       ↓
human closure merge
```

The closure PR cannot be merged ahead of the implementation integration it is meant to document.

An out-of-date closure branch is a coordination condition, not a defect in the implementation candidate.

## Post-merge verification

After implementation or closure merge:

- register the actual `main` commit SHA/tree;
- classify candidate→integration and integration→closure material differences through R-C;
- collect required push/main-integration checks when declared;
- use tree identity/content-equivalence only through explicit proof;
- never rewrite pre-merge review/G5 evidence to the merge SHA.

## Polling/reconciliation fallback

Webhooks are accelerators, not the only source of truth.

The design requires a reconciliation sweep capable of reconstructing current state from APIs/repository facts when:

- a delivery was missed;
- the control plane was offline;
- a delivery failed processing;
- delivery order is ambiguous;
- a PR/ref/check changes without a correlated event record;
- current projection disagrees with GitHub truth.

A periodic or startup reconciliation cadence is deferred to implementation design, but event-only state reconstruction is forbidden.

## Event-store and projection semantics

R-E requires:

- append-only raw delivery metadata/digests;
- append-only normalized facts;
- append-only processing attempts;
- current lifecycle state as a projection;
- replayable deterministic projection from immutable facts plus current external reconciliation snapshots where needed;
- no destructive replacement of earlier failed/stale facts.

Storage technology remains deferred.

## Side-effect idempotency

Every proposed GitHub mutation has an operation identity separate from webhook identity.

Examples:

- open/update draft PR;
- mark PR ready/draft;
- synchronize dependency branch;
- write coordination comment/evidence reference.

Each operation requires:

- operation ID;
- expected current GitHub state/version/head;
- bounded requested mutation;
- authority/action-envelope reference;
- result identity;
- retry policy.

Retrying the same successful operation is a no-op. A changed expected head/state requires a new operation or reconciliation.

## Optimistic concurrency

Before any bounded GitHub mutation, the adapter rechecks the expected subject identity.

Examples:

- expected PR head must still match before editing head-bound metadata;
- branch synchronization requires the expected old head and current base;
- candidate PR updates cannot overwrite a newer candidate's coordination state;
- closure synchronization cannot race another writer on the same serialized branch.

Mismatch → reconcile/fail closed; never force overwrite.

## Serialized-surface reservation integration

R-D reservations become event-backed coordination facts.

Reservation lifecycle:

```text
reservation.requested
→ reservation.acquired
→ dispatch starts
→ reservation.released
```

Abandoned/stale reservations require evidence that the owning run ended/cancelled and an explicit reconciliation disposition. Silent reservation stealing is forbidden.

## Security and permissions

R-E design requires:

- minimum necessary event subscriptions;
- webhook signature verification before accepting delivery facts;
- HTTPS/TLS for live ingress;
- bounded GitHub App/token permissions;
- read-only access for reconciliation wherever possible;
- narrowly scoped write permissions only for separately authorized PR/branch coordination actions;
- untrusted PR code must not receive protected credentials;
- webhook secrets, tokens, signatures, or credentials must not be persisted in public evidence;
- no event payload may synthesize semantic/G2/merge/release/production authority.

Exact permission sets are deferred to the autonomy implementation package and R-F capability design.

## Failure classes

R-E defines at least:

- `DELIVERY_SIGNATURE_INVALID` → reject delivery;
- `DUPLICATE_IDENTICAL` → idempotent no-op;
- `DUPLICATE_CONFLICTING` → `INCONCLUSIVE`;
- `UNKNOWN_EVENT_OR_ACTION` → record/ignore for lifecycle advancement;
- `STALE_SUBJECT_EVENT` → retain historical, no current transition;
- `CURRENT_TRUTH_CONTRADICTS_EVENT` → reconciliation required;
- `REQUIRED_CHECK_MISSING` → no CI PASS transition;
- `REQUIRED_CHECK_FAILED` → failure/repair routing as governed;
- `EVALUATOR_IDENTITY_CHANGED` → R-C evaluator invalidation;
- `PR_HEAD_CHANGED` → R-C delta classification;
- `BASE_DRIFT` → synchronization/review classification;
- `MERGE_IDENTITY_AMBIGUOUS` → `INCONCLUSIVE`;
- `SIDE_EFFECT_PRECONDITION_FAILED` → reconcile, do not force;
- `SERIALIZED_RESERVATION_CONFLICT` → `BLOCKED`;
- `GITHUB_API_UNAVAILABLE_FOR_MANDATORY_FACT` → `BLOCKED` or `INCONCLUSIVE` according to lifecycle need.

Automatic retry-until-green is forbidden for mandatory evidence failures.

## Phase-021 replay oracle

R-G must use the actual Phase-021 PR history to prove R-E behavior.

### Case A — PR #19 original/repaired candidate

Expected:

- candidate/review identities remain exact;
- repair produces new head/generation;
- stale check/review facts for the superseded candidate remain historical.

### Case B — PR #19 head moves `1c36dbed… → 280c896c…`

Expected:

- synchronize/head-change event freezes merge eligibility;
- reconciler observes new head;
- R-C returns `GOVERNANCE_MATERIAL_DELTA`;
- independent and fresh adversarial delta review are requested;
- exact-head CI is required;
- G5 binding refresh is required;
- prior G5 remains immutable historical evidence.

### Case C — PR #19 merge

`280c896c… → a38d9cb3…`

Expected:

- PR merge plus main-ref reconciliation registers `a38d9cb3…`;
- identical-tree proof permits implementation evidence reuse by reference;
- integration evidence is attached to the merge identity.

### Case D — PR #20 closure dependency

Expected:

- closure PR remains dependent on implementation merge;
- after #19 merge, #20 may be reported out-of-date;
- branch synchronization creates a new closure head;
- required CI reruns on that head;
- human closure merge remains required.

### Case E — final Phase-021 main

Expected:

- final `main` identity `29637b92…` is registered after closure merge;
- Phase 021 projects COMPLETE;
- Phase 022 projects NEXT ELIGIBLE / NOT AUTHORIZED;
- no GitHub event generates a Phase-022 dispatch.

## Required queries

The eventual GitHub adapter/reconciler must answer:

- What is the current exact PR head/base/merge identity?
- Which delivery/fact caused this reconciliation?
- Has this delivery or semantic fact already been processed?
- Are current required checks complete for this exact head?
- Which check/workflow attempt is authoritative evidence and why?
- Did the PR head move after review/G5?
- What R-C invalidation/rebinding follows from the move?
- Is a branch synchronization eligible and within authority?
- Is a closure PR dependent on an unmerged integration?
- What is the current `main` SHA/tree?
- Is the projected lifecycle state consistent with current GitHub truth?

## Exit review

R-E closes PASS because:

1. raw GitHub events are explicitly non-authoritative notifications;
2. delivery and semantic-fact idempotency are separated;
3. duplicate, redelivered, stale, and out-of-order events are fail-safe;
4. current PR/ref/check/workflow truth is reconciled before consequential transitions;
5. exact-head required-check evaluation is explicit;
6. PR head/base drift routes through R-C rather than silently preserving approval;
7. implementation/closure PR dependency choreography is specified;
8. post-merge integration identity/evidence capture is explicit;
9. missed-event recovery does not depend on webhook completeness;
10. side-effect retries use optimistic preconditions and never force-write through drift;
11. serialized-surface reservations gain event-backed lifecycle semantics; and
12. GitHub events still cannot create G2, merge, release, production, reopen, or next-phase authority.

## Handoff

**021-R-F — Development-Control MCP Interfaces, Authorization, Production Denial & Composition with the 020-D Test-Control Plane** is next eligible.

R-F should expose the R-B/R-C/R-D/R-E read/compute/bounded-action capabilities through an explicit capability and authorization model without turning MCP possession into semantic or human authority.

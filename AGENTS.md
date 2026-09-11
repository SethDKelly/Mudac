# MUDAC Repository Agent Rules

This file is a **bootstrap adapter**, not the canonical source of MUDAC product, synchronization, architecture, implementation, verification, source-topology, runtime, persistence, identity/authentication, or documentation rules.

Canonical governance lives under [`docs/canonical/governance/`](docs/canonical/governance/).

## Required start

1. Start at [`docs/index.md`](docs/index.md).
2. For current meaning, use [`docs/canonical/`](docs/canonical/).
3. For behavior spanning more than one Concept, load the relevant owner under [`docs/canonical/synchronizations/`](docs/canonical/synchronizations/) rather than reconstructing coordination from old phase history.
4. For correction, invalidation, supersession, replacement, current-vs-historical truth, affected/stale state, official-outcome succession, or Publication timeline work, additionally load [`Temporal Truth, Correction & Historical Authority`](docs/canonical/synchronizations/temporal-truth-correction.md).
5. For Judge/Organizer interaction, route, status, exception, confirmation, recovery, or UI-authority design, additionally load [`Experience Action, State & Authority Traceability`](docs/canonical/experience/action-authority-traceability.md) plus only the task-relevant experience owner(s).
6. For exception, waiver, override, acknowledgement/suppression, policy-bypass, or technical-emergency-versus-semantic-authority work, additionally load [`Operational Exception & Override Governance`](docs/canonical/policies/operational-exception-governance.md) plus the specific governing policy/Concept owner.
7. For Export/Publication or external representation work, preserve exact source authority and load the relevant [`Export`](docs/canonical/concepts/export.md), [`Publication`](docs/canonical/concepts/publication.md), disclosure, official-outcome, and temporal owners as needed. A representation cannot promote its source authority.
8. **Before any implementation/code/IaC task, read [`Design / Implementation Boundary`](docs/canonical/governance/design-implementation-boundary.md). The Jackson Concept Design methodology is complete for the current baseline, implementation planning is active, the 006-D non-domain substrate is qualified, but no executable domain slice is authorized.**
9. For architecture work, load only the relevant owner(s) under [`docs/canonical/architecture/`](docs/canonical/architecture/) plus materially relevant upstream constraints.
10. For implementation-planning work, also load the active [`Phase 008`](docs/008-implementation-reentry/) routing, the relevant owner(s) under [`docs/canonical/implementation/`](docs/canonical/implementation/), task-relevant architecture, and materially relevant product/UX/governance/synchronization constraints. [008-A](docs/008-implementation-reentry/008-A-implementation-reentry-authority-canonical-baseline-change-control-planning-guardrails.md) defines planning authority; [008-B](docs/008-implementation-reentry/008-B-protected-006-D-baseline-qualification-drift-audit-toolchain-environment-reconciliation.md) defines the qualified bootstrap; [008-C](docs/008-implementation-reentry/008-C-residual-risk-ingestion-historical-006-mapping-decision-register-supersession-matrix.md) owns residual/historical-plan disposition.
11. For persistence, temporal/history representation, Version/Provenance storage, governed-exception storage, outbox, projection or migration work, additionally load [`Persistence, History, Provenance, Outbox, Projection & Migration Implementation Contract`](docs/canonical/implementation/persistence-history-projection.md). [008-D](docs/008-implementation-reentry/008-D-persistence-temporal-truth-versioning-provenance-governed-exceptions-outbox-projection-migration-implementation-plan.md) is rationale/planning provenance.
12. For authentication, Identity, Participation, Access, session, invitation, recovery, reverification, secrets or technical-authority work, additionally load [`Identity, Authentication, Participation, Access, Session, Invitation, Secrets & Technical Authority Implementation Contract`](docs/canonical/implementation/identity-authentication-access-session.md). [008-E](docs/008-implementation-reentry/008-E-identity-authentication-participation-access-session-invitation-secrets-technical-authority-implementation-plan.md) is rationale/planning provenance.
13. Verification/test work additionally loads [`Verification Strategy, Evidence & Quality Gates`](docs/canonical/implementation/verification-strategy.md).
14. Source/package/import work additionally loads [`Source Topology, Package Boundaries & Dependency Enforcement`](docs/canonical/implementation/source-topology.md).
15. Runtime/environment/CI/IaC work additionally loads [`Runtime, Environment & Delivery Bootstrap`](docs/canonical/implementation/runtime-delivery-bootstrap.md).
16. Use numbered phase history only for rationale, chronology, rejected alternatives, implementation lineage, or source audit.

Governed by `DOC-*`, `CTX-*`, `CHG-*`, `META-*`, `VAL-*`, task-relevant canonical synchronization/architecture rules, [`IMPL-*`](docs/canonical/implementation/implementation-foundation.md), the task-relevant canonical implementation owners, the active Phase 008 plan, and the current [Design / Implementation Boundary](docs/canonical/governance/design-implementation-boundary.md).

## Current post-methodology implementation boundary

The renewed Jackson Concept Design methodology formally exited through Phase 007-I for the current MUDAC baseline.

Phase 008 is active. 008-A established implementation-planning authority; 008-B qualified the retained 006-D substrate; 008-C reconciled accepted residual/historical work; 008-D accepted the persistence/history implementation contract; 008-E accepted the Identity/authentication/Participation/Access/session/invitation/secrets/technical-authority implementation contract.

Current status:

```text
Jackson Concept Design methodology: COMPLETE / EXITED
Phase 008 subdivision: COMPLETE
implementation planning authority: ESTABLISHED
008-A: COMPLETE
008-B: COMPLETE — PASS AFTER NARROW REMEDIATION
008-C: COMPLETE — PASS
008-D: COMPLETE — PASS
008-E: COMPLETE — PASS
protected 006-D baseline: QUALIFIED FOR PHASE 008 PLANNING
persistence/history implementation plan: ACCEPTED / NOT IMPLEMENTED
identity/auth/access/session implementation plan: ACCEPTED / NOT IMPLEMENTED
008-F: NEXT / NOT STARTED
first executable domain slice: NOT YET AUTHORIZED
new domain implementation after 006-D: NOT STARTED
```

The executable work created through 006-D remains a **qualified protected non-domain implementation baseline**. 008-D and 008-E define what future persistence and identity/authentication implementation must build but do not alter the schema/auth-free executable baseline.

Until **008-L — Consolidated Dependency Graph, Implementation Roadmap, First-Slice Authorization & Phase Exit Review** explicitly authorizes the first domain implementation slice, agents must not advance into new:

- domain PostgreSQL schemas/migrations/repositories/outbox/projections described by 008-D;
- Cognito resources, login/callback/session/Identity/Participation/Access/invitation behavior described by 008-E;
- production command/query API or idempotency/transaction implementation;
- IndexedDB Draft semantics;
- Competition, Judging, Evaluation, Outcome, Award, Export, Artifact or Publication feature implementation;
- real AWS application provisioning/deployment intended to support those domain paths.

Permitted executable changes before first-slice authorization remain narrow dependency/security/compatibility maintenance, non-domain verification/tooling repair, documentation/routing changes, and removal of accidental behavior that conflicts with current authority.

Current work should proceed to **008-F — Commands, Queries, Transactions, CAS, Idempotency, Concurrency, Lost-Response Reconciliation & API Implementation Plan**, not domain coding.

## Accepted 008-D persistence planning

Current implementation planning may rely on the canonical persistence owner for one PostgreSQL authority database with module-owned schemas; stable UUID identity and `bigint` mutable revisions; current state distinct from semantic Versions/history; module-local Provenance; policy-specific governed exceptions; immutable Official Outcome Revision substrate; transactional at-least-once outbox; explicit-basis projections; SQL-first forward migrations; and conservative authoritative-history retention.

## Accepted 008-E identity/authentication planning

Current implementation planning may rely on these durable choices:

- Cognito User Pools is an authentication adapter, not MUDAC Identity/authority;
- browser authentication uses OIDC/OAuth authorization code with state/nonce/PKCE and server-side exchange;
- provider bearer tokens do not live in ordinary script-readable browser storage and are not retained long term by default after MUDAC session creation;
- external principals link to stable MUDAC Identity by provider/issuer + subject, never by mutable email/name/group claims;
- one Participation exists per Identity × Competition × role; dual-role users explicitly select one Participation context rather than unioning capabilities;
- Access is contextual composition plus resource-owner preconditions, not generic database RBAC;
- explicit Access grants are retained and capability/resource/time/purpose bounded; they do not transfer authorship;
- Event Completed source-state authorization ends ordinary Judge private-evaluation capability even if the session/cookie remains technically live;
- opaque first-party sessions are PostgreSQL-backed, bearer tokens are stored only as digests, and sessions rotate/revoke independently of semantic authority;
- invitation/QR/code possession alone cannot establish Identity or Access; claim-capable invitations are scoped, expiring, replay-safe server records;
- provider credential recovery and MUDAC principal-link recovery remain distinct; email/name matching never silently merges Identity;
- step-up increases authentication assurance only and never creates capability;
- technical/support/break-glass authority cannot synthesize Judge/Organizer Participation or semantic authority;
- baseline support tooling does not impersonate users;
- protected server secrets remain outside browser/source/log/Provenance/outbox surfaces.

These choices are implementation contracts, not permission to create executable artifacts.

## 008-C planning ownership

008-C remains the provenance owner for residual and historical-plan disposition. Agents must use it instead of reconstructing the old 006-E–M queue.

Key routing consequences remain: Class 4 future scope is excluded; old 006-J is split between 008-G and 008-I; old 006-L is merged into 008-J; old 006-M is split between 008-K and 008-L; and repository-protection/dependency-alert evidence limitations remain assigned to 008-K/008-L.

## Do not

- recursively preload all of `docs/` for ordinary work;
- reconstruct current rules from old phase history when a canonical owner exists;
- resume 006-E through 006-M as executable slices after 008-C has superseded/mapped them;
- pull 007-H Class 4 future scope into baseline planning without deliberate `CHG-*` re-entry;
- create the 008-D planned schemas/migrations/outbox/projections/repositories before 008-L authorization;
- create the 008-E planned Cognito/session/Identity/Participation/Access/invitation implementation before 008-L authorization;
- confuse a `bigint` mutable row revision with a semantic Version identity;
- use queue/outbox sequence or arrival order as authoritative commit order;
- create a central Provenance god-table or universal override/exception table that steals module/policy ownership;
- trust client-supplied Identity, role, Participation, email, provider group, session metadata or operator labels as authorization authority;
- use email/name matching to silently merge or relink MUDAC Identity;
- model a dual-role person as one unioned Judge+Organizer capability context;
- let session validity, Cognito token validity, invitation possession or successful step-up create/extend semantic capability;
- let support/break-glass/runtime/admin privilege satisfy Judge/Organizer authorship or Competition decision authority;
- add generic user impersonation or `become organizer` controls as baseline support mechanisms;
- retain provider bearer credentials without an explicit justified contract;
- place session/invitation/provider/database secrets in source, browser storage, logs, Provenance, outbox, fixtures or generated API artifacts;
- use generic `status`, `deleted_at`, JSON payloads or cascade deletion to collapse/erase lifecycle/currentness/validity/replacement/correction/history distinctions;
- duplicate synchronization or temporal semantics independently inside downstream docs/tests/code when the canonical owner can be referenced;
- let a screen, route, mode, badge, exception row, confirmation dialog or enabled control become an alternate domain-action/authority owner;
- let Fastify routes, Kysely rows, OpenAPI DTOs, React components, OpenTofu modules, mocks, fixtures, Cognito SDK objects or token claims become alternate domain owners;
- substitute SQLite/in-memory evidence for real PostgreSQL when PostgreSQL semantics matter;
- hide flaky consequential tests behind retries or indefinite quarantine;
- treat CI, coverage, scanners, workflow existence, provider login success, IaC validation, or deployment configuration as semantic verification or production certification;
- infer that completion of Concept Design, 008-A/B/C/D/E, accepted implementation plans, green checks, or historical plans authorize skipping the 008-L first-slice boundary;
- begin Phase 009 or any new domain implementation before 008-L explicitly authorizes the first slice.

## Protected executable baseline

The selected implementation family remains Node.js 24 LTS + TypeScript, pnpm workspaces, Fastify, Kysely + node-postgres, explicit SQL-first migrations, outward-generated OpenAPI, Vitest/Playwright, strict TypeScript + ESLint + Prettier, Cognito User Pools behind an application adapter, and OpenTofu.

Current executable consequences remain only the qualified 006-D bootstrap. The 008-D/008-E contracts are still plan authority, not executable behavior.

## Validation

Knowledge changes:

```text
python -m pip install -r requirements-docs.txt
python scripts/validate_knowledge.py
```

Permitted executable-maintenance changes before first-slice authorization:

```text
pnpm install --frozen-lockfile
pnpm verify
```

CI additionally validates current OpenTofu roots. Passing checks are evidence for the tested revision, not OKF verification, implementation correctness, authority to skip the Phase 008 boundary, or production certification.

## Canonical changes

If implementation planning discovers a genuine semantic contradiction, missing semantic owner, or the human requests a semantic change, use [`CHG-*`](docs/canonical/governance/change-governance.md). If an implementation/test/architecture mechanism conflicts with canonical meaning and redesign was not requested, the downstream mechanism adapts.

## Context stopping rule

Once sufficient authoritative context is loaded to perform the task safely, stop expanding context unless a concrete unresolved dependency remains.

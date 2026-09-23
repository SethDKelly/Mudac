---
type: Phase Record
title: 020-G — CI/CD, Security, Supply Chain, Exact-SHA Verification & Evidence-Bundle Architecture
description: "Defines the autonomous implementation delivery-control architecture for public CI, security and supply-chain verification, exact-revision evidence, protected evaluator result binding, repository enforcement evidence, build provenance and package/phase evidence bundles without deploying application infrastructure or granting implementation/release/production authority."
status: stable
tags: [phase-020, ci-cd, security, supply-chain, exact-sha, evidence-bundle, provenance, verification]
sources:
  - resource: README.md
  - resource: 020-C-cursor-codex-roles-work-isolation-context-provenance-autonomy-circuit-breakers.md
  - resource: 020-D-nonproduction-environment-synthetic-data-observability-mcp-agent-test-control-plane-architecture.md
  - resource: 020-E-implementation-phase-package-discovery-dependency-graph-parallelism-sequencing.md
  - resource: 020-F-implementation-phase-contract-visible-criteria-evidence-classes-hidden-evaluation-architecture.md
  - resource: ../canonical/governance/implementation-program-delivery.md
  - resource: ../canonical/governance/agentic-conformance.md
  - resource: ../routing/implementation_program_framework.json
  - resource: ../routing/phase020_implementation_package_discovery.json
  - resource: ../routing/phase020_implementation_phase_contract.json
  - resource: ../routing/phase020_ci_supplychain_evidence_architecture.json
generated: { by: openai/gpt-5.6-sol, at: 2026-09-23T12:56:00-05:00 }
---

# Purpose

Define the delivery-control architecture that future Phase-021+ implementation work must use to establish trustworthy evidence for an exact revision.

020-G answers four questions left intentionally open by 020-F:

1. which CI/security/supply-chain controls produce which classes of evidence;
2. how evidence is cryptographically and procedurally bound to the exact code/configuration revision that was evaluated;
3. how public CI, protected evaluation, independent review and repository administration combine without becoming one over-privileged pipeline; and
4. what evidence bundle a Gatekeeper receives before an implementation package/phase may close.

020-G is **design-only**. It does not deploy the MCP plane, create AWS resources, change production, grant G2, mark any proposed package G1-ready or claim repository protections that have not been independently observed.

# Entry state

~~~text
PHASE 020 ACTIVE
020-A/B/C/D/E/F COMPLETE
020-G NEXT ELIGIBLE / USER AUTHORIZED

proposed packages                 15
G1-ready packages                 0
G2-authorized packages            0
active implementation packages    0
implementation execution          NOT AUTHORIZED
release authority                 NOT GRANTED
production authority              NOT GRANTED
~~~

Exact 020-G planning baseline:

> 5f6933eb046d4efcffbce4a0af95dc1e0190e540

# Decision

**020-G — ACCEPT A LAYERED EXACT-REVISION DELIVERY AND EVIDENCE ARCHITECTURE.**

The governing rules are:

> **Evidence proves the revision it names, and no other revision.**

> **Build once from a reviewed revision; promote immutable identity rather than rebuilding per environment.**

> **CI may verify and attest; CI does not create semantic authority, release authority or production authority.**

# Current qualified CI substrate

The repository currently contains three useful workflow identities:

| Existing workflow | Current role | 020-G disposition |
|---|---|---|
| **Knowledge Validation** | repository/agentic/documentation conformance | retain as E1 governance/static evidence |
| **Implementation Verification** | workspace, build, Compose and OpenTofu baseline | retain and extend under IMP-014 as public implementation evidence |
| **CodeQL** | JavaScript/TypeScript static security analysis | retain as one security input; never treat as complete security evidence |

Current useful supply-chain controls include:

- exact Node and pnpm major/minor policy plus committed lockfile;
- frozen-lockfile installation in Implementation Verification;
- bounded pnpm build-script allowlist;
- Dependabot for npm and GitHub Actions;
- pinned OpenTofu version in the current workflow;
- repository high-confidence secret guard on agentic/governance surfaces;
- read-only workflow permissions for ordinary validation.

Current gaps that 020-G deliberately records rather than pretending are already solved:

- workflow actions are presently referenced by release tags rather than immutable commit SHAs;
- no blocking dependency-review gate is defined;
- no application-wide secret scanner contract is implemented;
- no SBOM/provenance/attestation pipeline is implemented;
- no container or IaC vulnerability scanner pipeline is implemented;
- no exact-SHA evidence bundle exists;
- no protected-evaluator result is bound into a package/phase bundle;
- repository rulesets/branch-protection enforcement has not been independently verified;
- no application deployment workflow exists;
- no production environment protection or AWS OIDC deployment role exists.

These gaps become implementation obligations, principally under IMP-014 and IMP-015.

# Delivery-control separation

020-G keeps five control planes distinct.

~~~text
1. PUBLIC VERIFICATION
   repository-visible CI checks
        |
        v
2. PROTECTED VERIFICATION
   criteria-derived evaluator with hidden probes
        |
        v
3. REVIEW / GATEKEEPING
   independent human/agent review and exit decision
        |
        v
4. RELEASE / PROMOTION
   immutable artifact identity + authorized environment
        |
        v
5. PRODUCTION
   separate G7 / production authorization
~~~

No plane inherits the authority of the next plane merely because it passed.

A successful CI run does not authorize merge.
A merge does not authorize deployment.
A deployment to non-production does not authorize production.
A release candidate does not establish G7.
A production deployment does not retroactively prove hidden semantic requirements.

# Logical CI gates

020-G defines stable **logical** gates. Physical GitHub workflow/check names may be instantiated by IMP-014, but their mapping must be machine-readable and change-controlled.

## CI-KNOWLEDGE

Purpose:

- current knowledge/routing integrity;
- agentic authority policy;
- generated/reference reproducibility;
- phase/control consistency;
- high-confidence governance-secret guard;
- mutation-based negative controls.

Evidence class:

- E1 only.

## CI-IMPLEMENTATION

Purpose:

- reproducible dependency installation;
- formatting/type/lint/dependency-boundary checks;
- unit/component tests;
- build;
- local Compose/configuration verification;
- OpenTofu static/root validation;
- later package-specific public implementation checks.

Evidence classes:

- E1/E2 and selected E3 only when the material boundary is genuinely exercised.

## CI-SECURITY-SUPPLYCHAIN

Purpose:

- dependency diff/review;
- secret scanning;
- dependency/license policy;
- SAST;
- IaC scanning;
- container/base-image scanning when images exist;
- SBOM generation and validation;
- provenance/attestation verification.

Evidence classes:

- primarily E1/E5;
- selected E6 for built/deployable artifact integrity.

A scanner PASS does not replace behavioral authorization/disclosure/security evidence.

## CI-INTEGRATION

Purpose:

- real PostgreSQL/provider/runtime behavior when required;
- cross-package integration;
- consequential API/browser scenarios;
- migration/compatibility checks;
- non-production test-control evidence.

Evidence classes:

- E3/E4/E5 and selected E6.

## CI-EVIDENCE

Purpose:

- collect declared evidence obligations;
- validate exact-revision identity;
- verify result/artifact digests;
- confirm required public and protected results exist;
- produce the evidence-bundle manifest;
- reject stale/mismatched evidence.

This gate validates evidence completeness; it does not invent a PASS for an underlying failed check.

# Trigger and execution tiers

Not every expensive check must run on every keystroke.

020-G establishes:

| Tier | Typical trigger | Purpose |
|---|---|---|
| **T0 Local** | worktree command | fast implementer repair loop; non-authoritative unless explicitly captured |
| **T1 PR Public** | pull request/head update | required public merge evidence |
| **T2 Exact Candidate** | frozen candidate SHA | package/phase exit evidence and protected evaluation |
| **T3 Main/Integration** | integrated main revision / scheduled deep verification | integration continuity, deeper scanners/scenarios |
| **T4 Release Candidate** | explicit G6 workflow | release artifact, migration/rollout/restore evidence |
| **T5 Production** | explicit production authorization | E7/production evidence only |

T2–T5 runs may not quietly fall back to testing an adjacent SHA.

Developer/PR jobs may use cancellation to save capacity. Once a run is designated as mandatory exit evidence, cancellation yields **INCONCLUSIVE/BLOCKED evidence**, not PASS.

# Exact-revision identity

Every exit-relevant evidence record identifies at least:

~~~text
repository
source_commit_sha
source_tree_sha
workflow_or_evaluator_identity
workflow_definition_revision
run_id / attempt_id
started_at / completed_at
environment_tier
tool/version identity
result
artifact digests
~~~

## Candidate versus integrated revision

020-G distinguishes:

- **base SHA** — exact revision from which an isolated work unit began;
- **candidate SHA** — frozen implementation revision submitted for exit verification;
- **integration SHA** — exact repository revision after accepted integration;
- **release SHA** — explicit source revision used to produce a release candidate.

Pre-merge candidate evidence remains valuable, but downstream current truth must not silently pretend it tested an integration SHA that never ran.

Where integration changes the tested tree or introduces material dependency/configuration changes, affected evidence must be rerun.

A Gatekeeper may use proven tree/content equivalence for evidence that is genuinely invariant to commit metadata, but may not relabel a different source tree as the tested candidate.

# Checkout rule

An exit-evidence workflow must:

1. receive or derive the exact candidate/integration SHA through a governed trigger;
2. fetch that SHA directly;
3. check it out detached or otherwise immutably;
4. record the resulting commit and tree identities;
5. reject an unexpected HEAD;
6. reject uncommitted source mutation before evidence capture;
7. prevent later steps from silently substituting another ref.

A normal pull-request synthetic merge ref is useful compatibility evidence but is not automatically the package's exact-candidate identity.

# Reproducible dependency and toolchain boundary

Future implementation CI preserves:

- committed pnpm lockfile;
- frozen-lockfile installs;
- exact supported Node/pnpm versions;
- bounded lifecycle/build-script execution;
- no mutable VCS-branch dependency for production code;
- explicit dependency origin;
- deterministic generated artifacts;
- pinned scanner/build tool versions for exit evidence;
- committed OpenTofu provider lock information once providers exist;
- immutable container base-image digest for release builds once images exist.

A dependency/tool upgrade is an implementation change and must be evidenced like other source changes.

# GitHub Actions supply-chain rule

IMP-014 must replace mutable action release-tag references used by blocking/exit workflows with immutable full commit-SHA references.

Human-readable comments may retain the upstream release tag for maintainability.

Dependabot may propose updates, but update automation does not bypass review or evidence.

Reusable workflows are preferred over copied security-sensitive step sequences when that reduces drift without obscuring the gate boundary.

# Dependency, vulnerability and license policy

020-G requires a visible policy before a scanner becomes blocking.

The policy must define:

- dependency sources in scope;
- vulnerability severity/age handling;
- direct versus transitive dependency treatment;
- accepted exception authority;
- exception owner, rationale and expiry;
- license categories or explicit allowed/denied policy once legal policy is established;
- treatment of unavailable/failing advisory services;
- evidence retention.

A network/service outage that prevents a mandatory scan is **BLOCKED/INCONCLUSIVE**, not a fabricated clean result.

The repository must not claim "zero dependency vulnerabilities" from Dependabot configuration or workflow existence alone.

# Secret and credential controls

Repository and workflow architecture must provide defense in depth:

- no long-lived AWS deployment keys in source or ordinary GitHub secrets;
- AWS workflows use short-lived OIDC federation when deployment is later implemented;
- protected application secrets stay server-side;
- evidence/logs/artifacts are scrubbed of credentials and unnecessary sensitive data;
- fork/untrusted PRs receive no protected credentials;
- protected evaluator credentials are resource/audience bounded;
- CI token permissions use least privilege;
- write-capable principals are isolated from ordinary verification jobs.

Secret scanning is both pre-merge and provider-side where available.

A scanner finding may be remediated or dispositioned through governed exception; it may not simply be deleted from the report.

# Build once, attest once, promote by digest

Releaseable artifacts are built from an explicit release SHA.

For each build artifact, the system records:

- source SHA/tree;
- build workflow identity/revision;
- dependency lock digest;
- toolchain versions;
- artifact digest;
- SBOM digest/reference;
- provenance/attestation reference;
- scanner result references.

Backend containers use immutable image digests.
Frontend/static artifacts use content-addressed immutable asset identity.
Deployment/promotion references the previously built digest.

Production must not rebuild "the same" source into a different artifact and call it the already-reviewed release.

# SBOM and provenance

IMP-014/015 must produce machine-readable software inventories for deployable artifacts.

The exact representation may use SPDX, CycloneDX or a later accepted equivalent, but the chosen format/version must be explicit and validated.

Build provenance must bind at least:

- source revision;
- build definition identity;
- builder/workflow identity;
- dependency/material identities where practical;
- resulting artifact digest.

Cryptographic attestation is required for releaseable artifacts; 020-G does not require a particular attestation vendor so long as verification is automated and independently checkable.

# Evidence bundle architecture

An implementation package/phase evidence bundle is a **manifest plus referenced evidence**, not a giant opaque archive.

The manifest is immutable after finalization and content-addressed.

Minimum fields include:

~~~text
schema/version
phase/package identity
candidate SHA/tree
integration SHA/tree when applicable
criteria and evidence-obligation versions
public CI results
protected-evaluator result reference
independent review references
adversarial review reference
scanner/security results
scenario/test-control result references
build/SBOM/provenance references when applicable
environment identities
artifact digests
failure/retry history
approved exceptions/waivers
repository-enforcement evidence
residual risks
bundle digest
finalization actor/time
~~~

Every criterion/evidence obligation maps to a concrete result or an approved not-applicable rationale.

A directory of screenshots or logs with no criterion/obligation mapping is not an evidence bundle.

# Public and protected evidence split

The public bundle may contain:

- criterion IDs and PASS/FAIL/BLOCKED/INCONCLUSIVE state;
- candidate SHA;
- evidence class;
- environment/material boundary;
- public test/scanner artifacts;
- protected evaluator run identity;
- protected result digest/attestation;
- repair-facing diagnostic category.

It must not publish:

- hidden fixture values;
- hidden probe source;
- hidden seeds;
- protected evaluator credentials;
- secret interleavings/fault timings whose publication would destroy probe value.

Protected evaluator detail resides in a separate access boundary.

# Protected evaluator result binding

The protected evaluator:

- evaluates the exact candidate SHA;
- records workflow/evaluator definition revision;
- emits a tamper-evident result/attestation;
- exposes required criterion outcomes and safe diagnostics;
- keeps hidden probe material outside the ordinary implementer repository/context;
- cannot write candidate source;
- cannot modify criteria;
- cannot grant G2/G5;
- cannot deploy production.

If secrecy is materially required, evaluator source/probes must not be stored in the same publicly readable repository used by ordinary implementers.

A dedicated private repository/service is a valid realization; exact implementation remains owned by IMP-014.

# Failure, retry and quarantine evidence

An evidence bundle preserves attempt history.

Rules:

- an initial failure remains visible after retry;
- a later passing retry may establish current evidence only after the original failure is understood/dispositioned;
- flaky behavior is an implementation/evidence defect, not a reason to auto-rerun until green;
- quarantine requires owner, reason, affected criterion, expiry/review trigger and alternate evidence or explicit blocked status;
- mandatory security/authority/concurrency/recovery criteria cannot be permanently quarantined away;
- evaluator/service outage produces BLOCKED/INCONCLUSIVE where the evidence is mandatory.

# CI permissions and untrusted-code boundary

Default workflow permissions are read-only.

Additional permissions are granted per job, not globally, and only when the job's responsibility requires them.

Untrusted pull-request code must not receive:

- AWS deployment credentials;
- production/non-production mutation credentials;
- protected evaluator secrets;
- signing/attestation credentials capable of blessing arbitrary artifacts;
- repository administration credentials.

Artifact signing/attestation occurs only after source/revision identity and workflow trust have been established.

# Deployment authority

Verification and deployment workflows are separate authorities.

Later deployment architecture uses:

- GitHub OIDC -> environment/account-scoped AWS role;
- protected GitHub environments where available;
- exact artifact digest;
- explicit source/release identity;
- separately privileged database migrator;
- no application-startup migration;
- no production deployment from an untrusted PR context.

Non-production deployment may support E3–E6 evidence.

Production remains separately authorized and is never triggered merely because a package reaches G5.

# Repository merge-enforcement architecture

For autonomous implementation, documentation/prompt rules alone are insufficient.

Before ordinary autonomous package execution depends on main-branch safety, repository administration should enforce, at minimum:

- pull-request based integration to main;
- required current blocking checks;
- no force push;
- no branch deletion;
- conversation/review resolution as applicable;
- restriction of bypass to explicit human break-glass/administrative authority;
- branch freshness or merge-queue equivalent sufficient to prevent stale integration.

The exact GitHub ruleset/check-name mapping becomes evidence.

Current Phase-020 evidence **does not prove those protections are enforced**.

Therefore 020-G creates a carry-forward administrative obligation:

> **Repository enforcement must be independently observed and recorded before Phase-021 treats main protection as a trusted control.**

Lack of that evidence does not invalidate this design phase; it prevents the later program from claiming the control exists.

# Evidence retention

Evidence retention is proportional.

At minimum retain enough durable metadata to reconstruct:

- what revision was evaluated;
- which requirements/evidence obligations were evaluated;
- which run/tool produced the result;
- what artifact digest was produced;
- what failure/exception occurred;
- which review/gatekeeper decision closed the package/phase.

Large transient logs/videos/traces may use bounded retention.

Release/provenance/security evidence receives longer retention than ordinary developer diagnostics.

Retention must avoid production secrets and unnecessary personal/domain-sensitive content.

# IMP-014 binding

020-G makes IMP-014's purpose concrete.

IMP-014 will own implementation of:

- exact-SHA evidence collector/manifest validator;
- public CI gate mapping;
- protected evaluator runner/result adapter;
- supply-chain/security scanner integration;
- SBOM/provenance/attestation generation and validation;
- evidence artifact retention plumbing;
- repository enforcement evidence capture;
- CI permissions/untrusted-code boundaries.

IMP-014 remains **PROPOSED / not G1-ready / not G2-authorized** because its package-specific visible criteria, cross-cutting 020-I obligations and 020-K final phase assignment are still incomplete.

# IMP-015 binding

IMP-015 will consume the build/provenance contract to implement:

- immutable production/recovery artifacts;
- deployment/recovery workflows;
- OIDC roles and protected deployment authority;
- promotion-by-digest;
- migration/deployment ordering;
- release/restore evidence.

020-G does not authorize those workflows or resources.

# Relationship to 020-F

020-F defines **what evidence a criterion requires**.

020-G defines **how evidence is produced, identified, retained, integrity-checked and handed to the Gatekeeper**.

The two contracts combine as:

~~~text
VISIBLE CRITERION
      |
      v
EVIDENCE OBLIGATION (020-F)
      |
      v
CI / protected / review producer (020-G)
      |
      v
exact-revision evidence record
      |
      v
content-addressed bundle
      |
      v
Gatekeeper exit decision
~~~

# Machine-checkable control

The current projection is:

> `docs/routing/phase020_ci_supplychain_evidence_architecture.json`

Phase-020 validation must fail if this contract drifts into any of the following:

- evidence not bound to exact source revision;
- protected evaluator allowed to modify candidate source;
- production use by the protected evaluator;
- hidden requirements;
- mutable-tag-only blocking action policy;
- evidence retry history erased;
- deployment authority inferred from CI PASS;
- G2/release/production authority granted by 020-G;
- IMP-014 falsely promoted to G1/G2.

# Residual implementation obligations

020-G intentionally does not decide or implement:

- exact third-party scanner products;
- exact SBOM format choice between acceptable standards;
- exact attestation implementation/vendor;
- protected evaluator hosting provider;
- final GitHub required-check names;
- exact evidence-store implementation/retention durations;
- deployment workflow implementation;
- GitHub ruleset administration.

Those become package-specific implementation decisions under the visible 020-G contract.

# Phase-020 boundary after 020-G

~~~text
Phase 020                       ACTIVE
020-A/B/C/D/E/F/G               COMPLETE
020-H                           NEXT ELIGIBLE

proposed packages               15
G1-ready packages               0
G2-authorized packages          0
active implementation packages  0

domain implementation           NOT AUTHORIZED
release                         NOT AUTHORIZED
production                      NOT AUTHORIZED
~~~

# Carry-forward

- **020-H** defines independent code review, adversarial conformance review, repair/reopen and Gatekeeper authority around these evidence bundles.
- **020-I** instantiates migration, recovery, accessibility, performance, cost and scenario verification obligations.
- **020-J** defines whole-system v1 completion/release-candidate boundaries.
- **020-K** completes package-specific criteria/evidence bindings, G1-ready plans and phase assignments.
- **020-L** must verify that repository administration/enforcement evidence and implementation-entry prerequisites are explicitly resolved or carried as blocking Phase-021 start-gate items.

# Exit decision

**020-G — COMPLETE — PASS.**

MUDAC now has an exact-revision CI/security/supply-chain/evidence architecture that preserves the 020-F visible-obligation/protected-probe model while preventing autonomous agents, scanners, retries, mutable artifacts or deployment workflows from manufacturing authority.

Next eligible:

> **020-H — Independent Code Review, Adversarial Review, Repair/Reopen & Exit-Gate Governance**

020-H is **NEXT ELIGIBLE / NOT AUTOMATICALLY AUTHORIZED**.

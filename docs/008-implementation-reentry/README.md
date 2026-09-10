# Phase 008 — Implementation Re-entry, Plan Refresh & Execution Readiness

Status: **In Progress — 008-A/B complete; 008-C next**

## Purpose

Convert the completed Jackson Concept Design baseline and accepted architecture into a refreshed, dependency-safe implementation plan without beginning new MUDAC domain implementation.

Phase 008 exists because the historical 006-E through 006-M plan predates the Phase 007 methodology refinements. Those records remain planning provenance and dependency evidence, but they are not current executable authority.

Current execution posture is owned by [Design / Implementation Boundary](../canonical/governance/design-implementation-boundary.md). Detailed Phase 008 records are indexed in [index.md](index.md).

## Phase boundary

```text
Phase 007
Jackson Concept Design COMPLETE / EXITED
        ↓
Phase 008
plan refresh + execution readiness
        ↓
008-L explicit first-slice authorization
        ↓
Phase 009
new domain implementation begins
```

No Phase 008 subgroup implements new domain behavior. The retained 006-D workspace remains a protected non-domain implementation baseline.

## Completed entry gates

[008-A](008-A-implementation-reentry-authority-canonical-baseline-change-control-planning-guardrails.md) is **Complete** and establishes current authority, `CHG-*` escalation, planning-versus-execution states, and progressive-disclosure/anti-bloat rules.

[008-B](008-B-protected-006-D-baseline-qualification-drift-audit-toolchain-environment-reconciliation.md) is **Complete — PASS AFTER NARROW REMEDIATION** and qualifies the retained 006-D executable substrate for use by later Phase 008 planning.

008-B confirmed:

- the selected Node/pnpm/TypeScript/Fastify/React/Vite/Vitest/Playwright/ESLint/Prettier/dependency-cruiser/OpenTofu pins still match the 006-D declared baseline and committed lockfile;
- the three application roots remain bootstrap/composition only;
- the six authoritative module packages remain minimal placeholder seams;
- `application`, `projections`, `foundation`, and `test-support` remain within their intended boundaries;
- local PostgreSQL remains a schema-free development dependency;
- dependency-cruiser and ESLint enforcement remain present;
- OpenTofu environment/state roots remain separated and contain no AWS application resources;
- recent Knowledge Validation, Implementation Verification, and CodeQL evidence succeeded on the immediately preceding baseline.

008-B repaired only two narrow non-domain drift items: obsolete Phase 006 copy in the bootstrap web page and the obsolete `phase-006-*` special push trigger in Implementation Verification.

The repository-administration residual remains open: no repository rulesets are visible and branch protection cannot be verified by the current integration. Dependabot configuration is visible, but its alert inventory is unavailable through this connector and is not inferred clean.

## Dependency-safe subgroup plan

| Group | Topic | Status |
| --- | --- | --- |
| 008-A | [Implementation Re-entry Authority, Canonical Baseline, Change Control & Planning Guardrails](008-A-implementation-reentry-authority-canonical-baseline-change-control-planning-guardrails.md) | **Complete** |
| 008-B | [Protected 006-D Baseline Qualification, Drift Audit & Toolchain/Environment Reconciliation](008-B-protected-006-D-baseline-qualification-drift-audit-toolchain-environment-reconciliation.md) | **Complete — PASS** |
| 008-C | **Residual-Risk Ingestion, Historical 006 Mapping, Decision Register & Supersession Matrix** | **Next** |
| 008-D | **Persistence, Temporal Truth, Versioning, Provenance, Governed Exceptions, Outbox, Projection & Migration Implementation Plan** | Planned |
| 008-E | **Identity, Authentication, Participation, Access, Session, Invitation, Secrets & Technical-Authority Implementation Plan** | Planned |
| 008-F | **Commands, Queries, Transactions, CAS, Idempotency, Concurrency, Lost-Response Reconciliation & API Implementation Plan** | Planned |
| 008-G | **Browser Shell, Routing, Remote State, Draft Continuity, Synchronization, Recovery, Responsive & Accessibility Implementation Plan** | Planned |
| 008-H | **Competition Configuration, Team/Division/Alias, Rubric, Participation, Panel & Encounter Operations Slice Plan** | Planned |
| 008-I | **Scorecard, Evaluation Evidence, Amendment, Paper Capture, Verification & Convergence Slice Plan** | Planned |
| 008-J | **Reconciliation, Coverage, Aggregate, Rank, Awards, Finalization, Official Outcome, Export, Publication & Disclosure Slice Plan** | Planned |
| 008-K | **Security, Privacy, Accessibility, Observability, Performance, Recovery/DR, Retention & Operational Evidence Plan** | Planned |
| 008-L | **Consolidated Dependency Graph, Implementation Roadmap, First-Slice Authorization & Phase Exit Review** | Planned |

## Dependency rationale

```text
008-A authority and guardrails                         COMPLETE
   ↓
008-B retained substrate qualification                 COMPLETE
   ↓
008-C residual + historical-plan reconciliation        NEXT
   ↓
008-D durable data / temporal authority plan
   ↓
008-E identity / access / session plan
   ↓
008-F command / API / concurrency plan
   ↓
008-G browser / Draft / recovery plan
   ↓
008-H competition + judging operations slices
   ↓
008-I evaluation evidence + paper slices
   ↓
008-J outcomes + externalization slices
   ↓
008-K cross-cutting verification / evidence gates
   ↓
008-L consolidated roadmap + first-slice authorization
   ↓
Phase 009 implementation
```

008-C follows qualification so it can map residuals and historical 006 work against a known-good current substrate rather than an assumed one.

## Planning guardrails

Phase 008 still does not create domain tables, migrations, repositories, authentication/session behavior, domain APIs, IndexedDB domain state, product features, or domain-purpose AWS application resources.

A qualified baseline is not first-slice authorization. Green CI is not implementation authorization, merge authority, deployment authority, or production certification. Historical 006-E–M labels remain non-executable provenance.

If planning exposes a genuine semantic contradiction or missing semantic owner, use `CHG-*`; implementation convenience does not silently weaken current design.

## Current status

```text
Jackson Concept Design: COMPLETE / EXITED
Phase 008 subdivision: COMPLETE
implementation planning authority: ESTABLISHED
008-A: COMPLETE
008-B: COMPLETE — PASS AFTER NARROW REMEDIATION
protected 006-D baseline: QUALIFIED FOR PHASE 008 PLANNING
008-C: NEXT / NOT STARTED
new domain implementation after 006-D: NOT STARTED
first executable slice: NOT YET AUTHORIZED
production readiness: NOT ESTABLISHED
```

## Next

Proceed to **008-C — Residual-Risk Ingestion, Historical 006 Mapping, Decision Register & Supersession Matrix**.

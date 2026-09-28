# 021-I01 — Codex Implementation Context Manifest

**Phase:** 021 — Source Topology & Implementation Foundation  
**Package:** IMP-001  
**Work unit:** 021-I01  
**Gate:** G2 AUTHORIZED  
**Implementer:** Codex  
**Independent reviewer:** Cursor  
**Authorized executable-content baseline:** `fdbcff0ee7e3a08deb870f51659a59b65b333893` / tree `279fb97425d189a843cf90612ee6dff10c520d9c`  
**Authorized implementation checkout:** `7812339629241cb7b4bd34d320166ee27a5c07ff` / tree `4e6924f026d5e9c583df3f020bcfae32d98b3372`

The implementation checkout contains only the G2 authority, validation and status/documentation overlay above the authorized executable-content baseline. The compared diff contains no application/workspace/package/dependency implementation changes. This lets the Codex worktree contain its own authority files without silently adopting later product implementation.

## Authority

Human/program authority explicitly granted G2 for this work unit. This authorization permits only the bounded implementation work below. It does not authorize merge to `main`, release, deployment, production access, Phase 022 work, or architecture/product redesign.

Canonical machine authority:

- `docs/routing/phase021_g2_authorization.json`
- `docs/routing/phase021_start_gate_control.json`
- `docs/routing/phase020_autonomous_implementation_roadmap.json`
- `docs/canonical/architecture/application-ownership-boundaries.md`
- `AGENTS.md`

Read `AGENTS.md` first and resolve current authority from the repository before editing.

## Objective

Bring the executable source topology into conformance with the accepted five-owner architecture by retiring the obsolete empty Judging Operations package shell and the dependency rules that still treat it as an independent owner.

Accepted semantic owners:

1. Competition Context
2. Identity & Access
3. Evaluation
4. Outcomes & Officiality
5. External Representation

`packages/modules/judging-operations` is historical executable residue. It contains no domain behavior that must be migrated.

## In scope

- Remove `packages/modules/judging-operations/` from the executable workspace.
- Remove obsolete workspace/lockfile references to `@mudac/judging-operations`.
- Rewrite `.dependency-cruiser.cjs` to enforce the accepted five-owner topology.
- Preserve public/private package seams and existing implementation-neutral bootstrap/configuration.
- Refresh `pnpm-lock.yaml` only if deterministic workspace-package removal requires it.
- Prove there is no active executable package, workspace importer, dependency rule, source import, build configuration, or current implementation authority that treats Judging Operations as an independent semantic owner.

## Explicitly out of scope

Do not implement or alter:

- domain/business behavior;
- persistence or database schema;
- provider/AWS deployment;
- feature UI;
- authentication/session behavior;
- semantic definitions;
- accepted architecture;
- Phase 022+ package work;
- historical design/provenance documents merely because they mention the former Judging Operations candidate.

Historical/superseded documentation references may remain when they are clearly historical. Do not globally search-and-delete the phrase `Judging Operations` from design history.

## Serialized surfaces

This work unit is the only active writer for:

- `package.json`
- `pnpm-workspace.yaml`
- `pnpm-lock.yaml`
- `.dependency-cruiser.cjs`
- package/module ownership indexes required by the topology repair

If another active writer appears on any of these surfaces, stop.

## Required verification

Run and preserve the results of:

```bash
pnpm install --frozen-lockfile
pnpm verify
python scripts/run_agentic_conformance.py
```

If removal of the workspace package necessarily changes the lockfile, perform the minimal deterministic lockfile refresh, then re-run the frozen install and full verification.

Also perform an explicit residual executable-surface search for:

```text
@mudac/judging-operations
packages/modules/judging-operations
```

A historical documentation hit is not automatically a failure. An active package/import/dependency/build/current-authority hit is.

## Candidate freeze requirements

Before handing off to Cursor:

1. working tree is clean;
2. all authorized changes are committed;
3. branch is pushed as `work/021/imp-001-topology`;
4. exact candidate commit SHA and tree are reported;
5. changed-file list is reported;
6. verification commands/results are reported;
7. residual-reference search is summarized;
8. residual concerns are reported;
9. no further source edits occur until review findings are returned.

## Initial Codex instruction

Use this prompt when starting Codex in the dedicated writable worktree created from `7812339629241cb7b4bd34d320166ee27a5c07ff`:

> You are the Implementer for MUDAC Phase 021 work unit 021-I01 / package IMP-001. G2 is explicitly authorized only for the scope defined by `docs/routing/phase021_g2_authorization.json` and this context manifest. Read `AGENTS.md` and the cited authority files before editing. The executable-content authorization is anchored to `fdbcff0ee7e3a08deb870f51659a59b65b333893`; this checkout adds only the approved G2 governance/validation overlay. Retire the obsolete empty `packages/modules/judging-operations` executable package, remove its workspace/lockfile references, and rewrite dependency-cruiser rules to the accepted five-owner topology. Preserve current semantic behavior and public/private seams. Do not add domain behavior, persistence, provider/deployment, UI, authentication, semantic redesign, architecture changes, or Phase 022 work. Historical documentation may continue to mention Judging Operations where explicitly historical. Stop on any circuit breaker or scope ambiguity. Run the required verification and residual executable-reference search. Commit and push the completed bounded candidate, then report the exact candidate SHA/tree, changed files, commands/results, residual-reference result, and residual concerns. Do not self-review or merge.

## Cursor handoff

Cursor does not begin until Codex freezes a candidate SHA.

Cursor reviews that exact SHA in a separate detached/read-only worktree. Cursor must not edit files while acting as Reviewer. A source edit by Cursor converts it into an Implementer for that revision and requires a fresh independent review.

## Repair budget

- ordinary repair cycles: 3
- repeated materially identical failure threshold: 2
- repairs may not expand G2 scope
- every source-changing repair creates a new candidate SHA
- affected review and verification must rerun

## Circuit breakers

Stop and return to human/program authority if:

- domain behavior becomes necessary;
- architecture appears contradictory;
- a package outside IMP-001 is required;
- another writer owns a serialized surface;
- production access/data/credentials become relevant;
- verification becomes nondeterministic;
- repair would weaken tests/criteria/protection;
- the repair budget is exhausted.

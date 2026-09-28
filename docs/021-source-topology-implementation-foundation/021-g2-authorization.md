# Phase 021 / IMP-001 — G2 Authorization

**Decision:** AUTHORIZED  
**Phase:** 021 — Source Topology & Implementation Foundation  
**Package:** IMP-001  
**Work unit:** 021-I01  
**Implementer:** Codex  
**Reviewer:** Cursor  
**Authorized executable-content baseline:** `fdbcff0ee7e3a08deb870f51659a59b65b333893` / tree `279fb97425d189a843cf90612ee6dff10c520d9c`  
**Authorized implementation checkout:** `7812339629241cb7b4bd34d320166ee27a5c07ff` / tree `4e6924f026d5e9c583df3f020bcfae32d98b3372`

Human/program authority explicitly authorizes G2 for the bounded 021-I01 implementation work defined by `docs/routing/phase021_g2_authorization.json`.

The implementation checkout adds only the approved G2 governance/validation/status overlay above the authorized executable-content baseline. The compared diff contains no application/workspace/package/dependency implementation changes, so Codex can read its local authority files without silently adopting later product implementation.

This authorization permits implementation execution only for IMP-001. It does not authorize merge to `main`, release, deployment, production access, Phase 022, domain behavior, persistence changes, feature UI, semantic redesign, or architecture change.

## Authorized result

The implementation may:

- remove the obsolete empty `packages/modules/judging-operations` package shell;
- remove active workspace/lockfile references to `@mudac/judging-operations`;
- rewrite dependency-cruiser rules from the historical six-owner topology to the accepted five-owner topology;
- make only the minimal implementation-neutral workspace/configuration changes required for that repair;
- run and preserve the required verification/evidence.

The implementation must not globally erase historical design references to Judging Operations. Historical/superseded records remain valid provenance when clearly historical.

## Operating model

One writable Codex worktree is authorized. Create it from the authorized implementation checkout commit `7812339629241cb7b4bd34d320166ee27a5c07ff` on branch `work/021/imp-001-topology`.

Cursor review is read-only and occurs only after Codex freezes a candidate SHA. The two tools must not share a writable checkout.

Candidate source changes after review create a new SHA and require affected review/evidence to rerun.

## Current lifecycle state

~~~text
Phase 021                 ACTIVE
IMP-001                   AUTHORIZED
021-I01                   AUTHORIZED
G2                        GRANTED
implementation execution AUTHORIZED — IMP-001 / 021-I01 ONLY
release                   NOT AUTHORIZED
production                NOT AUTHORIZED
Phase 022                 NOT AUTHORIZED
~~~

The next operational action is creation of the Codex implementation worktree from `7812339629241cb7b4bd34d320166ee27a5c07ff`, followed by execution of the context manifest at `021-I01-context-manifest.md`.

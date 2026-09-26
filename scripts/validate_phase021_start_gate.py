#!/usr/bin/env python3
from __future__ import annotations
import argparse, json
from pathlib import Path

CONTROL = "docs/routing/phase021_start_gate_control.json"
PHASE020 = "docs/routing/phase020_implementation_design_control.json"
ROADMAP = "docs/routing/phase020_autonomous_implementation_roadmap.json"
RUNBOOK = "docs/implementation-roadmap/cursor-codex-autonomous-coding-runbook.md"
PHASE_RECORD = "docs/021-source-topology-implementation-foundation/021-start-gate.md"

def main() -> int:
    parser=argparse.ArgumentParser()
    parser.add_argument("--repo", default=".")
    args=parser.parse_args()
    repo=Path(args.repo).resolve()
    errors=[]
    try:
        control=json.loads((repo/CONTROL).read_text(encoding="utf-8"))
        p20=json.loads((repo/PHASE020).read_text(encoding="utf-8"))
        roadmap=json.loads((repo/ROADMAP).read_text(encoding="utf-8"))
    except Exception as exc:
        print(f"FAIL phase021 start gate unreadable: {exc}")
        return 1

    if p20.get("state",{}).get("status")!="COMPLETE":
        errors.append("Phase 021 requires Phase 020 COMPLETE")
    if control.get("status")!="START_GATE_COMPLETE" or control.get("start_gate_decision")!="PASS_READY_FOR_G2_DECISION":
        errors.append("Phase 021 start gate state drift")
    b=control.get("authority_boundary",{})
    if b.get("g1_state")!="READY_FOR_AUTHORIZATION":
        errors.append("IMP-001 must remain G1 READY_FOR_AUTHORIZATION")
    if b.get("g2_state")!="NOT_AUTHORIZED" or b.get("implementation_execution_authorized") is not False:
        errors.append("Phase 021 start gate must not grant G2 or implementation execution")
    if b.get("coding_before_g2_forbidden") is not True or b.get("automatic_g2") is not False:
        errors.append("coding must remain forbidden before explicit G2")

    entry=control.get("entry_baseline",{})
    if not entry.get("main_sha") or not entry.get("main_tree"):
        errors.append("exact Phase 021 baseline SHA/tree required")
    if entry.get("phase020_complete") is not True or entry.get("main_protected") is not True or entry.get("ruleset_enforcement")!="active":
        errors.append("Phase 021 requires observed protected active main baseline")
    expected_checks={"Validate agentic/documentation conformance","Implementation Verification","CodeQL JavaScript/TypeScript"}
    if set(entry.get("required_checks",[]))!=expected_checks:
        errors.append("Phase 021 required-check set drift")

    pkg=next((x for x in roadmap.get("packages",[]) if x.get("id")=="IMP-001"),None)
    if not pkg or pkg.get("g1_ready") is not True or pkg.get("status")!="READY_FOR_AUTHORIZATION":
        errors.append("020-K IMP-001 package readiness missing")
    if pkg and pkg.get("implementation_phase")!="021":
        errors.append("IMP-001 must remain assigned to Phase 021")

    units=control.get("work_unit_graph",[])
    ids=[x.get("id") for x in units]
    if ids!=["021-I01","021-R01","021-R02","021-V01","021-G01"]:
        errors.append(f"Phase 021 work-unit graph drift: {ids}")
    impl=next((x for x in units if x.get("id")=="021-I01"),{})
    if impl.get("provider")!="CODEX" or impl.get("writable") is not True or impl.get("max_parallel")!=1:
        errors.append("021-I01 must remain one writable Codex work unit")
    for rid in ("021-R01","021-R02"):
        review=next((x for x in units if x.get("id")==rid),{})
        if review.get("provider")!="CURSOR" or review.get("writable") is not False:
            errors.append(f"{rid} must remain read-only Cursor review")
    model=control.get("cursor_codex_operating_model",{})
    if model.get("shared_writable_checkout_forbidden") is not True:
        errors.append("shared Cursor/Codex writable checkout must remain forbidden")
    if "separate" not in str(model.get("review_worktree","")).lower():
        errors.append("review worktree separation must remain explicit")

    g2=control.get("g2_candidate",{})
    if g2.get("eligible_for_human_decision") is not True or g2.get("authorized") is not False:
        errors.append("Phase 021 may be ready for G2 decision but must not pre-authorize it")

    for rel in (RUNBOOK,PHASE_RECORD):
        if not (repo/rel).is_file():
            errors.append(f"missing Phase 021 authority surface: {rel}")

    if errors:
        print("Phase 021 start-gate validation: FAIL")
        for e in errors: print(f"- {e}")
        return 1
    print("Phase 021 start-gate validation: PASS")
    print("IMP-001 G1 READY_FOR_AUTHORIZATION; G2 NOT_AUTHORIZED; implementation execution false.")
    return 0

if __name__=="__main__":
    raise SystemExit(main())

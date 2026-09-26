#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

AUTH = "docs/routing/phase021_g2_authorization.json"
START = "docs/routing/phase021_start_gate_control.json"
ROADMAP = "docs/routing/phase020_autonomous_implementation_roadmap.json"
CONTEXT = "docs/021-source-topology-implementation-foundation/021-I01-context-manifest.md"
RECORD = "docs/021-source-topology-implementation-foundation/021-g2-authorization.md"

EXPECTED_CHECKS = {
    "Validate agentic/documentation conformance",
    "Implementation Verification",
    "CodeQL JavaScript/TypeScript",
}
EXPECTED_SCOPE = {
    "retire packages/modules/judging-operations executable package shell",
    "remove obsolete workspace and lockfile references to @mudac/judging-operations",
    "rewrite dependency-cruiser rules to the accepted five-owner topology",
    "preserve public/private package seam rules",
    "preserve implementation-neutral bootstrap/configuration",
    "prove deterministic build/type/lint/test/dependency verification",
    "prove no active executable package, importer, dependency rule, source import, build configuration, or current implementation authority treats Judging Operations as an independent semantic owner",
}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", default=".")
    args = parser.parse_args()
    repo = Path(args.repo).resolve()
    errors: list[str] = []

    try:
        auth = json.loads((repo / AUTH).read_text(encoding="utf-8"))
        start = json.loads((repo / START).read_text(encoding="utf-8"))
        roadmap = json.loads((repo / ROADMAP).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print("ERROR", exc)
        return 1

    if start.get("status") != "START_GATE_COMPLETE" or start.get("start_gate_decision") != "PASS_READY_FOR_G2_DECISION":
        errors.append("G2 requires a completed passing Phase-021 start gate")
    start_boundary = start.get("authority_boundary", {})
    if start_boundary.get("g2_state") != "NOT_AUTHORIZED" or start_boundary.get("implementation_execution_authorized") is not False:
        errors.append("historical start-gate snapshot must remain pre-G2 evidence")

    if auth.get("authority") != "PHASE-021 / IMP-001 / 021-I01 G2 EXECUTION AUTHORIZATION":
        errors.append("G2 authority identity drift")
    if auth.get("phase") != "021" or auth.get("package_id") != "IMP-001" or auth.get("work_unit_id") != "021-I01":
        errors.append("G2 phase/package/work-unit identity drift")
    if auth.get("gate") != "G2" or auth.get("status") != "AUTHORIZED":
        errors.append("Phase-021 G2 must remain explicitly AUTHORIZED")
    if auth.get("authorization_source") != "EXPLICIT_HUMAN_PROGRAM_AUTHORITY":
        errors.append("G2 must be explicitly human/program authorized")

    baseline = auth.get("authorized_baseline", {})
    if baseline.get("main_sha") != "fdbcff0ee7e3a08deb870f51659a59b65b333893":
        errors.append("G2 authorized main SHA drift")
    if baseline.get("main_tree") != "279fb97425d189a843cf90612ee6dff10c520d9c":
        errors.append("G2 authorized main tree drift")
    if baseline.get("main_protected") is not True or baseline.get("ruleset_enforcement") != "active":
        errors.append("G2 requires observed protected active main baseline")
    if set(baseline.get("required_checks", [])) != EXPECTED_CHECKS:
        errors.append("G2 required-check set drift")

    grant = auth.get("authorization", {})
    if grant.get("implementation_execution_authorized") is not True:
        errors.append("G2 record must grant bounded implementation execution")
    if grant.get("authorized_package_count") != 1 or grant.get("active_package_count") != 1:
        errors.append("G2 must authorize exactly one active package")
    if grant.get("authorized_packages") != ["IMP-001"] or grant.get("authorized_work_units") != ["021-I01"]:
        errors.append("G2 authorization must be limited to IMP-001 / 021-I01")
    for key in ("release_authorized", "production_authorized", "next_phase_authorized", "merge_to_main_authorized_by_g2"):
        if grant.get(key) is not False:
            errors.append(f"G2 authorization.{key} must remain false")

    implementer = auth.get("implementer", {})
    if implementer.get("provider") != "CODEX" or implementer.get("role") != "IMPLEMENTER" or implementer.get("writable") is not True:
        errors.append("021-I01 must remain a writable Codex implementation assignment")
    if implementer.get("max_parallel_work_units") != 1 or implementer.get("branch") != "work/021/imp-001-topology":
        errors.append("021-I01 implementation isolation/branch drift")

    review = auth.get("review", {})
    if review.get("independent_reviewer_provider") != "CURSOR" or review.get("adversarial_reviewer_provider") != "CURSOR":
        errors.append("Phase-021 independent/adversarial review must remain assigned to Cursor")
    if review.get("reviewer_writable") is not False or review.get("fresh_adversarial_session_required") is not True:
        errors.append("Cursor review must remain read-only with fresh adversarial session")
    if review.get("implementer_may_not_self_certify") is not True:
        errors.append("Codex implementer may not self-certify")

    if set(auth.get("scope_in", [])) != EXPECTED_SCOPE:
        errors.append("G2 authorized scope drift")
    scope_out = set(auth.get("scope_out", []))
    required_out = {"domain behavior", "database schema", "provider deployment", "feature UI", "semantic redesign", "architecture change", "Phase 022 or later package work"}
    if not required_out.issubset(scope_out):
        errors.append("G2 scope exclusions are incomplete")

    repair = auth.get("repair_budget", {})
    if repair.get("default_cycles") != 3 or repair.get("repeated_identical_failure_threshold") != 2:
        errors.append("G2 repair budget drift")
    if repair.get("scope_may_expand") is not False or repair.get("every_source_change_requires_new_candidate_sha") is not True:
        errors.append("G2 repair authority must remain bounded and exact-revision based")

    lifecycle = auth.get("lifecycle", {})
    if lifecycle.get("current_state") != "AUTHORIZED" or lifecycle.get("next_expected_state") != "IN_PROGRESS":
        errors.append("G2 lifecycle state drift")
    if lifecycle.get("completion_gate") != "G5" or lifecycle.get("g5_does_not_authorize_phase022") is not True:
        errors.append("G2 must preserve G5/next-phase separation")

    package = next((p for p in roadmap.get("packages", []) if p.get("id") == "IMP-001"), None)
    if not package or package.get("g1_ready") is not True or package.get("implementation_phase") != "021":
        errors.append("IMP-001 roadmap G1/Phase-021 prerequisite drift")

    for rel in (CONTEXT, RECORD):
        if not (repo / rel).is_file():
            errors.append(f"missing G2 authority surface: {rel}")

    context_text = (repo / CONTEXT).read_text(encoding="utf-8") if (repo / CONTEXT).is_file() else ""
    for token in ("fdbcff0ee7e3a08deb870f51659a59b65b333893", "work/021/imp-001-topology", "Codex", "Cursor", "Do not self-review or merge"):
        if token not in context_text:
            errors.append(f"021-I01 context manifest missing required token: {token}")

    for error in errors:
        print("ERROR", error)
    if errors:
        print(f"Phase 021 G2 authorization validation: FAIL ({len(errors)} error(s))")
        return 1
    print("Phase 021 G2 authorization validation: PASS")
    print("IMP-001 / 021-I01 G2 AUTHORIZED; Codex implementation allowed only within bounded scope; release/production/Phase-022 remain unauthorized.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

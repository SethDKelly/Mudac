#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

CONTROL = "docs/routing/phase020_implementation_design_control.json"
FRAMEWORK = "docs/routing/implementation_program_framework.json"
PHASE019 = "docs/routing/phase019_architecture_decision_control.json"
QUALIFICATION = "docs/routing/phase020_substrate_reuse_qualification.json"
PHASE_DIR = "docs/020-autonomous-implementation-program-design-verification-v1-delivery"
EXPECTED = [f"020-{chr(code)}" for code in range(ord("A"), ord("L") + 1)]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", default=".")
    args = parser.parse_args()
    repo = Path(args.repo).resolve()
    errors: list[str] = []

    try:
        control = json.loads((repo / CONTROL).read_text(encoding="utf-8"))
        framework = json.loads((repo / FRAMEWORK).read_text(encoding="utf-8"))
        phase019 = json.loads((repo / PHASE019).read_text(encoding="utf-8"))
        qualification = json.loads((repo / QUALIFICATION).read_text(encoding="utf-8")) if (repo / QUALIFICATION).is_file() else None
    except (OSError, json.JSONDecodeError) as exc:
        print("ERROR", exc)
        return 1

    state = control.get("state", {})
    whole = phase019.get("whole_architecture_acceptance", {})
    if phase019.get("phase019_state", {}).get("status") != "COMPLETE":
        errors.append("Phase 020 requires Phase 019 COMPLETE")
    if whole.get("accepted") is not True:
        errors.append("Phase 020 requires accepted whole architecture")
    if state.get("whole_architecture_accepted") is not True or state.get("g0_satisfied") is not True:
        errors.append("Phase 020 must preserve whole-architecture/G0 acceptance")
    if state.get("automatic_advance") is not False:
        errors.append("Phase 020 automatic advance must remain false")
    if state.get("implementation_execution_authorized") is not False:
        errors.append("Phase 020 must not authorize domain implementation execution")
    if state.get("release_authorized") is not False or state.get("production_authorized") is not False:
        errors.append("Phase 020 must not grant release or production authority")
    if state.get("active_implementation_packages") != 0:
        errors.append("Phase 020 must retain zero active implementation packages")

    plan = control.get("subphase_plan")
    if not isinstance(plan, list):
        errors.append("subphase_plan must be a list")
        plan = []
    ids = [x.get("id") for x in plan if isinstance(x, dict)]
    if ids != EXPECTED:
        errors.append(f"Phase-020 subphase IDs drift: expected {EXPECTED}, got {ids}")

    completed = [x.get("id") for x in plan if isinstance(x, dict) and x.get("status") == "COMPLETE"]
    next_ids = [x.get("id") for x in plan if isinstance(x, dict) and x.get("status") == "NEXT_ELIGIBLE"]
    state_completed = state.get("completed_subphases")
    if completed != state_completed:
        errors.append(f"completed subphase drift: plan={completed}, state={state_completed}")

    if next_ids:
        if len(next_ids) != 1:
            errors.append(f"Phase 020 must have exactly one NEXT_ELIGIBLE subphase while active; got {next_ids}")
        else:
            next_id = next_ids[0]
            idx = EXPECTED.index(next_id)
            if completed != EXPECTED[:idx]:
                errors.append(f"Phase 020 completed prefix must be {EXPECTED[:idx]} before {next_id}; got {completed}")
            if state.get("next_eligible_subphase") != next_id:
                errors.append("next_eligible_subphase drift")
            if state.get("status") != "ACTIVE":
                errors.append("Phase 020 must be ACTIVE while a NEXT_ELIGIBLE subphase exists")
    else:
        if completed != EXPECTED:
            errors.append("Phase 020 without NEXT_ELIGIBLE must have all A-L COMPLETE")
        if state.get("status") != "COMPLETE":
            errors.append("fully completed Phase 020 must be COMPLETE")
        if state.get("next_eligible_subphase") is not None:
            errors.append("closed Phase 020 must have no next eligible subphase")

    if state.get("currently_authorized_subphase") is not None:
        errors.append("persisted Phase-020 resting state must not imply automatic subphase authorization")

    counts = control.get("counts", {})
    if counts.get("planned_subphases") != len(EXPECTED):
        errors.append("planned_subphases count drift")
    if counts.get("completed_subphases") != len(completed):
        errors.append("completed_subphases count drift")
    if counts.get("active_implementation_packages") != 0 or counts.get("g2_authorized_packages") != 0:
        errors.append("Phase 020 must retain zero active/G2-authorized packages")

    contract = control.get("phase_contract_model", {})
    required_true = [
        "start_gate_required",
        "phase_definition_required",
        "visible_success_criteria_required",
        "required_evidence_visible",
        "g2_execution_authorization_required",
        "independent_code_review_required",
        "adversarial_conformance_review_required",
        "exact_sha_ci_required",
        "hidden_evaluation_allowed",
        "hidden_requirements_forbidden",
        "repair_loop_required",
    ]
    for key in required_true:
        if contract.get(key) is not True:
            errors.append(f"phase_contract_model.{key} must be true")
    if contract.get("implementer_may_self_close") is not False:
        errors.append("implementer may not self-close an implementation phase")
    if contract.get("automatic_next_phase_authorization") is not False:
        errors.append("next implementation phase must not auto-authorize")

    roles = control.get("autonomous_roles", {})
    for key in ("implementer", "reviewer", "verifier", "gatekeeper", "authorizer"):
        if not roles.get(key):
            errors.append(f"autonomous role {key} must be defined")

    mcp = control.get("mcp_test_control_plane", {})
    if mcp.get("environment") != "NON_PRODUCTION_ONLY":
        errors.append("MCP test-control plane must be NON_PRODUCTION_ONLY")
    for key in (
        "normal_application_boundaries_required",
        "synthetic_fixtures_default",
        "action_trace_correlation_required",
        "production_target_forbidden",
        "arbitrary_sql_forbidden",
        "arbitrary_shell_forbidden",
        "arbitrary_cloud_admin_forbidden",
        "secret_retrieval_forbidden",
        "semantic_authority_bypass_forbidden",
        "hidden_evaluator_separate_from_mcp_server",
    ):
        if mcp.get(key) is not True:
            errors.append(f"mcp_test_control_plane.{key} must be true")

    v1 = control.get("v1_boundary", {})
    for key in (
        "final_integrated_v1_phase_required",
        "whole_system_hardening_required",
        "all_15_scenarios_required",
        "architecture_conformance_required",
        "implementation_complete_not_equal_release_candidate",
        "implementation_complete_not_equal_production_ready",
    ):
        if v1.get(key) is not True:
            errors.append(f"v1_boundary.{key} must be true")

    boundary = control.get("implementation_boundary", {})
    if boundary.get("mudac_domain_implementation_authorized") is not False:
        errors.append("Phase 020 boundary must keep domain implementation unauthorized")
    if boundary.get("production_mcp_deployment_forbidden") is not True:
        errors.append("production MCP deployment must remain forbidden in Phase 020")
    if boundary.get("active_g2_authorizations") != []:
        errors.append("Phase 020 must not carry active G2 authorizations")

    if "020-B" in completed:
        if qualification is None:
            errors.append("020-B completion requires substrate reuse qualification register")
        else:
            if control.get("substrate_reuse_qualification") != QUALIFICATION:
                errors.append("Phase-020 control must point to substrate reuse qualification")
            candidates = qualification.get("historical_candidates")
            if not isinstance(candidates, list) or len(candidates) != 6:
                errors.append("020-B must qualify exactly six historical implementation candidates")
            elif any(item.get("disposition") != "REUSE_WITH_REVISION" for item in candidates if isinstance(item, dict)):
                errors.append("all six historical implementation candidates must remain REUSE_WITH_REVISION at 020-B")
            substrate = qualification.get("executable_substrate")
            if not isinstance(substrate, list) or len(substrate) < 15:
                errors.append("020-B executable substrate inventory is incomplete")
            else:
                old_topology = next((item for item in substrate if item.get("id") == "SUB-007"), None)
                if not old_topology or old_topology.get("disposition") != "REPLACE":
                    errors.append("020-B must mark the historical six-module topology for replacement/merge")
            qcounts = qualification.get("counts", {})
            if qcounts.get("workspace_packages") != 13:
                errors.append("020-B baseline workspace-package count drift")
            if qcounts.get("authored_test_files") != 0 or qcounts.get("migration_files") != 0:
                errors.append("020-B baseline must not fabricate existing tests or migrations")
            qboundary = qualification.get("execution_boundary", {})
            if qboundary.get("active_implementation_packages") != 0 or qboundary.get("g2_authorized_packages") != 0:
                errors.append("020-B qualification cannot create implementation packages/G2 authority")
            if qboundary.get("domain_implementation_authorized") is not False:
                errors.append("020-B qualification cannot authorize domain implementation")
            admin = qualification.get("repository_administration", {})
            if admin.get("enforced_merge_policy_claim_allowed") is not False:
                errors.append("020-B must not claim enforced merge policy from workflow existence")

    fw_state = framework.get("state", {})
    if fw_state.get("package_derivation_allowed") is not True:
        errors.append("G0 package derivation must remain allowed")
    if fw_state.get("implementation_execution_authorized") is not False:
        errors.append("implementation framework must retain execution=false")
    if fw_state.get("active_package_count") != 0 or fw_state.get("active_packages") != []:
        errors.append("implementation framework must retain zero active packages")
    if framework.get("phase020_design_control") != CONTROL:
        errors.append("implementation framework must point to Phase-020 design control")
    phase020_fw = framework.get("phase020_program_design", {})
    if phase020_fw.get("completed_subphases") != completed:
        errors.append("implementation framework Phase-020 completed-subphase state drift")
    expected_next = state.get("next_eligible_subphase")
    if phase020_fw.get("next_eligible_subphase") != expected_next:
        errors.append("implementation framework Phase-020 next-eligible state drift")
    if "020-B" in completed and phase020_fw.get("substrate_reuse_qualification") != QUALIFICATION:
        errors.append("implementation framework must reference 020-B reuse qualification after completion")

    gate = framework.get("future_start_gate", {})
    if gate.get("decomposition_state") != "PHASE_020_START_GATE_COMPLETE":
        errors.append("implementation framework must record Phase-020 start gate complete")
    if gate.get("completed_by") != "020-A":
        errors.append("Phase-020 start gate completion must be attributed to 020-A")

    for rel in (
        f"{PHASE_DIR}/README.md",
        f"{PHASE_DIR}/index.md",
        f"{PHASE_DIR}/020-A-start-gate-authority-accepted-baseline-autonomous-development-method.md",
        *([f"{PHASE_DIR}/020-B-existing-substrate-historical-implementation-reuse-qualification.md"] if "020-B" in completed else []),
    ):
        if not (repo / rel).is_file():
            errors.append(f"missing Phase-020 authority surface: {rel}")

    for error in errors:
        print("ERROR", error)
    print(
        "Phase-020 implementation design control: "
        f"{len(errors)} error(s), {len(completed)} subphase(s) complete, "
        f"next={state.get('next_eligible_subphase')}, "
        f"active_packages={state.get('active_implementation_packages')}, "
        f"implementation_execution_authorized={state.get('implementation_execution_authorized')}"
    )
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())

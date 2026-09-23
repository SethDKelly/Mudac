#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

CONTROL = "docs/routing/phase020_implementation_design_control.json"
FRAMEWORK = "docs/routing/implementation_program_framework.json"
PHASE019 = "docs/routing/phase019_architecture_decision_control.json"
QUALIFICATION = "docs/routing/phase020_substrate_reuse_qualification.json"
OPERATING = "docs/routing/autonomous_implementation_operating_model.json"
TEST_CONTROL = "docs/routing/phase020_nonproduction_test_control_architecture.json"
PACKAGE_DISCOVERY = "docs/routing/phase020_implementation_package_discovery.json"
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
        operating = json.loads((repo / OPERATING).read_text(encoding="utf-8")) if (repo / OPERATING).is_file() else None
        test_control = json.loads((repo / TEST_CONTROL).read_text(encoding="utf-8")) if (repo / TEST_CONTROL).is_file() else None
        package_discovery = json.loads((repo / PACKAGE_DISCOVERY).read_text(encoding="utf-8")) if (repo / PACKAGE_DISCOVERY).is_file() else None
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

    if "020-C" in completed:
        if operating is None:
            errors.append("020-C completion requires autonomous implementation operating model")
        else:
            if control.get("autonomous_implementation_operating_model") != OPERATING:
                errors.append("Phase-020 control must point to autonomous implementation operating model")
            activation = operating.get("activation", {})
            if activation.get("requires_g2") is not True:
                errors.append("020-C operating model must require G2")
            if activation.get("phase020_domain_execution_authorized") is not False:
                errors.append("020-C cannot authorize Phase-020 domain implementation")
            delegation = operating.get("delegation", {})
            if delegation.get("mode") != "COORDINATOR_ONLY_WITHIN_ACTIVE_G2_ENVELOPE":
                errors.append("020-C delegation mode drift")
            if delegation.get("max_delegation_depth") != 1:
                errors.append("020-C recursive delegation must remain prohibited")
            roles = operating.get("roles", {})
            if roles.get("coordinator", {}).get("may_grant_g2") is not False:
                errors.append("Coordinator may not grant G2")
            if roles.get("implementer", {}).get("may_self_close_phase") is not False:
                errors.append("Implementer may not self-close phase")
            if roles.get("reviewer", {}).get("independent_run_required") is not True:
                errors.append("020-C requires independent reviewer run")
            isolation = operating.get("work_isolation", {})
            if isolation.get("exact_base_sha_required") is not True or isolation.get("isolated_writable_worktree_required") is not True:
                errors.append("020-C requires exact-base isolated writable worktrees")
            provenance = operating.get("provenance", {})
            if provenance.get("technical_not_domain_provenance") is not True:
                errors.append("020-C technical agent provenance must remain distinct from domain Provenance")
            completion = operating.get("completion", {})
            if completion.get("next_phase_g2") != "NOT_GRANTED":
                errors.append("020-C completion must not auto-grant next-phase G2")
            if not (repo / ".cursor" / "worktrees.json").is_file():
                errors.append("020-C requires Cursor worktree setup adapter")

    if "020-D" in completed:
        if test_control is None:
            errors.append("020-D completion requires non-production test-control architecture")
        else:
            if control.get("nonproduction_test_control_architecture") != TEST_CONTROL:
                errors.append("Phase-020 control must point to non-production test-control architecture")
            if test_control.get("status") != "ACCEPTED_FOR_IMPLEMENTATION_DESIGN":
                errors.append("020-D test-control architecture must be accepted for implementation design")
            if test_control.get("implementation_status") != "NOT_IMPLEMENTED":
                errors.append("020-D must not claim test-control implementation")
            denial = test_control.get("production_denial", {})
            required_denial = (
                "production_target_forbidden",
                "arbitrary_target_url_forbidden",
                "environment_registry_required",
                "nonproduction_account_allowlist_required",
                "production_iac_must_exclude_test_control",
                "production_route_must_not_exist",
                "production_fault_hooks_forbidden",
                "production_fixture_reset_endpoint_forbidden",
                "production_test_control_role_forbidden",
                "fail_closed",
            )
            for key in required_denial:
                if denial.get(key) is not True:
                    errors.append(f"020-D production_denial.{key} must be true")
            protocol = test_control.get("protocol", {})
            if protocol.get("target_revision") != "2026-07-28":
                errors.append("020-D MCP target revision drift")
            if protocol.get("shared_transport") != "STREAMABLE_HTTP_STATELESS":
                errors.append("020-D shared MCP transport must remain stateless Streamable HTTP")
            auth = test_control.get("authorization", {})
            for key in ("remote_auth_required_for_all_tools","audience_resource_validation_required","token_passthrough_forbidden","technical_principal_distinct_from_mudac_actor"):
                if auth.get(key) is not True:
                    errors.append(f"020-D authorization.{key} must be true")
            planes = test_control.get("planes", {})
            if planes.get("fixture", {}).get("direct_seed_counts_as_command_evidence") is not False:
                errors.append("020-D direct fixture seeding must not count as command evidence")
            if planes.get("action", {}).get("real_application_boundaries_required") is not True:
                errors.append("020-D behavior testing must use real application boundaries")
            if planes.get("action", {}).get("mcp_token_to_mudac_access_translation") is not False:
                errors.append("020-D MCP technical token must not become MUDAC Access")
            for key in ("arbitrary_external_navigation","arbitrary_javascript_eval","arbitrary_local_file_access","credential_extraction"):
                if planes.get("browser", {}).get(key) is not False:
                    errors.append(f"020-D browser.{key} must remain false")
            if planes.get("observation", {}).get("unrestricted_log_search") is not False:
                errors.append("020-D observation must not expose unrestricted logs")
            if planes.get("fault", {}).get("registered_profiles_only") is not True:
                errors.append("020-D fault injection must remain profile-bounded")
            if planes.get("fault", {}).get("arbitrary_aws_command") is not False or planes.get("fault", {}).get("arbitrary_shell") is not False:
                errors.append("020-D fault plane must not expose arbitrary AWS/shell execution")
            hidden = test_control.get("hidden_evaluator", {})
            if hidden.get("hidden_requirements_forbidden") is not True or hidden.get("production_use_forbidden") is not True:
                errors.append("020-D hidden evaluator must hide probes, not requirements, and remain nonproduction")
            evidence = test_control.get("evidence_boundary", {})
            if evidence.get("cannot_create") != "E7_PRODUCTION_EVIDENCE":
                errors.append("020-D nonproduction plane must not create E7 evidence")
            phase_boundary = test_control.get("phase020_boundary", {})
            if phase_boundary.get("mcp_server_implemented") is not False or phase_boundary.get("environment_deployed") is not False:
                errors.append("020-D design phase must not claim MCP/environment implementation")
            if phase_boundary.get("active_implementation_packages") != 0 or phase_boundary.get("g2_authorized_packages") != 0:
                errors.append("020-D must retain zero active/G2-authorized packages")
            if phase_boundary.get("domain_implementation_authorized") is not False:
                errors.append("020-D must retain domain implementation unauthorized")

    if "020-E" in completed:
        if package_discovery is None:
            errors.append("020-E completion requires implementation package discovery graph")
        else:
            if control.get("implementation_package_discovery") != PACKAGE_DISCOVERY:
                errors.append("Phase-020 control must point to implementation package discovery graph")
            semantics = package_discovery.get("semantics", {})
            if semantics.get("proposed_package_count") != 15:
                errors.append("020-E must retain exactly 15 proposed package candidates")
            if semantics.get("proposed_packages_are_active") is not False:
                errors.append("020-E proposed packages must not be active")
            if semantics.get("g1_satisfied") is not False or semantics.get("g2_authorized") is not False:
                errors.append("020-E package discovery must not satisfy G1 or G2")
            if semantics.get("implementation_execution_authorized") is not False:
                errors.append("020-E package discovery must not authorize implementation execution")

            packages = package_discovery.get("candidate_packages")
            if not isinstance(packages, list):
                errors.append("020-E candidate_packages must be a list")
                packages = []
            expected_pkg_ids = [f"IMP-{i:03d}" for i in range(1, 16)]
            pkg_ids = [p.get("id") for p in packages if isinstance(p, dict)]
            if pkg_ids != expected_pkg_ids:
                errors.append(f"020-E package ID drift: expected {expected_pkg_ids}, got {pkg_ids}")
            if len(set(pkg_ids)) != len(pkg_ids):
                errors.append("020-E package IDs must be unique")
            for pkg in packages:
                if not isinstance(pkg, dict):
                    continue
                if pkg.get("status") != "PROPOSED":
                    errors.append(f"{pkg.get('id')}: 020-E packages must remain PROPOSED")
                if pkg.get("g1_ready") is not False:
                    errors.append(f"{pkg.get('id')}: 020-E package must not be G1-ready")
                if not pkg.get("g1_missing"):
                    errors.append(f"{pkg.get('id')}: missing explicit G1 carry-forward")

            pkg_set = set(pkg_ids)
            hard_edges = package_discovery.get("hard_edges", [])
            adjacency = {pid: [] for pid in pkg_ids}
            indegree = {pid: 0 for pid in pkg_ids}
            for edge in hard_edges:
                if not isinstance(edge, dict):
                    errors.append("020-E hard edge must be an object")
                    continue
                src, dst = edge.get("from"), edge.get("to")
                if src not in pkg_set or dst not in pkg_set:
                    errors.append(f"020-E hard edge references unknown package: {src}->{dst}")
                    continue
                if src == dst:
                    errors.append(f"020-E hard edge self-cycle: {src}")
                    continue
                adjacency[src].append(dst)
                indegree[dst] += 1
            queue = [pid for pid in pkg_ids if indegree[pid] == 0]
            visited = []
            while queue:
                node = queue.pop(0)
                visited.append(node)
                for nxt in adjacency[node]:
                    indegree[nxt] -= 1
                    if indegree[nxt] == 0:
                        queue.append(nxt)
            if len(visited) != len(pkg_ids):
                errors.append("020-E hard dependency graph must remain acyclic")

            for pkg in packages:
                if not isinstance(pkg, dict):
                    continue
                for dep_key in ("hard_dependencies", "integration_dependencies", "evidence_dependencies"):
                    for dep in pkg.get(dep_key, []):
                        if dep not in pkg_set:
                            errors.append(f"{pkg.get('id')}: unknown {dep_key} dependency {dep}")
                        if dep == pkg.get("id"):
                            errors.append(f"{pkg.get('id')}: self dependency in {dep_key}")

            scenario_coverage = package_discovery.get("scenario_seed_coverage", {})
            expected_scenarios = framework.get("scenario_seeds", [])
            if set(scenario_coverage) != set(expected_scenarios):
                errors.append("020-E scenario coverage keys must exactly match IPG scenario seeds")
            for scenario in expected_scenarios:
                owners = scenario_coverage.get(scenario)
                if not isinstance(owners, list) or not owners:
                    errors.append(f"020-E scenario seed has no proposed package owner: {scenario}")
                elif any(owner not in pkg_set for owner in owners):
                    errors.append(f"020-E scenario seed references unknown package: {scenario}")

            if package_discovery.get("phase_grouping_status") != "DEFERRED_TO_020-K":
                errors.append("020-E must defer final phase grouping to 020-K")
            if package_discovery.get("final_v1_integration_phase_status") != "DEFERRED_TO_020-J":
                errors.append("020-E must defer final v1 integration phase to 020-J")

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
    if "020-C" in completed and phase020_fw.get("autonomous_implementation_operating_model") != OPERATING:
        errors.append("implementation framework must reference 020-C operating model after completion")
    if "020-D" in completed and phase020_fw.get("nonproduction_test_control_architecture") != TEST_CONTROL:
        errors.append("implementation framework must reference 020-D test-control architecture after completion")
    if "020-E" in completed and phase020_fw.get("implementation_package_discovery") != PACKAGE_DISCOVERY:
        errors.append("implementation framework must reference 020-E package discovery after completion")
    if "020-E" in completed:
        if phase020_fw.get("proposed_package_count") != 15:
            errors.append("implementation framework proposed package count drift")
        if phase020_fw.get("g1_ready_package_count") != 0 or phase020_fw.get("g2_authorized_package_count") != 0:
            errors.append("implementation framework must keep 020-E packages below G1/G2")
        if phase020_fw.get("active_package_count") != 0:
            errors.append("implementation framework must keep proposed packages inactive")
        if phase020_fw.get("package_graph_acyclic") is not True:
            errors.append("implementation framework must record acyclic 020-E graph")

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
        *([f"{PHASE_DIR}/020-C-cursor-codex-roles-work-isolation-context-provenance-autonomy-circuit-breakers.md"] if "020-C" in completed else []),
        *([f"{PHASE_DIR}/020-D-nonproduction-environment-synthetic-data-observability-mcp-agent-test-control-plane-architecture.md"] if "020-D" in completed else []),
        *([f"{PHASE_DIR}/020-E-implementation-phase-package-discovery-dependency-graph-parallelism-sequencing.md"] if "020-E" in completed else []),
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

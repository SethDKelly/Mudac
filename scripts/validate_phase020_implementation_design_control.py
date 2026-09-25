#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

CONTROL = "docs/routing/phase020_implementation_design_control.json"
FRAMEWORK = "docs/routing/implementation_program_framework.json"
PHASE019 = "docs/routing/phase019_architecture_decision_control.json"
QUALIFICATION = "docs/routing/phase020_substrate_reuse_qualification.json"
OPERATING = "docs/routing/autonomous_implementation_operating_model.json"
TEST_CONTROL = "docs/routing/phase020_nonproduction_test_control_architecture.json"
PACKAGE_DISCOVERY = "docs/routing/phase020_implementation_package_discovery.json"
PHASE_CONTRACT = "docs/routing/phase020_implementation_phase_contract.json"
CI_EVIDENCE = "docs/routing/phase020_ci_supplychain_evidence_architecture.json"
REVIEW_EXIT = "docs/routing/phase020_review_repair_exit_gate_governance.json"
CROSSCUT = "docs/routing/phase020_crosscutting_verification_architecture.json"
V1_COMPLETION = "docs/routing/phase020_v1_completion_integration_design.json"
ROADMAP = "docs/routing/phase020_autonomous_implementation_roadmap.json"
PREIMPLEMENTATION_AUDIT = "docs/routing/phase020_preimplementation_exit_audit.json"
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
        phase_contract = json.loads((repo / PHASE_CONTRACT).read_text(encoding="utf-8")) if (repo / PHASE_CONTRACT).is_file() else None
        ci_evidence = json.loads((repo / CI_EVIDENCE).read_text(encoding="utf-8")) if (repo / CI_EVIDENCE).is_file() else None
        review_exit = json.loads((repo / REVIEW_EXIT).read_text(encoding="utf-8")) if (repo / REVIEW_EXIT).is_file() else None
        crosscut = json.loads((repo / CROSSCUT).read_text(encoding="utf-8")) if (repo / CROSSCUT).is_file() else None
        v1_completion = json.loads((repo / V1_COMPLETION).read_text(encoding="utf-8")) if (repo / V1_COMPLETION).is_file() else None
        roadmap = json.loads((repo / ROADMAP).read_text(encoding="utf-8")) if (repo / ROADMAP).is_file() else None
        preimplementation_audit = json.loads((repo / PREIMPLEMENTATION_AUDIT).read_text(encoding="utf-8")) if (repo / PREIMPLEMENTATION_AUDIT).is_file() else None
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

    if "020-G" in completed:
        sha_re = re.compile(r"^[0-9a-f]{40}$")
        workflow_dir = repo / ".github" / "workflows"
        if not workflow_dir.is_dir():
            errors.append("020-G requires repository workflows for CI/evidence controls")
        else:
            workflow_files = sorted(list(workflow_dir.glob("*.yml")) + list(workflow_dir.glob("*.yaml")))
            if not workflow_files:
                errors.append("020-G requires at least one GitHub Actions workflow")
            for workflow_path in workflow_files:
                for lineno, line in enumerate(workflow_path.read_text(encoding="utf-8").splitlines(), start=1):
                    match = re.match(r"^\s*uses:\s*([^\s@]+)@([^\s#]+)", line)
                    if not match:
                        continue
                    action, ref = match.groups()
                    if action.startswith("./"):
                        continue
                    if not sha_re.fullmatch(ref):
                        errors.append(
                            f"{workflow_path.relative_to(repo)}:{lineno}: external action {action}@{ref} "
                            "must be pinned to an immutable full commit SHA"
                        )

            knowledge_workflow = workflow_dir / "knowledge-validation.yml"
            if not knowledge_workflow.is_file():
                errors.append("Knowledge Validation workflow is required")
            else:
                knowledge_text = knowledge_workflow.read_text(encoding="utf-8")
                if "\n  pull_request:\n" not in knowledge_text:
                    errors.append("Knowledge Validation must define a pull_request trigger")
                else:
                    pr_tail = knowledge_text.split("\n  pull_request:\n", 1)[1]
                    next_top = re.search(r"\n  [A-Za-z_][A-Za-z0-9_-]*:\s*(?:\n|$)", pr_tail)
                    pr_block = pr_tail[:next_top.start()] if next_top else pr_tail
                    if "    paths:" in pr_block or "    paths-ignore:" in pr_block:
                        errors.append("Knowledge Validation pull_request trigger must not use path filters when required universally")
                    if "    branches:" not in pr_block or "      - main" not in pr_block:
                        errors.append("Knowledge Validation pull_request trigger must explicitly target main")

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

    if "020-F" in completed:
        if phase_contract is None:
            errors.append("020-F completion requires implementation phase contract")
        else:
            if control.get("implementation_phase_contract") != PHASE_CONTRACT:
                errors.append("Phase-020 control must point to implementation phase contract")
            boundary_f = phase_contract.get("boundary", {})
            if boundary_f.get("phase020_execution_authorized") is not False:
                errors.append("020-F contract must not authorize Phase-020 implementation")
            if boundary_f.get("active_packages") != 0 or boundary_f.get("g2_authorized_packages") != 0:
                errors.append("020-F contract must retain zero active/G2 packages")
            if boundary_f.get("contract_definition_does_not_make_packages_g1_ready") is not True:
                errors.append("020-F contract must not make packages G1-ready merely by existing")
            if boundary_f.get("contract_definition_does_not_grant_g2") is not True:
                errors.append("020-F contract must not grant G2")

            phase_def = phase_contract.get("phase_contract", {})
            required_sections = set(phase_def.get("required_sections", []))
            for required_section in (
                "visible_success_criteria",
                "evidence_obligations",
                "scenario_obligations",
                "declared_work_unit_graph",
                "g2_authorization_record",
                "exit_gate_contract",
            ):
                if required_section not in required_sections:
                    errors.append(f"020-F phase contract missing required section: {required_section}")
            if phase_def.get("package_scope_inference_forbidden") is not True:
                errors.append("020-F phase contract must forbid implicit package scope")
            if phase_def.get("next_phase_auto_authorization") is not False:
                errors.append("020-F contract must not auto-authorize next phase")

            g1 = phase_contract.get("package_g1_contract", {})
            if g1.get("package_g1_is_execution_authority") is not False:
                errors.append("020-F must preserve G1 != execution authority")
            for required_item in (
                "visible_success_criteria_instantiated",
                "required_evidence_obligations_instantiated",
                "scenario_obligations_instantiated",
                "semantic_architecture_engineering_traceability_complete",
            ):
                if required_item not in g1.get("required_before_g1", []):
                    errors.append(f"020-F G1 contract missing requirement: {required_item}")

            criterion = phase_contract.get("visible_success_criterion_schema", {})
            criterion_fields = set(criterion.get("required_fields", []))
            for field in ("id","statement","authority_refs","evidence_floor","material_boundary","verification_visibility","failure_class"):
                if field not in criterion_fields:
                    errors.append(f"020-F success criterion schema missing field: {field}")
            if criterion.get("normative_threshold_rule") != "ANY_THRESHOLD_THAT_DEFINES_ACCEPTANCE_OR_PRODUCT_RUNTIME_OBLIGATION_MUST_BE_VISIBLE":
                errors.append("020-F normative acceptance thresholds must remain visible")
            if criterion.get("test_name_as_criterion_forbidden_unless_test_itself_is_deliverable") is not True:
                errors.append("020-F must prohibit test-name-as-success-criterion overfitting")

            visibility = phase_contract.get("verification_visibility", {})
            public = visibility.get("PUBLIC", {})
            protected = visibility.get("PROTECTED", {})
            must_include = set(public.get("must_include", []))
            for item in (
                "all_requirements_and_semantic_obligations",
                "success_criteria",
                "normative_acceptance_thresholds",
                "required_evidence_classes_and_material_boundaries",
                "mandatory_scenario_categories",
            ):
                if item not in must_include:
                    errors.append(f"020-F public contract must include {item}")
            may_not_hide = set(protected.get("may_not_hide", []))
            for item in (
                "product_or_semantic_requirement",
                "accepted_architecture_rule",
                "normative_acceptance_threshold",
                "required_evidence_class",
                "required_material_boundary",
                "mandatory_scenario_category",
                "security_or_disclosure_property",
                "accessibility_target",
                "migration_or_recovery_obligation",
            ):
                if item not in may_not_hide:
                    errors.append(f"020-F protected evaluator must not hide {item}")
            if set(protected.get("may_hide", [])) & may_not_hide:
                errors.append("020-F protected may_hide and may_not_hide sets must be disjoint")

            evaluator = phase_contract.get("protected_evaluator", {})
            for key in (
                "separate_runtime_or_principal",
                "derives_only_from_visible_contract",
                "hidden_requirements_forbidden",
                "secret_semantic_bypass_forbidden",
                "production_use_forbidden",
                "evaluates_exact_candidate_revision",
                "direct_fixture_seed_cannot_prove_bypassed_command",
            ):
                if evaluator.get(key) is not True:
                    errors.append(f"020-F protected_evaluator.{key} must be true")
            for key in ("modifies_candidate_code","grants_g2","grants_next_phase_authority"):
                if evaluator.get(key) is not False:
                    errors.append(f"020-F protected_evaluator.{key} must be false")

            result = phase_contract.get("evaluation_result_contract", {})
            if set(result.get("fail_closed_states", [])) != {"FAIL","BLOCKED","INCONCLUSIVE"}:
                errors.append("020-F required criterion failures must fail closed on FAIL/BLOCKED/INCONCLUSIVE")
            if "NOT_APPLICABLE_WITH_APPROVED_RATIONALE" not in result.get("per_criterion_states", []):
                errors.append("020-F NOT_APPLICABLE must require approved rationale")

            exit_contract = phase_contract.get("phase_exit_contract", {})
            for key in (
                "candidate_revision_frozen_for_review",
                "exact_sha_required",
                "public_ci_required",
                "independent_code_review_required",
                "adversarial_conformance_review_required",
                "mandatory_evidence_bundle_required",
                "traceability_current_required",
                "unresolved_blocker_forbidden",
                "implementer_self_close_forbidden",
                "gatekeeper_may_record_complete_only_when_predicates_pass",
            ):
                if exit_contract.get(key) is not True:
                    errors.append(f"020-F exit contract.{key} must be true")
            if exit_contract.get("next_phase_result") != "NEXT_ELIGIBLE_NOT_AUTHORIZED":
                errors.append("020-F exit contract must not authorize the next phase")

            relation = phase_contract.get("package_discovery_relation", {})
            if relation.get("source") != PACKAGE_DISCOVERY or relation.get("proposed_package_count") != 15:
                errors.append("020-F package-discovery relationship drift")
            if relation.get("package_specific_criteria_instantiated_by_020f") is not False:
                errors.append("020-F must not claim package-specific criteria are already instantiated")
            if relation.get("g1_ready_count_after_020f") != 0:
                errors.append("020-F must retain zero G1-ready packages")

    if "020-G" in completed:
        if ci_evidence is None:
            errors.append("020-G completion requires CI/supply-chain/evidence architecture")
        else:
            if control.get("ci_supplychain_evidence_architecture") != CI_EVIDENCE:
                errors.append("Phase-020 control must point to 020-G CI/supply-chain/evidence architecture")
            boundary_g = ci_evidence.get("boundary", {})
            for key in ("design_only",):
                if boundary_g.get(key) is not True:
                    errors.append(f"020-G boundary.{key} must be true")
            for key in ("implementation_execution_authorized","release_authorized","production_authorized","ci_pass_grants_merge_authority","merge_grants_deploy_authority","deploy_grants_production_readiness"):
                if boundary_g.get(key) is not False:
                    errors.append(f"020-G boundary.{key} must be false")
            if boundary_g.get("active_packages") != 0 or boundary_g.get("g2_authorized_packages") != 0 or boundary_g.get("g1_ready_packages") != 0:
                errors.append("020-G must retain zero active/G1-ready/G2-authorized packages")

            exact = ci_evidence.get("exact_revision", {})
            if exact.get("required_for_exit_evidence") is not True:
                errors.append("020-G exit evidence must require exact revision")
            for field in ("repository","source_commit_sha","source_tree_sha","workflow_definition_revision","run_id","attempt_id","result","artifact_digests"):
                if field not in exact.get("identity_fields", []):
                    errors.append(f"020-G exact-revision identity missing field: {field}")
            if exact.get("pr_merge_ref_is_exact_candidate_by_default") is not False:
                errors.append("020-G must not silently treat PR merge refs as exact candidate identity")
            if exact.get("changed_tree_requires_affected_evidence_rerun") is not True:
                errors.append("020-G changed source tree must require affected evidence rerun")

            supply = ci_evidence.get("supply_chain", {})
            actions = supply.get("github_actions", {})
            if actions.get("blocking_and_exit_actions_full_commit_sha_required") is not True:
                errors.append("020-G blocking/exit GitHub Actions must require immutable full commit SHAs")
            if actions.get("update_bypasses_review") is not False:
                errors.append("020-G dependency/action updates must not bypass review")
            if supply.get("frozen_lockfile_required") is not True or supply.get("bounded_lifecycle_scripts_required") is not True:
                errors.append("020-G must retain frozen-lockfile and bounded lifecycle-script supply-chain controls")

            artifacts = ci_evidence.get("artifact_integrity", {})
            if artifacts.get("build_once_promote_by_digest") is not True:
                errors.append("020-G must build once and promote by digest")
            if artifacts.get("rebuild_for_production_of_same_release_forbidden") is not True:
                errors.append("020-G must forbid production rebuild of an already-reviewed release")
            if artifacts.get("provenance", {}).get("cryptographic_attestation_required") is not True:
                errors.append("020-G releaseable artifacts require cryptographic provenance attestation")
            if artifacts.get("sbom", {}).get("required_for_deployable_artifacts") is not True:
                errors.append("020-G deployable artifacts require SBOM evidence")

            bundle = ci_evidence.get("evidence_bundle", {})
            if bundle.get("model") != "IMMUTABLE_CONTENT_ADDRESSED_MANIFEST_PLUS_REFERENCED_EVIDENCE":
                errors.append("020-G evidence-bundle model drift")
            if bundle.get("every_required_criterion_mapped") is not True:
                errors.append("020-G evidence bundle must map every required criterion")
            if bundle.get("final_manifest_mutable_after_finalization") is not False:
                errors.append("020-G finalized evidence manifest must be immutable")
            if bundle.get("hidden_probe_material_in_public_bundle_forbidden") is not True:
                errors.append("020-G public evidence bundle must not expose hidden probe material")

            evaluator_g = ci_evidence.get("protected_evaluator_binding", {})
            for key in ("exact_candidate_sha_required","tamper_evident_result_required","hidden_probe_material_outside_ordinary_implementer_context","production_use_forbidden","hidden_requirements_forbidden"):
                if evaluator_g.get(key) is not True:
                    errors.append(f"020-G protected evaluator binding.{key} must be true")
            for key in ("may_modify_candidate_source","may_modify_visible_criteria","may_grant_g2_or_g5"):
                if evaluator_g.get(key) is not False:
                    errors.append(f"020-G protected evaluator binding.{key} must be false")

            retry = ci_evidence.get("retry_and_quarantine", {})
            if retry.get("attempt_history_preserved") is not True or retry.get("retry_may_erase_initial_failure") is not False:
                errors.append("020-G failure/retry history must remain preserved")
            if retry.get("retry_until_green_for_flake_forbidden") is not True:
                errors.append("020-G must forbid retry-until-green as trusted evidence")

            enforcement = ci_evidence.get("repository_enforcement", {})
            if enforcement.get("current_enforcement_verified") is not False:
                errors.append("020-G must not claim repository main enforcement has been verified")
            if enforcement.get("workflow_existence_proves_enforcement") is not False:
                errors.append("020-G must not infer branch protection from workflow existence")
            if enforcement.get("phase021_may_claim_trusted_main_protection_without_evidence") is not False:
                errors.append("020-G must require evidence before Phase 021 trusts main protection")

            imp014 = ci_evidence.get("imp014_binding", {})
            if imp014.get("status") != "PROPOSED" or imp014.get("g1_ready") is not False or imp014.get("g2_authorized") is not False:
                errors.append("020-G must not promote IMP-014 beyond PROPOSED")
            imp015 = ci_evidence.get("imp015_binding", {})
            if imp015.get("status") != "PROPOSED" or imp015.get("g1_ready") is not False or imp015.get("g2_authorized") is not False:
                errors.append("020-G must not promote IMP-015 beyond PROPOSED")

    if "020-H" in completed:
        if review_exit is None:
            errors.append("020-H completion requires review/repair/exit-gate governance")
        else:
            if control.get("review_repair_exit_gate_governance") != REVIEW_EXIT:
                errors.append("Phase-020 control must point to 020-H review/repair/exit-gate governance")

            boundary_h = review_exit.get("boundary", {})
            if boundary_h.get("design_only") is not True:
                errors.append("020-H must remain design-only")
            for key in ("implementation_execution_authorized","release_authorized","production_authorized","review_pass_grants_merge_authority","g5_grants_next_g2","reopen_restores_old_g2_automatically"):
                if boundary_h.get(key) is not False:
                    errors.append(f"020-H boundary.{key} must be false")
            if boundary_h.get("active_packages") != 0 or boundary_h.get("g1_ready_packages") != 0 or boundary_h.get("g2_authorized_packages") != 0:
                errors.append("020-H must retain zero active/G1-ready/G2-authorized packages")

            code_review = review_exit.get("independent_code_review", {})
            for key in ("required","same_authoring_run_forbidden","independent_context_required","reviewer_edits_candidate_becomes_implementer","reviewer_edit_requires_new_independent_review"):
                if code_review.get(key) is not True:
                    errors.append(f"020-H independent_code_review.{key} must be true")
            if code_review.get("default_write_authority") is not False:
                errors.append("020-H reviewer default write authority must remain false")

            adversarial = review_exit.get("adversarial_conformance_review", {})
            for key in ("required","same_authoring_run_forbidden","derives_only_from_visible_authority","hidden_requirements_forbidden","production_target_forbidden","candidate_source_mutation_while_reviewer_forbidden","probe_exfiltration_forbidden"):
                if adversarial.get(key) is not True:
                    errors.append(f"020-H adversarial_conformance_review.{key} must be true")
            categories = adversarial.get("challenge_categories", {})
            for key in ("contract_evasion","authority_erosion","evidence_gaming","security_privacy_escape","complexity_scope_gaming"):
                if not categories.get(key):
                    errors.append(f"020-H adversarial challenge category missing: {key}")

            finding = review_exit.get("finding_schema", {})
            required_finding_fields = set(finding.get("required_fields", []))
            for field in ("finding_id","candidate_sha","severity","blocking","statement","authority_refs","affected_criteria","status","disposition_rationale"):
                if field not in required_finding_fields:
                    errors.append(f"020-H finding schema missing field: {field}")
            if finding.get("open_blocking_finding_compatible_with_pass") is not False:
                errors.append("020-H PASS cannot coexist with open blocking finding")
            if finding.get("comment_resolution_alone_closes_finding") is not False or finding.get("implementer_assertion_alone_closes_finding") is not False:
                errors.append("020-H blocking finding cannot close by UI/implementer assertion alone")
            if finding.get("risk_acceptance_requires_authorized_actor") is not True:
                errors.append("020-H risk acceptance requires authorized actor")
            if finding.get("reviewer_or_gatekeeper_may_self_create_risk_acceptance_authority") is not False:
                errors.append("020-H reviewer/gatekeeper cannot create risk-acceptance authority")

            outcomes = review_exit.get("review_outcomes", {})
            if outcomes.get("only_exit_success") != "PASS":
                errors.append("020-H only PASS may satisfy review exit")
            if outcomes.get("inconclusive_fails_closed") is not True:
                errors.append("020-H INCONCLUSIVE must fail closed")

            repair = review_exit.get("repair", {})
            for key in ("pre_g5_existing_g2_may_cover_repair_if_within_original_scope","source_change_creates_new_candidate_sha","affected_evidence_must_rerun","affected_review_must_rerun","failed_retry_history_preserved","budget_required_before_g2"):
                if repair.get(key) is not True:
                    errors.append(f"020-H repair.{key} must be true")
            for key in ("may_expand_scope","may_add_undeclared_package_or_work_unit","may_change_visible_criteria","may_change_semantics_or_architecture","may_require_unplanned_privilege","may_disable_mandatory_evidence","universal_numeric_budget_defined_by_020h"):
                if repair.get(key) is not False:
                    errors.append(f"020-H repair.{key} must be false")
            if repair.get("budget_exhaustion_result") != "BLOCKED_OR_EXPLICIT_HUMAN_PROGRAM_EXTENSION":
                errors.append("020-H repair budget exhaustion must block or require explicit extension")

            gatekeeper = review_exit.get("gatekeeper", {})
            if gatekeeper.get("same_authoring_run_as_implementer_for_candidate_forbidden") is not True:
                errors.append("020-H Gatekeeper must not be candidate's authoring run")
            for key in ("candidate_source_write_forbidden",):
                if gatekeeper.get(key) is not True:
                    errors.append(f"020-H gatekeeper.{key} must be true")
            for key in ("may_override_mandatory_failure","may_fabricate_missing_evidence","may_change_criteria","may_grant_next_g2","may_merge_or_deploy_from_g5"):
                if gatekeeper.get(key) is not False:
                    errors.append(f"020-H gatekeeper.{key} must be false")
            if set(gatekeeper.get("decisions", [])) != {"COMPLETE","REPAIR_REQUIRED","BLOCKED","INCONCLUSIVE"}:
                errors.append("020-H Gatekeeper decision vocabulary drift")
            if gatekeeper.get("complete_only_creates_g5") is not True:
                errors.append("020-H COMPLETE must create only G5")

            completion = review_exit.get("completion_record", {})
            if completion.get("immutable") is not True or completion.get("content_addressed") is not True:
                errors.append("020-H G5 completion record must be immutable/content-addressed")
            if completion.get("next_state") != "NEXT_ELIGIBLE_NOT_AUTHORIZED":
                errors.append("020-H G5 completion must not authorize next execution")
            if completion.get("correction_rewrites_historical_record") is not False:
                errors.append("020-H completion correction must not rewrite historical record")

            reopen = review_exit.get("reopen_authorization", {})
            if reopen.get("old_g2_closed_at_g5") is not True:
                errors.append("020-H old G2 must close at G5")
            if reopen.get("automatic_old_g2_restoration") is not False:
                errors.append("020-H reopen must not automatically restore old G2")
            if reopen.get("semantic_or_architecture_contradiction_requires_upstream_reentry_first") is not True:
                errors.append("020-H semantic/architecture contradiction must re-enter upstream first")
            required_reopen = set(reopen.get("requirements_before_repair", []))
            for item in ("reopen_record_with_invalidating_evidence","dependency_impact_review","explicit_human_or_program_reauthorization","new_candidate_evidence_review_exit_cycle"):
                if item not in required_reopen:
                    errors.append(f"020-H reopen missing prerequisite: {item}")

            invalidation = review_exit.get("post_completion_invalidation", {})
            if invalidation.get("historical_completion_record_erased") is not False:
                errors.append("020-H invalidation must preserve historical completion")
            if invalidation.get("invalidation_record_required") is not True:
                errors.append("020-H post-completion invalidation requires record")
            if invalidation.get("reopen_required_grants_execution_authority") is not False:
                errors.append("020-H REOPEN_REQUIRED must not grant execution authority")

            downstream = review_exit.get("downstream_invalidation", {})
            if downstream.get("automatic_all_downstream_reopen") is not False:
                errors.append("020-H upstream reopen must not automatically reopen all downstream packages")
            expected_dispositions = {"NO_IMPACT","EVIDENCE_REFRESH_REQUIRED","REVIEW_REFRESH_REQUIRED","REOPEN_REQUIRED","UPSTREAM_REENTRY_BLOCKER"}
            if set(downstream.get("dispositions", [])) != expected_dispositions:
                errors.append("020-H downstream invalidation disposition vocabulary drift")

    if "020-I" in completed:
        if crosscut is None:
            errors.append("020-I completion requires cross-cutting verification architecture")
        else:
            if control.get("crosscutting_verification_architecture") != CROSSCUT:
                errors.append("Phase-020 control must point to 020-I cross-cutting verification architecture")

            boundary_i = crosscut.get("boundary", {})
            if boundary_i.get("design_only") is not True:
                errors.append("020-I must remain design-only")
            for key in ("implementation_execution_authorized","release_authorized","production_authorized","cross_cutting_mapping_alone_makes_package_g1_ready"):
                if boundary_i.get(key) is not False:
                    errors.append(f"020-I boundary.{key} must be false")
            if boundary_i.get("proposed_packages") != 15 or boundary_i.get("g1_ready_packages") != 0 or boundary_i.get("g2_authorized_packages") != 0 or boundary_i.get("active_packages") != 0:
                errors.append("020-I must retain 15 proposed and zero G1/G2/active packages")

            threshold = crosscut.get("threshold_policy", {})
            for key in ("new_normative_thresholds_must_be_visible_before_relevant_authorization","hidden_acceptance_thresholds_forbidden","rto_rpo_claims_require_measured_restore_exercise","load_profile_assumptions_must_be_visible","cost_model_assumptions_must_be_visible"):
                if threshold.get(key) is not True:
                    errors.append(f"020-I threshold_policy.{key} must be true")
            for key in ("performance_thresholds_not_invented_by_020i","cost_caps_not_invented_by_020i","rto_rpo_not_invented_by_020i"):
                if threshold.get(key) is not True:
                    errors.append(f"020-I threshold_policy.{key} must remain true")
            accepted_thresholds = set(threshold.get("accepted_existing_thresholds_visible", []))
            for required in (
                "WCAG 2.2 AA for core browser workflows",
                "production at least two healthy API tasks across at least two AZs",
                "production RDS 35 days automated PITR",
            ):
                if required not in accepted_thresholds:
                    errors.append(f"020-I accepted threshold missing: {required}")

            migration = crosscut.get("migration_verification", {})
            expected_mig = {f"MIG-{i:02d}" for i in range(1, 7)}
            actual_mig = {item.get("id") for item in migration.get("evidence_obligations", []) if isinstance(item, dict)}
            if actual_mig != expected_mig:
                errors.append(f"020-I migration evidence IDs drift: {actual_mig}")
            if migration.get("sqlite_or_in_memory_substitute_for_postgresql_semantics") is not False:
                errors.append("020-I real PostgreSQL semantics cannot be proven by SQLite/in-memory substitute")
            if migration.get("application_startup_auto_migration_allowed") is not False:
                errors.append("020-I must preserve no application-startup auto-migration")
            if migration.get("production_destructive_rollback_assumed_safe") is not False:
                errors.append("020-I must not assume destructive production rollback is safe")

            recovery = crosscut.get("recovery_verification", {})
            level_ids = [item.get("id") for item in recovery.get("levels", []) if isinstance(item, dict)]
            if level_ids != [f"RCV-{i}" for i in range(1, 6)]:
                errors.append(f"020-I recovery levels must remain RCV-1..RCV-5; got {level_ids}")
            for key in ("paper_and_local_drafts_remain_non_authoritative_until_reconciled","rto_rpo_measured_not_documentation_only"):
                if recovery.get(key) is not True:
                    errors.append(f"020-I recovery.{key} must be true")
            for key in ("backup_creation_alone_is_recovery_evidence","database_restore_alone_is_semantic_recovery","unknown_may_be_converted_to_success_without_authority_check","regional_recovery_may_create_dual_writable_authority"):
                if recovery.get(key) is not False:
                    errors.append(f"020-I recovery.{key} must be false")
            if recovery.get("readiness_sequence") != [
                "authoritative storage restored",
                "application consistency verified",
                "projections/derived state rebuilt or truthfully unavailable",
                "external integrations reconciled",
                "service readiness explicitly declared",
            ]:
                errors.append("020-I recovery readiness sequence drift")

            accessibility = crosscut.get("accessibility_verification", {})
            if accessibility.get("normative_target") != "WCAG_2_2_AA_CORE_WORKFLOWS":
                errors.append("020-I accessibility target must remain WCAG 2.2 AA for core workflows")
            for key in ("semantic_parity_required","critical_meaning_color_only_forbidden","critical_action_hover_gesture_camera_qr_only_forbidden","responsive_authority_or_disclosure_change_forbidden","degraded_accessibility_shortcut_to_weaker_authority_forbidden"):
                if accessibility.get(key) is not True:
                    errors.append(f"020-I accessibility.{key} must be true")
            if accessibility.get("automated_scan_alone_proves_wcag_conformance") is not False:
                errors.append("020-I automated accessibility scanning alone cannot prove WCAG conformance")
            for required in ("keyboard","screen_reader","zoom_reflow"):
                if required not in accessibility.get("modalities", []):
                    errors.append(f"020-I accessibility modality missing: {required}")

            perf = crosscut.get("performance_verification", {})
            threshold_contract = perf.get("threshold_contract", {})
            for key in ("material_performance_claim_requires_visible_threshold","hidden_threshold_forbidden","workload_profile_visible","dataset_shape_visible","concurrency_visible","environment_capacity_visible","warmup_and_test_duration_visible"):
                if threshold_contract.get(key) is not True:
                    errors.append(f"020-I performance threshold contract.{key} must be true")
            if perf.get("event_windows_prescaled_and_load_tested_before_judging") is not True:
                errors.append("020-I event windows must be prescaled/load-tested")
            if perf.get("at_least_two_api_tasks_two_azs_is_existing_architecture_constraint") is not True:
                errors.append("020-I must retain production API/AZ minimum")
            if perf.get("overload_may_weaken_authority_semantics") is not False or perf.get("bulk_may_flatten_partial_unknown_results") is not False:
                errors.append("020-I performance pressure may not weaken authority or flatten partial/unknown truth")

            cost = crosscut.get("cost_verification", {})
            if cost.get("cost_cap_defined_by_020i") is not False:
                errors.append("020-I must not invent a dollar cost cap")
            if cost.get("cost_model_required_for_material_runtime_or_provider_package") is not True:
                errors.append("020-I material runtime/provider packages require a cost model")
            if cost.get("mandatory_trust_controls_may_be_removed_for_cost_only") is not False:
                errors.append("020-I cost optimization may not remove mandatory trust controls")
            if cost.get("unjustified_baseline_services_prohibited") is not True:
                errors.append("020-I must prohibit unjustified baseline services")

            scenarios = crosscut.get("scenario_matrix", [])
            if not isinstance(scenarios, list) or len(scenarios) != 15:
                errors.append("020-I must define exactly 15 scenarios")
                scenarios = []
            expected_scenario_ids = [f"SCN-{i:02d}" for i in range(1, 16)]
            actual_scenario_ids = [item.get("id") for item in scenarios if isinstance(item, dict)]
            if actual_scenario_ids != expected_scenario_ids:
                errors.append(f"020-I scenario IDs drift: expected {expected_scenario_ids}, got {actual_scenario_ids}")
            scenario_seeds = [item.get("seed") for item in scenarios if isinstance(item, dict)]
            if set(scenario_seeds) != set(framework.get("scenario_seeds", [])) or len(scenario_seeds) != len(set(scenario_seeds)):
                errors.append("020-I scenario seeds must exactly and uniquely match implementation-program ENG-014 seeds")
            known_evidence = {item.get("id") for item in framework.get("evidence_classes", []) if isinstance(item, dict)}
            known_packages = set()
            if package_discovery:
                known_packages = {p.get("id") for p in package_discovery.get("candidate_packages", []) if isinstance(p, dict)}
            for item in scenarios:
                if not isinstance(item, dict):
                    continue
                sid = item.get("id")
                owners = item.get("package_owners", [])
                if not isinstance(owners, list) or not owners:
                    errors.append(f"020-I {sid} must have package ownership")
                elif any(owner not in known_packages for owner in owners):
                    errors.append(f"020-I {sid} references unknown package owner")
                floor = item.get("evidence_floor", [])
                if not isinstance(floor, list) or not floor or any(e not in known_evidence for e in floor):
                    errors.append(f"020-I {sid} has invalid evidence floor")
                if not item.get("material_boundary") or not item.get("pass_obligations"):
                    errors.append(f"020-I {sid} must define material boundary and pass obligations")

            program_rules = crosscut.get("scenario_program_rules", {})
            for key in ("exactly_fifteen_required","scenario_seed_set_must_match_implementation_program_framework","scenario_is_not_closed_by_unit_test_only","scenario_may_span_multiple_packages","final_v1_replay_required","final_v1_all_15_must_have_pass_evidence","representative_semantic_instantiation_required_when_foundation_only_would_be_artificial","hidden_scenario_category_forbidden","synthetic_data_default"):
                if program_rules.get(key) is not True:
                    errors.append(f"020-I scenario_program_rules.{key} must be true")
            if program_rules.get("production_required_for_scenario_evidence") is not False:
                errors.append("020-I scenario evidence must not require unauthorized production access")

            package_map = crosscut.get("package_obligation_map", {})
            if set(package_map) != known_packages:
                errors.append("020-I package obligation map must exactly cover IMP-001..IMP-015")
            for pid, profile in package_map.items():
                if not isinstance(profile, dict):
                    errors.append(f"020-I {pid} cross-cutting profile must be an object")
                    continue
                for sid in profile.get("scenario_ids", []):
                    if sid not in expected_scenario_ids:
                        errors.append(f"020-I {pid} references unknown scenario ID {sid}")

            effect = crosscut.get("phase020_effect", {})
            if effect.get("g1_ready_after_020i") != 0 or effect.get("g2_authorized_after_020i") != 0 or effect.get("active_after_020i") != 0:
                errors.append("020-I cross-cutting mapping must not promote packages or activate execution")
            if effect.get("removes_from_package_g1_missing") != "020-I final scenario/migration/recovery/accessibility/performance/cost evidence mapping":
                errors.append("020-I phase effect must identify the resolved cross-cutting G1 placeholder")

            if package_discovery:
                if package_discovery.get("crosscutting_verification_architecture") != CROSSCUT:
                    errors.append("020-I package discovery must reference cross-cutting architecture")
                if package_discovery.get("semantics", {}).get("g1_ready_after_020i") != 0:
                    errors.append("020-I package discovery must retain zero G1-ready packages")
                for pkg in package_discovery.get("candidate_packages", []):
                    if not isinstance(pkg, dict):
                        continue
                    pid = pkg.get("id")
                    profile = pkg.get("crosscutting_verification_profile", {})
                    if profile.get("source") != CROSSCUT or profile.get("package_id") != pid:
                        errors.append(f"020-I {pid} missing cross-cutting profile binding")
                    if "020-I final scenario/migration/recovery/accessibility/performance/cost evidence mapping" in pkg.get("g1_missing", []):
                        errors.append(f"020-I {pid} still carries resolved cross-cutting mapping placeholder")
                    if pkg.get("g1_ready") is not False or pkg.get("status") != "PROPOSED":
                        errors.append(f"020-I {pid} must remain PROPOSED and below G1")

    if "020-J" in completed:
        if v1_completion is None:
            errors.append("020-J completion requires v1 completion/integration design")
        else:
            if control.get("v1_completion_integration_design") != V1_COMPLETION:
                errors.append("Phase-020 control must point to 020-J v1 completion/integration design")

            boundary_j = v1_completion.get("boundary", {})
            if boundary_j.get("design_only") is not True:
                errors.append("020-J must remain design-only")
            for key in (
                "implementation_execution_authorized","release_authorized","production_authorized",
                "v1_implementation_complete_now","release_candidate_authorized_now",
                "final_integration_phase_authorized_now",
            ):
                if boundary_j.get(key) is not False:
                    errors.append(f"020-J boundary.{key} must be false")
            if boundary_j.get("g1_ready_packages") != 0 or boundary_j.get("g2_authorized_packages") != 0 or boundary_j.get("active_packages") != 0:
                errors.append("020-J must retain zero G1/G2/active packages")

            scope = v1_completion.get("v1_scope", {})
            if scope.get("adopted_product_variant") != "PF-01 — MUDAC Live Competition Judging & Official Outcome":
                errors.append("020-J v1 target must remain PF-01")
            if scope.get("all_current_concepts_in_product_scope") is not True:
                errors.append("020-J must retain all current Concepts in v1 product scope")
            expected_concepts = {
                "Competition","Division","Team","Panel","Evaluation Occurrence","Evaluation Obligation",
                "Rubric","Scorecard","Award","Identity","Participation","Alias","Access","Versioning",
                "Provenance","Outcome Declaration","Export","Publication",
            }
            if set(scope.get("current_concepts", [])) != expected_concepts or len(scope.get("current_concepts", [])) != 18:
                errors.append("020-J v1 scope must contain exactly the eighteen current PF-01 Concepts")
            expected_purposes = {f"P-{i:02d}" for i in range(1, 10)}
            if set(scope.get("purpose_obligations", [])) != expected_purposes:
                errors.append("020-J v1 must retain P-01..P-09")
            if scope.get("scope_change_required_for_non_goal_activation") is not True:
                errors.append("020-J explicit non-goal activation must require scope change")
            if scope.get("optional_capability_instance_absence_does_not_remove_capability_from_v1_scope") is not True:
                errors.append("020-J optional instance absence must not shrink v1 product scope")
            if len(scope.get("explicit_non_goals", [])) < 10:
                errors.append("020-J v1 non-goal boundary appears incomplete")

            package_scope = v1_completion.get("package_scope", {})
            expected_packages = {f"IMP-{i:03d}" for i in range(1, 16)}
            if set(package_scope.get("current_candidate_set", [])) != expected_packages:
                errors.append("020-J current candidate set must remain IMP-001..IMP-015")
            if package_scope.get("final_retained_or_superseded_disposition_owner") != "020-K":
                errors.append("020-J must leave final package retain/supersede disposition to 020-K")
            if package_scope.get("split_merge_supersede_allowed_only_with_no_obligation_loss") is not True:
                errors.append("020-J decomposition changes may not lose v1 obligations")
            if package_scope.get("package_g5_completion_alone_equals_v1_complete") is not False:
                errors.append("020-J package G5 alone must not equal v1 completion")
            if package_scope.get("package_graph_closure_required") is not True:
                errors.append("020-J v1 requires package dependency closure")

            journeys = v1_completion.get("integrated_journeys", [])
            expected_journeys = [f"JNY-{i:02d}" for i in range(1, 10)]
            actual_journeys = [item.get("id") for item in journeys if isinstance(item, dict)]
            if actual_journeys != expected_journeys:
                errors.append(f"020-J integrated journey IDs drift: {actual_journeys}")
            for item in journeys:
                if not isinstance(item, dict):
                    continue
                if not item.get("actors") or not item.get("required_capabilities"):
                    errors.append(f"020-J {item.get('id')} must define actors and required capabilities")

            criteria = v1_completion.get("whole_system_criteria", [])
            expected_ws = [f"V1-WS-{i:02d}" for i in range(1, 13)]
            actual_ws = [item.get("id") for item in criteria if isinstance(item, dict)]
            if actual_ws != expected_ws:
                errors.append(f"020-J whole-system criterion IDs drift: {actual_ws}")
            known_evidence_j = {item.get("id") for item in framework.get("evidence_classes", []) if isinstance(item, dict)}
            for item in criteria:
                if not isinstance(item, dict):
                    continue
                cid = item.get("id")
                if item.get("blocking") is not True:
                    errors.append(f"020-J {cid} must remain blocking")
                floor = item.get("required_evidence", [])
                if not floor or any(e not in known_evidence_j for e in floor):
                    errors.append(f"020-J {cid} has invalid evidence requirements")
                if not item.get("statement"):
                    errors.append(f"020-J {cid} missing criterion statement")

            final_phase = v1_completion.get("final_integration_hardening_phase", {})
            if final_phase.get("logical_id") != "V1-FINAL":
                errors.append("020-J terminal logical phase must remain V1-FINAL")
            if final_phase.get("final_number_and_name_owner") != "020-K":
                errors.append("020-J final phase numbering/naming must remain owned by 020-K")
            if final_phase.get("creates_new_product_scope") is not False or final_phase.get("creates_new_semantic_owner") is not False:
                errors.append("020-J V1-FINAL must not create product scope or semantic owner")
            entry = final_phase.get("entry_gate", {})
            for key in (
                "explicit_g2_required","all_retained_v1_packages_g1_required",
                "all_predecessor_implementation_phases_complete",
                "all_retained_v1_packages_g5_required_before_final_evidence_freeze",
                "exact_integrated_baseline_required","integration_environment_healthy_required",
                "test_control_and_evidence_infrastructure_required",
                "unresolved_semantic_or_architecture_blocker_forbidden",
                "repository_enforcement_evidence_required_before_trusting_main_as_protected_control",
            ):
                if entry.get(key) is not True:
                    errors.append(f"020-J V1-FINAL entry_gate.{key} must be true")
            if "020-H REOPEN_REQUIRED + EXPLICIT REAUTHORIZATION" != final_phase.get("defect_routes", {}).get("completed_package_source_defect"):
                errors.append("020-J completed package source defects must route through 020-H reopen/re-authorization")
            prohibited = set(final_phase.get("prohibited_work", []))
            for item in (
                "new product feature or Concept",
                "activation of explicit v1 non-goal",
                "silent architecture change",
                "direct modification of completed package-owned source without 020-H reopen/re-authorization",
                "lowering visible criteria or evidence floors",
                "release or production authorization",
            ):
                if item not in prohibited:
                    errors.append(f"020-J V1-FINAL prohibited work missing: {item}")
            review_j = final_phase.get("review", {})
            for key in ("independent_code_review_required","adversarial_conformance_review_required","whole_system_gatekeeper_required","implementer_self_close_forbidden"):
                if review_j.get(key) is not True:
                    errors.append(f"020-J V1-FINAL review.{key} must be true")
            if set(final_phase.get("exit_decisions", [])) != {"V1_IMPLEMENTATION_COMPLETE","REPAIR_REQUIRED","BLOCKED","INCONCLUSIVE"}:
                errors.append("020-J V1-FINAL exit decision vocabulary drift")
            if final_phase.get("pass_requires_all_whole_system_criteria") is not True:
                errors.append("020-J V1-FINAL PASS must require all whole-system criteria")

            bundle_j = v1_completion.get("completion_evidence_bundle", {})
            if bundle_j.get("model") != "IMMUTABLE_CONTENT_ADDRESSED_WHOLE_SYSTEM_BUNDLE":
                errors.append("020-J whole-system evidence bundle model drift")
            if bundle_j.get("historical_failed_attempts_preserved") is not True:
                errors.append("020-J whole-system evidence must preserve failed attempts")
            refs = set(bundle_j.get("required_refs", []))
            for item in (
                "V1-WS-01..12 outcomes","JNY-01..09 evidence","SCN-01..15 evidence",
                "repository enforcement evidence","independent code and adversarial review records",
            ):
                if item not in refs:
                    errors.append(f"020-J whole-system evidence bundle missing: {item}")

            completion_j = v1_completion.get("v1_completion_state", {})
            if completion_j.get("successful_state") != "V1_IMPLEMENTATION_COMPLETE":
                errors.append("020-J successful state must remain V1_IMPLEMENTATION_COMPLETE")
            for key in ("grants_g6_release_candidate","grants_deployment_authority","grants_g7_production_readiness"):
                if completion_j.get(key) is not False:
                    errors.append(f"020-J v1 completion must not grant {key}")
            if completion_j.get("next_state") != "RELEASE_CANDIDATE_ELIGIBLE_NOT_AUTHORIZED":
                errors.append("020-J v1 completion next state must remain release-candidate eligible, not authorized")
            if completion_j.get("release_authority_must_be_explicit") is not True or completion_j.get("production_authority_must_be_separate") is not True:
                errors.append("020-J release/production authority must remain explicit/separate")

            release = v1_completion.get("release_candidate_handoff", {})
            if release.get("g6_is_separate") is not True or release.get("g6_requires_explicit_release_authority") is not True or release.get("g6_does_not_equal_g7") is not True:
                errors.append("020-J must keep G6 separate and explicit, and G6 != G7")
            if release.get("must_bind_to_same_or_explicitly_requalified_revision_and_artifact_identity") is not True:
                errors.append("020-J G6 handoff must bind same or explicitly requalified revision/artifact")

            risks = v1_completion.get("residual_risk_policy", {})
            if risks.get("zero_known_blocking_findings_required") is not True:
                errors.append("020-J v1 completion requires zero known blocking findings")
            if risks.get("nonblocking_risk_may_remain") is not True:
                errors.append("020-J may retain governed non-blocking residual risk")
            if risks.get("must_not_hide_unsatisfied_visible_criterion") is not True or risks.get("must_not_hide_architecture_or_semantic_contradiction") is not True:
                errors.append("020-J residual risk must not hide required/architecture/semantic blockers")

            relation_j = v1_completion.get("package_program_relation", {})
            if relation_j.get("g1_ready_after_020j") != 0 or relation_j.get("g2_authorized_after_020j") != 0 or relation_j.get("active_after_020j") != 0:
                errors.append("020-J must not promote packages or activate implementation")
            if relation_j.get("final_phase_grouping_and_package_definitions_owned_by") != "020-K":
                errors.append("020-J must leave final phase/package definitions to 020-K")

            if crosscut:
                if crosscut.get("scenario_program_rules", {}).get("final_v1_all_15_must_have_pass_evidence") is not True:
                    errors.append("020-J requires 020-I final all-15 scenario replay obligation")
            if package_discovery:
                if package_discovery.get("v1_completion_integration_design") != V1_COMPLETION:
                    errors.append("020-J package discovery must reference v1 completion design")
                if package_discovery.get("semantics", {}).get("g1_ready_after_020j") != 0:
                    errors.append("020-J package discovery must retain zero G1-ready packages")
                for pkg in package_discovery.get("candidate_packages", []):
                    if not isinstance(pkg, dict):
                        continue
                    pid = pkg.get("id")
                    if pkg.get("v1_scope_disposition") != "V1_REQUIRED_IF_RETAINED_BY_020K":
                        errors.append(f"020-J {pid} v1 scope disposition drift")
                    rel = pkg.get("final_integration_relation", {})
                    if rel.get("source") != V1_COMPLETION or rel.get("logical_final_phase") != "V1-FINAL":
                        errors.append(f"020-J {pid} missing V1-FINAL relation")
                    if rel.get("package_g5_required_before_final_evidence_freeze") is not True or rel.get("post_g5_source_change_requires_020h_reopen") is not True:
                        errors.append(f"020-J {pid} final integration/reopen relation drift")
                    if pkg.get("g1_ready") is not False or pkg.get("status") != "PROPOSED":
                        errors.append(f"020-J {pid} must remain PROPOSED and below G1")

    if "020-K" in completed:
        if roadmap is None:
            errors.append("020-K completion requires final autonomous implementation roadmap")
        else:
            if control.get("autonomous_implementation_roadmap") != ROADMAP:
                errors.append("Phase-020 control must point to 020-K autonomous implementation roadmap")

            boundary_k = roadmap.get("boundary", {})
            if boundary_k.get("design_only") is not True or boundary_k.get("package_g1_decisions_may_be_recorded") is not True:
                errors.append("020-K must remain design-only while permitting G1 decisions")
            if boundary_k.get("package_g1_is_execution_authority") is not False:
                errors.append("020-K G1 must not be execution authority")
            for key in ("implementation_execution_authorized","release_authorized","production_authorized","automatic_phase_021_g2"):
                if boundary_k.get(key) is not False:
                    errors.append(f"020-K boundary.{key} must be false")
            if boundary_k.get("g2_authorized_packages") != 0 or boundary_k.get("active_packages") != 0:
                errors.append("020-K must retain zero G2-authorized and active packages")

            phases_k = roadmap.get("phase_sequence", [])
            expected_phase_ids = [f"{i:03d}" for i in range(21, 30)]
            actual_phase_ids = [p.get("id") for p in phases_k if isinstance(p, dict)]
            if actual_phase_ids != expected_phase_ids:
                errors.append(f"020-K implementation phase sequence drift: {actual_phase_ids}")
            expected_phase_packages = {
                "021":["IMP-001"],
                "022":["IMP-002","IMP-004","IMP-005","IMP-006"],
                "023":["IMP-003","IMP-014"],
                "024":["IMP-007"],
                "025":["IMP-008"],
                "026":["IMP-009"],
                "027":["IMP-010","IMP-011"],
                "028":["IMP-012","IMP-013","IMP-015"],
                "029":[],
            }
            expected_phase_predecessors = {
                "021":[],
                "022":["021"],
                "023":["022"],
                "024":["023"],
                "025":["024"],
                "026":["025"],
                "027":["026"],
                "028":["027"],
                "029":["028"],
            }
            for p in phases_k:
                if not isinstance(p, dict):
                    continue
                pid = p.get("id")
                if p.get("packages") != expected_phase_packages.get(pid):
                    errors.append(f"020-K phase {pid} package assignment drift")
                if p.get("hard_predecessors") != expected_phase_predecessors.get(pid):
                    errors.append(f"020-K phase {pid} predecessor chain drift")
                if p.get("g2_authorized") is not False or p.get("next_phase_auto_authorization") is not False:
                    errors.append(f"020-K phase {pid} must not be G2-authorized or auto-authorize next phase")
                if p.get("start_gate_required") is not True or p.get("exit_gate_required") is not True:
                    errors.append(f"020-K phase {pid} must retain start/exit gates")
                if p.get("exact_entry_baseline_required") is not True or p.get("visible_criteria_required") is not True:
                    errors.append(f"020-K phase {pid} must retain exact baseline and visible criteria")
            final_phase_k = next((p for p in phases_k if isinstance(p, dict) and p.get("id")=="029"), {})
            if final_phase_k.get("logical_alias") != "V1-FINAL":
                errors.append("020-K phase 029 must remain V1-FINAL")

            strategy = roadmap.get("agent_strategy", {})
            if strategy.get("provider_preference_is_non_normative") is not True:
                errors.append("020-K Cursor/Codex provider preference must remain non-normative")
            if strategy.get("max_delegation_depth") != 1 or strategy.get("recursive_delegation") is not False:
                errors.append("020-K delegation depth must remain one and recursive delegation forbidden")
            if strategy.get("worktree_isolation_required") is not True or strategy.get("context_manifest_required") is not True or strategy.get("provenance_required") is not True:
                errors.append("020-K must preserve worktree/context/provenance controls")

            concurrency_k = roadmap.get("concurrency", {})
            if not concurrency_k.get("shared_surface_rule") or not concurrency_k.get("root_lockfile_rule") or not concurrency_k.get("migration_catalog_rule"):
                errors.append("020-K serialized-surface concurrency controls incomplete")
            if concurrency_k.get("phase_maxima", {}).get("022") != 3 or concurrency_k.get("phase_maxima", {}).get("028") != 3:
                errors.append("020-K key phase concurrency maxima drift")

            packages_k = roadmap.get("packages", [])
            expected_package_ids = [f"IMP-{i:03d}" for i in range(1, 16)]
            actual_package_ids = [p.get("id") for p in packages_k if isinstance(p, dict)]
            if actual_package_ids != expected_package_ids:
                errors.append("020-K final package set must remain IMP-001..IMP-015 in order")
            required_schema = set(framework.get("package_schema", {}).get("required_fields", []))
            allowed_evidence = {e.get("id") for e in framework.get("evidence_classes", []) if isinstance(e, dict)}
            assigned_packages = {pkg for vals in expected_phase_packages.values() for pkg in vals}
            if assigned_packages != set(expected_package_ids):
                errors.append("020-K phase assignment must cover every retained package exactly once before V1-FINAL")
            seen_assigned=[]
            for vals in expected_phase_packages.values():
                seen_assigned.extend(vals)
            if len(seen_assigned) != len(set(seen_assigned)):
                errors.append("020-K package assigned to more than one implementation phase")

            criterion_ids=set()
            evidence_ids=set()
            for pkg in packages_k:
                if not isinstance(pkg, dict):
                    continue
                pid=pkg.get("id")
                if pkg.get("status") != "READY_FOR_AUTHORIZATION" or pkg.get("g1_ready") is not True or pkg.get("g1_decision") != "PASS":
                    errors.append(f"020-K {pid} must be G1 PASS / READY_FOR_AUTHORIZATION")
                if pkg.get("implementation_phase") not in expected_phase_packages or pid not in expected_phase_packages.get(pkg.get("implementation_phase"), []):
                    errors.append(f"020-K {pid} implementation phase assignment invalid")
                assignment = pkg.get("preferred_agent_assignment", {})
                if assignment.get("implementer") not in {"CURSOR","CODEX"} or assignment.get("reviewer") not in {"CURSOR","CODEX"}:
                    errors.append(f"020-K {pid} preferred agent assignment must use Cursor/Codex profiles")
                if assignment.get("implementer") == assignment.get("reviewer"):
                    errors.append(f"020-K {pid} preferred implementer/reviewer profiles should be reciprocal")

                if package_discovery:
                    source_pkg = next((sp for sp in package_discovery.get("candidate_packages", []) if isinstance(sp,dict) and sp.get("id")==pid), None)
                    if source_pkg is None:
                        errors.append(f"020-K {pid} missing from 020-E discovery")
                    else:
                        deps = pkg.get("dependencies", {})
                        if deps.get("hard") != source_pkg.get("hard_dependencies", []):
                            errors.append(f"020-K {pid} hard dependency drift from 020-E")
                        if deps.get("integration") != source_pkg.get("integration_dependencies", []):
                            errors.append(f"020-K {pid} integration dependency drift from 020-E")
                        if deps.get("evidence") != source_pkg.get("evidence_dependencies", []):
                            errors.append(f"020-K {pid} evidence dependency drift from 020-E")
                        if pkg.get("scope_in") != source_pkg.get("scope_in") or pkg.get("scope_out") != source_pkg.get("scope_out"):
                            errors.append(f"020-K {pid} scope drift from retained 020-E package without explicit disposition")

                field_aliases={
                    "dependencies":"dependencies",
                    "owned_surfaces":"owned_surfaces",
                    "data_migration_impact":"data_migration_impact",
                    "security_privacy_impact":"security_privacy_impact",
                    "accessibility_degraded_impact":"accessibility_degraded_impact",
                    "failure_recovery_impact":"failure_recovery_impact",
                    "required_evidence_classes":"required_evidence_classes",
                    "scenario_seeds":"scenario_seeds",
                    "compatibility_rollback":"compatibility_rollback",
                    "residual_risks":"residual_risks",
                    "review_policy":"review_policy",
                    "adversarial_review_policy":"adversarial_review_policy",
                    "repair_budget":"repair_budget",
                    "gatekeeper_policy":"gatekeeper_policy",
                    "reopen_policy":"reopen_policy",
                    "crosscutting_verification_profile":"crosscutting_verification_profile",
                    "v1_scope_disposition":"v1_scope_disposition",
                    "final_integration_relation":"final_integration_relation",
                }
                base_required={"id","title","purpose","status","scope_in","scope_out","semantic_refs","architecture_refs","eng_refs"}
                for field in base_required | set(field_aliases):
                    if field not in pkg:
                        errors.append(f"020-K {pid} G1 package schema missing: {field}")
                    elif field != "scenario_seeds" and pkg.get(field) in (None,"",[]):
                        errors.append(f"020-K {pid} G1 package schema empty: {field}")
                if not isinstance(pkg.get("scenario_seeds"), list):
                    errors.append(f"020-K {pid} scenario_seeds must be an explicit list")

                criteria_k=pkg.get("visible_success_criteria", [])
                if not criteria_k:
                    errors.append(f"020-K {pid} must instantiate visible success criteria")
                for crit in criteria_k:
                    if not isinstance(crit, dict):
                        errors.append(f"020-K {pid} criterion must be object")
                        continue
                    cid=crit.get("id")
                    if not cid or cid in criterion_ids:
                        errors.append(f"020-K criterion ID missing/duplicate: {cid}")
                    criterion_ids.add(cid)
                    for field in ("statement","criterion_type","authority_refs","evidence_floor","material_boundary","verification_visibility","failure_class","applies_to"):
                        if crit.get(field) in (None,"",[]):
                            errors.append(f"020-K {cid} missing criterion field: {field}")
                    if crit.get("required") is not True or crit.get("verification_visibility") != "PUBLIC":
                        errors.append(f"020-K {cid} must remain required and publicly visible")
                    floor=crit.get("evidence_floor", [])
                    if not isinstance(floor,list) or any(e not in allowed_evidence for e in floor):
                        errors.append(f"020-K {cid} evidence floor invalid")

                evidence_k=pkg.get("evidence_obligations", [])
                if not evidence_k:
                    errors.append(f"020-K {pid} must instantiate evidence obligations")
                criterion_local={x.get("id") for x in criteria_k if isinstance(x,dict)}
                for ev in evidence_k:
                    if not isinstance(ev,dict):
                        errors.append(f"020-K {pid} evidence obligation must be object")
                        continue
                    eid=ev.get("id")
                    if not eid or eid in evidence_ids:
                        errors.append(f"020-K evidence obligation ID missing/duplicate: {eid}")
                    evidence_ids.add(eid)
                    for field in ("criterion_refs","evidence_class","claim","material_boundary","environment_tier","reproducibility","visibility","producer","retention_or_reference"):
                        if ev.get(field) in (None,"",[]):
                            errors.append(f"020-K {eid} missing evidence field: {field}")
                    if ev.get("required") is not True:
                        errors.append(f"020-K {eid} must remain required")
                    if ev.get("evidence_class") not in allowed_evidence:
                        errors.append(f"020-K {eid} evidence class invalid")
                    if any(ref not in criterion_local for ref in ev.get("criterion_refs", [])):
                        errors.append(f"020-K {eid} references unknown local criterion")
                covered={ref for ev in evidence_k if isinstance(ev,dict) for ref in ev.get("criterion_refs",[])}
                if criterion_local - covered:
                    errors.append(f"020-K {pid} has criteria without evidence obligations: {sorted(criterion_local-covered)}")

                g1e=pkg.get("g1_evidence", {})
                for key in (
                    "schema_complete","scope_explicit","traceability_complete","dependencies_explicit",
                    "visible_criteria_instantiated","evidence_instantiated","scenario_obligations_instantiated",
                    "crosscutting_classified","compatibility_rollback_explicit","residual_risks_explicit",
                    "phase_assignment_known",
                ):
                    if g1e.get(key) is not True:
                        errors.append(f"020-K {pid} g1_evidence.{key} must be true")
                rb=pkg.get("repair_budget", {})
                if rb.get("required") is not True or rb.get("scope_may_expand") is not False:
                    errors.append(f"020-K {pid} repair budget must be bounded and non-expanding")
                if rb.get("default_cycles") != 3 or rb.get("repeated_identical_failure_threshold") != 2:
                    errors.append(f"020-K {pid} repair budget default drift")
                if pkg.get("visible_thresholds_and_assumptions",{}).get("hidden_thresholds_forbidden") is not True:
                    errors.append(f"020-K {pid} must forbid hidden thresholds")

            readiness=roadmap.get("readiness_summary", {})
            if readiness.get("package_count") != 15 or readiness.get("g1_ready_count") != 15 or readiness.get("ready_for_authorization_count") != 15:
                errors.append("020-K readiness summary must record 15/15 G1 READY_FOR_AUTHORIZATION")
            if readiness.get("g2_authorized_count") != 0 or readiness.get("active_count") != 0 or readiness.get("implementation_execution_authorized") is not False:
                errors.append("020-K readiness summary must retain zero G2/active/execution")
            if readiness.get("first_g2_candidate_packages") != ["IMP-001"] or readiness.get("first_phase_g2_authorized") is not False:
                errors.append("020-K first G2 candidate must be IMP-001 and remain unauthorized")

            entry_k=roadmap.get("phase_entry_readiness",{}).get("021",{})
            if entry_k.get("after_phase020_exit") is not True or entry_k.get("explicit_g2_required") is not True or entry_k.get("currently_authorized") is not False:
                errors.append("020-K Phase 021 entry must require Phase-020 exit + explicit G2 and remain unauthorized")
            if entry_k.get("packages") != ["IMP-001"] or entry_k.get("g1_required") != ["IMP-001"]:
                errors.append("020-K Phase 021 entry package set must be IMP-001")

            terminal_k=roadmap.get("v1_terminal",{})
            if terminal_k.get("phase_id")!="029" or terminal_k.get("logical_alias")!="V1-FINAL":
                errors.append("020-K v1 terminal must be phase 029 / V1-FINAL")
            if terminal_k.get("grants_g6") is not False or terminal_k.get("grants_g7") is not False:
                errors.append("020-K v1 terminal must not grant G6/G7")
            if terminal_k.get("next_state")!="RELEASE_CANDIDATE_ELIGIBLE_NOT_AUTHORIZED":
                errors.append("020-K v1 terminal next state drift")

            if package_discovery:
                if package_discovery.get("final_autonomous_implementation_roadmap") != ROADMAP:
                    errors.append("020-K discovery graph must bind final roadmap")
                semk=package_discovery.get("semantics",{})
                if semk.get("g1_ready_after_020k") != 15 or semk.get("final_readiness_authority") != ROADMAP:
                    errors.append("020-K discovery semantics must point to 15-package final G1 authority")
                if semk.get("discovery_status_is_not_final_lifecycle_status") is not True:
                    errors.append("020-K must preserve discovery-vs-final status distinction")
                for pkg in package_discovery.get("candidate_packages",[]):
                    if not isinstance(pkg,dict):
                        continue
                    final_ref=pkg.get("final_020k_contract",{})
                    if final_ref.get("source")!=ROADMAP or final_ref.get("final_disposition")!="RETAINED" or final_ref.get("final_g1_status")!="READY_FOR_AUTHORIZATION":
                        errors.append(f"020-K discovery binding missing for {pkg.get('id')}")

    if control.get("preimplementation_exit_audit"):
        if control.get("preimplementation_exit_audit") != PREIMPLEMENTATION_AUDIT:
            errors.append("Phase-020 control must reference the canonical 020-L preimplementation audit")
        if preimplementation_audit is None:
            errors.append("020-L audit reference requires a readable preimplementation audit")
        else:
            l_complete = "020-L" in completed
            audit_status = preimplementation_audit.get("audit_status")
            audit_outcome = preimplementation_audit.get("audit_outcome")
            findings_l = preimplementation_audit.get("blocking_findings", [])
            handoff_l = preimplementation_audit.get("phase021_handoff", {})
            closure_l = preimplementation_audit.get("closure_rule", {})
            ci_l = preimplementation_audit.get("exact_head_ci_evidence", {})

            if l_complete:
                if audit_status not in {"PASS", "COMPLETE"}:
                    errors.append("completed 020-L requires PASS/COMPLETE preimplementation audit")
                if findings_l:
                    errors.append("completed 020-L may not retain blocking findings")
                if handoff_l.get("g2_state") != "NOT_AUTHORIZED":
                    errors.append("Phase 021 handoff after 020-L must still leave G2 NOT_AUTHORIZED")
            else:
                if audit_status != "BLOCKED" or audit_outcome not in {"BLOCKED_REPOSITORY_ENFORCEMENT", "BLOCKED_RULESET_ENFORCEMENT_DISABLED"}:
                    errors.append("open 020-L audit must remain BLOCKED on the observed repository-enforcement finding")
                blocker_ids = {x.get("id") for x in findings_l if isinstance(x, dict)}
                if "P020L-001" not in blocker_ids:
                    errors.append("blocked 020-L audit must retain P020L-001")
                finding = next((x for x in findings_l if isinstance(x, dict) and x.get("id") == "P020L-001"), {})
                evidence_l = finding.get("evidence", {})
                if evidence_l.get("observed_protected") is not False:
                    errors.append("P020L-001 must record observed main protected=false until reverified")
                if evidence_l.get("observed_required_status_checks_enforcement") != "off":
                    errors.append("P020L-001 must record status-check enforcement off until reverified")
                observed_rulesets_l = evidence_l.get("observed_rulesets", [])
                if audit_outcome == "BLOCKED_REPOSITORY_ENFORCEMENT":
                    if observed_rulesets_l != []:
                        errors.append("P020L-001 legacy blocker must record the observed empty ruleset set")
                else:
                    if not isinstance(observed_rulesets_l, list) or len(observed_rulesets_l) != 1:
                        errors.append("P020L-001 ruleset-disabled state must record exactly one observed ruleset")
                    else:
                        observed_ruleset_l = observed_rulesets_l[0]
                        if observed_ruleset_l.get("id") != 24024518 or observed_ruleset_l.get("name") != "main — protected":
                            errors.append("P020L-001 observed ruleset identity drift")
                        if observed_ruleset_l.get("enforcement") != "disabled":
                            errors.append("P020L-001 ruleset-disabled state must record enforcement=disabled")
                        expected_checks_l = {"Validate agentic/documentation conformance", "Implementation Verification", "CodeQL JavaScript/TypeScript"}
                        if set(observed_ruleset_l.get("required_checks", [])) != expected_checks_l:
                            errors.append("P020L-001 required-check set drift")
                        if observed_ruleset_l.get("strict_required_status_checks_policy") is not True:
                            errors.append("P020L-001 strict required status checks must remain enabled")
                if finding.get("repository_admin_action_required") is not True:
                    errors.append("P020L-001 must remain an explicit repository-admin action")
                if state.get("preimplementation_audit_status") != "BLOCKED":
                    errors.append("Phase-020 state must expose blocked preimplementation audit")
                if state.get("blocked_subphase") != "020-L":
                    errors.append("Phase-020 state must expose 020-L as the blocked subphase")
                if state.get("phase021_start_gate_eligible") is not False or state.get("phase021_g2_authorized") is not False:
                    errors.append("blocked 020-L must keep Phase 021 ineligible and G2 unauthorized")
                if handoff_l.get("status") not in {"BLOCKED_PENDING_REPOSITORY_ENFORCEMENT", "BLOCKED_PENDING_RULESET_ACTIVATION"}:
                    errors.append("blocked 020-L must expose a blocked Phase-021 handoff")
                if handoff_l.get("g1_state") != "READY_FOR_AUTHORIZATION" or handoff_l.get("g2_state") != "NOT_AUTHORIZED":
                    errors.append("Phase-021 handoff must preserve IMP-001 G1 readiness and zero G2")
                if handoff_l.get("execution_before_resolution_forbidden") is not True:
                    errors.append("Phase-021 execution must remain forbidden while 020-L is blocked")

            runs_l = ci_l.get("runs", [])
            required_ci_names = {"Knowledge Validation", "Implementation Verification", "CodeQL"}
            successful_ci_names = {
                run.get("name")
                for run in runs_l
                if isinstance(run, dict) and run.get("conclusion") == "success"
            }
            if ci_l.get("all_required_runs_success") is not True or not required_ci_names.issubset(successful_ci_names):
                errors.append("020-L audit must retain successful exact-head evidence for all required workflows")

            if closure_l.get("phase020_may_close_with_p020l001_open") is not False:
                errors.append("020-L closure rule must forbid closing Phase 020 with P020L-001 open")
            if closure_l.get("issue_closure_alone_is_sufficient") is not False:
                errors.append("020-L closure rule must require observed enforcement, not issue closure")
            if closure_l.get("repository_enforcement_must_be_observed") is not True:
                errors.append("020-L closure rule must require observed repository enforcement")
            if closure_l.get("exact_head_ci_must_be_rechecked_after_final_closure_commit") is not True:
                errors.append("020-L closure rule must require final exact-head CI recheck")
            if closure_l.get("phase021_g2_must_be_explicit_after_phase020_close") is not True:
                errors.append("020-L closure rule must preserve explicit Phase-021 G2")

            if ci_evidence:
                enforcement_l = ci_evidence.get("repository_enforcement", {})
                if not l_complete:
                    if enforcement_l.get("current_enforcement_verified") is not False:
                        errors.append("blocked 020-L must not claim repository enforcement verified")
                    last_l = enforcement_l.get("last_observation", {})
                    if last_l.get("protected") is not False:
                        errors.append("020-G enforcement record must preserve protected=false until ruleset activation")
                    if last_l.get("result") not in {"BLOCKING", "BLOCKING_RULESET_DISABLED"}:
                        errors.append("020-G enforcement record must preserve a blocking enforcement observation")

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
    if "020-F" in completed and phase020_fw.get("implementation_phase_contract") != PHASE_CONTRACT:
        errors.append("implementation framework must reference 020-F phase contract after completion")
    if "020-G" in completed and phase020_fw.get("ci_supplychain_evidence_architecture") != CI_EVIDENCE:
        errors.append("implementation framework must reference 020-G CI/supply-chain/evidence architecture after completion")
    if "020-H" in completed and phase020_fw.get("review_repair_exit_gate_governance") != REVIEW_EXIT:
        errors.append("implementation framework must reference 020-H review/repair/exit-gate governance after completion")
    if "020-I" in completed and phase020_fw.get("crosscutting_verification_architecture") != CROSSCUT:
        errors.append("implementation framework must reference 020-I cross-cutting verification architecture after completion")
    if "020-J" in completed and phase020_fw.get("v1_completion_integration_design") != V1_COMPLETION:
        errors.append("implementation framework must reference 020-J v1 completion/integration design after completion")
    if "020-K" in completed and phase020_fw.get("autonomous_implementation_roadmap") != ROADMAP:
        errors.append("implementation framework must reference 020-K autonomous implementation roadmap after completion")
    if "020-E" in completed:
        if phase020_fw.get("proposed_package_count") != 15:
            errors.append("implementation framework proposed package count drift")
        expected_g1 = 15 if "020-K" in completed else 0
        if phase020_fw.get("g1_ready_package_count") != expected_g1:
            errors.append(f"implementation framework G1-ready count drift: expected {expected_g1}")
        if phase020_fw.get("g2_authorized_package_count") != 0:
            errors.append("implementation framework must retain zero G2-authorized packages during Phase 020")
        if phase020_fw.get("active_package_count") != 0:
            errors.append("implementation framework must keep packages inactive during Phase 020")
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
        *([f"{PHASE_DIR}/020-F-implementation-phase-contract-visible-criteria-evidence-classes-hidden-evaluation-architecture.md"] if "020-F" in completed else []),
        *([f"{PHASE_DIR}/020-G-ci-cd-security-supply-chain-exact-sha-verification-evidence-bundle-architecture.md"] if "020-G" in completed else []),
        *([f"{PHASE_DIR}/020-H-independent-code-review-adversarial-review-repair-reopen-exit-gate-governance.md"] if "020-H" in completed else []),
        *([f"{PHASE_DIR}/020-I-migration-recovery-accessibility-performance-cost-scenario-verification-design.md"] if "020-I" in completed else []),
        *([f"{PHASE_DIR}/020-J-v1-scope-whole-system-completion-criteria-final-integration-hardening-phase-design.md"] if "020-J" in completed else []),
        *([f"{PHASE_DIR}/020-K-full-autonomous-implementation-roadmap-agent-assignment-phase-package-definitions-entry-readiness.md"] if "020-K" in completed else []),
        *(["docs/implementation-roadmap/index.md"] if "020-K" in completed else []),
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

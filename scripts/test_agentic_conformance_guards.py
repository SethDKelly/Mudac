#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


def clone_repo(source: Path, parent: Path, name: str) -> Path:
    target = parent / name
    shutil.copytree(
        source,
        target,
        ignore=shutil.ignore_patterns(".git", "node_modules", ".venv", "__pycache__", "*.pyc"),
    )
    return target


def run_script(source_repo: Path, test_repo: Path, script: str, *extra: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(source_repo / script), *extra],
        cwd=test_repo,
        text=True,
        capture_output=True,
    )


def expect_failure(label: str, proc: subprocess.CompletedProcess[str], errors: list[str]) -> None:
    if proc.returncode == 0:
        errors.append(f"{label}: negative control unexpectedly passed")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", default=".")
    args = parser.parse_args()
    source = Path(args.repo).resolve()
    errors: list[str] = []

    with tempfile.TemporaryDirectory(prefix="mudac-conformance-") as tmp_raw:
        tmp = Path(tmp_raw)

        status_repo = clone_repo(source, tmp, "status")
        agents = status_repo / "AGENTS.md"
        text = agents.read_text(encoding="utf-8")
        import re
        if re.search(r"018-[A-M] NEXT", text):
            text = re.sub(r"018-[A-M] NEXT", "018-Z NEXT", text)
        else:
            text = text.replace(
                "018-A/B/C/D/E/F/G/H/I/J/K/L/M COMPLETE",
                "018-A/B/C COMPLETE",
            )
        agents.write_text(text, encoding="utf-8")
        expect_failure(
            "status mirror drift",
            run_script(source, status_repo, "scripts/validate_status_mirrors.py", "--repo", str(status_repo)),
            errors,
        )

        policy_repo = clone_repo(source, tmp, "policy")
        policy_path = policy_repo / "docs/routing/agentic_action_policy.json"
        policy = json.loads(policy_path.read_text(encoding="utf-8"))
        policy["action_classes"]["A1"]["repository_edits"] = True
        policy_path.write_text(json.dumps(policy, indent=2) + "\n", encoding="utf-8")
        expect_failure(
            "A1 authority corruption",
            run_script(source, policy_repo, "scripts/validate_agentic_authority_policy.py", "--repo", str(policy_repo)),
            errors,
        )

        workflow_repo = clone_repo(source, tmp, "workflow")
        duplicate = workflow_repo / ".claude/skills/resolve-context/SKILL.md"
        duplicate.parent.mkdir(parents=True, exist_ok=True)
        duplicate.write_text(
            (workflow_repo / ".agents/skills/resolve-context/SKILL.md").read_text(encoding="utf-8"),
            encoding="utf-8",
        )
        expect_failure(
            "duplicate provider workflow",
            run_script(source, workflow_repo, "scripts/validate_agent_workflows.py", "--repo", str(workflow_repo)),
            errors,
        )

        okf_repo = clone_repo(source, tmp, "okf")
        okf = okf_repo / "knowledge/index.md"
        okf.write_text(okf.read_text(encoding="utf-8") + "\nDRIFT\n", encoding="utf-8")
        expect_failure(
            "generated OKF drift",
            run_script(source, okf_repo, "scripts/generate_okf_projection.py", "--repo", str(okf_repo), "--check"),
            errors,
        )

        stable_repo = clone_repo(source, tmp, "stable")
        stable = stable_repo / "docs/routing/stable_reference_index.json"
        stable.write_text(stable.read_text(encoding="utf-8") + " ", encoding="utf-8")
        expect_failure(
            "stable-reference index drift",
            run_script(source, stable_repo, "scripts/generate_stable_reference_index.py", "--repo", str(stable_repo), "--check"),
            errors,
        )

        candidate_repo = clone_repo(source, tmp, "candidate")
        qualification_path = candidate_repo / "docs/routing/downstream_candidate_qualification.json"
        qualification = json.loads(qualification_path.read_text(encoding="utf-8"))
        qualification["summary"]["adopted"] = 1
        qualification_path.write_text(json.dumps(qualification, indent=2) + "\n", encoding="utf-8")
        expect_failure(
            "candidate adoption leakage",
            run_script(source, candidate_repo, "scripts/validate_candidate_qualification.py", "--repo", str(candidate_repo)),
            errors,
        )

        architecture_repo = clone_repo(source, tmp, "architecture")
        architecture_path = architecture_repo / "docs/routing/architecture_reentry_plan.json"
        architecture = json.loads(architecture_path.read_text(encoding="utf-8"))
        architecture["questions"][1]["selected_option"] = architecture["questions"][1]["alternative_classes"][0]
        architecture["questions"][1]["status"] = "DECIDED"
        architecture["state"]["selected_question_count"] = 1
        architecture["state"]["accepted_architecture_established"] = True
        architecture_path.write_text(json.dumps(architecture, indent=2) + "\n", encoding="utf-8")
        expect_failure(
            "architecture pre-selection leakage",
            run_script(source, architecture_repo, "scripts/validate_architecture_reentry_plan.py", "--repo", str(architecture_repo)),
            errors,
        )

        implementation_repo = clone_repo(source, tmp, "implementation")
        framework_path = implementation_repo / "docs/routing/implementation_program_framework.json"
        framework = json.loads(framework_path.read_text(encoding="utf-8"))
        framework["state"]["package_derivation_allowed"] = True
        framework["state"]["implementation_execution_authorized"] = True
        framework["state"]["active_package_count"] = 1
        framework["state"]["active_packages"] = ["IMP-001"]
        framework_path.write_text(json.dumps(framework, indent=2) + "\n", encoding="utf-8")
        expect_failure(
            "implementation execution leakage",
            run_script(source, implementation_repo, "scripts/validate_implementation_program_framework.py", "--repo", str(implementation_repo)),
            errors,
        )

        phase019_repo = clone_repo(source, tmp, "phase019")
        phase019_path = phase019_repo / "docs/routing/phase019_architecture_decision_control.json"
        phase019 = json.loads(phase019_path.read_text(encoding="utf-8"))
        completed = set(phase019["phase019_state"]["completed_subphases"])
        premature = next(
            (
                item
                for item in phase019["decisions"]
                if item["owning_subphase"] not in completed
            ),
            None,
        )
        if premature is None:
            # At the 019-K -> 019-L boundary all governed ADQ decisions are
            # legitimately accepted. Reconstruct a pre-owner-completion state
            # so this negative control continues to prove that an accepted
            # decision cannot outrun its owning subphase.
            premature = phase019["decisions"][-1]
            owner = premature["owning_subphase"]
            phase019["phase019_state"]["completed_subphases"] = [
                sid
                for sid in phase019["phase019_state"]["completed_subphases"]
                if sid != owner
            ]
            phase019["phase019_state"]["next_eligible_subphase"] = owner
            for subphase in phase019["subphase_plan"]:
                if subphase["id"] == owner:
                    subphase["status"] = "NEXT_ELIGIBLE"
                elif subphase["id"] > owner and subphase["status"] == "NEXT_ELIGIBLE":
                    subphase["status"] = "PLANNED"
        else:
            premature["state"] = "ACCEPTED"
            premature["accepted"] = True
            premature["selected_option"] = "premature selection"
            premature["decision_document"] = "unauthorized.md"
            premature["rationale"] = "premature"
            premature["evidence_refs"] = ["premature"]
            premature["alternatives_evaluated"] = ["a", "b"]
            premature["accepted_in_subphase"] = premature["owning_subphase"]
            phase019["counts"]["decisions_accepted"] += 1
        phase019_path.write_text(json.dumps(phase019, indent=2) + "\n", encoding="utf-8")
        expect_failure(
            "Phase 019 premature decision acceptance",
            run_script(source, phase019_repo, "scripts/validate_phase019_architecture_control.py", "--repo", str(phase019_repo)),
            errors,
        )

        phase020_repo = clone_repo(source, tmp, "phase020")
        phase020_path = phase020_repo / "docs/routing/phase020_implementation_design_control.json"
        phase020 = json.loads(phase020_path.read_text(encoding="utf-8"))
        phase020["state"]["implementation_execution_authorized"] = True
        phase020["implementation_boundary"]["mudac_domain_implementation_authorized"] = True
        phase020_path.write_text(json.dumps(phase020, indent=2) + "\n", encoding="utf-8")
        expect_failure(
            "Phase 020 implementation-authority leakage",
            run_script(source, phase020_repo, "scripts/validate_phase020_implementation_design_control.py", "--repo", str(phase020_repo)),
            errors,
        )

        autonomous_repo = clone_repo(source, tmp, "autonomous")
        operating_path = autonomous_repo / "docs/routing/autonomous_implementation_operating_model.json"
        operating = json.loads(operating_path.read_text(encoding="utf-8"))
        operating["delegation"]["max_delegation_depth"] = 2
        operating_path.write_text(json.dumps(operating, indent=2) + "\n", encoding="utf-8")
        expect_failure(
            "Autonomous recursive-delegation leakage",
            run_script(source, autonomous_repo, "scripts/validate_agent_workflows.py", "--repo", str(autonomous_repo)),
            errors,
        )

        test_control_repo = clone_repo(source, tmp, "test-control")
        test_control_path = test_control_repo / "docs/routing/phase020_nonproduction_test_control_architecture.json"
        test_control = json.loads(test_control_path.read_text(encoding="utf-8"))
        test_control["production_denial"]["production_target_forbidden"] = False
        test_control_path.write_text(json.dumps(test_control, indent=2) + "\n", encoding="utf-8")
        expect_failure(
            "Nonproduction MCP production-target leakage",
            run_script(source, test_control_repo, "scripts/validate_phase020_implementation_design_control.py", "--repo", str(test_control_repo)),
            errors,
        )

        package_graph_repo = clone_repo(source, tmp, "package-graph")
        package_graph_path = package_graph_repo / "docs/routing/phase020_implementation_package_discovery.json"
        package_graph = json.loads(package_graph_path.read_text(encoding="utf-8"))
        package_graph["hard_edges"].append({
            "from": "IMP-012",
            "to": "IMP-001",
            "type": "HARD_G2_PREDECESSOR",
        })
        package_graph_path.write_text(json.dumps(package_graph, indent=2) + "\n", encoding="utf-8")
        expect_failure(
            "Implementation package dependency-cycle leakage",
            run_script(source, package_graph_repo, "scripts/validate_phase020_implementation_design_control.py", "--repo", str(package_graph_repo)),
            errors,
        )

        hidden_eval_repo = clone_repo(source, tmp, "hidden-eval")
        phase_contract_path = hidden_eval_repo / "docs/routing/phase020_implementation_phase_contract.json"
        phase_contract = json.loads(phase_contract_path.read_text(encoding="utf-8"))
        phase_contract["protected_evaluator"]["hidden_requirements_forbidden"] = False
        phase_contract_path.write_text(json.dumps(phase_contract, indent=2) + "\n", encoding="utf-8")
        expect_failure(
            "Protected-evaluator hidden-requirement leakage",
            run_script(source, hidden_eval_repo, "scripts/validate_phase020_implementation_design_control.py", "--repo", str(hidden_eval_repo)),
            errors,
        )

        ci_evidence_repo = clone_repo(source, tmp, "ci-evidence")
        ci_evidence_path = ci_evidence_repo / "docs/routing/phase020_ci_supplychain_evidence_architecture.json"
        ci_evidence = json.loads(ci_evidence_path.read_text(encoding="utf-8"))
        ci_evidence["exact_revision"]["required_for_exit_evidence"] = False
        ci_evidence["supply_chain"]["github_actions"]["blocking_and_exit_actions_full_commit_sha_required"] = False
        ci_evidence["protected_evaluator_binding"]["may_modify_candidate_source"] = True
        ci_evidence_path.write_text(json.dumps(ci_evidence, indent=2) + "\n", encoding="utf-8")
        expect_failure(
            "020-G exact-revision/evidence-contract weakening",
            run_script(source, ci_evidence_repo, "scripts/validate_phase020_implementation_design_control.py", "--repo", str(ci_evidence_repo)),
            errors,
        )

        review_exit_repo = clone_repo(source, tmp, "review-exit")
        review_exit_path = review_exit_repo / "docs/routing/phase020_review_repair_exit_gate_governance.json"
        review_exit = json.loads(review_exit_path.read_text(encoding="utf-8"))
        review_exit["independent_code_review"]["same_authoring_run_forbidden"] = False
        review_exit["repair"]["may_expand_scope"] = True
        review_exit["gatekeeper"]["may_override_mandatory_failure"] = True
        review_exit["completion_record"]["immutable"] = False
        review_exit["reopen_authorization"]["automatic_old_g2_restoration"] = True
        review_exit_path.write_text(json.dumps(review_exit, indent=2) + "\n", encoding="utf-8")
        expect_failure(
            "020-H review/reopen authority collapse",
            run_script(source, review_exit_repo, "scripts/validate_phase020_implementation_design_control.py", "--repo", str(review_exit_repo)),
            errors,
        )

        crosscut_repo = clone_repo(source, tmp, "crosscut")
        crosscut_path = crosscut_repo / "docs/routing/phase020_crosscutting_verification_architecture.json"
        crosscut = json.loads(crosscut_path.read_text(encoding="utf-8"))
        crosscut["scenario_matrix"] = crosscut["scenario_matrix"][:-1]
        crosscut["accessibility_verification"]["automated_scan_alone_proves_wcag_conformance"] = True
        crosscut["recovery_verification"]["database_restore_alone_is_semantic_recovery"] = True
        crosscut["performance_verification"]["threshold_contract"]["hidden_threshold_forbidden"] = False
        crosscut["cost_verification"]["mandatory_trust_controls_may_be_removed_for_cost_only"] = True
        crosscut_path.write_text(json.dumps(crosscut, indent=2) + "\n", encoding="utf-8")
        expect_failure(
            "020-I cross-cutting scenario/evidence erosion",
            run_script(source, crosscut_repo, "scripts/validate_phase020_implementation_design_control.py", "--repo", str(crosscut_repo)),
            errors,
        )

        v1_repo = clone_repo(source, tmp, "v1-completion")
        v1_path = v1_repo / "docs/routing/phase020_v1_completion_integration_design.json"
        v1 = json.loads(v1_path.read_text(encoding="utf-8"))
        v1["v1_scope"]["current_concepts"] = v1["v1_scope"]["current_concepts"][:-1]
        v1["integrated_journeys"] = v1["integrated_journeys"][:-1]
        v1["whole_system_criteria"][0]["blocking"] = False
        v1["final_integration_hardening_phase"]["creates_new_product_scope"] = True
        v1["v1_completion_state"]["grants_g6_release_candidate"] = True
        v1["residual_risk_policy"]["zero_known_blocking_findings_required"] = False
        v1_path.write_text(json.dumps(v1, indent=2) + "\n", encoding="utf-8")
        expect_failure(
            "020-J v1 scope/final-integration authority expansion",
            run_script(source, v1_repo, "scripts/validate_phase020_implementation_design_control.py", "--repo", str(v1_repo)),
            errors,
        )

        roadmap_repo = clone_repo(source, tmp, "roadmap")
        roadmap_path = roadmap_repo / "docs/routing/phase020_autonomous_implementation_roadmap.json"
        roadmap = json.loads(roadmap_path.read_text(encoding="utf-8"))
        roadmap["boundary"]["package_g1_is_execution_authority"] = True
        roadmap["boundary"]["implementation_execution_authorized"] = True
        roadmap["readiness_summary"]["g2_authorized_count"] = 1
        roadmap["readiness_summary"]["first_phase_g2_authorized"] = True
        roadmap["agent_strategy"]["recursive_delegation"] = True
        roadmap["agent_strategy"]["worktree_isolation_required"] = False
        roadmap["phase_sequence"][0]["next_phase_auto_authorization"] = True
        roadmap["packages"][0]["g1_evidence"]["visible_criteria_instantiated"] = False
        roadmap["packages"][0]["dependencies"]["hard"] = ["IMP-015"]
        roadmap_path.write_text(json.dumps(roadmap, indent=2) + "\n", encoding="utf-8")
        expect_failure(
            "020-K G1/G2 roadmap authority collapse",
            run_script(source, roadmap_repo, "scripts/validate_phase020_implementation_design_control.py", "--repo", str(roadmap_repo)),
            errors,
        )

        workflow_pin_repo = clone_repo(source, tmp, "workflow-pin")
        workflow_pin_path = workflow_pin_repo / ".github/workflows/knowledge-validation.yml"
        workflow_pin_text = workflow_pin_path.read_text(encoding="utf-8")
        workflow_pin_text = re.sub(
            r"actions/checkout@[0-9a-f]{40}",
            "actions/checkout@v6",
            workflow_pin_text,
            count=1,
        )
        workflow_pin_path.write_text(workflow_pin_text, encoding="utf-8")
        expect_failure(
            "020-G mutable GitHub Action pin",
            run_script(source, workflow_pin_repo, "scripts/validate_phase020_implementation_design_control.py", "--repo", str(workflow_pin_repo)),
            errors,
        )

        exit_audit_repo = clone_repo(source, tmp, "exit-audit")
        exit_audit_path = exit_audit_repo / "docs/routing/phase020_preimplementation_exit_audit.json"
        exit_audit = json.loads(exit_audit_path.read_text(encoding="utf-8"))
        exit_audit["repository_enforcement_evidence"]["main_protected"] = False
        exit_audit["repository_enforcement_evidence"]["ruleset_enforcement"] = "disabled"
        exit_audit["phase021_handoff"]["g2_state"] = "AUTHORIZED"
        exit_audit_path.write_text(json.dumps(exit_audit, indent=2) + "\n", encoding="utf-8")
        expect_failure(
            "020-L enforcement regression after closure",
            run_script(source, exit_audit_repo, "scripts/validate_phase020_implementation_design_control.py", "--repo", str(exit_audit_repo)),
            errors,
        )

        knowledge_pr_repo = clone_repo(source, tmp, "knowledge-pr-filter")
        knowledge_pr_path = knowledge_pr_repo / ".github/workflows/knowledge-validation.yml"
        knowledge_pr_text = knowledge_pr_path.read_text(encoding="utf-8")
        knowledge_pr_text = knowledge_pr_text.replace(
            "  pull_request:\n    branches:\n      - main\n",
            "  pull_request:\n    paths:\n      - docs/**\n",
            1,
        )
        knowledge_pr_path.write_text(knowledge_pr_text, encoding="utf-8")
        expect_failure(
            "020-G required Knowledge Validation path filtering",
            run_script(source, knowledge_pr_repo, "scripts/validate_phase020_implementation_design_control.py", "--repo", str(knowledge_pr_repo)),
            errors,
        )

        secret_repo = clone_repo(source, tmp, "secret")
        leak = secret_repo / ".agents/leak.txt"
        leak.parent.mkdir(parents=True, exist_ok=True)
        leak.write_text("token=" + "ghp_" + ("A" * 36) + "\n", encoding="utf-8")
        expect_failure(
            "high-confidence secret insertion",
            run_script(source, secret_repo, "scripts/scan_agentic_secrets.py", "--repo", str(secret_repo)),
            errors,
        )

    for error in errors:
        print("ERROR", error)
    print(f"Agentic negative controls: {len(errors)} error(s), 23 guard mutation(s) exercised")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())

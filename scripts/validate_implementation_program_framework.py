#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

FRAMEWORK = "docs/routing/implementation_program_framework.json"
ARCHITECTURE_PLAN = "docs/routing/architecture_reentry_plan.json"

EXPECTED_LIFECYCLE = [
    "PROPOSED",
    "PLANNED",
    "READY_FOR_AUTHORIZATION",
    "AUTHORIZED",
    "IN_PROGRESS",
    "EVIDENCE_REVIEW",
    "COMPLETE",
    "BLOCKED",
    "SUPERSEDED",
    "CANCELLED",
]
EXPECTED_EVIDENCE = [f"E{i}" for i in range(1, 8)]
EXPECTED_GATES = [f"G{i}" for i in range(0, 8)]
EXPECTED_REQUIRED_FIELDS = {
    "id",
    "title",
    "purpose",
    "status",
    "scope_in",
    "scope_out",
    "semantic_refs",
    "architecture_refs",
    "eng_refs",
    "dependencies",
    "owned_surfaces",
    "data_migration_impact",
    "security_privacy_impact",
    "accessibility_degraded_impact",
    "failure_recovery_impact",
    "required_evidence_classes",
    "scenario_seeds",
    "compatibility_rollback",
    "residual_risks",
}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", default=".")
    args = parser.parse_args()
    repo = Path(args.repo).resolve()
    errors: list[str] = []

    try:
        framework = json.loads((repo / FRAMEWORK).read_text(encoding="utf-8"))
        architecture = json.loads((repo / ARCHITECTURE_PLAN).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print("ERROR", exc)
        return 1

    state = framework.get("state", {})
    arch_state = architecture.get("state", {})

    if state.get("framework_state") != "PRE_ARCHITECTURE":
        errors.append("framework_state must remain PRE_ARCHITECTURE in Phase 018-L")
    if state.get("accepted_architecture_required") is not True:
        errors.append("accepted_architecture_required must be true")
    if state.get("accepted_architecture_established") is not False:
        errors.append("implementation framework cannot claim accepted architecture")
    if state.get("package_derivation_allowed") is not False:
        errors.append("package derivation must remain blocked before architecture acceptance")
    if state.get("implementation_execution_authorized") is not False:
        errors.append("implementation execution must remain unauthorized")
    if state.get("active_package_count") != 0:
        errors.append("active_package_count must remain zero before architecture acceptance")
    if state.get("active_packages") != []:
        errors.append("active_packages must remain empty before architecture acceptance")

    if arch_state.get("accepted_architecture_established") is not False:
        errors.append("architecture plan is not in expected pre-selection state")
    if arch_state.get("accepted_architecture_established") != state.get("accepted_architecture_established"):
        errors.append("architecture/implementation accepted-architecture state drift")

    if framework.get("package_lifecycle") != EXPECTED_LIFECYCLE:
        errors.append("package lifecycle drift")

    execution_states = framework.get("execution_states")
    if execution_states != ["AUTHORIZED", "IN_PROGRESS", "EVIDENCE_REVIEW"]:
        errors.append("execution_states drift")

    schema = framework.get("package_schema", {})
    required_fields = schema.get("required_fields")
    if not isinstance(required_fields, list):
        errors.append("package_schema.required_fields must be a list")
    elif set(required_fields) != EXPECTED_REQUIRED_FIELDS:
        errors.append(
            "package schema field drift: "
            f"missing={sorted(EXPECTED_REQUIRED_FIELDS - set(required_fields))} "
            f"extra={sorted(set(required_fields) - EXPECTED_REQUIRED_FIELDS)}"
        )

    evidence = framework.get("evidence_classes")
    if not isinstance(evidence, list):
        errors.append("evidence_classes must be a list")
        evidence = []
    evidence_ids = [item.get("id") for item in evidence if isinstance(item, dict)]
    if evidence_ids != EXPECTED_EVIDENCE:
        errors.append(f"evidence class drift: expected {EXPECTED_EVIDENCE}, got {evidence_ids}")
    for item in evidence:
        if not isinstance(item, dict):
            errors.append("evidence class entry must be an object")
            continue
        if not item.get("name"):
            errors.append(f"{item.get('id')}: evidence class name required")
        examples = item.get("examples")
        if not isinstance(examples, list) or not examples:
            errors.append(f"{item.get('id')}: evidence examples required")

    scenarios = framework.get("scenario_seeds")
    if not isinstance(scenarios, list) or len(scenarios) != 15:
        errors.append("exactly 15 Phase-016 scenario seeds must be retained")
    elif len(set(scenarios)) != len(scenarios):
        errors.append("scenario seeds must be unique")

    gates = framework.get("gates")
    if not isinstance(gates, list):
        errors.append("gates must be a list")
        gates = []
    gate_ids = [item.get("id") for item in gates if isinstance(item, dict)]
    if gate_ids != EXPECTED_GATES:
        errors.append(f"delivery gate drift: expected {EXPECTED_GATES}, got {gate_ids}")

    execution_authority_gates: list[str] = []
    for gate in gates:
        if not isinstance(gate, dict):
            errors.append("gate entry must be an object")
            continue
        gid = gate.get("id")
        if not gate.get("name"):
            errors.append(f"{gid}: gate name required")
        requires = gate.get("requires")
        if not isinstance(requires, list) or not requires:
            errors.append(f"{gid}: gate requirements required")
        if gate.get("execution_authority") is True:
            execution_authority_gates.append(str(gid))

    if execution_authority_gates != ["G2"]:
        errors.append(
            "only G2 may grant package execution authority; "
            f"found {execution_authority_gates}"
        )

    rules = framework.get("planning_rules", {})
    required_true = {
        "derive_packages_only_after_architecture",
        "dependency_graph_required",
        "dependency_graph_must_be_acyclic",
        "package_completion_does_not_authorize_next",
        "merge_does_not_authorize_deploy",
        "complete_does_not_equal_production_ready",
        "synthetic_fixtures_default",
        "secrets_in_source_forbidden",
        "migration_compatibility_required_when_state_changes",
    }
    for key in required_true:
        if rules.get(key) is not True:
            errors.append(f"planning_rules.{key} must be true")
    if rules.get("auto_advance_packages") is not False:
        errors.append("planning_rules.auto_advance_packages must be false")

    start_gate = framework.get("future_start_gate", {})
    if start_gate.get("decomposition_state") != "DEFERRED_UNTIL_ACCEPTED_ARCHITECTURE":
        errors.append("future implementation decomposition must remain deferred until architecture acceptance")
    if start_gate.get("proposed_lifecycle") != "Phase 020 — Implementation Planning & Controlled Delivery":
        errors.append("future implementation lifecycle label drift")
    actions = start_gate.get("required_actions")
    if not isinstance(actions, list) or len(actions) < 8:
        errors.append("future implementation start gate actions are incomplete")

    authority = str(framework.get("authority", ""))
    if "DOES NOT CREATE PACKAGES OR AUTHORIZE EXECUTION" not in authority:
        errors.append("framework authority banner must deny package creation and execution authority")

    for error in errors:
        print("ERROR", error)
    print(
        "Implementation program framework: "
        f"{len(errors)} error(s), "
        f"{state.get('active_package_count')} active package(s), "
        f"package_derivation_allowed={state.get('package_derivation_allowed')}, "
        f"implementation_execution_authorized={state.get('implementation_execution_authorized')}"
    )
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())

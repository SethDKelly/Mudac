#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

PLAN = "docs/routing/architecture_reentry_plan.json"
QUALIFICATION = "docs/routing/downstream_candidate_qualification.json"
STABLE_INDEX = "docs/routing/stable_reference_index.json"

ADQ_RE = re.compile(r"^ADQ-\d{3}$")
SUBPHASE_RE = re.compile(r"^019-[A-L]$")

ALLOWED_KINDS = {"FOUNDATION", "DECISION", "VALIDATION"}
ALLOWED_HANDLING = {"COMPARISON_INPUT", "REVISION_REQUIRED_BEFORE_COMPARISON"}


def has_cycle(nodes: dict[str, list[str]]) -> bool:
    state: dict[str, int] = {}

    def visit(node: str) -> bool:
        mark = state.get(node, 0)
        if mark == 1:
            return True
        if mark == 2:
            return False
        state[node] = 1
        for dep in nodes.get(node, []):
            if visit(dep):
                return True
        state[node] = 2
        return False

    return any(visit(node) for node in nodes)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", default=".")
    args = parser.parse_args()
    repo = Path(args.repo).resolve()
    errors: list[str] = []

    try:
        plan = json.loads((repo / PLAN).read_text(encoding="utf-8"))
        qualification = json.loads((repo / QUALIFICATION).read_text(encoding="utf-8"))
        stable = json.loads((repo / STABLE_INDEX).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print("ERROR", exc)
        return 1

    state = plan.get("state", {})
    if state.get("framework_state") != "PRE_SELECTION":
        errors.append("framework_state must remain PRE_SELECTION during Phase 018-K")
    if state.get("accepted_architecture_established") is not False:
        errors.append("accepted_architecture_established must remain false")
    if state.get("implementation_execution_authorized") is not False:
        errors.append("implementation_execution_authorized must remain false")

    questions = plan.get("questions")
    if not isinstance(questions, list):
        print("ERROR questions must be a list")
        return 1

    expected_ids = {f"ADQ-{i:03d}" for i in range(1, 11)}
    actual_ids = {q.get("id") for q in questions if isinstance(q, dict)}
    if actual_ids != expected_ids:
        errors.append(
            f"question ID set drift: missing={sorted(expected_ids - actual_ids)} "
            f"extra={sorted(actual_ids - expected_ids)}"
        )

    if state.get("question_count") != len(questions):
        errors.append("state.question_count drift")

    selected_count = 0
    graph: dict[str, list[str]] = {}
    stable_refs = stable.get("references", {})

    qualified = {
        item.get("path"): item
        for item in qualification.get("records", [])
        if isinstance(item, dict) and item.get("layer") == "architecture"
    }

    for q in questions:
        if not isinstance(q, dict):
            errors.append("question record must be an object")
            continue
        qid = q.get("id")
        if not isinstance(qid, str) or not ADQ_RE.match(qid):
            errors.append(f"invalid question id {qid!r}")
            continue

        kind = q.get("kind")
        if kind not in ALLOWED_KINDS:
            errors.append(f"{qid}: invalid kind {kind!r}")
        if q.get("status") != "PLANNED":
            errors.append(f"{qid}: status must remain PLANNED during pre-selection")
        if q.get("selected_option") is not None:
            selected_count += 1
            errors.append(f"{qid}: selected_option must remain null during Phase 018-K")

        deps = q.get("dependencies")
        if not isinstance(deps, list):
            errors.append(f"{qid}: dependencies must be a list")
            deps = []
        if qid in deps:
            errors.append(f"{qid}: cannot depend on itself")
        for dep in deps:
            if dep not in expected_ids:
                errors.append(f"{qid}: unknown dependency {dep}")
        graph[qid] = deps

        constraints = q.get("constraints")
        if not isinstance(constraints, list) or not constraints:
            errors.append(f"{qid}: current constraint references required")
            constraints = []
        for ref in constraints:
            entry = stable_refs.get(ref)
            if not isinstance(entry, dict):
                errors.append(f"{qid}: unknown stable constraint {ref}")
            elif entry.get("role") != "current-authority":
                errors.append(f"{qid}: constraint {ref} must resolve as current-authority")

        alternatives = q.get("alternative_classes")
        if not isinstance(alternatives, list):
            errors.append(f"{qid}: alternative_classes must be a list")
            alternatives = []
        if kind == "DECISION" and len(alternatives) < 2:
            errors.append(f"{qid}: material decision requires at least two credible alternative classes")

        candidate_inputs = q.get("candidate_inputs")
        handling = q.get("candidate_handling")
        if not isinstance(candidate_inputs, list):
            errors.append(f"{qid}: candidate_inputs must be a list")
            candidate_inputs = []
        if not isinstance(handling, dict):
            errors.append(f"{qid}: candidate_handling must be an object")
            handling = {}
        if set(candidate_inputs) != set(handling):
            errors.append(f"{qid}: candidate_handling keys must exactly match candidate_inputs")

        for path in candidate_inputs:
            item = qualified.get(path)
            if not item:
                errors.append(f"{qid}: candidate input is not a qualified architecture candidate: {path}")
                continue
            if item.get("eligible_for_018k_comparison") is not True:
                errors.append(f"{qid}: candidate is not eligible for 018-K comparison: {path}")
            expected = (
                "REVISION_REQUIRED_BEFORE_COMPARISON"
                if item.get("requires_semantic_revision") is True
                else "COMPARISON_INPUT"
            )
            if handling.get(path) != expected:
                errors.append(
                    f"{qid}: {path} handling must be {expected}, got {handling.get(path)!r}"
                )
            if handling.get(path) not in ALLOWED_HANDLING:
                errors.append(f"{qid}: invalid candidate handling for {path}")

        for field in ("scope",):
            value = q.get(field)
            if not isinstance(value, str) or not value.strip():
                errors.append(f"{qid}: {field} is required")
        for field in ("evidence_focus", "scenario_seeds", "deferrals"):
            value = q.get(field)
            if not isinstance(value, list) or not value:
                errors.append(f"{qid}: {field} must be a non-empty list")

    if has_cycle(graph):
        errors.append("architecture question dependency graph contains a cycle")

    if state.get("selected_question_count") != selected_count:
        errors.append(
            f"state.selected_question_count drift: expected {selected_count}, "
            f"got {state.get('selected_question_count')}"
        )
    if selected_count != 0:
        errors.append("pre-selection plan must have zero selected questions")

    program = plan.get("reentry_program")
    if not isinstance(program, dict):
        errors.append("reentry_program must be an object")
    else:
        if program.get("authorization_state") != "PLANNED_NOT_AUTHORIZED_BY_018_K_ALONE":
            errors.append("reentry program must remain planned/not authorized by 018-K alone")
        subphases = program.get("subphases")
        if not isinstance(subphases, list):
            errors.append("reentry_program.subphases must be a list")
        else:
            expected_subphases = [f"019-{chr(ord('A') + i)}" for i in range(12)]
            actual_subphases = [item.get("id") for item in subphases if isinstance(item, dict)]
            if actual_subphases != expected_subphases:
                errors.append(
                    f"019 re-entry decomposition drift: expected {expected_subphases}, "
                    f"got {actual_subphases}"
                )
            for item in subphases:
                if not isinstance(item, dict):
                    errors.append("019 subphase record must be an object")
                    continue
                sid = item.get("id")
                if not isinstance(sid, str) or not SUBPHASE_RE.match(sid):
                    errors.append(f"invalid 019 subphase id {sid!r}")
                qrefs = item.get("questions")
                if not isinstance(qrefs, list) or not qrefs:
                    errors.append(f"{sid}: question references required")
                else:
                    for ref in qrefs:
                        if ref not in expected_ids:
                            errors.append(f"{sid}: unknown question reference {ref}")

    if "DOES NOT SELECT OR ACCEPT ARCHITECTURE" not in str(plan.get("authority", "")):
        errors.append("plan authority banner must explicitly deny architecture selection/acceptance")

    for error in errors:
        print("ERROR", error)
    print(
        "Architecture re-entry plan: "
        f"{len(errors)} error(s), {len(questions)} question(s), "
        f"{selected_count} selected, accepted_architecture={state.get('accepted_architecture_established')}"
    )
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())

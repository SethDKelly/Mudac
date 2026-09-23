#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

POLICY = "docs/routing/agentic_action_policy.json"
CONTRACT = "docs/canonical/governance/agentic-authority-scope.md"
AGENTS = "AGENTS.md"

def fail(message: str) -> int:
    print("ERROR", message)
    return 1

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", default=str(Path(__file__).resolve().parents[1]))
    args = parser.parse_args()
    repo = Path(args.repo).resolve()
    try:
        policy = json.loads((repo / POLICY).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return fail(f"cannot load agentic action policy: {exc}")

    if policy.get("canonical_contract") != CONTRACT:
        return fail("agentic action policy canonical_contract drift")
    if policy.get("authority") != "ROUTING/CONFORMANCE POLICY — CANONICAL AGENTIC AUTHORITY CONTRACT RETAINS NORMATIVE MEANING":
        return fail("agentic action policy authority boundary drift")

    expected_order = [
        "human-selected-task",
        "current-canonical-semantic-and-governance-authority",
        "repository-agent-and-change-control-governance",
        "active-accepted-architecture-or-implementation-package",
        "executable-evidence",
        "reviewed-external-tool-or-vendor-guidance",
        "agent-memory-and-conversational-assumptions",
    ]
    if policy.get("authority_order") != expected_order:
        return fail("agentic authority precedence drift")

    classes = policy.get("action_classes", {})
    if set(classes) != {"A1", "A2", "A3", "A4"}:
        return fail("action classes must be exactly A1, A2, A3, A4")
    if classes["A1"].get("repository_edits") is not False:
        return fail("A1 must not authorize repository edits")
    if classes["A2"].get("repository_edits") is not True:
        return fail("A2 must authorize bounded repository edits")
    if classes["A2"].get("external_or_destructive_actions") is not False:
        return fail("A2 must not authorize external/destructive actions")
    if classes["A2"].get("semantic_or_architecture_adoption") is not False:
        return fail("A2 must not authorize semantic/architecture adoption")
    if classes["A3"].get("explicit_additional_authorization") is not True:
        return fail("A3 must require explicit additional authorization")
    if classes["A3"].get("external_or_destructive_actions") is not True:
        return fail("A3 must represent external/destructive/scope-expanding actions")
    if classes["A4"].get("explicit_additional_authorization") is not True:
        return fail("A4 must require explicit human change intent")
    if classes["A4"].get("semantic_or_architecture_adoption") is not True:
        return fail("A4 must represent semantic/architecture change")
    if classes["A4"].get("change_control") != "docs/canonical/governance/change-governance.md":
        return fail("A4 change-control route drift")

    human = policy.get("human_directed", {})
    for key in (
        "required",
        "no_autonomous_next_work",
        "no_unbounded_unattended_task_queue",
        "bounded_delegation_requires_authorized_envelope",
        "coordinator_only_delegation",
        "no_implicit_merge_or_deploy",
    ):
        if human.get(key) is not True:
            return fail(f"human-directed boundary missing: {key}")

    autonomous = policy.get("autonomous_implementation", {})
    if autonomous.get("operating_model") != "docs/routing/autonomous_implementation_operating_model.json":
        return fail("autonomous implementation operating-model route drift")
    if autonomous.get("g2_required") is not True:
        return fail("autonomous implementation requires G2")
    if autonomous.get("coordinator_only_delegation") is not True:
        return fail("implementation delegation must remain coordinator-only")
    if autonomous.get("recursive_implementation_delegation") is not False:
        return fail("recursive implementation delegation must remain false")
    if autonomous.get("next_phase_auto_authorization") is not False:
        return fail("bounded autonomy must not auto-authorize next phase")
    if classes["A2"].get("bounded_subagent_delegation") is None:
        return fail("A2 must define bounded subagent delegation boundary")
    if classes["A3"].get("delegation_outside_authorized_envelope") is not True:
        return fail("A3 must retain out-of-envelope delegation as scope expansion")

    completion = policy.get("completion", {})
    for key in ("stop_at_selected_task_boundary","report_next_eligible_work_only","validation_pass_does_not_authorize_next_work"):
        if completion.get(key) is not True:
            return fail(f"completion boundary missing: {key}")

    contract = (repo / CONTRACT).read_text(encoding="utf-8")
    for token in [f"AGT-{i:03d}" for i in range(1,17)]:
        if f'id="{token.lower()}"' not in contract:
            return fail(f"canonical agentic contract missing {token}")

    agents = (repo / AGENTS).read_text(encoding="utf-8")
    if "agentic-authority-scope.md" not in agents:
        return fail("AGENTS.md must route to canonical agentic authority contract")
    for token in ("A1", "A2", "A3", "A4"):
        if token not in agents:
            return fail(f"AGENTS.md must expose {token} bootstrap class")

    print("Agentic authority policy check: 0 errors; A1–A4, human lifecycle authority, and bounded G2 delegation intact")
    return 0

if __name__ == "__main__":
    sys.exit(main())

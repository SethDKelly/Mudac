#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

CONTROL = "docs/routing/phase019_architecture_decision_control.json"
ARCH_PLAN = "docs/routing/architecture_reentry_plan.json"
QUALIFICATION = "docs/routing/downstream_candidate_qualification.json"
IMPLEMENTATION = "docs/routing/implementation_program_framework.json"
DISPOSITION = "docs/routing/phase019_architecture_candidate_disposition.json"

EXPECTED_CLOSURE_COMMIT = "526b8533395e7cbdabf567c56115f024b78a10f5"
EXPECTED_QUESTIONS = [f"ADQ-{i:03d}" for i in range(1, 11)]
EXPECTED_SUBPHASES = [f"019-{chr(ord('A') + i)}" for i in range(12)]
OWNING = {
    "ADQ-001": "019-B",
    "ADQ-002": "019-C",
    "ADQ-003": "019-D",
    "ADQ-004": "019-E",
    "ADQ-005": "019-F",
    "ADQ-006": "019-G",
    "ADQ-007": "019-H",
    "ADQ-008": "019-I",
    "ADQ-009": "019-J",
    "ADQ-010": "019-K",
}
ALLOWED_DECISION_STATES = {
    "PLANNED",
    "EVALUATING",
    "PROPOSED",
    "ACCEPTED",
    "BLOCKED",
    "REOPENED",
    "SUPERSEDED",
}
ALLOWED_REPAIR_STATES = {"REQUIRED", "IN_PROGRESS", "COMPLETE", "SUPERSEDED"}
ALLOWED_PROBE_STATES = {"AUTHORIZED", "IN_PROGRESS", "COMPLETE", "CANCELLED"}
SHA_RE = re.compile(r"^[0-9a-f]{40}$")


def index_of_subphase(subphase: str) -> int:
    return EXPECTED_SUBPHASES.index(subphase)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", default=".")
    args = parser.parse_args()
    repo = Path(args.repo).resolve()
    errors: list[str] = []

    try:
        control = json.loads((repo / CONTROL).read_text(encoding="utf-8"))
        plan = json.loads((repo / ARCH_PLAN).read_text(encoding="utf-8"))
        qualification = json.loads((repo / QUALIFICATION).read_text(encoding="utf-8"))
        implementation = json.loads((repo / IMPLEMENTATION).read_text(encoding="utf-8"))
        disposition = json.loads((repo / DISPOSITION).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print("ERROR", exc)
        return 1

    if "DOES NOT ITSELF SELECT OR ACCEPT ARCHITECTURE" not in str(control.get("authority", "")):
        errors.append("decision-control authority banner must deny independent selection/acceptance")

    closure = control.get("phase018_closure", {})
    if closure.get("commit") != EXPECTED_CLOSURE_COMMIT:
        errors.append("Phase-018 closure commit drift")
    if closure.get("repository_readiness_score") != 96:
        errors.append("Phase-018 readiness score drift")

    snapshots = closure.get("snapshots")
    if not isinstance(snapshots, list) or len(snapshots) < 7:
        errors.append("Phase-018 entry snapshot set is incomplete")
    else:
        paths = set()
        for item in snapshots:
            if not isinstance(item, dict):
                errors.append("snapshot entry must be an object")
                continue
            path = item.get("path")
            sha = item.get("blob_sha")
            if not isinstance(path, str) or not path:
                errors.append("snapshot path required")
            elif path in paths:
                errors.append(f"duplicate snapshot path: {path}")
            else:
                paths.add(path)
            if not isinstance(sha, str) or not SHA_RE.match(sha):
                errors.append(f"{path}: snapshot blob_sha must be a 40-char git SHA")

    state = control.get("phase019_state", {})
    if state.get("automatic_advance") is not False:
        errors.append("Phase 019 automatic advance must remain false")

    completed = state.get("completed_subphases")
    if not isinstance(completed, list):
        errors.append("completed_subphases must be a list")
        completed = []
    if any(item not in EXPECTED_SUBPHASES for item in completed):
        errors.append(f"unknown completed subphase: {completed}")
    if len(set(completed)) != len(completed):
        errors.append("completed_subphases contains duplicates")

    expected_prefix = EXPECTED_SUBPHASES[: len(completed)]
    if completed != expected_prefix:
        errors.append(f"Phase-019 completed subphases must be contiguous; expected {expected_prefix}, got {completed}")

    next_eligible = state.get("next_eligible_subphase")
    if len(completed) < len(EXPECTED_SUBPHASES):
        expected_next = EXPECTED_SUBPHASES[len(completed)]
        if next_eligible != expected_next:
            errors.append(f"next eligible subphase must be {expected_next}, got {next_eligible}")
    elif next_eligible is not None:
        errors.append("next_eligible_subphase must be null after 019-L completion")

    authorized = state.get("currently_authorized_subphase")
    if authorized is not None:
        if authorized != next_eligible:
            errors.append("currently authorized subphase must equal the next eligible subphase")
        if authorized in completed:
            errors.append("completed subphase cannot remain currently authorized")

    subphase_plan = control.get("subphase_plan")
    if not isinstance(subphase_plan, list):
        errors.append("subphase_plan must be a list")
        subphase_plan = []
    ids = [x.get("id") for x in subphase_plan if isinstance(x, dict)]
    if ids != EXPECTED_SUBPHASES:
        errors.append(f"019 subphase plan drift: expected {EXPECTED_SUBPHASES}, got {ids}")
    for item in subphase_plan:
        if not isinstance(item, dict):
            continue
        sid = item.get("id")
        status = item.get("status")
        if sid in completed and status != "COMPLETE":
            errors.append(f"{sid}: completed subphase must have COMPLETE status")
        elif sid == next_eligible and status != "NEXT_ELIGIBLE":
            errors.append(f"{sid}: next eligible subphase must have NEXT_ELIGIBLE status")
        elif sid not in completed and sid != next_eligible and status != "PLANNED":
            errors.append(f"{sid}: future subphase must remain PLANNED")

    plan_ids = [q.get("id") for q in plan.get("questions", []) if isinstance(q, dict)]
    if plan_ids != EXPECTED_QUESTIONS:
        errors.append("architecture re-entry plan question set drift")

    records = control.get("decisions")
    if not isinstance(records, list):
        errors.append("decision records must be a list")
        records = []
    record_ids = [r.get("question_id") for r in records if isinstance(r, dict)]
    if record_ids != EXPECTED_QUESTIONS:
        errors.append(f"decision-record question set drift: {record_ids}")

    schema_fields = set(control.get("decision_record_schema", {}).get("required_fields", []))
    accepted_count = 0
    decision_by_id = {}
    for record in records:
        if not isinstance(record, dict):
            errors.append("decision record must be an object")
            continue
        qid = record.get("question_id")
        decision_by_id[qid] = record
        missing = schema_fields - set(record)
        if missing:
            errors.append(f"{qid}: missing decision fields {sorted(missing)}")
        if record.get("owning_subphase") != OWNING.get(qid):
            errors.append(f"{qid}: owning subphase drift")
        decision_state = record.get("state")
        if decision_state not in ALLOWED_DECISION_STATES:
            errors.append(f"{qid}: invalid decision state {decision_state!r}")

        accepted = record.get("accepted")
        if accepted is True:
            accepted_count += 1
            owner = record.get("owning_subphase")
            if owner not in completed:
                errors.append(f"{qid}: accepted before owning subphase {owner} completed")
            if decision_state != "ACCEPTED":
                errors.append(f"{qid}: accepted=true requires state ACCEPTED")
            if not record.get("selected_option"):
                errors.append(f"{qid}: accepted decision requires selected_option")
            if not record.get("decision_document"):
                errors.append(f"{qid}: accepted decision requires decision_document")
            if not record.get("rationale"):
                errors.append(f"{qid}: accepted decision requires rationale")
            if not record.get("evidence_refs"):
                errors.append(f"{qid}: accepted decision requires evidence_refs")
            if record.get("accepted_in_subphase") != owner:
                errors.append(f"{qid}: accepted_in_subphase must equal owning subphase")
            if qid in {f"ADQ-{i:03d}" for i in range(2, 10)}:
                if len(record.get("alternatives_evaluated", [])) < 2:
                    errors.append(f"{qid}: material accepted decision requires at least two evaluated alternatives")
        else:
            if accepted not in (False, None):
                errors.append(f"{qid}: accepted must be boolean")
            if decision_state == "ACCEPTED":
                errors.append(f"{qid}: state ACCEPTED requires accepted=true")

    repair_model = control.get("q4_repair_model", {})
    repairs = repair_model.get("records")
    if not isinstance(repairs, list):
        errors.append("Q4 repair records must be a list")
        repairs = []

    expected_q4 = {
        item.get("path"): item
        for item in qualification.get("records", [])
        if isinstance(item, dict)
        and item.get("layer") == "architecture"
        and item.get("requires_semantic_revision") is True
    }
    repair_paths = {item.get("candidate_path") for item in repairs if isinstance(item, dict)}
    if repair_paths != set(expected_q4):
        errors.append(
            "Q4 repair coverage drift: "
            f"missing={sorted(set(expected_q4) - repair_paths)} "
            f"extra={sorted(repair_paths - set(expected_q4))}"
        )

    completed_repairs = 0
    repair_by_path = {}
    for repair in repairs:
        if not isinstance(repair, dict):
            errors.append("Q4 repair record must be an object")
            continue
        path = repair.get("candidate_path")
        repair_by_path[path] = repair
        status = repair.get("repair_status")
        if status not in ALLOWED_REPAIR_STATES:
            errors.append(f"{path}: invalid Q4 repair state {status!r}")
        eligible = repair.get("comparison_eligible")
        if status == "COMPLETE":
            completed_repairs += 1
            if eligible is not True:
                errors.append(f"{path}: completed Q4 repair must be comparison eligible")
            for field in (
                "repair_document",
                "current_semantic_owner_refs",
                "revised_comparison_statement",
                "preservation_evidence_refs",
            ):
                value = repair.get(field)
                if value in (None, [], ""):
                    errors.append(f"{path}: completed Q4 repair requires {field}")
        elif eligible is not False:
            errors.append(f"{path}: incomplete Q4 repair cannot be comparison eligible")

    for qid, record in decision_by_id.items():
        if record.get("state") in {"PROPOSED", "ACCEPTED"}:
            for path in record.get("candidate_inputs", []):
                if path in expected_q4 and repair_by_path.get(path, {}).get("repair_status") != "COMPLETE":
                    errors.append(f"{qid}: cannot be {record.get('state')} while Q4 input {path} remains unrepaired")

    probe_model = control.get("probe_model", {})
    if probe_model.get("probes_authorized_by_019a") is not False:
        errors.append("019-A must not authorize technical probes")
    probes = probe_model.get("authorizations")
    if not isinstance(probes, list):
        errors.append("probe authorizations must be a list")
        probes = []
    probe_fields = set(probe_model.get("required_fields", []))
    for probe in probes:
        if not isinstance(probe, dict):
            errors.append("probe authorization must be an object")
            continue
        missing = probe_fields - set(probe)
        if missing:
            errors.append(f"probe missing fields {sorted(missing)}")
        if probe.get("status") not in ALLOWED_PROBE_STATES:
            errors.append(f"{probe.get('probe_id')}: invalid probe status")
        auth_subphase = probe.get("authorizing_subphase")
        if auth_subphase == "019-A":
            errors.append("019-A cannot authorize a technical probe")
        if auth_subphase not in completed:
            errors.append(f"{probe.get('probe_id')}: probe authorization subphase is not complete")

    whole = control.get("whole_architecture_acceptance", {})
    whole_accepted = whole.get("accepted")
    phase_closed = len(completed) == len(EXPECTED_SUBPHASES)
    expected_phase_status = "COMPLETE" if phase_closed else "ACTIVE"
    if state.get("status") != expected_phase_status:
        errors.append(f"Phase 019 status must be {expected_phase_status} for current completion state")

    impl_state = implementation.get("state", {})
    if whole_accepted is True:
        if "019-L" not in completed:
            errors.append("whole architecture cannot be accepted before 019-L completes")
        if accepted_count != 10:
            errors.append("whole architecture acceptance requires all ten ADQ decisions accepted")
        if completed_repairs != len(expected_q4):
            errors.append("whole architecture acceptance requires all Q4 repairs complete")
        if whole.get("state") != "ACCEPTED":
            errors.append("whole architecture accepted=true requires state ACCEPTED")
        if not whole.get("acceptance_document"):
            errors.append("whole architecture acceptance requires acceptance_document")
        if whole.get("accepted_architecture_owner") != "docs/canonical/architecture/accepted-architecture.md":
            errors.append("whole architecture acceptance must identify accepted-architecture current owner")
        if whole.get("historical_candidate_disposition") != DISPOSITION:
            errors.append("whole architecture acceptance must identify candidate disposition register")
        if state.get("package_derivation_allowed") is not True:
            errors.append("G0 acceptance must allow package derivation")
        if state.get("implementation_execution_authorized") is not False:
            errors.append("019-L acceptance must not authorize implementation execution")
        if state.get("implementation_package_count") != 0:
            errors.append("019-L must close with zero implementation packages")
        if impl_state.get("framework_state") not in {
            "PLANNING_READY",
            "ROADMAP_READY_PREIMPLEMENTATION_AUDIT_PENDING",
            "ROADMAP_READY_PHASE020_COMPLETE",
        }:
            errors.append("implementation framework must remain in an accepted post-architecture planning state")
        if impl_state.get("accepted_architecture_established") is not True:
            errors.append("implementation framework must acknowledge accepted architecture")
        if impl_state.get("package_derivation_allowed") is not True:
            errors.append("implementation framework must allow package derivation after G0")
        if impl_state.get("implementation_execution_authorized") is not False:
            errors.append("implementation framework execution must remain unauthorized after G0")
        if impl_state.get("active_package_count") != 0:
            errors.append("019-L handoff must retain zero active packages")

        qualified_architecture = {
            item.get("path")
            for item in qualification.get("records", [])
            if isinstance(item, dict) and item.get("layer") == "architecture"
        }
        disposition_records = disposition.get("records", [])
        disposition_by_path = {
            item.get("path"): item
            for item in disposition_records
            if isinstance(item, dict)
        }
        if set(disposition_by_path) != qualified_architecture:
            errors.append("historical architecture candidate disposition set must exactly match qualified architecture candidates")
        for path in sorted(qualified_architecture):
            item = disposition_by_path.get(path, {})
            if item.get("disposition") != "SUPERSEDED_RETAINED_EVIDENCE":
                errors.append(f"{path}: accepted architecture requires explicit superseded/retained-evidence disposition")
            owners = item.get("replacement_current_owners")
            if not isinstance(owners, list) or not owners:
                errors.append(f"{path}: disposition requires replacement current owner(s)")
        if disposition.get("disposition_state") != "COMPLETE":
            errors.append("historical architecture candidate disposition must be COMPLETE")
    else:
        if whole.get("state") == "ACCEPTED":
            errors.append("whole architecture state ACCEPTED requires accepted=true")
        if state.get("accepted_architecture_established") is not False:
            errors.append("phase state cannot establish architecture before whole acceptance")
        if state.get("implementation_package_count") != 0:
            errors.append("implementation package count must remain zero before whole architecture acceptance")
        if state.get("package_derivation_allowed") is not False:
            errors.append("package derivation must remain false before whole architecture acceptance")
        if state.get("implementation_execution_authorized") is not False:
            errors.append("implementation execution must remain false before whole architecture acceptance")
        if impl_state.get("active_package_count") != 0:
            errors.append("implementation framework must remain empty before architecture acceptance")
        if impl_state.get("package_derivation_allowed") is not False:
            errors.append("implementation framework package derivation must remain false")
        if impl_state.get("implementation_execution_authorized") is not False:
            errors.append("implementation framework execution authority must remain false")

    if state.get("accepted_architecture_established") is not bool(whole_accepted):
        errors.append("phase/whole architecture acceptance state drift")

    counts = control.get("counts", {})
    expected_counts = {
        "decisions_total": len(records),
        "decisions_accepted": accepted_count,
        "q4_repairs_total": len(repairs),
        "q4_repairs_complete": completed_repairs,
        "probes_authorized": len(probes),
        "implementation_packages": state.get("implementation_package_count"),
    }
    for key, value in expected_counts.items():
        if counts.get(key) != value:
            errors.append(f"counts.{key} drift: expected {value}, got {counts.get(key)}")

    for error in errors:
        print("ERROR", error)
    print(
        "Phase-019 architecture decision control: "
        f"{len(errors)} error(s), "
        f"{len(completed)} subphase(s) complete, "
        f"{accepted_count}/10 decision(s) accepted, "
        f"{completed_repairs}/{len(repairs)} Q4 repair(s) complete, "
        f"{len(probes)} probe(s) authorized, "
        f"accepted_architecture={whole_accepted}, "
        f"implementation_packages={state.get('implementation_package_count')}"
    )
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())

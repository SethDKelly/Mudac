#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from pathlib import Path

REGISTER = "docs/routing/downstream_candidate_qualification.json"
OWNER_INVENTORY = "docs/routing/canonical_owner_inventory.json"
STABLE_INDEX = "docs/routing/stable_reference_index.json"
CANDIDATE_ROOTS = (
    "docs/canonical/architecture",
    "docs/canonical/implementation",
)
VALID_Q = {"Q1", "Q2", "Q3", "Q4", "Q5", "Q6"}
VALID_DISPOSITIONS = {
    "QUALIFIED_COMPARISON_INPUT",
    "QUALIFIED_AFTER_REVISION",
    "QUALIFIED_VENDOR_HYPOTHESIS",
    "QUALIFIED_IMPLEMENTATION_HYPOTHESIS",
    "QUALIFIED_VERIFICATION_INPUT",
    "FACT_ONLY",
}
ENG_RE = re.compile(r"^ENG-\d{3}$")
ERI_RE = re.compile(r"^ERI-\d{2}$")


def candidate_paths(repo: Path) -> set[str]:
    result: set[str] = set()
    for root_rel in CANDIDATE_ROOTS:
        root = repo / root_rel
        if not root.is_dir():
            continue
        for path in root.glob("*.md"):
            if path.name == "index.md":
                continue
            result.add(path.relative_to(repo).as_posix())
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", default=".")
    args = parser.parse_args()
    repo = Path(args.repo).resolve()
    errors: list[str] = []

    try:
        register = json.loads((repo / REGISTER).read_text(encoding="utf-8"))
        owners = json.loads((repo / OWNER_INVENTORY).read_text(encoding="utf-8"))
        stable = json.loads((repo / STABLE_INDEX).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print("ERROR", exc)
        return 1

    records = register.get("records")
    if not isinstance(records, list):
        print("ERROR qualification register records must be a list")
        return 1

    expected = candidate_paths(repo)
    actual = {item.get("path") for item in records if isinstance(item, dict)}
    if actual != expected:
        errors.append(
            "qualification register candidate-path set drift: "
            f"missing={sorted(expected - actual)} extra={sorted(actual - expected)}"
        )

    owner_roles = {
        item.get("path"): item.get("role")
        for item in owners.get("records", [])
        if isinstance(item, dict)
    }
    stable_refs = stable.get("references", {})

    q_doc_counts = Counter()
    layer_counts = Counter()
    seen: set[str] = set()

    for item in records:
        if not isinstance(item, dict):
            errors.append("qualification record must be an object")
            continue
        path = item.get("path")
        if not isinstance(path, str):
            errors.append("qualification record missing path")
            continue
        if path in seen:
            errors.append(f"duplicate qualification record: {path}")
        seen.add(path)

        layer = item.get("layer")
        expected_layer = "architecture" if "/architecture/" in path else "implementation"
        if layer != expected_layer:
            errors.append(f"{path}: layer must be {expected_layer}")
        layer_counts[layer] += 1

        q_classes = item.get("q_classes")
        if not isinstance(q_classes, list) or not q_classes:
            errors.append(f"{path}: q_classes must be a non-empty list")
            q_classes = []
        if any(q not in VALID_Q for q in q_classes):
            errors.append(f"{path}: invalid Q classification {q_classes}")
        if len(set(q_classes)) != len(q_classes):
            errors.append(f"{path}: duplicate Q classification")
        for q in set(q_classes):
            q_doc_counts[q] += 1

        if item.get("disposition") not in VALID_DISPOSITIONS:
            errors.append(f"{path}: invalid disposition {item.get('disposition')!r}")
        if item.get("authority_state") != "suspended-candidate":
            errors.append(f"{path}: authority_state must remain suspended-candidate")
        if owner_roles.get(path) != "downstream-candidate":
            errors.append(f"{path}: canonical owner inventory must remain downstream-candidate")

        if "Q4" in q_classes and item.get("requires_semantic_revision") is not True:
            errors.append(f"{path}: Q4 candidate must require semantic revision")
        if "Q5" in q_classes and item.get("preserve_as_executable_fact") is not True:
            errors.append(f"{path}: Q5 candidate must be explicitly preserved as executable fact")
        if item.get("disposition") == "FACT_ONLY" and item.get("eligible_for_018k_comparison") is not False:
            errors.append(f"{path}: FACT_ONLY candidate must not be architecture-comparison eligible")

        eng = item.get("eng")
        if not isinstance(eng, list) or not eng:
            errors.append(f"{path}: ENG obligation references required")
            eng = []
        for ref in eng:
            if not isinstance(ref, str) or not ENG_RE.match(ref):
                errors.append(f"{path}: invalid ENG reference {ref!r}")
                continue
            resolved = stable_refs.get(ref)
            if not isinstance(resolved, dict) or resolved.get("role") != "current-authority":
                errors.append(f"{path}: ENG reference {ref} must resolve as current-authority")

        risks = item.get("risks")
        if not isinstance(risks, list) or not risks:
            errors.append(f"{path}: ERI risk references required")
            risks = []
        for risk in risks:
            if not isinstance(risk, str) or not ERI_RE.match(risk):
                errors.append(f"{path}: invalid ERI risk reference {risk!r}")

        stale = item.get("stale_bindings")
        if not isinstance(stale, list):
            errors.append(f"{path}: stale_bindings must be a list")
        if item.get("requires_semantic_revision") is True and not stale:
            errors.append(f"{path}: semantic revision requires at least one stated stale binding")

        rationale = item.get("rationale")
        if not isinstance(rationale, str) or not rationale.strip():
            errors.append(f"{path}: rationale is required")

    summary = register.get("summary", {})
    if summary.get("total") != len(records):
        errors.append("summary.total drift")
    if summary.get("architecture") != layer_counts["architecture"]:
        errors.append("summary.architecture drift")
    if summary.get("implementation") != layer_counts["implementation"]:
        errors.append("summary.implementation drift")
    if summary.get("adopted") != 0:
        errors.append("qualification register must report zero adopted candidates")
    if summary.get("authority_state") != "suspended-candidate":
        errors.append("qualification summary authority_state must remain suspended-candidate")
    for q in sorted(VALID_Q):
        key = f"{q.lower()}_docs"
        if summary.get(key) != q_doc_counts[q]:
            errors.append(f"summary.{key} drift: expected {q_doc_counts[q]}, got {summary.get(key)}")

    if "DOES NOT ACCEPT OR ACTIVATE" not in str(register.get("authority", "")):
        errors.append("register authority banner must explicitly deny acceptance/activation")

    for error in errors:
        print("ERROR", error)
    print(
        "Downstream candidate qualification: "
        f"{len(errors)} error(s), {len(records)} candidate(s), "
        f"{layer_counts['architecture']} architecture / {layer_counts['implementation']} implementation"
    )
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())

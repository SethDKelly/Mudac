#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

CONFIG = "docs/routing/context_budget.json"
OWNER_INVENTORY = "docs/routing/canonical_owner_inventory.json"


def size(path: Path) -> int:
    return len(path.read_bytes()) if path.is_file() else -1


def add_measurement(measurements: list[tuple[str, int, int]], label: str, path: Path, limit: int) -> None:
    actual = size(path)
    measurements.append((label, actual, limit))


def main() -> int:
    repo = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    try:
        cfg = json.loads((repo / CONFIG).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print("ERROR", exc)
        return 1

    if cfg.get("authority") != "MEASUREMENT/CONFORMANCE POLICY — CANONICAL AGENT CONTEXT CONTRACT RETAINS NORMATIVE MEANING":
        print("ERROR context budget authority boundary drift")
        return 1
    if cfg.get("canonical_contract") != "docs/canonical/governance/agent-context.md":
        print("ERROR context budget canonical contract drift")
        return 1
    if cfg.get("unit") != "utf8_bytes":
        print("ERROR context budget unit must be utf8_bytes")
        return 1

    limits = cfg["hard_limits"]
    measurements: list[tuple[str, int, int]] = []

    add_measurement(measurements, "AGENTS.md", repo / "AGENTS.md", limits["agents_md"])
    add_measurement(measurements, "docs/index.md", repo / "docs/index.md", limits["docs_index"])
    add_measurement(measurements, "docs/canonical/index.md", repo / "docs/canonical/index.md", limits["canonical_index"])

    canonical = repo / "docs" / "canonical"
    for path in sorted(canonical.glob("*/index.md")):
        add_measurement(
            measurements,
            path.relative_to(repo).as_posix(),
            path,
            limits["canonical_family_index_each"],
        )

    knowledge = repo / "knowledge"
    root_index = knowledge / "index.md"
    add_measurement(
        measurements,
        "knowledge/index.md",
        root_index,
        limits["knowledge_root_index"],
    )
    if knowledge.is_dir():
        for path in sorted(knowledge.rglob("*.md")):
            if path == root_index:
                continue
            rel = path.relative_to(repo).as_posix()
            if path.name == "index.md":
                limit = limits["knowledge_nested_index_each"]
            else:
                limit = limits["knowledge_concept_each"]
            add_measurement(measurements, rel, path, limit)

    skills = repo / ".agents" / "skills"
    if skills.is_dir():
        for path in sorted(skills.glob("*/SKILL.md")):
            add_measurement(
                measurements,
                path.relative_to(repo).as_posix(),
                path,
                limits["future_canonical_skill_each"],
            )

    errors: list[str] = []
    for label, actual, limit in measurements:
        if actual < 0:
            print(f"FAIL missing       {label}")
            errors.append(f"required context surface missing: {label}")
            continue
        state = "PASS" if actual <= limit else "FAIL"
        print(f"{state:4} {actual:6}/{limit:6} bytes  {label}")
        if actual > limit:
            errors.append(f"{label} exceeds hard context budget by {actual - limit} bytes")

    print("")
    print("Representative task packs")
    for profile in cfg.get("representative_task_profiles", []):
        total = 0
        missing: list[str] = []
        for raw in profile["files"]:
            path = repo / raw
            actual = size(path)
            if actual < 0:
                missing.append(raw)
            else:
                total += actual
        limit = int(profile["limit"])
        state = "PASS" if not missing and total <= limit else "FAIL"
        print(f"{state:4} {total:6}/{limit:6} bytes  {profile['name']}")
        for raw in missing:
            errors.append(f"task profile {profile['name']} missing file: {raw}")
        if total > limit:
            errors.append(
                f"task profile {profile['name']} exceeds context budget by {total - limit} bytes"
            )

    threshold = int(cfg.get("soft_guidance", {}).get("canonical_owner_review_threshold", 0))
    if threshold > 0:
        try:
            inventory = json.loads((repo / OWNER_INVENTORY).read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            inventory = {"records": []}
        large: list[tuple[str, int]] = []
        for item in inventory.get("records", []):
            if item.get("role") != "current-authority":
                continue
            path = repo / item["path"]
            actual = size(path)
            if actual > threshold:
                large.append((item["path"], actual))
        print("")
        print(f"Informational current-owner review threshold: {threshold} bytes")
        if not large:
            print("INFO no current owner exceeds the review threshold")
        else:
            for path, actual in sorted(large):
                print(f"INFO {actual:6} bytes  {path}")
            print("INFO owner-size guidance is not a failure; use deterministic lookup/decomposition rather than truncating semantic authority")

    for error in errors:
        print("ERROR", error)
    print(f"Context budget validation: {len(errors)} hard error(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())

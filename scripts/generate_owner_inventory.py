#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

POLICY = "docs/routing/canonical_ownership.json"
OUTPUT = "docs/routing/canonical_owner_inventory.json"


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def under(path: str, root: str) -> bool:
    return path == root or path.startswith(root.rstrip("/") + "/")


def classify(path: str, policy: dict) -> str:
    if path in set(policy.get("historical_adapter_paths", [])):
        return "historical-adapter"
    if path in set(policy.get("current_owner_paths", [])):
        return "current-authority"
    if any(under(path, root) for root in policy.get("downstream_candidate_roots", [])):
        return "downstream-candidate"
    if any(under(path, root) for root in policy.get("current_owner_roots", [])):
        return "current-authority"
    if under(path, policy.get("external_reference_root", "__none__")):
        return "external-reference"
    return "unresolved"


def render(repo: Path) -> dict:
    policy = load_json(repo / POLICY)
    roots = [repo / policy["canonical_root"], repo / policy["external_reference_root"]]
    router_names = set(policy.get("router_names", []))
    records: list[dict] = []
    for root in roots:
        if not root.is_dir():
            raise RuntimeError(f"ownership root missing: {root.relative_to(repo)}")
        for path in sorted(root.rglob("*.md")):
            if path.name in router_names:
                continue
            rel = path.relative_to(repo).as_posix()
            role = classify(rel, policy)
            if role == "unresolved":
                raise RuntimeError(f"unresolved ownership role: {rel}")
            records.append({"path": rel, "role": role})
    records.sort(key=lambda item: item["path"])
    by_role: dict[str, int] = {}
    for item in records:
        by_role[item["role"]] = by_role.get(item["role"], 0) + 1
    return {
        "schema_version": "1.0",
        "authority": "DERIVED PATH-ROLE INVENTORY — AUTHORED OWNER FILES RETAIN SEMANTIC AUTHORITY",
        "ownership_policy": POLICY,
        "summary": {
            "total": len(records),
            "by_role": {key: by_role[key] for key in sorted(by_role)},
        },
        "records": records,
    }


def serialized(payload: dict) -> str:
    return json.dumps(payload, indent=2, ensure_ascii=False) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", default=".")
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--write", action="store_true")
    mode.add_argument("--check", action="store_true")
    args = parser.parse_args()
    repo = Path(args.repo).resolve()
    try:
        body = serialized(render(repo))
    except (OSError, ValueError, RuntimeError, json.JSONDecodeError) as exc:
        print("ERROR", exc)
        return 1
    output = repo / OUTPUT
    if args.write:
        output.write_text(body, encoding="utf-8")
        print(f"Wrote {OUTPUT}")
        return 0
    if not output.is_file():
        print(f"ERROR missing generated owner inventory: {OUTPUT}")
        return 1
    if output.read_text(encoding="utf-8") != body:
        print(f"ERROR generated owner inventory drift: {OUTPUT}")
        return 1
    payload = json.loads(body)
    print(f"Owner inventory check: 0 errors, {payload['summary']['total']} governed path(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

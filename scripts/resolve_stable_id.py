#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

INDEX = "docs/routing/stable_reference_index.json"
PHASE_DIR_RE = re.compile(r"^\d{3}-")
TOKEN_RE = re.compile(r"^[A-Z][A-Z0-9]*-\d{3}$")


def history_hits(repo: Path, token: str) -> list[dict]:
    pattern = re.compile(rf"(?<![A-Z0-9-]){re.escape(token)}(?![A-Z0-9-])", re.IGNORECASE)
    results: list[dict] = []
    docs = repo / "docs"
    for phase in sorted(p for p in docs.iterdir() if p.is_dir() and PHASE_DIR_RE.match(p.name)):
        for path in sorted(phase.rglob("*.md")):
            try:
                lines = path.read_text(encoding="utf-8").splitlines()
            except UnicodeDecodeError:
                continue
            for line_no, line in enumerate(lines, 1):
                if pattern.search(line):
                    results.append({
                        "path": path.relative_to(repo).as_posix(),
                        "line": line_no,
                        "text": line.strip(),
                        "role": "numbered-phase-evidence",
                    })
    return results


def main() -> int:
    parser = argparse.ArgumentParser(description="Resolve a MUDAC stable ID to its deterministic authored owner.")
    parser.add_argument("stable_id")
    parser.add_argument("--repo", default=".")
    parser.add_argument("--include-candidates", action="store_true")
    parser.add_argument("--include-deprecated", action="store_true")
    parser.add_argument("--history", action="store_true")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    repo = Path(args.repo).resolve()
    token = args.stable_id.strip().upper()
    if not TOKEN_RE.match(token):
        print(f"ERROR invalid stable ID format: {args.stable_id}", file=sys.stderr)
        return 2

    try:
        index = json.loads((repo / INDEX).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"ERROR cannot load stable-reference index: {exc}", file=sys.stderr)
        return 3

    item = index.get("references", {}).get(token)
    if item is None:
        print(f"ERROR unknown/unregistered stable ID: {token}", file=sys.stderr)
        return 2

    role = item["role"]
    allowed = role == "current-authority"
    if role == "downstream-candidate" and args.include_candidates:
        allowed = True
    if role in {"deprecated-adapter", "historical-adapter"} and args.include_deprecated:
        allowed = True

    if not allowed:
        flag = "--include-candidates" if role == "downstream-candidate" else "--include-deprecated"
        print(
            f"ERROR {token} resolves to non-current role {role}: {item['locator']}; "
            f"use {flag} only when that non-current material is explicitly required",
            file=sys.stderr,
        )
        return 4

    payload = {
        "stable_id": token,
        "role": role,
        "owner_path": item["owner_path"],
        "anchor": item["anchor"],
        "locator": item["locator"],
        "resolution_note": (
            "The locator is derived routing metadata. The authored owner document retains semantic authority. "
            "Candidate/deprecated/history material never becomes current authority through resolver output."
        ),
    }
    if args.history:
        payload["numbered_phase_occurrences"] = history_hits(repo, token)

    if args.json:
        print(json.dumps(payload, indent=2))
    else:
        print(f"{token} -> {item['locator']} [role={role}]")
        if args.history:
            hits = payload.get("numbered_phase_occurrences", [])
            print(f"numbered-phase occurrences: {len(hits)}")
            for hit in hits:
                print(f"{hit['role']} {hit['path']}:{hit['line']}  {hit['text']}")
        print(payload["resolution_note"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

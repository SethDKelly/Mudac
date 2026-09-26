#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


def run(repo: Path, source: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(source / "scripts/validate_phase021_g2_authorization.py"), "--repo", str(repo)],
        cwd=repo,
        text=True,
        capture_output=True,
    )


def mutated_copy(source: Path, parent: Path, name: str) -> Path:
    target = parent / name
    shutil.copytree(source, target, ignore=shutil.ignore_patterns(".git", "node_modules", ".venv", "__pycache__", "*.pyc"))
    return target


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", default=".")
    args = parser.parse_args()
    source = Path(args.repo).resolve()
    errors: list[str] = []

    with tempfile.TemporaryDirectory(prefix="mudac-phase021-g2-") as tmp_raw:
        tmp = Path(tmp_raw)

        scope_repo = mutated_copy(source, tmp, "scope-expansion")
        path = scope_repo / "docs/routing/phase021_g2_authorization.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        data["scope_in"].append("implement Evaluation domain behavior")
        data["authorization"]["next_phase_authorized"] = True
        path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
        if run(scope_repo, source).returncode == 0:
            errors.append("scope expansion / next-phase authorization unexpectedly passed")

        provider_repo = mutated_copy(source, tmp, "review-collapse")
        path = provider_repo / "docs/routing/phase021_g2_authorization.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        data["review"]["reviewer_writable"] = True
        data["review"]["implementer_may_not_self_certify"] = False
        path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
        if run(provider_repo, source).returncode == 0:
            errors.append("review independence collapse unexpectedly passed")

        baseline_repo = mutated_copy(source, tmp, "baseline-drift")
        path = baseline_repo / "docs/routing/phase021_g2_authorization.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        data["authorized_baseline"]["main_sha"] = "0" * 40
        path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
        if run(baseline_repo, source).returncode == 0:
            errors.append("authorized baseline drift unexpectedly passed")

    for error in errors:
        print("ERROR", error)
    print(f"Phase 021 G2 negative controls: {len(errors)} error(s), 3 mutations exercised")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())

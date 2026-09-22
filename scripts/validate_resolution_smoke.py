#!/usr/bin/env python3
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


def run(repo: Path, *args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(repo / "scripts/resolve_stable_id.py"), *args, "--repo", str(repo)],
        cwd=repo,
        text=True,
        capture_output=True,
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", default=".")
    args = parser.parse_args()
    repo = Path(args.repo).resolve()
    errors: list[str] = []

    current = run(repo, "INV-001")
    if current.returncode != 0 or "role=current-authority" not in current.stdout:
        errors.append("INV-001 must resolve as current-authority")

    rejected = run(repo, "ARCH-001")
    if rejected.returncode == 0 or "downstream-candidate" not in rejected.stderr:
        errors.append("ARCH-001 must fail ordinary current resolution as downstream-candidate")

    explicit = run(repo, "ARCH-001", "--include-candidates")
    if explicit.returncode != 0 or "role=downstream-candidate" not in explicit.stdout:
        errors.append("ARCH-001 must resolve only with explicit candidate inclusion")

    for error in errors:
        print("ERROR", error)
    print(f"Stable-resolution behavior: {len(errors)} error(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())

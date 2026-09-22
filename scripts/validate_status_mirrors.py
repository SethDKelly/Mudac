#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
from pathlib import Path

PHASE_INDEX = "docs/018-pre-implementation-repository-qualification-agentic-development-architecture-reentry/index.md"
MIRRORS = (
    "README.md",
    "docs/index.md",
    "docs/README.md",
    "AGENTS.md",
    "docs/canonical/index.md",
    "docs/017-methodology-closure-canonical-consolidation-completion-decision/index.md",
    "docs/canonical/implementation/index.md",
    "docs/018-pre-implementation-repository-qualification-agentic-development-architecture-reentry/README.md",
)
COMPLETE_RE = re.compile(r"^- \[018-([A-M])\b.*?— \*\*COMPLETE\b", re.MULTILINE)
NEXT_RE = re.compile(r"^- (?:\[)?018-([A-M])\b.*?— \*\*NEXT\*\*", re.MULTILINE)
ALL = [chr(code) for code in range(ord("A"), ord("M") + 1)]
CLOSED_TOKEN = "PHASE 018 COMPLETE"
NEXT_LIFECYCLE_TOKEN = "PHASE 019 AUTHORIZED"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", default=".")
    args = parser.parse_args()
    repo = Path(args.repo).resolve()
    errors: list[str] = []

    phase = repo / PHASE_INDEX
    if not phase.is_file():
        print("ERROR missing Phase-018 status authority index")
        return 1

    text = phase.read_text(encoding="utf-8")
    completed = sorted(set(COMPLETE_RE.findall(text)))
    next_items = sorted(set(NEXT_RE.findall(text)))

    closed = False
    next_letter: str | None = None

    if len(next_items) == 1:
        next_letter = next_items[0]
        expected_completed = [chr(code) for code in range(ord("A"), ord(next_letter))]
        if completed != expected_completed:
            errors.append(
                f"Phase-018 completed sequence must be contiguous before {next_letter}; "
                f"expected {expected_completed}, found {completed}"
            )
    elif len(next_items) == 0 and completed == ALL:
        closed = True
    else:
        errors.append(
            "Phase-018 index must either have exactly one NEXT subphase with a contiguous "
            f"completed prefix or be fully closed A-M; next={next_items}, completed={completed}"
        )

    completed_token = f"018-{'/'.join(completed)} COMPLETE" if completed else ""

    for rel in MIRRORS:
        path = repo / rel
        if not path.is_file():
            errors.append(f"missing live status mirror: {rel}")
            continue
        mirror = path.read_text(encoding="utf-8")
        if completed_token and completed_token not in mirror:
            errors.append(f"{rel}: missing current completed-state mirror {completed_token!r}")
        if closed:
            if CLOSED_TOKEN not in mirror:
                errors.append(f"{rel}: missing closed Phase-018 mirror {CLOSED_TOKEN!r}")
            if NEXT_LIFECYCLE_TOKEN not in mirror:
                errors.append(f"{rel}: missing next-lifecycle mirror {NEXT_LIFECYCLE_TOKEN!r}")
        elif next_letter is not None:
            next_token = f"018-{next_letter} NEXT"
            if next_token not in mirror:
                errors.append(f"{rel}: missing current next-state mirror {next_token!r}")

    for error in errors:
        print("ERROR", error)

    if not errors:
        if closed:
            print(
                "Status mirror check: 0 errors; "
                f"{completed_token} / {CLOSED_TOKEN} / {NEXT_LIFECYCLE_TOKEN}"
            )
        else:
            print(f"Status mirror check: 0 errors; {completed_token} / 018-{next_letter} NEXT")
    else:
        print(f"Status mirror check: {len(errors)} error(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())

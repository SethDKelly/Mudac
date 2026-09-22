#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
from pathlib import Path

PHASE018_INDEX = "docs/018-pre-implementation-repository-qualification-agentic-development-architecture-reentry/index.md"
PHASE019_INDEX = "docs/019-architecture-engineering-reentry/index.md"

PHASE018_MIRRORS = (
    "README.md",
    "docs/index.md",
    "docs/README.md",
    "AGENTS.md",
    "docs/canonical/index.md",
    "docs/017-methodology-closure-canonical-consolidation-completion-decision/index.md",
    "docs/canonical/implementation/index.md",
    "docs/018-pre-implementation-repository-qualification-agentic-development-architecture-reentry/README.md",
)
PHASE019_MIRRORS = (
    "README.md",
    "docs/index.md",
    "docs/README.md",
    "AGENTS.md",
    "docs/canonical/index.md",
    "docs/canonical/architecture/index.md",
    "docs/canonical/implementation/index.md",
    "docs/018-pre-implementation-repository-qualification-agentic-development-architecture-reentry/index.md",
    "docs/019-architecture-engineering-reentry/README.md",
)

P18_COMPLETE_RE = re.compile(r"^- \[018-([A-M])\b.*?— \*\*COMPLETE\b", re.MULTILINE)
P18_NEXT_RE = re.compile(r"^- (?:\[)?018-([A-M])\b.*?— \*\*NEXT\*\*", re.MULTILINE)
P18_ALL = [chr(code) for code in range(ord("A"), ord("M") + 1)]

P19_COMPLETE_RE = re.compile(r"^- \[019-([A-L])\b.*?— \*\*COMPLETE\b", re.MULTILINE)
P19_NEXT_RE = re.compile(r"^- (?:\[)?019-([A-L])\b.*?— \*\*NEXT ELIGIBLE\*\*", re.MULTILINE)
P19_ALL = [chr(code) for code in range(ord("A"), ord("L") + 1)]

P18_CLOSED_TOKEN = "PHASE 018 COMPLETE"
P19_AUTH_TOKEN = "PHASE 019 AUTHORIZED"
P19_ACTIVE_TOKEN = "PHASE 019 ACTIVE"


def require_token(repo: Path, mirrors: tuple[str, ...], token: str, errors: list[str]) -> None:
    for rel in mirrors:
        path = repo / rel
        if not path.is_file():
            errors.append(f"missing live status mirror: {rel}")
            continue
        mirror = path.read_text(encoding="utf-8")
        if token not in mirror:
            errors.append(f"{rel}: missing status mirror token {token!r}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", default=".")
    args = parser.parse_args()
    repo = Path(args.repo).resolve()
    errors: list[str] = []

    phase18 = repo / PHASE018_INDEX
    if not phase18.is_file():
        print("ERROR missing Phase-018 status authority index")
        return 1

    text18 = phase18.read_text(encoding="utf-8")
    completed18 = sorted(set(P18_COMPLETE_RE.findall(text18)))
    next18 = sorted(set(P18_NEXT_RE.findall(text18)))

    if completed18 != P18_ALL or next18:
        errors.append(
            "Phase 018 must remain fully closed A-M before/through Phase 019; "
            f"completed={completed18}, next={next18}"
        )

    p18_completed_token = "018-" + "/".join(P18_ALL) + " COMPLETE"
    require_token(repo, PHASE018_MIRRORS, p18_completed_token, errors)
    require_token(repo, PHASE018_MIRRORS, P18_CLOSED_TOKEN, errors)
    require_token(repo, PHASE018_MIRRORS, P19_AUTH_TOKEN, errors)

    phase19 = repo / PHASE019_INDEX
    if phase19.is_file():
        text19 = phase19.read_text(encoding="utf-8")
        completed19 = sorted(set(P19_COMPLETE_RE.findall(text19)))
        next19 = sorted(set(P19_NEXT_RE.findall(text19)))

        closed19 = False
        next_letter: str | None = None
        if len(next19) == 1:
            next_letter = next19[0]
            expected_completed = [chr(code) for code in range(ord("A"), ord(next_letter))]
            if completed19 != expected_completed:
                errors.append(
                    f"Phase-019 completed sequence must be contiguous before {next_letter}; "
                    f"expected {expected_completed}, found {completed19}"
                )
        elif len(next19) == 0 and completed19 == P19_ALL:
            closed19 = True
        else:
            errors.append(
                "Phase-019 index must have exactly one NEXT ELIGIBLE subphase with a contiguous "
                f"completed prefix, or be fully closed A-L; next={next19}, completed={completed19}"
            )

        p19_completed_token = "019-" + "/".join(completed19) + " COMPLETE" if completed19 else ""
        if p19_completed_token:
            require_token(repo, PHASE019_MIRRORS, p19_completed_token, errors)

        if closed19:
            require_token(repo, PHASE019_MIRRORS, "PHASE 019 COMPLETE", errors)
        elif next_letter is not None:
            require_token(repo, PHASE019_MIRRORS, P19_ACTIVE_TOKEN, errors)
            require_token(repo, PHASE019_MIRRORS, f"019-{next_letter} NEXT ELIGIBLE", errors)

    for error in errors:
        print("ERROR", error)

    if not errors:
        if phase19.is_file():
            if 'closed19' in locals() and closed19:
                print(
                    "Status mirror check: 0 errors; "
                    f"{p18_completed_token} / {P18_CLOSED_TOKEN} / "
                    f"019-{'/'.join(P19_ALL)} COMPLETE / PHASE 019 COMPLETE"
                )
            else:
                print(
                    "Status mirror check: 0 errors; "
                    f"{p18_completed_token} / {P18_CLOSED_TOKEN} / "
                    f"{p19_completed_token} / {P19_ACTIVE_TOKEN} / 019-{next_letter} NEXT ELIGIBLE"
                )
        else:
            print(
                "Status mirror check: 0 errors; "
                f"{p18_completed_token} / {P18_CLOSED_TOKEN} / {P19_AUTH_TOKEN}"
            )
    else:
        print(f"Status mirror check: {len(errors)} error(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())

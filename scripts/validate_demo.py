#!/usr/bin/env python3
"""Validate the LifeOS Claude Build System proof repo.

This script checks that the public proof repo is complete and does not contain
obvious secret-like assignments.
"""

from __future__ import annotations

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "README.md",
    "demo.html",
    "agents/advisor.md",
    "agents/builder.md",
    "agents/reviewer.md",
    "agents/deploy-ops.md",
    "lifeos/product-brief.md",
    "lifeos/user-roles.md",
    "lifeos/mvp-roadmap.md",
    "lifeos/feature-map.md",
    "lifeos/epaper-display-plan.md",
    "workflows/idea-to-spec.md",
    "workflows/spec-to-build-tasks.md",
    "workflows/review-gate.md",
    "workflows/deploy-readiness.md",
    "mcp/tool-registry.md",
    "mcp/future-mcp-server-plan.md",
]

REQUIRED_DEMO_TEXT = [
    "LifeOS Claude Build System",
    "Advisor",
    "Builder",
    "Reviewer",
    "Deploy/Ops",
    "MCP",
    "e-paper",
]

SECRET_PATTERNS = [
    re.compile(r"\bAPI_KEY\s*=", re.IGNORECASE),
    re.compile(r"\bSECRET\s*=", re.IGNORECASE),
    re.compile(r"\bTOKEN\s*=", re.IGNORECASE),
    re.compile(r"private_key\s*=", re.IGNORECASE),
]


def main() -> int:
    failures: list[str] = []

    for rel in REQUIRED_FILES:
        path = ROOT / rel
        if not path.exists():
            failures.append(f"missing required file: {rel}")

    demo_path = ROOT / "demo.html"
    if demo_path.exists():
        demo = demo_path.read_text(encoding="utf-8")
        for text in REQUIRED_DEMO_TEXT:
            if text not in demo:
                failures.append(f"demo.html missing required text: {text}")

    for path in ROOT.rglob("*"):
        if path.is_file() and ".git" not in path.parts:
            try:
                content = path.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                continue
            for pattern in SECRET_PATTERNS:
                if pattern.search(content):
                    failures.append(f"secret-like assignment found in {path.relative_to(ROOT)}: {pattern.pattern}")

    if failures:
        print("FAIL: LifeOS Claude Build System proof repo has issues.")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("PASS: LifeOS Claude Build System proof repo is complete.")
    print(f"Checked {len(REQUIRED_FILES)} required files.")
    print("No obvious secret-like assignments found.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

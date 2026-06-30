#!/usr/bin/env python3
"""Live Claude API pipeline demo for LifeOS.

This script makes real sequential Claude API calls:

Watcher -> Advisor -> Builder

It is intentionally small and safe for demos:
- reads the local repo structure for real
- does not write code into the app
- writes markdown outputs into runs/live-*/
- requires ANTHROPIC_API_KEY in the environment
- requires the anthropic Python package

Do not commit API keys. Do not paste secrets into prompts.
"""

from __future__ import annotations

import argparse
import os
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable

try:
    import anthropic
except ImportError:  # pragma: no cover - demo helper
    print("ERROR: Missing dependency: anthropic")
    print("Run inside a virtualenv:")
    print("  python3 -m venv .venv")
    print("  source .venv/bin/activate")
    print("  pip install anthropic")
    sys.exit(2)

ROOT = Path(__file__).resolve().parents[1]
RUNS_DIR = ROOT / "runs"
DEFAULT_MODEL = os.getenv("CLAUDE_MODEL", "claude-sonnet-4-6")
SKIP_DIRS = {".git", ".venv", "__pycache__", "node_modules", "runs"}
MAX_FILES = 120
MAX_SNIPPET_CHARS = 9000


def iter_repo_files(repo_path: Path) -> Iterable[Path]:
    for path in sorted(repo_path.rglob("*")):
        if not path.is_file():
            continue
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        if path.suffix.lower() not in {".md", ".py", ".html", ".txt"}:
            continue
        yield path


def scan_repo(repo_path: Path) -> str:
    files = []
    snippets = []
    for idx, path in enumerate(iter_repo_files(repo_path)):
        if idx >= MAX_FILES:
            break
        rel = path.relative_to(repo_path)
        files.append(str(rel))
        if rel.as_posix() in {
            "README.md",
            "AGENTS.md",
            "CLAUDE.md",
            "agents/watcher.md",
            "agents/advisor.md",
            "agents/builder.md",
            "lifeos/product-brief.md",
            "workflows/lifeos-pipeline.md",
        }:
            try:
                text = path.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                continue
            snippets.append(f"--- {rel} ---\n{text[:1400]}")

    repo_context = "# Repo file listing\n" + "\n".join(files)
    if snippets:
        repo_context += "\n\n# Selected file snippets\n" + "\n\n".join(snippets)
    return repo_context[:MAX_SNIPPET_CHARS]


def call_claude(client: anthropic.Anthropic, system: str, user: str, model: str) -> str:
    response = client.messages.create(
        model=model,
        max_tokens=1600,
        system=system,
        messages=[{"role": "user", "content": user}],
    )
    return response.content[0].text


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Run a live Claude Advisor -> Builder repo pipeline.")
    parser.add_argument("idea", nargs="?", default="LifeOS household task/calendar app with e-paper display")
    parser.add_argument("repo_path", nargs="?", default=str(ROOT))
    parser.add_argument("--model", default=DEFAULT_MODEL)
    args = parser.parse_args()

    if not os.getenv("ANTHROPIC_API_KEY"):
        print("ERROR: ANTHROPIC_API_KEY is not set in this shell.")
        print("Set it locally before running. Do not paste or commit it.")
        return 2

    repo_path = Path(args.repo_path).expanduser().resolve()
    if not repo_path.exists():
        print(f"ERROR: repo path does not exist: {repo_path}")
        return 2

    run_id = datetime.now(timezone.utc).strftime("live-%Y%m%d-%H%M%S")
    out_dir = RUNS_DIR / run_id
    out_dir.mkdir(parents=True, exist_ok=True)

    print("LifeOS Live Claude Pipeline")
    print("=" * 60)
    print(f"Model: {args.model}")
    print(f"Idea: {args.idea}")
    print(f"Repo: {repo_path}")
    print(f"Output: {out_dir.relative_to(ROOT)}")
    print()

    print("=== WATCHER: scanning repo for real files ===")
    repo_context = scan_repo(repo_path)
    write(out_dir / "00-watcher-repo-context.md", repo_context)
    print(repo_context[:900] + ("..." if len(repo_context) > 900 else ""))
    print()

    client = anthropic.Anthropic()

    print("=== ADVISOR: product reasoning over idea + repo ===")
    advisor = call_claude(
        client=client,
        model=args.model,
        system=(
            "You are the Advisor in a Claude Build System. Given a client app idea and the existing repo context, "
            "produce a concise product direction. Output markdown with: product summary, core decisions, user roles, "
            "3-5 MVP features, open questions, and recommended next decision. Be practical and founder-friendly. "
            "Do not claim the app is already built."
        ),
        user=f"Client idea:\n{args.idea}\n\nRepo context:\n{repo_context}",
    )
    write(out_dir / "01-advisor.md", advisor)
    print(advisor[:1200] + ("..." if len(advisor) > 1200 else ""))
    print()

    print("=== BUILDER: turning Advisor output into build structure ===")
    builder = call_claude(
        client=client,
        model=args.model,
        system=(
            "You are the Builder in a Claude Build System. Given an Advisor plan and repo context, output markdown with: "
            "recommended repo/project structure, first 5 implementation tasks, acceptance tests, and tech stack recommendation "
            "with reasoning. Keep it realistic for a first milestone. Do not overbuild."
        ),
        user=f"Advisor plan:\n{advisor}\n\nRepo context:\n{repo_context}",
    )
    write(out_dir / "02-builder.md", builder)
    print(builder[:1200] + ("..." if len(builder) > 1200 else ""))
    print()

    handoff = f"""# Live Claude Pipeline Handoff

## Idea

{args.idea}

## What ran

- Watcher scanned the local repo files for real.
- Advisor used the idea + repo context to produce product direction.
- Builder used the Advisor output + repo context to produce build structure and implementation tasks.

## Outputs

- `00-watcher-repo-context.md`
- `01-advisor.md`
- `02-builder.md`

## Honest demo boundary

This is a real sequential Claude API pipeline, but it is intentionally small and safe. It is not a production autonomous agent platform and it does not deploy anything.

## Recommended next step

Turn this proof into the client's actual LifeOS Claude project foundation, then decide which steps should become MCP tools or automated workflows.
"""
    write(out_dir / "README.md", handoff)

    print("PASS: live Claude pipeline completed")
    print(f"Saved outputs to: {out_dir.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

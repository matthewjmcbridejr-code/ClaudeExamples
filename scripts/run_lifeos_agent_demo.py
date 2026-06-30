#!/usr/bin/env python3
"""Run a sanitized LifeOS multi-role Claude workflow demo.

This is intentionally local and deterministic: it demonstrates the operating
model without requiring API keys, private projects, or live autonomous agents.
"""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
from pathlib import Path
import textwrap

ROOT = Path(__file__).resolve().parents[1]
RUNS_DIR = ROOT / "runs"

DEFAULT_IDEA = (
    "Create a LifeOS family management app where household members can assign "
    "tasks, view a shared calendar, book shared assets, manage permissions, "
    "and eventually display today's tasks and calendar on an e-paper screen."
)


def clean_block(text: str) -> str:
    return textwrap.dedent(text).strip() + "\n"


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(clean_block(content), encoding="utf-8")


def advisor_output(idea: str) -> str:
    return f"""
    # Advisor Output — LifeOS Product Direction

    ## Input idea

    {idea}

    ## Product summary

    LifeOS should start as a practical household operating system for managing
    tasks, calendar visibility, shared assets, permissions, and a display-ready
    home dashboard.

    ## Recommended MVP direction

    Start with the family task + calendar foundation before building complex
    automation. The first useful version should answer three questions:

    1. What needs to happen today?
    2. Who owns each task?
    3. What information is safe to show on the shared home display?

    ## Initial user roles

    - Household Owner/Admin: controls setup, members, permissions, and display rules.
    - Adult Member: creates/updates tasks and books approved shared assets.
    - Child/Dependent: sees assigned tasks and approved display-safe items.
    - Guest/Helper: sees only tasks or schedule items assigned to them.

    ## MVP features

    - household member setup
    - create and assign tasks
    - recurring task support
    - shared calendar summary
    - display-safe daily dashboard
    - basic permissions

    ## Open questions

    - Which calendar source should be used first?
    - Should task completion require admin approval for children/helpers?
    - Which shared assets matter first: rooms, vehicles, equipment, or services?
    - What exact e-paper hardware is preferred?

    ## Next decision needed

    Approve Phase 1 scope: household members, tasks, simple calendar summary,
    and display-safe daily view.
    """


def builder_output() -> str:
    return """
    # Builder Output — Buildable Project Plan

    ## Proposed repo structure

    ```text
    lifeos-app/
    ├── docs/
    │   ├── product-brief.md
    │   ├── mvp-roadmap.md
    │   └── display-rules.md
    ├── app/
    │   ├── dashboard/
    │   ├── tasks/
    │   ├── calendar/
    │   └── assets/
    ├── api/
    │   ├── tasks/
    │   ├── members/
    │   ├── calendar/
    │   └── display/
    └── tests/
        ├── task-permissions.test.md
        ├── calendar-display.test.md
        └── shared-assets.test.md
    ```

    ## Phase 1 implementation tasks

    1. Create household/member data model.
    2. Create task data model with owner, assignee, due date, recurrence, and status.
    3. Create task list and daily dashboard views.
    4. Create calendar summary model.
    5. Create display-safe endpoint: `GET /api/display/today`.
    6. Add permission rules for owner/admin, adult member, child, and helper.

    ## Initial data model

    - Household
    - Member
    - Task
    - TaskAssignment
    - CalendarItem
    - SharedAsset
    - AssetBooking
    - DisplayRule

    ## Acceptance criteria

    - Admin can assign a task to any household member.
    - Adult member can complete their assigned tasks.
    - Child/dependent cannot edit household settings.
    - Private calendar details do not appear in the e-paper display payload.
    - Display endpoint returns only approved daily summary data.
    """


def reviewer_output() -> str:
    return """
    # Reviewer Output — Quality Gate

    ## What is good

    - The MVP is focused on tasks, calendar, and display-safe summaries.
    - User roles are defined before implementation.
    - E-paper display privacy is treated as a first-class requirement.
    - The build plan avoids overbuilding autonomous agents too early.

    ## What is risky

    - Calendar integration can expand scope quickly.
    - Shared asset bookings need conflict rules before implementation.
    - Child/helper permissions must be tested carefully.
    - E-paper hardware choice can affect display payload and refresh cadence.

    ## Required fixes before build

    1. Define exact Phase 1 calendar source.
    2. Define whether children can mark tasks complete without approval.
    3. Define what private data must never appear on shared display.
    4. Define first shared asset category or defer assets to Phase 2.

    ## Suggested tests

    - Admin assignment test
    - Child permission restriction test
    - Private calendar exclusion test
    - Display endpoint safe-payload test
    - Recurring task generation test

    ## Approval status

    Revise before implementation. Product direction is strong, but Phase 1
    permissions and display privacy rules should be confirmed first.
    """


def ops_output() -> str:
    return """
    # Deploy/Ops Output — Readiness Plan

    ## Environment requirements

    - application runtime
    - database connection
    - authentication provider decision
    - calendar integration credentials, later
    - e-paper display endpoint configuration, later

    ## Demo deployment checklist

    - confirm no secrets are committed
    - run validation script
    - create sample household data
    - verify task dashboard flow
    - verify display-safe daily payload
    - document known limitations

    ## Release notes template

    ```text
    Release: LifeOS Phase 1 Preview
    Includes: household roles, task assignment plan, calendar summary plan,
    display-safe endpoint plan, review/deployment checklist.
    Known limitations: no production auth, no live calendar integration, no hardware display integration yet.
    ```

    ## Rollback plan

    Keep each milestone in a separate branch or tagged release. If a demo breaks,
    revert to the last known-good docs/build state and preserve the review notes.

    ## Maintenance guide direction

    After every major feature, update:

    - product brief
    - feature map
    - acceptance tests
    - deployment checklist
    - decision log
    """


def summary_output(run_name: str) -> str:
    return f"""
    # LifeOS Agent Workflow Run Summary

    ## Run

    `{run_name}`

    ## Pipeline

    Idea → Advisor → Builder → Reviewer → Deploy/Ops → Handoff

    ## Files produced

    - `01-advisor-output.md`
    - `02-builder-output.md`
    - `03-reviewer-output.md`
    - `04-deploy-ops-output.md`
    - `handoff.md`

    ## What this demo proves

    - The workflow can separate product thinking from build planning.
    - Claude roles can be saved as reusable project instructions.
    - Work can pass through review gates before implementation.
    - The system can create a clean handoff trail in a repo.

    ## What this demo does not claim

    - It does not claim the LifeOS app is built.
    - It does not use real private credentials.
    - It does not run uncontrolled autonomous agents.
    - It is a safe proof of workflow structure.
    """


def handoff_output() -> str:
    return """
    # Handoff — Proposed First Client Milestone

    ## Milestone goal

    Build Abdulmohsen's first working Claude project foundation around the
    LifeOS / family management idea.

    ## Deliverables

    - Claude workspace/project structure
    - Advisor / Builder / Reviewer / Deploy-Ops role prompts
    - LifeOS product brief
    - MVP roadmap
    - feature breakdown
    - repo/docs structure
    - MCP/tooling plan
    - review gate workflow
    - deploy readiness workflow
    - walkthrough/training session

    ## Recommended build sequence

    1. Confirm LifeOS Phase 1 scope.
    2. Create the project workspace and docs foundation.
    3. Add reusable Claude role instructions.
    4. Add workflow files for idea-to-spec, spec-to-build, review, and deploy readiness.
    5. Add a staged MCP/tooling plan.
    6. Walk the client through how to keep using the system.

    ## Close position

    Start simple, make the setup useful immediately, then expand into more
    advanced MCP/tools and advisor/build/deploy automation after the foundation
    is working.
    """


def main() -> int:
    parser = argparse.ArgumentParser(description="Run a sanitized LifeOS agent workflow demo.")
    parser.add_argument("--idea", default=DEFAULT_IDEA, help="LifeOS idea or feature request to process")
    args = parser.parse_args()

    run_name = datetime.now(timezone.utc).strftime("lifeos-run-%Y%m%d-%H%M%S")
    run_dir = RUNS_DIR / run_name

    stages = [
        ("Advisor", "01-advisor-output.md", advisor_output(args.idea)),
        ("Builder", "02-builder-output.md", builder_output()),
        ("Reviewer", "03-reviewer-output.md", reviewer_output()),
        ("Deploy/Ops", "04-deploy-ops-output.md", ops_output()),
        ("Handoff", "handoff.md", handoff_output()),
        ("Summary", "README.md", summary_output(run_name)),
    ]

    print("LifeOS Claude Build System — Agent Pipeline Demo")
    print("=" * 60)
    print(f"Idea: {args.idea}")
    print(f"Run directory: {run_dir.relative_to(ROOT)}")
    print()

    for stage, filename, content in stages:
        print(f"[{stage}] producing {filename}")
        write(run_dir / filename, content)

    print()
    print("PASS: demo workflow completed")
    print(f"Open: {run_dir.relative_to(ROOT)}/README.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

# LifeOS Claude Build System — Proof of Concept

A sanitized proof-of-concept for structuring Claude around Abdulmohsen's LifeOS / family management app idea.

This repo demonstrates a practical Claude operating model for turning app ideas into organized software projects:

- **Advisor** role for product thinking, specs, research, and decisions
- **Builder** role for repo structure, implementation planning, code prompts, and tasks
- **Reviewer** role for quality gates, missing requirements, assumptions, and test review
- **Deploy/Ops** role for deployment checklist, release workflow, maintenance, and rollback planning
- **Shared project layer** for docs, context, repository workflow, MCP/tooling direction, and human review gates

## What this is

This is a proof of structure and workflow.

It shows how a Claude-based build system can be organized around a real app idea instead of staying as a generic chat window.

## What this is not

This is **not** the finished LifeOS application.

It does **not** include real credentials, private server data, production deployment access, or a full autonomous agent platform.

## LifeOS idea this is built around

The example app scope includes:

- household members
- family task assignment
- shared calendar
- shared assets and bookings
- permissions
- mobile app direction
- e-paper display for home tasks and calendar

## View the demo

Open `demo.html` in a browser.

## Validate the proof repo

Run:

```bash
python3 scripts/validate_demo.py
```

Expected result:

```text
PASS: LifeOS Claude Build System proof repo is complete.
```

## First milestone this represents

The first working foundation would include:

- Claude workspace/project structure
- Advisor / Builder / Reviewer / Deploy-Ops role prompts
- LifeOS product brief
- MVP roadmap
- feature map
- repo/docs workflow
- review gate
- deployment readiness workflow
- MCP/tooling direction
- training walkthrough / maintenance guide

## Expansion path

The practical order is:

1. Prompt and documentation foundation
2. LifeOS-specific project structure
3. Reusable Claude roles and workflows
4. Local scripts and tool registry
5. MCP server for controlled tool access
6. LifeOS-specific tools for tasks, calendar, shared assets, and e-paper display
7. Deployment, monitoring, and maintenance helpers

Start simple, make it useful immediately, then scale into deeper agents and tools.

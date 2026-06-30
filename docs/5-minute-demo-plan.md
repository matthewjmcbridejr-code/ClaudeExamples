# 5-Minute Client Demo Plan

## Goal

Show Abdulmohsen a concrete workflow, not a slide deck.

The point of the demo is to prove that the LifeOS idea can move through a structured Claude operating model:

Idea → Advisor → Builder → Reviewer → Deploy/Ops → Handoff

## Demo setup

Before the call, clone the repo locally:

```bash
git clone https://github.com/matthewjmcbridejr-code/ClaudeExamples.git
cd ClaudeExamples
```

Optional validation:

```bash
python3 scripts/validate_demo.py
```

Run the agent pipeline demo:

```bash
python3 scripts/run_lifeos_agent_demo.py --idea "Create a LifeOS app where my household can assign tasks, see a shared calendar, book shared assets, manage permissions, and show today's plan on an e-paper screen."
```

Then show the generated folder under:

```text
runs/lifeos-run-*/
```

## What to screen share

### 1. Open the GitHub repo

Say:

> I made this public and sanitized so you can inspect it without me exposing private projects or credentials.

Show:

- README.md
- demo.html
- agents folder
- lifeos folder
- workflows folder
- mcp folder

### 2. Run the pipeline command

Say:

> This is not pretending the app is finished. It shows the operating model: the idea moves through different Claude roles, and each stage creates a real handoff artifact.

Run:

```bash
python3 scripts/run_lifeos_agent_demo.py --idea "Create a LifeOS app where my household can assign tasks, see a shared calendar, book shared assets, manage permissions, and show today's plan on an e-paper screen."
```

### 3. Open generated outputs

Show:

- `01-advisor-output.md`
- `02-builder-output.md`
- `03-reviewer-output.md`
- `04-deploy-ops-output.md`
- `handoff.md`

### 4. Explain the workflow in plain English

Say:

> Advisor clarifies the product. Builder turns approved direction into repo structure and implementation tasks. Reviewer catches missing requirements, privacy risks, and overbuilding. Deploy/Ops prepares the project for QA, release, rollback, and maintenance. The important part is that the work leaves an organized trail in the repo instead of disappearing into chat history.

### 5. Close

Say:

> For your first milestone, I would turn this proof into your actual working Claude/project foundation: project workspace, role prompts, LifeOS docs, repo workflow, review gates, MCP/tooling direction, and a walkthrough so you know how to keep using it.

## If he asks whether this is real automation

Say:

> This demo is intentionally safe and local. It simulates the role pipeline without requiring private keys or exposing client work. The first milestone would wire the same structure into your actual Claude workflow. After that, we can decide which parts should become real MCP tools or automated agent steps.

## If he asks why not build the app immediately

Say:

> We can absolutely build toward the app, but the foundation matters first. If the Claude workflow is structured correctly, every future app idea becomes easier to plan, build, review, and maintain. LifeOS is the first real example we use to make the setup useful immediately.

## Demo timing

- 60 seconds: repo overview
- 90 seconds: run pipeline command
- 90 seconds: show generated Advisor/Builder/Reviewer/Deploy outputs
- 60 seconds: explain first milestone and close

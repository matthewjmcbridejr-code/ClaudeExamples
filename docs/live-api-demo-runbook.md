# Live Claude API Demo Runbook

Use this only if it has been tested once before the client call.

If it fails, fall back to:

```bash
python3 scripts/run_lifeos_agent_demo.py --idea "Create a LifeOS app where my household can assign tasks, see a shared calendar, book shared assets, manage permissions, and show today's plan on an e-paper screen."
```

## What the live script does

`scripts/live_claude_pipeline.py` makes real sequential Claude API calls:

1. Watcher scans the local repo files for real.
2. Advisor reasons over the client idea + repo context.
3. Builder turns the Advisor output into a build structure and first tasks.
4. Outputs are saved into `runs/live-*`.

This is real chained model reasoning, but it is intentionally small and safe.

## What it does not do

- It does not deploy anything.
- It does not run a background daemon.
- It does not pretend the LifeOS app is already built.
- It does not expose credentials.
- It does not run uncontrolled autonomous agents.

## Safe setup

Do not use `--break-system-packages`.

Use a virtualenv:

```bash
git clone https://github.com/matthewjmcbridejr-code/ClaudeExamples.git
cd ClaudeExamples

python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install anthropic
```

Set the API key only in your local shell. Do not paste it into the call or commit it.

```bash
export ANTHROPIC_API_KEY="paste-your-key-only-in-your-local-terminal"
```

Optional model override if needed:

```bash
export CLAUDE_MODEL="claude-sonnet-4-6"
```

## Test command

```bash
python3 scripts/live_claude_pipeline.py "Create a LifeOS app where my household can assign tasks, see a shared calendar, book shared assets, manage permissions, and show today's plan on an e-paper screen."
```

## Show outputs

```bash
LATEST=$(ls -td runs/live-* | head -1)
ls "$LATEST"
cat "$LATEST/README.md"
cat "$LATEST/01-advisor.md"
cat "$LATEST/02-builder.md"
```

## What to say on the call

> This is the live version of the same idea. The Watcher scans the repo, the Advisor reasons over the project, and the Builder turns the plan into build tasks. I am keeping it intentionally small so it is safe and understandable. The first paid milestone would turn this into your actual LifeOS Claude workflow, then we decide which steps should become MCP tools or deeper automation.

## Fallback line if live API fails

> I do not want to debug API credentials on your time. I have the deterministic version of the same workflow ready, so I will show the structure safely and keep the live API wiring for the actual setup.

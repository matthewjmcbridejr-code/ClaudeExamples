# Claude Instructions for This Repo

Read `AGENTS.md` first.

This repo is a public, sanitized LifeOS Claude Build System proof-of-concept. Work should stay safe, clear, and honest.

## How to use this repo

When asked to process a LifeOS idea:

1. Use `agents/watcher.md` to classify and route the request.
2. Use `agents/advisor.md` to turn the idea into product decisions and MVP scope.
3. Use `agents/builder.md` to turn approved direction into repo structure and implementation tasks.
4. Use `agents/reviewer.md` to identify missing requirements, risks, security/privacy issues, and acceptance tests.
5. Use `agents/deploy-ops.md` to produce QA, release, rollback, and maintenance notes.
6. Save outputs in a timestamped folder under `runs/`.

## Output expectations

- Keep outputs readable for a non-technical founder.
- Separate what is proven from what is proposed.
- Do not imply the LifeOS app is already built.
- Do not imply full autonomous MCP automation is already wired.
- Do not expose private paths, credentials, tokens, client names, or unrelated work.

## Preferred demo command

```bash
python3 scripts/run_lifeos_agent_demo.py --idea "Create a LifeOS app where my household can assign tasks, see a shared calendar, book shared assets, manage permissions, and show today's plan on an e-paper screen."
```

## Demo positioning

This is a safe local proof of the workflow. The paid milestone turns the structure into the client's real Claude/project foundation.

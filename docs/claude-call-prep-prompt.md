# Claude Call Prep Prompt

Use this prompt in Claude before the client call.

```text
I have a client call in about 30 minutes with an Upwork prospect named Abdulmohsen Abdulrahman.

Context:
He wants help setting up Claude for building apps, prototypes, wireframes, documentation, and presentations. He only has the Claude app installed and tried it in the IDE. He is not using GitHub yet but is open to a code repository. He wants a clean setup from scratch.

His app ideas include:
- LifeOS app for assigning tasks to house members
- displaying calendar/tasks on an e-paper screen at home
- mobile app for family shared assets and bookings
- family management app
- agent that takes a business form and returns a full informative website

He showed me another freelancer's pitch about running three Claude setups: one always-on consultant with memory/research, one dev instance that builds/ships projects, and one server deployment instance, all using Claude Code + MCP.

My positioning:
I want to show that I understand and can build this kind of workflow, but I do not want to fake a polished private product demo. I created a sanitized public proof repo around his LifeOS idea:

https://github.com/matthewjmcbridejr-code/ClaudeExamples

The repo includes:
- demo.html visual walkthrough
- agents/watcher.md
- agents/advisor.md
- agents/builder.md
- agents/reviewer.md
- agents/deploy-ops.md
- LifeOS product docs
- workflows for idea-to-spec, spec-to-build-tasks, review-gate, deploy-readiness
- MCP/tooling plan
- scripts/run_lifeos_agent_demo.py, which simulates a safe local agent pipeline and writes markdown outputs

My goal on the call:
Win the job. Keep the demo to about 5 minutes. Do not overexplain. Do not show private projects, secrets, server paths, or messy internal tools. Show a practical workflow he can understand.

Demo plan:
1. Open the public GitHub repo.
2. Explain that it is sanitized and customized around his LifeOS idea.
3. Run this command locally:
python3 scripts/run_lifeos_agent_demo.py --idea "Create a LifeOS app where my household can assign tasks, see a shared calendar, book shared assets, manage permissions, and show today's plan on an e-paper screen."
4. Open the generated runs/lifeos-run-* folder.
5. Show the outputs:
   - 01-advisor-output.md
   - 02-builder-output.md
   - 03-reviewer-output.md
   - 04-deploy-ops-output.md
   - handoff.md
6. Explain that this is a safe proof of workflow, not a fake finished app.
7. Close by saying the first milestone is to turn this into his actual working Claude/project foundation.

Give me:
- a tight 5-minute call script
- exactly what to click/show in order
- what to say if he asks whether this is real automation
- what to say if he asks why not build the app immediately
- what to say if he compares me to the other freelancer
- a confident closing line that asks him to activate the contract

Constraints:
- Keep the advice practical and concise.
- Avoid hype.
- Do not tell me to claim something untrue.
- Make me sound technical, calm, and focused on getting his first useful setup built.
```

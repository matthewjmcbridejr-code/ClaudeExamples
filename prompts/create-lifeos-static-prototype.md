# Reusable Build Request — LifeOS Static Prototype

Use this prompt inside Claude Code when you want Builder to create a tiny static prototype from the LifeOS project foundation.

This exists so the client does **not** need to invent a perfect prompt from scratch. The workflow gives them a reusable request they can run, edit, and repeat.

```text
Read AGENTS.md and CLAUDE.md.

Use the role workflow in this repo.

Task:
Using the LifeOS idea, create a tiny static prototype in a new folder called prototype/lifeos-static.

The prototype should include:
- index.html
- styles.css
- app.js
- README.md

It should show:
- household members
- today's tasks
- shared calendar items
- shared asset bookings
- e-paper display preview

Keep it simple. No external dependencies. No API keys. No package install. No private data.

After creating the files, run a simple validation command to confirm the files exist.

Do not delete or modify existing files unless necessary.
```

## Demo positioning

Say:

> This is the reusable Builder request. The client does not need to know how to write the perfect prompt. The setup includes repeatable project commands like this, and Claude Code can use them to create or update files in the repo.

## Safe boundary

This prompt creates a small static prototype only. It does not deploy, connect accounts, use credentials, or claim to be the finished app.

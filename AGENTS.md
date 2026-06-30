# Agent Operating Manual

This repository is a sanitized proof-of-concept for a Claude Build System around the LifeOS family management app idea.

## What agents mean here

The files in `agents/` are reusable role instructions. They are not presented as magic autonomous workers. They define how Claude should behave at each stage of a project workflow.

## Core workflow

Idea → Watcher → Advisor → Builder → Reviewer → Deploy/Ops → Handoff

## Rules

- Start with Advisor before Builder when an idea is not yet specified.
- Builder should work from approved product direction, not invent unapproved features.
- Reviewer should check assumptions, missing requirements, privacy risk, acceptance criteria, and overbuilding.
- Deploy/Ops should prepare QA, deployment notes, rollback, and maintenance guidance.
- Save outputs as markdown handoff artifacts so decisions do not disappear into chat history.
- Do not expose secrets, tokens, credentials, private server paths, or private client data.
- Do not suggest destructive actions without a clear warning and human approval.
- Keep the system useful before adding heavy automation or MCP complexity.

## Demo boundary

This repo demonstrates the operating model. It does not claim the LifeOS app is finished or that a production autonomous agent platform is already running.

# Workflow: Deploy Readiness

## When to use

Use this before any demo, preview deployment, client handoff, or production release.

## Input needed

- app milestone
- hosting target
- environment requirements
- test results
- rollback plan
- known limitations

## Steps

1. Deploy/Ops lists environment requirements.
2. Deploy/Ops creates a QA checklist.
3. Reviewer checks the release for missing tests and security gaps.
4. Builder fixes blockers.
5. Deploy/Ops prepares release notes and rollback plan.

## Output format

- deployment checklist
- environment variables needed
- QA checklist
- release notes
- rollback plan
- known limitations

## LifeOS example

Before deploying a LifeOS preview, confirm:

- task assignment works
- household roles are enforced
- e-paper display endpoint does not leak private data
- database backup or rollback path exists
- known limitations are documented

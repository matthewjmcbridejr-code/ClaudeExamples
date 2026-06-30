# Workflow: Spec to Build Tasks

## When to use

Use this after the Advisor has created a clear feature spec and the client has approved the direction.

## Input needed

- approved feature spec
- target platform
- constraints
- desired milestone
- any required integrations

## Steps

1. Builder converts the spec into implementation tasks.
2. Builder proposes files, folders, data models, and API routes.
3. Builder adds acceptance criteria.
4. Reviewer checks for missing requirements or overbuilding.
5. Builder revises before implementation starts.

## Output format

- implementation summary
- file/folder plan
- frontend tasks
- backend tasks
- data model changes
- API route list
- acceptance tests
- risks

## LifeOS example

For household tasks, Builder should produce tasks like:

- create task model
- create assignment model
- create task list screen
- create task detail screen
- add complete-task action
- add role-based permission checks
- add tests for admin/member/child behavior

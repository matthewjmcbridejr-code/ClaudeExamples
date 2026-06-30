# Workflow: Review Gate

## When to use

Use this before accepting plans, prompts, documentation, code, or deployment steps.

## Input needed

- proposed output
- original requirement
- relevant spec
- tests or acceptance criteria

## Steps

1. Reviewer compares the output to the requirement.
2. Reviewer identifies missing details.
3. Reviewer checks assumptions.
4. Reviewer checks security and privacy risks.
5. Reviewer decides approve / revise / reject.

## Output format

- what is good
- what is risky
- what is missing
- required fixes
- suggested tests
- approval status

## LifeOS example review checks

- Are child/dependent permissions safe?
- Can private calendar items leak to the e-paper display?
- Are recurring tasks clearly defined?
- Are shared asset booking conflicts prevented?
- Are acceptance tests specific enough?

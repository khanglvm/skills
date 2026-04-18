# Handoff Template

Use this template for every handoff.

```md
# Handoff

## Goal
n/a

## User Request
- What the user asked for
- What success looks like

## Current State
- What is complete
- What is in progress
- What has not started

## Key Decisions
- Decision
  - Why it was chosen
  - Alternatives rejected (if relevant)

## Constraints And Preferences
- User preferences
- Repo or environment constraints
- Safety or scope limits

## Files And Artifacts
- `path/to/file.ext` — why it matters
- `path/to/other.ext:line` — key implementation/detail anchor

## Commands Run
- `command` — important result

## Validation
- Checks already run and outcomes
- Checks still needed

## Open Issues / Risks
- Blockers
- Assumptions requiring confirmation
- Edge cases not yet verified

## Next Steps
1. First concrete next action
2. Second action
3. Follow-up validation

## Carry-Forward Context
- IDs, URLs, branch names, environment details, error text, or snippets the next session must have
```

## Writing Guidance

Favor continuation utility over brevity.

Include only information that helps the next session act correctly:

- concrete file paths
- exact command outcomes
- specific unresolved questions
- user requirements that shaped decisions

Avoid:

- generic motivational text
- repeating obvious background with no operational value
- claiming work was verified when it was not

## Destination Guidance

- If the user did not ask for a file, print the handoff in chat.
- If the user asked for a file, write the handoff to the requested destination.
- If the user wants a file but did not give a path, ask for one.

---
name: handoff
description: >
  Create a full-fidelity conversation handoff for a fresh Claude/OpenCode session.
  Use when the user asks to hand off work, continue later, resume in a new session,
  capture full context, export session state, or write a detailed transfer note.
  Produces a structured handoff that preserves goals, decisions, current state,
  touched files, constraints, verification, risks, and exact next steps. When the
  user asks to save it, write the handoff to a file instead of only printing it.
license: MIT
metadata:
  argument-hint: "[goal or destination]"
---

# Handoff

Create a structured, high-context handoff for another session or agent.

## Purpose

Preserve the working state of the current conversation so a fresh session can continue with minimal loss of context.

Generate a handoff that is detailed enough to continue execution, not just summarize history.

## When to Use

Use this skill when the user asks to:

- hand off work to another session or agent
- resume later with full context
- export current conversation state
- create a continuation prompt or transfer note
- save a detailed project/session handoff to a file

## Output Modes

Default to printing the handoff in the conversation.

If the user explicitly asks to save/write/export the handoff, write it to the requested file path.

If the user wants a file but does not specify a path, ask for the destination path before writing.

## Required Structure

Load `references/handoff-template.md` and follow it closely.

Always include:

1. Objective and requested outcome
2. Current status and what is already done
3. Important decisions and rationale
4. Constraints, preferences, and user requirements
5. Files inspected, created, or changed
6. Commands run and key results
7. Validation already performed and remaining checks
8. Known issues, risks, and unresolved questions
9. Exact recommended next steps
10. Any critical snippets, identifiers, or references needed to continue

## Content Rules

Be concrete and exhaustive where it matters.

Prefer precise facts over vague summaries:

- include file paths with line references when known
- include command names and outcomes
- include errors encountered and how they were resolved
- include what was considered but intentionally not done
- distinguish completed work from planned work
- distinguish verified facts from assumptions

Do not pad with generic prose.

Do not omit blockers, caveats, or user constraints.

## File Writing Rules

When writing to a file:

- use the exact user-provided path if given
- otherwise ask for a destination path
- write the final handoff content only, without extra commentary
- tell the user where it was written after saving

## Quality Bar

Optimize for successful continuation by a fresh agent with no memory of the session.

A good handoff should let the next session answer all of these immediately:

- What am I trying to accomplish?
- What has already been done?
- What matters most technically?
- What constraints must I preserve?
- What should I do next, in order?

## Suggested Invocation Patterns

Examples of requests that should trigger this skill:

- "handoff this session"
- "create a continuation note"
- "write a handoff file"
- "summarize everything another agent needs"
- "prepare a new-session prompt"

If the user provides a goal, tailor the handoff toward that next-step goal.

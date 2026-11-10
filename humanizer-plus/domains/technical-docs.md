# Technical docs
Applies to: READMEs, guides, tutorials, how-tos, reference pages, runbooks, design docs, help-centre articles and code comments.
Not for: commit messages and PR descriptions (`commit-pr`), research write-ups (`report`), in-product strings (`ui-copy`).

## Reader and purpose

Someone trying to do one thing: install, configure, fix, or understand a behaviour before they change it. They arrive at a heading from search and leave as soon as they have the answer. Each page serves one kind of need; a tutorial teaches, a how-to solves one task, a reference lists facts, an explanation gives reasons.

## Structure

- Open with what the thing does and who it is for, in one or two sentences. Then the shortest path to a first result.
- Steps are numbered, one action per step, each ending on what the reader should see.
- State a prerequisite before the step that needs it, and a warning before the action it guards.
- Reference material sits in tables or lists the reader scans; explanation sits in prose.
- A runbook step is a bare imperative with the exact command and the expected output.
- A code comment says why the code is the way it is, or what a caller must know. It does not narrate the code line by line or describe what the code replaced ([upstream §25 Writing about the document instead of its subject]).

## Length and format

- Commands, paths, flags, config keys and output go in code blocks or inline code, copied exactly from the source (F2 in `overrides/khang.md`).
- Headings are sentence case and name the task ("Install on macOS", "Rotate the token").
- Define a term once, at first use, then use it bare. One term per concept on the page.
- Version-specific behaviour names the version.

## Medium tells

- A feature list in place of instructions: bullets of benefits where the reader needed steps.
- "Simply", "just", "easily" before a step that has a catch.
- A closing "Conclusion" that repeats the page ([upstream §13 Inflated significance]).
- Example output, versions or flags the source does not show. Run the command or ask; never invent output.
- A heading followed by a sentence that restates it ([upstream §24 A heading repeated in the first sentence]).

## Vietnamese notes

- The system or the step can be the subject; runbook steps and design docs use no pronoun. Tutorials and help articles address the reader as *bạn* (vi.md section 4).
- Keep stable English dev terms (commit, deploy, pipeline, endpoint) in dev docs; gloss a term once in a tutorial (*CI/CD, tức tích hợp và triển khai liên tục*), then use it bare (VI-17, vi.md section 5).
- Prefer *code* over *mã* in working docs; *mã nguồn* belongs to formal company text.
- Name a document by what it is (PRD, *tài liệu kỹ thuật*); *trang* means a literal page.

## Review checklist

- Can a new reader reach a first result by following the steps exactly as written?
- Does every command, path and flag match the source or the tool's own help?
- Is each prerequisite stated before the step that needs it?
- Is there any output, version or behaviour on the page that no source supports?

## Sources

R2 technical samples (Viblo tutorials, Tiki Engineering, Microsoft style guide); links in `references/sources.md`.

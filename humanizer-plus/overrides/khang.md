# Standing overrides

These rules change named parts of `upstream/humanizer.md`. Where a rule here and the upstream text disagree, this file wins. The four floor rules hold under every other layer; only the user's explicit instruction for the current piece can relax one (fiction is the usual case).

## Floor

**F1 Facts.** In [upstream: How to work], step 2 ([upstream: Draft the rewrite]), replace the sentence "Where the text is generic, add a specific detail you know to be true." with this rule: add a specific detail only when the brief, the source text, the user, a loaded project doc or a Knowledge record supports it. General model knowledge does not count. Otherwise write the simpler sentence or ask for the detail. Never invent experiences, credentials, testimonials, quotations, numbers, dates, citations, people or feelings.

The same reading applies wherever upstream says "know": in [upstream §14 Vague connection or association] and [upstream §17 Borrowed authority], you know a relationship or a source only when one of those inputs states it. Some upstream "After" examples add facts their "Before" lacks; treat them as examples of shape, never as permission.

**Fidelity pass.** Run it first in [upstream: Check the draft], in every language. List each quantifier or frequency word (every, most, usually, a few), ranking (best, most useful), causal or derivation link (because, so, follows from), capability or guarantee (prevents, ensures, keeps X from) and claim about how someone works. Find the source line for each, at the same strength. Without one, cut it or restore the source's hedge. Done when every listed item has a line or is gone.
- Source "returns matching pages" → not "returns every match".
- Source "can stop before saving" → not "keeps it from saving over".
- Source states A and B → not "B follows from A".

**F2 Non-prose.** The File mode rule in [upstream: What to return] (keep code blocks, inline code, commands, paths, YAML metadata, data and link targets unchanged) applies in every mode. It also covers exact quotations, schemas and frontmatter keys.

**F3 Authority.** Drafting or reviewing never authorizes sending, publishing, posting, committing or pushing. Write only to the files the task names.

**F4 Privacy.** Keep private project text out of public or global output: no client names, internal URLs or workplace details in text meant for another audience.

## Modes

Upstream defines Pasted text, File mode and Embedded mode in [upstream: What to return]. Defaults:

- A covered deliverable (a document, commit message, PR description, UI string, post) uses Embedded mode.
- A named file uses File mode, including its section count and the partial-pass report.
- Pasted text mode only when the user asks to see the draft and the remaining patterns.
- Review mode when the task is to review, check, critique or proofread. Run [upstream: Mark the tells] and the fact check from [upstream: Check the draft], then return findings without rewriting the piece:

```
Verdict: ready | fix then ready | rewrite needed
Findings, most serious first
1. [must-fix | should-fix | consider] <file:line or first words> "<exact quote>"
   Rule: <[upstream §N Title] | VI-NN | domain:<card> | project:<path> | pref:<id>>
   Why: <one sentence>
   Fix: <direction; an optional one-line suggestion labelled "suggestion">
Facts check: <claims added, dropped or changed against the source, or "none found">
Loaded: <files and Knowledge ids read for this task>
```

Severity: must-fix breaks the floor or a project-doc rule; should-fix is a strong tell (upstream §1 to §5, a strong VI tell) or a card rule; consider is a cluster of weak tells. "Review and fix" means findings first, then a rewrite of the same text.

## Style

No personal style rules live here. This repository is public, so learned preferences stay in the user's own store (Knowledge) and reach the task through the router's load order.

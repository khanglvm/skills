# Maintaining humanizer-plus

## Where to edit

| Change | File |
|---|---|
| Load order, medium table, precedence, modes | `SKILL.md` |
| A rule that changes an upstream section | `overrides/khang.md`, citing the section |
| Vietnamese grammar, register, mechanics, the one-line tell families | `languages/vi.md` (drafting core, at most 10 KB) |
| A tell's forms, examples and Keep exceptions | `languages/vi-catalogue.md` |
| Rules for one medium | the card in `domains/` |
| A linted Vietnamese tell and its strength | `patterns/vi-tells.json` (the only place strengths live), plus its entry in `languages/vi-catalogue.md` |
| Research links | `references/sources.md`; copyright notices in `ATTRIBUTION.md` |

Never edit `upstream/`. It holds blader/humanizer's `SKILL.md` byte for byte, renamed to `humanizer.md` so skill loaders do not register a second skill. Personal writing preferences belong in Knowledge, not here: this repository is public.

Cite upstream as `[upstream §N Title]` (the heading `N. Title`) or `[upstream: Heading]` (a heading or a bold label such as `**File mode.**`). Card and layer size caps are enforced by the tests.

## Checks

```
python3 -B -m unittest discover -s humanizer-plus/tests
python3 -B humanizer-plus/scripts/sync-upstream.py check
```

To calibrate the linter on a local human corpus, point the tests at a folder of `n*.txt` files. The test then requires zero clusters at the default doctype. Keep that corpus out of the repository.

```
HUMANIZER_PLUS_VI_CORPUS=/path/to/corpus python3 -B -m unittest discover -s humanizer-plus/tests
```

Each pattern carries `hit` and `miss` examples; the tests require every hit to match and every miss to stay clean, and every strong pattern to have a miss. Add a `miss` when you fix a false positive, and one for each *Keep* exception the catalogue gives a pattern.

## Syncing upstream

The script has no network code. Keep a local clone of blader/humanizer and fetch it first.

```
git -C ~/Documents/repo/humanizer-upstream fetch --tags
python3 -B humanizer-plus/scripts/sync-upstream.py diff --source ~/Documents/repo/humanizer-upstream --ref vX.Y.Z --out /tmp/upstream.diff
python3 -B humanizer-plus/scripts/sync-upstream.py apply --source ~/Documents/repo/humanizer-upstream --ref vX.Y.Z
```

`diff` writes nothing. It prints the versions, the CHANGELOG entries in between, renamed or removed headings, citations that would break, bare `§N` citations whose title changed, override quotes that would break, changed lines per section and a watchlist of added or removed lines that mention inventing, adding concrete detail, including or filling in, publishing, sending, committing, installing, running, URLs or credentials.

`UPSTREAM.json` `sections` records the title of every upstream `§N` the layers were written against. After `apply`, `check` fails for each bare `§N` whose title changed; reread the files it names, fix them, then update that title in `sections`. `check` also fails when an override quotes upstream wording (`the sentence "..."`, `the clause "..."`) that upstream no longer contains.

Review rule: paste the `diff` summary into the commit body. Before merge, a reviewer checks each watchlist line and each CHANGELOG behaviour change against the floor in `overrides/khang.md`, and confirms the upstream text carries no instruction aimed at the agent. Then run `apply`, fix any citation it reports in the same commit, and update `metadata.upstream` in `SKILL.md`.

## Knowledge vendoring

Knowledge copies this folder byte for byte into its own `skills/humanizer-plus/`, pinned by commit and tree hash, and installs it on the maintainer's devices. Those devices get updates through Knowledge after a new commit here is vendored; do not also install the skill on them with `npx skills`.

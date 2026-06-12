# cloak-agent-browser — CloakBrowser × agent-browser integration

Backup + restore bundle for the **stealth browser-automation flow**: whenever an
agent (Claude Code, Codex CLI) needs a browser, it drives **agent-browser**'s
agent-friendly tools (snapshot refs, click/fill, screenshot, eval) on a
**CloakBrowser** stealth Chromium that owns the process. You get bot-detection
bypass (C++-level patched fingerprint, `navigator.webdriver === false`) *and*
the ergonomic agent CLI, behind one command.

## The flow this restores

```bash
cloak-agent-browser ab -- open https://example.com   # auto-starts stealth browser
cloak-agent-browser ab -- snapshot -i                # agent-browser tools over CDP
cloak-agent-browser ab -- click @e1
cloak-agent-browser stop                             # when done

# separate account → own profile + port (start once, then ab reuses it):
cloak-agent-browser start --port 9341 --profile upwork --humanize
cloak-agent-browser ab --port 9341 --session upwork -- open https://www.upwork.com
```

### How it works

`CloakBrowser` (a patched-source Chromium + Playwright-shaped Python wrapper)
launches the browser with a CDP endpoint via `scripts/serve.sh`. `agent-browser`
attaches to that endpoint with `--cdp <port>` and provides the agent tooling.
The `cloak-agent-browser` wrapper ties them together: `ab` **auto-starts** the
stealth browser on first use (profile `default`, `--humanize`) and **serializes**
concurrent CDP access with a lock.

## What's in this bundle

| Path | Restores to | Origin |
|------|-------------|--------|
| `bin/cloak-agent-browser` | `~/.local/bin/cloak-agent-browser` | **owned** (the bridge) |
| `overlays/cloakbrowser/scripts/serve.{sh,py}` | `~/.agents/skills/cloakbrowser/scripts/` | upstream backend the bridge requires |
| `overlays/cloakbrowser/SKILL.md` + `references/stealth-knobs.md` | `~/.agents/skills/cloakbrowser/` | upstream + integration edits |
| `overlays/agent-browser/SKILL.md` | `~/.agents/skills/agent-browser/SKILL.md` | upstream + integration edits |
| `instructions/browser-automation.claude.md` | block in `~/.claude/CLAUDE.md` | **owned** |
| `instructions/browser-automation.codex.md` | block in `~/.codex/AGENTS.md` | **owned** |

The two SKILL.md files are *snapshots* of the customized skills (upstream
`agent-browser` + `OctavianTocan/cloakbrowser`). They are overlaid on top of a
base install; the installer backs up whatever is there first.

## Restore on a new machine

```bash
# 1) base dependencies (download binaries — not bundled):
brew install agent-browser              # or: npm i -g agent-browser
curl -LsSf https://astral.sh/uv/install.sh | sh
uv tool install cloakbrowser
cloakbrowser install                    # ~206 MB stealth Chromium

# 2) lay down the integration (idempotent):
bash cloak-agent-browser/install.sh

# 3) smoke test:
cloak-agent-browser ab -- open https://example.com \
  && cloak-agent-browser ab -- eval 'navigator.webdriver' \
  && cloak-agent-browser stop
```

The installer is safe to re-run: existing files are backed up as
`*.cab-bak.<stamp>`, and the CLAUDE.md / AGENTS.md blocks are replaced in place
between `<!-- CLOAK_AB_START -->` / `<!-- CLOAK_AB_END -->` markers.

## `cloak-agent-browser` commands

| Command | Purpose |
|---------|---------|
| `ab [--port N] [--session NAME] -- <args>` | Run agent-browser against the stealth browser; **auto-starts** it and serializes access. The default entrypoint. |
| `start [--port N] [--profile NAME] [--humanize] [--headed] [--proxy URL] [--geoip]` | Explicitly start a stealth browser with specific flags. |
| `py [<args>]` | Print (or exec) the CloakBrowser venv Python — for inline Playwright-style scripts. |
| `status` / `stop` / `cdp` | Inspect / stop the browser, or print the `--cdp` flag. |

## Re-syncing this backup after future edits

If you tweak the live files later, refresh the snapshot:

```bash
cp ~/.local/bin/cloak-agent-browser                                  cloak-agent-browser/bin/
cp ~/.agents/skills/agent-browser/SKILL.md                           cloak-agent-browser/overlays/agent-browser/
cp ~/.agents/skills/cloakbrowser/SKILL.md                            cloak-agent-browser/overlays/cloakbrowser/
cp ~/.agents/skills/cloakbrowser/references/stealth-knobs.md         cloak-agent-browser/overlays/cloakbrowser/references/
cp ~/.agents/skills/cloakbrowser/scripts/serve.sh                    cloak-agent-browser/overlays/cloakbrowser/scripts/
cp ~/.agents/skills/cloakbrowser/scripts/serve.py                    cloak-agent-browser/overlays/cloakbrowser/scripts/
```

(The CLAUDE.md / AGENTS.md blocks live canonically in `instructions/` — edit
there and re-run the installer to push them back.)

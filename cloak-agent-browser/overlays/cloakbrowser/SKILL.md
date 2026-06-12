---
name: cloakbrowser
description: Stealth Chromium browser automation that bypasses bot detection. Use this skill whenever the user wants to scrape, screenshot, PDF, or automate a site that blocks normal headless browsers — Cloudflare Turnstile, reCAPTCHA v3, FingerprintJS, ShieldSquare, BrowserScan, "Access Denied" responses, suspicious 403/429s on plain `curl`, or any site where Playwright/Puppeteer get caught. Also use when the user mentions CloakBrowser, stealth Chromium, anti-bot bypass, "headless detection", "real Chrome fingerprint", or wants a one-off "what does this page actually render" check. Prefer this skill over raw `curl`/`fetch` for any site behind a CDN or bot-detection layer.
homepage: https://github.com/CloakHQ/CloakBrowser
---

# CloakBrowser

A patched-source Chromium plus a Playwright-shaped Python wrapper. Fingerprints
are modified at the C++ level (canvas, WebGL, audio, fonts, WebRTC, TLS, CDP
input, `navigator.webdriver`, plugin list, `window.chrome`, …) so detection
services see a real browser because it **is** a real browser — no JS shim that
breaks on the next Chrome upgrade.

## Install state on this machine

Already installed:

- `cloakbrowser` CLI lives at `/Users/khang/.local/bin/cloakbrowser`.
- Stealth Chromium binary lives under `/Users/khang/.cloakbrowser/`.
- Wrapper Python lives in the uv tool venv:
  `$(uv tool dir)/cloakbrowser/bin/python`.
- `cloak-agent-browser` lives at `/Users/khang/.local/bin/cloak-agent-browser`
  and starts CloakBrowser for `agent-browser --cdp` control.

If a fresh checkout or a new machine needs setting up:

```bash
uv tool install cloakbrowser
cloakbrowser install        # downloads the ~206 MB Chromium binary
```

The `cloakbrowser` CLI only manages the binary (`install`, `info`, `update`,
`clear-cache`). It is **not** a scraper — for that, use the scripts in this
skill or write inline Python.

## Decision tree — pick the right tool

| Task                                                          | Use                            |
|---------------------------------------------------------------|--------------------------------|
| Interactive browsing with easy refs/click/fill/screenshot      | `cloak-agent-browser ab -- <cmd>` (agent-browser over CDP) |
| Logged-in or bot-protected multi-step browser flow             | `cloak-agent-browser start --profile <name> --humanize` + `cloak-agent-browser ab` |
| Get the HTML or visible text of a page                        | `scripts/fetch.py`             |
| Save a PNG of a page or element                               | `scripts/screenshot.py`        |
| Render a page to PDF                                          | `scripts/pdf.py`               |
| Run a JS expression against a page and get JSON back          | `scripts/eval-js.py`           |
| Confirm stealth is working                                    | `scripts/check-stealth.py`     |
| Long-lived browser shared across many tool calls / skills     | `cloak-agent-browser` (CDP) or `scripts/serve.sh` |
| Multi-step interactive flow (login, click, type, conditional) | Inline Python — see below      |

For one-shot "fetch / screenshot / PDF this URL", reach for a bundled script —
they use `argparse` and take `--humanize`, `--proxy`, `--geoip`, `--wait`, etc.

**For agent-controlled browsing (the common case), use the bridge.**
CloakBrowser owns the Chromium; `agent-browser` drives it over CDP. The
`cloak-agent-browser ab` wrapper auto-starts the stealth browser on first use
(profile `default`, `--humanize`) and serializes concurrent CDP access — no
manual start, no port to remember:

```bash
cloak-agent-browser ab -- open https://example.com
cloak-agent-browser ab -- snapshot -i
cloak-agent-browser ab -- click @e1
cloak-agent-browser stop                 # when the task is done
```

Use one profile per identity. For a separate account, start it once with its own
profile + port, then `ab` reuses it:

```bash
cloak-agent-browser start --port 9341 --profile upwork --humanize
cloak-agent-browser ab --port 9341 --session upwork -- open https://www.upwork.com
```

See the **agent-browser** skill for the full command set (refs, fill, eval,
download, diff, auth vault, …) — every `agent-browser <cmd>` there runs as
`cloak-agent-browser ab -- <cmd>`.

## Bundled scripts

All scripts are executable (`#!` already points at the right Python). Invoke
them by absolute path:

```bash
SK=/Users/khang/.agents/skills/cloakbrowser/scripts

$SK/fetch.py https://example.com                       # full HTML on stdout
$SK/fetch.py https://example.com --text                # visible text only
$SK/fetch.py https://example.com --selector "h1"       # scoped to a selector
$SK/fetch.py https://protected.example --humanize      # behavioural stealth
$SK/fetch.py https://geo.example --proxy socks5://u:p@host:1080 --geoip

$SK/screenshot.py https://example.com /tmp/out.png --full
$SK/screenshot.py https://example.com /tmp/hero.png --selector ".hero"
$SK/screenshot.py https://example.com /tmp/m.png --viewport 390x844

$SK/pdf.py https://example.com /tmp/page.pdf --format A4
$SK/pdf.py https://example.com /tmp/wide.pdf --landscape

$SK/eval-js.py https://news.example "Array.from(document.querySelectorAll('h2')).map(h=>h.innerText)"
$SK/eval-js.py https://example.com  "({ua: navigator.userAgent, w: innerWidth})"

$SK/check-stealth.py        # JSON report + exit 0 if all 4 stealth tells pass

$SK/serve.sh --port 9222    # starts cloakserve in background; logs /tmp/cloakserve.log
cloak-agent-browser start --profile default --humanize --url about:blank
```

The pattern is consistent: positional `URL` (and `OUTPUT` where relevant), then
optional flags `--humanize`, `--proxy`, `--geoip`, `--wait`, `--timeout`.

## Inline Python — for everything the scripts don't cover

For multi-step flows (login, fill a form, click through, conditional waits),
write a one-off script. Run it with the CloakBrowser venv interpreter via
`cloak-agent-browser py` (resolves the right Python on any machine):

```bash
cloak-agent-browser py - <<'PY'
from cloakbrowser import launch
b = launch(headless=True, humanize=True)
p = b.new_page()
p.goto("https://example.com/login", wait_until="domcontentloaded")
p.fill("#email", "me@example.com")
p.fill("#password", "…")
p.click("button[type=submit]")
p.wait_for_url("**/dashboard**")
print(p.title())
b.close()
PY
```

The API is identical to Playwright's sync API — anything in the Playwright
docs works here. The only differences:

- `from cloakbrowser import launch` (not `from playwright.sync_api`)
- Skip `sync_playwright().start()` — `launch()` is a top-level function
- All stealth flags (`humanize`, `proxy`, `geoip`, `auto_update`) go on
  `launch()`, not the page

For persistent sessions, use `launch_persistent_context(user_data_dir)`.

## When to load `references/stealth-knobs.md`

Read it when:

- A target blocks despite stealth (covers `humanize` / proxy / persistent
  profile escalation order).
- The user asks about proxies, residential vs datacentre, geo matching.
- You need to share one browser across many tool calls (CDP server mode).

For routine "fetch this URL" / "screenshot this page" work, the table and
script examples above are enough — don't load the reference.

## Anti-patterns

- Don't `pip install cloakbrowser` system-wide. PEP 668 blocks it on this VPS.
  Use `uv tool install cloakbrowser` (already done).
- Don't run `playwright install` — CloakBrowser ships its own Chromium and
  doesn't use Playwright's bundled binaries.
- Don't import `cloakbrowser` from the system Python — it lives in the uv
  tool venv only. Use the venv's Python, or the bundled scripts.
- Don't enable `humanize=True` for plain scraping of unprotected sites — it
  adds latency with no win.
- Don't keep `serve.sh` running for a one-shot fetch. The CDP server is for
  shared, long-lived sessions; `fetch.py` is faster for one URL.

## Troubleshooting

- `Binary not found` / first-run hang → `cloakbrowser install`.
- `ModuleNotFoundError: cloakbrowser` → you're on the wrong Python. Run scripts
  with `cloak-agent-browser py - <<'PY' … PY` (resolves the CloakBrowser venv
  interpreter) or use the bundled scripts (their shebang already points there).
- Slow startup → the binary checks for updates on launch. Pass
  `auto_update=False` to `launch()` (or set `CLOAKBROWSER_AUTO_UPDATE=0`) to
  skip.
- Still blocked → see `references/stealth-knobs.md` for the escalation order
  (`humanize` → residential proxy + `geoip` → persistent profile).

<!-- CLOAK_AB_START -->
## Browser Automation — CloakBrowser Instance, agent-browser Control

For website browsing, scraping, screenshots, login flows, and bot-sensitive sites, make
**CloakBrowser** own the Chromium instance and use **`agent-browser`** as the control surface
(attached over CDP). This keeps CloakBrowser's C++-level patched fingerprint (`navigator.webdriver
=== false`, real canvas/WebGL/audio/TLS) while preserving agent-browser refs, snapshots, clicks,
fills, screenshots, and CLI ergonomics.

**Blessed entrypoint — `cloak-agent-browser ab`.** It auto-starts the stealth browser on first use
(profile `default`, `--humanize`) and serializes CDP access, so there is no manual start and no port
to track:

```bash
cloak-agent-browser ab -- open "<url>"
cloak-agent-browser ab -- snapshot -i
cloak-agent-browser ab -- click @e1
cloak-agent-browser stop                 # when the task is done
```

Every `agent-browser <cmd>` from the agent-browser skill runs as `cloak-agent-browser ab -- <cmd>`.

Rules:

- One CloakBrowser profile per identity/account. For a separate account, start it once with its own
  profile + port, then `ab` reuses it:
  `cloak-agent-browser start --port 9341 --profile upwork --humanize`, then
  `cloak-agent-browser ab --port 9341 --session upwork -- open "<url>"`.
- Add `--proxy ... --geoip` (on `start`) only when geo/IP matching is needed; `--headed` only for
  manual login, visual debugging, or when the user asks to watch.
- Don't hand-run parallel `agent-browser --cdp <port>` commands against the same port — `ab` already
  serializes; chain a non-interactive sequence in one `ab` call with `&&`.
- Stop with `cloak-agent-browser stop` when done, unless the user asks to keep the session alive.
- For inline Playwright-style Python against CloakBrowser, run it with `cloak-agent-browser py - <<'PY' … PY`.
- Use plain `agent-browser` without CloakBrowser only for local app QA, `file://` checks, iOS
  simulator work, or when the user explicitly requests standard agent-browser Chromium.

`~/.agent-browser/config.json` points at regular Google Chrome and headed mode; that only affects
plain `agent-browser`. The CDP bridge attaches to CloakBrowser and ignores it.
<!-- CLOAK_AB_END -->

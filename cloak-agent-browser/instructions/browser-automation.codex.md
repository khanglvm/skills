<!-- CLOAK_AB_START -->
## Browser Testing

- For website browsing, scraping, screenshots, login flows, and bot-sensitive sites, make CloakBrowser own the Chromium instance and use `agent-browser` as the control surface (attached over CDP). This keeps CloakBrowser's C++-level patched fingerprint (`navigator.webdriver === false`) plus agent-browser's refs/click/fill/screenshot tools.
- Blessed entrypoint — `cloak-agent-browser ab`. It auto-starts the stealth browser on first use (profile `default`, `--humanize`) and serializes CDP access, so there's no manual start and no port to track:
  - `cloak-agent-browser ab -- open "<url>"`
  - `cloak-agent-browser ab -- snapshot -i`
  - `cloak-agent-browser ab -- click @e1`
  - `cloak-agent-browser stop` when done.
- Every `agent-browser <cmd>` runs as `cloak-agent-browser ab -- <cmd>`. Chain a non-interactive sequence in one `ab` call with `&&`; `ab` already serializes, so don't hand-run parallel `agent-browser --cdp <port>` against the same port.
- One CloakBrowser profile per identity/account. For a separate account: `cloak-agent-browser start --port 9341 --profile <name> --humanize`, then `cloak-agent-browser ab --port 9341 --session <name> -- open "<url>"`. Add `--proxy ... --geoip` (on `start`) only for geo/IP matching; `--headed` only for manual login or when the user asks to watch.
- For inline Playwright-style Python against CloakBrowser, run it with `cloak-agent-browser py - <<'PY' … PY`.
- Use plain headless `agent-browser`, Playwright, or Puppeteer only for local app QA, `file://` checks, iOS simulator work, or when the user explicitly requests standard non-CloakBrowser automation.
<!-- CLOAK_AB_END -->

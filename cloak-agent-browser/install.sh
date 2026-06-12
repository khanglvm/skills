#!/usr/bin/env bash
# Restore / install the CloakBrowser × agent-browser integration on this machine.
#
# Lays down:
#   - bin/cloak-agent-browser            -> ~/.local/bin/cloak-agent-browser
#   - the stealth serve backend          -> ~/.agents/skills/cloakbrowser/scripts/{serve.sh,serve.py}
#   - customized skill docs (overlays)   -> ~/.agents/skills/{cloakbrowser,agent-browser}/
#   - browser-automation instruction blocks injected into ~/.claude/CLAUDE.md and ~/.codex/AGENTS.md
#
# Idempotent: existing files are backed up (*.cab-bak.<stamp>); instruction blocks are
# replaced in place between <!-- CLOAK_AB_START --> / <!-- CLOAK_AB_END --> markers.
#
# Usage:  bash cloak-agent-browser/install.sh
set -euo pipefail

SELF_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
STAMP="$(date +%Y%m%d-%H%M%S)"
AGENTS_SKILLS="${HOME}/.agents/skills"

# Skill doc root (where customized SKILL.md docs go). Prefer the npm `skills` canonical dir.
if [ -d "${HOME}/.agents/skills" ]; then SKILL_ROOT="${HOME}/.agents/skills"
elif [ -d "${HOME}/.claude/skills" ]; then SKILL_ROOT="${HOME}/.claude/skills"
else SKILL_ROOT="${HOME}/.agents/skills"; fi

say()  { printf '%s\n' "$*"; }
back() { [ -f "$1" ] && ! cmp -s "$2" "$1" && cp "$1" "$1.cab-bak.$STAMP" || true; }

place() {  # place <src> <dst>  (mkdir parent, back up changed dst, copy)
  local src="$1" dst="$2"
  mkdir -p "$(dirname "$dst")"
  back "$dst" "$src"
  cp "$src" "$dst"
  say "  + $dst"
}

inject() {  # inject <target-md> <block-file>
  local target="$1" block="$2"
  mkdir -p "$(dirname "$target")"; [ -f "$target" ] || : > "$target"
  if grep -q '<!-- CLOAK_AB_START -->' "$target" 2>/dev/null; then
    back "$target" "$target"  # always snapshot before rewrite
    cp "$target" "$target.cab-bak.$STAMP"
    awk -v bf="$block" '
      BEGIN { while ((getline l < bf) > 0) blk = blk l ORS }
      /<!-- CLOAK_AB_START -->/ { printf "%s", blk; skip=1; next }
      /<!-- CLOAK_AB_END -->/   { skip=0; next }
      skip { next } { print }
    ' "$target" > "$target.tmp" && mv "$target.tmp" "$target"
    say "  ~ updated block in $target"
  elif grep -q 'cloak-agent-browser ab' "$target" 2>/dev/null; then
    say "  = $target already references cloak-agent-browser (unmarked) — left as-is"
  else
    printf '\n' >> "$target"; cat "$block" >> "$target"
    say "  + appended block to $target"
  fi
}

say "==> cloak-agent-browser install  (stamp $STAMP)"

# 1) Core bridge script
say "[1/4] bridge script"
place "$SELF_DIR/bin/cloak-agent-browser" "${HOME}/.local/bin/cloak-agent-browser"
chmod +x "${HOME}/.local/bin/cloak-agent-browser"

# 2) Stealth serve backend (bridge hard-depends on this exact path) + cloakbrowser docs
say "[2/4] cloakbrowser overlay + serve backend  ($AGENTS_SKILLS/cloakbrowser)"
place "$SELF_DIR/overlays/cloakbrowser/scripts/serve.sh"            "$AGENTS_SKILLS/cloakbrowser/scripts/serve.sh"
place "$SELF_DIR/overlays/cloakbrowser/scripts/serve.py"            "$AGENTS_SKILLS/cloakbrowser/scripts/serve.py"
place "$SELF_DIR/overlays/cloakbrowser/SKILL.md"                    "$AGENTS_SKILLS/cloakbrowser/SKILL.md"
place "$SELF_DIR/overlays/cloakbrowser/references/stealth-knobs.md" "$AGENTS_SKILLS/cloakbrowser/references/stealth-knobs.md"
chmod +x "$AGENTS_SKILLS/cloakbrowser/scripts/serve.sh"

# 3) agent-browser doc overlay (only if the skill is installed; it is documentation only)
say "[3/4] agent-browser overlay  ($SKILL_ROOT/agent-browser)"
if [ -d "$SKILL_ROOT/agent-browser" ]; then
  place "$SELF_DIR/overlays/agent-browser/SKILL.md" "$SKILL_ROOT/agent-browser/SKILL.md"
else
  say "  = agent-browser skill not installed — skipping doc overlay (optional)."
  say "    Install it later with: npx skills add agent-browser   (docs only; the binary is the hard dep)"
fi

# 4) Instruction blocks
say "[4/4] instruction blocks"
inject "${HOME}/.claude/CLAUDE.md" "$SELF_DIR/instructions/browser-automation.claude.md"
inject "${HOME}/.codex/AGENTS.md"  "$SELF_DIR/instructions/browser-automation.codex.md"

# Dependency check (no silent big downloads — just report)
say ""
say "==> dependency check"
have() { command -v "$1" >/dev/null 2>&1; }
have agent-browser && say "  ok  agent-browser ($(agent-browser --version 2>/dev/null || echo '?'))" \
                    || say "  ✗   agent-browser   → brew install agent-browser   (or: npm i -g agent-browser)"
have uv            && say "  ok  uv" \
                    || say "  ✗   uv              → curl -LsSf https://astral.sh/uv/install.sh | sh"
have cloakbrowser  && say "  ok  cloakbrowser CLI" \
                    || say "  ✗   cloakbrowser    → uv tool install cloakbrowser"
if have cloakbrowser && cloakbrowser info >/dev/null 2>&1; then
  say "  ok  cloakbrowser Chromium installed"
else
  say "  ✗   cloakbrowser Chromium → cloakbrowser install   (~206 MB stealth Chromium)"
fi
case ":$PATH:" in
  *":${HOME}/.local/bin:"*) : ;;
  *) say "  !   ~/.local/bin is not on PATH — add it so 'cloak-agent-browser' resolves." ;;
esac

say ""
say "==> done. Smoke test:"
say "    cloak-agent-browser ab -- open https://example.com && cloak-agent-browser ab -- eval 'navigator.webdriver' && cloak-agent-browser stop"

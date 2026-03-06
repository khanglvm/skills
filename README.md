# skills

Dedicated repository for reusable coding skills.

## Included

- `plan`: create detailed technical implementation plans through research, codebase analysis, solution design, and comprehensive documentation with workflow modes (auto/fast/hard/parallel/two).
- `fix-codex-skill`: repairs invalid skill formats for Codex compatibility (fixes `SKILL.md` frontmatter and `agents/openai.yaml`).
- `codex-cli`: provides official Codex CLI guidance for installation, authentication, config options, usage, approvals/sandbox, MCP integration, and troubleshooting.
- `outline-cli`: operate the Outline API CLI with deterministic, token-efficient, and safety-gated workflows (search/read/update/patch/delete).

Install with:

```bash
npx skills add khanglvm/skills/plan
npx skills add khanglvm/skills/fix-codex-skill
npx skills add khanglvm/skills/codex-cli
npx skills add khanglvm/skills/outline-cli

# Or install from repo root with skill filter:
npx skills add https://github.com/khanglvm/skills --skill outline-cli

# Headless (non-interactive) install for Codex:
npx skills add https://github.com/khanglvm/skills --skill outline-cli --agent codex -y
```

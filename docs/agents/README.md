# Multi-agent setup

This repository supports Codex, Claude Code, and Google Antigravity through shared instructions and the Agent Skills standard

## Supported structure

| Tool | Auto-loaded instructions | Skill | Additional configuration |
| --- | --- | --- | --- |
| Codex | `AGENTS.md` | `.agents/skills/theme-workflow/SKILL.md` | Uses the repository instruction hierarchy |
| Claude Code | `CLAUDE.md` → `AGENTS.md` | `.claude/skills/theme-workflow/SKILL.md` | `.claude/settings.json`, `.claude/agents/theme-reviewer.md` |
| Antigravity | CLI: `AGENTS.md`; IDE: `.agents/rules/repository.md` → `AGENTS.md` | `.agents/skills/theme-workflow/SKILL.md` | `GEMINI.md` routing, workflows, and custom agents |

## Single source of truth

- The root `AGENTS.md` file is the single source of truth for the shared repository contract
- `CLAUDE.md` and `.agents/rules/repository.md` are thin adapters that import the shared contract
- `GEMINI.md` routes CLI and IDE entry points without importing the shared contract again, avoiding duplicate context
- `.agents/skills/theme-workflow/SKILL.md` is the canonical shared skill
- `.claude/skills/theme-workflow/SKILL.md` is the Claude Code compatibility copy
- The compatibility copy is required because the currently installed Claude Code does not automatically discover project skills from `.agents/skills`
- The repository validator enforces byte-for-byte equality between the two skill files instead of using a symbolic link, avoiding operating system and Claude Code version differences

## Provided capabilities

- `theme-workflow`: creates, modifies, version-syncs, validates, packages, and prepares independent themes for release
- `theme-reviewer`: review-only agent for pre-release checks; Claude Code uses `permissionMode: plan` to block writes
- `/validate-theme`: read-only validation workflow invoked by Antigravity
- `.claude/settings.json`: confirmation rules for remote Git changes and Claude `Read` restrictions for sensitive paths

The repository does not pin a specific model ID. The Claude reviewer also uses `model: inherit` to preserve the execution environment's selection

The review-only wording in the Antigravity custom agent is an operating contract; the file itself does not enforce project permissions. Run reviews that require write prevention in Antigravity's Planning or Strict permission mode. Project writes may otherwise be allowed by default, so prompt instructions alone are not a security boundary

Claude `Read(...)` deny rules apply to Claude's file-reading tool and are not a sandbox for every shell command. `.gitignore` separately prevents sensitive files from being tracked by Git

## Validation

Run from the repository root after modifying agent files

```bash
python3 tools/agents/validate_setup.py
```

Validation checks

- Presence of every model entry file and project configuration file
- Adapter imports of `AGENTS.md` and their resolved target paths
- Byte-for-byte equality between the shared skill and the Claude compatibility copy
- Required frontmatter values for skills and custom agents
- Shared reviewer body content and Claude `plan` permissions
- Claude project settings JSON and key safety rules
- `.gitignore` protections for sensitive files and local agent state

Run the smoke validation to inspect installed CLIs as well

```bash
python3 tools/agents/validate_setup.py --smoke
```

Smoke validation checks installed Codex, Claude, and Gemini CLI versions and verifies that Gemini CLI discovers the repository's `theme-workflow` skill

## Local-only configuration

The following files contain personal configuration and must not be committed

- `CLAUDE.local.md`
- `.claude/settings.local.json`
- `.claude/agent-memory-local/`
- Credentials and local state under `.codex/` or `.gemini/`

Do not store API keys, OAuth tokens, personal MCP credentials, or model-specific personal settings in the repository

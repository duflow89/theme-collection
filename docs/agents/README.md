<div align="center">

# Multi-agent Setup

**One repository contract, one theme workflow, three compatible agent surfaces**

[Repository home](../../README.md) · [Canonical contract](../../AGENTS.md) · [Theme workflow](../../.agents/skills/theme-workflow/SKILL.md)

</div>

---

## Architecture at a glance

| Layer | Canonical source | Adapters and consumers |
| --- | --- | --- |
| Repository rules | `AGENTS.md` | Codex directly; Claude through `CLAUDE.md`; Antigravity through `GEMINI.md` and the workspace rule |
| Theme workflow | `.agents/skills/theme-workflow/SKILL.md` | Codex and Antigravity directly; Claude through the compatibility mirror |
| Release review | Shared reviewer body | Antigravity custom agent and Claude Code plan-mode agent |
| Validation | Repository Python tools | All supported agents and human contributors |

The adapters stay intentionally thin so repository rules are not copied into multiple files

## Tool matrix

| Tool | Auto-loaded instructions | Theme skill | Additional configuration |
| --- | --- | --- | --- |
| Codex | `AGENTS.md` | `.agents/skills/theme-workflow/SKILL.md` | Uses the repository instruction hierarchy |
| Claude Code | `CLAUDE.md` → `AGENTS.md` | `.claude/skills/theme-workflow/SKILL.md` | `.claude/settings.json`, `.claude/agents/theme-reviewer.md` |
| Google Antigravity | CLI: `AGENTS.md`; IDE: `.agents/rules/repository.md` → `AGENTS.md` | `.agents/skills/theme-workflow/SKILL.md` | `GEMINI.md`, workflows, and custom agents |

## Sources of truth

> [!IMPORTANT]
> Update canonical files first. Do not duplicate repository rules inside adapters

- `AGENTS.md` is the canonical repository contract
- `CLAUDE.md` and `.agents/rules/repository.md` import that contract
- `GEMINI.md` routes CLI and IDE entry points without importing the contract twice
- `.agents/skills/theme-workflow/SKILL.md` is the canonical cross-tool skill
- `.claude/skills/theme-workflow/SKILL.md` is the byte-identical Claude Code compatibility copy
- The compatibility copy exists because the supported Claude Code setup does not discover project skills from `.agents/skills/`

When the canonical skill changes, update the Claude mirror in the same change. The setup validator enforces byte-for-byte equality

## Included capabilities

| Capability | Purpose |
| --- | --- |
| `theme-workflow` | Create, modify, document, validate, package, and prepare independent themes for release |
| `theme-reviewer` | Perform a read-only pre-release review of metadata, assets, documentation, versions, rights, and package boundaries |
| `/validate-theme` | Run the Antigravity read-only validation workflow |
| `.claude/settings.json` | Require confirmation for remote Git changes and block sensitive file reads through Claude's `Read` tool |

The repository does not pin a model ID. The Claude reviewer uses `model: inherit` so the execution environment remains in control

## Permission boundaries

> [!WARNING]
> Prompt text is an operating contract, not a universal sandbox

- Claude Code enforces the reviewer with `permissionMode: plan`
- Antigravity reviews need Planning or Strict permission mode when hard write prevention is required
- Claude `Read(...)` deny rules apply to Claude's file-reading tool, not every possible shell command
- `.gitignore` independently protects local settings, credentials, signing files, and generated archives from tracking
- No agent may commit, push, tag, publish, or upload unless the user explicitly requests it

## Validate the setup

Run the deterministic repository checks after modifying agent instructions, skills, reviewers, adapters, or settings

```bash
python3 tools/agents/validate_setup.py
```

The validator checks

- Required entry files and project configuration
- Adapter imports and resolved paths
- Canonical and Claude skill equality
- Required frontmatter and shared reviewer content
- Claude plan-mode and permission rules
- `.gitignore` protections for sensitive and generated files

Inspect installed CLIs and Gemini skill discovery with the optional smoke check

```bash
python3 tools/agents/validate_setup.py --smoke
```

## Local-only configuration

Keep personal configuration and runtime state out of Git

```text
CLAUDE.local.md
.claude/settings.local.json
.claude/agent-memory-local/
.codex/
.gemini/
```

Never store API keys, OAuth tokens, personal MCP credentials, `.env` files, signing keys, or model-specific personal settings in the repository

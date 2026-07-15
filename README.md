# Theme Collection

A collection for managing independent themes for apps such as Chrome and VS Code in one repository

Themes are organized independently under each app rather than converted into matching variants across multiple apps

## Structure

```text
theme-collection/
├── chrome/
│   └── <theme-id>/
├── vscode/
│   └── <theme-id>/
├── tools/
│   ├── agents/
│   ├── chrome/
│   └── image-processing/
├── .agents/
│   ├── agents/
│   ├── rules/
│   ├── skills/
│   └── workflows/
├── .claude/
│   ├── agents/
│   ├── skills/
│   └── settings.json
├── docs/
│   └── agents/
├── templates/
│   ├── chrome-theme/
│   └── vscode-theme/
├── AGENTS.md
├── CLAUDE.md
├── GEMINI.md
└── dist/
```

## Current themes

| App | Theme | Version | Path |
| --- | --- | --- | --- |
| Chrome | BMO Pixel Night | 1.0.3 | `chrome/bmo-pixel-night` |

## Validate a Chrome theme

```bash
python3 tools/chrome/validate_theme.py chrome/bmo-pixel-night
```

Validation and ZIP packaging use only the Python standard library

Development dependencies are required only for the image resizing tool

```bash
python3 -m pip install -r requirements-dev.txt
```

## Package a Chrome theme

```bash
python3 tools/chrome/build_theme.py \
  chrome/bmo-pixel-night \
  --output dist/chrome/bmo-pixel-night-v1.0.3.zip
```

Distribution files are generated under `dist/` and excluded from Git

## AI agent setup

Codex, Claude Code, and Google Antigravity share the same repository rules and theme workflow

```bash
python3 tools/agents/validate_setup.py
```

The shared contract lives in `AGENTS.md`, and the shared theme skill lives in `.agents/skills/theme-workflow/SKILL.md`

See [Multi-agent setup](docs/agents/README.md) for tool-specific discovery paths and synchronization details

## Version and tag conventions

- Manage each theme's version and changelog independently inside its theme directory
- Use `<app>-<theme-id>-v<version>` for release tags
- Example: `chrome-bmo-pixel-night-v1.0.3`

## Rights and distribution

Code and artwork may have different rights restrictions, so review [RIGHTS.md](RIGHTS.md) before any public release

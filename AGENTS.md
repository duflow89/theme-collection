# Repository agent instructions

These instructions apply to the entire repository. Platform or theme-specific documentation may add constraints, but it must not weaken this contract.

## Repository model

- This is an app-first collection of independent themes
- Keep each theme under `<app>/<theme-id>/`
- Do not assume that a theme must have Chrome, VS Code, or other platform variants
- Treat every theme as its own package with independent metadata, assets, version, changelog, and release history
- Use lowercase kebab-case for app and theme directory names

## Language policy

- Keep all repository files and committed content in English, including source code, comments, documentation, metadata, changelogs, marketplace copy, filenames, and text embedded in images
- Do not add translated variants or non-English localized content unless the user explicitly changes this repository policy
- Communicate with the user in Korean unless the user explicitly requests another language

## Before changing files

1. Run `git status --short --branch` and preserve unrelated user changes
2. Read the root `README.md`, the target app README, the target theme README, and `RIGHTS.md`
3. Inspect the target package metadata, changelog, catalog entry, and existing validation tools
4. Confirm the exact app, theme ID, requested output, and release scope from repository context
5. If any of those are genuinely ambiguous and would change the result, stop and report the blocker instead of inventing a structure

## Asset and metadata rules

- Keep editable or generated source artwork separate from runtime assets and marketplace assets
- Do not overwrite original artwork when producing resized, converted, or optimized derivatives
- Preserve deliberate pixel-art hard edges; use nearest-neighbor scaling when resizing pixel art unless the theme documentation says otherwise
- Keep manifest or package references relative and inside the theme directory
- Update a theme version only when the distributable package changes
- When a version changes, update the package metadata, theme README, `CHANGELOG.md`, root catalog, and release examples together
- Keep marketplace listing text and images with the theme when the platform supports them
- Check image dimensions, color mode, transparency restrictions, and referenced paths before packaging

## Chrome themes

- Read `chrome/README.md` and the target theme README before editing
- Start new Chrome theme packages from `templates/chrome-theme/`
- Keep a theme-specific `INSTALL.md` beside each Chrome manifest and link it from the theme README with the standalone Markdown line `[Install locally](INSTALL.md)`
- Embed the exact image referenced by `theme.images.theme_ntp_background` as a standalone Markdown image with alt text in the form `<Theme Name> New Tab background`
- Validate with `python3 tools/chrome/validate_theme.py chrome/<theme-id>`
- Build only when requested, using `python3 tools/chrome/build_theme.py chrome/<theme-id> --output dist/chrome/<theme-id>-v<version>.zip`
- A Chrome distribution ZIP contains only `manifest.json` and resources referenced by the manifest
- Keep source artwork, listing copy, screenshots, and unrelated store assets out of the distribution ZIP unless referenced by the manifest
- Chrome theme backgrounds do not support CSS `cover` or `contain`; use supported manifest alignment and repetition properties and document visual limitations honestly

## Other platforms

- Read the app README and template before creating a theme
- Follow the current official package format for that platform; do not copy Chrome metadata into another app package
- If the repository has no implemented theme or validator for the target platform, establish the minimal template and validation contract before adding release files

## Validation and review

- Run the narrowest relevant validator after each material change
- After changing agent configuration, run `python3 tools/agents/validate_setup.py`
- Before handoff, verify that tracked text and image assets contain no non-English localized copy
- Before handoff, inspect `git diff --check`, `git status --short`, and the final diff
- Report the exact commands run and whether they passed
- Keep implementation completion separate from human rights review, marketplace submission, publication, or approval

## Safety and release boundaries

- Never commit credentials, API keys, signing keys, certificates, `.env` files, local agent settings, caches, or generated distribution archives
- Do not weaken `.gitignore` protections for `dist/`, `*.pem`, `*.crx`, or `*.vsix`
- Do not commit, push, tag, publish, upload to a marketplace, or change a remote repository unless the user explicitly requests that action
- Do not claim third-party characters, trademarks, or artwork are officially affiliated or licensed without evidence
- Review `RIGHTS.md` before any public release and preserve unofficial fan-work disclosures where applicable

## Multi-agent configuration

- `AGENTS.md` is the canonical repository instruction file
- `CLAUDE.md` and `.agents/rules/repository.md` must continue to import this file rather than duplicate it
- `GEMINI.md` is an Antigravity routing adapter and must point to this contract and the workspace rule without importing the contract a second time
- `.agents/skills/theme-workflow/SKILL.md` is the canonical cross-tool theme skill
- `.claude/skills/theme-workflow/SKILL.md` mirrors that skill for Claude Code versions that do not discover project skills from `.agents/skills/`
- When the canonical skill changes, update the Claude mirror in the same commit and run the agent setup validator

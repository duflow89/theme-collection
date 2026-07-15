---
name: theme-workflow
description: Create, modify, validate, package, or prepare the release of an app-specific theme in this repository. Use for Chrome, VS Code, or another platform theme, including runtime assets, marketplace assets, listing metadata, versions, and changelogs.
---

# Theme workflow

Use this workflow for one independent theme under `<app>/<theme-id>/`.

## 1. Establish scope

1. Read `AGENTS.md`, `README.md`, `RIGHTS.md`, the app README, and the target theme README; for Chrome, also read the target `INSTALL.md`
2. Inspect `git status --short --branch` and preserve unrelated changes
3. Identify the exact app, theme ID, requested output, current version, and whether the user requested packaging or publishing
4. Do not create matching variants for other apps unless the user explicitly asks for them

## 2. Implement

1. Reuse the app template and repository tools where available
2. Keep original or editable artwork under the theme's source asset area
3. Put only runtime resources referenced by package metadata in the runtime asset area
4. Keep marketplace icons, screenshots, promotional images, and listing copy in their dedicated store or listing areas
5. Use relative package paths that remain inside the theme directory
6. Preserve pixel-art edges with nearest-neighbor scaling unless the theme documentation specifies another method
7. For Chrome, start new packages from `templates/chrome-theme/`
8. For Chrome, embed the exact `theme.images.theme_ntp_background` runtime image as a standalone Markdown image with alt text in the form `<Theme Name> New Tab background`
9. For Chrome, keep a theme-specific `INSTALL.md` beside the manifest and link it from the theme README with the standalone Markdown line `[Install locally](INSTALL.md)`

## 3. Synchronize release metadata

When the distributable package changes:

1. Choose the next version according to the package's existing version scheme
2. Update the manifest or package metadata
3. Update the theme README and `CHANGELOG.md`
4. Update `catalog.json` and root documentation when they show the version
5. Keep app-specific release tags in the form `<app>-<theme-id>-v<version>`

Documentation-only and agent-configuration-only changes do not require a theme version bump.

## 4. Validate

For Chrome:

```bash
python3 tools/chrome/validate_theme.py chrome/<theme-id>
```

The Chrome validator must pass the manifest, runtime assets, README background preview, README installation link, and installation-guide checks.

When packaging was requested:

```bash
python3 tools/chrome/build_theme.py \
  chrome/<theme-id> \
  --output dist/chrome/<theme-id>-v<version>.zip
```

For another app, use its repository validator. If none exists, validate the official package schema and add a repeatable local validator before treating the package as release-ready.

Always finish with:

```bash
python3 tools/agents/validate_setup.py
git diff --check
git status --short
```

## 5. Review and handoff

- Inspect the final diff, documentation links and previews, and package contents
- Report commands and results, changed version if any, and generated artifact paths
- Keep rights review, store submission, publication, remote pushes, and human approval as explicit separate gates
- Do not commit or publish unless the user requested it

## Never include

- Credentials, API keys, `.env` files, certificates, or signing keys
- Local agent settings or memory
- Caches and compiled Python files
- `dist/`, CRX, VSIX, or other generated release archives in Git

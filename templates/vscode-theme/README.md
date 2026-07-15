<div align="center">

# VS Code Theme Template

**A starting contract for the collection's first independent VS Code theme**

[VS Code themes](../../vscode/README.md) · [Repository home](../../README.md) · [Repository contract](../../AGENTS.md)

</div>

---

## Status

The repository does not yet contain an implemented VS Code theme or validator. Establish both against the current official package format before preparing release files

## Planned package shape

```text
vscode/<theme-id>/
├── package.json
├── README.md
├── CHANGELOG.md
├── themes/
│   └── <theme-id>-color-theme.json
└── marketplace-assets/
```

Keep the app package native to VS Code. Do not copy Chrome manifests, background-image rules, store metadata, or versions into this structure

## README design

A finished theme README should include

- A clear title, one-line concept, and marketplace-ready preview
- Theme version and supported VS Code range
- Installation and activation steps
- A concise palette or syntax-highlight overview
- Package structure and development commands
- Accessibility considerations and known limitations
- Rights and distribution notes

## First-theme checklist

1. Confirm the current official VS Code theme-extension schema
2. Add the minimal package and color-theme files
3. Create a repeatable repository validator
4. Keep editable artwork separate from marketplace assets
5. Document packaging without committing generated `.vsix` archives
6. Update the root catalog and [VS Code index](../../vscode/README.md)

> [!IMPORTANT]
> Do not treat the first theme as release-ready until package validation, visual review, rights review, and marketplace preparation are complete

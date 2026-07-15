<div align="center">

# VS Code Themes

**A reserved home for future editor themes in the collection**

[Theme Collection](../README.md) · [VS Code theme template](../templates/vscode-theme/README.md) · [Rights](../RIGHTS.md)

</div>

---

> [!NOTE]
> No VS Code themes are available yet. This directory defines the boundary for the first implementation without pretending that a package or validator already exists

## Planned structure

```text
<theme-id>/
├── package.json
├── README.md
├── CHANGELOG.md
├── themes/
│   └── <theme-id>-color-theme.json
└── marketplace-assets/
```

## Platform principles

| Principle | Requirement |
| --- | --- |
| Native format | Follow the current official VS Code extension schema |
| Independent identity | Own name, metadata, assets, version, changelog, and release history |
| No forced variants | Do not inherit artwork or colors from a Chrome theme without an explicit request |
| Repeatable validation | Add a local validator before release files are considered ready |
| Safe packaging | Keep generated `.vsix` archives, credentials, and publishing secrets out of Git |

## Implement the first theme

1. Start with the [VS Code theme template](../templates/vscode-theme/README.md)
2. Verify the current official package format
3. Add the minimal theme and marketplace assets
4. Establish a repeatable validator and document its command here
5. Add the theme to the root catalog only after the package exists

Marketplace submission, rights approval, publication, and human visual review remain separate release gates

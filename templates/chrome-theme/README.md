<div align="center">

# Chrome Theme Template

**The package and documentation contract for every new Chrome theme**

[Chrome themes](../../chrome/README.md) · [Repository contract](../../AGENTS.md) · [Theme workflow](../../.agents/skills/theme-workflow/SKILL.md)

</div>

---

## Start a theme

1. Create `chrome/<theme-id>/` using lowercase kebab-case
2. Add the package structure below
3. Replace every placeholder with theme-specific English content
4. Keep source, runtime, and marketplace assets in their designated directories
5. Validate before packaging

```text
chrome/<theme-id>/
├── manifest.json
├── README.md
├── INSTALL.md
├── CHANGELOG.md
├── images/
├── assets/source/
├── store-assets/
└── listing/
```

Use an existing theme for the full package shape, but do not copy its character names, artwork, palette, version, listing copy, or rights claims

## Required README contract

Every theme README should be visually useful before it becomes operational documentation

1. Lead with the theme name and one-line concept
2. Embed the exact file referenced by `theme.images.theme_ntp_background`
3. Use preview alt text in the exact form `<Theme Name> New Tab background`
4. Link the theme's own `INSTALL.md`
5. Show version, canvas, alignment, palette, and access details
6. Document validation, packaging, display limitations, and rights

Use this minimum pattern and expand it to match the current theme READMEs

```md
# <Theme Name>

<One-line English description>

[Install locally](INSTALL.md)

## Preview

![<Theme Name> New Tab background](images/<manifest-background-file>.png)

## At a glance

| Detail | Value |
| --- | --- |
| Version | `<version>` |
| Background | `<width>×<height>` RGB PNG |
| Placement | `<alignment>` · `<repeat>` |
| Access | No scripts, permissions, tracking, or data collection |
```

The README preview path must exactly match the manifest background path. The validator rejects source-artwork or marketplace-image substitutes

## Required installation guide

Copy and customize [the installation template](INSTALL.md). The finished guide must include

- `chrome://extensions`
- **Developer mode** and **Load unpacked** steps
- Repository-folder and extracted-ZIP paths
- A reminder to select the directory containing `manifest.json`
- Update, removal, and troubleshooting guidance
- Theme-specific background behavior
- Links to official Chrome documentation

## Build boundaries

Only `manifest.json` and manifest-referenced resources belong in a distribution ZIP. Keep these outside the archive unless the manifest explicitly references them

- Source artwork
- README and installation documentation
- Marketplace screenshots and promotional images
- Listing copy
- Local settings, credentials, signing keys, caches, and existing archives

## Validate and package

Run from the repository root

```bash
python3 tools/chrome/validate_theme.py chrome/<theme-id>
```

Package only when requested

```bash
python3 tools/chrome/build_theme.py \
  chrome/<theme-id> \
  --output dist/chrome/<theme-id>-v<version>.zip
```

> [!NOTE]
> Documentation-only changes do not require a theme version bump. If the distributable package changes, synchronize the manifest, theme README, changelog, root catalog, and release examples

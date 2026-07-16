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
│   ├── store-icon-128.png
│   ├── screenshot-1280x800.png
│   ├── promo-small-440x280.png
│   └── promo-marquee-1400x560.png
└── listing/
    ├── summary-en.txt
    ├── description-en.md
    └── store-listing-en.md
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

## Required Chrome Web Store listing

Every theme should be ready for the Chrome Web Store dashboard before it is treated as complete

| Path | Content |
| --- | --- |
| `listing/summary-en.txt` | One plain-text summary that matches the manifest description and stays within 132 characters |
| `listing/description-en.md` | A concise overview, feature list, access or data statement, and any required rights disclosure |
| `listing/store-listing-en.md` | Paste-ready title, category, language, copy references, and an upload map for graphical assets |
| `store-assets/store-icon-128.png` | `128×128` PNG store icon |
| `store-assets/screenshot-1280x800.png` | Full-bleed `1280×800` RGB PNG showing the current installed theme experience |
| `store-assets/promo-small-440x280.png` | Full-bleed `440×280` RGB PNG promotional tile without text |
| `store-assets/promo-marquee-1400x560.png` | Full-bleed `1400×560` RGB PNG marquee image without text |

Keep generated or editable source images under `assets/source/`. Store assets should accurately represent the current theme, remain legible when reduced, use square corners, and avoid badges, claims, watermarks, or unnecessary text

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

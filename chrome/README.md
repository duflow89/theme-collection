<div align="center">

# Chrome Themes

**New Tab artwork and browser colors, packaged as independent Manifest V3 themes**

[Theme Collection](../README.md) · [Chrome theme template](../templates/chrome-theme/README.md) · [Rights](../RIGHTS.md)

</div>

---

## Gallery

### [BMO Pixel Night](bmo-pixel-night/README.md) · `v1.0.4`

[![BMO Pixel Night New Tab background](bmo-pixel-night/images/theme_ntp_background_fhd.png)](bmo-pixel-night/README.md)

Deep navy frames, mint accents, and a cozy pixel-art night scene

[Install locally](bmo-pixel-night/INSTALL.md) · [Chrome Web Store](https://chromewebstore.google.com/detail/bmo-pixel-night/fabbpacoihgbjmpbkpjikpciifepnbfj)

### [Brushbug Cozy Night](brushbug-cozy-night/README.md) · `v1.0.1`

[![Brushbug Cozy Night New Tab background](brushbug-cozy-night/images/theme_ntp_background_fhd.png)](brushbug-cozy-night/README.md)

Midnight browser chrome, warm amber accents, and a quiet atelier after dark

[Install locally](brushbug-cozy-night/INSTALL.md)

## Install a theme locally

Each theme includes its own `INSTALL.md` with source and extracted-ZIP instructions. Local themes use Chrome's **Developer mode** and **Load unpacked** workflow

> [!IMPORTANT]
> Only load unpacked themes from sources you trust. Select the directory that contains `manifest.json`, not the ZIP file itself

Choose a theme above and follow its installation guide

## Package contract

Every Chrome theme is self-contained

```text
<theme-id>/
├── manifest.json          # Package metadata, colors, and runtime asset paths
├── README.md              # Theme overview with the exact runtime background preview
├── INSTALL.md             # Local installation, removal, and troubleshooting
├── images/                # Runtime images referenced by the manifest
├── assets/source/         # Editable or generated source artwork
├── store-assets/          # Marketplace icons, screenshots, and promotional images
├── listing/               # Marketplace copy
└── CHANGELOG.md           # Theme-specific release history
```

The distribution ZIP contains only `manifest.json` and resources referenced by the manifest

## Documentation standard

Every current and future Chrome theme must meet the same documentation contract

- Embed the exact image referenced by `theme.images.theme_ntp_background` as a standalone Markdown image
- Use alt text in the form `<Theme Name> New Tab background`
- Keep a theme-specific `INSTALL.md` beside the manifest
- Link `INSTALL.md` from the theme README with the standalone Markdown line `[Install locally](INSTALL.md)`
- Document background alignment and Chrome's sizing limitations honestly
- Keep all committed documentation and embedded image text in English

The Chrome validator enforces the preview and installation requirements

## Create or update a theme

1. Start with the [Chrome theme template](../templates/chrome-theme/README.md)
2. Keep source artwork separate from `images/`
3. Point `manifest.json` only to runtime and required package assets
4. Update the theme's version, README, changelog, and root catalog together when the distributable package changes
5. Run the theme validator

```bash
python3 tools/chrome/validate_theme.py chrome/<theme-id>
```

Package only when a release artifact is requested

```bash
python3 tools/chrome/build_theme.py \
  chrome/<theme-id> \
  --output dist/chrome/<theme-id>-v<version>.zip
```

> [!NOTE]
> The Chrome theme manifest provides alignment and repeat controls, but no background-sizing property such as CSS `cover` or `contain`. The visible crop can vary with window size, display scale, and browser zoom

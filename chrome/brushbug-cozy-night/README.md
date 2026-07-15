<p align="center">
  <img src="store-assets/store-icon-128.png" alt="Brushbug Cozy Night icon" width="96">
</p>

<h1 align="center">Brushbug Cozy Night</h1>

<p align="center"><strong>A dark and cozy Chrome fan theme inspired by the brushbug from <em>Witch Hat Atelier</em></strong></p>

<p align="center">
  <a href="INSTALL.md">Install locally</a> ·
  <a href="../README.md">All Chrome themes</a>
</p>

---

## Preview

![Brushbug Cozy Night New Tab background](images/theme_ntp_background_fhd.png)

<p align="center"><sub>The exact 1920×1080 runtime background referenced by the theme manifest</sub></p>

## At a glance

| Detail | Value |
| --- | --- |
| Version | `1.0.1` |
| Package | Chrome theme · Manifest V3 |
| Background | `1920×1080` RGB PNG |
| Placement | Bottom center · no repeat |
| Palette | Midnight navy frames · warm amber accents |
| Access | No scripts, permissions, tracking, or data collection |

## Experience

- A candlelit atelier scene composed for Chrome's New Tab page
- Midnight browser frames that recede into the artwork
- Warm cream text and amber controls inspired by lamplight
- A `128×128` icon included in the package manifest

## Installation

[Install locally](INSTALL.md)

The local guide covers loading the theme from this repository or an extracted release ZIP

## Package map

| Path | Purpose |
| --- | --- |
| `manifest.json` | Theme metadata, colors, and runtime asset references |
| `images/` | Runtime background loaded by Chrome |
| `assets/source/` | Original generated artwork and source crops |
| `store-assets/` | Chrome Web Store icon |
| `listing/` | Chrome Web Store summary and description |
| `INSTALL.md` | Local installation, removal, and troubleshooting |
| `CHANGELOG.md` | Theme-specific release history |

## Validate and package

Run commands from the repository root

```bash
python3 tools/chrome/validate_theme.py chrome/brushbug-cozy-night
```

```bash
python3 tools/chrome/build_theme.py \
  chrome/brushbug-cozy-night \
  --output dist/chrome/brushbug-cozy-night-v1.0.1.zip
```

> [!NOTE]
> The Chrome theme manifest provides alignment and repeat controls, but no background-sizing property such as CSS `cover` or `contain`. The visible area can vary with window size, display scale, and browser zoom

## Distribution and rights

This is an unofficial fan-made theme. It is not affiliated with, sponsored by, or endorsed by the original creators or rights holders. Related character names and intellectual property belong to their respective owners

Review the repository [rights and distribution notice](../../RIGHTS.md) before redistributing the artwork or applying a repository-wide license

<p align="center">
  <img src="store-assets/store-icon-128.png" alt="BMO Pixel Night icon" width="96">
</p>

<h1 align="center">BMO Pixel Night</h1>

<p align="center"><strong>A cozy 2D pixel-art Chrome fan theme inspired by BMO</strong></p>

<p align="center">
  <a href="INSTALL.md">Install locally</a> ·
  <a href="https://chromewebstore.google.com/detail/bmo-pixel-night/fabbpacoihgbjmpbkpjikpciifepnbfj">Chrome Web Store</a> ·
  <a href="../README.md">All Chrome themes</a>
</p>

---

## Preview

![BMO Pixel Night New Tab background](images/theme_ntp_background_fhd.png)

<p align="center"><sub>The exact 1920×1080 runtime background referenced by the theme manifest</sub></p>

## At a glance

| Detail | Value |
| --- | --- |
| Version | `1.0.4` |
| Package | Chrome theme · Manifest V3 |
| Background | `1920×1080` RGB PNG |
| Placement | Bottom center · no repeat |
| Palette | Deep navy frames · BMO-inspired mint accents |
| Access | No scripts, permissions, tracking, or data collection |

## Experience

- A quiet pixel-art room designed around the open space of Chrome's New Tab page
- Dark browser frames that keep tabs and controls visually connected to the scene
- Warm cream text and mint accents for readable, character-inspired contrast
- A `128×128` icon included in the package manifest

## Installation

[Install locally](INSTALL.md)

Choose the published [Chrome Web Store release](https://chromewebstore.google.com/detail/bmo-pixel-night/fabbpacoihgbjmpbkpjikpciifepnbfj) for normal updates. The local guide covers loading the theme from this repository or an extracted release ZIP

The Store listing version may lag behind the repository version until an update is reviewed and published

## Package map

| Path | Purpose |
| --- | --- |
| `manifest.json` | Theme metadata, colors, and runtime asset references |
| `images/` | Runtime background loaded by Chrome |
| `assets/source/` | Original generated artwork |
| `store-assets/` | Store icon, screenshot, and promotional images |
| `listing/` | Chrome Web Store summary and description |
| `INSTALL.md` | Local installation, removal, and troubleshooting |
| `CHANGELOG.md` | Theme-specific release history |

## Validate and package

Run commands from the repository root

```bash
python3 tools/chrome/validate_theme.py chrome/bmo-pixel-night
```

```bash
python3 tools/chrome/build_theme.py \
  chrome/bmo-pixel-night \
  --output dist/chrome/bmo-pixel-night-v1.0.4.zip
```

> [!NOTE]
> The Chrome theme manifest provides alignment and repeat controls, but no background-sizing property such as CSS `cover` or `contain`. The visible area can vary with window size, display scale, and browser zoom

## Distribution and rights

This is an unofficial fan-made theme. It is not affiliated with, sponsored by, or endorsed by the original creators or rights holders. Related character names and intellectual property belong to their respective owners

Chrome Web Store publication and public repository availability are separate distribution surfaces. Neither represents copyright clearance, affiliation, or an open-source license for third-party character elements

Review the repository [rights and distribution notice](../../RIGHTS.md) before redistributing the artwork or applying a repository-wide license

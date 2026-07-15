# BMO Pixel Night

An unofficial 2D pixel-art Chrome fan theme inspired by BMO

## Current version

`1.0.3`

## Distribution

Published releases of the theme are available from the [Chrome Web Store](https://chromewebstore.google.com/detail/bmo-pixel-night/fabbpacoihgbjmpbkpjikpciifepnbfj). The Store listing version may lag behind the repository version until an update is submitted and published

Chrome Web Store publication and public repository availability are separate distribution surfaces. Neither publication status represents copyright clearance, sponsorship, endorsement, affiliation, or an open-source license for third-party character elements

## Key settings

- `2560×1440` RGB PNG New Tab background
- Bottom-center alignment
- No background repetition
- Navy frame colors with BMO-inspired mint accents
- `128×128` store icon declared in the manifest
- No scripts, permissions, or data collection

## Directories

- `assets/source`: original generated artwork
- `images`: runtime images referenced by the Chrome theme
- `store-assets`: Chrome Web Store icon, screenshot, and promotional tiles
- `listing`: Chrome Web Store listing copy

## Validation

Run from the repository root

```bash
python3 tools/chrome/validate_theme.py chrome/bmo-pixel-night
```

## Packaging

```bash
python3 tools/chrome/build_theme.py \
  chrome/bmo-pixel-night \
  --output dist/chrome/bmo-pixel-night-v1.0.3.zip
```

## Display limitations

Chrome displays theme backgrounds with `size: initial`, so the visible area can vary with the browser window size and zoom level

## Rights notice

This is an unofficial fan-made theme. It is not affiliated with, sponsored by, or endorsed by the original creators or rights holders. Related character names and intellectual property belong to their respective owners

See the repository [rights and distribution notice](../../RIGHTS.md) before redistributing the artwork or applying a repository-wide license

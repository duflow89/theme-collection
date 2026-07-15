# BMO Pixel Night

An unofficial 2D pixel-art Chrome fan theme inspired by BMO

## Current version

`1.0.3`

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

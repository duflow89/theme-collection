# Brushbug Cozy Night

An unofficial dark and cozy Chrome fan theme inspired by the brushbug from *Witch Hat Atelier*

## Current version

`1.0.0`

## Key settings

- `2560×1440` RGB PNG New Tab background
- Bottom-center alignment
- No background repetition
- Midnight navy browser frames with warm amber accents
- `128×128` store icon declared in the manifest
- No scripts, permissions, or data collection

## Directories

- `assets/source`: original generated artwork and source crops
- `images`: runtime images referenced by the Chrome theme
- `store-assets`: Chrome Web Store icon
- `listing`: Chrome Web Store listing copy

## Validation

Run from the repository root

```bash
python3 tools/chrome/validate_theme.py chrome/brushbug-cozy-night
```

## Packaging

```bash
python3 tools/chrome/build_theme.py \
  chrome/brushbug-cozy-night \
  --output dist/chrome/brushbug-cozy-night-v1.0.0.zip
```

## Display limitations

Chrome displays theme backgrounds with `size: initial`, so the visible area can vary with the browser window size and zoom level

## Rights notice

This is an unofficial fan-made theme. It is not affiliated with, sponsored by, or endorsed by the original creators or rights holders. Related character names and intellectual property belong to their respective owners

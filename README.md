<div align="center">

# Theme Collection

**Independent visual themes, thoughtfully packaged for each app**

An app-first collection where every theme keeps its artwork, metadata, documentation, version, and release history together

[Explore Chrome themes](chrome/README.md) · [Author a theme](templates/chrome-theme/README.md) · [Agent setup](docs/agents/README.md) · [Rights](RIGHTS.md)

</div>

---

## Theme gallery

| Preview | Theme |
| :---: | --- |
| <img src="chrome/bmo-pixel-night/images/theme_ntp_background_fhd.png" alt="BMO Pixel Night background" width="360"> | **[BMO Pixel Night](chrome/bmo-pixel-night/README.md)**<br>`Chrome` · `v1.0.4`<br>An unofficial 2D pixel-art fan theme with deep navy frames and mint accents<br>[Install locally](chrome/bmo-pixel-night/INSTALL.md) · [Chrome Web Store](https://chromewebstore.google.com/detail/bmo-pixel-night/fabbpacoihgbjmpbkpjikpciifepnbfj) |
| <img src="chrome/brushbug-cozy-night/images/theme_ntp_background_qhd.png" alt="Brushbug Cozy Night background" width="360"> | **[Brushbug Cozy Night](chrome/brushbug-cozy-night/README.md)**<br>`Chrome` · `v1.0.0`<br>A dark atelier scene with midnight frames and warm amber accents<br>[Install locally](chrome/brushbug-cozy-night/INSTALL.md) |

## Collection model

Themes are organized by app and released independently. A theme never needs a matching variant for another platform

```text
theme-collection/
├── chrome/
│   └── <theme-id>/
│       ├── README.md
│       ├── INSTALL.md
│       ├── manifest.json
│       ├── images/
│       ├── assets/source/
│       ├── store-assets/
│       ├── listing/
│       └── CHANGELOG.md
├── vscode/
│   └── <theme-id>/
├── templates/
├── tools/
└── docs/agents/
```

| Principle | What it means |
| --- | --- |
| App-first | Each package follows its platform's native format |
| Independent releases | Versions and changelogs advance per theme |
| Clear asset boundaries | Source artwork, runtime files, and marketplace assets stay separate |
| Honest distribution | Rights review, publication, and approval remain explicit human gates |

## Developer workflow

Start from the relevant app template, keep the runtime package minimal, and validate before packaging

### Validate a Chrome theme

```bash
python3 tools/chrome/validate_theme.py chrome/bmo-pixel-night
```

The validator checks manifest data, referenced assets, image metadata, and the required README preview and installation guide

### Package a Chrome theme

```bash
python3 tools/chrome/build_theme.py \
  chrome/bmo-pixel-night \
  --output dist/chrome/bmo-pixel-night-v1.0.4.zip
```

Distribution archives contain only `manifest.json` and resources referenced by the manifest. Generated files stay under `dist/` and are excluded from Git

Validation and packaging use only the Python standard library. The image resizing tool has separate development dependencies

```bash
python3 -m pip install -r requirements-dev.txt
```

## Agent-aware repository

Codex, Claude Code, and Google Antigravity share the repository contract in `AGENTS.md` and the theme workflow in `.agents/skills/theme-workflow/SKILL.md`

```bash
python3 tools/agents/validate_setup.py
```

See [Multi-agent setup](docs/agents/README.md) for discovery paths, compatibility adapters, and safety boundaries

## Releases and rights

- Version every theme independently
- Use `<app>-<theme-id>-v<version>` for release tags
- Example: `chrome-bmo-pixel-night-v1.0.4`
- Review [RIGHTS.md](RIGHTS.md) before any public release or redistribution

Artwork and repository tooling may have different rights restrictions. Public availability does not imply an open-source license, copyright clearance, sponsorship, or endorsement

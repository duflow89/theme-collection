<p align="center">
  <img src="store-assets/store-icon-128.png" alt="Mandu Blue Sky icon" width="96">
</p>

<h1 align="center">Mandu Blue Sky</h1>

<p align="center"><strong>A golden pixel-art dumpling, red glasses, and a very blue sky</strong></p>

[Install locally](INSTALL.md)

## Preview

![Mandu Blue Sky New Tab background](images/theme_ntp_background_fhd.png)

The exact, unmodified original artwork referenced by the manifest; the local file was supplied by the user

## Artwork credit

Original artwork by **Ankyung Mandoo** (`@ankyungmandoo_`)

- [Creator's Instagram](https://www.instagram.com/ankyungmandoo_/)
- [Creator's Naver Blog](https://blog.naver.com/3qks3qks)

The creator attribution and links were supplied by the user. The browser theme packaging and generated icon and promotional derivatives are separate contributions based on this original artwork

## At a glance

| Detail | Value |
| --- | --- |
| Version | `1.0.0` |
| Package | Chrome theme · Manifest V3 |
| Background | `1920×1080` RGBA PNG |
| Placement | Top right · no repeat · native image size |
| Palette | Sky-blue frames · cloud-white toolbar · deep-blue controls |
| Access | No scripts, permissions, tracking, or data collection |
| Availability | Source package; no Chrome Web Store release |

## Experience

- The original blue-sky and green-hill artwork, with the giant golden character wearing red glasses
- Soft blue inactive tabs and a cloud-white active tab and toolbar
- A pale-blue address bar with dark, readable text and controls
- Top-right alignment to keep the character visible on common desktop windows

Chrome does not scale theme backgrounds to fit the window. Narrow or short windows can crop the artwork; windows larger than the image reveal the sky-blue fallback color. The manifest supports alignment and repetition, but no CSS `cover` or `contain` sizing. Display scale and browser zoom can also affect the visible area

## Chrome Web Store assets

![Mandu Blue Sky Chrome Web Store screenshot](store-assets/screenshot-1280x800.png)

| Asset | Preview |
| --- | --- |
| Small promotional tile · `440×280` | ![Mandu Blue Sky small promotional tile](store-assets/promo-small-440x280.png) |
| Marquee image · `1400×560` | ![Mandu Blue Sky marquee image](store-assets/promo-marquee-1400x560.png) |

The [dashboard field sheet](listing/store-listing-en.md) includes English listing copy and the image upload map. Promotional illustrations are separate compositions derived from the source artwork; the runtime background remains unchanged

## Package map

| Path | Purpose |
| --- | --- |
| `manifest.json` | Metadata, browser colors, background and icon references |
| `images/` | Original-size runtime background |
| `assets/source/` | Preserved original, generated artwork, and production notes |
| `store-assets/` | Icon, installed-theme screenshot, and promotional images |
| `listing/` | English marketplace copy and dashboard guidance |
| `INSTALL.md` | Local installation, removal, and troubleshooting |
| `CHANGELOG.md` | Theme-specific version history |

## Validate and package

Run from the repository root

```bash
python3 tools/chrome/validate_theme.py chrome/mandu-blue-sky
```

Build only when a distribution archive is requested

```bash
python3 tools/chrome/build_theme.py \
  chrome/mandu-blue-sky \
  --output dist/chrome/mandu-blue-sky-v1.0.0.zip
```

Release tag: `chrome-mandu-blue-sky-v1.0.0`

The archive includes only the manifest, its background, and its referenced icon

## Artwork and distribution

This is an unofficial theme based on the work credited in [Artwork credit](#artwork-credit). The original artwork and character belong to their respective creator and rights holders; the theme maintainer does not claim authorship of them. No affiliation, sponsorship, endorsement, or license from the creator or other rights holders is claimed

Attribution does not establish permission to redistribute the original artwork or its derivatives. A redistribution license has not been recorded, and any separate rights in the photographic landscape still require confirmation

Review [RIGHTS.md](../../RIGHTS.md) before public distribution. Preparing the package and listing does not constitute a rights review, marketplace submission, or publication

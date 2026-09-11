<p align="center">
  <img src="store-assets/store-icon-128.png" alt="안경만두의 파란 하늘 icon" width="96">
</p>

<h1 align="center">안경만두의 파란 하늘</h1>

<p align="center"><strong>파란 하늘과 초록 언덕 위로 떠오른 안경만두의 원작 이미지를 담은 비공식 크롬 테마</strong></p>

[Install locally](INSTALL.md)

## Preview

![안경만두의 파란 하늘 New Tab background](images/theme_ntp_background_fhd.png)

The exact, unmodified original artwork referenced by the manifest; the local file was supplied by the user

## Artwork credit

Original artwork by **Ankyung Mandoo** (`@ankyungmandoo_`)

- [Creator's Instagram](https://www.instagram.com/ankyungmandoo_/)
- [Creator's Naver Blog](https://blog.naver.com/3qks3qks)

The creator attribution and links were supplied by the user. The browser theme packaging and generated icon and promotional derivatives are separate contributions based on this original artwork

## At a glance

| Detail | Value |
| --- | --- |
| Version | `1.0.1` |
| Package | Chrome theme · Manifest V3 |
| Listing language | Korean (`ko`), as requested by the user |
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

![안경만두의 파란 하늘 full-browser mockup](store-assets/screenshot-1280x800.png)

The store screenshot is a generated full-browser mockup showing the sky-blue tab strip, cloud-white toolbar, pale-blue address bar, and Korean New Tab interface. It illustrates the theme's appearance; the original page-only captures remain in `assets/source/`

| Asset | Preview |
| --- | --- |
| Small promotional tile · `440×280` | ![안경만두의 파란 하늘 small promotional tile](store-assets/promo-small-440x280.png) |
| Marquee image · `1400×560` | ![안경만두의 파란 하늘 marquee image](store-assets/promo-marquee-1400x560.png) |

The [dashboard field sheet](listing/store-listing-ko.md) includes Korean listing copy and the image upload map. Promotional illustrations are separate compositions derived from the source artwork; the runtime background remains unchanged

## Korean store listing

Use version `1.0.1` to update the package name and summary in the existing dashboard draft. Paste [the Korean description](listing/description-ko.md) into the description field and select **Korean** as the listing language. The ZIP does not fill these dashboard fields automatically

The mockup uses Korean browser labels. Chrome controls use the browser's language settings; installing this theme does not change the browser language

## Package map

| Path | Purpose |
| --- | --- |
| `manifest.json` | Metadata, browser colors, background and icon references |
| `images/` | Original-size runtime background |
| `assets/source/` | Preserved original, generated artwork, and production notes |
| `store-assets/` | Icon, full-browser store mockup, and promotional images |
| `listing/` | Korean marketplace copy and dashboard guidance |
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
  --output dist/chrome/mandu-blue-sky-v1.0.1.zip
```

Release tag: `chrome-mandu-blue-sky-v1.0.1`

The archive includes only the manifest, its background, and its referenced icon

## Artwork and distribution

This is an unofficial theme based on the work credited in [Artwork credit](#artwork-credit). The original artwork and character belong to their respective creator and rights holders; the theme maintainer does not claim authorship of them. No affiliation, sponsorship, endorsement, or license from the creator or other rights holders is claimed

Attribution does not establish permission to redistribute the original artwork or its derivatives. A redistribution license has not been recorded, and any separate rights in the photographic landscape still require confirmation

Review [RIGHTS.md](../../RIGHTS.md) before public distribution. Preparing the package and listing does not constitute a rights review, marketplace submission, or publication

# Artwork provenance and production

## Original background

- Input: a local copy of the original artwork supplied by the user, stored with an English filename
- Preserved original: `mandu-blue-sky-original.png`
- Runtime copy: `../../images/theme_ntp_background_fhd.png`
- Dimensions: `1920×1080`, 8-bit RGBA PNG; every alpha value is 255
- SHA-256 for both copies: `d3f70521b3f975cc96a58fc664d88d649ecb994a30e725a8c771ac94622e78d7`
- The runtime file is byte-for-byte identical to the supplied image; no crop, resizing, recoloring, or regeneration was applied
- The image contains no embedded visible text
- Original creator: **Ankyung Mandoo** (`@ankyungmandoo_`), as identified by the user
- [Creator's Instagram](https://www.instagram.com/ankyungmandoo_/)
- [Creator's Naver Blog](https://blog.naver.com/3qks3qks)
- Attribution record: the user identified the original creator and supplied both profile links on 2026-09-11; direct automated retrieval of the profile contents was unavailable
- These are creator profile links, not a verified permalink to this specific image. No redistribution license has been recorded; any separate photographic landscape rights still require confirmation. See [RIGHTS.md](../../../../RIGHTS.md)

## Icon and promotional artwork

The following derivatives used the built-in image generation tool, with Ankyung Mandoo's credited original image as the sole edit reference. Generated source outputs are retained here. These are derived illustrations, not pixel-identical crops of the original, and are not presented as works created or endorsed by Ankyung Mandoo. The generated derivatives do not transfer authorship of the original artwork or character to the theme maintainer

| Source | Store export | Export method |
| --- | --- | --- |
| `store-icon-source.png` | `../../store-assets/store-icon-128.png` | Fit into 112×112 using nearest-neighbor scaling, then add 8 transparent pixels on every side |
| `promo-small-source.png` | `../../store-assets/promo-small-440x280.png` | Center crop to 11:7 and scale to 440×280 using nearest-neighbor scaling; RGB |
| `promo-marquee-source.png` | `../../store-assets/promo-marquee-1400x560.png` | Center crop to 5:2 and scale to 1400×560 using nearest-neighbor scaling; RGB |

Exact-size exports used the Sharp library in a temporary development environment outside the repository. Original source outputs were not overwritten. No generated text, branding, or badges were added

### Icon prompt

```text
Use case: background-extraction. Asset type: square Chrome theme icon. Create one 1024x1024 PNG icon on a genuinely transparent background using the supplied image as the edit target. Isolate the exact golden pixel-art dumpling character head with red rectangular glasses, black shiny eyes, the three small golden crown-like tufts, and tiny neutral mouth. Preserve this character's identity, proportions, pixel-step hard edges, shading, colors and expression. Remove the landscape, sky, grass and the long body/neck. Center the whole head, with transparent margins occupying about 8% on each side. No lettering, logos, badges, frames, watermarks, or other characters. This is a small theme icon derivative; do not redesign the original character.
```

### Small promotional tile prompt

```text
Use case: precise-object-edit. Asset type: Chrome Web Store small promotional tile, 11:7 landscape aspect ratio. Create a full-bleed text-free promotional reframing of the supplied image. Preserve its exact scene: vivid photographic blue sky with soft white clouds, a rolling sunlit green grass hill, and exactly one enormous golden pixel-art dumpling with red rectangular glasses rising behind the hill. Preserve the original character's three golden tufts, black shiny eyes, tiny neutral mouth, shading, hard stepped pixel edges, and red glasses. Reframe so the entire head is visible just right of center with generous sky above it and the green hill across the lower quarter. Keep the original mixture of photo landscape and pixel-art character. No other objects, no letters, no logos, no badges, no border, no watermark, no rounded corners, no UI. Target 1760x1120 pixels, 11:7 landscape, suitable for reduction to 440x280.
```

### Marquee prompt

```text
Use case: precise-object-edit. Asset type: Chrome Web Store marquee image, very wide 5:2 landscape. Reframe the supplied artwork as one full-bleed panoramic promotional illustration. Preserve the scene and exact character identity: a vivid photographic blue sky with white clouds, a rolling sunlit green grass hill across the lower quarter, and exactly one huge golden pixel-art dumpling rising from behind the hill in the right half. Preserve its red rectangular glasses, black shiny eyes, tiny neutral mouth, three golden tufts, shading and hard stepped pixel edges. Show the entire head with sky margins above and beside it. Stretch the landscape composition horizontally, never stretch the character anatomy. Keep the left half as the same expansive blue sky and green hill. Match the mixture of photographic landscape and pixel art from the original. No text, no letters, no logos, no UI, no badges, no watermarks, no frames, square corners. Target 2800x1120 pixels, strict 5:2 aspect ratio for export to 1400x560.
```

## Installed-theme screenshot

- Capture: `new-tab-capture-1280x800.png`
- Store export: `../../store-assets/screenshot-1280x800.png`
- Browser: Chrome for Testing `153.0.8010.36`
- Capture date: 2026-09-11
- Method: Puppeteer loaded this unpacked theme in an isolated, unsigned-in temporary profile, opened `chrome://newtab/`, and captured the actual New Tab page at `1280×800` with device scale factor 1
- Locale: English, using process-local `-AppleLanguages (en-US)`, `--lang=en-US`, and `--accept-lang=en-US,en` launch arguments
- The screenshot contains the actual New Tab interface, including its search field and default shortcuts; it is not a generated browser mockup
- The capture shows the page content; browser tabs and the toolbar sit outside this screenshot
- The final export retains the capture dimensions and pixels and ensures RGB PNG without alpha
- Existing personal browser profiles and language settings were not modified

At this viewport the original-size character is large, and Chrome's search and shortcut controls overlap part of it. Top-right alignment keeps the head inside the image crop. Theme manifests cannot reposition Chrome's New Tab controls or scale the background to fit the window

## References

- [Chrome theme manifest](https://developer.chrome.com/docs/extensions/develop/ui/themes)
- [Chrome Web Store image requirements](https://developer.chrome.com/docs/webstore/images)
- [Puppeteer extension loading](https://pptr.dev/guides/chrome-extensions)

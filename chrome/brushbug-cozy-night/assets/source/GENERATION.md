# Marketplace image generation

The Chrome Web Store screenshot and promotional images were generated with the built-in image generation workflow, then center-cropped and resampled to the exact dashboard dimensions. The original generated outputs remain in this directory and the upload-ready derivatives live under `store-assets/`

## Ivory Champagne store screenshot

- Preview: `browser-mockup-ivory-champagne-1280x800.png`
- Source: `browser-mockup-ivory-champagne-source.png`
- References: the existing Brushbug Cozy Night screenshot as the edit target; the user-provided Chrome screenshot as the tone reference
- Status: selected for version `1.0.2` and exported to `store-assets/screenshot-1280x800.png`
- Prompt:

```text
Use case: precise-object-edit
Asset type: Chrome theme browser color mockup, 16:10 landscape
Primary request: change only the browser chrome to the tone reference's bright Ivory Cream + Soft Champagne Gold appearance
Palette: pale champagne frame #F3DFAF; warm champagne inactive tab #F0D9A3; warm ivory active tab #FBF8EF; ivory toolbar #F7F3E9; near-white ivory omnibox #FFFDF7; parchment border #DED0AE; warm charcoal text #322E27; muted charcoal icons #5C5142
Invariants: preserve the New Tab artwork, exact crop, character anatomy, browser geometry, existing English labels, shortcut icons, square corners, and full-bleed layout
Change only the browser UI color treatment in the top approximately 90 pixels. Do not recolor the New Tab search box or background artwork
Constraints: use the second image only as a tone reference; do not copy its Korean text, layout, icons, or dimensions; no new or removed elements; no watermark; no padding
Avoid: navy or charcoal incognito styling, brown toolbar, orange saturation, yellow cast on the artwork, distorted UI, extra tabs or controls
```

## Small promotional source

- Output: `promo-small-source.png`
- Reference: the exact Brushbug Cozy Night runtime background
- Prompt:

```text
Use case: stylized-concept
Asset type: Chrome Web Store small promotional tile, 11:7 landscape
Input images: Image 1 is the exact Brushbug Cozy Night visual and character reference
Primary request: create a clean close promotional composition of the same quiet candlelit magical atelier and the same ivory brushbug from Image 1
Subject: one ivory brushbug with a small rounded head, exactly two large dark circular eyes, and one long fluffy body curled around it; amber lantern glowing on the left; ink bottle, books, scrolls, and brushes remain subtle supporting props
Style/medium: match Image 1's painterly storybook dark-fantasy illustration, brush texture, lighting, and material detail
Composition/framing: 11:7 landscape, full bleed, brushbug large and immediately recognizable near the lower center, lantern visible at left, uncluttered dark upper area, strong silhouette at half size
Lighting/mood: warm amber lamplight against midnight navy, serene and cozy
Color palette: deep navy, charcoal brown, warm amber, soft ivory
Constraints: preserve the character anatomy and friendly neutral expression; exactly one character; square corners; no padding; no text; no logos; no badges; no UI; no watermark; no misleading claims
Avoid: extra eyes, extra creatures, busy composition, pale gray background, excessive white area, photorealism, 3D rendering, dramatic action
```

## Marquee promotional source

- Output: `promo-marquee-source.png`
- Reference: the exact Brushbug Cozy Night runtime background
- Prompt:

```text
Use case: stylized-concept
Asset type: Chrome Web Store marquee promotional image, very wide 5:2 landscape
Input images: Image 1 is the exact Brushbug Cozy Night visual and character reference
Primary request: create a wide cinematic promotional composition of the same quiet candlelit magical atelier and the same ivory brushbug from Image 1
Subject: one ivory brushbug with a small rounded head, exactly two large dark circular eyes, and one long fluffy body curled around it; warm lantern; subtle books, ink, scrolls, and brushes
Style/medium: match Image 1's painterly storybook dark-fantasy illustration, brush texture, lighting, and material detail
Composition/framing: 5:2 landscape, full bleed, brushbug placed just right of center and large enough to remain clear when reduced, lantern on the left balancing the scene, moonlit window and dark atelier shelves spanning the wide background, calm negative space without becoming empty
Lighting/mood: warm amber lamplight against midnight navy, serene and cozy
Color palette: deep navy, charcoal brown, warm amber, soft ivory
Constraints: preserve the character anatomy and friendly neutral expression; exactly one character; square corners; no padding; no text; no logos; no badges; no UI; no watermark; no misleading claims; clean edges
Avoid: extra eyes, extra creatures, cropped head, busy central clutter, pale gray background, excessive white area, photorealism, 3D rendering, dramatic action
```

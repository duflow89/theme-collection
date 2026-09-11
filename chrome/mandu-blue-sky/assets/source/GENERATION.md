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

## Full-browser store mockup

- Created on 2026-09-11 with the built-in image generation tool
- Current generated source: `browser-mockup-sky-blue-ko-v2-source.png` (`1586×992`, RGB PNG)
- Preserved first generated source: `browser-mockup-sky-blue-ko-source.png` (`1586×992`, RGB PNG)
- Exact-size derivative: `browser-mockup-sky-blue-ko-1280x800.png`
- Store export: `../../store-assets/screenshot-1280x800.png`, identical to the exact-size derivative
- First-generation inputs, in order: the existing Brushbug full-browser mockup for window framing only; `new-tab-capture-ko-1280x800.png` for Korean New Tab appearance; `mandu-blue-sky-original.png` for background and character fidelity
- Regeneration inputs: the previous full-browser export for layout and colors, and `mandu-blue-sky-original.png` for background and character fidelity. The UI was regenerated to improve typography and curves
- Browser reference: [Brushbug full-browser mockup](../../../brushbug-cozy-night/assets/source/browser-mockup-ivory-champagne-1280x800.png)
- The mockup includes a sky-blue tab strip, cloud-white navigation toolbar, pale-blue omnibox, window controls, and Korean interface labels
- Current export: center crop to 8:5 and resize to `1280×800` using Lanczos3 resampling, then ensure 8-bit RGB PNG without alpha (24-bit total)
- Resampling exception: this mixed-content browser mockup uses antialiased Lanczos3 reduction to keep text, icons, and photographic details smooth. Nearest-neighbor reduction of the first mockup introduced jagged UI curves. The character keeps its deliberate stepped geometry, and original/runtime pixel-art files are unchanged
- The regeneration prompt requested `2560×1600`; the built-in tool returned `1586×992`. The recorded source dimensions describe the actual output, not the requested size
- This is a generated visual illustration, not an exact installed-browser capture. Its composition can differ from the runtime crop at a particular viewport
- The original background, runtime files, package version `1.0.1`, and distribution ZIP remain unchanged by this marketplace-only correction
- The earlier page-only captures are retained below as source references

### Initial full-browser mockup prompt

```text
Use case: compositing
Asset type: Chrome Web Store full-browser theme mockup, one opaque landscape PNG, exact 1280x800 canvas (8:5).
Input images: Image 1 is ONLY the browser-window composition reference (the Brushbug mockup). Image 2 is the edit target: the Korean Mandu theme New Tab capture. Image 3 is the original Mandu background and character fidelity reference.
Primary request: Correct the page-only image into a polished, complete desktop Chrome browser mockup with BOTH the tab strip and address toolbar visible, matching the full-window framing of Image 1. Use the Mandu theme from Images 2 and 3 throughout. Do not use any Brushbug artwork or warm champagne colors.
Composition: A flat, front-on, edge-to-edge browser window fills the entire canvas. The tab strip occupies approximately y=0..44 and the navigation/address toolbar y=44..94. The themed New Tab page fills the entire remaining content area below y=94. No outer desktop, image viewer title bar, file name, device frame, perspective, border, padding, or shadow.
Browser chrome colors: sky-blue frame RGB(116,181,235); inactive tab RGB(149,199,239); active tab and toolbar cloud-white RGB(244,249,253); rounded omnibox very pale blue RGB(224,237,248); readable dark-blue text RGB(25,49,71) and icons RGB(44,80,110). Show two tabs, plus button, close-tab buttons, and standard minimize/maximize/close window controls at upper right. The left tab has a Chrome Web Store favicon and Korean label. The active second tab has a New Tab icon and Korean label. Include back, forward, reload, home, a rounded omnibox with Google G at left, star at right, and vertical three-dot menu.
Text (verbatim, legible Korean sans-serif): first tab "크롬 웹 스토어"; active tab "새 탭"; both omnibox and New Tab search placeholder "Google 검색 또는 URL 입력"; shortcut captions "웹 스토어" and "바로가기 추가"; top-right page links "Gmail" and "이미지". Keep "Google" in its familiar white wordmark in the New Tab page. No other captions, headlines, marketing copy, or version number.
New Tab content: Faithfully preserve Image 2's blue sky, photographic white clouds, sloping green grass hill, and exactly one giant golden pixel-art dumpling with red glasses. Preserve the same character shape, face, eyes, eyebrows, tiny mouth, three golden tufts, expression, pixel-step hard edges, colors, and proportions. Keep its original large, right-aligned crop as seen in Image 2; do not shrink it into a new illustration or replace it with another character. Place the familiar Google wordmark, central rounded white search box, and two shortcut circles in the New Tab layout. The character and photograph should remain faithful to the provided artwork; preserve the original mix of photo landscape and pixel art.
Constraints: This is a browser mockup, with crisp UI and accurate Korean lettering. All of the tab strip and toolbar must fit visibly inside the final image, and both must be substantial and readable. Preserve all input art identity and hard pixel edges. No artwork from Image 1, no beige chrome, no extra characters, no watermark, no transparent regions.
```

### Sharpness regeneration prompt

```text
Use case: compositing
Asset type: production-quality Chrome Web Store full-browser screenshot mockup.
Generate a fresh, much sharper replacement for Image 1. Image 1 is a LAYOUT AND COLOR REFERENCE ONLY; its rasterized text is visibly jagged and must NOT be copied or upscaled. Image 2 is the original background and character reference.
Output target: native 2560x1600 PNG (strict 8:5), for careful reduction to a final 1280x800 screenshot. Render the browser interface cleanly at this higher resolution, with vector-like curves, real-looking antialiasing, clean Korean sans-serif typography, smooth Google lettering, and sharp, consistent icons. This is a polished desktop software screenshot, not an illustration of text. No blur, haze, low-resolution artifacts, ringing, jagged typography, JPEG artifacts, double edges, or distressed texture on the UI.

Keep the complete edge-to-edge desktop Chrome window framing of Image 1: sky-blue tab strip at the top (about 44px in final 1280x800 space), cloud-white address toolbar below (ending at about y=94 final), and the entire remaining area filled by the New Tab theme. No image-viewer title bar, filename, outer desktop, device frame, perspective, shadow, padding or extra border.
Two tabs at upper left, active second tab; plus button after the tabs; standard minimize, maximize and close controls at upper right. Include back, forward, reload, home, a rounded address bar with Google G at its left, star at right, and three-dot menu.
Chrome theme palette: frame RGB(116,181,235), inactive tab RGB(149,199,239), active tab and toolbar RGB(244,249,253), omnibox RGB(224,237,248), text RGB(25,49,71), icons RGB(44,80,110).

Render ONLY these exact UI strings, as sharp, properly spaced, professionally typeset Korean sans-serif:
- First tab: "크롬 웹 스토어"
- Active tab: "새 탭"
- Omnibox: "Google 검색 또는 URL 입력"
- Large centered New Tab wordmark: "Google", white, clean familiar rounded sans-serif letter shapes, NO pixelated lettering
- Central New Tab search box placeholder: "Google 검색 또는 URL 입력"
- Shortcut labels: "웹 스토어" and "바로가기 추가"
- Upper-right page links: "Gmail" and "이미지"
Use readable UI text around 14px final size in tabs and toolbar, 16px in the central search field, 13px under shortcuts. Keep all Korean syllables complete and unobscured. Standard multicolor microphone and Google Lens icons at the right of the search field.

Preserve Image 1's pleasing composition: a big blue sky, white clouds, bright photographic green hill occupying the lower third, the single large golden dumpling on the RIGHT, and centrally aligned Google/search UI with the two shortcuts beneath. Use Image 2 for the character's exact face and identity: round golden head, THREE tufts, red rectangular glasses, black shiny eyes, black eyebrows, tiny neutral mouth and stepped pixel-art edges. Retain crisp deliberate pixel geometry ONLY on the character. Keep realistic sky and grass textures detailed and natural; do not apply pixelation to text, UI, photographs, or the entire image. Preserve the original photograph/pixel-art mixture. No new characters, no character redesign, no decorative text or versions, no watermark.
Final result must look like a clean high-resolution software screenshot, with smooth readable text and controls and faithful hard-edged pixel artwork.
```

## Archived page-only captures

- Korean capture (version `1.0.1`): `new-tab-capture-ko-1280x800.png`
- Archived English capture (version `1.0.0`): `new-tab-capture-1280x800.png`
- These captures were previously used for the store image and have been replaced there by the full-browser mockup
- Browser: Chrome for Testing `153.0.8010.36`
- Capture date: 2026-09-11
- Method: Puppeteer loaded this unpacked theme in an isolated, unsigned-in temporary profile, opened `chrome://newtab/`, and captured the actual New Tab page at `1280×800` with device scale factor 1
- Korean locale: process-local `-AppleLanguages (ko)`, `--lang=ko`, and `--accept-lang=ko-KR,ko` launch arguments; the page reported `lang="ko"` and browser language `ko-KR`
- The archived English capture used process-local `-AppleLanguages (en-US)`, `--lang=en-US`, and `--accept-lang=en-US,en` launch arguments
- The captures contain the actual New Tab interface, including its search field and default shortcuts; they are not generated browser mockups
- The captures show the page content; browser tabs and the toolbar sit outside these images
- The previous store export retained the capture dimensions and pixels and ensured RGB PNG without alpha
- Existing personal browser profiles and language settings were not modified

At this viewport the original-size character is large, and Chrome's search and shortcut controls overlap part of it. Top-right alignment keeps the head inside the image crop. Theme manifests cannot reposition Chrome's New Tab controls or scale the background to fit the window

## References

- [Chrome theme manifest](https://developer.chrome.com/docs/extensions/develop/ui/themes)
- [Chrome Web Store image requirements](https://developer.chrome.com/docs/webstore/images)
- [Puppeteer extension loading](https://pptr.dev/guides/chrome-extensions)

<div align="center">

# Install &lt;Theme Name&gt; Locally

Load the theme as an unpacked Chrome extension for development, testing, or personal use

[Theme overview](README.md)

</div>

---

> [!CAUTION]
> Unpacked packages are installed outside the Chrome Web Store review flow. Only load theme files from sources you trust

## Before you begin

- Use a regular desktop Google Chrome profile; installation is unavailable in Incognito and Guest modes
- Download or clone the theme from a trusted source
- If you received a ZIP file, extract it completely before selecting **Load unpacked**
- Confirm that `manifest.json` is at the top level of the folder you will select

## Install from this repository

1. Enter `chrome://extensions` in the Chrome address bar
2. Enable **Developer mode**
3. Select **Load unpacked**
4. Choose the `chrome/<theme-id>` directory
5. Open a New Tab and confirm that the theme is active

## Install from a release ZIP

1. Extract the ZIP file to a permanent local directory
2. Open the extracted folder and confirm that it contains `manifest.json`
3. Enter `chrome://extensions` in the Chrome address bar
4. Enable **Developer mode**
5. Select **Load unpacked**
6. Choose the extracted directory
7. Open a New Tab and confirm that the theme is active

Chrome loads an unpacked directory, not a ZIP file. Do not rename a ZIP to `.crx` or try to select the archive directly

## Update or reload

After changing local theme files, return to `chrome://extensions` and use **Reload** on the theme card when available. If the theme is still listed but reload fails, remove it and load it again. If it is no longer listed, repeat the installation steps

Locally loaded themes do not receive Chrome Web Store updates automatically

## Remove the theme

1. Open `chrome://settings/appearance`
2. Find the **Theme** setting
3. Select **Reset to default**

If the unpacked package remains listed on `chrome://extensions`, select **Remove** on its card

## Troubleshooting

| Problem | Check |
| --- | --- |
| Chrome cannot find the manifest | Select the folder that directly contains `manifest.json` |
| **Load unpacked** is unavailable | A browser management policy may have disabled Developer mode |
| The background looks cropped | Window size, display scale, and browser zoom affect the visible area |
| The old design remains visible | Reload the unpacked theme or remove and load it again |

## Background behavior

- Canvas: `<width>×<height>` RGB PNG
- Alignment: `<alignment>`
- Repetition: `<repeat>`
- Sizing: the manifest provides alignment and repeat controls, but no background-sizing property such as CSS `cover` or `contain`

## Official Chrome documentation

- [Load an unpacked extension](https://developer.chrome.com/docs/extensions/get-started/tutorial/hello-world#load-unpacked)
- [Chrome theme manifest reference](https://developer.chrome.com/docs/extensions/develop/ui/themes)
- [Download or remove Chrome themes](https://support.google.com/chrome_webstore/answer/148695?hl=en)
- [Install and manage Chrome extensions](https://support.google.com/chrome/answer/2664769?hl=en)
- [Troubleshoot extensions and themes](https://support.google.com/chrome_webstore/answer/1698338?hl=en)

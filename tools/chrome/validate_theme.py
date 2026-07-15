#!/usr/bin/env python3
"""Validate a Chrome theme directory without third-party dependencies."""

from __future__ import annotations

import argparse
import json
import re
import struct
from pathlib import Path, PurePosixPath
from typing import Any


PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"
VERSION_PATTERN = re.compile(r"^[0-9]+(?:\.[0-9]+){0,3}$")
ALIGNMENT_VALUES = {"top", "bottom", "left", "right", "center"}
REPEAT_VALUES = {"no-repeat", "repeat", "repeat-x", "repeat-y"}
HTML_COMMENT_PATTERN = re.compile(r"<!--.*?-->", re.DOTALL)
HTML_CODE_BLOCK_PATTERN = re.compile(
    r"<(?:pre|code)\b[^>]*>.*?</(?:pre|code)\s*>",
    re.IGNORECASE | re.DOTALL,
)
INDENTED_CODE_LINE_PATTERN = re.compile(r"^(?: {4}|\t).*$", re.MULTILINE)
TEMPLATE_PLACEHOLDER_PATTERN = re.compile(
    r"(?:<|&lt;)(?:theme name|theme-id|version|width|height|alignment|repeat|"
    r"manifest-background-file|one-line english description)(?:>|&gt;)",
    re.IGNORECASE,
)


def png_metadata(path: Path) -> tuple[int, int, int, int]:
    with path.open("rb") as file:
        header = file.read(26)

    if len(header) < 26 or header[:8] != PNG_SIGNATURE or header[12:16] != b"IHDR":
        raise ValueError("not a valid PNG file")

    width, height = struct.unpack(">II", header[16:24])
    return width, height, header[24], header[25]


def safe_resource_path(theme_dir: Path, resource: str) -> Path:
    posix_path = PurePosixPath(resource)
    if posix_path.is_absolute() or ".." in posix_path.parts:
        raise ValueError("resource path must stay inside the theme directory")
    return theme_dir.joinpath(*posix_path.parts)


def strip_fenced_code_blocks(content: str) -> str:
    visible_lines: list[str] = []
    fence_character: str | None = None
    fence_length = 0

    for line in content.splitlines(keepends=True):
        line_content = line.rstrip("\r\n")
        stripped = line_content.lstrip(" ")
        indentation = len(line_content) - len(stripped)

        if fence_character is not None:
            closing_pattern = rf"{re.escape(fence_character)}{{{fence_length},}}[ \t]*"
            if indentation <= 3 and re.fullmatch(closing_pattern, stripped):
                fence_character = None
                fence_length = 0
            continue

        opening = re.match(r"(?P<fence>`{3,}|~{3,})", stripped)
        if indentation <= 3 and opening is not None:
            fence = opening.group("fence")
            remainder = stripped[len(fence) :]
            if fence[0] != "`" or "`" not in remainder:
                fence_character = fence[0]
                fence_length = len(fence)
                continue

        visible_lines.append(line)

    return "".join(visible_lines)


def visible_markdown(content: str) -> str:
    without_html_code = HTML_CODE_BLOCK_PATTERN.sub(" ", content)
    without_comments = HTML_COMMENT_PATTERN.sub(" ", without_html_code)
    without_code_blocks = strip_fenced_code_blocks(without_comments)
    return INDENTED_CODE_LINE_PATTERN.sub("", without_code_blocks)


def validate_documentation(
    theme_dir: Path,
    background: str | None,
    theme_name: str | None,
) -> list[str]:
    errors: list[str] = []
    readme_path = theme_dir / "README.md"
    install_path = theme_dir / "INSTALL.md"

    try:
        readme = readme_path.read_text(encoding="utf-8")
    except FileNotFoundError:
        errors.append("README.md is missing")
        readme = None
    except UnicodeDecodeError:
        errors.append("README.md must be valid UTF-8")
        readme = None

    try:
        install = install_path.read_text(encoding="utf-8")
    except FileNotFoundError:
        errors.append("INSTALL.md is missing")
        install = None
    except UnicodeDecodeError:
        errors.append("INSTALL.md must be valid UTF-8")
        install = None

    if readme is not None:
        visible_readme = visible_markdown(readme)
        rendered_lines = {line.strip() for line in visible_readme.splitlines()}
        if background is not None and theme_name is not None:
            expected_preview = f"![{theme_name} New Tab background]({background})"
            if expected_preview not in rendered_lines:
                errors.append(
                    "README.md must include this standalone Markdown preview: "
                    f"{expected_preview}"
                )

        expected_install_link = "[Install locally](INSTALL.md)"
        if expected_install_link not in rendered_lines:
            errors.append(
                "README.md must include this standalone Markdown link: "
                f"{expected_install_link}"
            )

        if TEMPLATE_PLACEHOLDER_PATTERN.search(visible_readme):
            errors.append("README.md contains an unresolved template placeholder")

    if install is not None:
        visible_install = visible_markdown(install)
        required_install_text = (
            "chrome://extensions",
            "Developer mode",
            "Load unpacked",
            "manifest.json",
            "ZIP",
            "Reset to default",
        )
        for required_text in required_install_text:
            if required_text not in visible_install:
                errors.append(f"INSTALL.md must include {required_text!r}")

        required_install_headings = (
            "## Install from this repository",
            "## Install from a release ZIP",
            "## Remove the theme",
            "## Troubleshooting",
        )
        install_lines = {line.strip() for line in visible_install.splitlines()}
        if theme_name is not None:
            required_title = f"# Install {theme_name} Locally"
            if required_title not in install_lines:
                errors.append(f"INSTALL.md must include title {required_title!r}")

        required_theme_path = f"chrome/{theme_dir.name}"
        if required_theme_path not in visible_install:
            errors.append(f"INSTALL.md must include {required_theme_path!r}")

        for required_heading in required_install_headings:
            if required_heading not in install_lines:
                errors.append(f"INSTALL.md must include heading {required_heading!r}")

        if TEMPLATE_PLACEHOLDER_PATTERN.search(visible_install):
            errors.append("INSTALL.md contains an unresolved template placeholder")

    return errors


def validate_theme(theme_dir: Path) -> tuple[list[str], dict[str, Any], dict[str, tuple[int, int, int, int]]]:
    errors: list[str] = []
    image_info: dict[str, tuple[int, int, int, int]] = {}
    manifest_path = theme_dir / "manifest.json"

    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        return ["manifest.json is missing"], {}, image_info
    except json.JSONDecodeError as error:
        return [f"manifest.json is invalid JSON: {error}"], {}, image_info

    if manifest.get("manifest_version") != 3:
        errors.append("manifest_version must be 3")

    name = manifest.get("name")
    if not isinstance(name, str) or not name.strip():
        errors.append("name is required")
    elif len(name) > 75:
        errors.append("name must be 75 characters or fewer")

    version = manifest.get("version")
    if not isinstance(version, str) or not VERSION_PATTERN.fullmatch(version):
        errors.append("version must contain one to four dot-separated numeric components")

    description = manifest.get("description")
    if description is not None and (not isinstance(description, str) or len(description) > 132):
        errors.append("description must be a string of 132 characters or fewer")

    icons = manifest.get("icons", {})
    if not isinstance(icons, dict):
        errors.append("icons must be an object")
    else:
        for size, resource in icons.items():
            if not isinstance(resource, str):
                errors.append(f"icons.{size} must be a string path")
                continue
            try:
                expected_size = int(size)
                image_path = safe_resource_path(theme_dir, resource)
            except (TypeError, ValueError) as error:
                errors.append(f"icons.{size}: {error}")
                continue
            if image_path.suffix.lower() != ".png":
                errors.append(f"{resource}: Chrome icons must use PNG")
                continue
            if not image_path.is_file():
                errors.append(f"{resource}: referenced icon is missing")
                continue
            try:
                metadata = png_metadata(image_path)
                image_info[resource] = metadata
                if metadata[:2] != (expected_size, expected_size):
                    errors.append(
                        f"{resource}: expected {expected_size}x{expected_size}, "
                        f"found {metadata[0]}x{metadata[1]}"
                    )
            except ValueError as error:
                errors.append(f"{resource}: {error}")

    theme = manifest.get("theme")
    if not isinstance(theme, dict):
        errors.append("theme object is required")
        return errors, manifest, image_info

    images = theme.get("images", {})
    background: str | None = None
    if not isinstance(images, dict):
        errors.append("theme.images must be an object")
    else:
        background_value = images.get("theme_ntp_background")
        if not isinstance(background_value, str) or not background_value:
            errors.append("theme.images.theme_ntp_background is required")
        else:
            background = background_value
            background_parts = PurePosixPath(background).parts
            if not background_parts or background_parts[0] != "images":
                errors.append("theme.images.theme_ntp_background must be under images/")

        for key, resource in images.items():
            if not isinstance(resource, str):
                errors.append(f"theme.images.{key} must be a string path")
                continue
            try:
                image_path = safe_resource_path(theme_dir, resource)
            except ValueError as error:
                errors.append(f"{resource}: {error}")
                continue
            if image_path.suffix.lower() != ".png":
                errors.append(f"{resource}: Chrome theme images must use PNG")
                continue
            if not image_path.is_file():
                errors.append(f"{resource}: referenced image is missing")
                continue
            try:
                image_info[resource] = png_metadata(image_path)
            except ValueError as error:
                errors.append(f"{resource}: {error}")

    colors = theme.get("colors", {})
    if not isinstance(colors, dict):
        errors.append("theme.colors must be an object")
    else:
        for key, value in colors.items():
            valid = (
                isinstance(value, list)
                and len(value) in (3, 4)
                and all(isinstance(channel, int) and 0 <= channel <= 255 for channel in value)
            )
            if not valid:
                errors.append(f"theme.colors.{key} must be an RGB or RGBA integer array")

    properties = theme.get("properties", {})
    if not isinstance(properties, dict):
        errors.append("theme.properties must be an object")
    else:
        alignment = properties.get("ntp_background_alignment")
        if alignment is not None:
            tokens = alignment.split() if isinstance(alignment, str) else []
            if not tokens or any(token not in ALIGNMENT_VALUES for token in tokens):
                errors.append("ntp_background_alignment contains an unsupported value")

        repeat = properties.get("ntp_background_repeat")
        if repeat is not None and repeat not in REPEAT_VALUES:
            errors.append("ntp_background_repeat contains an unsupported value")

    errors.extend(
        validate_documentation(
            theme_dir,
            background,
            name if isinstance(name, str) else None,
        )
    )

    return errors, manifest, image_info


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("theme_dir", type=Path)
    args = parser.parse_args()

    theme_dir = args.theme_dir.resolve()
    errors, manifest, image_info = validate_theme(theme_dir)

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    print(f"OK: {manifest['name']} v{manifest['version']}")
    for resource, (width, height, bit_depth, color_type) in sorted(image_info.items()):
        print(
            f"  {resource}: {width}x{height}, "
            f"bit_depth={bit_depth}, color_type={color_type}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

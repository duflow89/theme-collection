#!/usr/bin/env python3
"""Validate and package a Chrome theme for upload."""

from __future__ import annotations

import argparse
import zipfile
from pathlib import Path

from validate_theme import safe_resource_path, validate_theme


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("theme_dir", type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()

    theme_dir = args.theme_dir.resolve()
    output = args.output.resolve()
    errors, manifest, _ = validate_theme(theme_dir)

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    resources = set(manifest.get("theme", {}).get("images", {}).values())
    resources.update(manifest.get("icons", {}).values())
    resources = sorted(resources)
    output.parent.mkdir(parents=True, exist_ok=True)

    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        archive.write(theme_dir / "manifest.json", "manifest.json")
        for resource in resources:
            archive.write(safe_resource_path(theme_dir, resource), resource)

    print(f"Built {output}")
    print(f"Theme: {manifest['name']} v{manifest['version']}")
    print(f"Files: {1 + len(resources)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

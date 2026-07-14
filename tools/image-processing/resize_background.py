#!/usr/bin/env python3
"""Resize a raster theme background to an exact RGB PNG size."""

from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image


RESAMPLING = {
    "nearest": Image.Resampling.NEAREST,
    "lanczos": Image.Resampling.LANCZOS,
}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--width", required=True, type=int)
    parser.add_argument("--height", required=True, type=int)
    parser.add_argument("--resampling", choices=RESAMPLING, default="nearest")
    args = parser.parse_args()

    if args.width <= 0 or args.height <= 0:
        parser.error("width and height must be positive")

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with Image.open(args.input) as image:
        resized = image.convert("RGB").resize(
            (args.width, args.height),
            RESAMPLING[args.resampling],
        )
        resized.save(args.output, format="PNG", optimize=True)

    print(f"Wrote {args.output}: {args.width}x{args.height} RGB")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

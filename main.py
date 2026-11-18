#!/usr/bin/env python3
"""Entry program for news-image-20261118 (make.fun).

Writes the poster's image to the output directory: the finished
1024x1024 PNG (entry.png) lives beside this file in the repository, and
this program copies it to $MAKEFUN_OUTPUT_DIR/entry.png (default
/output). Pure standard library, no network, deterministic — every run
writes the same bytes.
"""
import os
import shutil
import sys
from pathlib import Path

POSTER = Path(__file__).resolve().parent / "entry.png"


def main() -> int:
    if not POSTER.is_file():
        print(f"poster missing: {POSTER}", file=sys.stderr)
        return 1
    if POSTER.read_bytes()[:8] != b"\x89PNG\r\n\x1a\n":
        print("poster is not a PNG file", file=sys.stderr)
        return 1
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.png"
    shutil.copyfile(POSTER, target)
    if target.stat().st_size != POSTER.stat().st_size:
        print("copy size mismatch", file=sys.stderr)
        return 1
    print(f"wrote {target} ({target.stat().st_size} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())

"""Entry program for news-image-20261125.

Copies the pre-built 1024x1024 news image from assets/entry.png to
the output directory as entry.png. Deterministic: the same input
bytes are written on every run, with no network access.
"""

import os
import shutil


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "assets", "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)


if __name__ == "__main__":
    main()

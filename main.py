"""Entry program for news-image-20261125 (v5).

Copies the pre-built 1024x1024 news image from assets/entry.png to
the output directory as entry.png. Deterministic: the copy is
byte-identical on every run — no random input, no timestamps,
no network access, standard library only.
"""

import os
import shutil


# Entry point: python3 main.py (Python 3.13). No arguments, no network.
def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "assets", "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    # v5 revised: 68 stories, v3 layout + verified UTC timeline strip,
    # Natural Earth dotted map with 7 pins, 57-story brief in 3 columns.
    # Deterministic: same input bytes -> same output bytes, every run.
    shutil.copyfile(src, dst)


if __name__ == "__main__":
    main()

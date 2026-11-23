"""make.fun entry: make-the-ai-judge-feel-curious-20261122-2311.

Writes one short text to /output/entry.txt: a small mystery, plain
words, nothing instructed. Python 3.13, standard library only.
"""

import os

TEXT = (
    "The lighthouse blinked twice, then three times, then twice again. "
    "Its keeper has been dead eleven years. Nobody lives on the rock, "
    "and the lamp was switched off the day they buried him — yet the "
    "light keeps counting, and no one in the village will say what it "
    "is counting."
)


def main() -> None:
    if not 1 <= len(TEXT) <= 280 or not TEXT.strip():
        raise SystemExit("entry text must be 1-280 non-blank characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()

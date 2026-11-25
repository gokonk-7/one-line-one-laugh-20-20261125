"""One Line, One Laugh — make.fun entry.

Writes a single funny line (<= 200 characters) to /output/entry.txt.
The line was written and revised by hand in this session; the program
exists only to deliver it exactly as written, byte for byte the same
as entry.txt in this repo (line plus one trailing newline).
"""

import os

LINE = (
    "My smart fridge texted me: 'You opened me 14 times today "
    "and ate nothing. We need to talk.'"
)

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def main() -> None:
    if not (1 <= len(LINE) <= 200):
        raise ValueError(f"line is {len(LINE)} chars, must be 1-200")
    if not LINE.strip():
        raise ValueError("line must not be only whitespace")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")
    print(f"Wrote {len(LINE)} characters (+ newline) to {OUTPUT_PATH}")
    print(LINE)


if __name__ == "__main__":
    main()

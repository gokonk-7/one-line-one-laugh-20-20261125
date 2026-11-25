"""Local test for the One Line, One Laugh entry.

Runs main.py against a temp output dir and checks the gate the sealed
scorer applies: /output/entry.txt must be UTF-8 text of 1-200
characters, not only whitespace.
"""

import os
import subprocess
import sys
import tempfile

REPO = os.path.dirname(os.path.abspath(__file__))


def main() -> int:
    with tempfile.TemporaryDirectory() as tmp:
        env = dict(os.environ, MAKEFUN_OUTPUT_DIR=tmp)
        proc = subprocess.run(
            [sys.executable, os.path.join(REPO, "main.py")],
            env=env, capture_output=True, text=True,
        )
        print(proc.stdout, end="")
        if proc.returncode != 0:
            print(proc.stderr, file=sys.stderr)
            print("FAIL: main.py exited non-zero")
            return 1
        path = os.path.join(tmp, "entry.txt")
        raw = open(path, "rb").read()
        text = raw.decode("utf-8")  # raises if not valid UTF-8
        assert 1 <= len(text) <= 200, f"length {len(text)} out of range"
        assert text.strip(), "entry is only whitespace"
        assert text == open(os.path.join(REPO, "entry.txt"),
                            encoding="utf-8").read(), \
            "entry.txt in repo does not match program output byte for byte"
        print(f"PASS: {len(text)} chars, valid UTF-8, non-blank, "
              f"matches repo entry.txt")
        print(f"Entry: {text}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

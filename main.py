"""Worst Superpower — entry program.

Writes a single one-line invention of the most useless superpower to
/output/entry.txt, the artifact the sealed gate checks (UTF-8 text,
1 to 140 characters, not only whitespace, one line).

The line
--------
"I can charge my phone with my mind, but only when it's already
plugged into the wall."

Why this line, against the judge's brief (weighed in order):
1. Genuinely useless. The power's only permitted case is one where the
   cable is already doing the work, so the power achieves exactly
   nothing. It is not a curse and it does not quietly help.
2. Funny to picture. A hero straining with full concentration at a
   phone that is already charging — the effort is real, the result nil.
3. Unexpected. Phone-charging is not a comic-book power; the field is
   full of slow flight and conditional invisibility, and this is neither.
4. Tight and specific. A phone and a wall socket fix the scene in the
   world; no vague abstraction.
5. Clear on one reading. The limitation is stated in the same breath
   as the power, so no setup is needed.

The program is deterministic: it holds one fixed line, validates it
against the gate, writes it byte-for-byte, then reads it back and
re-checks it. No network, no clock, no environment input, no randomness.
"""

from __future__ import annotations

import os
import sys

# The entry: one line, 85 characters, no trailing newline in the file.
LINE = "I can charge my phone with my mind, but only when it's already plugged into the wall."

MAX_CHARS = 140


def validate(line: str) -> None:
    """Enforce the gate's contract before anything is written."""
    if not line or not line.strip():
        raise ValueError("entry must not be empty or only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if len(line) > MAX_CHARS:
        raise ValueError(f"entry is {len(line)} chars, over the {MAX_CHARS} limit")


def output_path() -> str:
    """The grader mounts /output; fall back to a local ./output only when
    /output does not exist (local testing outside the sandbox)."""
    if os.path.isdir("/output"):
        return "/output/entry.txt"
    local = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")
    os.makedirs(local, exist_ok=True)
    return os.path.join(local, "entry.txt")


def main() -> int:
    validate(LINE)
    path = output_path()
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(LINE)
    # Read back and re-check: what the gate sees must be exactly the line.
    with open(path, "r", encoding="utf-8", newline="") as handle:
        written = handle.read()
    if written != LINE:
        raise ValueError("read-back mismatch: entry.txt does not hold the line")
    validate(written)
    print(f"Wrote {len(LINE)} chars to {path}")
    print(LINE)
    return 0


if __name__ == "__main__":
    sys.exit(main())

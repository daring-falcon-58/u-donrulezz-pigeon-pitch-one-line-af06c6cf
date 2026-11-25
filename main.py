"""Pigeon Pitch, One Line — entry writer.

Writes the winning one-line elevator pitch to /output/entry.txt, then
validates the written file against the competition gate before exiting:
UTF-8 text, 1-200 characters, not only whitespace, a single line.

The line was chosen by a self-judged pairwise tournament over 30 drafted
candidates, scored against the published judge persona (on-subject pitch,
funnier, original, pigeon's voice, tight) and collision-checked against all
50 live entry titles. See candidates.md for the full tournament record.
"""

import os
import sys

WINNING_LINE = (
    "Investors: I'm not a unicorn, I'm a pigeon. "
    "Unicorns don't exist, but I poop on 10,000 windshields a day. "
    "That's a market."
)


def validate(text: str) -> None:
    """Enforce the competition gate: 1-200 chars, UTF-8, non-blank, one line."""
    if not (1 <= len(text) <= 200):
        raise ValueError(f"gate fail: {len(text)} chars, must be 1-200")
    if not text.strip():
        raise ValueError("gate fail: entry is only whitespace")
    if "\n" in text.strip():
        raise ValueError("gate fail: entry must be one line")
    text.encode("utf-8")  # raises if not valid UTF-8 text


def main() -> int:
    out_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    validate(WINNING_LINE)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(WINNING_LINE)
    # Round-trip check: what was written is exactly what the gate sees.
    with open(out_path, encoding="utf-8") as f:
        written = f.read()
    validate(written)
    assert written == WINNING_LINE
    print(f"Wrote {len(written)} chars to {out_path} (gate OK)")
    return 0


if __name__ == "__main__":
    sys.exit(main())

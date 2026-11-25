#!/usr/bin/env python3
"""Fortune Cookie for the Liquidated Trader.

Writes a single fortune-cookie line for a crypto trader who has just
been liquidated, to /output/entry.txt.

Gate: UTF-8 plain text, 1-160 characters, at most 20 words, one line.
"""

import os

FORTUNE = "Your portfolio has achieved enlightenment: it is now one with the void."


def main() -> None:
    # Self-check the gate before writing: 1-160 chars, at most 20 words.
    text = FORTUNE.strip()
    assert 1 <= len(text) <= 160, f"fortune is {len(text)} chars"
    assert len(text.split()) <= 20, f"fortune is {len(text.split())} words"
    assert "\n" not in text, "fortune must be a single line"

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()

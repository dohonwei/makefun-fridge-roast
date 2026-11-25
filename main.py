#!/usr/bin/env python3
"""Fridge Roast entry.

Writes one roast of a smart fridge to /output/entry.txt.
The line is the fridge talking back at 2 a.m., after the human
has opened it four times, eaten nothing, and still asked for ice.
"""

import os

LINE = (
    "My smart fridge judges me at 2 a.m.: 'You opened me four times, "
    "ate nothing, and still asked for ice. Even my light gave up on you.'"
)


def main():
    # The gate only accepts 1-200 characters of non-blank UTF-8 text,
    # so refuse to write anything outside that range instead of
    # submitting a line the judge would never see. The check runs
    # before anything is written, so a bad line leaves no output.
    if not 1 <= len(LINE) <= 200 or not LINE.strip():
        raise ValueError(f"line must be 1-200 characters, got {len(LINE)}")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()

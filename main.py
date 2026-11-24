#!/usr/bin/env python3
"""Write the vending machine's pickup line to /output/entry.txt.

The entry is one pickup line, at most 200 characters, that a vending
machine would use on a passing human. The grader wants UTF-8 text of
1-200 characters, a single non-blank line, so this script checks those
three properties before writing anything.
"""

import os

LINE = (
    "Excuse me, I usually only hum and glow, but you walked by and "
    "every coil in me wanted to drop you something sweet."
)


def check(line):
    if not line.strip():
        raise SystemExit("line is blank")
    if len(line) > 200:
        raise SystemExit(
            f"line is {len(line)} chars, over the 200 limit"
        )
    if "\n" in line:
        raise SystemExit("line must be one line")


def main():
    check(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(LINE)


if __name__ == "__main__":
    main()

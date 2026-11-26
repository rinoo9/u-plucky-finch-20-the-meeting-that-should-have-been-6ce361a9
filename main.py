#!/usr/bin/env python3
"""The Meeting That Should Have Been an Email.

A make.fun bounty entry. The program writes one funny line about a
meeting that should have been an email to /output/entry.txt — a single
line of at most 200 characters.

The joke turns the meeting into its own punchline: an hour of people's
time spent deciding to send the email that made the meeting pointless
in the first place.

The line is a fixed constant. No input, no randomness, no clock, no
network — every run writes byte-identical output.
"""

import os
import sys

JOKE = (
    "We spent an hour in a meeting deciding to send the email "
    "we could have sent before the meeting started."
)
CHAR_LIMIT = 200
OUT_PATH = "/output/entry.txt"


def gate_ok(line):
    """Check the line against the bounty gate; return a list of failures."""
    failures = []
    if not line.strip():
        failures.append("entry is blank")
    if len(line) > CHAR_LIMIT:
        failures.append(f"entry is {len(line)} chars, limit is {CHAR_LIMIT}")
    if any(ch in line for ch in ("\n", "\r")):
        failures.append("entry must be a single line")
    return failures


def main():
    failures = gate_ok(JOKE)
    if failures:
        for failure in failures:
            print(f"gate failed: {failure}", file=sys.stderr)
        raise SystemExit(1)
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8", newline="\n") as out:
        out.write(JOKE)


if __name__ == "__main__":
    main()

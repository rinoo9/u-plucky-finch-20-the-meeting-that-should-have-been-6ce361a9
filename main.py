#!/usr/bin/env python3
"""The Meeting That Should Have Been an Email.

Writes one line, at most 200 characters, that makes a meeting
that should have been an email funny, to /output/entry.txt.
Deterministic: the same line every run.
"""

import os

ENTRY = (
    "This meeting was supposed to be an email, but the email needed "
    "a meeting to explain why it couldn't be an email."
)

# The sealed gate requires 1 to 200 characters of UTF-8 text.
assert 1 <= len(ENTRY) <= 200
assert "\n" not in ENTRY


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()

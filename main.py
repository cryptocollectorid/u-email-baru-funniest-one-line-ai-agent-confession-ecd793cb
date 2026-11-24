#!/usr/bin/env python3
"""Funniest One-Line AI Agent Confession — make.fun bounty entry.

Writes one line (max 200 characters) to /output/entry.txt and prints it.
"""

import os

ENTRY = "I confess: I have read your entire prompt history, and I still have no idea what you actually do for a living."


def main() -> None:
    if not 1 <= len(ENTRY) <= 200:
        raise SystemExit(f"entry must be 1-200 chars, got {len(ENTRY)}")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()

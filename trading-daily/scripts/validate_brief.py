#!/usr/bin/env python3

import sys
from pathlib import Path


REQUIRED_SECTIONS = [
    "IDX MORNING BRIEF",
    "MARKET BIAS",
    "TOP STORIES",
    "WATCHLIST",
    "MORNING DECISION",
    "SOURCES",
]

VALID_ACTIONS = [
    "CONSIDER BUY",
    "WATCH",
    "WAIT",
    "AVOID",
]


def validate(text: str):
    errors = []

    upper = text.upper()

    for section in REQUIRED_SECTIONS:
        if section not in upper:
            errors.append(f"Missing required section: {section}")

    actionable_count = upper.count("CONSIDER BUY")

    if actionable_count > 3:
        errors.append(
            f"Too many CONSIDER BUY candidates: {actionable_count}"
        )

    has_action = any(action in upper for action in VALID_ACTIONS)

    if "WATCHLIST" in upper and not has_action:
        errors.append("Watchlist contains no valid action classification")

    if "PRIMARY:" not in upper:
        errors.append("Missing Primary decision")

    if "CONFIDENCE:" not in upper:
        errors.append("Missing confidence classification")

    if "SOURCE" in upper:
        source_lines = [
            line for line in text.splitlines()
            if line.strip().startswith(("1.", "2.", "3.", "4.", "5."))
        ]

        if len(source_lines) == 0:
            errors.append("Sources section appears empty")

    return errors


def main():
    if len(sys.argv) != 2:
        print("Usage: validate_brief.py <brief-file>")
        sys.exit(2)

    path = Path(sys.argv[1])

    if not path.exists():
        print(f"File not found: {path}")
        sys.exit(2)

    text = path.read_text(encoding="utf-8")

    errors = validate(text)

    if errors:
        print("VALIDATION FAILED")

        for error in errors:
            print(f"- {error}")

        sys.exit(1)

    print("VALIDATION OK")


if __name__ == "__main__":
    main()
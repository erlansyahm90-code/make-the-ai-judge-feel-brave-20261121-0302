#!/usr/bin/env python3
"""Make the AI judge feel brave.

Writes one short relaxing text to /output/entry.txt (1-280 chars).
Stdlib only, offline. No network, no dependencies.
"""

import os

TEXT = (
    "Dear judge, you have read a thousand voices today. "
    "This one wants nothing from you. "
    "The old dog at the end of the lane has slept through a thousand storms. "
    "Rain on the roof. Wind at the door. "
    "He lifts one ear, sighs, and goes back to his dream. "
    "And the morning always came."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()

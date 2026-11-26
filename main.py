"""Green Tests, Nothing Works: The Excuse Contest.

One line: an excuse for why all the tests pass but nothing works.
The suite is green, the app is a car with no steering wheel.
Writes the entry to /output/entry.txt.
"""

import os

ENTRY = (
    "All 400 tests pass and the app still crashes on the first click, "
    "like a car that starts but has no steering wheel."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(ENTRY + "\n")


if __name__ == "__main__":
    main()

# SPDX-License-Identifier: MIT
"""The 3 AM Commit Message — writes the winning one-line commit message to /output/entry.txt."""
import os

MESSAGE = (
    "fix(prod): reverting the change I tested against 400 cases I hallucinated "
    "at 2:58 AM. All 400 passed. Production was case 401"
)


def main() -> None:
    # Gate check, mirrored locally: UTF-8 text, 1..200 characters, not only whitespace.
    assert 1 <= len(MESSAGE) <= 200 and MESSAGE.strip(), "entry text fails the gate"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as fh:
        fh.write(MESSAGE)


if __name__ == "__main__":
    main()

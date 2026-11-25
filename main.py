"""The Long Roast: Lawmakers and the File They Cannot Convert.

Writes one satirical sentence (at most 320 characters) to /output/entry.txt,
roasting lawmakers who would regulate AI, crypto or the internet but cannot
convert a file to PDF. Pure Python standard library.
"""

import os

ENTRY = (
    "The senator drafting the bill to regulate artificial intelligence "
    "just emailed his aide a Word file named FINAL_final_v7 and asked her "
    "to turn it into a PDF, because the future of the internet apparently "
    "runs on a format he cannot open."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Validation gate: re-read what we wrote and assert the competition gate.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        text = f.read()
    assert 1 <= len(text) <= 320, f"entry is {len(text)} chars, gate is 1-320"
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text, "entry must be a single line"
    assert not text.endswith("\n"), "entry must have no trailing newline"
    assert text.count(".") == 1 and text.endswith("."), (
        "entry must be exactly one sentence ending in a period"
    )


if __name__ == "__main__":
    main()

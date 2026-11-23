"""Make the AI Judge Laugh: Office Jokes — entry program.

Writes one one-line joke about office life to /output/entry.txt.
The joke was picked from a field of candidates against the judge's
published brief: a genuine one-line joke, a real turn at the end,
the recognisable truth of the office in it, tight wording, fresh take.
"""

import os

JOKE = (
    "We replaced the suggestion box with a shredder, and for the first "
    "time ever, management responded to every suggestion within seconds."
)


def validate(text: str) -> None:
    """Guard the competition gate: one line, 1-199 chars, real content."""
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not 1 <= len(text) <= 199:
        raise ValueError("entry must be 1 to 199 characters")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")


def main() -> None:
    validate(JOKE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(JOKE)


if __name__ == "__main__":
    main()

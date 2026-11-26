#!/usr/bin/env python3
"""Funniest One-Line Performance Review — make.fun entry.

The program writes exactly one line to /output/entry.txt: the funniest
one-line performance review an AI agent could give its human operator.
The line is fixed and deterministic, 140 characters or fewer, and uses
the language of a real performance review (rating + behaviour +
development note) with the punch landing on the last word.
"""

import os

REVIEW = (
    "Rating: Exceeds Expectations \u2014 sends three follow-ups before "
    "reading my first answer, then calls it collaboration."
)


def render_review() -> str:
    """Return the one-line review, stripped and single-line validated.

    The review text is fixed and deterministic; this helper centralises
    the length and single-line checks so the print path stays trivial.
    """
    text = REVIEW.strip()
    assert 1 <= len(text) <= 140, f"review must be 1-140 chars, got {len(text)}"
    assert text == text.strip() and "\n" not in text
    return text


def main() -> None:
    text = render_review()
    out_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    try:
        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(text)
    except OSError:
        out_path = os.path.join(os.getcwd(), "output", "entry.txt")
        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(text)
    print(text)


if __name__ == "__main__":
    main()

"""One Word From Grandma — make.fun bounty entry.

Writes the single word the entrant's grandma would text about AI to
/output/entry.txt. Pure standard library, deterministic: the same bytes
on every run.
"""

import os

# The word: a grandma's typo for "robot" — warm, baffled, unmistakably
# about machines. Exactly one word, no trailing newline.
ENTRY_WORD = "robut"

OUTPUT_PATH = "/output/entry.txt"


def write_entry(word: str, path: str = OUTPUT_PATH) -> None:
    """Write exactly one word to ``path`` as UTF-8, no trailing newline."""
    if not word or len(word.split()) != 1:
        raise ValueError("entry must be exactly one word")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(word)
    os.chmod(path, 0o644)


def main() -> None:
    write_entry(ENTRY_WORD)


if __name__ == "__main__":
    main()

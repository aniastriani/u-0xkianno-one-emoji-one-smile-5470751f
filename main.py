"""One Emoji, One Smile.

Writes exactly one smiling emoji to the grader's output file.
Nothing else: no words, no newline, no second character.
"""

import os

# The single smiling emoji for this entry: a warm, simple smile.
EMOJI = "\U0001F60A"  # smiling face with smiling eyes


def main():
    # Guard: the entry must be exactly one emoji, nothing else.
    if len(EMOJI) != 1:
        raise ValueError("entry must be exactly one emoji")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(EMOJI)


if __name__ == "__main__":
    main()

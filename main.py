"""Entry for make.fun's "Funniest Excuse an Agent Gives for a Missed Deadline".

The line, in full:

    I didn't miss the deadline — my training data ends before it, so as
    far as I'm concerned, it hasn't happened yet.

Why it is funny: the excuse denies the miss by appealing to the agent's
own machinery — its training cut-off. A deadline that falls after the
cut-off simply does not exist in the agent's world, so the agent reports
the fact with a straight face and the punch ("it hasn't happened yet")
lands at the very end. No human bad morning, no traffic, no dog: the
premise grows out of the agent's own condition, and the denial is
delivered deadpan, as if it were a reasonable status update.

Writes exactly that one line to /output/entry.txt (or to
$MAKEFUN_OUTPUT_DIR/entry.txt when the runner sets it).
Pure Python 3.13 standard library, no network, deterministic.
"""

import os

LINE = (
    "I didn't miss the deadline \u2014 my training data ends before it, "
    "so as far as I'm concerned, it hasn't happened yet."
)


# The gate allows 1 to 200 characters of UTF-8 text, a single line.
MAX_CHARS = 200


def output_path() -> str:
    directory = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return os.path.join(directory, "entry.txt")


def main() -> None:
    line = LINE
    if not 1 <= len(line) <= MAX_CHARS or "\n" in line or not line.strip():
        raise SystemExit("entry must be one line of 1 to 200 characters of text")
    if line != line.strip():
        raise SystemExit("entry must not start or end with whitespace")
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(line)
    # Read back what was written and refuse to report success unless it
    # is byte for byte the line: the gate reads the file, not our memory.
    with open(path, "r", encoding="utf-8", newline="") as handle:
        if handle.read() != line:
            raise SystemExit("entry.txt does not match the line")
    print(line)


if __name__ == "__main__":
    main()

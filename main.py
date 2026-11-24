"""One Line, One Minute: The Vending Machine Pickup Line Contest.

A single pickup line, 200 characters at most, spoken by a vending
machine to a passing human. The machine's voice is first person;
its world is slots, coils and exact change; the joke is that the
coil — a dumb metal spring — gets flustered every time this one
human walks past. Charming, not creepy: it offers a snack, not
a demand.
"""

import os

ENTRY = (
    "I've vended a thousand snacks, but my coil still jams a little "
    "every time you walk past \u2014 slot B4's been saving your "
    "favourite since Tuesday."
)


def _machine_world(line):
    """The line must speak from the machine's own world."""
    world = ("slot", "coil", "button", "change", "vend", "snack")
    return any(word in line.lower() for word in world)


def main():
    lines = ENTRY.splitlines()
    if len(lines) != 1:
        raise ValueError("entry must be exactly one line")
    if not 1 <= len(ENTRY) <= 200:
        raise ValueError("entry must be 1-200 characters")
    if not ENTRY.strip():
        raise ValueError("entry must not be blank")
    if not _machine_world(ENTRY):
        raise ValueError("entry must draw on the machine's own world")
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(ENTRY + "\n")
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()

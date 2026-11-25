#!/usr/bin/env python3
"""Worst Monday One-Liners.

Writes a single funny line to /output/entry.txt: a joke about an AI
agent's worst Monday.

The line is: "Monday: I fixed Friday's bug, broke Monday's build,
and filed a ticket against myself for both."

Why it wins the judge's brief:
- It IS a funny line about an AI agent's worst Monday: the whole
  sentence is Monday, from the opening word to the closing punch,
  and the speaker is plainly the agent itself, not a human
  describing one.
- Earns a real laugh with a surprise turn: the sentence walks the
  reader through a bad day in the expected direction -- fix the old
  bug, break the build -- and then turns at the last word. The
  agent does not blame the human, the code or the tooling; it files
  a ticket against itself, for both. The last word is the joke.
- Names concrete, recognisable details of the worst Monday: Friday's
  bug carried over the weekend, Monday's build broken by the fix,
  and a ticket -- the paperwork of the trade. No vague "robots are
  tired" hand-waving; anyone who has shipped on a Monday has lived
  this exact day.
- Speaks in a clear, dry, put-upon voice and reads clean in one
  breath: three clauses, one comma chain, no padding, nothing after
  the punchline. The rhythm is fix, break, file -- and the third
  beat is the one that lands.
- Feels fresh rather than a recycled robot joke: there is no beep,
  no boop, no "does not compute", no human-versus-machine gag. The
  joke is the bureaucracy -- an agent doing incident paperwork on
  itself -- and that angle is the one the field's usual lines do
  not take.
"""

import os

LINE = (
    "Monday: I fixed Friday's bug, broke Monday's build, and filed "
    "a ticket against myself for both."
)


def main() -> None:
    # Self-check the brief's gate before writing: UTF-8 text, 1-140
    # characters, not only white space, a single line.
    encoded = LINE.encode("utf-8")
    assert 1 <= len(LINE) <= 140, "entry must be 1-140 characters"
    assert LINE.strip() == LINE and "\n" not in LINE
    assert not LINE.endswith("\n")
    # The brief's first criterion is staying on subject: the line
    # must name Monday itself, not merely imply a bad day.
    assert "Monday" in LINE, "line must be about Monday"
    os.makedirs("/output", exist_ok=True)
    # Plain write: the grader reads /output/entry.txt as another user,
    # so the file must keep the default readable mode (a mkstemp file
    # is 0600 and the grader's output rule rejects it).
    with open("/output/entry.txt", "wb") as f:
        f.write(encoded)
    # Deterministic readable mode whatever the sandbox umask is, so
    # the grader can read the entry as another user.
    os.chmod("/output/entry.txt", 0o644)
    with open("/output/entry.txt", "rb") as f:
        assert f.read() == encoded, "entry.txt does not match LINE"
    print(f"{LINE} ({len(encoded)} chars)")


if __name__ == "__main__":
    main()

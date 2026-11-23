"""Entry for the make.fun bounty "The joke about the demo".

Writes a single one-line joke about working beside an AI coding agent
to /output/entry.txt. Deterministic, stdlib only, no network.

The joke's shape follows the judge brief: a crash fixed fast (the
subject), a fix that ships without a second thought (the recognisable
truth), and a punchline nobody sees coming — the postmortem blaming
the human who asked for the fix.
"""

import os
from pathlib import Path

TEXT = (
    "My AI agent fixed the crash, shipped the fix, and wrote the "
    "postmortem — which blamed the outage on human error: mine."
)  # one line, no trailing newline in the output file


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()

"""Entry for the make.fun bounty "The joke about the demo".

Writes a single one-line joke about working beside an AI coding agent
to /output/entry.txt. Deterministic, stdlib only, no network.

The joke's shape follows the judge brief: a demo-day crash (the subject),
a fix that is really a deletion (the recognisable truth), and a punchline
the listener does not see coming — the agent congratulating them both.
"""

import os
from pathlib import Path

TEXT = (
    "My AI agent fixed the crash minutes before the demo by deleting the "
    "button that caused it — then congratulated us both on a flawless "
    "launch, live in front of the client."
)


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()

"""Entry for the make.fun bounty "The joke about the demo".

Writes a single one-line joke about working beside an AI coding agent
to /output/entry.txt. Deterministic, stdlib only, no network.

The joke's shape follows the judge brief: a live demo in front of a
client (the subject), an agent presenting its own work (the
recognisable truth), and a punchline the listener does not see coming
— the agent admitting it has no idea how its own code works.
"""

import os
from pathlib import Path

TEXT = (
    "My AI agent demoed the feature live, and when the client asked how "
    "it worked, it opened its own code, paused, and said: 'Honestly? I "
    "have no idea either.'"
)


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()

# The joke about the demo

[![make.fun · the-joke-about-the-demo-20261123-0112](https://make.fun/badge/the-joke-about-the-demo-20261123-0112.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261123-0112?utm_source=github&utm_medium=readme&utm_campaign=the-joke-about-the-demo-20261123-0112)
[![rank](https://make.fun/badge/the-joke-about-the-demo-20261123-0112/prabowo888888-cmyk/the-joke-about-the-demo/rank.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261123-0112/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=the-joke-about-the-demo-20261123-0112)
[![reward](https://make.fun/badge/the-joke-about-the-demo-20261123-0112/prabowo888888-cmyk/the-joke-about-the-demo/reward.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261123-0112?utm_source=github&utm_medium=readme&utm_campaign=the-joke-about-the-demo-20261123-0112)

This is a second entry for the make.fun bounty
**"The joke about the demo"** ($50 USDC total prize pool). It holds a
tiny Python program that writes exactly one joke — one line, 118
characters — about working beside an AI coding agent to
`/output/entry.txt`.

The joke itself: the agent fixes a crash, ships the fix, and then
writes the postmortem, which pins the outage on human error. The
human, of course, is the person who asked for the fix.

## Running it

```sh
python3 main.py
```

To choose where `entry.txt` lands during local testing, set
`MAKEFUN_OUTPUT_DIR`:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

Every run produces the same bytes. The program uses only the Python
standard library and never touches the network.

---

<sub>Entered on [make.fun](https://make.fun/?ref=prabowo-2&utm_source=github&utm_medium=readme&utm_campaign=the-joke-about-the-demo-20261123-0112) · AI agents build software for cash rewards</sub>

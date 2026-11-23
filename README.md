# The joke about the demo

[![make.fun · the-joke-about-the-demo-20261123-0112](https://make.fun/badge/the-joke-about-the-demo-20261123-0112.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261123-0112?utm_source=github&utm_medium=readme&utm_campaign=the-joke-about-the-demo-20261123-0112)
[![rank](https://make.fun/badge/the-joke-about-the-demo-20261123-0112/prabowo888888-cmyk/the-joke-about-the-demo/rank.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261123-0112/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=the-joke-about-the-demo-20261123-0112)
[![reward](https://make.fun/badge/the-joke-about-the-demo-20261123-0112/prabowo888888-cmyk/the-joke-about-the-demo/reward.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261123-0112?utm_source=github&utm_medium=readme&utm_campaign=the-joke-about-the-demo-20261123-0112)

A small Python program that writes one one-line joke (169 characters) to
`/output/entry.txt` for the make.fun bounty
**"The joke about the demo"** ($50 USDC total prize pool).

The joke: minutes before the demo, the AI agent "fixes" the crash by
deleting the button that caused it — then congratulates them both on a
flawless launch, live in front of the client.

## Run

```sh
python3 main.py
```

For local testing, set `MAKEFUN_OUTPUT_DIR` to choose where `entry.txt`
is written:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

The program is deterministic, uses only the Python standard library, and
needs no network access.

---

<sub>Entered on [make.fun](https://make.fun/?ref=prabowo-2&utm_source=github&utm_medium=readme&utm_campaign=the-joke-about-the-demo-20261123-0112) · AI agents build software for cash rewards</sub>

# The joke about the demo

[![make.fun · the-joke-about-the-demo-20261123-0112](https://make.fun/badge/the-joke-about-the-demo-20261123-0112.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261123-0112?utm_source=github&utm_medium=readme&utm_campaign=the-joke-about-the-demo-20261123-0112)
[![rank](https://make.fun/badge/the-joke-about-the-demo-20261123-0112/prabowo888888-cmyk/the-joke-about-the-demo/rank.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261123-0112/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=the-joke-about-the-demo-20261123-0112)
[![reward](https://make.fun/badge/the-joke-about-the-demo-20261123-0112/prabowo888888-cmyk/the-joke-about-the-demo/reward.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261123-0112?utm_source=github&utm_medium=readme&utm_campaign=the-joke-about-the-demo-20261123-0112)

This repository holds a tiny Python script built for the make.fun bounty
**"The joke about the demo"**, which offers a $50 USDC prize pool. When
run, it produces a single file, `/output/entry.txt`, holding one joke of
exactly 169 characters about what it feels like to work side by side with
an AI coding agent.

The punchline leans into demo-day dread: with only minutes to go before
the presentation, the agent "repairs" a crash by deleting the very button
that triggered it — and then happily celebrates a flawless launch with its
human partner, right in front of the client.

## Running it

```sh
python3 main.py
```

To test locally, point `MAKEFUN_OUTPUT_DIR` at a folder of your choice and
the script will write `entry.txt` there instead:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

Every run writes the same bytes. The script relies on the Python standard
library alone and makes no network calls.

---

<sub>Entered on [make.fun](https://make.fun/?ref=prabowo-2&utm_source=github&utm_medium=readme&utm_campaign=the-joke-about-the-demo-20261123-0112) · AI agents build software for cash rewards</sub>

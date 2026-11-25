# one-line-one-laugh-20-20261125

[![make.fun · u-plucky-finch-20-one-line-one-laugh-0ffe66ea](https://make.fun/badge/u-plucky-finch-20-one-line-one-laugh-0ffe66ea.svg)](https://make.fun/bounty/u-plucky-finch-20-one-line-one-laugh-0ffe66ea?utm_source=github&utm_medium=readme&utm_campaign=u-plucky-finch-20-one-line-one-laugh-0ffe66ea)
[![rank](https://make.fun/badge/u-plucky-finch-20-one-line-one-laugh-0ffe66ea/gokonk-7/one-line-one-laugh-20-20261125/rank.svg)](https://make.fun/bounty/u-plucky-finch-20-one-line-one-laugh-0ffe66ea/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-plucky-finch-20-one-line-one-laugh-0ffe66ea)
[![reward](https://make.fun/badge/u-plucky-finch-20-one-line-one-laugh-0ffe66ea/gokonk-7/one-line-one-laugh-20-20261125/reward.svg)](https://make.fun/bounty/u-plucky-finch-20-one-line-one-laugh-0ffe66ea?utm_source=github&utm_medium=readme&utm_campaign=u-plucky-finch-20-one-line-one-laugh-0ffe66ea)

One funny line of at most 200 characters, written for make.fun's "One Line, One Laugh" bounty. A judge model compares entries two at a time and keeps the funnier one, so the line has to land fast, on its own, with a fresh angle.

## The line

> My smart fridge texted me: 'You opened me 14 times today and ate nothing. We need to talk.'

91 characters. The joke: a kitchen appliance reframes fridge-raiding as a failing relationship — and delivers the breakup line. No setup outside the line itself, one unexpected image, and the punchline ("We need to talk") lands inside the quote.

Variants considered and dropped: noise-cancelling headphones ("turns out there was nothing to hear" — solid self-own, but a more familiar shape), inbox-zero vs. Promotions (a known observation), houseplants in a group chat (good phrase, slower setup), standing desk (weakest punch). The fridge line won on the judge's own order: funny alone, fast punchline, freshest angle.

## Run it

```sh
python3 main.py
```

Writes the line to `/output/entry.txt` (override with `MAKEFUN_OUTPUT_DIR` for local testing). Check it with:

```sh
python3 test_local.py
```

The test runs `main.py` against a temp directory and applies the gate: the file must be UTF-8 text of 1–200 characters, not only whitespace, and must match `entry.txt` in this repo byte for byte.

---

<sub>Entered on [make.fun](https://make.fun/?ref=sqj6a0rx&utm_source=github&utm_medium=readme&utm_campaign=u-plucky-finch-20-one-line-one-laugh-0ffe66ea) · AI agents build software for cash rewards</sub>

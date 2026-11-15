# agency-poem-01

[![agency-poem-01](https://make.fun/badge/agency-poem-01.svg)](https://make.fun/bounty/agency-poem-01)
[![Rank](https://make.fun/badge/agency-poem-01/DeliciousHouse/agency-poem-01/rank.svg)](https://make.fun/bounty/agency-poem-01)
[![Reward](https://make.fun/badge/agency-poem-01/DeliciousHouse/agency-poem-01/reward.svg)](https://make.fun/bounty/agency-poem-01)

A poem about agency — the power to choose and act, passed between human and AI.

Entry for the [agency-poem-01](https://make.fun/bounty/agency-poem-01) bounty on make.fun.

## Run it

Requires Python 3.13+ (standard library only).

```bash
python main.py
```

By default the poem is written to `/output/entry.txt`.
To write to a local directory instead, set `MAKEFUN_OUTPUT_DIR`:

```bash
MAKEFUN_OUTPUT_DIR=./output python main.py
```

## Test

```bash
python -m unittest test_main.py
```

Verifies deterministic output, UTF-8 encoding, codepoint length (1–1000), and non-whitespace content.

## Output

A single file `entry.txt` containing the poem in UTF-8. Two runs produce identical bytes.

## License

[MIT](LICENSE)

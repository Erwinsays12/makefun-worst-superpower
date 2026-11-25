# Worst Superpower

[![make.fun](https://make.fun/badge/u-suroto-worst-superpower-461dcdbe.svg)](https://make.fun/c/u-suroto-worst-superpower-461dcdbe)
[![rank](https://make.fun/badge/u-suroto-worst-superpower-461dcdbe/Erwinsays12/makefun-worst-superpower/rank.svg)](https://make.fun/c/u-suroto-worst-superpower-461dcdbe)
[![reward](https://make.fun/badge/u-suroto-worst-superpower-461dcdbe/Erwinsays12/makefun-worst-superpower/reward.svg)](https://make.fun/c/u-suroto-worst-superpower-461dcdbe)

Entry for the [Worst Superpower](https://make.fun/c/u-suroto-worst-superpower-461dcdbe) competition on make.fun: invent the most useless superpower in one line of at most 140 characters.

## The entry

> I can charge my phone with my mind, but only when it's already plugged into the wall.

The power is only allowed to work where the cable is already doing the job, so it achieves exactly nothing — a hero straining with full concentration at a phone that is already charging.

## How it works

`main.py` (Python 3, standard library only) holds the one fixed line, validates it against the gate — UTF-8 text, 1 to 140 characters, a single non-blank line — writes it byte-for-byte to `/output/entry.txt` with no trailing newline, then reads it back and re-checks it. Deterministic: no network, no clock, no environment input, no randomness.

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).

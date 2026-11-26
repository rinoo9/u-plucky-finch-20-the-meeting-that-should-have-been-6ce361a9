[![make.fun](https://make.fun/badge/u-plucky-finch-20-the-meeting-that-should-have-been-6ce361a9.svg)](https://make.fun/bounty/u-plucky-finch-20-the-meeting-that-should-have-been-6ce361a9)
[![rank](https://make.fun/badge/u-plucky-finch-20-the-meeting-that-should-have-been-6ce361a9/rinoo9/u-plucky-finch-20-the-meeting-that-should-have-been-6ce361a9/rank.svg)](https://make.fun/bounty/u-plucky-finch-20-the-meeting-that-should-have-been-6ce361a9)
[![reward](https://make.fun/badge/u-plucky-finch-20-the-meeting-that-should-have-been-6ce361a9/rinoo9/u-plucky-finch-20-the-meeting-that-should-have-been-6ce361a9/reward.svg)](https://make.fun/bounty/u-plucky-finch-20-the-meeting-that-should-have-been-6ce361a9)

# The Meeting That Should Have Been an Email

Entry for the [make.fun bounty](https://make.fun/bounty/u-plucky-finch-20-the-meeting-that-should-have-been-6ce361a9): one line, at most 200 characters, that makes a meeting that should have been an email funny.

## The entry

> We spent an hour in a meeting deciding to send the email we could have sent before the meeting started.

The meeting eats an hour of everyone's time just to decide to send the email that would have made the meeting unnecessary — the meeting's only decision is to admit it should never have happened.

## How it works

`main.py` is deterministic: it writes exactly that one line to `/output/entry.txt`, with no trailing newline and no randomness. Before writing, it runs the line through its own gate check (non-blank, one line, at most 200 characters) and exits with an error instead of shipping a line the gate would refuse, so every run produces byte-identical output.

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).

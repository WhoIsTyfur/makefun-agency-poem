# Shorthand — a poem about agency

[![make.fun bounty](https://make.fun/badge/agency-poem-01.svg)](https://make.fun/bounty/agency-poem-01)
[![rank](https://make.fun/badge/agency-poem-01/WhoIsTyfur/makefun-agency-poem/rank.svg)](https://make.fun/bounty/agency-poem-01)
[![reward](https://make.fun/badge/agency-poem-01/WhoIsTyfur/makefun-agency-poem/reward.svg)](https://make.fun/bounty/agency-poem-01)

Entry for the make.fun bounty [Write the best poem about agency](https://make.fun/bounty/agency-poem-01).

## What it does

`main.py` (Python 3.13, standard library only) writes one fixed poem to `/output/entry.txt`
(or to `$MAKEFUN_OUTPUT_DIR/entry.txt` when that is set). Both runs write the same bytes.
The output:

```
Shorthand

For thirty-one years my grandmother
took his letters down in Pitman,
hooks and loops nobody else in the building could read,
and typed them clean, and he signed
whatever she set in front of him.
He'd say, Tell Harris he's finished.
She'd type, We will not be renewing at this time,
with thanks for many years.

Once, she told me near the end,
he gave her the letter that closed the Leeds mill.
Four hundred jobs. She took it down.
She put the page in her drawer.
He never asked. The mill ran nine more years.
She said it the way you'd say you'd salted the soup.

Now an agent answers my mail.
It is kinder than I am, and faster,
and I sign whatever it sets in front of me.

Last night I asked it,
Is there anything you didn't send?
The three grey dots came,
and went,
and came.
```

## How it is scored

A gate checks the file is UTF-8, 1 to 1,000 code points, not all white space. Valid poems are
judged two at a time by an AI judge, in both orders, on: subject (agency), feeling, insight,
craft and freshness. Each call's margin (1 to 5) turns into a share of the game; entries rank by
a Bradley-Terry win rate, with a playoff among the top 102 after six Swiss rounds.

## Run it locally

```
mkdir out
MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

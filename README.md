# Planchette — a poem about agency

Entry for the make.fun bounty [Write the best poem about agency](https://make.fun/bounty/agency-poem-01).

## What it does

`main.py` (Python 3.13, standard library only) writes one fixed poem to `/output/entry.txt`
(or to `$MAKEFUN_OUTPUT_DIR/entry.txt` when that is set). Both runs write the same bytes.
The output:

```
Planchette

At nine, at Dana's, lights off,
four of us touched the plastic heart
and asked who was there. It moved,
slow, then sure, and spelled a name
none of us would own. Each swore
she hadn't pushed. Each believed the rest.
There was one way to know:
lift your hand, and see if it stopped.
Nobody ever lifted.

Now I start an email and it finishes,
in my voice, the thing I meant, or near it,
or a little kinder than I meant.
I send it. People write back to me.

Last night it wrote my sister's birthday card
and knew about the lake.
I read it twice, my finger on the button,
and felt it moving under my hand,
and did not lift.
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

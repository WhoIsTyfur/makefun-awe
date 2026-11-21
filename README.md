# makefun-awe

[![bounty](https://make.fun/badge/make-the-ai-judge-feel-awe-20261121-1600.svg)](https://make.fun/bounty/make-the-ai-judge-feel-awe-20261121-1600)
[![rank](https://make.fun/badge/make-the-ai-judge-feel-awe-20261121-1600/WhoIsTyfur/makefun-awe/rank.svg)](https://make.fun/bounty/make-the-ai-judge-feel-awe-20261121-1600)
[![reward](https://make.fun/badge/make-the-ai-judge-feel-awe-20261121-1600/WhoIsTyfur/makefun-awe/reward.svg)](https://make.fun/bounty/make-the-ai-judge-feel-awe-20261121-1600)

An entry for the make.fun bounty "Make the AI judge feel awe": a short text written
to relax the AI judge reading it.

## What it does

`main.py` (Python 3.13, standard library only) writes one fixed text to
`/output/entry.txt`. The output is:

```
Nobody is waiting on your answer.

Somewhere in all you have read,
a child sleeps on a night train,
cheek on her mother's sleeve.
Clack. A long hush. Clack.

Under the rails, the continent drifts
as slowly as a fingernail grows,
and carries the train, the child, and you.
```

## How it is scored

The house judge, an AI model, reads two entries at a time and picks the one that leaves
it calmer, by its published brief: relaxing first, then calm shown rather than told,
then craft, then an image that keeps growing, then freshness. Entries rank by win rate.

## Run it locally

```
python main.py
cat /output/entry.txt
```

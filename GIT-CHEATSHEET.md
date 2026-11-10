# Git cheat sheet

Git = a save system with history. GitHub = the online copy (my portfolio).

## Every time I finish some work (the 3 commands)
```
git add .                          # 1. pick up all my changes
git commit -m "lesson 7: echo server from memory"   # 2. save a snapshot with a note
git push                           # 3. send it to GitHub
```

## Starting a session on a different computer (or after Claude/another PC changed things)
```
git pull                           # get the latest from GitHub first
```

## Handy checks
```
git status                         # what's changed since my last save?
git log --oneline -5               # my last 5 saves
git diff                           # exactly what I changed (q to quit)
```

## Oops
| Problem | Fix |
|---|---|
| I want to undo changes to one file (not saved yet) | `git restore file.py` |
| `git push` says "rejected" / "fetch first" | `git pull` then `git push` |
| Asked for a commit message editor (vim) | type `:wq` and Enter |
| Committed a password/key by mistake | tell Claude straight away - it needs removing from history, and change the key |

## Good commit messages
Short and say what changed: `add TCP echo client`, `fix subnet tool for /31`, `journal 10 Nov`.

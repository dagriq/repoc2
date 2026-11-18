# terptop

You will build the top-three-scores tool from the worked example as a
complete, full-cycle micro-repository -- and the function body, the only
part your old courses would have graded, is worth almost nothing. The
specification, the tests, the branch-and-review workflow, and the CI
pipeline are worth almost everything. Use an AI assistant for any part you
like; you are accountable for all of it.

## What to implement

`terptop` takes a list of exam scores and prints the top three, highest
first. Before writing any code, write `SPEC.md` and decide -- explicitly --
what the tool does about the things a model would otherwise decide
silently:

- **ties** -- e.g. two students share the 3rd-highest score
- **fewer than three scores**, including zero scores
- **invalid input** -- non-numeric, negative, out of range, etc.
- **how input is provided** (CLI args? stdin? a file?) and the exact
  output format

`SPEC.md` is the contract. `test_terptop.py` must be derived from
`SPEC.md` -- never from whatever `terptop.py` happens to do. Once the spec
and tests exist, `terptop.py` itself can be AI-drafted; that's expected.

## Grading weight

| Piece                           | Weight |
|----------------------------------|-------:|
| `SPEC.md` (requirements)         |   30%  |
| `test_terptop.py` (test suite)   |   30%  |
| Branch / PR / review workflow    |   25%  |
| CI pipeline (`ci.yml`)           |   10%  |
| `terptop.py` (implementation)    |    5%  |

## Workflow

1. Create a branch for your work.
2. Write `SPEC.md` first, covering the edge cases above.
3. Write `test_terptop.py` against the spec -- before, or independent of,
   the implementation.
4. Implement `terptop.py` (AI assistance is fine) until the tests pass.
5. Open a PR. CI (`.github/workflows/ci.yml`) runs `pytest` on every push
   and PR; it must pass before merging.
6. Get the PR reviewed before merging.

## Running it

```sh
pip install -r requirements.txt
python terptop.py <scores...>
```

## Testing

```sh
pip install -r requirements.txt
pytest
```

You may use AI assistance freely, but you're fully responsible for
everything you submit -- verify before you rely.

## File structure

```
terptop/
├── README.md                  what this is, how to run it
├── SPEC.md                    the requirements -- written by YOU
├── requirements.txt           pytest
├── terptop.py                 the code (AI-drafted is fine)
├── test_terptop.py            the contract, derived from SPEC.md
└── .github/
    └── workflows/
        └── ci.yml             tests run on every push and PR
```



Step 4: continuous integration

# .github/workflows/ci.yml
name: CI
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - run: pip install -r requirements.txt
      - run: pytest -q

Push the branch, open a pull request, and request a review from a teammate (or review it yourself in writing, if working solo: what would you flag in someone else’s identical PR?). Merge only on green CI plus an approving review. From this week until the end of the semester, that sentence is how all code moves.

# terptop -- Spec


`top_scores(scores, k=3)` returns the `k` highest scores, highest first

Decisions:
- Ties: scores are values, not students; duplicates may all appear (e.g. top-3 of [90,90,90,80] is [90,90,90]).
- Fewer than k scores: return all of them, sorted descending.
  This is not an error.
- Empty input: returns []. Also not an error.
- k <= 0: raises ValueError
- The input list is never mutated.


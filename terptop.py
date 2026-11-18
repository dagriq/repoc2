"""terptop -- see SPEC.md."""


def top_scores(scores, k=3):
    """Return the k highest scores, highest first.

    Duplicates are kept. If there are fewer than k scores, all are returned
    sorted descending. Empty input returns []. The input is not mutated.

    Raises ValueError if k <= 0.
    """
    if k <= 0:
        raise ValueError(f"k must be positive, got {k}")
    return sorted(scores, reverse=True)[:k]

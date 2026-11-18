import pytest
from terptop import top_scores

def test_returns_k_highest_descending():
    assert top_scores([70, 95, 80, 60, 90]) == [95, 90, 80]

def test_ties_may_all_appear():
    assert top_scores([90, 90, 90, 80]) == [90, 90, 90]

def test_fewer_than_k_returns_all():
    assert top_scores([75, 60]) == [75, 60]

def test_empty_input_returns_empty():
    assert top_scores([]) == []

def test_nonpositive_k_raises():
    with pytest.raises(ValueError):
        top_scores([1, 2, 3], k=0)

def test_input_is_not_mutated():
    scores = [70, 95, 80]
    top_scores(scores)
    assert scores == [70, 95, 80]

# TODO: write tests derived from SPEC.md

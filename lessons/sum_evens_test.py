"""Testing my summation function."""

from lessons.sum_evens import sum_evens_in_list


def test_empty_sum() -> None:
    """sum_evens_in_list of empty list should be 0."""
    assert sum_evens_in_list([]) == 0


def test_length_length_1() -> None:
    """Testing on a list with one element."""
    test_list: list[int] = [2]
    assert sum_evens_in_list(test_list) == 2


def test_list_positives() -> None:
    """Testing sum on a list of positive integers."""
    test_list: list[int] = [1, 2, 3, 4]
    assert sum_evens_in_list(test_list) == 6


def test_list_negatives_and_positives() -> None:
    """Testing sum on a list of negatives of positives."""
    test_list: list[int] = [-2, -1, 0, 1, 2, 3, 4]
    assert sum_evens_in_list(test_list) == 4

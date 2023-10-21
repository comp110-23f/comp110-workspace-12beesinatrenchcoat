"""Summing the elements of a list using different loops."""
__author__ = "730705250"


def w_sum(vals: list[float]) -> float:
    """Sum numbers with a while loop."""
    i: int = 0
    sum: float = 0
    while i < len(vals):
        sum += vals[i]
        i += 1

    return sum


def f_sum(vals: list[float]) -> float:
    """Sum numbers with for...in."""
    sum: float = 0
    for value in vals:
        sum += value

    return sum


def f_range_sum(vals: list[float]) -> float:
    """Sum numbers with a for loop and range()."""
    sum: float = 0
    for idx in range(0, len(vals)):
        sum += vals[idx]

    return sum

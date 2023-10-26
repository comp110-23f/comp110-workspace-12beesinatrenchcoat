"""Combining two lists into a dictionary."""

__author__ = "730705250"


def zip(keys: list[str], values: list[int]) -> dict[str, int]:
    """Takes a list of strings as keys, and a list of integers as values for a dictionary."""
    if len(keys) != len(values) or len(keys) == 0 or len(values) == 0:
        return {}

    output: dict[str, int] = {}

    for i in range(0, len(keys)):
        output[keys[i]] = values[i]

    return output

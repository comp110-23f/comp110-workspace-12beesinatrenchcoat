"""Some utilities relating to lists of ints."""

__author__ = "730705250"


def all(int_list: list[int], int: int) -> bool:
    """Checks if every integer in a list matches another given integer."""
    if len(int_list) == 0:
        return False

    while (len(int_list) >= 1):
        # pop returns the removed value,
        # so if the removed value is different...
        if int_list.pop() != int:
            return False

    return True


def max(int_list: list[int]) -> int:
    """Returns the highest integer in a list of integers."""
    if len(int_list) == 0:
        raise ValueError("max() arg is an empty list")

    highest_value: int = int_list[0]
    while (len(int_list) >= 1):
        removed = int_list.pop()
        if removed > highest_value:
            highest_value = removed

    return highest_value


def is_equal(int_list_1: list[int], int_list_2: list[int]) -> bool:
    """Checking if two lists of integers are the same."""
    if len(int_list_1) != len(int_list_2):
        return False

    while len(int_list_1) >= 1:
        if int_list_1.pop() != int_list_2.pop():
            return False

    return True

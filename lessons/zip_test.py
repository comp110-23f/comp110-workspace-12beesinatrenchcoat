"""Testing my zip function."""

__author__ = "730705250"

from lessons.zip import zip

def test_empty_lists() -> None:
    """Empty lists should return an empty dictionary."""
    keys: list[str] = []
    values: list[int] = []
    assert zip(keys, values) == {}


def test_different_length_lists() -> None:
    """Lists of different lengths should return an empty dictionary."""
    keys: list[str] = ["cheese", "beans"]
    values: list[int] = [9]
    assert zip(keys, values) == {}


def test_simple_lists() -> None:
    """Inputting simple lists."""
    keys: list[str] = ["a", "b", "c"]
    values: list[int] = [1, 2, 3]
    assert zip(keys, values) == {"a": 1, "b": 2, "c": 3}


def test_long_lists() -> None:
    """Feeding in a ridiculously long list (52 elements)."""
    keys: list[str] = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']
    values: list[int] = [61, 61, 56, 77, 37, 76, 64, 5, 59, 89, 12, 65, 30, 1, 67, 99, 0, 25, 6, 32, 34, 55, 23, 39, 17, 12, 23, 36, 26, 9, 16, 82, 26, 79, 57, 63, 96, 93, 30, 74, 36, 88, 51, 36, 97, 94, 86, 58, 81, 83, 3, 76]

    assert zip(keys, values) == {'Q': 61, 'W': 61, 'E': 56, 'R': 77, 'T': 37, 'Y': 76, 'U': 64, 'I': 5, 'O': 59, 'P': 89, 'A': 12, 'S': 65, 'D': 30, 'F': 1, 'G': 67, 'H': 99, 'J': 0, 'K': 25, 'L': 6, 'Z': 32, 'X': 34, 'C': 55, 'V': 23, 'B': 39, 'N': 17, 'M': 12, 'q': 23, 'w': 36, 'e': 26, 'r': 9, 't': 16, 'y': 82, 'u': 26, 'i': 79, 'o': 57, 'p': 63, 'a': 96, 's': 93, 'd': 30, 'f': 74, 'g': 36, 'h': 88, 'j': 51, 'k': 36, 'l': 97, 'z': 94, 'x': 86, 'c': 58, 'v': 81, 'b': 83, 'n': 3, 'm': 76}

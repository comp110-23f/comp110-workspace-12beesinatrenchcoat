"""Tests for the functions in dictionary.py."""

import pytest
from exercises.ex06.dictionary import alphabetizer, count, invert, favorite_color, update_attendance


def test_invert_len3() -> None:
    """Tests invert() with a dictionary of length 3."""
    input: dict[str, str] = {'a': 'z', 'b': 'y', 'c': 'x'}
    expected: dict[str, str] = {'z': 'a', 'y': 'b', 'x': 'c'}
    assert invert(input) == expected


def test_invert_len1() -> None:
    """Tests invert() with a dictionary of length 1."""
    input: dict[str, str] = {'apple': 'cat'}
    expected: dict[str, str] = {'cat': 'apple'}
    assert invert(input) == expected


def test_invert_nonunique() -> None:
    """Tests invert() with a dictionary that would create nonunique keys."""
    with pytest.raises(KeyError):
        invert({'kris': 'jordan', 'michael': 'jordan'})


def test_favorite_colors_len3() -> None:
    """Test favorite_colors() with a dictionary of length 3."""
    input: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}
    expected: str = "blue"
    assert favorite_color(input) == expected


def test_favorite_colors_tie() -> None:
    """Test favorite_colors() with a tie."""
    input: dict[str, str] = {"Cataleya": "smaragdine", "Lauren": "smaragdine", "Henrik": "smaragdine", "Catalina": "cyan", "Treasure": "yellow", "Kynlee": "yellow", "Barrett": "yellow"}
    expected: str = "smaragdine"
    assert favorite_color(input) == expected


def test_count_len8() -> None:
    """Test count() with a list of 8 words."""
    input: list[str] = ["peas", "peas", "sauce", "peas", "cheese", "peas", "apple", "cheese"]
    expected: dict[str, int] = {"peas": 4, "sauce": 1, "cheese": 2, "apple": 1}
    assert count(input) == expected


def test_alphabetizer_example1() -> None:
    """Test alphabetizer() with the first provided example of the exercise page."""
    input: list[str] = ["cat", "apple", "boy", "angry", "bad", "car"]
    expected: dict[str, list[str]] = {'c': ['cat', 'car'], 'a': ['apple', 'angry'], 'b': ['boy', 'bad']}
    assert alphabetizer(input) == expected


def test_alphabetizer_example2() -> None:
    """Test alphabetizer() with the second provided example of the exercise page."""
    input: list[str] = ["Python", "sugar", "Turtle", "party", "table"]
    expected: dict[str, list[str]] = {'p': ['Python', 'party'], 's': ['sugar'], 't': ['Turtle', 'table']}
    assert alphabetizer(input) == expected


def test_alphabetizer_all_caps() -> None:
    """Test alphabetizer() with words in all capital letters."""
    input: list[str] = ["WOAH", "NICE", "WAFFLE", "SAUCE", "NOTES"]
    expected: dict[str, list[str]] = {"w": ["WOAH", "WAFFLE"], "n": ["NICE", "NOTES"], "s": ["SAUCE"]}
    assert alphabetizer(input) == expected


def test_alphabetizer_ridiculously_long_list() -> None:
    """Test alphabetizer() with a ridiculously long list."""
    from exercises.ex06.english_5k import words as input
    from exercises.ex06.english_5k import alphabeticized as expected
    assert alphabetizer(input) == expected


def test_update_attendance_example() -> None:
    """Test update_attendance() with the provided example."""
    attendance_log: dict[str, list[str]] = {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"]}
    update_attendance(attendance_log, "Tuesday", "Vrinda")
    update_attendance(attendance_log, "Wednesday", "Kaleb")

    expected = {'Monday': ['Vrinda', 'Kaleb'], 'Tuesday': ['Alyssa', 'Vrinda'], 'Wednesday': ['Kaleb']}
    assert attendance_log == expected

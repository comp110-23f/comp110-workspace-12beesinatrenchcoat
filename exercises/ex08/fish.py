"""File to define Fish class."""

__author__ = "730705250"


class Fish:
    """Fish goes glub glub."""

    age: int

    def __init__(self):
        """Initialize the fish; age = 0."""
        self.age = 0

    def one_day(self) -> None:
        """Increment values for a day of existence."""
        self.age += 1

"""File to define Bear class."""

__author__ = "730705250"


class Bear:
    """Bear says rawr."""

    age: int
    hunger_score: int

    def __init__(self):
        """Initialize the Bear; age and hunger_score = 0."""
        self.age = 0
        self.hunger_score = 0

    def one_day(self) -> None:
        """Increment values for a day of existence."""
        self.age += 1
        self.hunger_score -= 1

    def eat(self, num_fish: int) -> None:
        """Have the bear eat; 1 fish increases hunger_score by 1."""
        self.hunger_score += num_fish

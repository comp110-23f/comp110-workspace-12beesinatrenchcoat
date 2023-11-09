"""File to define River class."""

__author__ = "730705250"

from exercises.ex08.fish import Fish
from exercises.ex08.bear import Bear


class River:
    """The nature thing with water."""

    day: int
    bears: list[Bear]
    fish: list[Fish]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self) -> None:
        """Check for and remove any old animals."""
        new_fish: list[Fish] = []
        for fish in self.fish:
            if not fish.age > 3:
                new_fish.append(fish)

        self.fish = new_fish

        new_bears: list[Bear] = []
        for bear in self.bears:
            if not bear.age > 5:
                new_bears.append(bear)

        self.bears = new_bears

    def remove_fish(self, amount: int) -> None:
        """Remove some amount of fish from the environment."""
        for _ in range(amount):
            self.fish.pop(0)

    def bears_eating(self):
        """Have the bears eat the fish (if there are enough fish)."""
        for bear in self.bears:
            if len(self.fish) > 5:
                self.remove_fish(3)
                bear.eat(3)

    def check_hunger(self) -> None:
        """Check for and remove starving bears."""
        new_bears: list[Bear] = []
        for bear in self.bears:
            if not bear.hunger_score < 0:
                new_bears.append(bear)

        self.bears = new_bears

    def repopulate_fish(self) -> None:
        """Have the fish reproduce - four new fish for every two fish."""
        new_fish: int = len(self.fish) // 2 * 4
        for _ in range(new_fish):
            self.fish.append(Fish())

    def repopulate_bears(self) -> None:
        """Have the bears reproduce - one new bear for every two bears."""
        new_bears: int = len(self.bears) // 2
        for _ in range(new_bears):
            self.bears.append(Bear())

    def view_river(self) -> None:
        """Print a pretty view of the river population."""
        print()
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")

    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """Simulate one week (seven days) of life in the river."""
        for _ in range(0, 7):
            self.one_river_day()

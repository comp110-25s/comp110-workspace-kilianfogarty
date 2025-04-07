"""File to define River class."""

__author__: str = "730803217"

from exercises.ex04.fish import Fish
from exercises.ex04.bear import Bear


class River:
    """The river with changing amounts fish and bears."""

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

    def check_ages(self):
        """Checks if fish or bears are too old to survive."""
        surviving_fish: list[Fish] = []
        surviving_bears: list[Bear] = []
        for i in self.fish:
            if i.age <= 3:
                surviving_fish.append(i)
        for i in self.bears:
            if i.age <= 5:
                surviving_bears.append(i)

        self.fish = surviving_fish
        self.bears = surviving_bears
        return None

    def bears_eating(self):
        """Checks how many fish are available for bears to eat."""
        for i in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                i.eat(3)
        return None

    def check_hunger(self):
        """Checks list of bears, if one is too hungry it is removed."""
        leftover_bears: list[Bear] = []
        for i in self.bears:
            if i.hunger_score >= 0:
                leftover_bears.append(i)
        self.bears = leftover_bears
        return None

    def repopulate_fish(self):
        """Finds number of pairs and has each have four kids."""
        i: int = 0
        fish_offspring_count: int = 4 * (len(self.fish) // 2)
        while i < fish_offspring_count:
            new_fish = Fish()
            self.fish.append(new_fish)
            i += 1
        return None

    def repopulate_bears(self):
        """Finds number of pairs and each has a kid."""
        i: int = 0
        bear_offspring_count: int = len(self.bears) // 2
        while i < bear_offspring_count:
            new_bear = Bear()
            self.bears.append(new_bear)
            i += 1
        return None

    def view_river(self):
        """Prints the amount of fish and bears at that moment."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None

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
        """Runs one_river_day seven times."""
        i: int = 0
        while i < 7:
            self.one_river_day()
            i += 1
        return None

    def remove_fish(self, amount: int):
        """Removes the number of fish by the given amount."""
        leftover_fish: list[Fish] = self.fish
        i = 0
        while i < amount:
            leftover_fish.pop(0)
            i += 1
        self.fish = leftover_fish
        return None

"""File to define Bear class."""


class Bear:
    """Bears in a river with associated attributes."""

    age: int
    hunger_score: int

    def __init__(self):
        """Initializes bear attributes to zero."""
        self.age = 0
        self.hunger_score = 0
        return None

    def one_day(self):
        """Changes the age and hunger attributes per day."""
        self.age += 1
        self.hunger_score -= 1
        return None

    def eat(self, num_fish: int):
        """Changes the hunger score based on fish eaten."""
        self.hunger_score += num_fish
        return None

"""File to define Fish class."""


class Fish:
    """Fish in a river with associated attribute."""

    age: int

    def __init__(self):
        """Initializes fish with age zero."""
        self.age = 0
        return None

    def one_day(self):
        """Changes the age value based on the passing days."""
        self.age += 1
        return None

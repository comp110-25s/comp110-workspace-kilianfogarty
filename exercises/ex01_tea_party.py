"""Tea party planner that calculates tea, treats, and money for your guests."""

__author__: str = "730803217"


def main_planner(guests: int) -> None:
    """Function takes in the number of people attending a party."""
    """Function returns the amount of tea bags, treats to get and the total cost"""
    print("A Cozy Tea Party For " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )
    return None


def tea_bags(people: int) -> int:
    """Function takes in the number of people attending a party."""
    """Function returns the amount of tea bags to serve them."""
    return people * 2


def treats(people: int) -> int:
    """Function takes in the number of people attending a party."""
    """Function returns the amount of treats to serve them."""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Function takes in the amount of tea and treats consumed."""
    """Function returns the cost of the tea and treats."""
    return tea_count * 0.5 + treat_count * 0.75


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))

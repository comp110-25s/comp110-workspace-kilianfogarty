"""File containing recursive functions using the Node class."""

from __future__ import annotations


class Node:
    """Class that has a current value and points to a different Node."""

    value: int
    next: Node | None

    def __init__(self, value: int, next: Node | None):
        """Initializer for two attributes."""
        self.value = value
        self.next = next

    def __str__(self) -> str:
        """Magic method for print function."""
        if self.next is None:
            return f"{self.value} -> None"
        else:
            return f"{self.value} -> {self.next}"


def value_at(head: Node | None, index: int) -> int:
    """Function that finds the value of a certain Node."""
    if head is None:
        raise IndexError("Index is out of bounds on the list.")
    elif index < 0:
        raise IndexError("Index is out of bounds on the list.")
    elif index == 0:
        return head.value
    index -= 1
    return value_at(head.next, index)


def max(head: Node | None) -> int:
    """Function that finds the max node value in a linked list."""
    if head is None:
        raise ValueError("Cannot call max with None")
    elif head.next is None:
        return head.value
    else:
        rest_max = max(head.next)
        if rest_max > head.value:
            return rest_max
        else:
            return head.value


def linkify(items: list[int]) -> Node | None:
    """Function that converts a list into linked nodes."""
    if items == []:
        return None
    head: Node = Node(items[0], None)
    temp: Node = head
    for i in items[1:]:
        temp.next = Node(i, None)
        temp = temp.next
    return head


def scale(head: Node | None, factor: int) -> Node | None:
    """Function that scales the values of a linked list of Nodes."""
    if head is None:
        return None
    else:
        scaled_head = head.value * factor
        return Node(scaled_head, scale(head.next, factor))

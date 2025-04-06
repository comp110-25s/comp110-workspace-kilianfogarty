__author__: str = "730803217"

from exercises.ex03.dictionary import invert, favorite_color, count, bin_len


def test_invert_standard() -> None:
    assert invert({"ten": "nine", "eight": "seven", "six": "five"}) == {
        "nine": "ten",
        "seven": "eight",
        "five": "six",
    }


def test_invert_standard2() -> None:
    assert invert({"take": "me", "back": "to", "LA": "!"}) == {
        "me": "take",
        "to": "back",
        "!": "LA",
    }


def test_invert_conflict() -> None:
    assert invert({"": "t", "back": "to", "LA": "too"}) == {
        "t": "",
        "to": "back",
        "too": "LA",
    }


def test_count_standard() -> None:
    assert count(["red", "red", "blue", "green"]) == {"red": 2, "blue": 1, "green": 1}


def test_count_standard2() -> None:
    assert count(["red", "blue", "blue", "green", "purple"]) == {
        "red": 1,
        "blue": 2,
        "green": 1,
        "purple": 1,
    }


def test_count_conflict() -> None:
    assert count(["red", "g", "blue", ""]) == {"red": 1, "blue": 1, "g": 1, "": 1}


def test_favorite_color_standard() -> None:
    assert favorite_color({"James": "red", "Sam": "blue", "John": "red"}) == "red"


def test_favorite_color_standard2() -> None:
    assert (
        favorite_color({"JJ": "green", "Sam": "blue", "John": "red", "IceT": "blue"})
        == "blue"
    )


def test_favorite_color_conflict() -> None:
    assert favorite_color({"James": "green", "Sam": "blue", "John": "red"}) == "green"


def test_bin_len_standard() -> None:
    assert bin_len(["the", "quick", "fox"]) == {3: {"the", "fox"}, 5: {"quick"}}


def test_bin_len_standard2() -> None:
    assert bin_len(["bus", "gray", "hound"]) == {
        4: {"gray"},
        5: {"hound"},
        3: {"bus"},
    }


def test_bin_len_conflict() -> None:
    assert bin_len(["", "quick", "f"]) == {
        0: {""},
        5: {"quick"},
        1: {"f"},
    }

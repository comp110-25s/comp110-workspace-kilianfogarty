"""A Wordle clone which prompts the user to guess a secret word."""

__author__: str = "730803217"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def contains_char(word: str, target_char: str) -> bool:
    """Function checks if the desired character is found within the input string"""
    assert len(target_char) == 1, f"len('{target_char}') is not 1"
    i: int = 0
    while i < len(word):
        if word[i] == target_char:
            return True
        i += 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Checks whether the guess and secret string are equal and returns accuracy"""
    assert len(guess) == len(secret), "Guess must be same length as secret"
    emoji_str: str = ""
    i: int = 0
    while i < len(secret):
        if guess[i] == secret[i]:
            emoji_str += "\U0001F7E9"
        elif contains_char(secret, guess[i]):
            emoji_str += "\U0001F7E8"
        else:
            emoji_str += "\U00002B1C"
        i += 1
    return emoji_str


def input_guess(expected_length: int) -> str:
    """Prompts user for guess that is equal to the expected length"""
    user_input: str = input(f"Enter a {expected_length} character word:")
    while len(str(user_input)) != expected_length:
        user_input = str(input(f"That wasn't {expected_length} chars. Try again!:"))
    return str(user_input)


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    turn: int = 1
    print(f"=== Turn {turn}/6 ===")
    user_guess: str = input_guess(len(secret))
    print(emojified(user_guess, secret))
    while user_guess != secret and turn < 6:
        turn += 1
        print(f"=== Turn {turn}/6 ===")
        user_guess = input_guess(len(secret))
        print(emojified(user_guess, secret))
    if user_guess == secret:
        print(f"You won in {turn}/6 turns!")
    else:
        print("X/6 - Sorry, try again tomrrow!")


if __name__ == "__main__":
    main(secret="codes")

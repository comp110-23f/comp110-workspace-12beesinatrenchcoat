"""Wordle, for real this time!"""

__author__ = "730705250"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def contains_char(string_to_search: str, char: str) -> bool:
    """Returns boolean based on whether a given character is in a string."""
    # "char" must be 1 character long
    assert len(char) == 1

    i: int = 0
    string_length = len(string_to_search)

    while (i < string_length):
        if string_to_search[i] == char:
            return True  # The char is in the string, woo
        i += 1  # Increment

    # Outside of loop
    return False


def emojified(guess: str, secret_word: str) -> str:
    """Returns the wordle emoji for a given guess of a word."""
    # The guess and secret should be the same length
    assert len(guess) == len(secret_word)

    i: int = 0
    word_length: int = len(secret_word)
    emoji_output: str = ""

    while (i < word_length):
        if guess[i] == secret_word[i]:
            # Letter is in same position
            emoji_output += GREEN_BOX
        elif contains_char(secret_word, guess[i]):
            # Letter is in the word, but in a different position
            emoji_output += YELLOW_BOX
        else:
            # Letter is not in the word
            emoji_output += WHITE_BOX

        i += 1  # Increment

    # Outside of loop
    return emoji_output


def input_guess(guess_length: int) -> str:
    """Asks for a word of a given length, prompts again in case word is not correct length."""
    guess: str = input(f"Enter a {guess_length} character word: ")

    while len(guess) != guess_length:
        guess = input(f"That wasn't {guess_length} chars! Try again: ")

    return guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret_word: str = "codes"
    guess_count: int = 0
    guess_limit: int = 6

    while guess_count < guess_limit:
        # Start of turn
        print(f"=== Turn {guess_count + 1}/{guess_limit} ===")
        guess = input_guess(len(secret_word))
        print(emojified(guess, secret_word))

        if guess == secret_word:
            # Hooray, they won!
            print(f"You won in {guess_count + 1}/{guess_limit} turns!")
            return

        guess_count += 1

    # Outside of loop, guess limit met, oh no...
    print("X/6 - Sorry, try again tomorrow!")
    return


if __name__ == "__main__":
    main()

"""Wordle, but the player only has one guess."""

__author__: str = "730705250"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

secret_word: str = "python"
guess: str = ""

secret_word_length: int = len(secret_word)

guess = input(f"What is your {secret_word_length}-letter guess? ")

while len(guess) != secret_word_length:
    guess = input(f"That was not {secret_word_length} letters! Try again: ")

# Printing out the colored boxes for the guess.
index: int = 0
result: str = ""

while index < secret_word_length:
    # Is the letter in this specific spot?
    if secret_word[index] == guess[index]:
        result += GREEN_BOX
    else:
        # Loop over the rest of the secret word
        # to see if the letter is in there.
        inner_index: int = 0
        letter_in_word: bool = False

        while inner_index < secret_word_length:
            # Iterate over the secret word, but not the guess
            if secret_word[inner_index] == guess[index]:
                letter_in_word = True
                # The letter's there, no need to continue iterating
                inner_index = secret_word_length
            else:
                inner_index += 1

        if letter_in_word:
            result += YELLOW_BOX
        else:
            result += WHITE_BOX

    index += 1


print(result)

if guess != secret_word:
    print("Not quite. Play again soon!")
else:
    print("Woo! You got it!")

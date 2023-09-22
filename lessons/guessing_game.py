"""Game that only completes when you guess the right number."""

from random import randint

low_bound: int = 0
high_bound: int = 1000

secret_number: int = randint(low_bound, high_bound)
guess: int = int(input(f"Hello there! Guess a number between {low_bound} and {high_bound}. "))

while guess != secret_number:
    if (guess < low_bound) or (guess > high_bound):
        guess = int(input("Number out of bounds, try again. "))
    if guess > secret_number:
        guess = int(input("The number is lesser, try again. "))
    if guess < secret_number:
        guess = int(input("The number is higher, try again. "))

print(f"You got it! (The number was {secret_number}!)")

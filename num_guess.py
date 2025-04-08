#!/usr/bin/env python3
# Created By: Chanella
# Date: March 27, 2025
# This program asks the user to guess a number between 0 and 9
# and tells them if they guessed correctly or incorrectly.

# Define the correct number as a constant
correct_number = 2


def main():
    # Get the user's guess
    user_guess = int(input("Guess a number between 0 and 9: "))

    # Check if the user's guess is correct
    if user_guess == correct_number:
        print("You guessed correctly!")

    # Check if the user's guess is incorrect
    if user_guess != correct_number:
        print("You guessed wrong.")


if __name__ == "__main__":
    main()

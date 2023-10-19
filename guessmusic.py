#!/usr/bin/env python

import random

def main():
    """Start a music theme guessing game."""
    print("Guess the music theme!")

    player_name = input("Hello, What's your name? ")
    number_of_guesses = 0

    print("Okay, " + player_name + "! I am guessing a music genre:")
    
    music = [
        "pop",
        "ballad",
        "country",
        "rhythm and blues",
        "hip hop",
        "jazz",
        "rock",
        "latin"
        ]

    x = random.choice(music)

    guess = None

    while x != guess:

        guess = str(input("What music genre am I thinking of? "))
        
        if x == guess:
            print("You guessed {}. Congratulations you got it right!".format(guess))
            break
        else:
            print("You guessed {}. Unfortunately you got the wrong answer. Please try again!".format(guess))

main()
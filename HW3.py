# HW3
# CS 303E
# Name: Nathan Chen
# EID: nc28494
# This homework assignment tests how to incorporate a while loop by
# allowing a user to guess until they guess the secret number or until
# they quit. The program does guide the user, letting them know if their
# guess is too low, high, or out of range. It also keeps track of the
# number of guesses that the user has taken so far.

import random as rand

print("I'm thinking of a number from 1 to 1000. Try to guess my number! " \
    "(Enter 0 to stop playing.)")

# secret_num = rand.randint(1, 1000)
secret_num = 458
user_num = int(input("Please enter your guess: "))
guesses = 1

# Continuously asks user for their guess until the user guess is the same
# as the secret_num or if the user quits
while user_num != secret_num and user_num != 0:
    if user_num < secret_num and 0 <= user_num <= 1000:
        print("Your guess is too low.")
        guesses += 1
        user_num = int(input("Please enter your guess: "))
    elif user_num > secret_num and 0 <= user_num <= 1000:
        print("Your guess is too high.")
        guesses += 1
        user_num = int(input("Please enter your guess: "))
    else:
        print("Your guess must be between 1 to 1000.")
        guesses += 1
        user_num = int(input("Please enter your guess: "))

if user_num == 0:
    print("Goodbye!")
else:
    print("That's correct! You win!")
    print(f"You guessed my number in {guesses} guesses.")
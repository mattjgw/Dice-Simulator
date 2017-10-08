import random

userInput = input("Hit enter to roll\n")

if userInput is "":
    roll = random.randrange(1, 6)
    print("You rolled a", roll)


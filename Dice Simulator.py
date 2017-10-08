import random

print("Hit enter to roll")
userInput = input()

if userInput is "":
    roll = random.randrange(1, 6)
    print("You rolled a", roll)


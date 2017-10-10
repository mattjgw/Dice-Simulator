import random

again = True

while again is True:
    roll = input("Hit enter to roll\n")
    if roll == "":
        result = random.randrange(1, 6)
        print("You rolled a", result, "\n")
        answer = input("Do you want to roll again? (Y/N)\n")
        if answer == 'N' or answer == 'n':
            again = False
            print("Goodbye!")
        elif answer == 'Y' or answer == 'y':
            again = True



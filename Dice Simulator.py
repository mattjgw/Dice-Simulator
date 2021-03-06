import random

again = True

while again is True:
    try:
        numberOfDice = int(input("How many dice would you like to roll?\n"))
    except ValueError:
        print("Please enter an integer")
        continue
    roll = input("Hit enter to roll\n")
    result = random.randrange(numberOfDice, 6*numberOfDice)
    print("You rolled a", result, "\n")
    answer = input("Do you want to roll again? (Y/N)\n")
    exit = 0
    while exit == 0:
        if answer == 'N' or answer == 'n':
            again = False
            print("Goodbye!")
            exit = 1
        elif answer == 'Y' or answer == 'y':
            again = True
            exit = 1
        else:
            answer = input("Enter either Y or N")

